#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `histdata_downloader` package."""

import pytest

from click.testing import CliRunner

from histdata_downloader import histdata_downloader
from histdata_downloader import cli


def test_date_formatter():
    """test the date formater used to convert raw date in well structured
    datetime."""
    raw_date = '20190101'
    raw_time = '20000000'
    expected = '2019-01-01 00:00:00.0'
    assert histdata_downloader.date_formatter(raw_date+raw_time) == expected


@pytest.fixture()
def runner():
    return CliRunner()


class TestCommandLineInterface():
    """Test suite for command line interface."""

    def test_main_call(self, runner):
        """Test the call of the cli without command."""
        res = runner.invoke(cli.main)
        assert res.exit_code == 0

    def test_main_help(self, runner):
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert 'Show this message and exit.' in help_result.output


@pytest.fixture()
def dataset():
    return histdata_downloader.DataSet('EURUSD', 2018, 1)


class TestDataSet():
    """Test suite for dataset object."""

    def test_url_property(self, dataset):
        assert dataset.url == dataset.ohlc_url + '/EURUSD/2018/1'

    def test_str_method(self, dataset):
        assert dataset.__str__() == 'EURUSD/y2018/m1'

    def test_type_property(self, dataset):
        assert dataset.type == 'M1'
        dataset.type = 'ticks'
        assert dataset.type == 'ticks'
        with pytest.raises(ValueError):
            dataset.type = ''
