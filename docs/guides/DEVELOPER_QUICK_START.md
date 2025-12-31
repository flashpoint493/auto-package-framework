# 开发者快速开始指南

> 从想法到发布，5分钟创建你的第一个 Python 包

本指南将帮助你快速使用 `auto-package-framework` 和 `python-package-template` 创建自己的 Python 包。

## 📚 两个仓库的作用

### 1. `auto-package-framework` - 自动化框架
- **作用**: 自动化工具，帮你从想法到发布
- **功能**: 生成项目、AI 代码生成、GitHub 集成、PyPI 发布
- **安装**: `pip install auto-package-framework`

### 2. `python-package-template` - 项目模板
- **作用**: 专业项目模板（已内置到框架中）
- **功能**: 提供完整的项目结构、CI/CD、文档模板
- **使用**: 框架自动使用，无需手动操作

## 🚀 快速开始（3 步）

### 步骤 1: 安装框架

```bash
# 方式 1: 使用 pip 安装
pip install auto-package-framework

# 方式 2: 使用 uvx（无需安装）
uvx auto-package-framework --help
```

### 步骤 2: 配置 API Keys

选择以下**两种模式之一**：

#### 模式 A: API Key 模式（自动生成代码）

```bash
# 设置环境变量（推荐）
export OPENAI_API_KEY="sk-xxxxx"          # 或使用 Anthropic
export ANTHROPIC_API_KEY="sk-ant-xxxxx"  # 二选一即可
export GITHUB_TOKEN="ghp_xxxxx"           # 可选，用于 GitHub 集成
export PYPI_TOKEN="pypi-xxxxx"            # 可选，用于 PyPI 发布
```

#### 模式 B: Cursor IDE 模式（手动生成代码）

```bash
# 只需要 GitHub 和 PyPI（可选）
export GITHUB_TOKEN="ghp_xxxxx"           # 可选
export PYPI_TOKEN="pypi-xxxxx"            # 可选
# 不需要 AI API Key，代码在 Cursor IDE 中生成
```

### 步骤 3: 创建你的包

```bash
# 使用命令行工具
auto-package \
  --project-name "my-awesome-package" \
  --idea "一个用于数据处理的 Python 包，提供数据清洗、转换和分析功能" \
  --github-repo "my-awesome-package" \
  --publish  # 可选，自动发布到 PyPI
```

## 📖 详细使用指南

### 场景 1: 使用 API Key 模式（全自动）

**适用场景**: 想要完全自动化，AI 自动生成代码

#### 1.1 准备 API Keys

```bash
# 获取 OpenAI API Key
# 访问: https://platform.openai.com/api-keys
export OPENAI_API_KEY="sk-xxxxx"

# 或使用 Anthropic
# 访问: https://console.anthropic.com/
export ANTHROPIC_API_KEY="sk-ant-xxxxx"

# GitHub Token（可选，用于自动创建仓库）
# 访问: https://github.com/settings/tokens
export GITHUB_TOKEN="ghp_xxxxx"

# PyPI Token（可选，用于自动发布）
# 访问: https://pypi.org/manage/account/token/
export PYPI_TOKEN="pypi-xxxxx"
```

#### 1.2 创建配置文件（可选）

创建 `config.yaml`:

```yaml
github:
  username: your_github_username
  # token 通过环境变量设置，更安全

ai:
  provider: openai  # 或 anthropic
  # api_key 通过环境变量设置
  model: gpt-4  # 或 claude-3-opus-20240229

pypi:
  # token 通过环境变量设置
```

#### 1.3 运行创建命令

```bash
auto-package \
  --project-name "data-processor" \
  --idea "一个强大的数据处理包，支持 CSV、JSON、Excel 文件的读取、清洗、转换和导出" \
  --github-repo "data-processor" \
  --output "./my-projects"
```

**框架会自动**:
1. ✅ 生成项目结构（基于模板）
2. ✅ AI 生成初始代码
3. ✅ 创建 GitHub 仓库（如果配置了 token）
4. ✅ 推送代码到 GitHub
5. ✅ 设置 CI/CD 工作流
6. ✅ 发布到 PyPI（如果使用 `--publish`）

### 场景 2: 使用 Cursor IDE 模式（半自动）

**适用场景**: 想要在 Cursor IDE 中与 AI 对话生成代码，更灵活可控

#### 2.1 配置环境变量

