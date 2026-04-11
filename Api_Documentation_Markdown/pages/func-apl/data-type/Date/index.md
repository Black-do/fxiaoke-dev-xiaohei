#  Date类型

# # Date类型

Date - 日期类型，格式为YYYY-MM-DD，使用时用""封装

定义Date：Date date = "<YYYY-MM-DD>"

例：
    
    
    Date date = "2019-01-01"
    
    

Date类型的方法：

Date.now()：获取当前时间的年月日 例：
    
    
    Date d = Date.now()
    

date.withYear(<Integer year>)：设置日期的年，返回新的日期 返回值类型：Date

例：
    
    
    date.withYear(2018) //返回：2018-01-01
    

date.withMonth(<Integer month>)：设置日期的月，返回新的日期 返回值类型：Date

例：
    
    
    date.withMonth(12) //返回：2019-12-01
    

date.withDay(<Integer day>)：设置日期的日，返回新的日期 返回值类型：Date

例：
    
    
    date.withDay(30) //返回：2019-01-30
    

date.toTimestamp()：日期转时间戳 返回值类型：Long

例：
    
    
    date.toTimestamp() //返回：1567958400000
    

date.year：获取日期中的年 例：
    
    
    date.year //返回：2019
    

date.month：获取日期中的月 例：
    
    
    date.month //返回：1
    

date.day：获取日期中的日 例：
    
    
    date.day //返回：1
    

date.dayOfWeek：当前日期是周几 例：
    
    
    date.dayOfWeek //返回：1(周一)
    

date.weekOfYear：当前日期是本年第几周 例：
    
    
    date.weekOfYear //返回：1(本年第一周)
    

date.weekOfMonth：当前日期是本月第几周 例：
    
    
    date.weekOfMonth //返回：1(本月第一周)
    

date.dayOfYear：当前日期是本年第几天 例：
    
    
    date.dayOfYear //返回：1(本年第一天)
    

date.daysBetween(<Date date>)：返回两个日期间隔的天数 例：
    
    
    Date date1 = "2020-01-02"
    
    Date date2 = "2020-01-03"
    
    date1.daysBetween(date2) //返回：2
    

date.monthsBetween(<Date date>)：返回两个日期间隔的月数 例：
    
    
    Date date1 = "2020-01-01"
    
    Date date2 = "2020-03-03"
    
    date1.monthsBetween(date2) //返回：2
    

  * date.toStartOfMonth()：返回本月开始日期 例：


    
    
    Date date = "2020-01-20"
    
    Date dateRetrun = date.toStartOfMonth() //返回：2020-01-01
    

  * date.toStartOfWeek()：返回本周开始日期 例：


    
    
    Date date = "2020-01-01"
    
    Date dateRetrun = date.toStartOfWeek() //返回：2020-12-30
    

  * Date.of(Long timestamp)：时间戳转date 例：


    
    
    Long timestamp = 1618972431890
    
    Date d =  Date.of(timestamp)
    

  * Date.of(<String a>)：字符串转date 例：


    
    
    String a = "2020-01-01"
    Date date = Date.of(a)
    log.info("date:"+date)
    

[Time类型](../Time/) [Boolean类型](../Boolean/)

← [Time类型](../Time/) [Boolean类型](../Boolean/)→ 

  * 跟随系统 
  * 浅色模式 
  * 深色模式 
  * 阅读模式 


