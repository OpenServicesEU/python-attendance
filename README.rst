========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis| |requires|
        | |codecov|

.. |docs| image:: https://readthedocs.org/projects/python-attendance/badge/?style=flat
    :target: https://readthedocs.org/projects/python-attendance
    :alt: Documentation Status

.. |travis| image:: https://travis-ci.org/fladi/python-attendance.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/fladi/python-attendance

.. |requires| image:: https://requires.io/github/fladi/python-attendance/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/fladi/python-attendance/requirements/?branch=master

.. |codecov| image:: https://codecov.io/github/fladi/python-attendance/coverage.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/fladi/python-attendance

.. end-badges

Records attendance for students through RFID cards (Backend).

* Free software: BSD license

Documentation
=============

https://python-attendance.readthedocs.io/

Development
===========

To run the all tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
