.. include:: /extras.rst.txt
.. highlight:: rst
.. index:: reST; Admonitions
.. _rest-admonitions:

===================
Admonition Messages
===================

|

Admonitions are a particular group of reST directives.

Admonitions purpose is to highlight a message to the user with colour
and formatting.

|

.. _how-to-admonitions:

How-to
========

The code block below demonstrates the syntax for one of the available
admonition styles and is the "note" directive.

|

.. tab:: Desireable syntax spacing

    .. code-block:: rest
        :linenos:
        :emphasize-lines: 8

        .. note:: Text in the title bar or
            on the first row will be displayed
            in the message body, with one exception.  The general purpose
            :sep:`.. admonition::` includes text in the Title bar as a title.

            See :ref:`Admonition <reference-admonition>` for details.

            Here is the note admonition...

    Pay attention to the spacing of the highlighted message block line.

    As you can see below, this renders correctly.

    .. note:: Text in the title bar or
          on the first row will be displayed
          in the message body, with one exception.  The general purpose
          :sep:`.. admonition::` includes text in the Title bar as a title.

          See :ref:`Admonition <reference-admonition>` for details.

          Here is the note admonition...

.. tab:: Undesirable syntax spacing

     .. code-block:: rest
        :linenos:
        :emphasize-lines: 8, 10

        .. note:: Text in the title bar or
            on the first row will be displayed
            in the message body, with one exception.  The general purpose
            :sep:`.. admonition::` includes text in the Title bar as a title.

            See :ref:`Admonition <reference-admonition>` for details.

                Here is the note admonition...

         Here is the note admonition...

    Here the spacing of the highlighted message block lines doesn't produce the
    desired layout for this example.

    As you can see below, this does not render correctly.

    .. note:: Text in the title bar or
            on the first row will be displayed
            in the message body, with one exception.  The general purpose
            :sep:`.. admonition::` includes text in the Title bar as a title.

            See :ref:`Admonition <reference-admonition>` for details.

                Here is the note admonition...

         Here is the note admonition...

|

.. _reference-admonitions:

Reference
=========

|

:sep:`Many other examples follow below, in the How it Looks and reST syntax
tabs.`

|

.. index:: reST directives; admonition
.. _reference-admonition:

Admonition
---------

|

.. tab:: How it Looks

    .. admonition:: A generic, Titled admonition

       This is some random text on the topic.

.. tab:: reST syntax

    .. code-block:: rest
        :linenos:

        .. admonition:: A generic, Titled admonition

           This is some random text on the topic.

|

.. warning:: :sep:`Admonition directive Title is required!`

    The syntax must look like this :sep:`.. admonition:: Some User Title.`
    or this particular style may not render correctly.

|

.. index:: reST directives; seealso

See also
--------

|

.. tab:: How it Looks

    .. seealso::

       Admonitions in `docutils <http://docutils.sourceforge.net/0.7/docs/ref/rst/directives.html#admonitions>`__.

.. tab:: reST syntax

    .. code-block:: rest
        :linenos:

         .. seealso::

            Admonitions in `docutils <http://docutils.sourceforge.net/0.7/docs/ref/rst/directives.html#admonitions>`__.

|

.. index:: reST directives; note

Note
----

|

.. tab:: How it Looks

    .. note::

        Here is a short note.

.. tab:: reST syntax

    .. code-block:: rest
        :linenos:

        .. note::

            Here is a short note.

|

.. index:: reST directives; tip

Tip
---

.. tab:: How it Looks

    .. tip::

        A tip is an idea that can help.

.. tab:: reST syntax

    .. code-block:: rest
        :linenos:

        .. tip::

           A tip is an idea that can help.

|

.. index:: reST directives; hint

Hint
----

|

.. tab:: How it Looks

    .. hint::

       A hint is an indirect suggestion or advice.

.. tab:: reST syntax

    .. code-block:: rest
        :linenos:

        .. hint::

          A hint is an indirect suggestion or advice.

|

.. index:: reST directives; important

Important
---------

|

.. tab:: How it Looks

    .. important::

       Important information that should be considered.

