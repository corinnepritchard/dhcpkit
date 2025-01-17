IPv6 Server configuration
=========================

This describes the configuration file for the DHCPKit IPv6 DHCP Server. The syntax of this file is loosely based
on the Apache configuration style. It is implemented using `ZConfig <https://pypi.python.org/pypi/ZConfig>`_.

The configuration file consists of some :ref:`basic server settings <schema_parameters>`, some
:ref:`listeners` that receive messages from the network and some :ref:`handlers` that process the request and
generate the response (possibly surrounded by some :ref:`filters` that determine which handlers get applies to
which request).

.. toctree::

    config_file

Overview of sections
--------------------

.. toctree::
    :maxdepth: 1

    logging

Overview of section types
-------------------------

.. toctree::
    :maxdepth: 2

    duid
    filter_factory
    handler_factory
    listener_factory
    loghandler
