# PyPI 发布问题排查指南

## 🔍 检查步骤

### 1. 检查 GitHub Actions Workflow

访问：https://github.com/flashpoint493/auto-package-framework/actions

查看 `Release` workflow 的运行状态：
- ✅ 如果显示成功：检查 PyPI 网站
- ❌ 如果显示失败：查看错误日志

### 2. 常见问题

#### 问题 1: 缺少 PYPI_API_TOKEN Secret

**症状**：
- Workflow 运行但 PyPI 发布步骤失败
- 错误信息：`HTTPError: 403 Client Error: Invalid or non-existent authentication information`

**解决方案**：
1. 访问 GitHub 仓库设置：https://github.com/flashpoint493/auto-package-framework/settings/secrets/actions
2. 点击 "New repository secret"
3. 名称：`PYPI_API_TOKEN`
4. 值：你的 PyPI API Token（格式：`pypi-xxxxx`）
5. 点击 "Add secret"

**如何获取 PyPI API Token**：
1. 访问：https://pypi.org/manage/account/token/
2. 点击 "Add API token"
3. 选择作用域：
   - **项目级别**（推荐）：只允许发布 `auto-package-framework` 项目
   - **账户级别**：可以发布所有项目
4. 复制生成的 token（格式：`pypi-xxxxx`）

#### 问题 2: Token 权限不足

**症状**：
- 错误信息：`403 Forbidden` 或 `401 Unauthorized`

**解决方案**：
- 确保 token 有正确的权限
- 如果是项目级别 token，确保项目名称匹配：`auto-package-framework`

#### 问题 3: 版本已存在

**症状**：
- 错误信息：`File already exists` 或 `This filename has already been used`

**解决方案**：
- 检查 PyPI 上是否已有该版本：https://pypi.org/project/auto-package-framework/
- 如果已存在，需要更新版本号

#### 问题 4: 包描述格式错误

**症状**：
- 错误信息：`The description failed to render`

**解决方案**：
- 检查 `README.md` 格式是否正确
- 运行 `twine check dist/*` 检查包

## 🚀 手动发布方案

如果 GitHub Actions 无法自动发布，可以手动发布：

### 步骤 1: 构建包

```bash
cd auto_package_framework
pip install build twine
python -m build
```

### 步骤 2: 检查包

```bash
twine check dist/*
```

### 步骤 3: 发布到 PyPI

```bash
# 使用 API Token
python -m twine upload dist/* \
    --username __token__ \
    --password pypi-你的token
```

或者使用环境变量：

```bash
# Windows PowerShell
$env:TWINE_USERNAME="__token__"
$env:TWINE_PASSWORD="pypi-你的token"
python -m twine upload dist/*

# Linux/Mac
export TWINE_USERNAME="__token__"
export TWINE_PASSWORD="pypi-你的token"
python -m twine upload dist/*
```

### 步骤 4: 验证发布

访问：https://pypi.org/project/auto-package-framework/

检查版本 `0.2.0` 是否已发布。

## 📋 检查清单

在发布前，确保：

- [ ] `pyproject.toml` 中的版本号已更新（当前：`0.2.0`）
- [ ] `CHANGELOG.md` 已更新
- [ ] 已创建并推送 git tag（`v0.2.0`）
- [ ] GitHub Actions 中配置了 `PYPI_API_TOKEN` secret
- [ ] PyPI API Token 有正确的权限
- [ ] 本地构建成功（`python -m build`）
- [ ] 包检查通过（`twine check dist/*`）

## 🔗 相关链接

- GitHub Actions: https://github.com/flashpoint493/auto-package-framework/actions
- PyPI 项目页面: https://pypi.org/project/auto-package-framework/
- PyPI Token 管理: https://pypi.org/manage/account/token/
- GitHub Secrets: https://github.com/flashpoint493/auto-package-framework/settings/secrets/actions

