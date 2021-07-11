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
        # |<----   Preferably using up to 50 chars   --->|<--Max of 72 chars-->|
        # Example: docs(style):Added a new reST style guide #42


        # (Optional) Explain why this change is being made
        # |<----   Try To Limit Each Line to a Maximum Of 72 Characters   ---->|
        # Example: There wasnt a reST style guide


        # (Optional) Provide links or keys to any relevant tickets, articles or other resources
        # Example: closes #42


        # --- COMMIT END ---
        # Tag can be
        #    feat     (new feature)
        #    fix      (bug fix)
        #    refactor (refactoring code)
        #    style    (formatting, missing semi colons, etc; no code change)
        #    doc      (changes to documentation)
        #    test     (adding or refactoring tests; no production code change)
        #    version  (version bump/new release; no production code change)
        #    jsrXXX   (Patches related to the implementation of jsrXXX, where XXX the JSR number)
        #    jdkX     (Patches related to supporting jdkX as the host VM, where X the JDK version)
        #    dbg      (Changes in debugging code/frameworks; no production code change)
        #    license  (Edits regarding licensing; no production code change)
        #    hack     (Temporary fix to make things move forward; please avoid it)
        #    WIP      (Work In Progress; for intermediate commits to keep patches reasonably sized)
        #    defaults (changes default options)
        #
        # Note: Multiple tags can be combined, e.g. [fix][jsr292] Fix issue X with methodhandles
        # --------------------
        # Remember to:
        #   * Capitalize the subject line
        #   * Use the imperative mood in the subject line
        #   * Do not end the subject line with a period
        #   * Separate subject from body with a blank line
        #   * Use the body to explain what and why vs. how
        #   * Can use multiple lines with "-" or "*" for bullet points in body
        # --------------------


|

.. important::
    For Auto-generate CHANGELOG Github Action to pick up the changes, the heading must be in the format.

    tag(subject):<Description>  #nn being the issue number if it exists

    Example: docs(style):Added a new reST style guide #42

|


**CHANGELOG**
--------------

|

Auto-generate CHANGELOG uses
`BobAnkh/auto-generate-changelog <https://github.com/BobAnkh/auto-generate-changelog>`__.

|

.. code-block:: yaml
    :linenos:

    name: Auto-generate CHANGELOG
    on:
    release:
        types: [created, edited]
        schedule:
        - cron: "0 2 * * *"
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
            TYPE: "feat:Feature,fix:Bug Fixes,docs:Documentation,refactor:Refactor,perf:Performance Improvements,test:Tests, chore:Chore"


|

.. important::

    Don't forget to change line 18 if you are using this for your Github repo.


|


More to come:
