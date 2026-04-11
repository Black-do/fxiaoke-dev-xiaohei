#  Fx.mq

## # Fx.mq

### # 1\. pub 发送消息，通过事件监听做消息路由匹配

> `Fx.mq.pub(<String channel>, <Map body>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
channel | String | 消息通道，类似消息topic，不同业务使用不同channel；对应事件监听的消息通道值 | 是  
body | Map | 消息内容 | 是  
  
**Groovy 举例**
    
    
    Map body = ["key": "value", "xxxKey": "xxxValue"]
    Fx.mq.pub("xxx_channel", body)
    
    

[Fx.lock](../LockAPI/) [Fx.sign](../SignAPI/)

← [Fx.lock](../LockAPI/) [Fx.sign](../SignAPI/)→ 

  * 跟随系统 
  * 浅色模式 
  * 深色模式 
  * 阅读模式 