```bash
# 只需要 GitHub 和 PyPI（可选）
export GITHUB_TOKEN="ghp_xxxxx"
export PYPI_TOKEN="pypi-xxxxx"
# 不需要 AI API Key
```

#### 2.2 创建配置文件

创建 `config.yaml`:

```yaml
github:
  username: your_github_username

# 不配置 AI，使用 Cursor IDE 模式
code_generation:
  mode: cursor  # 使用 Cursor IDE 对话模式
```

#### 2.3 运行创建命令

```bash
auto-package \
  --project-name "my-package" \
  --idea "一个用于文件管理的包" \
  --output "./my-projects"
```

**框架会**:
1. ✅ 生成项目结构
2. ⏸️ **暂停**，等待你在 Cursor IDE 中生成代码
3. ✅ 提供引导文件（`AI_CODE_GENERATION_DIALOGUE.md`）
4. ✅ 等待你完成代码生成后继续
5. ✅ 创建 GitHub 仓库（如果配置了）

#### 2.4 在 Cursor IDE 中生成代码

1. **打开项目目录**:
   ```bash
   cd ./my-projects/my-package
   ```

2. **在 Cursor 中打开项目**:
   - 使用 Cursor IDE 打开该目录
   - 查看 `AI_CODE_GENERATION_DIALOGUE.md` 文件

3. **与 AI 对话生成代码**:
   ```
   你: "根据 PROJECT_IDEA.md 和 AI_CONTEXT.md，帮我生成核心功能代码"
   
   Cursor AI: 会根据项目想法和上下文生成代码
   ```

4. **完成后继续**:
   - 框架会自动检测生成的文件
   - 继续后续流程（GitHub、PyPI 等）

### 场景 3: 使用 Cursor Skill（最便捷）

**适用场景**: 在 Cursor IDE 中直接使用 Skill，无需命令行

#### 3.1 安装 Skill

1. 打开 Cursor 设置（`Cmd+Shift+J` 或 `Ctrl+Shift+J`）
2. 选择 **Beta** 选项卡
3. 将更新渠道设置为 **Nightly**
4. 重启 Cursor
5. 在 **Settings → Rules** 中，开启 **Agent Skills**

#### 3.2 在 Cursor 中对话

```
你: "我想创建一个名为 'text-analyzer' 的 Python 包，用于文本分析和情感分析"

Cursor AI: "好的，我来帮你创建。请确认：
           1. 包名: text-analyzer
           2. 功能: 文本分析和情感分析
           3. 是否需要创建 GitHub 仓库？
           4. 是否需要发布到 PyPI？"
```

Cursor AI 会自动调用 Skill 完成所有步骤。

## 🎯 完整示例

### 示例 1: 创建一个数据处理包（API 模式）

```bash
# 1. 设置环境变量
export OPENAI_API_KEY="sk-xxxxx"
export GITHUB_TOKEN="ghp_xxxxx"

# 2. 创建包
auto-package \
  --project-name "data-processor" \
  --idea "一个数据处理包，支持 CSV、JSON、Excel 的读取、清洗、转换和导出。主要功能包括：
  - 数据读取：支持多种格式
  - 数据清洗：去除空值、重复值
  - 数据转换：类型转换、格式转换
  - 数据导出：导出为多种格式" \
  --github-repo "data-processor" \
  --output "./projects"

# 3. 查看结果
cd ./projects/data-processor
ls -la
```

### 示例 2: 创建一个工具包（Cursor 模式）

```bash
# 1. 创建包（不配置 AI API Key）
auto-package \
  --project-name "file-manager" \
  --idea "一个文件管理工具包，提供文件操作、搜索、批量处理功能" \
  --output "./projects"

# 2. 在 Cursor IDE 中打开
cd ./projects/file-manager
# 在 Cursor 中打开此目录

# 3. 查看引导文件
cat AI_CODE_GENERATION_DIALOGUE.md

# 4. 在 Cursor 中与 AI 对话生成代码
# 完成后，框架会自动继续
```

## 🔧 配置说明

### 环境变量配置

