# Cursor Skill 实现方案讨论

## 📋 概述

本文档讨论如何将 `auto-package-framework` 的工作流程转化为 Cursor IDE 的 Skill，让 Cursor AI 能够内化并自动执行 Python 包的创建、开发和发布流程。

## 🎯 目标

将以下完整工作流程转化为 Cursor Skill：

```
用户提供项目想法
    ↓
1. 自动生成项目结构（基于内置模板）
    ↓
2. AI 生成初始代码
    ↓
3. 创建 GitHub 仓库并推送
    ↓
4. 设置 CI/CD 工作流
    ↓
5. 构建并发布到 PyPI
    ↓
6. 创建 GitHub Release
```

## 🔍 Cursor Skills 基础

### 什么是 Cursor Skills？

Cursor Skills 是 Cursor IDE 的扩展功能，允许：
- **自定义 AI 能力**：让 Cursor AI 学会执行特定任务
- **可执行脚本**：包含 Python/Bash 等脚本
- **上下文理解**：AI 能够理解何时使用该技能
- **安全执行**：在受控环境中运行

### Skill 结构

```
auto-package-skill/
├── SKILL.md              # 必需：技能定义和说明
├── scripts/              # 可执行脚本
│   ├── create_package.py
│   ├── setup_github.py
│   └── publish_pypi.py
├── references/           # 参考文档
│   ├── workflow.md
│   └── templates/
└── assets/               # 资源文件（可选）
```

## 💡 实现方案

### 方案 1：轻量级 Skill（推荐）

**核心思路**：Skill 作为 Cursor AI 的"知识库"和"执行助手"

#### 结构设计

```
auto-package-skill/
├── SKILL.md                    # 技能定义
├── scripts/
│   ├── create_project.py       # 项目创建脚本
│   ├── generate_code.py        # AI 代码生成（调用框架）
│   ├── setup_github.py         # GitHub 集成
│   └── publish_pypi.py         # PyPI 发布
├── references/
│   ├── workflow_guide.md       # 工作流程指南
│   ├── template_structure.md   # 模板结构说明
│   └── best_practices.md       # 最佳实践
└── config.example.yaml         # 配置示例
```

#### SKILL.md 内容要点

```markdown
# Auto Package Framework Skill

## 功能描述
帮助用户从想法到发布，全自动创建 Python 包。

## 使用场景
- 用户说："我想创建一个新的 Python 包，用于..."
- 用户说："帮我创建一个包并发布到 PyPI"
- 用户提供项目想法，需要自动化流程

## 执行步骤
1. 解析用户的项目想法
2. 调用 create_project.py 生成项目结构
3. 使用 AI 生成初始代码
4. 设置 GitHub 仓库（如果用户提供凭据）
5. 构建并发布到 PyPI（如果用户要求）

## 安全注意事项
- 需要用户明确授权才能访问 GitHub/PyPI
- 敏感信息（token）通过环境变量传递
- 发布前需要用户确认
```

### 方案 2：完整集成 Skill

**核心思路**：Skill 直接调用 `auto-package-framework` 包

#### 优势
- 复用现有框架代码
- 保持功能一致性
- 易于维护和更新

#### 实现方式

```python
# scripts/create_package.py
import sys
import os
from pathlib import Path

# 确保框架已安装
try:
    from framework.core import AutoPackageFramework
except ImportError:
    print("请先安装: pip install auto-package-framework")
    sys.exit(1)

def main():
    # 从环境变量或参数获取配置
    project_name = os.getenv("PROJECT_NAME")
    project_idea = os.getenv("PROJECT_IDEA")
    
    # 初始化框架
    framework = AutoPackageFramework()
    
    # 执行创建流程
    result = framework.create_package(
        project_name=project_name,
        project_idea=project_idea,
        # ... 其他参数
    )
    
    return result
```

## 🔒 安全性讨论

### 关键安全考虑

#### 1. **凭据管理**
- ✅ **推荐**：使用环境变量，不硬编码
- ✅ **推荐**：在 SKILL.md 中明确说明需要哪些凭据
- ❌ **禁止**：在脚本中硬编码 token/密码
- ❌ **禁止**：将凭据提交到代码库

#### 2. **执行权限**
- ✅ **推荐**：关键操作（如发布到 PyPI）需要用户明确确认
- ✅ **推荐**：提供 `--dry-run` 模式，预览操作不执行
- ✅ **推荐**：分步骤执行，每步都允许用户审查

#### 3. **代码审查**
- ✅ **推荐**：AI 生成的代码需要用户审查
- ✅ **推荐**：提供代码审查检查清单
- ✅ **推荐**：自动运行 lint 和测试

