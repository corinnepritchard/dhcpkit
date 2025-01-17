.. _marked-with:

Marked-with
===========

Filter incoming messages based on the mark set by i.e. the listener.


Example
-------

.. code-block:: dhcpkitconf

    <marked-with bla>
        <ignore-request/>
    </marked-with>

Possible sub-section types
--------------------------

:ref:`Filters <filters>`
    Configuration sections that specify filters. A filter limits which handlers get applied to which messages.
    Everything inside a filter gets ignored if the filter condition doesn't match. That way you can configure
    the server to only apply certain handlers to certain messages, for example to return different information
    options to different clients.

:ref:`Handlers <handlers>`
    Configuration sections that specify a handler. Handlers are the things that process requests, build the
    response etc. Some of them add information options to the response, others look up the client in a CSV file
    and assign addresses and prefixes, and others can abort the processing and tell the server not to answer
    at all.

    You can make the server do whatever you want by configuring the appropriate handlers.

