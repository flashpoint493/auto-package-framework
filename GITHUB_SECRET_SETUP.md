# GitHub Secret 配置指南

本指南说明如何在 GitHub 仓库中配置 `PYPI_API_TOKEN`，以便 GitHub Actions 能够自动发布到 PyPI。

## 📍 快速链接

**直接访问设置页面**：
https://github.com/flashpoint493/auto-package-framework/settings/secrets/actions

## 🔧 详细步骤

### 步骤 1: 获取 PyPI API Token

1. **访问 PyPI Token 管理页面**
   - 链接：https://pypi.org/manage/account/token/
   - 需要先登录 PyPI 账户

2. **创建新的 API Token**
   - 点击页面上的 **"Add API token"** 按钮
   - 填写 Token 名称（例如：`auto-package-framework-github-actions`）

3. **选择 Token 作用域**
   - **项目级别**（推荐，更安全）：
     - 选择项目：`auto-package-framework`
     - 只能用于发布这个特定项目
   - **账户级别**（如果发布多个项目）：
     - 选择 "Entire account"
     - 可以用于发布所有项目

4. **复制 Token**
   - 点击 "Add token" 后，会显示生成的 token
   - **重要**：Token 只显示一次，请立即复制保存
   - Token 格式：`pypi-xxxxx...`（以 `pypi-` 开头）

### 步骤 2: 添加 GitHub Secret

#### 方法 1: 通过网页界面（推荐）

1. **打开仓库设置**
   - 访问：https://github.com/flashpoint493/auto-package-framework
   - 点击仓库页面顶部的 **"Settings"** 标签

2. **进入 Secrets 设置**
   - 在左侧菜单中找到 **"Secrets and variables"**
   - 展开后点击 **"Actions"**

3. **添加新的 Secret**
   - 点击页面右上角的 **"New repository secret"** 按钮
   - 填写以下信息：
     - **Name**: `PYPI_API_TOKEN`（必须完全一致，区分大小写）
     - **Secret**: 粘贴刚才复制的 PyPI API Token（`pypi-xxxxx...`）
   - 点击 **"Add secret"** 保存

4. **验证**
   - 在 Secrets 列表中应该能看到 `PYPI_API_TOKEN`
   - 注意：Secret 的值会被隐藏，只显示 `***`

#### 方法 2: 通过 GitHub CLI（高级用户）

如果你安装了 GitHub CLI (`gh`)，可以使用命令行：

```bash
# 登录 GitHub CLI（如果还没登录）
gh auth login

# 设置 Secret
gh secret set PYPI_API_TOKEN --repo flashpoint493/auto-package-framework
# 然后粘贴你的 PyPI token
```

### 步骤 3: 验证配置

1. **检查 Workflow 文件**
   - 确认 `.github/workflows/release.yml` 中有以下配置：
   ```yaml
   env:
     TWINE_USERNAME: __token__
     TWINE_PASSWORD: ${{ secrets.PYPI_API_TOKEN }}
   ```

2. **测试自动发布**
   - 创建一个新的 tag 并推送：
   ```bash
   git tag v0.2.1
   git push origin v0.2.1
   ```
   - 或者手动触发 workflow：
     - 访问：https://github.com/flashpoint493/auto-package-framework/actions/workflows/release.yml
     - 点击 "Run workflow"

3. **查看 Workflow 运行结果**
   - 访问：https://github.com/flashpoint493/auto-package-framework/actions
   - 查看 "Release" workflow 的运行状态
   - 如果成功，应该能看到 "Publish to PyPI" 步骤成功

## 🔒 安全注意事项

### ✅ 最佳实践

1. **使用项目级别 Token**
   - 只给必要的权限
   - 如果 Token 泄露，影响范围更小

2. **定期轮换 Token**
   - 建议每 6-12 个月更换一次
   - 在 PyPI 上删除旧 Token，创建新 Token，然后更新 GitHub Secret

3. **不要分享 Token**
   - 永远不要将 Token 提交到代码库
   - 不要在公开场合分享 Token
   - 如果 Token 泄露，立即删除并创建新的

4. **使用最小权限原则**
   - 只给 Token 必要的权限
   - 项目级别 Token 比账户级别更安全

### ❌ 常见错误

1. **Secret 名称错误**
   - ❌ 错误：`PYPI_TOKEN`、`pypi_api_token`、`PYPI-API-TOKEN`
   - ✅ 正确：`PYPI_API_TOKEN`（必须完全一致）

2. **Token 格式错误**
   - ❌ 错误：只复制了部分 token
   - ✅ 正确：完整的 token（以 `pypi-` 开头）

3. **在代码中硬编码**
   - ❌ 错误：在 workflow 文件中直接写 token
   - ✅ 正确：使用 `${{ secrets.PYPI_API_TOKEN }}`

## 📋 检查清单

配置完成后，确认：

- [ ] 已在 PyPI 创建 API Token
- [ ] Token 已复制并保存（安全的地方）
- [ ] 已在 GitHub 添加 `PYPI_API_TOKEN` secret
- [ ] Secret 名称完全正确（区分大小写）
- [ ] Workflow 文件中正确引用了 secret
- [ ] 已测试自动发布流程

## 🔗 相关链接

- **GitHub Secrets 设置**：https://github.com/flashpoint493/auto-package-framework/settings/secrets/actions
- **PyPI Token 管理**：https://pypi.org/manage/account/token/
- **GitHub Actions**：https://github.com/flashpoint493/auto-package-framework/actions
- **Release Workflow**：https://github.com/flashpoint493/auto-package-framework/actions/workflows/release.yml

## 🆘 故障排查

### 问题 1: Workflow 显示 "Secret not found"

**原因**：Secret 名称不匹配或未正确配置

**解决**：
1. 检查 Secret 名称是否为 `PYPI_API_TOKEN`（完全一致）
2. 确认 Secret 已添加到正确的仓库
3. 检查 workflow 文件中的引用是否正确

### 问题 2: PyPI 发布失败，显示 403 错误

**原因**：Token 无效或权限不足

**解决**：
1. 检查 Token 是否完整（以 `pypi-` 开头）
2. 确认 Token 未过期
3. 如果是项目级别 Token，确认项目名称匹配：`auto-package-framework`

### 问题 3: Workflow 没有自动触发

**原因**：Tag 推送未触发 workflow 或 workflow 配置问题

**解决**：
1. 确认 tag 格式为 `v*`（例如：`v0.2.0`）
2. 检查 workflow 的触发条件：
   ```yaml
   on:
     push:
       tags:
         - 'v*'
   ```
3. 可以手动触发 workflow 进行测试

## 📝 示例 Workflow 配置

你的 `.github/workflows/release.yml` 应该包含：

```yaml
- name: Publish to PyPI
  env:
    TWINE_USERNAME: __token__
    TWINE_PASSWORD: ${{ secrets.PYPI_API_TOKEN }}
  run: python -m twine upload dist/*
```

---

**配置完成后，每次推送 `v*` 格式的 tag 时，GitHub Actions 会自动构建并发布到 PyPI！** 🚀

