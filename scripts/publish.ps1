# PowerShell 自动化发布脚本

param(
    [Parameter(Mandatory=$true)]
    [string]$Version
)

Write-Host "🚀 开始发布 v$Version" -ForegroundColor Green

# 检查环境变量
if (-not $env:PYPI_TOKEN) {
    Write-Host "❌ 错误: 未设置 PYPI_TOKEN 环境变量" -ForegroundColor Red
    Write-Host "请设置: `$env:PYPI_TOKEN='pypi-xxxxx'" -ForegroundColor Yellow
    exit 1
}

# 更新版本号
Write-Host "📝 更新版本号到 $Version" -ForegroundColor Cyan
$content = Get-Content pyproject.toml -Raw
$content = $content -replace 'version = ".*"', "version = `"$Version`""
Set-Content pyproject.toml -Value $content

# 清理旧的构建产物
Write-Host "🧹 清理旧的构建产物" -ForegroundColor Cyan
Remove-Item -Recurse -Force dist, build, *.egg-info -ErrorAction SilentlyContinue

# 构建
Write-Host "📦 构建包" -ForegroundColor Cyan
python -m build

# 检查构建产物
if (-not (Test-Path "dist/auto_package_framework-$Version.tar.gz")) {
    Write-Host "❌ 错误: 构建失败，未找到 dist/auto_package_framework-$Version.tar.gz" -ForegroundColor Red
    exit 1
}

# 发布到PyPI
Write-Host "📤 发布到PyPI" -ForegroundColor Cyan
$env:TWINE_USERNAME = "__token__"
$env:TWINE_PASSWORD = $env:PYPI_TOKEN
python -m twine upload dist/*

# 创建Git标签
Write-Host "🏷️  创建Git标签 v$Version" -ForegroundColor Cyan
git add pyproject.toml
git commit -m "chore: bump version to $Version" 2>$null
git tag -a "v$Version" -m "Release v$Version"
git push origin main 2>$null
git push origin "v$Version" 2>$null

Write-Host "✅ 发布完成: v$Version" -ForegroundColor Green
Write-Host "📋 下一步: 在GitHub创建Release" -ForegroundColor Yellow

