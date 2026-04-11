#  Time类型

# # Time类型

Time - 时间类型，格式为hh:mm，使用时用""封装

定义Time：Time time = "<hh:mm>"

例：
    
    
    Time time = "09:30"
    Time类型的方法：
    

  * Time.now()：获取当前时间的时分 例：


    
    
    Time t = Time.now()
    

  * time.withHour(<Integer hour>)：设置时间的小时，返回新的时间 返回值类型：Time



例：
    
    
    time.withHoue(13) //返回：13:30
    

  * time.withMinute(<Integer day>)：设置时间的分钟，返回新的时间 返回值类型：Time



例：
    
    
    time.withMinute(50) //返回：9:50
    

  * time.toTimestamp()：日期转时间戳 返回值类型：BigDecimal



例：
    
    
    time.toTimestamp() //返回：4260000
    

  * time.hour：获取时间中的小时 例：


    
    
    time.hour //返回：9
    

  * time.minute：获取时间中的分钟 例：


    
    
    time.minute //返回：30
    

[DateTime类型](../DateTime/) [Date类型](../Date/)

← [DateTime类型](../DateTime/) [Date类型](../Date/)→ 

  * 跟随系统 
  * 浅色模式 
  * 深色模式 
  * 阅读模式 