.. tab:: reST syntax

    .. code-block:: rest
        :linenos:

        .. important::

          Important information that should be considered.

|

.. index:: reST directives; caution


Caution
-------

|

.. tab:: How it Looks

    .. caution::

       Caution dragons may live here.

.. tab:: reST syntax

    .. code-block:: rest
        :linenos:

        .. caution::

          Caution dragons may live here.


|

.. index:: reST directives; warning

Warning
-------

|

.. tab:: How it Looks

    .. warning::

       Warning dragons probably live here.

.. tab:: reST syntax

    .. code-block:: rest
        :linenos:

        .. warning::

          Warning dragons probably live here.

|

.. index:: reST directives; danger

Danger
------

|

.. tab:: How it Looks

    .. danger::

       Danger dragons do live here.

.. tab:: reST syntax

    .. code-block:: rest
        :linenos:

        .. danger::

          Danger dragons do live here.

|

.. index:: reST directives; attention

Attention
---------

|

.. tab:: How it Looks

    .. attention::

       Look out the dragon has seen you!

.. tab:: reST syntax

    .. code-block:: rest
        :linenos:

        .. attention::

          Look out the dragon has seen you!

|

.. index:: reST directives; error

Error
-----


.. tab:: How it Looks

    .. error::

        Ooops to late you didnt heed all the messages about dragons...

.. tab:: reST syntax

    .. code-block:: rest
        :linenos:

        .. error::

            Ooops to late you didnt heed all the messages about dragons...

|

.. _discussion-admonitions:

Discussion
==========

|

Please consider the display order of admonitions in the
:ref:`Reference <reference-admonitions>` section and the accompanying messages
in each.

You may notice a hierarchy of colour and message urgency as you scroll down
the page.

This hierarchy is a good guide for using the admonitions in your documentation
and serves as a reference to maintain consistency in admonitions usage.

|
There are a few different ways to write admonitions. Depending on the length and style of the message, each has its merits.

For example, this works, but it looks messy in the text file.

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


.. code-block:: rest
    :linenos:

    .. note:: Here is a line of
        text that doesn't produce anything of interest; it just looks messy and challenging to follow in the text file where it's written.  The line width is too wide for the text editor,
        and you need to scroll to get the message

|

.. note:: Here is a line of
    text that doesn't produce anything of interest; it just looks messy and challenging to follow in the text file where it's written.  The line width is too wide for the text editor,
    and you need to scroll to get the message

|

Here are two alternative ways to layout the same :sep:`.. note::` and text that
improves the source text files readability and produce the same output as the
first example.

|

.. code-block:: rest
    :linenos:

    .. note::
            Here is a line of text that doesn't produce anything of interest;
            it just looks messy and challenging to follow in the text file where
            it's written.  The line width is too wide for the text editor,
            and you need to scroll to get the message

.. code-block:: rest
    :linenos:

    .. note::

            Here is a line of text that doesn't produce anything of interest;
            it just looks messy and challenging to follow in the text file where
            it's written.  The line width is too wide for the text editor,
            and you need to scroll to get the message

|

Here are two short message options for a readable layout in the text editor.
Both produce the same results.

|

.. code-block:: rest
    :linenos:

    .. note:: Here is a short message.

    .. note::

        Here is a short message.


.. note:: Here is a short message.

|

Admonition messages give you the flexibility to combine many different reST
options to provide a rich statement.

See below for some demonstrated common options.

.. code-block:: rest
    :linenos:

    .. note::

        Here is a short message with **bold** text.

        Here is a short message *with some italic text.*

            Here is some short text with an indentation!

        Here is a link to :ref:`Reference <reference-admonitions>`.

        Here is a link to `Google <https://google.com>`__.

|

.. note::

        Here is a short message with **bold** text.

        Here is a short message *with some italic text.*

            Here is some short text with an indentation!

        Here is a link to :ref:`Reference <reference-admonitions>`.

        Here is a link to `Google <https://google.com>`__.


|

Further Reading
===============

|

For further interesting reading on this topic, see `reStructuredText directives in docutils documentation
<http://docutils.sourceforge.net/docs/ref/rst/directives.html#specific-admonitions>`__.
