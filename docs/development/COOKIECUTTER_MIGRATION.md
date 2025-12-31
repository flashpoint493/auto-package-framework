# Cookiecutter 迁移完成说明

> 本文档说明从自定义模板系统迁移到 Cookiecutter 的完成情况

## 📋 迁移概述

我们已经成功将 `auto-package-framework` 的模板系统从自定义实现迁移到标准的 [Cookiecutter](https://github.com/cookiecutter/cookiecutter) 格式。

## ✅ 已完成的工作

### 1. 模板标准化

#### cookiecutter.json 创建
- 位置：`PROJECT_TEMPLATE/cookiecutter.json`
- 定义了所有模板变量及其默认值
- 支持派生变量计算（package_name, project_slug, main_class）

#### 模板文件转换
所有模板文件已转换为 cookiecutter 格式（使用 `{{ cookiecutter.variable_name }}`）：

- ✅ `pyproject.toml` - 项目配置
- ✅ `README.md` - 项目说明
- ✅ `llms.txt.template` - LLM 上下文文件
- ✅ 其他模板文件（如需要）

### 2. 代码重构

#### ProjectGenerator 重构
- **文件**：`src/framework/project_generator.py`
- **变更**：完全使用 cookiecutter API
- **保持**：向后兼容的接口，不影响现有代码

#### 依赖更新
- **文件**：`pyproject.toml`
- **变更**：添加 `cookiecutter>=2.6.0`

## 🔄 变量映射

### 旧格式 → 新格式

| 旧格式 | 新格式 | 说明 |
|--------|--------|------|
| `[Project Name]` | `{{ cookiecutter.project_name }}` | 项目名称 |
| `[package-name]` | `{{ cookiecutter.package_name }}` | 包名（下划线） |
| `[package_name]` | `{{ cookiecutter.package_name }}` | 包名（下划线） |
| `[USERNAME]` | `{{ cookiecutter.github_username }}` | GitHub 用户名 |
| `[PROJECT_NAME]` | `{{ cookiecutter.project_slug }}` | 项目 slug |
| `Your Name` | `{{ cookiecutter.author_name }}` | 作者名 |
| `your.email@example.com` | `{{ cookiecutter.author_email }}` | 作者邮箱 |

### 派生变量

以下变量由 cookiecutter 自动计算：

- `package_name`: 从 `project_name` 转换（小写，下划线）
- `project_slug`: 从 `project_name` 转换（小写，连字符）
- `main_class`: 从 `project_name` 转换（PascalCase）

## 📝 使用方式

### 对于框架用户

**无变化**：API 接口保持不变，使用方式完全相同。

```python
from framework import AutoPackageFramework

framework = AutoPackageFramework()
result = framework.create_package(
    project_name="my-package",
    project_idea="一个测试包",
    output_path=Path("./output"),
    replacements={
        "github_username": "myuser",
        "author_name": "My Name",
    }
)
```

### 对于模板维护者

现在模板使用标准的 cookiecutter 格式：

1. **变量定义**：在 `cookiecutter.json` 中定义
2. **变量使用**：在模板文件中使用 `{{ cookiecutter.variable_name }}`
3. **派生变量**：使用 Jinja2 表达式计算

## 🎯 优势

### 1. 标准化
- ✅ 符合业界标准（24.5k stars）
- ✅ 易于理解和维护
- ✅ 可以使用 cookiecutter 生态系统

### 2. 功能增强
- ✅ 支持更复杂的变量计算
- ✅ 支持条件变量（未来可扩展）
- ✅ 支持 hooks（未来可扩展）

### 3. AI 友好
- ✅ 标准化格式更易被 AI 理解
- ✅ 可以使用 cookiecutter 社区模板
- ✅ 更容易生成符合规范的模板

## 🔧 技术细节

### CookieCutter 上下文准备

`ProjectGenerator._prepare_context()` 方法负责：
1. 读取 `cookiecutter.json` 获取默认值
2. 从 `replacements` 参数获取用户提供的值
3. 计算派生变量（package_name, project_slug, main_class）
4. 返回完整的上下文字典

### 目录结构

Cookiecutter 会在输出目录下创建以 `project_name` 命名的子目录。
我们的代码会自动处理这个逻辑，确保生成的文件在正确的位置。

## 📚 相关文档

- [Cookiecutter 官方文档](https://cookiecutter.readthedocs.io/)
- [Cookiecutter JSON 格式](https://cookiecutter.readthedocs.io/en/latest/advanced/cookiecutter_json.html)
- [集成分析文档](./COOKIECUTTER_INTEGRATION_ANALYSIS.md)

## 🚀 未来扩展

### 可选的增强功能

1. **Hooks 支持**
   - `pre_gen_project.py` - 生成前执行
   - `post_gen_project.py` - 生成后执行

2. **条件变量**
   - 根据用户选择显示/隐藏某些选项

3. **交互式提示**
   - 在 CLI 模式下提供交互式输入

## ⚠️ 注意事项

1. **模板必须包含 cookiecutter.json**
   - 如果模板目录缺少此文件，会抛出错误

2. **变量命名规范**
   - 使用小写下划线格式（snake_case）
   - 例如：`github_username` 而不是 `githubUsername`

3. **向后兼容**
   - API 接口保持不变
   - 但模板格式已改变，需要更新模板

---

**迁移完成日期**: 2025-01-XX  
**状态**: ✅ 已完成

