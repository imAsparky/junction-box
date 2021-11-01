.. include:: /extras.rst.txt
.. highlight:: rst
.. index:: reST; In-Line-Tabs
.. _rest-in-line-tabs:

============
In-Line-Tabs
============

|

Basic
=====

Create a tab with the tab directive. Consecutive tab directives
create a single set of tabs.

|

.. code-block:: rest
   :linenos:

    This is text before the tabs.

    .. tab:: First

        First tab text is interesting.

    .. tab:: Second

        Second tab text is twice as interesting as the first tab.

    .. tab:: Third

        Third  tab is an odd one indeed.

    .. tab:: Fourth

        Fourth is four times better.

    Text directly below the tabs will be visible in all the tabs and
    does not break the document flow.

|

*See the styling above rendered by Sphinx below.*

|

This is text before the tabs.

.. tab:: First

    First tab text is interesting.

.. tab:: Second

    Second tab text is  twice as interesting as the first tab.

.. tab:: Third

    Third  tab is an odd one indeed.

.. tab:: Fourth

    Fourth is four times better.

Text directly below the tabs will be visible in all the tabs and
does not break the document flow.

|

Multiple Tab Sets
=================

|

It is possible to start a new tab within an existing tab by placing content
between sets or providing the  :sep:`:new-set:` option to the tab directive.

|

.. code-block:: rest
   :linenos:

    This is text before the tabs.

    .. tab:: First

        First tab text is interesting.

    .. tab:: Second

        Second tab text is  twice as interesting as the first tab.

    .. tab:: Third

        Third  tab is an odd one indeed.
    .. tab:: Fourth

            Fourth is four times better.
    .. tab:: Fifth
        :new-set:

    Five is a nice number.

    .. tab:: Sixth

        Six is also nice.

|

*See the styling above rendered by Sphinx below.*

|

This is text before the tabs.

.. tab:: First

    First tab text is interesting.

.. tab:: Second

    Second tab text is  twice as interesting as the first tab.

.. tab:: Third

    Third  tab is an odd one indeed.

.. tab:: Fourth

    Fourth is four times better.

.. tab:: Fifth
    :new-set:

    Five is a nice number.

.. tab:: Sixth

    Six is also nice.

|

Code in Tabs
============
|

Code-block's in a tabs' content area will display in the tab contents, making
things very straightforward for programming language snippets and OS-based
command suggestions.

|

.. code-block:: rest

    .. tab:: Python

        .. code-block:: Python
            :linenos:

            print("Hello World!")

        .. code-block:: Python

            print("Another Hello World!")

    .. tab:: Yaml

        .. code-block:: Yaml
            :linenos:

            name: Auto-generate CHANGELOG-WIP
            on:
            # release:
            #   types: [created, edited]
            # # schedule:
            #   - cron: "0 14 * * *"
            # push:
            #   branches:
            #     - main
            workflow_dispatch:

            jobs:
            generate-changelog:
                runs-on: ubuntu-latest
                steps:
                - uses: actions/checkout@v2
                    with:
                    fetch-depth: 0
                - uses: BobAnkh/auto-generate-changelog@master
                    with:
                    REPO_NAME: "your repo/your-project"
                    ACCESS_TOKEN: ${{secrets.GITHUB_TOKEN}}
                    PATH: "/CHANGELOG.md"
                    COMMIT_MESSAGE: "docs(CHANGELOG): update release notes:repo"
                    TYPE: "chore:Chore,feat:Feature,fix:Bug Fixes,docs:Documentation,
                    perf:Performance Improvements,refactor:Refactor,style:Styling,test:Tests, WIP:In Progress"

    .. tab:: C++

        .. code-block:: C++
            :linenos:

            #include <iostream>

            int main() {
            std::cout << "Hello World!" << std::endl;
            }

*See the styling above rendered by Sphinx below.*