#### 4. **错误处理**
- ✅ **推荐**：完善的错误处理和回滚机制
- ✅ **推荐**：详细的日志记录
- ✅ **推荐**：失败时不影响用户现有项目

### 安全最佳实践

```python
# 示例：安全的凭据获取
def get_credentials():
    """安全获取凭据"""
    github_token = os.getenv("GITHUB_TOKEN")
    pypi_token = os.getenv("PYPI_TOKEN")
    
    if not github_token:
        raise ValueError(
            "GITHUB_TOKEN 未设置。"
            "请设置环境变量或使用 --config 指定配置文件"
        )
    
    return {
        "github_token": github_token,
        "pypi_token": pypi_token,
    }
```

## 📝 Skill 定义示例

### SKILL.md 完整示例

```markdown
# Auto Package Framework Skill

## 功能
自动化 Python 包的创建、开发和发布流程。

## 触发条件
当用户提到以下内容时，建议使用此技能：
- "创建一个新的 Python 包"
- "帮我发布包到 PyPI"
- "自动生成项目结构"
- "设置 GitHub 仓库和 CI/CD"

## 使用步骤

### 1. 准备阶段
- 询问用户项目名称和想法
- 确认是否需要 GitHub 和 PyPI 集成
- 检查必要的凭据（环境变量）

### 2. 执行阶段
```bash
# 调用脚本创建项目
python scripts/create_project.py \
    --name "project-name" \
    --idea "项目描述"
```

### 3. 确认阶段
- 展示生成的项目结构
- 等待用户确认后再执行发布操作

## 所需环境变量
- `GITHUB_TOKEN`: GitHub Personal Access Token（可选）
- `PYPI_TOKEN`: PyPI API Token（可选）
- `OPENAI_API_KEY` 或 `ANTHROPIC_API_KEY`: AI API 密钥（可选）

## 安全提示
⚠️ 发布到 PyPI 前，请确保：
1. 代码已通过测试
2. 已审查 AI 生成的代码
3. 版本号正确
4. 已阅读并理解发布的内容

## 示例对话
用户: "我想创建一个用于数据处理的包"
AI: "好的，我来帮你创建。请告诉我：
     1. 包的具体名称
     2. 主要功能描述
     3. 是否需要自动发布到 GitHub 和 PyPI？"
```

## 🚀 实施建议

### 阶段 1：基础 Skill（MVP）
1. ✅ 创建 SKILL.md 定义文件
2. ✅ 实现基础的项目创建脚本
3. ✅ 添加安全检查和确认机制
4. ✅ 测试在 Cursor 中的使用

### 阶段 2：完整集成
1. ✅ 集成 `auto-package-framework` 包
2. ✅ 添加 GitHub 和 PyPI 集成
3. ✅ 实现 AI 代码生成
4. ✅ 添加错误处理和回滚

### 阶段 3：优化和分享
1. ✅ 完善文档和示例
2. ✅ 创建使用教程
3. ✅ 考虑发布到 OpenSkills 或类似平台
4. ✅ 收集用户反馈并改进

## 📚 参考资源

### Cursor Skills 相关
- [Cursor Custom Modes 文档](https://cursor.npmlib.com/docs/editor/chat/custom-modes)
- [Cursor Agent Skills 指南](https://cursor.zone/faq/cursor-agent-skills-guide.html)
- OpenSkills 项目（如果存在）

### 我们的框架
- `auto-package-framework` 主仓库
- 工作流程文档
- API 参考文档

## ❓ 待讨论问题

### 1. 技能范围
- **问题**：Skill 应该包含完整流程，还是分步骤？
- **建议**：先实现完整流程，后续可拆分为多个子技能

### 2. 依赖管理
- **问题**：Skill 是否需要自动安装 `auto-package-framework`？
- **建议**：提供安装脚本，但允许用户手动安装

### 3. 配置方式
- **问题**：配置是通过环境变量、文件，还是 Cursor 设置？
- **建议**：支持多种方式，优先环境变量

### 4. 错误处理
- **问题**：失败时如何处理？是否需要回滚？
- **建议**：详细日志 + 分步骤执行，失败时保留已完成部分

### 5. 用户交互
- **问题**：是否需要交互式确认，还是完全自动化？
- **建议**：关键操作（发布）需要确认，其他可自动化

## 🎯 下一步行动

1. **讨论和确认**：与团队讨论上述方案和问题
2. **创建 MVP**：实现基础 Skill 进行测试
3. **安全审查**：确保安全措施到位
4. **用户测试**：在 Cursor 中测试 Skill
5. **迭代改进**：根据反馈优化

---

**创建日期**: 2024
**状态**: 讨论中
**维护者**: Auto Package Framework Team

