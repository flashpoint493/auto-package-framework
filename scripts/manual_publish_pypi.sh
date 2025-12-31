#!/bin/bash
# 手动发布到 PyPI 的 Bash 脚本
# 使用方法: bash scripts/manual_publish_pypi.sh

set -e

echo "🚀 开始手动发布到 PyPI..."

# 检查环境变量
if [ -z "$PYPI_TOKEN" ]; then
    echo "❌ 错误: 未设置 PYPI_TOKEN 环境变量"
    echo "请先设置: export PYPI_TOKEN='pypi-你的token'"
    exit 1
fi

# 检查构建文件
if [ ! -f "dist/auto_package_framework-0.2.0-py3-none-any.whl" ]; then
    echo "📦 构建包..."
    python -m build
fi

# 检查包
echo "🔍 检查包..."
python -m twine check dist/auto_package_framework-0.2.0*

# 发布到 PyPI
echo "📤 发布到 PyPI..."
export TWINE_USERNAME="__token__"
export TWINE_PASSWORD="$PYPI_TOKEN"

python -m twine upload dist/auto_package_framework-0.2.0*

if [ $? -eq 0 ]; then
    echo "✅ 发布成功！"
    echo "🔗 查看: https://pypi.org/project/auto-package-framework/"
else
    echo "❌ 发布失败"
    exit 1
fi

