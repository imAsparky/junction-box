.. include:: /extras.rst.txt


====================
**Developer Styles**
====================

|

**Git**
=======

|


**Commit Message**
------------------

|

The git commit message follows the
`Conventional Commits <https://www.conventionalcommits.org/en/v1.0.0/>`__ style.

|

.. code-block:: python
    :linenos:


    # tag(subject):<Description>  #nn being the issue number if it exists
    # (subject): CHANGELOG update groups items with the same subject.
    # |<----   Preferably using up to 50 chars   --->|<--Max of 72 chars-->|
    # Example: docs(style):Added a new reST style guide #42


    # (Optional) Explain why this change is being made
    # |<----   Try To Limit Each Line to a Maximum Of 72 Characters   ---->|
    # Example: There wasnt a reST style guide.


    # (Optional) Provide links or keys to any relevant tickets, articles or other resources
    # Example: closes #42


    # --- COMMIT END ---
    # Tags with ** will be included in the CHANGELOG
    # **   chore    (a chore that needs to be done)
    #      dbg      (changes in debugging code/frameworks; no production code change)
    #      defaults (changes default options)
    # **   doc      (changes to documentation)
    # **   feat     (new feature)
    # **   fix      (bug fix)
    #      hack     (temporary fix to make things move forward; please avoid it)
    #      license  (edits regarding licensing; no production code change)
    # **   perf     (performance improvement)
    # **   refactor (refactoring code)
    # **   style    (formatting, missing semi colons, etc; no code change)
    # **   test     (adding or refactoring tests; no production code change)
    #      version  (version bump/new release; no production code change)
    #      WIP      (Work In Progress; for intermediate commits to keep patches reasonably sized)
    #      jsrXXX   (patches related to the implementation of jsrXXX, where XXX the JSR number)
    #      jdkX     (patches related to supporting jdkX as the host VM, where X the JDK version)
    #
    # --------------------
    # Remember to:
    #   * Capitalize the subject line start
    #   * Use the imperative mood in the subject line
    #   * Do not end the subject line with a period
    #   * Separate subject from body with a blank line
    #   * Use the body to explain what and why vs. how
    #   * Can use multiple lines with "-" or "*" for bullet points in body
    # --------------------


|

.. important::
    For Auto-generate CHANGELOG Github Action to pick up the changes, the heading must be in the following format.

    tag(subject):<Description>  #nn being the issue number if it exists

    Example: docs(style):Added a new reST style guide #42

    (subject): CHANGELOG update groups items with the same subject.

|


**CHANGELOG**
--------------

|

Two Auto-generate CHANGELOG yaml files use
`BobAnkh/auto-generate-changelog <https://github.com/BobAnkh/auto-generate-changelog>`__.


The first, below, updates the CHANGELOG for the :sep:`repo` and includes additional tags to assist the developers, particularly with WIP.

|
.. code-block:: yaml
    :linenos:
    :emphasize-lines: 18

    name: Auto-generate CHANGELOG-WIP
    on:
    release:
        types: [created, edited]
    schedule:
        - cron: "0 23 * * *"
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
            REPO_NAME: "imAsparky/junction-box"
            ACCESS_TOKEN: ${{secrets.GITHUB_TOKEN}}
            PATH: "/CHANGELOG.md"
            COMMIT_MESSAGE: "docs(CHANGELOG): update release notes"
            TYPE: "chore:Chore,feat:Feature,fix:Bug Fixes,docs:Documentation,perf:Performance Improvements,refactor:Refactor,style:Styling,test:Tests"


|

.. important::

    Don't forget to change line 18 if you are using this for your Github repo.


|

The second, below, updates the CHANGELOG for the :sep:`docs` and excludes the additional tags to assist the developers.

.. code-block:: yaml
    :linenos:
    :emphasize-lines: 24

    name: Auto-generate CHANGELOG-DOCS
    on:
    release:
        types: [created, edited]
    schedule:
        - cron: "0 23 * * *"
    push:
        branches:
        - main
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
            REPO_NAME: "imAsparky/junction-box"
            ACCESS_TOKEN: ${{secrets.GITHUB_TOKEN}}
            PATH: "/docs/source/CHANGELOG.md"
            COMMIT_MESSAGE: "docs(CHANGELOG): update release notes:docs"
            TYPE: "feat:Feature,fix:Bug Fixes,docs:Documentation,perf:Performance Improvements,refactor:Refactor,style:Styling,test:Tests"



.. important::

    Don't forget to change line 24 if you are using this for your Github repo.


    More to come:
