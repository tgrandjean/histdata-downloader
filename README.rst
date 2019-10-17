===================
Histdata Downloader
===================


.. image:: https://img.shields.io/pypi/v/histdata-downloader.svg
        :target: https://pypi.python.org/pypi/histdata-downloader

.. image:: https://img.shields.io/travis/tgrandjean/histdata-downloader.svg
        :target: https://travis-ci.org/tgrandjean/histdata-downloader

.. image:: https://readthedocs.org/projects/histdata-downloader/badge/?version=latest
        :target: https://histdata-downloader.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status



**Educational purpose project !**

I'm a student and this is a dummy project to learn.

Simple script to download forex historical data from 'www.histdata.com'

usage:: 

    $histdata_downloader tui


.. image:: https://github.com/tgrandjean/histdata-downloader/blob/master/images/1.png
        
.. image:: https://github.com/tgrandjean/histdata-downloader/blob/master/images/2.png


command line usage::

    $histdata_downloader download --help
    Usage: histdata_downloader download [OPTIONS]

    Options:
        -t, --type [M1|ticks]
        -ds, --date-start [%Y-%m-%d]  [required]
        -de, --date-end [%Y-%m-%d]    [required]
        -i, --instruments TEXT        [required]
        -o, --output-path PATH        [required]
        --tqdm
        --help                        Show this message and exit.
    
* Free software: MIT license
* Documentation: https://histdata-downloader.readthedocs.io.


Features
--------

* TODO

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
