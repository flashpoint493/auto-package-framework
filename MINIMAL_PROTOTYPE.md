# 最小原型测试指南

本文档说明如何测试Auto Package Framework的最小原型。

## 🎯 测试目标

验证框架能够：
1. ✅ 从模板生成项目结构
2. ✅ 使用AI生成代码
3. ✅ 创建GitHub仓库并推送代码
4. ✅ 构建并发布到PyPI

## 📋 前置条件

### 1. 安装依赖

```bash
cd auto_package_framework
pip install -e ".[dev]"
```

### 2. 配置凭据

创建 `config.yaml` (参考 `config.yaml.example`):

```yaml
github:
  username: your_github_username
  token: your_github_token

pypi:
  token: pypi-your_token

ai:
  provider: openai
  api_key: your_openai_key
  model: gpt-4

template_path: ../PROJECT_TEMPLATE
```

**或者使用环境变量**:

```bash
export GITHUB_TOKEN=ghp_xxxxx
export PYPI_TOKEN=pypi-xxxxx
export OPENAI_API_KEY=sk-xxxxx
```

### 3. 获取API凭据

#### GitHub Token
1. 访问: https://github.com/settings/tokens
2. 创建新的 Personal Access Token (classic)
3. 权限: 勾选 `repo` (完整仓库访问)

#### PyPI Token
1. 访问: https://pypi.org/manage/account/token/
2. 创建新的 API token
3. 复制token (格式: `pypi-xxxxx`)

#### OpenAI API Key
1. 访问: https://platform.openai.com/api-keys
2. 创建新的API key
3. 确保账户有余额

## 🧪 测试步骤

### 测试1: 仅生成项目（不发布）

这是最安全的测试，不会创建GitHub仓库或发布到PyPI。

```python
from framework.core import AutoPackageFramework

framework = AutoPackageFramework(config_path="config.yaml")

result = framework.create_package(
    project_name="test-package-001",
    project_idea="一个简单的测试包，用于验证框架功能",
    # 不指定github_repo，不会创建GitHub仓库
    auto_publish=False,
)

print(result)
```

**预期结果**:
- ✅ 项目目录已创建
- ✅ 模板文件已复制并替换占位符
- ✅ PROJECT_IDEA.md已生成
- ✅ AI已生成初始代码（如果配置了AI）

### 测试2: 生成项目 + GitHub（不发布到PyPI）

```python
from framework.core import AutoPackageFramework

framework = AutoPackageFramework(config_path="config.yaml")

result = framework.create_package(
    project_name="test-package-002",
    project_idea="测试GitHub集成",
    github_repo="test-package-002",  # 指定仓库名
    auto_publish=False,  # 不发布到PyPI
)

print(result)
```

**预期结果**:
- ✅ 项目已生成
- ✅ GitHub仓库已创建
- ✅ 代码已推送到GitHub
- ✅ 可以在GitHub上看到仓库

### 测试3: 完整流程（生成+GitHub+PyPI）

⚠️ **注意**: 这会实际发布到PyPI，请使用测试项目名！

```python
from framework.core import AutoPackageFramework

framework = AutoPackageFramework(config_path="config.yaml")

result = framework.create_package(
    project_name="test-package-003",
    project_idea="完整流程测试",
    github_repo="test-package-003",
    auto_publish=True,  # 发布到PyPI
)

print(result)
```

**预期结果**:
- ✅ 所有上述步骤完成
- ✅ 包已构建
- ✅ 包已发布到PyPI
- ✅ 可以在PyPI上搜索到包

### 测试4: 使用CLI

```bash
# 仅生成项目
python -m framework.cli \
    --project-name "test-cli-001" \
    --idea "CLI测试项目"

# 生成 + GitHub
python -m framework.cli \
    --project-name "test-cli-002" \
    --idea "CLI GitHub测试" \
    --github-repo "test-cli-002"

# 完整流程
python -m framework.cli \
    --project-name "test-cli-003" \
    --idea "CLI完整测试" \
    --github-repo "test-cli-003" \
    --publish
```

## 🔍 验证检查清单

### 生成的项目检查

```bash
cd test-package-001

# 检查文件结构
ls -la
ls -la src/
ls -la tests/

# 检查代码质量
ruff check .
mypy . --ignore-missing-imports

# 运行测试
pytest
```

### GitHub仓库检查

1. 访问: https://github.com/your_username/test-package-002
2. 检查:
   - ✅ README.md存在
   - ✅ 代码已推送
   - ✅ PROJECT_IDEA.md存在
   - ✅ pyproject.toml配置正确

### PyPI发布检查

1. 访问: https://pypi.org/project/test-package-003/
2. 检查:
   - ✅ 包信息正确
   - ✅ 可以安装: `pip install test-package-003`

## 🐛 常见问题

### 1. GitHub Token无效

**错误**: `BadCredentialsException`

**解决**:
- 检查token是否正确
- 确认token有 `repo` 权限
- 确认token未过期

### 2. PyPI上传失败

**错误**: `HTTPError: 400 Client Error`

**解决**:
- 检查包名是否已存在（PyPI不允许重复）
- 使用TestPyPI测试: 修改代码使用 `publish_to_testpypi()`
- 检查token格式: 应该是 `pypi-xxxxx`

### 3. AI生成代码失败

**错误**: `APIError` 或超时

**解决**:
- 检查API key是否正确
- 确认账户有余额（OpenAI/Anthropic）
- 尝试使用更便宜的模型（如gpt-3.5-turbo）

### 4. 模板路径不存在

**错误**: `ValueError: 模板路径不存在`

**解决**:
- 检查 `config.yaml` 中的 `template_path`
- 确认 `PROJECT_TEMPLATE` 目录存在
- 使用绝对路径

## 📊 性能基准

在标准配置下的预期时间：

- **仅生成项目**: ~5-10秒
- **生成 + AI代码**: ~30-60秒（取决于AI响应时间）
- **生成 + GitHub**: ~10-20秒
- **完整流程**: ~60-120秒

## 🎉 成功标准

最小原型测试成功的标志：

1. ✅ 能够从模板生成项目
2. ✅ AI能够生成基本可用的代码
3. ✅ 能够自动创建GitHub仓库
4. ✅ 能够自动发布到PyPI
5. ✅ 生成的包可以通过pip安装
6. ✅ 生成的代码通过基本的lint检查

## 🚀 下一步

测试成功后，可以：

1. 优化AI提示词，提高代码质量
2. 添加更多模板选项
3. 支持批量创建
4. 添加项目监控功能
5. 集成更多AI提供商

