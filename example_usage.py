"""使用示例"""

from pathlib import Path
from framework.core import AutoPackageFramework

# 示例1: 基本使用
def example_basic():
    """基本使用示例"""
    # 初始化框架（需要config.yaml或环境变量）
    framework = AutoPackageFramework(config_path="config.yaml")

    # 创建包
    result = framework.create_package(
        project_name="my-awesome-package",
        project_idea="""
        一个用于自动化任务调度的Python包。
        
        核心功能:
        - 支持定时任务
        - 支持任务依赖管理
        - 提供简单的API接口
        """,
        github_repo="my-awesome-package",
        auto_publish=False,  # 首次测试时不发布
    )

    print(f"创建结果: {result}")


# 示例2: 仅生成项目（不发布）
def example_generate_only():
    """仅生成项目示例"""
    framework = AutoPackageFramework(config_path="config.yaml")

    result = framework.create_package(
        project_name="test-package",
        project_idea="一个简单的工具包",
        # 不指定github_repo，不会创建GitHub仓库
        # auto_publish=False，不会发布
    )

    print(f"项目已生成到: {result.get('project_path')}")


# 示例3: 完整流程（生成+GitHub+PyPI）
def example_full_workflow():
    """完整工作流示例"""
    framework = AutoPackageFramework(config_path="config.yaml")

    result = framework.create_package(
        project_name="production-package",
        project_idea="""
        生产环境使用的包。
        
        功能:
        - 核心业务逻辑
        - 数据验证
        - 错误处理
        """,
        github_repo="production-package",
        auto_publish=True,  # 自动发布到PyPI
        replacements={
            "USERNAME": "your_github_username",
            "email": "your.email@example.com",
            "author": "Your Name",
        },
    )

    if result["success"]:
        print("✅ 项目创建并发布成功！")
        print(f"📁 路径: {result.get('project_path')}")
        print(f"🔗 GitHub: {result.get('github_repo')}")
        if result.get("pypi_published"):
            print("📦 已发布到PyPI")
    else:
        print("❌ 失败:")
        for error in result.get("errors", []):
            print(f"  - {error}")


if __name__ == "__main__":
    print("运行示例...")
    print("\n注意: 需要先配置config.yaml或环境变量")
    print("请查看README.md了解配置方法\n")

    # 取消注释以运行示例
    # example_basic()
    # example_generate_only()
    # example_full_workflow()

