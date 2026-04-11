#  DateTime类型

# # DateTime类型

Date - 日期类型（具体），格式为YYYY-MM-DD hh:mm，使用时用""封装

定义Date：DateTime dateTime = "<YYYY-MM-DD hh:mm>"

例：
    
    
     DateTime dateTime = "2019-01-01 12:00"
    
    

DateTime类型的方法：

  * DateTime.now()：获取当前时间的年月日时分 例：


    
    
     DateTime d = DateTime.now()
    
    

  * dateTime.withYear(<Integer year>)：设置日期的年，返回新的日期 返回值类型：DateTime



例：
    
    
     dateTime.withYear(2018) //返回：2018-01-01 12:00
    
    

  * dateTime.withMonth(<Integer month>)：设置日期的月，返回新的日期 返回值类型：DateTime



例：
    
    
     dateTime.withMonth(12) //返回：2019-12-01 12:00
    
    

  * dateTime.withDay(<Integer day>)：设置日期的日，返回新的日期 返回值类型：DateTime



例：
    
    
     dateTime.withDay(30) //返回：2019-01-30 12:00
    
    

  * dateTime.withHour(<Integer hour>)：设置日期的小时，返回新的日期 返回值类型：DateTime



例：
    
    
     dateTime.withHour(13) //返回：2019-01-01 13:00
    
    

  * dateTime.withMinute(<Integer day>)：设置日期的分钟，返回新的日期 返回值类型：DateTime



例：
    
    
     dateTime.withMinute(30) //返回：2019-01-01 12:30
    
    

  * dateTime.toTimestamp()：日期转时间戳 返回值类型：Long



例：
    
    
     dateTime.toTimestamp() //返回：1568001600000
    

  * dateTime.year：获取日期中的年 例：


    
    
      dateTime.year //返回：2019
    

  * dateTime.month：获取日期中的月 例：


    
    
      dateTime.month //返回：1
    

  * dateTime.day：获取日期中的日 例：


    
    
       dateTime.day //返回：1
    

  * dateTime.hour：获取日期中的小时 例：


    
    
       dateTime.hour //返回：12
    

  * dateTime.minute：获取日期中的分钟 例：


    
    
       dateTime.minute //返回：0
    

  * dateTime.dayOfWeek：当前日期是周几 例：


    
    
      dateTime.dayOfWeek //返回：1(周一)
    

  * dateTime.weekOfYear：当前日期是本年第几周 例：


    
    
      dateTime.weekOfYear //返回：1(本年第一周)
    

  * dateTime.weekOfMonth：当前日期是本月第几周 例：


    
    
      dateTime.weekOfMonth //返回：1(本月第一周)
    

  * dateTime.toDate：日期时间转日期 例：


    
    
      DateTime dateTime = "2019-01-01 12:00"
      Date date = dateTime.toDate()
    
      log.info(date)
    

  * DateTime.of(Long timestamp)：时间戳转dateTime


    
    
    Long timestamp = 1618972431890
    
    DateTime d1 = DateTime.of(timestamp)
    

  * DateTime.of(<String a>)：字符串转date 例：


    
    
    String b = "2020-01-01 00:00"
    DateTime dateTime = DateTime.of(b)
    log.info("dateTime"+ dateTime)
    

[List类型](../List/) [Time类型](../Time/)

← [List类型](../List/) [Time类型](../Time/)→ 

  * 跟随系统 
  * 浅色模式 
  * 深色模式 
  * 阅读模式 


