.. include:: /extras.rst.txt
.. highlight:: rst
.. index:: reST; Introduction
.. _intro-rest-sphinx:

===============================
Introduction to reST and Sphinx
===============================

reStructuredText, commonly referred to as reST, is an easy-to-read plaintext
markup syntax and parser system.

It is excellent for inline program documentation (such as Python docstrings),
quickly creating simple web pages and standalone documents using Sphinx.


.. ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. index:: reST; Paragraphs

Paragraphs
==========

Paragraphs are text separated by one or more blank lines.

.. code-block:: rest
   :linenos:

   This is some text in a paragraph.
   This is some more text in the same paragraph.
   Here is more text that is written in the first paragraph.

   This is some text in a New paragraph.


:emph:`See Paragraph styling above rendered by Sphinx below.`


This is some text in a paragraph.
This is some more text in the same paragraph.
Here is more text that is written in the first paragraph.

This is some text in a New paragraph.


.. note::

    The next code block took from the following example of using text in a paragraph
    from `here <https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html>`__.


.. code-block:: rest
    :linenos:

    Paragraphs contain text and may contain inline markup:
    *emphasis*, **strong emphasis**, `interpreted text`, ``inline
    literals``, standalone hyperlinks (http://www.python.org),
    external hyperlinks (Python_), internal cross-references
    (example_), footnote references ([1]_), citation references
    ([CIT2002]_), substitution references (|example|),
    and _`inline internal targets`.

    Paragraphs are separated by blank lines and are left-aligned.

:emph:`See Paragraph styling above rendered by Sphinx below.`

Paragraphs contain text and may contain inline markup:
*emphasis*, **strong emphasis**,
standalone hyperlinks (http://www.python.org),
external hyperlinks (Python_), internal cross-references
(example_), footnote references ([1]_), citation references
([CIT2002]_), substitution references (|example|),
and _`inline internal targets`.

Paragraphs are separated by blank lines and are left-aligned.


.. index:: reST; Indentation

Indentation
===========

All indentation is significant; the level of indentation must be consistent.
For example, indentation is the sole markup indicator for block quotes.


.. note::

    This example of using text in a paragraph was taken from
    `here <https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#indentation>`__

.. code-block:: rest
    :linenos:

    This is a top-level paragraph.

     This paragraph belongs to a first-level blockquote.

      This paragraph belongs to a second-level blockquote.

    This is another top-level paragraph.

      This paragraph belongs to a second-level block quote.

    This paragraph belongs to a first-level block quote.  The
    second-level block quote above is inside this first-level
    block quote.



:emph:`See Indentation styling above rendered by Sphinx below.`

This is a top-level paragraph.

 This paragraph belongs to a first-level blockquote.

  This paragraph belongs to a second-level blockquote.

This is another top-level paragraph.

  This paragraph belongs to a second-level block quote.

This paragraph belongs to a first-level block quote.  The
second-level block quote above is inside this first-level
block quote



Further Reading
===============

For further interesting reading on this topic, see
:ref:`reST How-to Index <rest-index>`
