# 贡献指南

感谢你考虑为纷享开发助手项目做出贡献！

## 行为准则

本项目采用开放、包容的社区准则。请尊重所有贡献者，营造友好的协作环境。

## 如何贡献

### 报告 Bug

1. 在 [Issues](../../issues) 中搜索是否已存在相同问题
2. 如果没有，创建新 Issue，包含以下信息：
   - 清晰的标题和描述
   - 复现步骤
   - 期望行为和实际行为
   - 环境信息（Python 版本、操作系统等）
   - 相关日志或截图

### 提交功能请求

1. 在 [Issues](../../issues) 中搜索是否已有类似请求
2. 创建新 Issue，描述：
   - 功能的使用场景
   - 预期的实现方式
   - 可能的替代方案

### 提交代码

1. Fork 本仓库
2. 创建功能分支
   ```bash
   git checkout -b feature/amazing-feature
   ```
3. 进行修改并测试
4. 提交更改
   ```bash
   git commit -m 'feat: 添加某某功能'
   ```
5. 推送到分支
   ```bash
   git push origin feature/amazing-feature
   ```
6. 创建 Pull Request

## 开发环境

### 前置要求

- Python >= 3.8
- pip 包管理器

### 安装依赖

```bash
pip install scikit-learn numpy
```

### 运行测试

```bash
python api_doc_helper.py
```

## 代码风格

### Python 代码规范

- 遵循 [PEP 8](https://pep8.org/) 编码规范
- 使用 4 个空格缩进
- 函数和变量使用 snake_case 命名
- 类使用 PascalCase 命名
- 添加必要的文档字符串（docstring）

### 文档规范

- 使用 Markdown 格式
- 中文文档使用简体中文
- 代码示例必须符合纷享 APL 语法限制
- 保持文档简洁清晰

## 提交信息规范

使用 Conventional Commits 规范：

```
<type>(<scope>): <subject>

<body>

<footer>
```

### Type 类型

- `feat:` 新功能
- `fix:` Bug 修复
- `docs:` 文档更新
- `style:` 代码格式调整（不影响功能）
- `refactor:` 代码重构
- `test:` 测试相关
- `chore:` 构建/工具相关

### 示例

```
feat(api): 添加批量查询 API 支持

- 新增 batchFind 方法
- 支持分页查询
- 添加相关测试用例

Closes #123
```

## Pull Request 检查清单

提交 PR 前，请确认：

- [ ] 代码通过所有测试
- [ ] 代码符合 PEP 8 规范
- [ ] 更新了相关文档
- [ ] 提交信息清晰规范
- [ ] 没有引入新的敏感信息

## 文档贡献

### 完善 API 文档

1. 文档位于 `Api_Documentation_Markdown/pages/func-apl/` 目录
2. 遵循现有文档格式
3. 确保代码示例可运行
4. 标注语法限制

### 翻译文档

欢迎将文档翻译成其他语言：
- 在项目根目录创建 `docs/<language>/` 目录
- 保持原文档结构
- 在 README 中添加语言链接

## 问题反馈

如有任何问题，可以通过以下方式联系：

- 创建 [Issue](../../issues)
- 发送邮件至 locc233@163.com

## 许可证

通过贡献代码，你同意你的代码将按照 [GPL v3](LICENSE) 许可证开源。

---

再次感谢你的贡献！🎉
