#!/usr/bin/env python3
"""
Auto Package Framework - Cursor Skill 脚本
用于在 Cursor 中创建 Python 包
"""

import sys
import os
import argparse
from pathlib import Path

# 尝试导入框架
try:
    from framework.core import AutoPackageFramework
    from framework.config import Config
except ImportError:
    print("❌ 错误: 未找到 auto-package-framework")
    print("请先安装: pip install auto-package-framework")
    sys.exit(1)


def check_credentials(config: Config, require_github: bool = False, require_pypi: bool = False):
    """检查必要的凭据"""
    missing = []
    
    if require_github and not config.github_token:
        missing.append("GITHUB_TOKEN (GitHub 集成需要)")
    
    if require_pypi and not config.pypi_token:
        missing.append("PYPI_TOKEN (PyPI 发布需要)")
    
    if missing:
        print("⚠️  缺少必要的环境变量:")
        for item in missing:
            print(f"   - {item}")
        print("\n请设置环境变量或创建 config.yaml 文件")
        return False
    
    return True


def main():
    """主函数"""
    parser = argparse.ArgumentParser(
        description="Auto Package Framework - 创建 Python 包"
    )
    parser.add_argument(
        "--name", "-n",
        required=True,
        help="项目名称"
    )
    parser.add_argument(
        "--idea", "-i",
        required=True,
        help="项目想法描述"
    )
    parser.add_argument(
        "--output", "-o",
        help="输出路径（默认：当前目录）"
    )
    parser.add_argument(
        "--github-repo", "-g",
        help="GitHub 仓库名称（如果为 None，使用项目名）"
    )
    parser.add_argument(
        "--publish", "-p",
        action="store_true",
        help="自动发布到 PyPI（需要确认）"
    )
    parser.add_argument(
        "--config", "-c",
        help="配置文件路径（默认：config.yaml）"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="预览模式，不实际执行"
    )
    
    args = parser.parse_args()
    
    # 初始化框架
    try:
        framework = AutoPackageFramework(config_path=args.config)
    except Exception as e:
        print(f"❌ 初始化框架失败: {e}")
        sys.exit(1)
    
    # 检查凭据
    require_github = bool(args.github_repo)
    require_pypi = args.publish
    
    if not check_credentials(framework.config, require_github, require_pypi):
        if not args.dry_run:
            sys.exit(1)
    
    # 确定输出路径
    output_path = Path(args.output) if args.output else Path.cwd() / args.name
    
    # 预览模式
    if args.dry_run:
        print("🔍 预览模式 - 将执行以下操作:")
        print(f"   项目名称: {args.name}")
        print(f"   输出路径: {output_path}")
        print(f"   项目想法: {args.idea}")
        if args.github_repo:
            print(f"   GitHub 仓库: {args.github_repo}")
        if args.publish:
            print(f"   PyPI 发布: 是（需要确认）")
        print("\n使用 --dry-run=false 来实际执行")
        return 0
    
    # 确认发布操作
    if args.publish:
        print("⚠️  警告: 即将发布到 PyPI")
        confirm = input("请确认是否继续 (yes/no): ")
        if confirm.lower() != "yes":
            print("❌ 已取消发布")
            args.publish = False
    
    # 执行创建
    print(f"🚀 开始创建项目: {args.name}")
    
    try:
        result = framework.create_package(
            project_name=args.name,
            project_idea=args.idea,
            output_path=output_path,
            github_repo=args.github_repo or args.name,
            auto_publish=args.publish,
        )
        
        if result["success"]:
            print("\n✅ 项目创建成功！")
            print(f"📁 项目路径: {result.get('project_path', 'N/A')}")
            
            if "github_repo" in result:
                print(f"🔗 GitHub: {result['github_repo']}")
            
            if result.get("pypi_published"):
                print("📦 已发布到 PyPI")
            
            print("\n📋 执行步骤:")
            for step in result.get("steps", []):
                print(f"   ✓ {step}")
        else:
            print("\n❌ 项目创建失败")
            for error in result.get("errors", []):
                print(f"   - {error}")
            sys.exit(1)
            
    except KeyboardInterrupt:
        print("\n\n⚠️  操作被用户中断")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ 发生错误: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()

