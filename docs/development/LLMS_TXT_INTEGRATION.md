# llms.txt 集成指南

## 📋 概述

`llms.txt` 是一个 LLM 上下文文件，用于向 AI 助手提供项目的完整 API 参考文档。本文档说明如何将其整合到 `auto-package-framework` 中。

## 🎯 文件用途

### 1. **LLM 上下文提供**
- 让 AI 理解项目的 API 结构和用法
- 帮助 AI 生成符合项目风格的代码
- 确保代码和文档的一致性

### 2. **文档生成模板**
- 作为生成 API 文档的参考格式
- 帮助 AI 创建结构化的文档
- 保持文档风格统一

### 3. **代码质量提升**
- 参考高质量的 API 文档格式
- 生成更规范的代码
- 创建更完整的文档

## 🔧 集成方案

### 方案 1: 作为模板文件（已实现）

**位置**: `PROJECT_TEMPLATE/llms.txt.template`

**特点**:
- 使用 Jinja2 模板语法
- 包含占位符变量
- 自动替换项目特定信息

**变量**:
- `{{ PROJECT_NAME }}` - 项目名称
- `{{ PACKAGE_NAME }}` - 包名
- `{{ MAIN_CLASS }}` - 主类名
- `{{ PROJECT_DESCRIPTION }}` - 项目描述
- 等等...

### 方案 2: 作为 AI 代码生成上下文（已实现）

在 `CursorCodeGenerator` 中：
- 读取 `llms.txt.template` 作为参考格式
- 在对话提示中包含格式参考
- 引导 AI 生成符合格式的代码和文档

### 方案 3: 自动生成 llms.txt（计划中）

框架可以：
1. 在代码生成后，自动生成 `llms.txt`
2. 基于代码注释和结构
3. 使用模板填充内容

## 📝 模板文件说明

### 文件位置

```
PROJECT_TEMPLATE/
└── llms.txt.template  # Jinja2 模板文件
```

### 模板变量

| 变量 | 说明 | 默认值 |
|------|------|--------|
| `PROJECT_NAME` | 项目名称 | 从 project_name 获取 |
| `PACKAGE_NAME` | 包名 | 从 project_name 转换 |
| `PROJECT_DESCRIPTION` | 项目描述 | "A Python package: {name}" |
| `MAIN_CLASS` | 主类名 | 从项目名生成 |
| `PYTHON_VERSION` | Python 版本 | "3.8" |
| `PLATFORMS` | 支持平台 | "Windows, macOS, Linux" |
| `LICENSE` | 许可证 | "MIT" |

### 使用方式

模板文件会在项目生成时自动处理：
1. 读取 `llms.txt.template`
2. 使用 Jinja2 渲染
3. 生成 `llms.txt`（移除 .template 后缀）
4. 替换所有变量

## 🚀 在代码生成中使用

### Cursor 模式

`CursorCodeGenerator` 会自动：
1. 检查是否存在 `llms.txt.template`
2. 读取作为参考格式
3. 在对话提示中包含格式说明
4. 引导 AI 生成符合格式的代码

### API 模式

`APICodeGenerator`（未来）可以：
1. 读取 `llms.txt` 作为上下文
2. 在生成代码时参考其格式
3. 生成符合格式的 API 文档

## 📊 模板特点

### 通用化设计

模板已完全通用化，使用 Jinja2 变量替代所有业务特定内容：
- 所有项目名称、包名、类名都使用变量
- 技术栈描述通用化
- 集成说明可选化

### 保留的通用内容

- ✅ 文档结构（章节组织）
- ✅ 格式规范（Markdown）
- ✅ 示例风格（代码示例写法）
- ✅ API 文档模式（参数说明、返回值等）

## 🔄 工作流程

```
1. 用户创建项目
   ↓
2. 框架生成项目结构
   ↓
3. llms.txt.template 被处理
   ↓
4. 生成 llms.txt（填充变量）
   ↓
5. 代码生成时读取 llms.txt 作为参考
   ↓
6. AI 生成符合格式的代码和文档
```

## 📚 相关文件

- `PROJECT_TEMPLATE/llms.txt.template` - 通用模板
- `docs/development/LLMS_TXT_ANALYSIS.md` - 分析文档
- `src/framework/project_generator.py` - 模板处理逻辑
- `src/framework/code_generator.py` - 代码生成器（使用模板）

## 🎯 最佳实践

### 1. 自定义模板

用户可以：
1. 修改 `llms.txt.template`
2. 添加项目特定的章节
3. 调整格式和风格

### 2. 动态生成

框架可以：
1. 基于代码注释自动生成
2. 使用 AI 填充具体内容
3. 保持与代码同步

### 3. 持续更新

- 代码变更时更新 `llms.txt`
- 使用工具自动同步
- 验证格式和完整性

---

**结论**: `llms.txt` 已成功整合到框架中，作为模板文件和 AI 代码生成的参考格式。

