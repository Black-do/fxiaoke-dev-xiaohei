#  List类型

# # List类型

List - 集合类型，使用时用[]封装，中间数据用,分隔

定义List：List list = []

例：
    
    
     List colors = ["red","blue","green","yellow"]
    

List类型的方法：

  * list.add(<Object any_type>)：向列表添加元素 返回值类型：Boolean



例：
    
    
        List colors = ["red", "blue", "green"]
        colors.add("yellow") //返回：true
    

  * list.addAll(<List list1>)：向列表添加多个元素 返回值类型：Boolean



例：
    
    
        List colors = ["red", "blue"]
        colors.addAll(["green", "yellow"]) //返回：true
    

  * list.clear()：清空字符串 返回值类型：无返回值



例：
    
    
        List colors = ["red", "blue"]
        colors.clear()
    

  * list.contains(<Object any_type>)：判断列表中是否存在指定元素。如果列表中存在元素, 则返回"true" 返回值类型：Boolean



例：
    
    
        List colors = ["red", "blue", "green", "yellow"]
        result = colors.contains("red") //返回：true
    

  * list.containsAll(<List list1>)：判断列表中是否存在所有指定元素。如果列表中存在元素, 则返回"true" 返回值类型：Boolean



例：
    
    
        List colors = ["red", "blue", "green"]
        result = colors.containsAll(["red", "yellow"]) //返回：false
    

  * list.indexOf(<Object any_type>)：返回给定元素在列表中的位置 (第一个元素的位置为 "0") 返回值类型：int



例：
    
    
         List colors = ["red", "blue", "green", "yellow"]
         result = colors.indexOf("green") //返回：2
    

  * list.get(<int indexNumber>)：返回给定位置在列表中的元素 (第一个元素的位置为 "0") 返回值类型：Object



例：
    
    
         List colors = ["red", "blue", "green", "yellow"]
         result = colors.get(1) // 返回: "blue"
    

  * list.size()：返回列表中元素的数目 返回值类型：int



例：
    
    
        List colors = ["red", "blue", "green", "yellow"]
        result = colors.size() //返回：4
    

  * list.sort(<Boolean bool>)列表排序,可选布尔值指定升序 (true)/降序 (false),为空时默认为升序 返回值类型：List



例：
    
    
        List colors = ["red", "blue", "green", "yellow"]
        colors.sort() // 返回: ["blue","green","red","yellow"]
    

  * list.subList(<int startIndex>,<int endIndex>) 根据指定的开始和结束索引 (包含指定的索引，不包括结束索引) 从给定列表中返回一组元素 返回值类型：List



例：
    
    
        List colors = ["red", "blue", "green", "yellow"]
        result = colors.subList(1, 3); // 返回: ["blue","green"]
    

  * list.remove(<int index>)移除并返回指定索引处的元素 (第一个元素的索引为 "0") 返回值类型：Object



例：
    
    
         List colors = ["red", "blue", "green", "yellow"]
         colors.remove(2) // 返回: "green"
    

  * list.isEmpty()判断列表是否为空。返回一个布尔值-如果列表中不包含任何值, 则为true; 否则为-如果列表中包含值, 则为false 返回值类型：Boolean



例：
    
    
         List colors = ["red", "blue", "green", "yellow"]
         result = colors.isEmpty() // 返回: false
    

  * list.intersect(<List list>) 返回指定列表与当前列表的交集 返回值类型：List



例：
    
    
         colors = ["red", "blue", "green", "orange"]
         fruits = ["apple","orange","banana"]
         result = colors.intersect(fruits) // 返回：["orange"]
    

  * list.lastIndexOf(<Object any_type>) 返回指定元素在列表中的最后一个匹配项的位置 返回值类型：BigDecimal



例：
    
    
          colors = ["red", "blue", "green", "yellow", "green"]
          result = colors.lastIndexOf("green") //返回：4
    

  * list.eachWithIndex(<Closure closure>) 遍历列表中的数据，闭包中传入item和index 返回值类型：List



例：
    
    
          List list = ["a", "c"]
          list.eachWithIndex { item, int i ->
              log.info(item)
              log.info(i)
          } //运行日志：a  0  b  1
    

  * list.each(<Closure closure>) 遍历列表中的数据，闭包中传入item 返回值类型：List



例：
    
    
          List list = ["a", "c"]
          list.each { item ->
              log.info(item)
          } //运行日志：a   b
    

  * list.any{<Closure closure>} 判断是否至少有一个元素有效 返回值类型：Boolean



例1：
    
    
          List list = ["a", "b"]
          Boolean b = list.any { x -> x == "a" } // list中是否有一个元素为"a"
          log.info(b)
          // 运行日志：true
    

例2：
    
    
          List list = [["a":1], ["a":2]]
          Boolean b = list.any { x -> (x.a as Integer) > 1 } // list中元素为map，并且key为"a"的value值是否有一个大于1
          log.info(b)
          // 运行日志：true
    

  * list.collect{<Closure closure>} list中的元素为map，取出每个map中的value值 返回值类型：List



例：
    
    
          List list = [["a":1], ["a":2]]
          List result = list.collect { x -> x.a }
          log.info(result)
          // 运行日志：[1, 2]
    

  * list.find{<Closure closure>} list中的元素为map，取出每个map中第一个符合条件的value值 返回值类型：Map



例：
    
    
          List list = [["a":1], ["a":2]]
          Map map = list.find { x -> (x.a as Integer) > 1 }
          log.info(map)
          // 运行日志：{a=2}
    

[Map类型](../Map/) [DateTime类型](../DateTime/)

← [Map类型](../Map/) [DateTime类型](../DateTime/)→ 

  * 跟随系统 
  * 浅色模式 
  * 深色模式 
  * 阅读模式 


