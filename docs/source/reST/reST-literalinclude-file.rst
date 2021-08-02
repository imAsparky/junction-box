.. include:: /extras.rst.txt
.. highlight:: rst
.. index:: reST; Literal Include
.. _rest-literal-include:

==============
File Inclusion
==============

|

:sep:`..literalincludes::` is a particular Sphinx reST directive.

:sep:`..literalincludes::` purpose is to read and render text files into
the documentation.

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. _how-to-literal-include:


How-to
======


.. tab:: How it Looks

    .. caution::

        `..literalinclude` does not use the System Path to connect to target
        files.  The target files location is relative to the calling file.

        Often the target file is in the same folder as the calling file, as in
        this example, see the reST syntax tab for the code.

        See the Path Examples tab for more information on how to access target
        files in different directories.

    .. literalinclude:: file_tree_literal_include_example_1.txt
        :language: text
        :linenos:
        :emphasize-lines: 1, 24, 27

    .. note::

        Line 1: Example file name.

        Line 24: Location of the `.. literalinclude::` calling the file.

        Line 27: Location of the file being called.

.. tab:: reST syntax

    .. code-block:: rest
        :linenos:

        .. literalinclude:: file_tree_literal_include_example_1.txt
        :language: text
        :linenos:
        :emphasize-lines: 1, 24, 27


.. tab:: Path Example 2

    .. hint::

        This example demonstrates :sep:`..literalinclude <path-to-file>` with
        the target file three folders above.

    .. code-block:: rest
       :linenos:

       .. literalinclude:: ../../../file_tree_literal_include_example_2.txt
        :language: text
        :linenos:
        :emphasize-lines: 1, 4, 24


    .. literalinclude:: ../../../file_tree_literal_include_example_2.txt
        :language: text
        :linenos:
        :emphasize-lines: 1, 4, 24

    .. note::

        Line 1: Example file name.

        Line 4: Location of the file being called.

        Line 24: Location of the `.. literalinclude::` calling the file.

.. tab:: Path Example 3

    .. hint::

        This example demonstrates :sep:`..literalinclude <path-to-file>` with
        the target file up one folder and across two folders.

    .. code-block:: rest
       :linenos:

       .. literalinclude:: ../_static/code_examples/file_tree_literal_include_example_2.txt
        :language: text
        :linenos:
        :emphasize-lines: 1, 16, 24


    .. literalinclude:: ../_static/code_examples/file_tree_literal_include_example_3.txt
        :language: text
        :linenos:
        :emphasize-lines: 1, 16, 24

    .. note::

        Line 1: Example file name.

        Line 4: Location of the file being called.

        Line 24: Location of the `.. literalinclude::` calling the file.

See :ref:`Reference <reference-literal-include>` section below for modifying options.




+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. _reference-literal-include:

Reference
=========

|

:sep:`Examples follow below, in the How it Looks and reST syntax
tabs of using optional classes to change the rendered files appearance.`

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Line Numbers

.. tab:: How it Looks

    .. literalinclude:: ../../../.readthedocs.yaml
        :language: yaml
        :linenos:


.. tab:: reST syntax

    .. code-block:: rest
        :linenos:
        :emphasize-lines: 3

        .. literalinclude:: ../../../.readthedocs.yaml
            :language: yaml
            :linenos:

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Line Highlight

.. tab:: How it Looks

    .. literalinclude:: ../../../.readthedocs.yaml
        :language: yaml
        :linenos:
        :emphasize-lines: 1,2, 10-13


.. tab:: reST syntax

    .. code-block:: rest
        :linenos:
        :emphasize-lines: 4

        .. literalinclude:: ../../../.readthedocs.yaml
            :language: yaml
            :linenos:
            :emphasize-lines: 1,2, 10-13

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Line Selection

.. tab:: How it Looks

    .. literalinclude:: ../../../.readthedocs.yaml
        :language: yaml
        :linenos:
        :lines: 1,2, 10-13

    .. tip::

        Compare this example with the Line Highlight example above.

        As seen in the reST syntax tabs, the same lines have been selected and
        appear here.

        Notice that the line numbers in this example are consecutive and don't
        indicate the source file line numbers.

.. tab:: reST syntax

    .. code-block:: rest
        :linenos:
        :emphasize-lines: 4

        .. literalinclude:: ../../../.readthedocs.yaml
            :language: yaml
            :linenos:
            :lines: 1,2, 10-13

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Code Language

|

.. seealso::

        All examples above have used a single yaml file to display the options.

        Other code language options exist, and here is a Python file
        to demonstrate.

        For other supported coding languages see
        `Pygments Lexers <https://pygments.org/docs/lexers/>`__


.. tab:: How it Looks

    .. literalinclude:: ../_static/code_examples/square_example.py
        :language: python
        :linenos:


.. tab:: reST syntax

    .. code-block:: rest
        :linenos:

        .. literalinclude:: ../_static/code_examples/square_example.py
            :language: python
            :linenos:

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

File Diff

.. tab:: How it Looks

    .. literalinclude:: file_tree_literal_include_example_1.txt
        :language: text
        :linenos:
        :diff: file_tree_literal_include_example_1_old.txt


.. tab:: reST syntax

    .. code-block:: rest
        :linenos:
        :emphasize-lines: 4

        .. literalinclude:: file_tree_literal_include_example_1.txt
        :language: text
        :linenos:
        :diff: file_tree_literal_include_example_1_old.txt

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

File Encoding

.. tab:: How it Looks

    .. literalinclude:: ../../../.readthedocs.yaml
        :language: yaml
        :linenos:
        :encoding: utf-8-sig


    .. note::

        Default file encoding is utf-8-sig.

        Use this class for different target file encodings, e.g. latin-1.

.. tab:: reST syntax

    .. code-block:: rest
        :linenos:
        :emphasize-lines: 4

        .. literalinclude:: ../../../.readthedocs.yaml
            :language: yaml
            :linenos:
            :encoding: utf-8-sig

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


.. _discussion-literal-include:

Discussion
==========

The documentation may include more extended text displays by storing the
example text in an external plain text file.

Literal include is handy for including code files and has several classes
included in the :sep:`.. code-block::` directive.

It is a more lightweight tool than the Autodoc Sphinx extension to keep small
files documentation synchronised with the source file.

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Further Reading
===============

|

For further interesting reading on this topic, see `Spinx Directives
<https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html>`__.
