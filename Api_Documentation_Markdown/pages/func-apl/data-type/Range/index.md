#  Range类型

# # Range类型

在自定义函数中不支持for循环，但是可以用Range完成循环语句逻辑

定义：
    
    
    Range range = Ranges.of(Integer start,Integer end)
    
    range.each{
    
    }
    
    

注：最多循环500次

举例：
    
    
    Range range = Ranges.of(1,5)
    
    range.each{ it ->
      log.info(it)
    }  
    //[1,2,3,4,5]
    

[CollectionUtils类型](../CollectionUtils/) [HttpResult类型](../HttpResult/)

← [CollectionUtils类型](../CollectionUtils/) [HttpResult类型](../HttpResult/)→ 

  * 跟随系统 
  * 浅色模式 
  * 深色模式 
  * 阅读模式 


