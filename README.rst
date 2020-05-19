dj-bootstrap-components
=======================

.. image:: https://api.travis-ci.com/IshanManchanda/dj-bootstrap-components.svg?branch=master
  :target: https://travis-ci.com/IshanManchanda/dj-bootstrap-components

.. image:: https://readthedocs.org/projects/dj-bootstrap-components/badge/?version=latest
  :target: https://dj-bootstrap-components.readthedocs.io/en/latest/?badge=latest

.. image:: https://badge.fury.io/py/dj-bootstrap-components.svg
  :target: https://badge.fury.io/py/dj-bootstrap-components

.. image:: https://img.shields.io/pypi/dm/dj-bootstrap-components

Django Bootstrap components
Supported Python versions: 3.7+
Supported Django versions: 3.0.0+

Quick start
-----------

Documentation: https://dj-bootstrap-components.rtfd.io/

1. Install "dj-bootstrap-components". The recommended and only officially
supported way is using pip::

    pip install dj-bootstrap-components


2. Add "bootstrap_components" to your INSTALLED_APPS setting::

    INSTALLED_APPS = [
        ...
        'bootstrap_components',
    ]


3. Add the following to your base template or to each template that will use the
components::

    <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk" crossorigin="anonymous">
    <script src="https://code.jquery.com/jquery-3.5.1.min.js" integrity="sha256-9/aliU8dGd2tb6OSsuzixeV4y/faTqgFtohetphbbj0=" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/js/bootstrap.min.js" integrity="sha384-OgVRvuATP1z7JjHLkuOU7Xw704+h835Lr+6QL9UvYjZE3Ipu6Tp75j7Bh/kR0JKI" crossorigin="anonymous"></script>


Note that you can use any other CDN or self-host the files if you like.

4. Within a template, simply include the needed component and pass it the required context::

    {% include 'bootstrap_components/alert.html' with content='<b> bold </b> sample text' color='primary' %}

