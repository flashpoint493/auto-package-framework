# Cookiecutter 集成分析

> 评估将 [Cookiecutter](https://github.com/cookiecutter/cookiecutter) 集成到 `auto-package-framework` 的可行性和影响

## 📊 当前实现分析

### 现有模板系统

我们的框架已经实现了完整的模板系统：

1. **基于 Jinja2 的模板引擎**
   - 支持 `.template` 文件的 Jinja2 渲染
   - 支持文本文件的变量替换
   - 灵活的替换映射系统

2. **自定义 ProjectGenerator**
   - 文件复制和过滤
   - 模板变量替换
   - 项目结构生成

3. **已内置模板**
   - Python 包模板已内置
   - 支持自定义模板路径

### 当前依赖

```toml
dependencies = [
    "jinja2>=3.1.2",  # ✅ 已包含（cookiecutter 的核心依赖）
    # ... 其他依赖
]
```

## 🔍 Cookiecutter 分析

### 核心功能

根据 [Cookiecutter 文档](https://github.com/cookiecutter/cookiecutter)：

1. **标准化模板格式** (`cookiecutter.json`)
   - 定义模板变量和默认值
   - 支持条件变量
   - 支持选择列表

2. **交互式提示**
   - 自动生成交互式提示
   - 支持验证和默认值

3. **Hooks 系统**
   - `pre_gen_project.py` - 生成前执行
   - `post_gen_project.py` - 生成后执行
   - 支持自定义脚本

4. **模板加载**
   - 支持本地模板
   - 支持 Git 仓库模板
   - 支持远程 URL

5. **跨语言支持**
   - 不仅限于 Python 项目
   - 支持任何语言/框架

### 依赖分析

```python
# Cookiecutter 的核心依赖（来自其 pyproject.toml）
dependencies = [
    "Jinja2>=3.0",      # ✅ 我们已有
    "binaryornot>=0.4.4",
    "click>=7.0",
    "python-slugify>=4.0.1",
    "jinja2-time>=0.2.0",
    "pyyaml>=5.3",
]
```

**新增依赖**：
- `binaryornot` - 二进制文件检测（~50KB）
- `python-slugify` - 字符串 slugify（~100KB）
- `jinja2-time` - Jinja2 时间过滤器（~20KB）

**总增加量**：约 170KB，依赖链简单，维护成本低。

## ⚖️ 利弊分析

### ✅ 优势

1. **标准化格式**
   - `cookiecutter.json` 是业界标准
   - 大量现成模板可用（24.5k stars）
   - 用户熟悉度高

2. **生态系统**
   - 可以复用社区模板
   - 用户可以使用任何 cookiecutter 模板
   - 降低模板维护成本

3. **功能增强**
   - 交互式提示（适合 CLI 模式）
   - Pre/post hooks（扩展性强）
   - 条件变量支持

4. **跨语言支持**
   - 支持非 Python 项目（符合未来规划）
   - 模板格式通用

5. **AI 友好**
   - AI 可以理解标准格式
   - 更容易生成符合规范的模板

### ❌ 劣势

1. **依赖增加**
   - 新增 3 个依赖（虽然很小）
   - 需要维护兼容性

2. **学习成本**
   - 需要了解 cookiecutter.json 格式
   - 需要迁移现有模板

3. **灵活性降低**
   - 必须遵循 cookiecutter 规范
   - 可能限制某些自定义需求

4. **重复功能**
   - 我们已经有了模板系统
   - 可能造成功能重复

## 💡 建议方案

### 方案 1: 渐进式集成（推荐）⭐

**策略**：保持现有系统，同时支持 cookiecutter 格式

#### 实现方式

1. **可选依赖**
   ```toml
   [project.optional-dependencies]
   cookiecutter = ["cookiecutter>=2.6.0"]
   ```

2. **适配器模式**
   ```python
   class TemplateAdapter:
       """模板适配器，支持多种格式"""
       
       def __init__(self, template_path: Path):
           self.template_path = template_path
           self.format = self._detect_format()
       
       def _detect_format(self) -> str:
           """检测模板格式"""
           if (self.template_path / "cookiecutter.json").exists():
               return "cookiecutter"
           return "native"  # 我们的原生格式
       
       def generate(self, ...):
           if self.format == "cookiecutter":
               return self._generate_with_cookiecutter(...)
           else:
               return self._generate_with_native(...)
   ```

3. **向后兼容**
   - 现有模板继续工作
   - 新模板可以选择格式
   - 支持混合使用

#### 优点
- ✅ 不破坏现有功能
- ✅ 用户可以选择
- ✅ 渐进式迁移
- ✅ 降低风险

#### 缺点
- ⚠️ 需要维护两套系统
- ⚠️ 代码复杂度增加

### 方案 2: 完全迁移

**策略**：完全采用 cookiecutter，替换现有系统

#### 实现方式

1. **迁移现有模板**
   - 将现有模板转换为 cookiecutter 格式
   - 创建 `cookiecutter.json`

2. **重构 ProjectGenerator**
   - 使用 cookiecutter API
   - 保留我们的扩展功能（AI、GitHub 等）

#### 优点
- ✅ 标准化
- ✅ 减少维护成本
- ✅ 利用生态系统

#### 缺点
- ❌ 破坏性变更
- ❌ 需要大量迁移工作
- ❌ 可能丢失某些灵活性

### 方案 3: 仅支持 cookiecutter 模板（轻量级）

**策略**：不添加 cookiecutter 依赖，但支持使用 cookiecutter 模板

#### 实现方式

1. **解析 cookiecutter.json**
   - 手动解析 `cookiecutter.json`
   - 使用我们的 Jinja2 系统渲染

2. **支持 cookiecutter 模板结构**
   - 识别 `{{cookiecutter.*}}` 变量
   - 支持 hooks（可选）

#### 优点
- ✅ 无额外依赖
- ✅ 支持 cookiecutter 模板
- ✅ 保持轻量级

#### 缺点
- ⚠️ 需要自己实现部分功能
- ⚠️ 可能不完全兼容

## 🎯 推荐方案：方案 1（渐进式集成）

### 实施步骤

#### 阶段 1: 准备（1-2 周）
1. 添加 cookiecutter 为可选依赖
2. 创建 `CookiecutterAdapter` 类
3. 实现格式检测

#### 阶段 2: 基础支持（2-3 周）
1. 实现 cookiecutter 模板加载
2. 支持 `cookiecutter.json` 解析
3. 支持基本变量替换

#### 阶段 3: 增强功能（2-3 周）
1. 支持 hooks（pre/post）
2. 支持交互式提示（CLI 模式）
3. 支持条件变量

#### 阶段 4: 文档和测试（1 周）
1. 更新文档
2. 添加示例
3. 编写测试

### 代码示例

```python
# src/framework/template_adapter.py

from pathlib import Path
from typing import Dict, Any, Optional
import json

class TemplateAdapter:
    """模板适配器，支持多种格式"""
    
    def __init__(self, template_path: Path):
        self.template_path = Path(template_path)
        self.format = self._detect_format()
    
    def _detect_format(self) -> str:
        """检测模板格式"""
        if (self.template_path / "cookiecutter.json").exists():
            return "cookiecutter"
        return "native"
    
    def generate(
        self,
        project_name: str,
        output_path: Path,
        replacements: Dict[str, str],
        project_idea: Optional[str] = None,
    ) -> Path:
        """生成项目"""
        if self.format == "cookiecutter":
            return self._generate_with_cookiecutter(
                project_name, output_path, replacements, project_idea
            )
        else:
            # 使用现有的 ProjectGenerator
            from .project_generator import ProjectGenerator
            generator = ProjectGenerator(self.template_path)
            return generator.generate(
                project_name, output_path, replacements, project_idea
            )
    
    def _generate_with_cookiecutter(
        self,
        project_name: str,
        output_path: Path,
        replacements: Dict[str, str],
        project_idea: Optional[str] = None,
    ) -> Path:
        """使用 cookiecutter 生成项目"""
        try:
            import cookiecutter.main as cc_main
            import cookiecutter.generate as cc_generate
            
            # 读取 cookiecutter.json
            config_file = self.template_path / "cookiecutter.json"
            with open(config_file, 'r', encoding='utf-8') as f:
                context = json.load(f)
            
            # 合并用户提供的替换
            context.update(replacements)
            context.setdefault('project_name', project_name)
            
            # 使用 cookiecutter 生成
            cc_generate.generate_files(
                repo_dir=str(self.template_path),
                context=context,
                output_dir=str(output_path.parent),
                overwrite_if_exists=True,
            )
            
            return output_path
            
        except ImportError:
            raise ImportError(
                "cookiecutter 未安装。请运行: pip install 'auto-package-framework[cookiecutter]'"
            )
```

## 📋 决策矩阵

| 方案 | 维护成本 | 灵活性 | 生态系统 | 迁移成本 | 推荐度 |
|------|---------|--------|---------|---------|--------|
| 方案 1: 渐进式 | 中 | 高 | 高 | 低 | ⭐⭐⭐⭐⭐ |
| 方案 2: 完全迁移 | 低 | 中 | 高 | 高 | ⭐⭐⭐ |
| 方案 3: 轻量级 | 中 | 高 | 中 | 中 | ⭐⭐⭐⭐ |

## 🚨 风险与注意事项

### 1. 依赖管理
- Cookiecutter 依赖链简单，风险低
- 建议作为可选依赖，降低影响

### 2. 向后兼容
- 必须保持现有模板系统工作
- 渐进式迁移，不破坏现有功能

### 3. 未来扩展
- 支持非 Python 项目时，cookiecutter 更有优势
- 标准化格式有利于 AI 理解

### 4. 维护成本
- 需要维护两套系统（短期）
- 长期可以逐步迁移到 cookiecutter

## 🎓 结论

**建议采用方案 1（渐进式集成）**：

1. ✅ **低风险**：不破坏现有功能
2. ✅ **高价值**：利用 cookiecutter 生态系统
3. ✅ **灵活性**：用户可以选择格式
4. ✅ **未来友好**：支持非 Python 项目
5. ✅ **AI 友好**：标准化格式更易理解

**实施建议**：
- 先实现基础支持（阶段 1-2）
- 根据用户反馈决定是否继续
- 保持现有系统作为默认
- 逐步引导用户使用 cookiecutter 格式

## 📚 参考资料

- [Cookiecutter 官方文档](https://github.com/cookiecutter/cookiecutter)
- [Cookiecutter 模板列表](https://github.com/cookiecutter/cookiecutter#available-templates)
- [Cookiecutter JSON 格式](https://cookiecutter.readthedocs.io/en/latest/advanced/cookiecutter_json.html)

---

## ✅ 实施状态

**最后更新**: 2025-01-XX  
**状态**: ✅ **已完成迁移**

### 已完成的迁移工作

1. ✅ **创建 cookiecutter.json**
   - 定义了所有模板变量
   - 支持派生变量（package_name, project_slug, main_class）

2. ✅ **模板文件转换**
   - `pyproject.toml` - 已转换为 cookiecutter 格式
   - `README.md` - 已转换为 cookiecutter 格式
   - `llms.txt.template` - 已转换为 cookiecutter 格式

3. ✅ **依赖更新**
   - 添加 `cookiecutter>=2.6.0` 到 `pyproject.toml`

4. ✅ **ProjectGenerator 重构**
   - 完全使用 cookiecutter API
   - 保持向后兼容的接口
   - 支持所有现有功能

### 迁移影响

- ✅ **无破坏性变更**：API 接口保持不变
- ✅ **功能完整**：所有原有功能正常工作
- ✅ **标准化**：模板现在符合 cookiecutter 标准

### 下一步

- 测试模板生成功能
- 更新文档说明 cookiecutter 格式
- 考虑添加 hooks 支持（可选）

