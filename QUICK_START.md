# 快速开始指南

> 5分钟快速上手Auto Package Framework

## ⚡ 超快速开始

### 1. 安装

```bash
cd auto_package_framework
pip install -e ".[dev]"
```

### 2. 配置环境变量

```bash
# Windows PowerShell
$env:GITHUB_TOKEN="ghp_xxxxx"
$env:PYPI_TOKEN="pypi-xxxxx"
$env:OPENAI_API_KEY="sk-xxxxx"

# Linux/Mac
export GITHUB_TOKEN=ghp_xxxxx
export PYPI_TOKEN=pypi-xxxxx
export OPENAI_API_KEY=sk-xxxxx
```

### 3. 创建第一个包

```python
from framework.core import AutoPackageFramework

framework = AutoPackageFramework()

result = framework.create_package(
    project_name="hello-world-package",
    project_idea="一个简单的Hello World包，用于测试框架",
)
```

完成！项目已生成到 `hello-world-package/` 目录。

## 📚 详细步骤

### 步骤1: 获取API凭据

#### GitHub Token
1. 访问 https://github.com/settings/tokens
2. 点击 "Generate new token (classic)"
3. 勾选 `repo` 权限
4. 复制token（格式: `ghp_xxxxx`）

#### PyPI Token（可选，如果需要发布）
1. 访问 https://pypi.org/manage/account/token/
2. 创建新的API token
3. 复制token（格式: `pypi-xxxxx`）

#### OpenAI API Key（可选，如果需要AI生成代码）
1. 访问 https://platform.openai.com/api-keys
2. 创建新的API key
3. 确保账户有余额

### 步骤2: 配置框架

**选项A: 环境变量（推荐）**

```bash
export GITHUB_TOKEN=ghp_xxxxx
export PYPI_TOKEN=pypi-xxxxx
export OPENAI_API_KEY=sk-xxxxx
```

**选项B: 配置文件**

```bash
cp config.yaml.example config.yaml
# 编辑config.yaml填入凭据
```

### 步骤3: 测试生成项目

```python
from framework.core import AutoPackageFramework

framework = AutoPackageFramework()

# 测试1: 仅生成项目（最安全）
result = framework.create_package(
    project_name="test-package",
    project_idea="测试项目",
)

print(result)
```

### 步骤4: 创建GitHub仓库（可选）

```python
result = framework.create_package(
    project_name="my-package",
    project_idea="我的项目描述",
    github_repo="my-package",  # 指定仓库名
)
```

### 步骤5: 发布到PyPI（可选）

⚠️ **注意**: 这会实际发布到PyPI，请确保包名唯一！

```python
result = framework.create_package(
    project_name="my-unique-package-name",
    project_idea="我的项目描述",
    github_repo="my-unique-package-name",
    auto_publish=True,  # 发布到PyPI
)
```

## 🎯 使用场景

### 场景1: 快速原型

```python
# 快速创建一个原型项目
framework.create_package(
    project_name="prototype-001",
    project_idea="快速验证一个想法",
)
```

### 场景2: 标准开源包

```python
# 创建完整的开源包
framework.create_package(
    project_name="awesome-tool",
    project_idea="""
    一个强大的工具包。
    
    功能:
    - 核心功能1
    - 核心功能2
    """,
    github_repo="awesome-tool",
    auto_publish=True,
)
```

### 场景3: 内部工具包

```python
# 创建内部工具（不发布到PyPI）
framework.create_package(
    project_name="internal-utils",
    project_idea="内部使用的工具函数集合",
    github_repo="internal-utils",
    auto_publish=False,
)
```

## 🔧 常见问题

### Q: 如何跳过某个步骤？

A: 不提供相应参数即可：
- 不提供 `github_repo` → 不创建GitHub仓库
- `auto_publish=False` → 不发布到PyPI
- 不配置AI → 不生成AI代码

### Q: 如何自定义项目信息？

A: 使用 `replacements` 参数：

```python
framework.create_package(
    project_name="my-package",
    project_idea="描述",
    replacements={
        "USERNAME": "my_github_username",
        "email": "my.email@example.com",
        "author": "My Name",
    },
)
```

### Q: 生成的代码质量如何？

A: AI生成的代码是初始版本，建议：
1. 运行 `ruff check .` 检查代码质量
2. 运行 `pytest` 确保测试通过
3. 人工审查关键代码
4. 根据需要进行优化

### Q: 可以批量创建吗？

A: 目前需要循环调用，未来版本会支持批量创建：

```python
projects = [
    ("package-1", "描述1"),
    ("package-2", "描述2"),
]

for name, idea in projects:
    framework.create_package(
        project_name=name,
        project_idea=idea,
    )
```

## 📖 下一步

- 查看 [README.md](./README.md) 了解完整功能
- 查看 [EXTERNAL_TOOLS.md](./EXTERNAL_TOOLS.md) 了解所需工具
- 查看 [MINIMAL_PROTOTYPE.md](./MINIMAL_PROTOTYPE.md) 进行完整测试
- 查看 [example_usage.py](./example_usage.py) 查看更多示例

## 🆘 需要帮助？

- 查看文档: [README.md](./README.md)
- 查看测试指南: [MINIMAL_PROTOTYPE.md](./MINIMAL_PROTOTYPE.md)
- 查看示例代码: [example_usage.py](./example_usage.py)

