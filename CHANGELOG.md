# CHANGELOG

## Unreleased

Changes unreleased.

### Feature

- sphinx:
  - Theme is now sphinx_rtd_theme ([97174c7](https://github.com/imAsparky/junction-box/commit/97174c733cda618f11e6c0c875c13421e07008b4)) ([#29](https://github.com/imAsparky/junction-box/pull/29))
  - Theme is now  t3SphinxThemeRtd #12 ([86f3afb](https://github.com/imAsparky/junction-box/commit/86f3afbbb57082b0cf167fd3f7ecba8c77b03057)) ([#27](https://github.com/imAsparky/junction-box/pull/27))

### Bug Fixes

- yaml:
  - Cron job not formatted correctly ([a64530e](https://github.com/imAsparky/junction-box/commit/a64530eb6bbba6f293b3ba8a210211e68db97d9f)) ([#34](https://github.com/imAsparky/junction-box/pull/34))

### Documentation

- log:
  - Add additional tags to update-changelog.yaml# ([dce6027](https://github.com/imAsparky/junction-box/commit/dce60279223d53983c3f365583954e1fe042da7a)) ([#45](https://github.com/imAsparky/junction-box/pull/45))

- README:
  - Added logo to the git README #37 ([7be1e99](https://github.com/imAsparky/junction-box/commit/7be1e99e661850f2895c1522a0acd5c248046c12)) ([#39](https://github.com/imAsparky/junction-box/pull/39))

- images:
  - Add .png and .svg logo's #37 ([1c7abc3](https://github.com/imAsparky/junction-box/commit/1c7abc39c1c225d34e6ff2f04e0ca4b2f5589a36)) ([#38](https://github.com/imAsparky/junction-box/pull/38))

- style:
  - Add Development Pipeline style #35 ([c9847bb](https://github.com/imAsparky/junction-box/commit/c9847bbe7777ee429c9231e75b329464f0d1ec72)) ([#36](https://github.com/imAsparky/junction-box/pull/36))
  - Added reST style guide. TOC update #23 ([78aad68](https://github.com/imAsparky/junction-box/commit/78aad68cc078dac547e7932f3238a22daba0ed1a)) ([#32](https://github.com/imAsparky/junction-box/pull/32))

- about:
  - Change to match reST style guide. ([230dd44](https://github.com/imAsparky/junction-box/commit/230dd44246be82f710e0c686f461243030d91c96)) ([#31](https://github.com/imAsparky/junction-box/pull/31))
  - Improve wording in the Why section ([ec5c76e](https://github.com/imAsparky/junction-box/commit/ec5c76e0ce1329aa39d2df4b541e6a3e5b50a59c)) ([#26](https://github.com/imAsparky/junction-box/pull/26))

- Style:
  - Add intro Style Guide, Update Index ([2df9ad0](https://github.com/imAsparky/junction-box/commit/2df9ad09c3fd1b69871b83de9bc72a34191f1cb5)) ([#30](https://github.com/imAsparky/junction-box/pull/30))

## [v0.0.1-alpha-1](https://github.com/imAsparky/junction-box/releases/tag/v0.0.1-alpha-1) - 2021-07-08 07:35:04

Sphinx and the Furo theme have been installed with basic configurations.
A basic about page was written and deployed to readthedocs.
Snyk was deployed to monitor this project.

### Feature

- sphinx:
  - Added custom theme furo #12 ([e3f351b](https://github.com/imAsparky/junction-box/commit/e3f351bf6ef2e03c496418ee07ae199c5869d4b3)) ([#20](https://github.com/imAsparky/junction-box/pull/20))
  - Update requirements.txt ([7403cd7](https://github.com/imAsparky/junction-box/commit/7403cd7b3f5ec5fc2177fa2cecad26233ae3b9a4)) ([#16](https://github.com/imAsparky/junction-box/pull/16))
  - Install with base config ([75a8fb5](https://github.com/imAsparky/junction-box/commit/75a8fb5fddb6fc44660f2ab3ff0710235bfbd0bd)) ([#15](https://github.com/imAsparky/junction-box/pull/15))

### Bug Fixes

- sphinx:
  - readthedocs build failed (pkg-resources==0.0.0) #18 ([581a99d](https://github.com/imAsparky/junction-box/commit/581a99d8e3b3f48b6f432b71efbc8c47a6f3584d)) ([#19](https://github.com/imAsparky/junction-box/pull/19))

### Documentation

- README:
  - Add a link to the readthedocs docs ([2f4159d](https://github.com/imAsparky/junction-box/commit/2f4159df777f7293cca2f4de5df6360c6712f8b5)) ([#22](https://github.com/imAsparky/junction-box/pull/22))

- about:
  - Add an about page, update index ([09c9cc1](https://github.com/imAsparky/junction-box/commit/09c9cc1730cb8c79e3f17a5430a9ed972ac0509f)) ([#21](https://github.com/imAsparky/junction-box/pull/21))

## [v0.0.1-alpha](https://github.com/imAsparky/junction-box/releases/tag/v0.0.1-alpha) - 2021-07-07 08:23:31

Basic git workflow setup.

### Chore

- venv:
  - Added requirements.txt ([4eef7b4](https://github.com/imAsparky/junction-box/commit/4eef7b437f161d21d16b0295b830f12bd1dc8d1d)) ([#9](https://github.com/imAsparky/junction-box/pull/9))

### Feature

- pre-commit:
  - Add tox.ini ([6db58b0](https://github.com/imAsparky/junction-box/commit/6db58b0562d93c499b116bfe1d75d9b1f681d9fe)) ([#10](https://github.com/imAsparky/junction-box/pull/10))
  - Add pyproject.toml file ([cce2a1c](https://github.com/imAsparky/junction-box/commit/cce2a1c02ddb67bca46df2f9ff97ca297ba791dc)) ([#10](https://github.com/imAsparky/junction-box/pull/10))
  - Add yaml config file ([8cc0799](https://github.com/imAsparky/junction-box/commit/8cc079977f16cb3bdae1078fbf2834dc88954ce2)) ([#10](https://github.com/imAsparky/junction-box/pull/10))

- #6:
  - Add chore to CHANGELOG choices
https://www.conventionalcommits.org/en/v1.0.0/ allows other choices for commit.
Chore was added because it was missing in our choices.
This change adds additional flexibility for categorizing commit messages.
issue (#6) ([4ae4a80](https://github.com/imAsparky/junction-box/commit/4ae4a809993c7d4a3fc4aa7c6d0adaaf80814ccb)) ([#9](https://github.com/imAsparky/junction-box/pull/9))
  - Delete CHANGELOG template
The template is no longer required for this feature upgrade.
issue #6 ([35f489c](https://github.com/imAsparky/junction-box/commit/35f489ca1cb97687cac4a7bae1ac0ad6152ef1ac)) ([#7](https://github.com/imAsparky/junction-box/pull/7))
  - Update CHANGELOG  yaml
Rewrite update-changelog.yaml and point it to https://github.com/BobAnkh/auto-generate-changelog
issue #6 ([b9920f1](https://github.com/imAsparky/junction-box/commit/b9920f128348c2004abf74dae595ba97f43a421c)) ([#7](https://github.com/imAsparky/junction-box/pull/7))

\* *This CHANGELOG was automatically generated by [auto-generate-changelog](https://github.com/BobAnkh/auto-generate-changelog)*
