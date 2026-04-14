# Fx.object 核心 API 参考

## 查询 API

| 方法 | 用途 | 返回值 |
|------|------|--------|
| `Fx.object.find(apiName, fqlAttribute, selectAttribute)` | FQL 查询多条数据 | `(Boolean error, QueryResult queryResult, String errorMessage)` |
| `Fx.object.findOne(apiName, fqlAttribute, selectAttribute)` | FQL 查询单条数据 | `(Boolean error, Map data, String errorMessage)` |
| `Fx.object.findById(apiName, id, fqlAttribute, selectAttribute)` | 按 ID 查询单条数据 | `(Boolean error, Map data, String errorMessage)` |

## 创建 API

| 方法 | 用途 | 返回值 |
|------|------|--------|
| `Fx.object.create(apiName, objectData, details, createAttribute)` | 创建对象（支持主从） | `(Boolean error, Map data, String errorMessage)` |
| `Fx.object.batchCreate(apiName, objects, createAttribute)` | 批量创建（最多 500 条/批） | `(Boolean error, List<Map> data, String errorMessage)` |

## 更新 API

| 方法 | 用途 | 返回值 |
|------|------|--------|
| `Fx.object.update(apiName, objectId, updateFields, updateAttribute)` | 增量更新单条数据 | `(Boolean error, Map data, String errorMessage)` |
| `Fx.object.update(apiName, queryTemplate, updateFields, updateAttribute)` | 按条件批量更新 | `(Boolean error, Object result, String errorMessage)` |

## 删除 API

| 方法 | 用途 | 返回值 |
|------|------|--------|
| `Fx.object.delete(apiName, objectId)` | 删除单条数据 | `(Boolean error, Map data, String errorMessage)` |
| `Fx.object.batchDelete(apiName, objectIds)` | 批量删除 | `(Boolean error, List<Map> data, String errorMessage)` |

## 其他 API

| 方法 | 用途 | 返回值 |
|------|------|--------|
| `Fx.object.changeOwner(apiName, objectId, newOwnerId)` | 变更负责人 | `(Boolean error, Map data, String errorMessage)` |
| `Fx.object.batchChangeOwner(apiName, objectIds, newOwnerId)` | 批量变更负责人 | `(Boolean error, List<Map> data, String errorMessage)` |

## FQL 查询构建器

```groovy
// 基本查询
Fx.object.find('AccountObj',
    FQLAttribute.builder()
        .columns(['_id', 'name', 'owner'])
        .queryTemplate(QueryTemplate.AND([
            'name': QueryOperator.LIKE('%公司%'),
            'owner': QueryOperator.EQ('1000')
        ]))
        .limit(100)
        .offset(0)
        .build()
)

// 单条查询（推荐）
Fx.object.findOne('AccountObj',
    FQLAttribute.builder()
        .columns(['_id', 'name'])
        .queryTemplate(QueryTemplate.AND(['_id': QueryOperator.EQ('xxx')]))
        .build()
)

// 查询所有记录
Fx.object.find('AccountObj',
    FQLAttribute.builder()
        .columns(['_id', 'name'])
        .queryTemplate(QueryTemplate.AND(['_id': QueryOperator.NE('')]))
        .limit(10)
        .build()
)
```

## ⚠️ 重要提示

**queryTemplate 使用规范已在 [syntax-limits.md](syntax-limits.md) 详细说明，请务必遵守：**
- ❌ 禁止使用空的 `QueryTemplate.AND([:])`
- ✅ 使用有效的查询条件，如 `QueryTemplate.AND(['_id': QueryOperator.NE('')])`

## 常用查询操作符

| 操作符 | 用途 | 示例 |
|--------|------|------|
| `QueryOperator.EQ` | 等于 | `QueryOperator.EQ('value')` |
| `QueryOperator.NE` | 不等于 | `QueryOperator.NE('value')` |
| `QueryOperator.LIKE` | 模糊匹配 | `QueryOperator.LIKE('%keyword%')` |
| `QueryOperator.IN` | 包含于 | `QueryOperator.IN(['a', 'b'])` |
| `QueryOperator.GT` | 大于 | `QueryOperator.GT(100)` |
| `QueryOperator.LT` | 小于 | `QueryOperator.LT(100)` |
| `QueryOperator.GTE` | 大于等于 | `QueryOperator.GTE(100)` |
| `QueryOperator.LTE` | 小于等于 | `QueryOperator.LTE(100)` |
