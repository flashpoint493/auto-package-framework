# 项目结构说明

本文档说明 `auto-package-framework` 的完整项目结构。

## 📁 目录结构

```
auto_package_framework/
├── src/                          # 源代码目录
│   └── framework/                # 框架核心代码
│       ├── __init__.py
│       ├── config.py             # 配置管理
│       ├── core.py                # 核心工作流引擎
│       ├── project_generator.py   # 项目生成器
│       ├── github_client.py      # GitHub 客户端
│       ├── pypi_client.py         # PyPI 客户端
│       ├── ai_developer.py       # AI 代码生成器
│       ├── cli.py                 # 命令行接口
│       └── templates/             # 内置项目模板
│           ├── __init__.py
│           ├── *.md              # 模板文档文件
│           ├── pyproject.toml    # 模板配置
│           └── .github/           # GitHub 工作流模板
│
├── tests/                         # 测试文件
│   ├── __init__.py
│   ├── test_config.py
│   └── test_project_generator.py
│
├── scripts/                       # 工具脚本
│   ├── publish_pypi.ps1          # Windows PyPI 发布脚本
│   ├── publish_pypi.sh           # Linux/Mac PyPI 发布脚本
│   └── self_publish.py            # 框架自身发布脚本
│
├── cursor_skill/                  # Cursor Skill 实现
│   ├── SKILL.md                   # Skill 定义文件
│   ├── README.md                  # Skill 使用说明
│   ├── scripts/
│   │   └── create_package.py     # Skill 执行脚本
│   └── references/
│       └── workflow_guide.md     # 工作流程参考
│
├── docs/                          # 文档目录（建议）
│   ├── guides/                    # 指南文档
│   │   ├── QUICK_START.md
│   │   ├── PUBLISH_GUIDE.md
│   │   └── GITHUB_SECRET_SETUP.md
│   ├── troubleshooting/           # 故障排查
│   │   ├── CHECK_PYPI_RELEASE.md
│   │   └── BADGES_SETUP.md
│   └── development/               # 开发文档
│       ├── CURSOR_SKILL_PROPOSAL.md
│       ├── EXTERNAL_TOOLS.md
│       └── MINIMAL_PROTOTYPE.md
│
├── .github/                       # GitHub 配置
│   └── workflows/
│       ├── ci.yml                 # CI 工作流
│       └── release.yml            # 发布工作流
│
├── pyproject.toml                 # 项目配置
├── MANIFEST.in                    # 包文件清单
├── release-please-config.json     # Release Please 配置
├── config.yaml.example            # 配置示例
├── CHANGELOG.md                   # 更新日志
├── README.md                      # 主文档
└── SUMMARY.md                     # 项目总结
```

## 📂 目录说明

### `src/framework/` - 核心代码

框架的核心实现，包含所有主要功能模块。

- **config.py**: 配置管理，支持 YAML 文件和环境变量
- **core.py**: 核心工作流引擎，协调各个组件
- **project_generator.py**: 从模板生成项目结构
- **github_client.py**: GitHub API 集成
- **pypi_client.py**: PyPI 发布集成
- **ai_developer.py**: AI 代码生成（支持 OpenAI 和 Anthropic）
- **cli.py**: 命令行接口
- **templates/**: 内置项目模板（已内置到包中）

### `scripts/` - 工具脚本

开发和维护工具脚本。

- **publish_pypi.ps1/sh**: 手动发布到 PyPI 的脚本
- **self_publish.py**: 框架自身发布脚本（用于发布框架本身）

### `cursor_skill/` - Cursor Skill

Cursor IDE 的 Skill 实现，让 Cursor AI 能够使用框架。

- **SKILL.md**: Skill 定义文件（Cursor AI 会读取）
- **scripts/create_package.py**: Skill 执行脚本（直接调用框架）
- **references/**: 参考文档，帮助 AI 理解工作流程

### `docs/` - 文档（建议结构）

建议将文档分类整理到此目录。

- **guides/**: 使用指南
- **troubleshooting/**: 故障排查
- **development/**: 开发文档

### 根目录文件

- **pyproject.toml**: Python 项目配置（版本、依赖等）
- **MANIFEST.in**: 指定包含在包中的文件
- **config.yaml.example**: 配置文件示例
- **README.md**: 项目主文档
- **CHANGELOG.md**: 版本更新日志

## 🔄 文件命名规范

### Python 文件
- 使用小写字母和下划线：`project_generator.py`
- 模块名清晰描述功能

### 脚本文件
- **Windows**: `.ps1` 后缀，使用小写+下划线：`publish_pypi.ps1`
- **Linux/Mac**: `.sh` 后缀，使用小写+下划线：`publish_pypi.sh`
- **Python 脚本**: `.py` 后缀，使用小写+下划线：`self_publish.py`

### 文档文件
- 使用大写字母和下划线：`QUICK_START.md`
- 或使用标题格式：`Quick-Start.md`（推荐统一为一种）

### 配置文件
- 使用小写字母和点号：`config.yaml.example`
- JSON 配置文件：`release-please-config.json`

## 📝 文件分类

### 核心代码
- `src/framework/*.py` - 框架核心实现

### 工具脚本
- `scripts/*.ps1` - Windows 脚本
- `scripts/*.sh` - Linux/Mac 脚本
- `scripts/*.py` - Python 工具脚本

### 文档
- `README.md` - 主文档
- `CHANGELOG.md` - 更新日志
- `docs/guides/*.md` - 使用指南
- `docs/troubleshooting/*.md` - 故障排查
- `docs/development/*.md` - 开发文档

### 配置
- `pyproject.toml` - 项目配置
- `config.yaml.example` - 配置示例
- `.github/workflows/*.yml` - GitHub Actions 工作流

### Cursor Skill
- `cursor_skill/SKILL.md` - Skill 定义
- `cursor_skill/scripts/*.py` - Skill 脚本
- `cursor_skill/references/*.md` - 参考文档

## 🎯 整理建议

### 当前需要整理的内容

1. **scripts/ 目录**
   - ✅ 统一命名：`publish_pypi.ps1` / `publish_pypi.sh`
   - ✅ 合并重复脚本
   - ✅ 重命名 `publish_now.py` → `self_publish.py`

2. **文档结构**
   - 建议创建 `docs/` 目录
   - 将文档分类整理

3. **命名统一**
   - 统一使用小写+下划线（Python 风格）
   - 或统一使用大写+下划线（文档风格）

## 📋 维护清单

定期检查：

- [ ] 文件命名是否统一
- [ ] 是否有重复的脚本
- [ ] 文档是否分类清晰
- [ ] 是否有未使用的文件
- [ ] 目录结构是否合理

---

**最后更新**: 2024-12
**维护者**: Auto Package Framework Team

