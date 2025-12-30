# Auto Package Framework 工作流程指南

本文档详细说明 Auto Package Framework 的完整工作流程，供 Cursor AI 参考。

## 📋 完整工作流程

```
用户输入项目想法
    ↓
1. 解析和验证输入
    ↓
2. 从模板生成项目结构
    ↓
3. AI 生成初始代码（可选）
    ↓
4. 运行代码检查和测试
    ↓
5. 创建 GitHub 仓库（可选）
    ↓
6. 初始化 Git 并推送代码
    ↓
7. 设置 CI/CD 工作流
    ↓
8. 构建包（wheel + source）
    ↓
9. 发布到 PyPI（可选，需确认）
    ↓
10. 创建 GitHub Release
```

## 🔍 详细步骤说明

### 步骤 1: 解析和验证输入

**输入**:
- 项目名称（必需）
- 项目想法描述（必需）
- GitHub 仓库名（可选）
- 输出路径（可选）

**验证**:
- 项目名称是否符合 Python 包命名规范
- 输出路径是否存在且可写
- 必要的凭据是否已配置

### 步骤 2: 从模板生成项目结构

**操作**:
- 使用内置模板（`framework/templates/`）
- 替换模板变量（项目名、作者等）
- 生成标准 Python 包结构

**生成的文件**:
- `pyproject.toml` - 项目配置
- `README.md` - 项目文档
- `src/package_name/` - 源代码目录
- `tests/` - 测试目录
- `.github/workflows/` - CI/CD 配置
- 其他模板文件

### 步骤 3: AI 生成初始代码（可选）

**前提条件**:
- 配置了 AI API（OpenAI 或 Anthropic）
- 提供了项目想法描述

**生成内容**:
- `src/package_name/__init__.py` - 包初始化
- `src/package_name/main.py` - 主要功能模块
- `tests/test_main.py` - 基础测试

**注意事项**:
- AI 生成的代码需要人工审查
- 确保代码符合项目规范
- 运行测试验证功能

### 步骤 4: 代码检查和测试

**执行**:
- `ruff check` - 代码检查
- `ruff format` - 代码格式化
- `mypy` - 类型检查
- `pytest` - 运行测试

**如果失败**:
- 记录错误信息
- 允许用户修复后继续
- 或跳过此步骤（根据配置）

### 步骤 5-6: GitHub 集成（可选）

**前提条件**:
- 配置了 `GITHUB_TOKEN`
- 指定了 GitHub 仓库名

**操作**:
1. 使用 GitHub API 创建仓库
2. 初始化本地 Git 仓库
3. 添加远程仓库
4. 提交并推送代码

**注意事项**:
- 检查仓库是否已存在
- 处理权限问题
- 设置仓库描述和主题

### 步骤 7: 设置 CI/CD

**自动配置**:
- GitHub Actions workflow（`.github/workflows/ci.yml`）
- 代码检查、测试、覆盖率
- 自动发布 workflow（`.github/workflows/release.yml`）

### 步骤 8: 构建包

**执行**:
```bash
python -m build
```

**生成**:
- `dist/package_name-x.x.x-py3-none-any.whl` - Wheel 包
- `dist/package_name-x.x.x.tar.gz` - 源码包

### 步骤 9: 发布到 PyPI（可选）

**前提条件**:
- 配置了 `PYPI_TOKEN`
- 用户明确确认
- 包已通过测试

**操作**:
```bash
python -m twine upload dist/*
```

**安全措施**:
- 发布前必须确认
- 建议先使用 TestPyPI 测试
- 检查版本号是否正确

### 步骤 10: 创建 GitHub Release

**操作**:
- 使用 GitHub API 创建 Release
- 使用 CHANGELOG.md 作为 Release 说明
- 标记版本标签

## ⚠️ 错误处理

### 常见错误及处理

1. **模板路径不存在**
   - 检查内置模板是否完整
   - 回退到相对路径（开发环境）

2. **GitHub API 错误**
   - 检查 Token 权限
   - 验证仓库名是否可用
   - 处理网络错误

3. **PyPI 发布失败**
   - 检查包名是否已存在
   - 验证版本号
   - 检查 Token 权限

4. **AI 代码生成失败**
   - 记录错误但继续流程
   - 允许用户手动添加代码

## 🔄 回滚机制

如果某个步骤失败：
1. 保留已完成的步骤
2. 记录详细的错误信息
3. 提供修复建议
4. 允许用户手动修复后继续

## 📊 执行结果

**成功时返回**:
```python
{
    "success": True,
    "project_path": "/path/to/project",
    "github_repo": "https://github.com/user/repo",
    "pypi_published": True,
    "steps": ["步骤1", "步骤2", ...]
}
```

**失败时返回**:
```python
{
    "success": False,
    "errors": ["错误1", "错误2", ...],
    "steps": ["已完成的步骤"]
}
```

## 🎯 最佳实践

1. **分步骤执行**: 每步都允许用户审查
2. **详细日志**: 记录所有操作和结果
3. **安全第一**: 关键操作需要确认
4. **错误恢复**: 失败时保留已完成部分
5. **用户友好**: 提供清晰的提示和反馈

