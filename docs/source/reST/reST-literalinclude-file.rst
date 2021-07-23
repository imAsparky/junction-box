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

    .. literalinclude:: /_static/code-examples/.readthedocs-example.yaml
        :language: yaml

    .. seealso::

        The example displayed above has no modifier options.

        See :ref:`Reference <reference-literal-include>` section below
        for modifying options.

.. tab:: reST syntax

    .. code-block:: rest
       :linenos:

       .. literalinclude:: /_static/code-examples/.readthedocs-example.yaml

    .. tip::

        Usually, the file name is relative to the current file's path.

        However, it can be relative to the top source directory if it is
        absolute, i.e. starting with /, as shown in the example above.

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

    .. literalinclude:: /_static/code-examples/.readthedocs-example.yaml
        :language: yaml
        :linenos:


.. tab:: reST syntax

    .. code-block:: rest
        :linenos:

        .. literalinclude:: /_static/code-examples/.readthedocs-example.yaml
            :language: yaml
            :linenos:

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Line Highlight

.. tab:: How it Looks

    .. literalinclude:: /_static/code-examples/.readthedocs-example.yaml
        :language: yaml
        :linenos:
        :emphasize-lines: 1,2, 10-13


.. tab:: reST syntax

    .. code-block:: rest
        :linenos:

        .. literalinclude:: /_static/code-examples/.readthedocs-example.yaml
            :language: yaml
            :linenos:
            :emphasize-lines: 1,2, 10-13

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Line Selection

.. tab:: How it Looks

    .. literalinclude:: /_static/code-examples/.readthedocs-example.yaml
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

        .. literalinclude:: /_static/code-examples/.readthedocs-example.yaml
            :language: yaml
            :linenos:
            :lines: 1,2, 10-13

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

File Encoding

.. tab:: How it Looks

    .. literalinclude:: /_static/code-examples/.readthedocs-example.yaml
        :language: yaml
        :linenos:
        :encoding: utf-8-sig

    .. note::

        Default file encoding is utf-8-sig.

        Use this class for different file encodings, e.g. latin-1.

.. tab:: reST syntax

    .. code-block:: rest
        :linenos:

        .. literalinclude:: /_static/code-examples/.readthedocs-example.yaml
            :language: yaml
            :linenos:
            :encoding: utf-8-sig

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Code Language

.. tab:: How it Looks

    .. literalinclude:: /_static/code-examples/square-example.py
        :language: python
        :linenos:

    .. note::

        All examples above have used a single yaml file to display the options.

        Other code language options exist, and here is a Python file
        to demonstrate.

        For other supported coding languages see
        `Pygments Lexers <https://pygments.org/docs/lexers/>`__


.. tab:: reST syntax

    .. code-block:: rest
        :linenos:

        .. literalinclude:: /_static/code-examples/square-example.py
            :language: python
            :linenos:

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
