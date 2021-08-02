.. include:: /extras.rst.txt


================
Developer Styles
================

|

Git
===

|


Commit Message
--------------

|

The git commit message follows the
`Conventional Commits <https://www.conventionalcommits.org/en/v1.0.0/>`__ style.

|

.. literalinclude:: ../../../.github/.git-commit-template.txt
    :linenos:



|

.. important::
    For Auto-generate CHANGELOG Github Action to pick up the changes,
    the heading must be in the following format.

    tag(subject):<Description>  #nn being the issue number if it exists

    Example: docs(style):Added a new reST style guide #42

    (subject): The CHANGELOG's update groups items with the same subject.

|


CHANGELOG
---------

|

Two Auto-generate CHANGELOG yaml files use
`BobAnkh/auto-generate-changelog <https://github.com/BobAnkh/auto-generate-changelog>`__.


The first, below, updates the CHANGELOG for the :sep:`repo` and includes
additional tags to assist the developers, particularly with WIP.

|

.. literalinclude:: ../../../.github/workflows/update-changelog-WIP.yaml
    :language: yaml
    :linenos:
    :emphasize-lines: 21


.. important::

    Don't forget to change line 21 REPO_NAME if you are using this for your
    Github repo.


|

.. literalinclude:: ../../../.github/workflows/update-changelog-DOCS.yaml
    :language: yaml
    :linenos:
    :emphasize-lines: 22

.. important::

    Don't forget to change line 22 REPO_NAME if you are using this for
    your Github repo.



:sep:`More to come:`
