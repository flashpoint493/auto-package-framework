# 手动发布到 PyPI 的 PowerShell 脚本
# 使用方法: .\scripts\publish_pypi.ps1

Write-Host "🚀 开始手动发布到 PyPI..." -ForegroundColor Green

# 检查环境变量
if (-not $env:PYPI_TOKEN) {
    Write-Host "❌ 错误: 未设置 PYPI_TOKEN 环境变量" -ForegroundColor Red
    Write-Host "请先设置: `$env:PYPI_TOKEN='pypi-你的token'" -ForegroundColor Yellow
    exit 1
}

# 检查构建文件
if (-not (Test-Path "dist\auto_package_framework-0.2.0-py3-none-any.whl")) {
    Write-Host "📦 构建包..." -ForegroundColor Yellow
    python -m build
    if ($LASTEXITCODE -ne 0) {
        Write-Host "❌ 构建失败" -ForegroundColor Red
        exit 1
    }
}

# 检查包
Write-Host "🔍 检查包..." -ForegroundColor Yellow
python -m twine check dist\auto_package_framework-0.2.0*
if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ 包检查失败" -ForegroundColor Red
    exit 1
}

# 发布到 PyPI
Write-Host "📤 发布到 PyPI..." -ForegroundColor Yellow
$env:TWINE_USERNAME = "__token__"
$env:TWINE_PASSWORD = $env:PYPI_TOKEN

python -m twine upload dist\auto_package_framework-0.2.0*
if ($LASTEXITCODE -eq 0) {
    Write-Host "✅ 发布成功！" -ForegroundColor Green
    Write-Host "🔗 查看: https://pypi.org/project/auto-package-framework/" -ForegroundColor Cyan
} else {
    Write-Host "❌ 发布失败" -ForegroundColor Red
    exit 1
}

