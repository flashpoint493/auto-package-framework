# 架构设计文档 - 多模式代码生成与 Agent 监督

## 📋 概述

本文档描述 `auto-package-framework` 的架构设计，特别是代码生成模块的多模式支持和未来的 Agent 自动监督机制。

## 🎯 设计目标

1. **多模式代码生成**：支持 API 调用、Cursor IDE 对话、Agent 自动生成
2. **可扩展架构**：易于添加新的代码生成方式
3. **自动监督**：未来支持 Agent 自动完成和监督整个流程
4. **灵活配置**：用户可以选择不同的代码生成方式

## 🏗️ 架构设计

### 1. 核心抽象接口

```python
# 代码生成器抽象基类
class CodeGenerator(ABC):
    """代码生成器抽象接口"""
    
    @abstractmethod
    def generate_code(
        self,
        project_idea: str,
        project_structure: Dict[str, Any],
        existing_files: Optional[Dict[str, str]] = None,
    ) -> Dict[str, str]:
        """生成代码文件"""
        pass
    
    @abstractmethod
    def can_generate(self) -> bool:
        """检查是否可以生成代码"""
        pass
```

### 2. 实现类层次结构

```
CodeGenerator (抽象基类)
├── APICodeGenerator (当前实现)
│   ├── OpenAIGenerator
│   └── AnthropicGenerator
├── CursorCodeGenerator (新实现)
│   └── 通过 Cursor IDE 对话和 auto processed 模式
└── AgentCodeGenerator (未来实现)
    └── 完全自动化的 Agent 监督
```

### 3. 工作流编排器

```python
class WorkflowOrchestrator:
    """工作流编排器 - 协调各个组件"""
    
    def __init__(self):
        self.code_generator: Optional[CodeGenerator] = None
        self.supervisor: Optional[AgentSupervisor] = None
        self.executor: Optional[TaskExecutor] = None
```

### 4. Agent 监督机制（未来）

```python
class AgentSupervisor:
    """Agent 监督器 - 自动监督和完成所有任务"""
    
    def supervise_workflow(self, workflow: Workflow) -> WorkflowResult:
        """监督整个工作流"""
        pass
    
    def monitor_progress(self) -> ProgressStatus:
        """监控进度"""
        pass
    
    def auto_fix_issues(self, issue: Issue) -> FixResult:
        """自动修复问题"""
        pass
```

## 📐 详细设计

### 阶段 1: 多模式代码生成（当前 + 近期）

#### 1.1 重构 AIDeveloper 为 CodeGenerator 接口

**当前结构**：
```
AIDeveloper
├── generate_code() - 直接调用 API
└── _generate_with_openai/anthropic()
```

**新结构**：
```
CodeGenerator (接口)
├── APICodeGenerator
│   ├── OpenAIGenerator
│   └── AnthropicGenerator
└── CursorCodeGenerator
    ├── 通过 Cursor IDE API
    └── 使用 auto processed 模式
```

#### 1.2 CursorCodeGenerator 实现

**设计思路**：
- 利用 Cursor IDE 的 API 或文件系统监控
- 通过对话模式引导 AI 生成代码
- 使用 auto processed 模式自动处理

**实现方式**：
1. **文件监控模式**：监控项目目录，当检测到 `PROJECT_IDEA.md` 时触发
2. **API 模式**：如果 Cursor 提供 API，直接调用
3. **对话模式**：生成对话提示，引导用户在 Cursor 中完成

### 阶段 2: Agent 自动监督（中期）

#### 2.1 任务分解

将整个流程分解为可监督的任务：

```python
class Task:
    """任务抽象"""
    name: str
    status: TaskStatus  # pending, in_progress, completed, failed
    dependencies: List[Task]
    executor: TaskExecutor
    supervisor: AgentSupervisor
```

#### 2.2 监督机制

```python
class AgentSupervisor:
    """Agent 监督器"""
    
    def __init__(self):
        self.monitor = ProgressMonitor()
        self.executor = TaskExecutor()
        self.fixer = AutoFixer()
    
    def supervise(self, workflow: Workflow):
        """监督工作流执行"""
        for task in workflow.tasks:
            # 1. 检查前置条件
            if not self._check_prerequisites(task):
                self._wait_for_prerequisites(task)
            
            # 2. 执行任务
            result = self.executor.execute(task)
            
            # 3. 验证结果
            if not self._validate_result(result):
                # 4. 自动修复
                fix_result = self.fixer.fix(result)
                if not fix_result.success:
                    # 5. 人工介入
                    self._request_human_intervention(task)
```

