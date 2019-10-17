#!/usr/bin/env python
# encoding: utf-8

"""Terminal UI for histdata_downloader project."""
import os
import sys
import logging
import subprocess
from datetime import date
import time

import npyscreen

from histdata_downloader.logger import log_setup
from histdata_downloader.histdata_downloader import load_available_pairs

logger = logging.getLogger(__name__)


class TestApp(npyscreen.NPSAppManaged):

    def onStart(self):
        logger.debug("On start")
        self.registerForm("MAIN", MainForm())

    def onCleanExit(self):
        logger.debug("onCleanExit called")


class MainForm(npyscreen.ActionFormV2):

    def create(self):
        logger.debug("main form method called.")

        self.type = self.add(npyscreen.TitleSelectOne, name='type',
                             max_height=2, values=['M1', 'ticks'],
                             scroll_exit=True)
        self.date_start = self.add(npyscreen.TitleDateCombo, name="Date start")
        self.date_start.value = date(2019, 1, 1)
        self.date_end = self.add(npyscreen.TitleDateCombo, name="Date end")
        self.instruments = self.add(npyscreen.TitleMultiSelect,
                                    name='instruments', max_height=5,
                                    values=load_available_pairs(),
                                    scroll_exit=True)
        self.select_all = self.add(SelectAllButton,
                                   name='select all', relx=20)
        self.unselect_all = self.add(UnselectAllButton,
                                     name='unselect all', relx=20)
        self.output_path = self.add(npyscreen.TitleFilenameCombo,
                                    name="Output path", label=True)
        self.verbosity = self.add(npyscreen.TitleSelectOne, name='verbosity',
                                  max_height=3, values=['DEBUG',
                                                        'INFO',
                                                        'WARNING'],
                                  scroll_exit=True, value=1)
        self.command = self.add(npyscreen.TitleFixedText, name="cmd",
                                editable=False,
                                value='histdata_downloader download')
        self.launch_button = self.add(LauchButton, name='Run', relx=50)
        self.log = self.add(Output, name='Output',
                            editable=True, scroll_exit=True,
                            values=['Waiting...'])

    def while_editing(self, *args):
        verb = self.selected_verbosity[0]
        cmd = "histdata_downloader -v {} download".format(verb)
        if self.type.value:
            cmd += " -t %s " % self.selected_type[0]

        if self.date_end.value:
            cmd += " -ds {} -de {}".format(self.date_start.value,
                                          self.date_end.value)
        if self.output_path.value:
            cmd += " -o {}".format(self.output_path.value)

        if self.instruments.value:
            sub_cmd = ' '.join(['-i %s' % i for i in self.selected_instruments])
            cmd += ' ' + sub_cmd

        self.command.value = cmd
        self.command.update()

    def afterEditing(self):
        self.parentApp.setNextForm(None)

    def return_as_config(self):
        logger.debug('return_as_config method called.')
        config = {'type' : self.type.values[self.type.value[0]],
                  'date_start': self.date_start.value,
                  'date_end': self.date_end.value,
                  'instruments': self.selected_instruments,
                  'output_path': self.output_path.value}
        return config

    @property
    def selected_instruments(self):
        name_field = lambda idx : self.instruments.values[idx]
        return list(map(name_field, self.instruments.value))

    @property
    def selected_type(self):
        name_field = lambda idx : self.type.values[idx]
        return list(map(name_field, self.type.value))

    @property
    def selected_verbosity(self):
        name_field = lambda idx : self.verbosity.values[idx]
        return list(map(name_field, self.verbosity.value))

def perform(cmd, log):
    with subprocess.Popen(cmd, shell=True,
                          stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE) as proc:
        for line in iter(proc.stdout.readline, b''):
            log.values.append(line.decode('ascii'))
            log.display()
        for line in iter(proc.stderr.readline, b''):
            log.values.append(line.decode('ascii'))
            log.display()


class LauchButton(npyscreen.ButtonPress):
    def whenPressed(self):
        self.parent.log.values = ['Executing %s.' % self.parent.command.value]
        self.parent.log.display()
        perform(self.parent.command.value, self.parent.log)

class SelectAllButton(npyscreen.ButtonPress):
    def whenPressed(self):
        instr = self.parent.instruments
        instr.value = [x for x in range(len(instr.values))]
        instr.display()

class UnselectAllButton(npyscreen.ButtonPress):
    def whenPressed(self):
        instr = self.parent.instruments
        instr.value = []
        instr.display


class Output(npyscreen.BoxTitle):
    _contained_widget = npyscreen.MultiLine


if __name__ == "__main__":
    App = TestApp()
    App.run()
