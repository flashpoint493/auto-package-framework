# 发布指南 - Auto Package Framework

本指南说明如何将 `auto_package_framework` 发布到GitHub和PyPI。

## 📋 发布前准备

### 1. 更新项目信息

编辑 `pyproject.toml`，更新以下信息：

```toml
[project]
name = "auto-package-framework"
version = "0.1.0"  # 更新版本号
description = "AI驱动的自动化Python包创建、开发和发布框架"
authors = [
    {name = "你的名字", email = "your.email@example.com"}  # 更新作者信息
]

[project.urls]
Homepage = "https://github.com/你的用户名/auto-package-framework"  # 更新URL
Documentation = "https://github.com/你的用户名/auto-package-framework#readme"
Repository = "https://github.com/你的用户名/auto-package-framework"
Issues = "https://github.com/你的用户名/auto-package-framework/issues"
```

### 2. 获取API凭据

#### GitHub Token
1. 访问: https://github.com/settings/tokens
2. 点击 "Generate new token (classic)"
3. 勾选权限:
   - ✅ `repo` (完整仓库访问)
   - ✅ `workflow` (如果需要管理Actions)
4. 生成并复制token（格式: `ghp_xxxxx`）

#### PyPI Token（推荐使用API Token）
1. 访问: https://pypi.org/manage/account/token/
2. 点击 "Add API token"
3. 选择作用域:
   - 项目级别（推荐，更安全）
   - 或账户级别（如果发布多个项目）
4. 生成并复制token（格式: `pypi-xxxxx`）

⚠️ **重要**: 不要将token提交到代码库！

## 🔐 配置凭据（三种方式选一种）

### 方式1: 环境变量（最推荐，最安全）

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

**永久设置（Linux/Mac）:**
```bash
# 编辑 ~/.bashrc 或 ~/.zshrc
echo 'export GITHUB_TOKEN=ghp_你的token' >> ~/.bashrc
echo 'export PYPI_TOKEN=pypi-你的token' >> ~/.bashrc
source ~/.bashrc
```

### 方式2: .env文件（本地开发）

在项目根目录创建 `.env` 文件：

```bash
# .env
GITHUB_TOKEN=ghp_你的token
PYPI_TOKEN=pypi-你的token
```

⚠️ **确保 `.env` 已在 `.gitignore` 中！**

### 方式3: 临时设置（仅用于发布）

发布时临时设置环境变量，发布后清除。

## 📦 发布步骤

### 步骤1: 准备Git仓库

```bash
cd auto_package_framework

# 如果还没有初始化Git
git init

# 添加所有文件
git add .

# 提交
git commit -m "chore: prepare for initial release v0.1.0"
```

### 步骤2: 创建GitHub仓库

#### 方式A: 使用GitHub网页创建（推荐首次发布）

1. 访问: https://github.com/new
2. 仓库名称: `auto-package-framework`
3. 描述: "AI驱动的自动化Python包创建、开发和发布框架"
4. 选择: Public（或Private）
5. **不要**勾选 "Initialize this repository with a README"（因为本地已有）
6. 点击 "Create repository"

#### 方式B: 使用GitHub CLI（如果已安装）

```bash
gh repo create auto-package-framework --public --description "AI驱动的自动化Python包创建、开发和发布框架"
```

#### 方式C: 使用框架自己（元！）

```python
from framework.core import AutoPackageFramework

framework = AutoPackageFramework()

# 使用框架自己创建自己的仓库（元操作！）
result = framework.create_package(
    project_name="auto-package-framework",
    project_idea="AI驱动的自动化Python包创建、开发和发布框架",
    github_repo="auto-package-framework",
    auto_publish=False,  # 先不发布，手动发布
)
```

### 步骤3: 推送代码到GitHub

```bash
# 添加远程仓库（替换为你的用户名）
git remote add origin https://github.com/你的用户名/auto-package-framework.git

# 或者使用SSH
# git remote add origin git@github.com:你的用户名/auto-package-framework.git

# 推送代码
git branch -M main
git push -u origin main
```

### 步骤4: 构建包

