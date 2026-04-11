#  Map类型

# # Map类型

Map - 集合类型，使用时用[]封装，中间数据用,分隔，以键值对的形式存在

定义Map：

例：
    
    
     Map map = ["a":1, "b": 2, "c":3]
    

Map类型的方法：

  * map.keys()：获取字典所有的属性名称 返回值类型：List



例：
    
    
    Map map = ["a": 1, "b": 2]
    
    result = map.keys()  // 返回: ["a", "b"]
    
    

  * map.size()：返回字典中元素的数目 返回值类型：BigDecimal



例：
    
    
    Map map = ["a": 1, "b": 2]
    
    result = map.size()  // 返回: 2
    
    

  * map.isEmpty()：判断字典是否为空。如果不包含键值映射, 则返回布尔值-true；如果包含键值映射, 则为false 返回值类型：Boolean



例：
    
    
     Map map = ["a": 1, "b": 2]
    
     result = map.isEmpty()  // 返回: false
    

  * map.remove(<String key>)：移除并返回指定键的元素 返回值类型：Object



例：
    
    
    Map map = ["a": 1, "b": 2]
    
    map.remove("a")  // 返回: 1
    

  * map.clear()：从字典中移除所有键值对 返回值类型：无返回值



例：
    
    
     Map map = ["a": 1, "b": 2]
    
    map.clear()
    

  * map.put(<String key>,<Object value>)：存放键值对 返回值类型：无返回值



例：
    
    
    Map map = ["a": 1, "b": 2]
    
    map.put('c', 3)
    

  * map.putIfAbsent(<String key>,<Object value>)：存放键值对，如果key存在的情况下，在putIfAbsent下不会修改 返回值类型：Object



例：
    
    
    Map map = ["a": 1, "b": 2]
    
    map.putIfAbsent('a', 2)  //此时键“a”的值还是1
    

  * map.containsKey(<String key>)：是否包含key 返回值类型：Boolean



例：
    
    
    Map map = ["a": 1, "b": 2]
    
    map.containsKey("a");  // 返回: true
    

  * map.containsValue(<Object value>)：是否包含value 返回值类型：Boolean



例：
    
    
     Map map = ["a": 1, "b": 2]
    
    map.containsValue(2);  // 返回: true
    

  * map.values()：返回所有值的集合 返回值类型：List



例：
    
    
    Map map = ["a": 1, "b": 2]
    
    map.values();  // 返回: [1, 2]
    

  * map.each(<Closure closure>)：遍历字典中的数据，闭包中传入key和value 返回值类型：List



例：
    
    
    Map map = ["a": 1, "b": 2]
    
    map.each {String key,value ->
    
        log.info(key)
    
        log.info(value)
    
    }
    

[Duration类型](../Duration/) [List类型](../List/)

← [Duration类型](../Duration/) [List类型](../List/)→ 

  * 跟随系统 
  * 浅色模式 
  * 深色模式 
  * 阅读模式 


