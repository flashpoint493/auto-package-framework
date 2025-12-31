# 迁移计划 - 多模式代码生成架构

## 📋 概述

本文档描述从当前单一 API 模式迁移到多模式代码生成架构的计划。

## 🎯 迁移目标

1. **保持向后兼容**：现有代码继续工作
2. **平滑过渡**：逐步迁移，不破坏现有功能
3. **功能增强**：添加 Cursor 模式和未来 Agent 模式支持

## 📅 迁移时间表

### Phase 1: 基础架构（v0.3.0）✅ 当前阶段

**目标**：建立抽象接口和基础实现

- [x] 创建 `CodeGenerator` 抽象接口
- [x] 实现 `CodeGeneratorFactory`
- [x] 实现 `CursorCodeGenerator` 基础版本
- [x] 更新 `Config` 支持代码生成模式配置
- [x] 更新 `Core` 使用新接口（保持向后兼容）
- [ ] 添加单元测试
- [ ] 更新文档

**状态**：进行中

### Phase 2: 完善 Cursor 模式（v0.4.0）

**目标**：完善 Cursor 代码生成功能

- [ ] 实现文件监控机制
- [ ] 添加超时处理
- [ ] 改进对话提示生成
- [ ] 添加进度反馈
- [ ] 完善错误处理
- [ ] 添加配置选项

### Phase 3: 迁移 API 实现（v0.4.1）

**目标**：将 AIDeveloper 迁移到 APICodeGenerator

- [ ] 重构 `AIDeveloper` → `APICodeGenerator`
- [ ] 保持 API 兼容性
- [ ] 更新所有引用
- [ ] 添加迁移测试
- [ ] 更新文档

### Phase 4: Agent 监督（v0.5.0）

**目标**：添加 Agent 监督机制

- [ ] 实现 `AgentSupervisor`
- [ ] 任务分解和依赖管理
- [ ] 基本的自动修复
- [ ] 进度监控
- [ ] 报告生成

### Phase 5: 完全自动化（v1.0.0）

**目标**：实现完全自动化的 Agent

- [ ] 实现 `AutonomousAgent`
- [ ] 持续改进机制
- [ ] 完整的监控系统
- [ ] 性能优化

## 🔄 迁移步骤

### 步骤 1: 添加新接口（已完成）

```python
# src/framework/code_generator.py
class CodeGenerator(ABC):
    @abstractmethod
    def generate_code(...) -> Dict[str, str]:
        pass
```

### 步骤 2: 实现 Cursor 生成器（已完成基础）

```python
class CursorCodeGenerator(CodeGenerator):
    def generate_code(...):
        # 创建对话文件
        # 等待用户完成
        # 收集生成的文件
```

### 步骤 3: 更新 Core（已完成）

```python
# core.py
def _generate_code(...):
    code_gen = self._get_code_generator(project_path)
    if code_gen:
        generated_files = code_gen.generate_code(...)
```

### 步骤 4: 配置支持（已完成）

```yaml
# config.yaml
code_generation:
  mode: "auto"  # 或 "api", "cursor"
  api: {...}
  cursor: {...}
```

### 步骤 5: 迁移 AIDeveloper（待完成）

```python
# 将 AIDeveloper 重构为 APICodeGenerator
class APICodeGenerator(CodeGenerator):
    # 从 AIDeveloper 迁移代码
```

## ⚠️ 向后兼容性

### 保持兼容的方式

1. **保留 AIDeveloper**：暂时保留，逐步迁移
2. **默认行为**：如果未配置新模式，使用旧的 AIDeveloper
3. **配置迁移**：自动检测旧配置并转换

### 兼容性检查清单

- [x] 现有代码可以继续使用 `AIDeveloper`
- [x] 新代码可以使用 `CodeGenerator` 接口
- [x] 配置向后兼容
- [ ] 文档更新
- [ ] 迁移指南

## 📝 使用示例

### 当前方式（向后兼容）

```python
from framework.core import AutoPackageFramework

framework = AutoPackageFramework()
# 仍然使用 AIDeveloper（如果配置了）
```

### 新方式（推荐）

```python
from framework.core import AutoPackageFramework

framework = AutoPackageFramework()
# 自动使用 CodeGenerator（根据配置选择模式）
```

### 指定模式

```yaml
# config.yaml
code_generation:
  mode: "cursor"  # 明确指定使用 Cursor 模式
```

## 🧪 测试计划

### 单元测试

- [ ] `CodeGenerator` 接口测试
- [ ] `CursorCodeGenerator` 测试
- [ ] `APICodeGenerator` 测试（迁移后）
- [ ] `CodeGeneratorFactory` 测试

### 集成测试

- [ ] 完整工作流测试（API 模式）
- [ ] 完整工作流测试（Cursor 模式）
- [ ] 模式切换测试
- [ ] 向后兼容性测试

## 📚 文档更新

- [x] 架构设计文档
- [ ] 迁移指南
- [ ] API 文档更新
- [ ] 使用示例
- [ ] 配置说明

## 🔗 相关文档

- [架构设计文档](./ARCHITECTURE_DESIGN.md)
- [Cursor Skill 实现方案](./CURSOR_SKILL_PROPOSAL.md)

---

**最后更新**: 2024-12
**状态**: Phase 1 进行中
**维护者**: Auto Package Framework Team

