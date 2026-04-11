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
    'Account__c',
    FQLAttribute.builder()
        .columns(['_id', 'name'])
        .queryTemplate(QueryTemplate.AND([:]))
        .limit(10)
        .build()
)

if (!error && queryResult.dataList) {
    queryResult.dataList.each { record ->
        log.info("记录名称: " + record.name)
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
    log.error("查询失败: " + errorMessage)
    return
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
