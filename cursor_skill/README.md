# Auto Package Framework - Cursor Skill

这是 `auto-package-framework` 的 Cursor Skill 实现，让 Cursor AI 能够自动执行 Python 包的创建、开发和发布流程。

## 📁 目录结构

```
cursor_skill/
├── SKILL.md                    # 技能定义文件（必需）
├── scripts/                     # 可执行脚本
│   └── create_package.py       # 项目创建脚本
├── references/                  # 参考文档（可选）
└── README.md                    # 本文件
```

## 🚀 快速开始

### 1. 安装依赖

```bash
pip install auto-package-framework
```

### 2. 设置环境变量

```bash
# GitHub（可选，用于 GitHub 集成）
export GITHUB_TOKEN=ghp_xxxxx

# PyPI（可选，用于发布）
export PYPI_TOKEN=pypi-xxxxx

# AI API（可选，用于代码生成）
export OPENAI_API_KEY=sk-xxxxx
# 或
export ANTHROPIC_API_KEY=sk-ant-xxxxx
```

### 3. 在 Cursor 中启用 Skill

1. 打开 Cursor 设置（`Cmd+Shift+J` 或 `Ctrl+Shift+J`）
2. 选择 **Beta** 选项卡
3. 将更新渠道设置为 **Nightly**
4. 重启 Cursor
5. 在 **Settings → Rules** 中，开启 **Agent Skills**

### 4. 安装 Skill

将 `cursor_skill` 目录添加到 Cursor 的技能路径中，或使用 OpenSkills 工具安装。

## 💡 使用方法

### 在 Cursor 中对话

```
你: "我想创建一个名为 'my-package' 的 Python 包，用于处理数据"

Cursor AI: "好的，我来帮你创建。请确认：
           1. 包名: my-package
           2. 功能: 处理数据
           3. 是否需要创建 GitHub 仓库？
           4. 是否需要发布到 PyPI？"
```

### 直接使用脚本

```bash
python scripts/create_package.py \
    --name "my-package" \
    --idea "一个用于数据处理的包" \
    --github-repo "my-package" \
    --publish
```

## 🔒 安全提示

1. **凭据管理**
   - 使用环境变量，不要硬编码
   - 不要将包含凭据的文件提交到 Git

2. **发布确认**
   - 发布到 PyPI 前需要明确确认
   - 建议先使用 TestPyPI 测试

3. **代码审查**
   - AI 生成的代码需要人工审查
   - 运行测试确保质量

## 📚 相关文档

- [Cursor Skill 实现方案讨论](../CURSOR_SKILL_PROPOSAL.md)
- [Auto Package Framework 主文档](../README.md)
- [快速开始指南](../QUICK_START.md)

## 🐛 问题反馈

如果遇到问题，请：
1. 检查环境变量是否正确设置
2. 确认 `auto-package-framework` 已正确安装
3. 查看错误日志
4. 在 GitHub 上提交 Issue

## 📝 许可证

与主项目相同（MIT License）

