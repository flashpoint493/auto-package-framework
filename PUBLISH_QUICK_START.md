# 快速发布指南

> 5分钟快速发布 auto_package_framework 到GitHub和PyPI

## ⚡ 超快速发布

### 1. 获取API Token

#### GitHub Token
1. 访问: https://github.com/settings/tokens
2. 点击 "Generate new token (classic)"
3. 勾选 `repo` 权限
4. 复制token（格式: `ghp_xxxxx`）

#### PyPI Token
1. 访问: https://pypi.org/manage/account/token/
2. 点击 "Add API token"
3. 复制token（格式: `pypi-xxxxx`）

### 2. 设置环境变量

**Windows PowerShell:**
```powershell
$env:GITHUB_TOKEN="ghp_你的token"
$env:PYPI_TOKEN="pypi-你的token"
```

**Linux/Mac:**
```bash
export GITHUB_TOKEN=ghp_你的token
export PYPI_TOKEN=pypi-你的token
```

### 3. 更新项目信息

编辑 `pyproject.toml`，替换以下内容：

```toml
authors = [
    {name = "你的名字", email = "your.email@example.com"}
]

[project.urls]
Homepage = "https://github.com/你的用户名/auto-package-framework"
Documentation = "https://github.com/你的用户名/auto-package-framework#readme"
Repository = "https://github.com/你的用户名/auto-package-framework"
Issues = "https://github.com/你的用户名/auto-package-framework/issues"
```

### 4. 初始化Git仓库（如果还没有）

```bash
cd auto_package_framework
git init
git add .
git commit -m "chore: initial commit"
```

### 5. 创建GitHub仓库

访问: https://github.com/new
- 仓库名: `auto-package-framework`
- 描述: "AI驱动的自动化Python包创建、开发和发布框架"
- 选择 Public
- **不要**勾选初始化README
- 点击创建

### 6. 推送代码到GitHub

```bash
git remote add origin https://github.com/你的用户名/auto-package-framework.git
git branch -M main
git push -u origin main
```

### 7. 构建和发布到PyPI

```bash
# 安装构建工具
pip install build twine

# 构建
python -m build

# 发布（会提示输入凭据，Username填: __token__, Password填: pypi-你的token）
python -m twine upload dist/*
```

### 8. 创建GitHub Release

访问: https://github.com/你的用户名/auto-package-framework/releases/new
- 标签: `v0.1.0`
- 标题: `v0.1.0 - Initial Release`
- 描述: 写一些发布说明
- 发布

## ✅ 完成！

现在你的包已经：
- ✅ 在GitHub上
- ✅ 在PyPI上（可以通过 `pip install auto-package-framework` 安装）

## 🔄 后续版本发布

### 使用脚本（推荐）

**Linux/Mac:**
```bash
chmod +x scripts/publish.sh
./scripts/publish.sh 0.2.0
```

**Windows PowerShell:**
```powershell
.\scripts\publish.ps1 -Version 0.2.0
```

### 手动发布

1. 更新 `pyproject.toml` 中的版本号
2. 构建: `python -m build`
3. 发布: `python -m twine upload dist/*`
4. 创建Git标签: `git tag v0.2.0 && git push origin v0.2.0`
5. 在GitHub创建Release

## 📝 重要提示

1. **不要将token提交到代码库**
   - 使用环境变量
   - 确保 `.env` 在 `.gitignore` 中

2. **首次发布建议先测试**
   - 先发布到TestPyPI: `python -m twine upload --repository testpypi dist/*`
   - 测试安装: `pip install -i https://test.pypi.org/simple/ auto-package-framework`

3. **版本号遵循语义化版本**
   - MAJOR.MINOR.PATCH
   - 例如: 0.1.0, 0.2.0, 1.0.0

## 🆘 需要帮助？

查看详细指南: [PUBLISH_GUIDE.md](./PUBLISH_GUIDE.md)

