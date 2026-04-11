#  Fx.work

## # Fx.work

### # 1\. createTask 发任务

> `Fx.work.createTask(<string title>, <string description>, <integer deadLine>, <object executeUsers>, <object atUsers>)`

**参数说明**

入参格式

参数名称 | object | 描述 | 是否必填  
---|---|---|---  
title | string |  | 是  
description | string |  | 是  
deadLine | integer |  | 是  
executeUsers | object |  | 是  
atUsers | object |  | 是  
executeUsers | object | 描述 | 是否必填  
---|---|---|---  
users | array[string] |  | 是  
departments | array[string] |  | 是  
atUsers | object | 描述 | 是否必填  
---|---|---|---  
users | array[string] |  | 是  
departments | array[string] |  | 是  
  
出参格式

出参样例
    
    
    {}
    
    

**Groovy 举例**
    
    
    DateTime deadLine = DateTime.now + 1.days
    Fx.work.createTask("hello", "world", deadLine, [users: ["1059"]], [users: ["1059","1025"],departments:["253937"]])
    
    

**注意事项**

>   * executeUsers map keys : "users" 用户 ，"departments" 部门
>   * atUsers map keys : "users" 用户 ，"departments" 部门
> 


### # 2\. createTaskV2 创建任务v2，返回任务id

> `Fx.work.createTaskV2(<string title>, <string description>, <integer deadLine>, <boolean multiExecute>, <object executeUsers>, <object atUsers>, <array objects>)`

**参数说明**

入参格式

参数名称 | object | 描述 | 是否必填  
---|---|---|---  
title | string |  | 是  
description | string |  | 是  
deadLine | integer |  | 是  
multiExecute | boolean |  | 是  
executeUsers | object |  | 是  
atUsers | object |  | 是  
objects | array[object] |  | 是  
executeUsers | object | 描述 | 是否必填  
---|---|---|---  
users | array[string] |  | 是  
departments | array[string] |  | 是  
atUsers | object | 描述 | 是否必填  
---|---|---|---  
users | array[string] |  | 是  
departments | array[string] |  | 是  
objects | object | 描述 | 是否必填  
---|---|---|---  
object_api_name | string |  | 是  
id | string |  | 是  
  
出参格式

参数名称 | object | 描述  
---|---|---  
taskId | string |   
  
出参样例
    
    
    {"taskId":"taskId"}
    
    

**Groovy 举例**
    
    
    DateTime deadLine = DateTime.now + 1.days
    List objects = [
      [object_api_name: "object_l9348__c", id: "60d53e038bc25c00016c75f6"],
      [object_api_name: "ContractObj", id: "60f54c9c4fc0fa000107c1f7"],
      [object_api_name: "ContractObj", id: "8e82821584474cb79ae693c267cc7395"]
    ]
    def (Boolean error, String taskId, String errorMessage) = Fx.work.createTaskV2("hello", "world", deadLine, false, [users: ["1000"]], [users: ["1000"]], objects)
    if (error) {
      log.info(errorMessage)
    } else {
      log.info(taskId)
    }
    
    

### # 3\. executeTask 执行任务

> `Fx.work.executeTask(<string taskId>, <integer userId>)`

**参数说明**

入参格式

参数名称 | object | 描述 | 是否必填  
---|---|---|---  
taskId | string |  | 是  
userId | integer |  | 是  
  
出参格式

参数名称 | object | 描述  
---|---|---  
postId | string |   
  
出参样例
    
    
    {
        "postId": "taskId"
    }
    
    

**Groovy 举例**
    
    
    Fx.work.executeTask("3b4d8c49b207417f99941688c8ee719f", "1017")
    
    

### # 4\. cancelTask 取消任务

> `Fx.work.cancelTask(<string taskId>)`

**参数说明**

入参格式

参数名称 | object | 描述 | 是否必填  
---|---|---|---  
taskId | string |  | 是  
  
出参格式

出参样例
    
    
    {
        "$schema": "http://json-schema.org/draft-07/schema#",
        "type": "object",
        "additionalProperties": false
    }
    
    

**Groovy 举例**
    
    
    Fx.work.cancelTask("3b4d8c49b207417f99941688c8ee719f")
    
    

### # 5\. createSchedule 创建日程绑定业务对象

> `Fx.work.createSchedule(<string content>, <integer beginTime>, <integer endTime>, <boolean isFullDate>, <boolean needReceipt>, <array remindTimes>, <object attenders>, <array objects>)`

**参数说明**

入参格式

