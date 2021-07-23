.. include:: /extras.rst.txt
.. highlight:: rst
.. index:: reST; Titles and Headings
.. _rest-titles-headings:

===================
Titles and Headings
===================

|

Titles and headings are reST formats for defining the document structure.

Text is modified with adornments from valid characters to create the document
structural elements Title, Heading and Subheadings.

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. _how-to-titles-headings:

How-to
========

.. tab:: Document Structure

    .. important::

      Following is the list of valid adornment characters

       :sep:`! " # $ % & ' ( ) * + , - . / : ; < = > ? @ [ \ ] ^ _  { | } ~`

      Following is the list of recommended adornment characters

        :sep:`= - ~ ' . *`

      reST does not enforce any particular adornment or order of usage when
      building the document structure.

      The first adornment style encountered will be the top level, and each
      adornment style discovered after that will increment down the structure.

.. tab:: reST syntax

    .. code-block:: rest
        :linenos:

        ==============
        Document Title
        ==============

        Heading 1 Title
        ===============

        Section 1 Title
        ---------------

        Section 2 Title
        ~~~~~~~~~~~~~~~

        Section 3 Title
        '''''''''''''''

        Section 4 Title
        ...............

        Section 5 Title
        ***************



:sep:`See how the document sections look with the recommended adornments below.`

:sep:`The document structure is visible in the index to the right under How-to.`


==============
Document Title
==============

Heading 1 Title
===============

Section 1 Title
---------------

Section 2 Title
~~~~~~~~~~~~~~~

Section 3 Title
'''''''''''''''

Section 4 Title
...............

Section 5 Title
***************

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. _reference-titles-headings:

Reference
=========

|

:sep:`Reference documentation is included in the reST syntax tab in the`
:ref:`How-to section <how-to-titles-headings>`.



+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. _discussion-titles-headings:

Discussion
==========

|

Document titles, headings and sections form the structural elements of the
documents hierarchy tree.

Sphinx reads these structural elements in the building process and constructs,
then renders the Document Tree to the specified format, for example, HTML,
pdf and epub.

The Document Titles are the most common element in the Table of Contents (TOC);
however,  configuring the Document Tree depth using the
:emph:`:maxdepth:` directive in the :emph:`.. toctree::` offers excellent
flexibility for the design.

The TOC is a valuable source of information for a user. Structural elements
combination planning, completed early in the document writing process,
improves user experience and reduces author fatigue.