.. tab:: Python

    .. code-block:: Python
        :linenos:

        print("Hello World!")

    .. code-block:: Python
        :linenos:

        print("Another Hello World!")

.. tab:: Yaml

    .. code-block:: Yaml
         :linenos:

         name: Auto-generate CHANGELOG-WIP
         on:
         # release:
         #   types: [created, edited]
         # # schedule:
         #   - cron: "0 14 * * *"
         # push:
         #   branches:
         #     - main
         workflow_dispatch:

         jobs:
         generate-changelog:
             runs-on: ubuntu-latest
             steps:
             - uses: actions/checkout@v2
                 with:
                 fetch-depth: 0
             - uses: BobAnkh/auto-generate-changelog@master
                 with:
                 REPO_NAME: "your repo/your-project"
                 ACCESS_TOKEN: ${{secrets.GITHUB_TOKEN}}
                 PATH: "/CHANGELOG.md"
                 COMMIT_MESSAGE: "docs(CHANGELOG): update release notes:repo"
                 TYPE: "chore:Chore,feat:Feature,fix:Bug Fixes,docs:Documentation,
                 perf:Performance Improvements,refactor:Refactor,style:Styling,
                 test:Tests, WIP:In Progress"

.. tab:: C++

    .. code-block:: C++
        :linenos:

        #include <iostream>

        int main() {
        std::cout << "Hello World!" << std::endl;
        }

|

Synchronisation
===============

|

With JavaScript enabled on the end users browser, Tabs across multiple sets
will synchronise unconditionally.

|

.. hint::

    Synchronisation behaviour is unconditional because tabbed content usually
    stays consistent, for example, the Operating System or programming language.

|

.. code-block:: rest

    .. tab:: Unix (MacOS / Linux)

        .. code-block:: console
            :linenos:

            $ python -m pip install sphinx

    .. tab:: Windows

        .. code-block:: console
            :linenos:

            $ py -m pip install sphinx

    .. tab:: Unix (MacOS / Linux)
        :new-set:

        .. code-block:: console
            :linenos:

            $ make html

    .. tab:: Windows

        .. code-block:: console
            :linenos:

            $ make.bat html

|

*See the styling above rendered by Sphinx below.*

|

:emph:`Click on the Windows tab to see Synchronisation in action.`

|

.. tab:: Unix (MacOS / Linux)

    .. code-block:: console
        :linenos:

        $ python -m pip install sphinx

.. tab:: Windows

    .. code-block:: console
        :linenos:

        $ py -m pip install sphinx

.. tab:: Unix (MacOS / Linux)
    :new-set:

    .. code-block:: console
        :linenos:

        $ make html


.. tab:: Windows

    .. code-block:: console
        :linenos:

        $ make.bat html

|

.. hint::

    For good document flow, keep the tab order the same throughout the document.
    As shown above, Unix precedes Windows.

|

Nesting
-------

|

Nested Tabs allow the creation of decision trees using
tabs. Nested tabs are also synchronised.

|

.. code-block:: rest

    .. tab:: Unix (MacOS / Linux)

        .. tab:: Bash

            .. code-block:: Bash
                :linenos:

                bash

        .. tab:: Zsh

            .. code-block:: Zsh
                :linenos:

                zsh

    .. tab:: Windows

        .. tab:: Command Prompt

            .. code-block:: console
                :linenos:

                cmd.exe

        .. tab:: Powershell

            .. code-block:: Powershell
                :linenos:

                ps2.exe

|

*See the styling above rendered by Sphinx below.*

|

.. tab:: Unix (MacOS / Linux)

    .. tab:: Bash

        .. code-block:: Bash
            :linenos:

            bash

    .. tab:: Zsh

        .. code-block:: Zsh
            :linenos:

            zsh

.. tab:: Windows

    .. tab:: Command Prompt

        .. code-block:: console
            :linenos:

            cmd.exe

    .. tab:: Powershell

        .. code-block:: Powershell
            :linenos:

            ps2.exe
