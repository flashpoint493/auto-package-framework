#!/bin/bash
# 自动化发布脚本

set -e

VERSION=$1
if [ -z "$VERSION" ]; then
    echo "用法: ./scripts/publish.sh <版本号>"
    echo "示例: ./scripts/publish.sh 0.1.0"
    exit 1
fi

echo "🚀 开始发布 v$VERSION"

# 检查环境变量
if [ -z "$PYPI_TOKEN" ]; then
    echo "❌ 错误: 未设置 PYPI_TOKEN 环境变量"
    echo "请设置: export PYPI_TOKEN=pypi-xxxxx"
    exit 1
fi

# 更新版本号
echo "📝 更新版本号到 $VERSION"
if [[ "$OSTYPE" == "darwin"* ]]; then
    # macOS
    sed -i '' "s/version = \".*\"/version = \"$VERSION\"/" pyproject.toml
else
    # Linux
    sed -i "s/version = \".*\"/version = \"$VERSION\"/" pyproject.toml
fi

# 清理旧的构建产物
echo "🧹 清理旧的构建产物"
rm -rf dist/ build/ *.egg-info

# 构建
echo "📦 构建包"
python -m build

# 检查构建产物
if [ ! -f "dist/auto_package_framework-$VERSION.tar.gz" ]; then
    echo "❌ 错误: 构建失败，未找到 dist/auto_package_framework-$VERSION.tar.gz"
    exit 1
fi

# 发布到PyPI
echo "📤 发布到PyPI"
python -m twine upload dist/*

# 创建Git标签
echo "🏷️  创建Git标签 v$VERSION"
git add pyproject.toml
git commit -m "chore: bump version to $VERSION" || true
git tag -a "v$VERSION" -m "Release v$VERSION"
git push origin main || echo "⚠️  警告: 推送main分支失败，请手动推送"
git push origin "v$VERSION" || echo "⚠️  警告: 推送标签失败，请手动推送"

echo "✅ 发布完成: v$VERSION"
echo "📋 下一步: 在GitHub创建Release: https://github.com/USERNAME/auto-package-framework/releases/new"

