#  Fx.random

## # Fx.random

### # 1\. nextInt 随机生成任一整数

> `Fx.random.nextInt()`

**Groovy 举例**
    
    
    Fx.random.nextInt()
    //int值
    
    

### # 2\. nextInt 随机生成任一小于bound的非负整数

> `Fx.random.nextInt(<Integer bound>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
bound | Integer | 必须是正数 | 是  
  
**Groovy 举例**
    
    
    Fx.random.nextInt(10)
    
    

### # 3\. randomUUID 随机生成UUID

> `Fx.random.randomUUID()`

**Groovy 举例**
    
    
    String str = Fx.random.randomUUID()
    log.info(str)
    
    

**注意事项**

>   * 生成格式为: 8-4-4-4-12
> 


[Fx.work](../WorkAPI/) [Fx.crypto](../CryptoAPI/)

← [Fx.work](../WorkAPI/) [Fx.crypto](../CryptoAPI/)→ 

  * 跟随系统 
  * 浅色模式 
  * 深色模式 
  * 阅读模式 


