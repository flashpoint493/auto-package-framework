# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.2.2] - 2024-12-31

### Features

- **API配置命令**: 新增CLI命令用于配置API密钥，支持持续使用
  - `auto-package config set-ai`: 配置AI API密钥（OpenAI/Anthropic）
  - `auto-package config set-github`: 配置GitHub Token
  - `auto-package config set-pypi`: 配置PyPI Token
  - `auto-package config show`: 查看当前配置
  - `auto-package config clear`: 清除所有配置
  - 配置自动保存到 `~/.auto_package_framework/` 目录，支持持续使用
- **IDE Skill接口**: 新增IDE skill接口，使AI IDE能够识别和使用框架能力
  - `auto-package skill`: 导出skill信息（JSON/Markdown格式）
  - Python API: `from framework import get_skill_interface`
  - 提供完整的能力描述和使用示例
- **配置管理模块**: 新增 `ConfigManager` 类用于管理用户配置的持久化存储
  - 支持JSON配置文件和.env文件
  - 自动加载用户配置目录的配置
  - 与现有配置系统无缝集成

### Improvements

- 改进CLI命令结构，使用命令组（create, config, skill）
- 配置系统支持从用户配置目录自动加载
- 更新README文档，添加新功能使用说明

### Bug Fixes

- 修复 `project_generator.py` 中的合并冲突标记
- 修复 `core.py` 中 `code_generator` 属性未初始化的问题
- 完善 `APICodeGenerator` 实现，正确使用 `AIDeveloper`

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

