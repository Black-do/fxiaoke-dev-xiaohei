#  Fx.json

## # Fx.json

### # 1\. toJson 对象转json字符串

> `Fx.json.toJson(<Object data>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
data | Object | 转json的对象 | 是  
  
**Groovy 举例**
    
    
    Fx.json.toJson(["a" : 1, "b" : 2]) //返回：{"a":1,"b":2}
    
    

### # 2\. toJson 对象转json字符串，指定序列化特性

> `Fx.json.toJson(<Object data>, <SerializerFeature[] features>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
data | Object | 转json的对象 | 是  
features | SerializerFeature[] | 可变参数，序列化特性列表 | \--  
  
**Groovy 举例**
    
    
    Map m = ["a": 1, "b": null]
    log.info(Fx.json.toJson(m))
    log.info(Fx.json.toJson(m, SerializerFeature.WriteMapNullValue))
    
    

### # 3\. parse json转Map

> `Fx.json.parse(<String data>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
data | String | json字符串 | 是  
  
**Groovy 举例**
    
    
    Map map = Fx.json.parse("{\"a\" : 1, \"b\" : 2}")
    
    

### # 4\. parseList json转List

> `Fx.json.parseList(<String data>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
data | String | jsonarray字符串 | 是  
  
**Groovy 举例**
    
    
    List list = Fx.json.parseList('[{"a": 1, "b": 2},{"a": 10, "b": 20}]')
    
    

**注意事项**

>   * 这里的字符串是jsonArray字符串，以[开头，以]结尾
> 


### # 5\. parseObject json转class类

> `Fx.json.parseObject(<String text>, <Class clazz>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
text | String | json字符串 | 是  
clazz | Class | 需要转换的类型，例如List.class | 是  
  
**Groovy 举例**
    
    
    List tmp = Fx.json.parseObject('[{"a": 1, "b": 2},{"a": 10, "b": 20}]', List.class)
    
    

[Fx.crypto](../CryptoAPI/) [Fx.location](../LocationAPI/)

← [Fx.crypto](../CryptoAPI/) [Fx.location](../LocationAPI/)→ 

  * 跟随系统 
  * 浅色模式 
  * 深色模式 
  * 阅读模式 


