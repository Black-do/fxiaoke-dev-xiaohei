---
name: "fxiaoke-dev-xiaohei"
description: "Intelligent API document retrieval for Fenxiang APL development. Invoke when user develops Fenxiang functions or queries API usage. 触发词：纷享开发、API 查询、纷享 API."
---

# 纷享开发助手

## When to Use

Invoke this skill when:
- User develops Fenxiang APL functions (Groovy language)
- User queries Fenxiang API usage
- User encounters API-related issues during development
- Detect project is Fenxiang-related

## 何时使用

当以下情况时调用此 skill：
- 用户进行纷享 APL 函数开发（Groovy 语言）
- 用户查询纷享 API 用法
- 用户在开发过程中遇到 API 相关问题
- 检测到项目与纷享相关

## Core Functionality

- **API Document Retrieval**: Use `api_doc_helper.py` for intelligent search
- **Code Development**: Generate code based on API documentation
- **Problem Solving**: Help resolve API usage issues

## 核心功能

- **API 文档检索**：使用 `api_doc_helper.py` 进行智能搜索
- **代码开发**：基于 API 文档生成代码
- **问题解决**：帮助解决 API 使用问题

## 工作流程

1. **接收请求**：用户提出 API 问题或开发需求
2. **搜索文档**：调用 `api_doc_helper.search_api_docs()` 进行检索
3. **分析内容**：提取关键信息
4. **生成响应**：提供 API 用法和代码示例

## 代码编写优先级

1. **本地 APL 文档** - 优先使用 skill 内的 `Api_Documentation_Markdown` 文档
2. **联网检索** - 如果本地文档不完整
3. **标准 Groovy** - 最后才使用，必须遵守 APL 限制

## ⚠️ 必须遵守：语法限制

**编写纷享 APL 代码时必须遵守以下限制：**

### 输出方法
```groovy
// ❌ 禁止使用
println, print, System.out.println

// ✅ 必须使用
log.info("信息")
log.error("错误")
log.warn("警告")
```

### 异常处理
```groovy
// ❌ 禁止使用
try-catch, throw, throws

// ✅ 必须使用返回值元组判断
def (Boolean error, QueryResult result, String errorMessage) = Fx.object.find(...)
if (error) {
    log.error("失败: " + errorMessage)
    return
}
```

### 循环语法
```groovy
// ❌ 禁止使用
for, while, do-while

// ✅ 必须使用 each 方法
dataList.each { item ->
    log.info(item.name)
}

// Range.each 用于分页（最多 500 次循环）
Range range = Ranges.of(0, 500)
range.each { offset ->
    // 分页逻辑
}
```

### 闭包内变量命名
```groovy
// ❌ 禁止在闭包内使用的变量名
owner, this, delegate

// ✅ 正确写法
dataList.each { item -> }  // 使用其他名称
```

## 文档结构

```
Api_Documentation_Markdown/
├── index.md
└── pages/func-apl/
    ├── api/              # API 模块
    ├── data-type/        # 数据类型
    ├── start/            # 入门指南
    ├── syntax-limits.md  # 语法限制详细说明
    └── api-reference.md  # API 参考表
```

## 检索机制

**所有 API 文档检索必须使用 `api_doc_helper.py`：**
- 向量搜索 + 关键词搜索
- 自动提取相关代码片段
- 确保代码风格与官方文档一致

## 命名规范

| 类型 | 规则 | 示例 |
|------|------|------|
| **内置对象** | 无 `__c` 后缀 | `AccountObj`, `ContactObj`, `ProductObj` |
| **自定义对象** | 以 `__c` 结尾 | `MyCustomObj__c` |
| **自定义字段** | 以 `__c` 结尾 | `field_4zWog__c` |
| **内置字段** | 无 `__c` 后缀 | `_id`, `name`, `owner`, `created_by` |

## 常用内置字段

| 字段 | API Name | 说明 |
|-----|----------|------|
| 唯一标识 | `_id` | 对象唯一 ID |
| 主属性 | `name` | 主要属性字段 |
| 负责人 | `owner` | 对象负责人 |
| 创建人 | `created_by` | 创建人 |
| 创建时间 | `create_time` | 创建时间戳 |

## 错误处理模式

```groovy
// 查询单条记录（推荐使用 findOne）
def (Boolean error, Map data, String errorMessage) = Fx.object.findOne(
    'AccountObj',
    FQLAttribute.builder()
        .columns(['_id', 'name'])
        .queryTemplate(QueryTemplate.AND(['_id': QueryOperator.NE('')]))
        .build()
)

if (error) {
    log.error("查询失败：" + errorMessage)
    return
}

if (data) {
    log.info("记录：" + data.getAt('name'))
}
```

## 注意事项

- **文档优先**：始终优先使用本地 `Api_Documentation_Markdown` 文档
- **语法合规**：所有代码必须遵守纷享 APL 语法限制
- **批量操作**：优先使用 `batchCreate`、`batchUpdate`、`batchDelete` 提升性能
- **分页查询**：使用 `Range.each`，最多 500 次循环

## Example

**User**: 如何查询纷享的对象数据？

**Skill Response**:
1. 检索 ObjectDataAPI 文档
2. 提供 Fx.object.find 示例代码
3. 说明语法限制和最佳实践

```groovy
// 示例：查询对象数据（使用 find 查询多条记录）
def (Boolean error, QueryResult result, String errorMessage) = Fx.object.find(
    'Account__c',
    FQLAttribute.builder()
        .columns(['_id', 'name', 'owner'])
        .queryTemplate(QueryTemplate.AND(['_id': QueryOperator.NE('')]))
        .limit(10)
        .build()
)

if (error) {
    log.error("查询失败：" + errorMessage)
    return
}

if (result.dataList && result.dataList.size() > 0) {
    result.dataList.each { record ->
        // 使用 getAt 方法访问字段，避免静态类型检查错误
        log.info("记录：" + record.getAt('name'))
    }
}
```
