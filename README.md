Introduction
============

Project buildout including both development and deployment profiles for the
JMS Plone Site.

Installation
------------

The buildout is self-contained and includes all custom packages and site
specific configuration. To bootstrap a local development environment it is 
recommended to use a Python virtualenv in combination with this buildout to
archieve the best isolation orm portential site packages possible.

    $ /path/to/python/bin/virutalenv jms-venv
    $ cd ./jms-venv
    $ python bootstrap.py -c development.cfg
    $ bin/buildout -c development.cfg

Please note, that the development profile assumes a *nix based OS/environment
and therfore installs 'sauna.reload' which in turn relies on the availability
of 'watchdog' for partial reloads.


Site specific packages
----------------------

the site specific python packages are managed by mr.developer and kept inside
the buildout's './src' directory:

    * meetshaus.sitetheme (Diazo based Plone Theme)
    * meetshaus.sitecontent (Dexterity, five.grok based content types and
        funtionality)
