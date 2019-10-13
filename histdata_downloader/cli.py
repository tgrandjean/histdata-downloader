# -*- coding: utf-8 -*-

"""Console script for histdata_downloader."""
import sys
import logging
import click

from histdata_downloader.logger import log_setup

logger = logging.getLogger(__name__)


@click.command()
@click.option("--verbosity", "-v", default='INFO')
def main(verbosity):
    """Console script for histdata_downloader."""
    log_setup(verbosity, 'activity.log')
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
