# Auto Package Framework Skill

## 功能描述

这是一个自动化 Python 包创建、开发和发布的 Cursor Skill。当用户想要创建一个新的 Python 包时，此技能可以帮助：

1. 从模板自动生成项目结构
2. 使用 AI 生成初始代码
3. 创建 GitHub 仓库并推送代码
4. 设置 CI/CD 工作流
5. 构建并发布包到 PyPI

## 使用场景

在以下情况下，建议使用此技能：

- 用户说："我想创建一个新的 Python 包，用于..."
- 用户说："帮我创建一个包并发布到 PyPI"
- 用户提供项目想法，需要自动化流程
- 用户需要快速搭建标准的 Python 包项目结构

## 执行流程

### 1. 信息收集阶段
- 询问用户项目名称
- 收集项目想法和功能描述
- 确认是否需要 GitHub 和 PyPI 集成
- 检查必要的环境变量和凭据

### 2. 项目创建阶段
```bash
# 调用项目创建脚本
python scripts/create_package.py \
    --name "project-name" \
    --idea "项目描述" \
    --output "./output"
```

### 3. 代码生成阶段（可选）
- 如果配置了 AI API，自动生成初始代码
- 生成的文件包括：
  - `src/package_name/__init__.py`
  - `src/package_name/main.py`
  - `tests/test_main.py`

### 4. GitHub 集成阶段（可选）
- 创建 GitHub 仓库
- 初始化 Git 并推送代码
- 设置 CI/CD 工作流

### 5. PyPI 发布阶段（可选，需用户确认）
- 构建包（wheel 和 source distribution）
- 上传到 PyPI
- 创建 GitHub Release

## 所需环境变量

### 必需（根据使用场景）
- `GITHUB_TOKEN`: GitHub Personal Access Token（用于 GitHub 集成）
- `PYPI_TOKEN`: PyPI API Token（用于 PyPI 发布）
- `OPENAI_API_KEY` 或 `ANTHROPIC_API_KEY`: AI API 密钥（用于代码生成）

### 配置方式
1. **环境变量**（推荐）：
   ```bash
   export GITHUB_TOKEN=ghp_xxxxx
   export PYPI_TOKEN=pypi-xxxxx
   export OPENAI_API_KEY=sk-xxxxx
   ```

2. **配置文件**：
   创建 `config.yaml` 文件（参考 `config.yaml.example`）

## 安全注意事项

⚠️ **重要安全提示**：

1. **凭据安全**
   - 永远不要在代码中硬编码 token 或密码
   - 使用环境变量或安全的配置文件
   - 不要将包含凭据的文件提交到 Git

2. **发布前确认**
   - 发布到 PyPI 前，必须经过用户明确确认
   - 建议先使用 TestPyPI 进行测试
   - 检查版本号和包内容

3. **代码审查**
   - AI 生成的代码需要人工审查
   - 运行测试确保代码质量
   - 检查安全漏洞

4. **权限最小化**
   - GitHub Token 使用最小必要权限
   - PyPI Token 使用 API Token 而非密码

## 使用示例

### 示例 1：基础项目创建
```
用户: "我想创建一个用于数据处理的 Python 包"

AI: "好的，我来帮你创建。请告诉我：
     1. 包的具体名称（例如：data-processor）
     2. 主要功能描述
     3. 是否需要自动发布到 GitHub 和 PyPI？"
```

### 示例 2：完整流程
```
用户: "创建一个名为 'my-tool' 的包，功能是处理文件，并发布到 PyPI"

AI: "收到！我将执行以下步骤：
     1. 创建项目结构
     2. 生成初始代码
     3. 创建 GitHub 仓库
     4. 构建并发布到 PyPI
     
     请确认是否继续？"
```

## 错误处理

如果执行过程中出现错误：
- 记录详细的错误信息
- 保留已完成的步骤
- 提供回滚建议
- 允许用户手动修复后继续

## 依赖要求

- Python 3.8+
- `auto-package-framework` 包（可通过 `pip install auto-package-framework` 安装）
- Git（用于版本控制）
- 可选的 AI API 访问权限

## 相关文档

- [Auto Package Framework 主文档](../README.md)
- [快速开始指南](../QUICK_START.md)
- [工作流程说明](../SUMMARY.md)

## 版本信息

- Skill 版本: 1.0.0
- 框架版本: 0.1.0
- 最后更新: 2024

---

**注意**: 这是一个示例 Skill 定义。实际使用时，请根据 Cursor 的最新文档和要求进行调整。

