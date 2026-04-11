#  Fx.cache

## # Fx.cache

### # 1\. getDefaultCache DefaultCache

> `Fx.cache.getDefaultCache()`

**Groovy 举例**
    
    
    Cache cache = Fx.cache.getDefaultCache()
    log.info(cache.get("key1"))
    //put单位为秒，1~172800有效
    cache.put("key1", 1234, 5)
    log.info(cache.contains("key1"))
    Integer value = (Integer) cache.get("key1")
    log.info(value)
    log.info(cache.inc("key1"))
    if(cache.remove("key1")) {
      log.info("remove success!")
    }
    log.info(cache.get("key1"))
    
    

**参考对象**

  * 参考Cache



**注意事项**

>   * 限制
>   * key字符串最大长度256
>   * value字符串最大长度1M
>   * 最大失效时间48h
>   * 单位秒
> 


## # 参考类 com.fxiaoke.functions.interfaces.Cache

### # 字段说明

参数名称 | object | 描述  
---|---|---  
  
### # 1\. contains 缓存key是否存在

> `Cache.contains()`

**负责人：斯作益seth**

### # 2\. put 插入键值对

> `Cache.put()`

**负责人：斯作益seth**

### # 3\. get 不推荐使用，通过键获取值，key不存在返回null，返回结果是Object，需要根据需求转换类型 as String / as Integer

> `Cache.get()`

**负责人：斯作益seth**

### # 4\. getString 通过键获取值，返回结果类型是String

> `Cache.getString()`

**负责人：斯作益seth**

### # 5\. getInteger 通过键获取值，返回结果类型是Integer

> `Cache.getInteger()`

**负责人：斯作益seth**

### # 6\. getLong 通过键获取值，返回结果类型是Long

> `Cache.getLong()`

**负责人：斯作益seth**

### # 7\. remove 删除缓存

> `Cache.remove()`

**负责人：斯作益seth**

### # 8\. inc 对数字key加一（value为字符串不支持）

> `Cache.inc()`

**负责人：斯作益seth**

### # 9\. dec 对数字key减一（value为字符串不支持）

> `Cache.dec()`

**负责人：斯作益seth**

[Fx.BI](../BIAPI/) [Fx.stage](../StageAPI/)

← [Fx.BI](../BIAPI/) [Fx.stage](../StageAPI/)→ 

  * 跟随系统 
  * 浅色模式 
  * 深色模式 
  * 阅读模式 


