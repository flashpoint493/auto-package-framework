# 徽章设置指南

本文档说明如何激活和配置README中的各种徽章。

## ✅ 已自动工作的徽章

以下徽章在文件创建后会自动工作（无需额外配置）：

- ✅ **PyPI Version**: 包发布到PyPI后自动显示
- ✅ **Python Versions**: 从PyPI自动获取
- ✅ **License**: 静态徽章，已配置
- ✅ **GitHub Stars**: 自动显示
- ✅ **GitHub Downloads**: 自动显示
- ✅ **Last Commit**: 自动显示
- ✅ **Commit Activity**: 自动显示
- ✅ **Open Issues/PRs**: 自动显示
- ✅ **Contributors**: 自动显示
- ✅ **Latest Release**: 创建Release后自动显示

## 🔧 需要配置的徽章

### 1. CI 徽章

**状态**: 已创建workflow文件，需要触发一次运行

**激活步骤**:
1. ✅ 已创建 `.github/workflows/ci.yml`
2. 推送代码到GitHub（已推送）
3. 等待workflow运行完成
4. 徽章会自动显示状态

**如果徽章仍为空**:
- 检查 [Actions页面](https://github.com/flashpoint493/auto-package-framework/actions)
- 确保workflow已运行至少一次
- 如果失败，修复错误后重新运行

### 2. Release 徽章

**状态**: 已创建workflow文件，需要触发一次运行

**激活步骤**:
1. ✅ 已创建 `.github/workflows/release.yml`
2. 创建第一个Release或推送tag
3. 等待workflow运行完成
4. 徽章会自动显示状态

**测试方法**:
```bash
# 创建测试tag
git tag v0.1.0
git push origin v0.1.0
```

### 3. Codecov 徽章

**状态**: 需要设置Codecov账户

**激活步骤**:

1. **注册Codecov账户**
   - 访问: https://codecov.io
   - 使用GitHub账号登录
   - 授权访问你的仓库

2. **添加仓库到Codecov**
   - 在Codecov dashboard中添加 `flashpoint493/auto-package-framework`
   - 获取仓库的Codecov token（如果需要）

3. **配置GitHub Secret（如果需要）**
   - 如果Codecov要求token，在GitHub仓库设置中添加：
     - Settings → Secrets and variables → Actions
     - 添加 `CODECOV_TOKEN`

4. **确保CI workflow上传覆盖率**
   - ✅ 已在 `ci.yml` 中配置了Codecov上传步骤
   - 覆盖率数据会在测试运行时自动上传

5. **等待首次运行**
   - 推送代码触发CI
   - 等待测试完成并上传覆盖率
   - 徽章会自动更新

**注意**: Codecov徽章可能需要几分钟才能显示数据。

### 4. Downloads 徽章 (pepy.tech)

**状态**: 需要包有下载记录

**激活步骤**:
1. 包已发布到PyPI ✅
2. 等待pepy.tech索引（可能需要几小时到几天）
3. 徽章会自动显示下载量

**如果徽章显示"not found"**:
- 这是正常的，pepy.tech需要时间索引新包
- 等待24-48小时后检查
- 或者手动访问 https://pepy.tech/project/auto-package-framework 查看

### 5. Pre-commit 徽章

**状态**: 需要配置pre-commit

**激活步骤**:
1. 创建 `.pre-commit-config.yaml` 文件
2. 安装pre-commit: `pip install pre-commit`
3. 安装hooks: `pre-commit install`
4. 徽章会自动显示为绿色

**如果不需要pre-commit**:
- 可以从README中移除这个徽章

## 🚀 快速激活所有徽章

### 步骤1: 触发CI运行

```bash
# 做一个小改动并推送
echo "# Test" >> README.md
git add README.md
git commit -m "chore: trigger CI"
git push origin main
```

### 步骤2: 设置Codecov

1. 访问 https://codecov.io
2. 登录并添加仓库
3. 等待CI运行并上传覆盖率

### 步骤3: 创建Release（可选）

```bash
# 创建tag
git tag v0.1.0
git push origin v0.1.0

# 或在GitHub网页创建Release
# https://github.com/flashpoint493/auto-package-framework/releases/new
```

## 📊 徽章状态检查清单

- [ ] CI徽章 - 等待workflow运行
- [ ] Release徽章 - 等待workflow运行或创建Release
- [ ] Codecov徽章 - 需要设置Codecov账户
- [ ] Downloads徽章 - 等待pepy.tech索引（可能需要1-2天）
- [x] PyPI Version - ✅ 已工作
- [x] Python Versions - ✅ 已工作
- [x] License - ✅ 已工作
- [x] GitHub Stars - ✅ 已工作

## 🔍 故障排除

### CI徽章显示"workflow does not exist"

**原因**: workflow文件路径错误或未提交

**解决**:
1. 检查 `.github/workflows/ci.yml` 是否存在
2. 确保文件已提交到GitHub
3. 检查文件名和路径是否正确

### Codecov徽章显示"unknown"

**原因**: 未设置Codecov或未上传覆盖率

**解决**:
1. 注册Codecov账户
2. 添加仓库
3. 确保CI workflow中上传了覆盖率数据

### Downloads徽章显示"not found"

**原因**: pepy.tech尚未索引你的包

**解决**:
- 这是正常的，等待1-2天
- 包需要有实际下载才会显示数字

## 📚 参考链接

- [GitHub Actions文档](https://docs.github.com/en/actions)
- [Codecov文档](https://docs.codecov.com/)
- [pepy.tech](https://pepy.tech/)
- [Shields.io徽章生成器](https://shields.io/)