### 阶段 3: 完全自动化（长期）

#### 3.1 自主 Agent

```python
class AutonomousAgent:
    """自主 Agent - 完全自动化"""
    
    def __init__(self):
        self.supervisor = AgentSupervisor()
        self.planner = WorkflowPlanner()
        self.executor = TaskExecutor()
        self.monitor = ProgressMonitor()
    
    def create_package_autonomously(
        self,
        project_idea: str,
        constraints: Dict[str, Any]
    ) -> PackageResult:
        """完全自主地创建包"""
        # 1. 规划工作流
        workflow = self.planner.plan(project_idea, constraints)
        
        # 2. 执行和监督
        result = self.supervisor.supervise(workflow)
        
        # 3. 持续监控和改进
        self.monitor.monitor(result)
        
        return result
```

#### 3.2 持续改进机制

```python
class ContinuousImprovement:
    """持续改进机制"""
    
    def learn_from_failures(self, failures: List[Failure]):
        """从失败中学习"""
        pass
    
    def optimize_workflow(self, workflow: Workflow) -> Workflow:
        """优化工作流"""
        pass
    
    def suggest_improvements(self) -> List[Improvement]:
        """建议改进"""
        pass
```

## 🔄 迁移路径

### 步骤 1: 抽象化当前实现（v0.3.0）

1. 创建 `CodeGenerator` 抽象基类
2. 将 `AIDeveloper` 重构为 `APICodeGenerator`
3. 更新 `core.py` 使用新的接口

### 步骤 2: 实现 Cursor 模式（v0.4.0）

1. 实现 `CursorCodeGenerator`
2. 添加配置选项选择代码生成方式
3. 更新文档和示例

### 步骤 3: 添加监督机制（v0.5.0）

1. 实现 `AgentSupervisor`
2. 添加任务分解和依赖管理
3. 实现基本的自动修复

### 步骤 4: 完全自动化（v1.0.0）

1. 实现 `AutonomousAgent`
2. 添加持续改进机制
3. 完整的监控和报告系统

## 📊 架构图

```
┌─────────────────────────────────────────────────────────┐
│                  AutoPackageFramework                    │
│                      (核心编排器)                        │
└──────────────────────┬──────────────────────────────────┘
                       │
        ┌──────────────┼──────────────┐
        │              │              │
┌───────▼──────┐ ┌────▼──────┐ ┌─────▼──────┐
│ Project      │ │ Code      │ │ GitHub    │
│ Generator    │ │ Generator │ │ Client    │
└──────────────┘ └────┬──────┘ └───────────┘
                       │
        ┌──────────────┼──────────────┐
        │              │              │
┌───────▼──────┐ ┌─────▼──────┐ ┌─────▼──────┐
│ API Code     │ │ Cursor     │ │ Agent      │
│ Generator    │ │ Generator  │ │ Generator  │
│ (当前)       │ │ (v0.4.0)  │ │ (v1.0.0)  │
└──────────────┘ └────────────┘ └─────┬──────┘
                                      │
                            ┌─────────▼─────────┐
                            │  Agent Supervisor │
                            │   (v0.5.0)        │
                            └───────────────────┘
```

## 🔧 实现细节

### CodeGenerator 接口设计

```python
from abc import ABC, abstractmethod
from typing import Dict, Any, Optional, List
from pathlib import Path

class CodeGenerator(ABC):
    """代码生成器抽象接口"""
    
    @abstractmethod
    def generate_code(
        self,
        project_idea: str,
        project_structure: Dict[str, Any],
        existing_files: Optional[Dict[str, str]] = None,
        context: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, str]:
        """
        生成代码文件
        
        Args:
            project_idea: 项目想法描述
            project_structure: 项目结构信息
            existing_files: 现有文件内容
            context: 额外上下文信息
            
        Returns:
            生成的代码文件字典 {文件路径: 代码内容}
        """
        pass
    
    @abstractmethod
    def can_generate(self) -> bool:
        """检查是否可以生成代码（检查环境、配置等）"""
        pass
    
    @abstractmethod
    def get_status(self) -> str:
        """获取生成器状态"""
        pass
    
    def validate_result(
        self,
        generated_files: Dict[str, str]
    ) -> Dict[str, Any]:
        """
        验证生成的结果
        
        Returns:
            验证结果字典，包含 errors 和 warnings
        """
        return {"errors": [], "warnings": []}
```

