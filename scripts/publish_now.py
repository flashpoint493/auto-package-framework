"""立即发布脚本 - 使用框架自己发布自己"""

import os
import sys
from pathlib import Path

# 设置UTF-8编码（Windows兼容）
if sys.platform == "win32":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

# 添加src到路径
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from framework.config import Config
from framework.github_client import GitHubClient
from framework.pypi_client import PyPIClient
from git import Repo

def main():
    """执行发布流程"""
    print("🚀 开始发布 auto-package-framework...")
    
    # 加载配置
    config = Config()
    project_path = Path(__file__).parent.parent
    
    # 检查环境变量
    github_token = config.github_token
    pypi_token = config.pypi_token
    
    if not github_token:
        print("❌ 错误: 未找到 GITHUB_TOKEN 环境变量")
        return 1
    
    if not pypi_token:
        print("❌ 错误: 未找到 PYPI_TOKEN 环境变量")
        return 1
    
    print("✅ 已找到API凭据")
    
    # 步骤1: 创建GitHub仓库
    print("\n📦 步骤1: 创建GitHub仓库...")
    try:
        github_client = GitHubClient(token=github_token, username=config.github_username)
        
        repo_name = "auto-package-framework"
        
        # 检查仓库是否已存在
        if github_client.repository_exists(repo_name):
            print(f"⚠️  仓库 {repo_name} 已存在，跳过创建")
        else:
            repo = github_client.create_repository(
                name=repo_name,
                description="AI驱动的自动化Python包创建、开发和发布框架",
                private=False,
                auto_init=False,
            )
            print(f"✅ 已创建GitHub仓库: {repo.html_url}")
    except Exception as e:
        print(f"❌ 创建GitHub仓库失败: {e}")
        return 1
    
    # 步骤2: 推送代码到GitHub
    print("\n📤 步骤2: 推送代码到GitHub...")
    try:
        # 获取GitHub用户名
        github_username = config.github_username
        if not github_username:
            # 从GitHub API获取
            github_client_temp = GitHubClient(token=github_token)
            github_username = github_client_temp.username
            print(f"ℹ️  从GitHub API获取用户名: {github_username}")
        
        repo = Repo(project_path)
        
        # 检查是否已有远程仓库
        if "origin" not in [remote.name for remote in repo.remotes]:
            remote_url = f"https://{github_token}@github.com/{github_username}/{repo_name}.git"
            repo.create_remote("origin", remote_url)
            print("✅ 已添加远程仓库")
        else:
            # 更新远程URL
            origin = repo.remotes.origin
            origin.set_url(f"https://{github_token}@github.com/{github_username}/{repo_name}.git")
            print("✅ 已更新远程仓库URL")
        
        # 确保在main分支
        current_branch = repo.active_branch.name
        if current_branch != "main":
            if "main" in [head.name for head in repo.heads]:
                repo.git.checkout("main")
            else:
                repo.git.checkout("-b", "main")
        
        # 推送代码
        repo.git.push("origin", "main", force=False)
        print("✅ 代码已推送到GitHub")
    except Exception as e:
        print(f"❌ 推送代码失败: {e}")
        print("⚠️  继续执行后续步骤...")
    
    # 步骤3: 构建包
    print("\n🔨 步骤3: 构建包...")
    try:
        import subprocess
        result = subprocess.run(
            [sys.executable, "-m", "build"],
            cwd=project_path,
            capture_output=True,
            text=True,
        )
        if result.returncode != 0:
            print(f"❌ 构建失败: {result.stderr}")
            return 1
        print("✅ 包构建成功")
    except Exception as e:
        print(f"❌ 构建失败: {e}")
        return 1
    
    # 步骤4: 发布到PyPI
    print("\n📦 步骤4: 发布到PyPI...")
    try:
        pypi_client = PyPIClient(token=pypi_token)
        pypi_client.publish(project_path, repository="pypi", skip_build=True)
        print("✅ 已发布到PyPI")
    except Exception as e:
        print(f"❌ 发布到PyPI失败: {e}")
        return 1
    
    # 步骤5: 创建Git标签
    print("\n🏷️  步骤5: 创建Git标签...")
    try:
        repo = Repo(project_path)
        version = "0.1.0"
        tag_name = f"v{version}"
        
        # 检查标签是否已存在
        if tag_name in [tag.name for tag in repo.tags]:
            print(f"⚠️  标签 {tag_name} 已存在，跳过创建")
        else:
            repo.create_tag(tag_name, message=f"Release {tag_name}")
            print(f"✅ 已创建标签: {tag_name}")
        
        # 推送标签
        try:
            repo.git.push("origin", tag_name)
            print(f"✅ 标签已推送到GitHub")
        except Exception as e:
            print(f"⚠️  推送标签失败（可能已存在）: {e}")
    except Exception as e:
        print(f"⚠️  创建标签失败: {e}")
    
    print("\n✅ 发布流程完成！")
    print(f"📋 下一步: 在GitHub创建Release: https://github.com/{config.github_username}/{repo_name}/releases/new")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())

