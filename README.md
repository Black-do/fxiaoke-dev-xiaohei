# 纷享开发助手 Skill - 小黑

[![License](https://img.shields.io/badge/license-GPL%20v3-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.8%2B-brightgreen.svg)](https://www.python.org/)

> 智能 API 文档检索助手，为纷享 APL 开发者提供高效的文档查询和代码生成支持

## 功能特性

- **智能文档检索** - 基于向量搜索和关键词搜索的混合检索机制
- **代码示例生成** - 自动生成符合纷享 APL 语法规范的代码示例
- **语法限制提示** - 内置纷享 APL 语法限制，避免常见错误
- **离线文档支持** - 完整的本地 API 文档，无需联网即可使用

## 快速开始

### 安装依赖

```bash
pip install scikit-learn numpy
```

### 使用方法

本技能支持多个 AI 开发工具平台：

#### 支持的平台

| 平台 | 配置目录 | 说明 |
|------|---------|------|
| **Trae IDE** | `.trae/skills/` | 原生支持 |
| **Cursor** | `.cursor/skills/` | 需配置 skills 目录 |
| **Claude Desktop** | `~/.claude/skills/` | 支持 MCP 协议 |
| **VSCode + Copilot** | `.vscode/skills/` | 需安装扩展 |
| **其他 AI 工具** | 根据工具文档配置 | 支持自定义 skills |

#### 配置步骤

1. 将项目放置在对应平台的 skills 目录下
2. 在 AI 助手中询问关于纷享 API 的问题
3. Skill 会自动检索相关文档并提供帮助

**示例配置（Trae IDE）**：
```
.trae/
└── skills/
    └── fxiaoke-dev-xiaohei/
        ├── Api_Documentation_Markdown/
        ├── SKILL.md
        └── api_doc_helper.py
```

**示例配置（Cursor）**：
```
.cursor/
└── skills/
    └── fxiaoke-dev-xiaohei/
        ├── Api_Documentation_Markdown/
        ├── SKILL.md
        └── api_doc_helper.py
```

### 编程接口

```python
from api_doc_helper import search_api_docs, get_api_info

# 搜索 API 文档
results = search_api_docs('ObjectDataAPI')
for result in results['results']:
    print(f"{result['title']}: {result['relative_path']}")

# 获取特定 API 信息
api_info = get_api_info('ObjectDataAPI')
print(f"API: {api_info['title']}")
```

## 文档结构

```
fxiaoke-dev-xiaohei/
├── SKILL.md                        # Skill 定义文件
├── api_doc_helper.py               # 文档检索工具
├── Api_Documentation_Markdown/     # API 文档目录
│   ├── index.md
│   └── pages/func-apl/
│       ├── api/                    # API 模块文档
│       │   ├── ObjectDataAPI/      # 对象数据 API
│       │   ├── UserAPI/            # 用户 API
│       │   └── ...
│       ├── data-type/              # 数据类型文档
│       └── start/                  # 入门指南
├── LICENSE                         # GPL v3 许可证
├── README.md                       # 项目说明
└── CONTRIBUTING.md                 # 贡献指南
```

## 核心功能

### 1. API 文档检索

支持多种检索方式：
- 向量搜索（基于 TF-IDF）
- 关键词搜索
- 混合搜索（向量 + 关键词）

### 2. 语法限制提醒

纷享 APL 有严格的语法限制，Skill 会自动提醒：

```groovy
// ❌ 禁止使用
println, print, System.out.println
try-catch, throw, throws
for, while, do-while

// ✅ 必须使用
log.info("信息")
log.error("错误")
dataList.each { item -> }
```

### 3. 代码示例

提供符合规范的代码示例：

```groovy
// 查询对象数据
def (Boolean error, QueryResult result, String errorMessage) = Fx.object.find(
    'Account__c',
    FQLAttribute.builder()
        .columns(['_id', 'name', 'owner'])
        .queryTemplate(QueryTemplate.AND([:]))
        .limit(10)
        .build()
)

if (!error) {
    result.dataList.each { record ->
        log.info("记录: " + record.name)
    }
}
```

## 常用 API 参考

| API 类别 | 说明 | 文档路径 |
|---------|------|---------|
| ObjectDataAPI | 对象数据操作 | `pages/func-apl/api/ObjectDataAPI/` |
| UserAPI | 用户管理 | `pages/func-apl/api/UserAPI/` |
| OrganizationAPI | 组织架构 | `pages/func-apl/api/OrganizationAPI/` |
| MessageAPI | 消息通知 | `pages/func-apl/api/MessageAPI/` |
| FileAPI | 文件管理 | `pages/func-apl/api/FileAPI/` |

## 贡献

欢迎贡献代码、文档或提出建议！请阅读 [CONTRIBUTING.md](CONTRIBUTING.md) 了解详情。

### 贡献方式

- 报告 Bug 或提出功能请求
- 完善或翻译文档
- 提交代码改进
- 分享使用经验

## 许可证

本项目采用 [GNU General Public License v3.0](LICENSE) 许可证开源。

这意味着：
- ✅ 可以自由使用、修改和分发
- ✅ 衍生作品必须使用相同的 GPL v3 许可证
- ✅ 必须保留版权声明和许可证副本
- ✅ 修改后的文件必须明确标注

## 致谢

- 感谢纷享销客提供的 APL 开发平台
- 感谢所有贡献者的支持

## 联系方式

- 作者：小黑
- 邮箱：locc233@163.com
- 项目地址：[GitHub](https://github.com/Black-do/fxiaoke-dev-xiaohei)

---

**注意**：本项目为第三方开发工具，与纷享销客官方无关。使用时请遵守纷享销客的开发者协议。
