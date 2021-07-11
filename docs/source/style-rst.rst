===========================
**reStructured Text Style**
===========================

There may be a need to modify one of the pre-existing templates or create a new one to improve how the author can convey their message.

For those occasions, here is Junction Box's reST styling guide.

**Text Emphasis**
=================

**Bold and Italic**
-------------------

Sphinx can render text as either bold or italic but not both.

.. code-block:: rest
   :linenos:

   Normal text, **bold text** and *italic text*.

*See the styling above rendered by Sphinx below.*

|

Normal text, **bold text** and *italic text*.


**Line Spaces**
----------------

Line spaces can help emphasise text in some cases.

Text not separated by a blank line will join.

Blank lines in reST don't render as blank lines in the document.

Line spaces will render when using the \| symbol.

.. code-block:: rest
   :linenos:

      Text on line 1
      Text on line 2




      Text on line 4

      |

      Text on line 6

|

*See the styling above rendered by Sphinx below.*

|

Text on line 1
Text on line 2




Text on line 4

|

Text on line 6

.. important::

  See the effect of no line separation between Text on line 1 and Text on Line 2.

  \| symbol is not rendered but provides a clean line space.

.. _document-headings:

**Document Headings**
=====================

In reST, you can use different underlining styles in any order.

For reST (.rst) Title and Heading styles, see below.

.. code-block:: rest
   :linenos:

      ============
      **DocTitle**
      ============

      **Heading 1**
      =============

      **Heading 1.1**
      ---------------

      **Heading 1.1.1**
      ~~~~~~~~~~~~~~~~~

      **Heading 1.1.1.1**
      """""""""""""""""""

|

*See the styling above rendered by Sphinx below.*

============
**DocTitle**
============

**Heading 1**
=============

**Heading 1.1**
---------------

**Heading 1.1.1**
~~~~~~~~~~~~~~~~~

**Heading 1.1.1.1**
"""""""""""""""""""

|

**Links**
=========

**Link to a Heading**
---------------------

Sphinx provides the ability to link to internal document references.

.. code-block:: rest
   :linenos:

   .. _random-heading:

   Random Heading
   ==============

   Some random text to help with some unexpected challenges.





   See here :ref:`random-heading` for information to help with your unexpected challenge.


.. important::

   Sphinx is sensitive to line spaces in this scenario.

   If your link doesn't appear, check for an empty line between the internal link reference and the heading declaration.

*See the styling above rendered by Sphinx below.*


.. _random-heading-link:

**Random Heading**
==================

Some random text to help some unexpected challenge.

|
|
|

**Scroll down so  "Random Heading" is off the screen, and click the hyperlink to see the internal linking in action.**

|
|
|
|

See here :ref:`random-heading-link` for information to help with your unexpected challenge.

|
|

.. important::

   The \:ref:\`random heading-link\` text is surrounded by backticks,
   not single apostrophe's!
