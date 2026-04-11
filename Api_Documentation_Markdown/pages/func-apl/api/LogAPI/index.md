#  Fx.log

## # Fx.log

### # 1\. info 运行日志

> `Fx.log.info(<Object data>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
data | Object | 要记录的日志 | 是  
  
**Groovy 举例**
    
    
    log.info(' Hello fxiaoke ')
    
    

**注意事项**

>   * info+warn+error级别最多共记录400行
> 


### # 2\. warn 运行日志

> `Fx.log.warn(<Object data>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
data | Object | 要记录的日志 | 是  
  
**Groovy 举例**
    
    
    log.info(' Hello fxiaoke ')
    
    

**注意事项**

>   * info+warn+error级别最多共记录400行
> 


### # 3\. error 运行日志

> `Fx.log.error(<Object data>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
data | Object | 要记录的日志 | 是  
  
**Groovy 举例**
    
    
    log.error(' Hello fxiaoke ')
    
    

**注意事项**

>   * info+warn+error级别最多共记录400行
> 


### # 4\. debug 调试日志只在调试窗口输出，不记录在运行日志中

> `Fx.log.debug(<Object data>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
data | Object | 要记录的日志 | 是  
  
**Groovy 举例**
    
    
    log.debug(' Hello fxiaoke ')
    
    

### # 5\. lap 耗时每个步骤的统计，仅对debug生效

> `Fx.log.lap(<String step>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
step | String | 统计步骤 | 是  
  
**Groovy 举例**
    
    
    log.lap('createObject-AccountObj')
    
    

[Fx.http](../HttpAPI/) [Fx.crm](../CRMAPI/)

← [Fx.http](../HttpAPI/) [Fx.crm](../CRMAPI/)→ 

  * 跟随系统 
  * 浅色模式 
  * 深色模式 
  * 阅读模式 


