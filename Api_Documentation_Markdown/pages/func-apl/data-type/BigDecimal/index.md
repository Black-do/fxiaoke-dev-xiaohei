#  BigDecimal类型

# # BigDecimal类型

BigDecimal - 数字类型

定义BigDecimal：BigDecimal b

例：
    
    
    BigDecimal b = 0.01
    

BigDecimal类型的静态方法：

  * BigDecimal.of(<String value>)
  * BigDecimal.of(<Number value>)



保留小数：

  * b.setScale(小数位数,BigDecimal.ROUND_HALF_UP) 四舍五入
  * b.setScale(小数位数,BigDecimal.ROUND_HALF_DOWN) 舍弃部分>5时ROUND_UP，否则ROUND_DOWN
  * b.setScale(小数位数,BigDecimal.ROUND_UP) 不管保留数字后面是大是小(0除外)都会进1
  * b.setScale(小数位数,BigDecimal.ROUND_DOWN) 保留设置数字，后面所有直接去除



例：
    
    
    BigDecimal a = 3.435
    BigDecimal b = a.setScale(2, BigDecimal.ROUND_UP)
    BigDecimal c = a.setScale(2, BigDecimal.ROUND_DOWN)
    BigDecimal d = a.setScale(2, BigDecimal.ROUND_HALF_UP)
    BigDecimal e = a.setScale(2, BigDecimal.ROUND_HALF_DOWN)
    
    log.info(b) //3.44
    log.info(c) //3.43
    log.info(d) //3.44
    log.info(e) //3.43
    

[Boolean类型](../Boolean/) [String类型](../String/)

← [Boolean类型](../Boolean/) [String类型](../String/)→ 

  * 跟随系统 
  * 浅色模式 
  * 深色模式 
  * 阅读模式 


