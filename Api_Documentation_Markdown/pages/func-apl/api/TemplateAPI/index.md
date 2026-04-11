#  Fx.template

## # Fx.template

### # 1\. print 使用对象打印模板输出打印文件

> `Fx.template.print(<boolean error>, <Email data>, <String errorMessage>)`

**参数说明**

入参格式

参数名称 | object | 描述 | 是否必填  
---|---|---|---  
error | boolean | 是否执行异常 | 是  
data | Email | 返回结果 | 是  
errorMessage | String | 异常提示信息 | 是  
data | Email | 返回结果 | 是否必填  
---|---|---|---  
path | String | NPath | 是  
fileSize | Integer | 文件大小 | 是  
name | String | 文件名称 | 是  
fileType | String | 文件类型 | 是  
  
出参格式

参数名称 | APIResult | 参数列表  
---|---|---  
error | boolean | 是否执行异常  
data | Email | 返回结果  
errorMessage | String | 异常提示信息  
  
出参样例
    
    
    {
      "error": false,
      "data": {},
      "errorMessage": ""
    }
    
    

**Groovy 举例**
    
    
    // 打印数据的对象APIName
    String objectAPIName = "object_kFc8w__c"
    // 打印数据Id
    String objectId = "6209cfbcdac8a0000127187f"
    // 模板Id
    String templateId = "64d5dae417eb092ee3bbd9b1"
    // 流程实例Id
    String instanceId = null
    // 文档输出方向
    String orientation = "Landscape"
    // 语言tag
    String locale = "zh-CN"
    
    def(Boolean error, Map data, String errorMessage) = Fx.template.print(objectAPIName, objectId, templateId, instanceId, orientation, locale)
    if (error) {
      Fx.log.info("打印错误 ： " + errorMessage)
    } else {
      Fx.log.info(Fx.json.toJson(data))
    }
    
    

**注意事项**

>   * 打印调耗时会比较长，请尽量放在流程后动作，或者异步函数中，避免页面执行超时
> 


[Fx.bpm](../BpmAPI/) [Fx.BI](../BIAPI/)

← [Fx.bpm](../BpmAPI/) [Fx.BI](../BIAPI/)→ 

  * 跟随系统 
  * 浅色模式 
  * 深色模式 
  * 阅读模式 


