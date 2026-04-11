#  Fx.function

## # Fx.function

### # 1\. executeAsyncFunc 异步执行控制器函数

> `Fx.function.executeAsyncFunc(<String functionApiName>, <Map param>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
functionApiName | String | 需要执行的函数apiName | 是  
param | Map | 执行函数时传入的参数 | 是  
  
**Groovy 举例**
    
    
    Map keyValue = [
    "key1":"value1",
    "key2":"value2"
    ]
    
    Map param = [
    "map":keyValue
    ]
    def (error,result,errorMessage) = Fx.function.executeAsyncFunc("funcCalled__c",param)
    if(error){
        log.error("executeAsyncFunc error: "+errorMessage)
        //1.使用报错终止执行
        //Fx.message.throwException("executeAsyncFunc error: "+errorMessage)
    
        //2.使用return终止执行
        //return;
    
        //3.继续执行
    } 
    
    //dosomething
    
    

**注意事项**

>   * 异步执行控制器没有执行结果
> 


### # 2\. executeOrderlyAsyncFunc 顺序执行异步控制器函数

> `Fx.function.executeOrderlyAsyncFunc(<String functionApiName>, <Map param>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
functionApiName | String | 需要执行的函数apiName | 是  
param | Map | 执行函数时传入的参数 | 是  
  
**Groovy 举例**
    
    
    Map keyValue = [
    "key1":"value1",
    "key2":"value2"
    ]
    
    Map param = [
    "map":keyValue
    ]
    def (error,result,errorMessage) = Fx.function.executeOrderlyAsyncFunc("funcCalled__c",param)
    if(error){
        log.error("executeOrderlyAsyncFunc error: "+errorMessage)
        //1.使用报错终止执行
        //Fx.message.throwException("executeOrderlyAsyncFunc error: "+errorMessage)
    
        //2.使用return终止执行
        //return;
    
        //3.继续执行
    } 
    
    //dosomething
    
    

**注意事项**

>   * 异步执行没有执行结果
> 


### # 3\. ontimeFunc 定时执行控制器函数

> `Fx.function.ontimeFunc(<String functionApiName>, <Map param>, <String runTime>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
functionApiName | String | 需要执行的函数apiName | 是  
param | Map | 执行函数时传入的参数 | 是  
runTime | String | 定时执行的时间 | 是  
  
**Groovy 举例**
    
    
    Map keyValue = [
    "key1":"value1",
    "key2":"value2"
    ]
    
    Map param = [
    "map":keyValue
    ]
    def (error,result,errorMessage) = Fx.function.ontimeFunc("funcCalled__c",param,"2021-05-03 00:00:00")
    if(error){
        log.error("ontimeFunc error: "+errorMessage)
        //1.使用报错终止执行
        //Fx.message.throwException("ontimeFunc error: "+errorMessage)
    
        //2.使用return终止执行
        //return;
    
        //3.继续执行
    } 
    log.info("transactionId="+result)
    //dosomething
    
    

**注意事项**

>   * 指定执行会返回一个transactionId，该结果对排查问题较为重要，可以考虑做记录
> 


### # 4\. asyncOnVipQueue 使用独立的队列执行异步任务，不影响其他异步任务的执行（需要单独付费）

> `Fx.function.asyncOnVipQueue(<String functionApiName>, <Map param>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
functionApiName | String | 需要执行的函数apiName | 是  
param | Map | 执行函数时传入的参数 | 是  
  
**Groovy 举例**
    
    
    Map param = [
      "map":[
        "a": 123,
        "b": "sdte"
      ]
    ]
    
    def (error,result,errorMessage) = Fx.function.asyncOnVipQueue("func_U4Oqt__c", param)
    if(error){
        log.error("asyncOnVipQueue error: "+errorMessage)
        //1.使用报错终止执行
        //Fx.message.throwException("asyncOnVipQueue error "+errorMessage)
    
        //2.使用return终止执行
        //return;
    
        //3.继续执行
    } 
    log.info("traceId="+result)
    //dosomething
    
    

**注意事项**

>   * 返回值为traceId
> 


### # 5\. asyncOnVipQueue 使用独立的队列执行异步任务，指定队列，不影响其他异步任务的执行（需要单独付费）

> `Fx.function.asyncOnVipQueue(<String functionApiName>, <Map param>, <Integer queueIndex>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
functionApiName | String | 需要执行的函数apiName | 是  
param | Map | 执行函数时传入的参数 | 是  
queueIndex | Integer | 指定执行的队列（队列的下标，从0开始，当大于购买数量时做取模运算） | 是  
  
**Groovy 举例**
    
    
    Map param = [
      "map":[
        "a": 123,
        "b": "sdte"
      ]
    ]
    
    
    def (error,result,errorMessage) = Fx.function.asyncOnVipQueue("func_U4Oqt__c", param, 0)
    if(error){
        log.error("asyncOnVipQueue error: "+errorMessage)
        //1.使用报错终止执行
        //Fx.message.throwException("asyncOnVipQueue error "+errorMessage)
    
        //2.使用return终止执行
        //return;
    
        //3.继续执行
    } 
    log.info("traceId="+result)
    //dosomething
    
    

[Fx.file](../FileAPI/) [Fx.utils](../UtilsAPI/)

← [Fx.file](../FileAPI/) [Fx.utils](../UtilsAPI/)→ 

  * 跟随系统 
  * 浅色模式 
  * 深色模式 
  * 阅读模式 