### CursorCodeGenerator 实现

```python
class CursorCodeGenerator(CodeGenerator):
    """通过 Cursor IDE 生成代码"""
    
    def __init__(self, project_path: Path):
        self.project_path = project_path
        self.cursor_api = CursorAPI()  # 如果 Cursor 提供 API
        self.file_monitor = FileMonitor(project_path)
    
    def generate_code(
        self,
        project_idea: str,
        project_structure: Dict[str, Any],
        existing_files: Optional[Dict[str, str]] = None,
        context: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, str]:
        """通过 Cursor IDE 生成代码"""
        
        # 方式1: 如果 Cursor 提供 API
        if self.cursor_api.available():
            return self._generate_via_api(project_idea, project_structure)
        
        # 方式2: 通过文件监控和对话
        return self._generate_via_dialogue(project_idea, project_structure)
    
    def _generate_via_dialogue(
        self,
        project_idea: str,
        project_structure: Dict[str, Any]
    ) -> Dict[str, str]:
        """通过对话模式生成代码"""
        
        # 1. 创建对话提示文件
        dialogue_file = self.project_path / ".cursor_dialogue.md"
        prompt = self._build_dialogue_prompt(project_idea, project_structure)
        dialogue_file.write_text(prompt, encoding="utf-8")
        
        # 2. 等待 Cursor 处理（监控文件变化）
        self.file_monitor.wait_for_changes(
            timeout=300,  # 5分钟超时
            pattern="src/**/*.py"
        )
        
        # 3. 读取生成的文件
        return self._collect_generated_files()
    
    def _build_dialogue_prompt(
        self,
        project_idea: str,
        project_structure: Dict[str, Any]
    ) -> str:
        """构建对话提示"""
        return f"""
# Cursor Auto Processed Mode

请根据以下项目想法生成代码：

## 项目想法
{project_idea}

## 项目结构
- 包名: {project_structure.get('package_name')}
- Python版本: {project_structure.get('python_version', '3.8+')}

## 需要生成的文件
1. src/{project_structure.get('package_name')}/__init__.py
2. src/{project_structure.get('package_name')}/main.py
3. tests/test_main.py

## 要求
- 遵循 PEP 8
- 包含类型注解和文档字符串
- 代码注释使用中文
- 代码使用英文
- 包含基本测试

请使用 auto processed 模式自动生成这些文件。
"""
```

## 🎯 配置设计

### config.yaml 扩展

```yaml
code_generation:
  # 代码生成方式: "api" | "cursor" | "agent" | "auto"
  mode: "auto"  # auto 会自动选择可用的方式
  
  # API 模式配置
  api:
    provider: "openai"  # 或 "anthropic"
    api_key: ${OPENAI_API_KEY}
    model: "gpt-4"
  
  # Cursor 模式配置
  cursor:
    enabled: true
    auto_processed: true
    dialogue_file: ".cursor_dialogue.md"
    timeout: 300  # 秒
  
  # Agent 模式配置（未来）
  agent:
    enabled: false
    supervisor: true
    auto_fix: true
    human_intervention: true
```

## 📝 实施计划

### Phase 1: 抽象化（v0.3.0）
- [ ] 创建 `CodeGenerator` 抽象接口
- [ ] 重构 `AIDeveloper` → `APICodeGenerator`
- [ ] 更新 `core.py` 使用新接口
- [ ] 添加配置选项

### Phase 2: Cursor 支持（v0.4.0）
- [ ] 实现 `CursorCodeGenerator`
- [ ] 添加文件监控机制
- [ ] 实现对话模式
- [ ] 文档和示例

### Phase 3: 监督机制（v0.5.0）
- [ ] 实现 `AgentSupervisor`
- [ ] 任务分解和依赖管理
- [ ] 基本的自动修复
- [ ] 进度监控

### Phase 4: 完全自动化（v1.0.0）
- [ ] 实现 `AutonomousAgent`
- [ ] 持续改进机制
- [ ] 完整的监控系统
- [ ] 性能优化

## 🔗 相关文档

- [Cursor Skill 实现方案](./CURSOR_SKILL_PROPOSAL.md)
- [外部工具说明](./EXTERNAL_TOOLS.md)
- [项目结构说明](../../PROJECT_STRUCTURE.md)

---

**最后更新**: 2024-12
**状态**: 设计阶段
**维护者**: Auto Package Framework Team

