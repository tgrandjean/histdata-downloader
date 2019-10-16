#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Click>=6.0',
                'beautifulsoup4',
                'future_fstrings',
                'lxml',
                'pyaml',
                'pandas',
                'requests',
                'tables',
                'tqdm']

setup_requirements = ['pytest-runner', ]

test_requirements = ['pytest', ]

setup(
    author="Thibault Grandjean",
    author_email='thibault.grandjean@protonmail.ch',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    description="Simple script to download forex historical data from 'www.histdata.com'",
    entry_points={
        'console_scripts': [
            'histdata_downloader=histdata_downloader.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='histdata_downloader',
    name='histdata_downloader',
    packages=find_packages(include=['histdata_downloader']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/tgrandjean/histdata-downloader',
    version='0.4.0',
    zip_safe=False,
)
