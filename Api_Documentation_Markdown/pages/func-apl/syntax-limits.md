# 纷享平台语法限制

## 循环语法限制

| 语法 | 支持状态 | 替代方案 |
|------|----------|----------|
| `for` 循环 | ❌ 不支持 | `each` 方法 |
| `while` 循环 | ❌ 不支持 | `each` 方法 |
| `do-while` 循环 | ❌ 不支持 | `each` 方法 |

## 容器类 each 用法

### List.each - 遍历列表

```groovy
// 遍历查询结果
def (Boolean error, QueryResult queryResult, String errorMessage) = Fx.object.find(
    'AccountObj',
    FQLAttribute.builder()
        .columns(['_id', 'name'])
        .queryTemplate(QueryTemplate.AND(['_id': QueryOperator.NE('')]))
        .limit(10)
        .build()
)

if (!error && queryResult.dataList) {
    queryResult.dataList.each { record ->
        log.info("记录名称：" + record.getAt('name'))
    }
}
```

### Map.each - 遍历字典

```groovy
Map map = ["a": 1, "b": 2, "c": 3]
map.each { String key, value ->
    log.info("键: " + key + ", 值: " + value)
}
```

### Range.each - 数字范围循环

```groovy
// 最多循环500次
Range range = Ranges.of(1, 5)
range.each { it ->
    log.info("当前值: " + it)
}
```

## 变量命名限制

闭包内禁用的变量名：
- `owner`
- `this`
- `delegate`

```groovy
// ❌ 错误
dataList.each { owner -> }

// ✅ 正确
dataList.each { item -> }
```

## 输出语法限制

| 语法 | 支持状态 | 替代方案 |
|------|----------|----------|
| `println` | ❌ 不支持 | `log.info()` |
| `print` | ❌ 不支持 | `log.info()` |
| `System.out.println` | ❌ 不支持 | `log.info()` |

```groovy
// ❌ 错误
println "hello"
System.out.println("hello")

// ✅ 正确
log.info("hello")
log.error("error message")
log.warn("warning message")
```

## 异常处理限制

| 语法 | 支持状态 | 替代方案 |
|------|----------|----------|
| `try-catch` | ❌ 不支持 | 返回值元组判断 |
| `throw` | ❌ 不支持 | 返回错误信息 |
| `throws` | ❌ 不支持 | 返回错误信息 |

```groovy
// ❌ 错误
try {
    def result = Fx.object.find(...)
} catch (Exception e) {
    // 不支持
}

// ✅ 正确
def (Boolean error, QueryResult queryResult, String errorMessage) = Fx.object.find(...)
if (error) {
    log.error("查询失败：" + errorMessage)
    return
}
```

## ⚠️ queryTemplate 强制规范

**使用 `Fx.object.find/findOne` 时必须遵守：**

| 查询条件 | 状态 | 说明 |
|---------|------|------|
| `QueryTemplate.AND([:])` | ❌ **禁止** | 会报错 "parameter cannot be empty" |
| `QueryTemplate.AND(['_id': QueryOperator.NE('')])` | ✅ **推荐** | 查询所有记录 |
| `QueryTemplate.AND(['field': QueryOperator.EQ('value')])` | ✅ **推荐** | 条件查询 |

```groovy
// ❌ 错误：空查询条件（会报错）
def (Boolean error, QueryResult result, String errorMessage) = Fx.object.find(
    'AccountObj',
    FQLAttribute.builder()
        .columns(['_id', 'name'])
        .queryTemplate(QueryTemplate.AND([:]))
        .build()
)

// ✅ 正确：查询所有记录（默认 limit=10，最高 100）
def (Boolean error, QueryResult result, String errorMessage) = Fx.object.find(
    'AccountObj',
    FQLAttribute.builder()
        .columns(['_id', 'name'])
        .queryTemplate(QueryTemplate.AND(['_id': QueryOperator.NE('')]))
        .limit(10)  // 默认 10 条，最高 100 条
        .build()
)
```

**常用查询操作符：**
```groovy
QueryOperator.EQ('value')        // 等于
QueryOperator.NE('')             // 不等于（查询所有推荐）
QueryOperator.GT(100)            // 大于
QueryOperator.LT(100)            // 小于
QueryOperator.LIKE('%keyword%')  // 模糊匹配
QueryOperator.IN(['a', 'b'])     // 在数组中
```

## ⚠️ limit 限制规范

**FQL/SQL 查询的 limit 默认值和上限：**

| 场景 | 默认值 | 最高限制 | 说明 |
|------|--------|---------|------|
| `Fx.object.find` | 10 条 | 100 条 | 未设置 limit 时默认查询 10 条 |
| `Fx.object.findOne` | 1 条 | 1 条 | 只返回第一条匹配记录 |
| 分页查询 | - | 100 条 | 单次查询最高 100 条 |

```groovy
// 默认查询 10 条（未设置 limit）
Fx.object.find('AccountObj',
    FQLAttribute.builder()
        .columns(['_id', 'name'])
        .queryTemplate(QueryTemplate.AND(['_id': QueryOperator.NE('')]))
        .build()  // 默认 limit=10
)

// 手动设置 limit（最高 100 条）
Fx.object.find('AccountObj',
    FQLAttribute.builder()
        .columns(['_id', 'name'])
        .queryTemplate(QueryTemplate.AND(['_id': QueryOperator.NE('')]))
        .limit(50)  // ✅ 有效范围：1-100
        .build()
)

// ❌ 错误：超过最高限制
Fx.object.find('AccountObj',
    FQLAttribute.builder()
        .queryTemplate(QueryTemplate.AND(['_id': QueryOperator.NE('')]))
        .limit(200)  // 超过 100 条限制！
        .build()
)

// 分页查询（使用 SQL + 闭包处理大批量数据）
// 适用于查询大量数据的场景，自动分页处理
def objectName = 'AccountObj'
def sql = "select _id, name from ${objectName} where _id != ''"
Fx.object.select(sql, SelectAttribute.builder().build(), { list ->
    list.each { item ->
        Map map = item as Map
        log.info("记录 ID: " + map['_id'] + ", 名称：" + map['name'])
    }
}).result()

// 或使用 SQL 分页查询（适合需要分页的场景）
// FQL 不支持 offset，必须使用 SQL 语法：limit row_count offset offset
def offset = 0
def limit = 100
def sqlPage = "select _id, name from ${objectName} where _id != '' limit ${limit} offset ${offset}"
def rst = Fx.object.select(
    sqlPage,
    SelectAttribute.builder().build()
).result() as QueryResult

// 处理分页数据
if (rst) {
    rst.dataList.each { record ->
        log.info("记录：" + record.getAt('name'))
    }
}
```

## 函数调用限制

| API | 限制值 |
|-----|--------|
| `Fx.object` | 300 次/函数 |
| `Fx.http` | 50 次/函数 |
| `Fx.function` | 50 次/函数 |
| `Fx.message` | 50 次/函数 |

## 执行时间限制

| 命名空间 | 限制值 |
|----------|--------|
| debug 执行 | 120s |
| 按钮 | 60s |
| 流程 | 300s |
| 计划任务 | 600s |
| 默认 | 15s |