参数名称 | object | 描述 | 是否必填  
---|---|---|---  
content | string |  | 是  
beginTime | integer |  | 是  
endTime | integer |  | 是  
isFullDate | boolean |  | 是  
needReceipt | boolean |  | 是  
remindTimes | array[string] |  | 是  
attenders | object |  | 是  
objects | array[object] |  | 是  
attenders | object | 描述 | 是否必填  
---|---|---|---  
users | array[string] |  | 是  
departments | array[string] |  | 是  
objects | object | 描述 | 是否必填  
---|---|---|---  
object_api_name | string |  | 是  
id | string |  | 是  
  
出参格式

参数名称 | object | 描述  
---|---|---  
feedId | string |   
  
出参样例
    
    
    {
        "feedId": "feedId"
    }
    
    

**Groovy 举例**
    
    
    DateTime endTime = DateTime.now + 1.hours;
    def ret = Fx.work.createSchedule("hello", DateTime.now(), endTime , false, false, [RemindTime.BEGIN()], [users: ["1001","1017","1018"]], [[apiName:"LeadsObj", dataId:"5dc276e1a25b1800018dafe9"],[apiName:"AccountObj", dataId:"5f3f86136ede600001da386e"]]);
    
    

**参考对象**

  * 参考RemindTime.BEGIN.FIVE_MINUTES_AGO.FIFTEEN_MINUTES_AGO.THIRTY_MINUTES_AGO.ONE_HOURS_AGO.TWO_HOURS_AGO



**注意事项**

>   * atUsers map keys : "users" 用户 ，"departments" 部门
>   * object keys : "apiName" 对象API名称 ，"dataId" 业务数据Id
> 


### # 6\. feedBatchAddCcEmployeeToFeeds 为一组FeedId增加抄送人

> `Fx.work.feedBatchAddCcEmployeeToFeeds(<array feedIds>, <integer ccEmployeeId>)`

**参数说明**

入参格式

参数名称 | object | 描述 | 是否必填  
---|---|---|---  
feedIds | array[integer] |  | 是  
ccEmployeeId | integer |  | 是  
  
出参格式

参数名称 | object | 描述  
---|---|---  
succeedFeedIds | array[integer] |   
failedFeedIds | array[integer] |   
failedReason | string |   
  
出参样例
    
    
    {
        "succeedFeedIds": [
            100000006,
            100000004
        ],
        "failedFeedIds": [
            100000003,
            100000002
        ],
        "failedReason": "xxx"
    }
    
    

**Groovy 举例**
    
    
    List feedIds = [100000006,100000004,100000003,100000002]
    Integer ccEmployeeId = 1105
    def(Boolean error, Map data, String errorMessage) = Fx.work.feedBatchAddCcEmployeeToFeeds(feedIds, ccEmployeeId)
    log.info(ret)
    if (error) {
      log.info(errorMessage)
    } else{
      log.info(data)
    }
    
    

### # 7\. followUpSearchResourceListByUUID 查询跟进动态里的FeedId

> `Fx.work.followUpSearchResourceListByUUID(<string objectApiName>, <string objectId>, <integer fromFeedId>, <integer limit>)`

**参数说明**

入参格式

参数名称 | object | 描述 | 是否必填  
---|---|---|---  
objectApiName | string |  | 是  
objectId | string |  | 是  
fromFeedId | integer |  | 是  
limit | integer |  | 是  
  
出参格式

参数名称 | object | 描述  
---|---|---  
feedIds | array[integer] |   
hasMore | boolean |   
  
出参样例
    
    
    {
        "feedIds": [
            100000006,
            100000004
        ],
        "hasMore": true
    }
    
    

**Groovy 举例**
    
    
    String objectApiName = "AccountObj"
    String objectId = "631859a4cd0f460001e69bf2"
    Long fromFeedId = 100000006
    Integer limit = 2
    def(Boolean error, Map data, String errorMessage) = Fx.work.followUpSearchResourceListByUUID(objectApiName, objectId, fromFeedId, limit)
    log.info(ret)
    if (error) {
      log.info(errorMessage)
    } else{
      log.info(data)
    }
    
    

## # 参考类 com.fxiaoke.functions.enums.RemindTime

### # 字段说明

参数名称 | object | 2小时前 1小时前 30分钟前 15分钟前 5分钟前 开始时 Created by liyiguang on 2018/9/20.  
---|---|---  
  
[Fx.crm](../CRMAPI/) [Fx.random](../RandomAPI/)

← [Fx.crm](../CRMAPI/) [Fx.random](../RandomAPI/)→ 

  * 跟随系统 
  * 浅色模式 
  * 深色模式 
  * 阅读模式 


