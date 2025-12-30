# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.2.0] - 2024-12-XX

### Features

- **Built-in project template**: Template is now included in the package, no external dependency needed
- **Cursor Skill support**: Add Cursor Skill implementation for AI-driven package automation
  - SKILL.md definition file
  - Executable scripts for package creation
  - Workflow guide and reference documentation
- **Improved template path detection**: Automatic detection of built-in templates with fallback support

### Bug Fixes

- Fix CI workflow: Adjust ruff/mypy paths and add continue-on-error
- Fix Release workflow: Replace deprecated actions/create-release with softprops/action-gh-release
- Fix template path resolution: Support built-in templates and custom template paths

### Documentation

- Add CURSOR_SKILL_PROPOSAL.md with implementation discussion
- Update README with built-in template information
- Add workflow guide for Cursor Skill

## [0.1.0] - 2024-XX-XX

### Features

- Initial release
- Project generation from template
- GitHub integration
- PyPI publishing
- AI code generation support
- Command-line interface