```bash
# 安装构建工具
pip install build twine

# 清理旧的构建产物
rm -rf dist/ build/ *.egg-info

# 构建包
python -m build
```

构建完成后，检查 `dist/` 目录：
- `auto_package_framework-0.1.0.tar.gz` (源码包)
- `auto_package_framework-0.1.0-py3-none-any.whl` (wheel包)

### 步骤5: 测试发布到TestPyPI（强烈推荐！）

```bash
# 使用TestPyPI测试
python -m twine upload --repository testpypi dist/*

# 输入凭据:
# Username: __token__
# Password: pypi-你的token
```

测试安装：
```bash
pip install -i https://test.pypi.org/simple/ auto-package-framework
```

### 步骤6: 发布到正式PyPI

```bash
# 发布到PyPI
python -m twine upload dist/*

# 输入凭据:
# Username: __token__
# Password: pypi-你的token
```

### 步骤7: 创建GitHub Release

1. 访问: https://github.com/你的用户名/auto-package-framework/releases/new
2. 选择标签: `v0.1.0`（如果不存在，创建新标签）
3. 标题: `v0.1.0 - Initial Release`
4. 描述:
   ```
   ## 🎉 首次发布
   
   - ✅ 项目生成器
   - ✅ GitHub集成
   - ✅ PyPI发布集成
   - ✅ AI代码生成器
   - ✅ 命令行工具
   ```
5. 点击 "Publish release"

## 🔄 后续版本发布

### 更新版本号

编辑 `pyproject.toml`:
```toml
version = "0.2.0"  # 更新版本号
```

### 发布流程

```bash
# 1. 更新代码并提交
git add .
git commit -m "feat: 新功能"
git push

# 2. 构建
python -m build

# 3. 发布到PyPI
python -m twine upload dist/*

# 4. 创建Git标签
git tag -a v0.2.0 -m "Release v0.2.0"
git push origin v0.2.0

# 5. 在GitHub创建Release（或使用网页）
```

## 🛠️ 自动化发布脚本

创建 `scripts/publish.sh` (Linux/Mac):

```bash
#!/bin/bash
set -e

VERSION=$1
if [ -z "$VERSION" ]; then
    echo "用法: ./scripts/publish.sh <版本号>"
    echo "示例: ./scripts/publish.sh 0.1.0"
    exit 1
fi

# 更新版本号
sed -i "s/version = \".*\"/version = \"$VERSION\"/" pyproject.toml

# 构建
python -m build

# 发布到PyPI
python -m twine upload dist/*

# 创建Git标签
git add pyproject.toml
git commit -m "chore: bump version to $VERSION"
git tag -a "v$VERSION" -m "Release v$VERSION"
git push origin main
git push origin "v$VERSION"

echo "✅ 发布完成: v$VERSION"
```

使用:
```bash
chmod +x scripts/publish.sh
./scripts/publish.sh 0.1.0
```

## ✅ 验证发布

### 验证PyPI

1. 访问: https://pypi.org/project/auto-package-framework/
2. 检查包信息是否正确
3. 测试安装:
   ```bash
   pip install auto-package-framework
   ```

### 验证GitHub

1. 访问: https://github.com/你的用户名/auto-package-framework
2. 检查代码是否已推送
3. 检查Release是否已创建

## 🐛 常见问题

### Q: PyPI上传失败，提示包名已存在

A: 包名在PyPI上必须唯一。如果已存在，需要：
- 更改包名（修改 `pyproject.toml` 中的 `name`）
- 或联系原包维护者

### Q: GitHub推送失败，提示权限不足

A: 检查：
- Token是否有 `repo` 权限
- Token是否过期
- 仓库是否存在

### Q: 如何更新已发布的版本？

A: PyPI不允许覆盖已发布的版本。需要：
- 发布新版本（更新版本号）
- 或联系PyPI管理员删除旧版本（不推荐）

## 📚 参考资源

- [PyPI上传指南](https://packaging.python.org/en/latest/guides/distributing-packages-using-setuptools/)
- [GitHub Releases文档](https://docs.github.com/en/repositories/releasing-projects-on-github)
- [语义化版本](https://semver.org/lang/zh-CN/)

---

**祝发布顺利！** 🚀