| 变量名 | 必需 | 说明 | 获取方式 |
|--------|------|------|----------|
| `OPENAI_API_KEY` | API 模式必需 | OpenAI API Key | https://platform.openai.com/api-keys |
| `ANTHROPIC_API_KEY` | API 模式必需 | Anthropic API Key | https://console.anthropic.com/ |
| `GITHUB_TOKEN` | 可选 | GitHub Personal Access Token | https://github.com/settings/tokens |
| `PYPI_TOKEN` | 可选 | PyPI API Token | https://pypi.org/manage/account/token/ |
| `GITHUB_USERNAME` | 可选 | GitHub 用户名 | 自动从 token 获取 |

### 配置文件（config.yaml）

```yaml
# GitHub 配置
github:
  username: your_github_username
  # token 通过环境变量设置

# PyPI 配置
pypi:
  # token 通过环境变量设置

# AI 配置（API 模式）
ai:
  provider: openai  # 或 anthropic
  model: gpt-4      # 或 claude-3-opus-20240229
  # api_key 通过环境变量设置

# 代码生成模式
code_generation:
  mode: auto  # auto, api, cursor, agent
  # auto: 自动选择（优先 Cursor，其次 API）
  # api: 使用 API 模式
  # cursor: 使用 Cursor IDE 模式
  # agent: Agent 模式（未来支持）
```

## 📝 工作流程对比

### API 模式工作流

```
想法 → 配置 API Key → 运行命令 → AI 生成代码 → GitHub → PyPI → 完成
         (1分钟)      (1分钟)      (2-5分钟)    (1分钟)  (1分钟)
```

**总时间**: 约 5-10 分钟

### Cursor IDE 模式工作流

```
想法 → 运行命令 → 生成结构 → 在 Cursor 中生成代码 → GitHub → PyPI → 完成
         (1分钟)    (30秒)        (5-30分钟)          (1分钟)  (1分钟)
```

**总时间**: 约 8-35 分钟（取决于代码复杂度）

## ❓ 常见问题

### Q1: 我应该选择哪种模式？

- **API 模式**: 想要快速生成，代码质量要求不高，适合原型
- **Cursor 模式**: 想要更好的代码质量，需要与 AI 交互调整，适合生产项目

### Q2: 如何获取 API Keys？

- **OpenAI**: https://platform.openai.com/api-keys
- **Anthropic**: https://console.anthropic.com/
- **GitHub**: https://github.com/settings/tokens（需要 `repo` 权限）
- **PyPI**: https://pypi.org/manage/account/token/

### Q3: 模板在哪里？

模板已内置到 `auto-package-framework` 包中，无需单独下载。如果需要查看模板，可以访问：
https://github.com/flashpoint493/python-package-template

### Q4: 如何自定义模板？

1. Fork [python-package-template](https://github.com/flashpoint493/python-package-template)
2. 修改模板内容
3. 在 `config.yaml` 中指定 `template_path`

### Q5: 代码生成失败怎么办？

- **API 模式**: 检查 API Key 是否正确，账户余额是否充足
- **Cursor 模式**: 确保在 Cursor IDE 中打开了项目，并按照引导文件操作

### Q6: 如何只生成项目结构，不生成代码？

```bash
# 使用 Cursor 模式，但不完成代码生成步骤
auto-package \
  --project-name "my-package" \
  --idea "项目描述" \
  --output "./projects"
# 然后手动在 Cursor 中生成代码
```

## 🎓 下一步

创建项目后，你可以：

1. **查看生成的项目结构**
   ```bash
   cd your-project-name
   tree -L 2
   ```

2. **阅读项目文档**
   - `README.md` - 项目说明
   - `PROJECT_IDEA.md` - 项目想法
   - `AI_CONTEXT.md` - AI 上下文
   - `QUICK_START.md` - 快速开始

3. **开发功能**
   - 在 `src/your_package/` 中添加代码
   - 在 `tests/` 中添加测试

4. **运行测试**
   ```bash
   pip install -e ".[dev]"
   pytest
   ```

5. **发布到 PyPI**
   ```bash
   # 如果之前没有使用 --publish
   # 可以手动发布
   python -m build
   twine upload dist/*
   ```

## 🔗 相关资源

- [Auto Package Framework 主文档](../README.md)
- [Python Package Template](https://github.com/flashpoint493/python-package-template)
- [Cursor Skill 使用指南](../cursor_skill/README.md)
- [架构设计文档](../development/ARCHITECTURE_DESIGN.md)

---

**需要帮助？** 在 [GitHub Issues](https://github.com/flashpoint493/auto-package-framework/issues) 提问！

