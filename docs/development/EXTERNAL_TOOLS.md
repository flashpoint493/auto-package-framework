# 所需外部工具和API

本文档列出了Auto Package Framework所需的外部工具、库和API服务。

## 🔧 必需工具

### 1. GitHub API

**用途**: 创建仓库、提交代码、创建Release

**库选择**:
- **推荐**: `PyGithub` (https://github.com/PyGithub/PyGithub)
  - 安装: `pip install PyGithub`
  - 文档完善，使用简单
  - 支持所有GitHub API功能

**认证方式**:
1. **Personal Access Token (推荐)**
   - 创建: GitHub Settings → Developer settings → Personal access tokens → Tokens (classic)
   - 所需权限:
     - `repo` (完整仓库访问)
     - `workflow` (如果需要管理Actions)
   - 安全: 使用环境变量 `GITHUB_TOKEN` 存储

2. **OAuth App** (高级用法)
   - 适合需要用户授权的场景

**API限制**:
- 认证请求: 5000次/小时
- 未认证请求: 60次/小时

### 2. PyPI API

**用途**: 构建和上传Python包

**库选择**:
- **build**: `pip install build` - 构建包（生成wheel和sdist）
- **twine**: `pip install twine` - 上传包到PyPI

**认证方式**:
1. **API Token (强烈推荐)**
   - 创建: PyPI Account Settings → API tokens
   - 格式: `pypi-xxxxx`
   - 使用: `TWINE_USERNAME=__token__` + `TWINE_PASSWORD=pypi-xxxxx`
   - 安全: 可以设置作用域（只允许特定项目）

2. **用户名+密码** (不推荐)
   - 安全性较低
   - 需要启用2FA时可能有问题

**测试环境**:
- TestPyPI: https://test.pypi.org
- 用于测试发布流程

### 3. AI代码生成

**用途**: 根据项目想法自动生成代码

**选项1: OpenAI API**

- **库**: `openai` (官方SDK)
  - 安装: `pip install openai>=1.0.0`
- **模型推荐**:
  - `gpt-4`: 最佳代码质量，较慢
  - `gpt-4-turbo`: 平衡质量和速度
  - `gpt-3.5-turbo`: 快速，质量可接受
- **认证**: API Key
  - 获取: https://platform.openai.com/api-keys
  - 环境变量: `OPENAI_API_KEY`
- **定价**: 按token计费，gpt-4较贵

**选项2: Anthropic API**

- **库**: `anthropic` (官方SDK)
  - 安装: `pip install anthropic>=0.18.0`
- **模型推荐**:
  - `claude-3-opus-20240229`: 最佳质量
  - `claude-3-sonnet-20240229`: 平衡选择
  - `claude-3-haiku-20240307`: 快速
- **认证**: API Key
  - 获取: https://console.anthropic.com/
  - 环境变量: `ANTHROPIC_API_KEY`
- **定价**: 按token计费

**选项3: 本地模型** (高级)

- 使用 `ollama`, `llama.cpp` 等
- 需要额外集成代码
- 无API费用，但需要本地资源

### 4. Git操作

**用途**: 本地Git仓库管理

**库选择**:
- **GitPython**: `pip install GitPython>=3.1.40`
  - 功能完整
  - 文档: https://gitpython.readthedocs.io/

**功能**:
- 初始化仓库
- 添加文件
- 提交更改
- 推送到远程

## 📦 辅助工具

### 5. 配置文件处理

- **PyYAML**: `pip install pyyaml>=6.0`
  - 解析YAML配置文件

- **python-dotenv**: `pip install python-dotenv>=1.0.0`
  - 加载 `.env` 文件中的环境变量

### 6. 模板渲染

- **Jinja2**: `pip install jinja2>=3.1.2`
  - 模板文件处理（如果需要动态模板）

### 7. CLI框架

- **Click**: `pip install click>=8.1.7`
  - 命令行接口框架
  - 或使用 **Typer** (基于类型提示)

## 🔒 安全最佳实践

### 凭据管理

1. **使用环境变量**
   ```bash
   export GITHUB_TOKEN=ghp_xxxxx
   export OPENAI_API_KEY=sk-xxxxx
   export PYPI_TOKEN=pypi-xxxxx
   ```

2. **使用 `.env` 文件** (添加到.gitignore)
   ```
   GITHUB_TOKEN=ghp_xxxxx
   OPENAI_API_KEY=sk-xxxxx
   PYPI_TOKEN=pypi-xxxxx
   ```

3. **使用密钥管理服务** (生产环境)
   - AWS Secrets Manager
   - HashiCorp Vault
   - Azure Key Vault

### Token权限

- **GitHub Token**: 最小权限原则，只授予必要的 `repo` 权限
- **PyPI Token**: 使用项目级别的token，而不是账户级别
- **AI API Key**: 设置使用限额和监控

## 📊 成本估算

### GitHub API
- **免费**: 个人账户有足够的API限额
- **限制**: 5000次/小时（认证后）

### PyPI
- **免费**: 完全免费
- **限制**: 无硬性限制，但建议合理使用

### AI API (示例，实际价格请查看官网)

**OpenAI**:
- GPT-4: ~$0.03/1K输入tokens, ~$0.06/1K输出tokens
- GPT-3.5-turbo: ~$0.0015/1K输入tokens, ~$0.002/1K输出tokens

**Anthropic**:
- Claude 3 Opus: ~$0.015/1K输入tokens, ~$0.075/1K输出tokens
- Claude 3 Sonnet: ~$0.003/1K输入tokens, ~$0.015/1K输出tokens

**估算**: 生成一个简单Python包（~500行代码）约需 $0.10-0.50

## 🚀 快速设置

### 1. 安装依赖

```bash
cd auto_package_framework
pip install -e ".[dev]"
```

### 2. 配置凭据

创建 `config.yaml`:
```yaml
github:
  token: ${GITHUB_TOKEN}  # 或直接写token

pypi:
  token: ${PYPI_TOKEN}

ai:
  provider: openai
  api_key: ${OPENAI_API_KEY}
  model: gpt-4
```

或使用环境变量:
```bash
export GITHUB_TOKEN=ghp_xxxxx
export PYPI_TOKEN=pypi-xxxxx
export OPENAI_API_KEY=sk-xxxxx
```

### 3. 测试连接

```python
from framework.core import AutoPackageFramework

framework = AutoPackageFramework()
# 如果配置正确，各个客户端应该已初始化
```

## 📚 参考资源

- [GitHub API文档](https://docs.github.com/en/rest)
- [PyPI上传指南](https://packaging.python.org/en/latest/guides/distributing-packages-using-setuptools/)
- [OpenAI API文档](https://platform.openai.com/docs)
- [Anthropic API文档](https://docs.anthropic.com/)
- [GitPython文档](https://gitpython.readthedocs.io/)

