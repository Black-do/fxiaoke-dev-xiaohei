#  Fx.stage

## # Fx.stage

### # 1\. trigger 触发阶段推进器

> `Fx.stage.trigger(<String entityId>, <String objectId>, <String userId>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
entityId | String | 发起对象apiName | 是  
objectId | String | 发起对象的数据id | 是  
userId | String | 阶段推进器发起人的ID | 是  
  
出参格式

参数名称 | APIResult | 描述  
---|---|---  
workflowInstanceId | string | 阶段推进器实例id  
  
出参样例
    
    
    {
        "workflowInstanceId": "66f50d510cf87e114caaa447"
    }
    
    

**Groovy 举例**
    
    
    def(Boolean error, Map data, String errorMessage) = Fx.stage.trigger("object_qep6N__c", "617f9b7340beec0001b9b14e", "1000")
    if (error) {
      log.info(errorMessage)
    } else{
      log.info(data)
    }
    
    

### # 2\. matchDef 匹配可以触发的阶段推进器(非商机2.0)

> `Fx.stage.matchDef(<String entityId>, <String objectId>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
entityId | String | 发起对象apiName | 是  
objectId | String | 发起对象的数据id | 是  
  
出参格式

参数名称 | APIResult | 描述  
---|---|---  
stagePropellerName | string | 阶段推进器定义名称  
isCurrentDef | boolean | 当前实例是否为当前定义  
sourceWorkflowId | string | 匹配上的阶段推进器定义id  
hasInstance | boolean | 是否存在流程实例  
  
出参样例
    
    
    {
      "sourceWorkflowId": "66f3f79122907b00016f0849",
      "isCurrentDef": true,
      "hasInstance": true,
      "stagePropellerName": "非必须完成测试"
    }
    
    

**Groovy 举例**
    
    
    def api_name = context.data.object_describe_api_name as String
    def object_id = context.data._id as String
    log.info(api_name + "," + object_id)
    def match_result = Fx.stage.matchDef(api_name, object_id, "1000")
    log.info(match_result)
    
    

### # 3\. change 切换阶段推进器(非商机2.0 ， 商机2.0对象不允许使用这个函数来操作)

> `Fx.stage.change(<String entityId>, <String objectId>, <String sourceWorkflowId>, <String stageId>, <String userId>)`

**参数说明**

入参格式

参数名称 | object | 描述 | 是否必填  
---|---|---|---  
entityId | String | 对象ApiName | 是  
objectId | String | 数据Id | 是  
sourceWorkflowId | String | 由预匹配得到的阶段推进器的定义Id，可参考Fx.stage.matchDef | 是  
stageId | String | 初始化阶段Id | 是  
userId | String | 用户Id | 是  
  
出参格式

参数名称 | object | 描述  
---|---|---  
isError | Boolean | 是否报错  
data | Map | 返回的数据  
message | String | 信息  
  
出参样例
    
    
    {
        "isError": false,
        "data": {},
        "message": ""
    }
    
    

**Groovy 举例**
    
    
    // 非商机2.0对象切换阶段推进器
    def match_result = Fx.stage.change("object_qep6N__c", "66f61a1f3005aa0001d14b54", "61a87f17bb3d4700017f5a78", "1", "1000")
    log.info(match_result)
    
    // 注意：商机2.0对象，建议使用Fx.object.update修改「销售流程」字段来实现切换阶段推进器。
    // 以下代码仅供参考:
    String sourceWorkflowId = "640ac64fd7d00c767d0d9641"  //要切换的阶段推进器的sourceWorkflowId
    String stageId="1"  //切换阶段推进器后，初始化的阶段ID
    String objectAPIName = "NewOpportunityObj"
    String objectId = context.objectIds[0]
    Map updateData = [
      "sales_process_id":sourceWorkflowId,
      "sales_stage":stageId
    ]
    def (Boolean error, Map data, String errorMessage) = Fx.object.update( objectAPIName,  objectId, updateData,  false, false)
    if (error) {
      log.info("error:" + errorMessage )
    }
    log.info(data)
    
    

**注意事项**

>   * 仅支持非商机2.0对象，商机2.0对象不允许使用该函数切换阶段推进器
> 


### # 4\. changeTaskHandler 更换处理人

> `Fx.stage.changeTaskHandler(<String taskId>, <List candidateIds>, <String userId>)`

**参数说明**

入参格式

参数名称 | object | 描述 | 是否必填  
---|---|---|---  
taskId | String | 任务Id | 是  
candidateIds | List | 要更换的处理人Id集合 | 是  
userId | String | 用户Id | 是  
  
出参格式

参数名称 | object | 描述  
---|---|---  
isError | Boolean | 是否报错  
data | Map | 返回的数据  
message | String | 信息  
  
出参样例
    
    
    {
        "isError": false,
        "data": {},
        "message": ""
    }
    
    

**Groovy 举例**
    
    
    def rst = Fx.stage.changeTaskHandler("6343ff9e80f4841c79cbcb5c", ["1000"], "1106")
    log.info(rst)
    
    

### # 5\. completeCreateAndRelatedTask 完成选择关联的任务

> `Fx.stage.completeCreateAndRelatedTask(<String taskId>, <String entityId>, <String objectId>, <String ignoreNoBlockValidate>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
taskId | String | 任务id | 是  
entityId | String | 创建对象的apiname | \--  
objectId | String | 创建对象的数据id，如果有多个id，id之间用竖线隔开 | \--  
ignoreNoBlockValidate | String | 忽略非阻断异常,完成任务时如果出现非阻断的异常，忽略异常继续执行 | \--  
  
出参格式

参数名称 | APIResult | 描述  
---|---|---  
currentStageTaskAllCompleted | boolean | 当前阶段下的任务是否全部完成  
  
出参样例
    
    
    {
        "currentStageTaskAllCompleted": false
    }
    
    

**Groovy 举例**
    
    
    def rst = Fx.stage.completeCreateAndRelatedTask("6343ff9e80f4841c79cbcb5c", "object_qep6N__c", "617f9b7340beec0001b9b14e|617f9b7340beec0001b9b14f", "1106")
    log.info(rst)
    
    

### # 6\. updateAndCompleteTask 更新并完成任务

> `Fx.stage.updateAndCompleteTask(<String taskId>, <Map data>, <String userId>)`

**参数说明**

入参格式

参数名称 | object | 描述 | 是否必填  
---|---|---|---  
taskId | String | 任务Id | 是  
data | Map | 要更新的数据信息 | 是  
userId | String | 用户Id | 是  
  
出参格式

参数名称 | object | 描述  
---|---|---  
isError | Boolean | 是否报错  
data | Map | 返回的数据  
message | String | 信息  
  
出参样例
    
    
    {
        "isError": true,
        "data": null,
        "message": "任务不存在，请确认"
    }
    
    

**Groovy 举例**
    
    
    def data = ["name": "value"]
    def rst = Fx.stage.updateAndCompleteTask("6343ff9e80f4841c79cbcb5c", data, "1001")
    log.info(rst)
    
    

### # 7\. reactive 重新激活

> `Fx.stage.reactive(<String workflowInstanceId>, <String activeStageId>, <Map data>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
workflowInstanceId | String | 流程实例id | 是  
activeStageId | String | 要跳转的阶段id | 是  
data | Map | 重新激活表单数据 | \--  
  
出参格式

参数名称 | APIResult | 描述  
---|---|---  
success | boolean | 是否成功激活  
ruleMessage | object | 重新激活阻断异常信息  
skipInNonBlockMessage | string | 重新激活非阻断异常信息  
jobId | string | 当阶段跳转为异步时，通过该值获取跳转状态  
versionCheckBlocked | boolean | 更新数据时是否编辑冲突  
dataConflicts | object | 数据冲突的内容  
  
出参样例
    
    
    {
        "success": true
    }
    
    

**Groovy 举例**
    
    
    //重新激活函数demo
    //实例id
    def workflowInstanceId="62c3da4e0d9f997b27dfd90e"
    //要跳转的阶段
    def activeStageId="47u3S02Gz"
    //重新激活表单填写
    Map data= ["field_0mvhC__c": "90"]
    def userId= "1000"
    def(boolean error, Map result, String message) = Fx.stage.reactive(workflowInstanceId, activeStageId, data, userId)
    if (error) {
      log.info("error :" + message)
    } else {
      log.info(result)
    }
    
    

### # 8\. reactiveValidate 重新激活校验

> `Fx.stage.reactiveValidate(<String workflowInstanceId>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
workflowInstanceId | String | 需要激活的实例id | 是  
  
出参格式

参数名称 | APIResult | 描述  
---|---|---  
success | boolean | 是否校验通过  
stageFieldApiName | string | 阶段字段apiname  
ruleMessage | Map | 重新激活校验阻断异常信息  
reactiveTaskData | object | 重新激活表单的数据  
canMoveToStageIds | List[string] | 可激活的目标阶段id  
skipInNonBlockMessage | string | 重新激活校验非阻断异常信息  
  
出参样例
    
    
    {
        "success": true,
        "canMoveToStageIds": [
            "AaSah2ef5",
            "xr1ER6AL8"
        ],
        "stageFieldApiName": "field_2xqgf__c"
    }
    
    

**Groovy 举例**
    
    
    //重新激活校验函数接口demo
    //实例id
    def workflowInstanceId= "62c3da4e0d9f997b27dfd90e"
    def userId = context.userId
    def(boolean error, Map result, String message) = Fx.stage.reactiveValidate(workflowInstanceId, userId)
    if (error) {
      log.info("error: " + message)
    } else {
      log.info(result)
    }
    
    

### # 9\. getInstanceInfo 获取对象的阶段实例信息(form下发layout ， desc和data)

> `Fx.stage.getInstanceInfo(<String entityId>, <String objectId>)`

**参数说明**

入参格式

参数名称 | object | 描述 | 是否必填  
---|---|---|---  
entityId | String | 对象ApiName | 是  
objectId | String | 数据Id | 是  
  
出参格式

参数名称 | object | 描述  
---|---|---  
isError | Boolean | 是否报错  
data | Map | 返回的数据  
message | String | 信息  
  
出参样例
    
    
    {
        "isError": false,
        "data": {},
        "message": ""
    }
    
    

**Groovy 举例**
    
    
    def objectId = "63f6d5b94315da0001585821";  //数据id
    def entityId = "object_8F03i__c";       //对象apiName
    def (Boolean error, Map data, String message) = Fx.stage.getInstanceInfo(entityId, objectId);
    if (error) {
        log.info("error:" + message)
    }
    log.info(data)
    
    

### # 10\. regenerateHandler 重新解析任务处理人

> `Fx.stage.regenerateHandler(<String stageTaskId>, <String opinion>)`

**参数说明**

入参格式

参数名称 | object | 描述 | 是否必填  
---|---|---|---  
stageTaskId | String | 阶段任务Id | 是  
opinion | String | 意见 | 是  
  
出参格式

参数名称 | object | 描述  
---|---|---  
isError | Boolean | 是否报错  
data | Map | 返回的数据  
message | String | 信息  
  
出参样例
    
    
    {
        "isError": true,
        "data": {},
        "message": "Fx.stage.regenerateHandler error. status code:400"
    }
    
    

**Groovy 举例**
    
    
    def stageTaskId = "63f6d7a3363f0627220ac287";   //阶段ID
    def opinion = "数据负责人变化自动刷新任务处理人";   //意见
    def (Boolean error, Map data, String message) = Fx.stage.regenerateHandler(stageTaskId, opinion);
    if (error) {
        log.info("error:" + message)
    }
    log.info(data)
    
    

### # 11\. completeTask 完成任务

> `Fx.stage.completeTask(<String taskId>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
taskId | String | 任务id | 是  
  
出参格式

参数名称 | APIResult | 描述  
---|---|---  
currentStageTaskAllCompleted | boolean | 当前阶段下的任务是否全部完成  
blockMessage | string | 函数阻断异常信息  
nonBlockMessage | string | 函数非阻断异常信息  
ruleMessage | object | 校验规则异常信息  
  
出参样例
    
    
    {
        "currentStageTaskAllCompleted": false
    }
    
    

**Groovy 举例**
    
    
    //注：完成编辑任务请使用Fx.stage.updateAndCompleteTask；
    // 完成创建关联对象任务请使用Fx.stage.completeCreateAndRelatedTask
    def taskId = "67e0feea650b3007ce0ee6b7" 
    def userId = "1002" 
    
    // blockMessage：函数阻断异常信息，nonBlockMessage：函数非阻断异常信息，ruleMessage：校验规则异常信息
    def message = Fx.stage.completeTask(taskId, userId)[1]
        .with { data -> 
            data["blockMessage"] ?: data["nonBlockMessage"] ?: data["ruleMessage"] 
        }
    
    // 记录日志（明确提示未找到时的场景）
    if (message) {
        log.error("异常信息: ${message}")
    } else {
        log.error("未发现任何异常信息")
    }
    
    

### # 12\. getInstanceTasks 根据entityId和objectId获取阶段推进器实例中的所有任务

> `Fx.stage.getInstanceTasks(<String entityId>, <String objectId>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
entityId | String | 对象apiName | 是  
objectId | String | 数据id | 是  
  
出参格式

参数名称 | APIResult | 描述  
---|---|---  
tasks | List[object] | 阶段推进器实例中所有的任务  
tasks | object | 描述  
---|---|---  
name | string | 任务名称  
taskId | string | 任务id  
executionType | string | 任务类型，update——编辑任务，addRelatedObject——选择或创建，batchUpdateDetailObj——批量编辑，empty——空任务，operateObject——操作对象  
state | string | 任务状态  
  
出参样例
    
    
    {
        "tasks": [
            {
                "executionType": "update",
                "name": "编辑",
                "state": "pass",
                "taskId": "66f50d510cf87e114caaa44c"
            }
        ]
    }
    
    

**Groovy 举例**
    
    
    def entityId = "NewOpportunityObj"          //对象apiName
    def objectId = context.data._id as String   //数据id
    def ret = Fx.stage.getInstanceTasks(entityId, objectId)
    log.info(ret)
    
    

### # 13\. getBySourceWorkflowId 根据sourceWorkflowId获取阶段推进器定义

> `Fx.stage.getBySourceWorkflowId(<String sourceWorkflowId>)`

**参数说明**

入参格式

参数名称 | object | 描述 | 是否必填  
---|---|---|---  
sourceWorkflowId | String | 阶段推进器ApiName(阶段推进器的唯一标识) | 是  
  
出参格式

参数名称 | object | 描述  
---|---|---  
isError | Boolean | 是否报错  
data | Map | 返回的数据  
message | String | 信息  
  
出参样例
    
    
    {
        "isError": false,
        "data": {
            "modifier": "1002",
            "description": "",
            "rule": {
                "deleted": false,
                "conditionPattern": "",
                "workflowSrcId": "66f61a1f3005aa0001d14b54",
                "entityId": "object_scheduled_object__c",
                "ruleId": "66f61a1f0cf87e114caaa717"
            }
        },
        "message": ""
    }
    
    

**Groovy 举例**
    
    
    def(boolean error, Map data, String message) = Fx.stage.getBySourceWorkflowId("667bc6b9ed7d04000171daaf")
    if (error) {
      log.info("error: " + message)
    } else {
      log.info(data)
    }
    
    

**注意事项**

>   * 该函数用于根据阶段推进器的sourceWorkflowId获取阶段推进器的详细信息，由于返回的数据较长，出参样例中只展示了一部分信息，具体可以打印日志来查看完整的出参结构
> 


### # 14\. cancel 根据对象apiName和数据ID终止数据上的阶段推进器实例（仅支持非商机2.0对象的实例）

> `Fx.stage.cancel(<String entityId>, <String objectId>)`

**参数说明**

入参格式

参数名称 | object | 描述 | 是否必填  
---|---|---|---  
entityId | String | 对象ApiName | 是  
objectId | String | 数据Id | 是  
  
出参格式

参数名称 | object | 描述  
---|---|---  
isError | Boolean | 是否报错  
data | Map | 返回的数据  
message | String | 信息  
  
出参样例
    
    
    {
        "isError": true,
        "data": {},
        "message": "不存在阶段流程实例"
    }
    
    

**Groovy 举例**
    
    
    def entityId = "object_8F03i__c"
    def objectId = context.data._id
    def(Boolean error, Map data, String message) = Fx.stage.cancel(entityId, objectId)
    if (error) {
        log.info("error:" + message)
    }
    log.info(data)
    
    

**注意事项**

>   * 该函数仅支持 非商机2.0 对象的实例
> 


[Fx.cache](../CacheAPI/) [Fx.lock](../LockAPI/)

← [Fx.cache](../CacheAPI/) [Fx.lock](../LockAPI/)→ 

  * 跟随系统 
  * 浅色模式 
  * 深色模式 
  * 阅读模式 


