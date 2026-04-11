#  Fx.bpm

## # Fx.bpm

### # 1\. findInstances 查找指定对象和指定数据的所有业务流实例

> `Fx.bpm.findInstances(<String objectApiName>, <String state>, <String dataId>, <Integer pageSize>, <Integer pageNumber>)`

**参数说明**

入参格式

参数名称 | object | 描述 | 是否必填  
---|---|---|---  
objectApiName | String | 对象的ApiName | 是  
state | String | 业务流状态 | 是  
dataId | String | 数据Id | 是  
pageSize | Integer | 一页的数据数量，最大100条 | 是  
pageNumber | Integer | 当前页面 | 是  
  
出参格式

参数名称 | object | 描述  
---|---|---  
isError | Boolean | 是否报错  
data | object |   
message | String | 信息  
data | object | 描述  
---|---|---  
QueryResult | object |   
QueryResult | object | 描述  
---|---|---  
total | Integer | 总量  
dateList | List[object] | 返回的数据  
dateList | object | 描述  
---|---|---  
instanceId | String | 流程实例Id  
workflowName | String | 流程名称  
state | String | 状态  
applicantId | String | 流程发起人  
  
出参样例
    
    
    {
        "isError": false,
        "data": {
            "QueryResult": {
                "total": 1,
                "dateList": [
                    {
                        "instanceId": "66f3c627e268c669f62e2a3e",
                        "workflowName": "测试业务流",
                        "state": "in_progress",
                        "applicantId": "1014"
                    }
                ]
            }
        },
        "message": ""
    }
    
    

**Groovy 举例**
    
    
    def ret = Fx.bpm.findInstances("object_C6kha__c", "in_progress", "600558de3dacbe000167a1d9", 10, 1)
    log.info(ret)
    
    

**注意事项**

>   * 入参的state业务流状态，支持：in_progress进行中、pass通过、cancel取消 和 error异常
> 


### # 2\. findTaskList 查找业务流所有任务节点

> `Fx.bpm.findTaskList(<String instanceId>, <Integer pageSize>, <Integer pageNumber>)`

**参数说明**

入参格式

参数名称 | object | 描述 | 是否必填  
---|---|---|---  
instanceId | String | 业务流程实例Id | 是  
pageSize | Integer | 一页的数据数量，最大100条 | 是  
pageNumber | Integer | 当前页数 | 是  
  
出参格式

参数名称 | object | 描述  
---|---|---  
isError | Boolean | 是否报错  
data | List[Map] | 返回的数据  
message | String | 信息  
  
出参样例
    
    
    {
        "isError": false,
        "data": [
            {
                "taskId": "213312",
                "taskName": "这里是任务名称",
                "state": "in_progress"
            }, {
                "taskId": "213312e12",
                "taskName": "这里是任务名称1",
                "state": "in_progress"
            }
        ],
        "message": ""
    }
    
    

**Groovy 举例**
    
    
    def ret = Fx.bpm.findTaskList("600655f76cf582000145d366", 10, 1)
    log.info(ret)
    
    

**注意事项**

>   * 入参中，pageSize一页的数据数量，最大支持100条
> 


### # 3\. findTask 查找某个节点的详细信息

> `Fx.bpm.findTask(<String taskId>, <Boolean notGetData>)`

**参数说明**

入参格式

参数名称 | object | 描述 | 是否必填  
---|---|---|---  
taskId | String | 任务Id | 是  
notGetData | Boolean | 获取流程编辑任务的时候不获取对象数据 | 是  
  
出参格式

参数名称 | object | 描述  
---|---|---  
isError | Boolean |   
data | object |   
message | string |   
data | object | 描述  
---|---|---  
name | String |   
state | String |   
applicantId | String |   
apiName | String |   
dataId | String |   
candidateIds | List[String] |   
processIds | List |   
activityInstanceIds | List |   
  
出参样例
    
    
    {
      "isError" : false,
      "data" : {
          "name": "业务活动",
          "state": "in_progress",
          "applicantId": "0",
          "apiName": "object_k91i0__c",
          "dataId": "66f3c5c585821400013bd90e",
          "candidateIds": ["1000"],
          "processIds": [],
          "activityInstanceIds": "0"
      },
      "message" : ""
    }
    
    

**Groovy 举例**
    
    
    def ret = Fx.bpm.findTask("600655f76cf582000145d367", true)
    log.info(ret)
    
    

### # 4\. cancel 取消流程实例

> `Fx.bpm.cancel(<String instanceId>, <String reason>)`

**参数说明**

入参格式

参数名称 | object | 描述 | 是否必填  
---|---|---|---  
instanceId | String | 业务流程实例Id | 是  
reason | String | 取消原因 | 是  
  
出参格式

参数名称 | object | 描述  
---|---|---  
isError | Boolean | 是否报错  
data | Map | 返回的数据  
message | String | 信息  
  
出参样例
    
    
    {
      "isError" : false,
      "data" : {},
      "message" : ""
    }
    
    

**Groovy 举例**
    
    
    def ret = Fx.bpm.cancel("60058b414349d20001b32aef", "不要了")
    log.info(ret)
    
    

### # 5\. approval 对审批节点进行操作（不支持需要指定下一节点任务处理人的节点）

> `Fx.bpm.approval(<String taskId>, <String userId>, <String action>, <String opinion>)`

**参数说明**

入参格式

参数名称 | object | 描述 | 是否必填  
---|---|---|---  
taskId | String | 审批任务节点Id | 是  
userId | String | 审批处理Id | 是  
action | String | 审批操作类型(agree、reject) | 是  
opinion | String | 审批意见 | 是  
  
出参格式

参数名称 | object | 描述  
---|---|---  
isError | Boolean | 是否报错  
data | Map | 返回的数据  
message | String | 信息  
  
出参样例
    
    
    {
      "isError" : false,
      "data" : {},
      "message" : ""
    }
    
    

**Groovy 举例**
    
    
    def ret = Fx.bpm.approval("60058bd24349d20001b32af2", "1000", "agree", "绝对同意")
    log.info(ret)
    
    

### # 6\. complete 对业务节点进行完成操作

> `Fx.bpm.complete(<string taskId>, <string userId>, <string opinion>, <map map>)`

**参数说明**

入参格式

参数名称 | object | 描述 | 是否必填  
---|---|---|---  
taskId | string | 任务Id | 是  
userId | string | 用户Id | 是  
opinion | string | 可选参数，与map一并使用，处理意见 | 是  
map | map | 可选参数，与opinion一并使用，其他参数 | 是  
  
出参格式

参数名称 | object | 描述  
---|---|---  
isError | Boolean | 是否报错  
data | Map | 返回的数据  
message | String | 信息  
  
出参样例
    
    
    {
      "isError" : false,
      "data" : {},
      "message" : ""
    }
    
    

**Groovy 举例**
    
    
    //选择或新建关联对象类的业务流节点可以通过函数自动完成，可在第四个参数设置 key:"relatedObjectId" ->value:新建关联对象的id
    Map map = ["relatedObjectId": "5e16cc13e4817e0001ee1a3e"]
    def ret = Fx.bpm.complete("60058b414349d20001b32af0", "1000", "通过", map)
    log.info(ret)
    
    

### # 7\. changeCandidateIds 更换当前节点处理人

> `Fx.bpm.changeCandidateIds(<String taskId>, <List candidateIds>, <String opinion>)`

**参数说明**

入参格式

参数名称 | object | 描述 | 是否必填  
---|---|---|---  
taskId | String | 任务Id | 是  
candidateIds | List[string] | 需要更换的处理人 | 是  
opinion | String | 更换人的意见 | 是  
  
出参格式

参数名称 | object | 描述  
---|---|---  
isError | Boolean | 是否报错  
data | null |   
message | String | 触发返回信息  
  
出参样例
    
    
    {
        "isError": false,
        "data": null,
        "message": "success!"
    }
    
    

**Groovy 举例**
    
    
    def ret = Fx.bpm.changeCandidateIds("600655f76cf582000145d367", [1000, 1001, 1002])
    log.info(ret)
    
    

### # 8\. startInstance 触发业务流

> `Fx.bpm.startInstance(<String id>, <String objectId>, <String entityId>)`

**参数说明**

入参格式

参数名称 | object | 描述 | 是否必填  
---|---|---|---  
id | String | 业务流定义Id | 是  
objectId | String | 对象数据Id | 是  
entityId | String | 对象ApiName | 是  
  
出参格式

参数名称 | object | 描述  
---|---|---  
isError | Boolean | 是否报错  
data | String | 触发的实例Id  
message | string |   
  
出参样例
    
    
    {
        "isError": false,
        "data": "触发的实例Id",
        "message": ""
    }
    
    

### # 8\. 触发业务流,通过sourceWorkflowId

> `Fx.bpm.start(<String sourceWorkflowId>, <String objectId>, <String entityId>)`

**参数说明**

入参格式

参数名称 | 触发业务流程,通过sourceWorkflowId触发 | 描述 | 是否必填  
---|---|---|---  
sourceWorkflowId | String | 业务流sourceWorkflowId | 是  
objectId | String | 对象数据Id | 是  
entityId | String | 对象ApiName | 是  
  
出参格式

参数名称 | object | 描述  
---|---|---  
isError | Boolean | 是否报错  
data | String | 触发的实例Id  
message | string |   
  
出参样例
    
    
    {
        "isError": false,
        "data": "触发的实例Id",
        "message": ""
    }
    
    

**Groovy 举例**
    
    
    /**
     * @author 崔永旭
     * @codeName triggerBpm
     * @description triggerBpm
     * @createTime 2025-03-12
     * @bindingObjectLabel 
     * @bindingObjectApiName object_Yw3f8__c
     * @函数需求编号
     */
    
    String objectId = context.data._id
    String entityId = context.data.object_describe_api_name
    
    
    def result = Fx.bpm.start( "67d148372602fe00017f1ad5", objectId,entityId)
    log.info(result)
    
    

### # 9\. getDefinitionList 获取业务流定义列表

> `Fx.bpm.getDefinitionList(<String entityId>, <Integer page>, <Integer pageSize>)`

**参数说明**

入参格式

参数名称 | object | 描述 | 是否必填  
---|---|---|---  
entityId | String | 对象ApiName | 是  
page | Integer | 页码 | 是  
pageSize | Integer | 查询数量 | 是  
  
出参格式

参数名称 | object | 描述  
---|---|---  
isError | Boolean | 是否报错  
data | Map[object] | 定义列表list  
message | string |   
data | object | 描述  
---|---|---  
id | String | 流程定义id  
sourceWorkflowId | String | 流程版本定义id  
workflowName | String | 流程定义名称  
  
出参样例
    
    
    {
        "isError": false,
        "data": [
            {
                "id": "流程定义id1",
                "sourceWorkflowId": "流程版本定义id1",
                "workflowName": "流程定义名称1"
            },
            {
                "id": "流程定义id2",
                "sourceWorkflowId": "流程版本定义id2",
                "workflowName": "流程定义名称2"
            }
        ],
        "message": ""
    }
    
    

**Groovy 举例**
    
    
    //根据对象ApiName获取定义
    def(Boolean error, Map data, String message) = Fx.bpm.getDefinitionList("FundReturnBackObj", 1, 10)
    if(false == error){
      //获取定义列表
      List item = data['data'] as List
    
      item.each{
        //根据流程定义名称获取相关定义
        i ->if('被函数获取的定义' == i['workflowName']){
          //触发业务流
          Fx.bpm.startInstance(i['id'] as String, '62c39d5d71f9010001ae0ea9', 'FundReturnBackObj')
        }
      }
    }
    
    

### # 10\. delayTaskImmediatelyExecute 业务流等待节点立即执行

> `Fx.bpm.delayTaskImmediatelyExecute(<String taskId>)`

**参数说明**

入参格式

参数名称 | object | 描述 | 是否必填  
---|---|---|---  
taskId | String | 任务Id | 是  
  
出参格式

参数名称 | APIResult | 描述  
---|---|---  
isError | Boolean | 是否错误  
data | Map | 返回的数据  
message | String | 信息  
  
出参样例
    
    
    {
      "isError" : false,
      "data" : {},
      "message" : ""
    }
    
    

**Groovy 举例**
    
    
    APIResult res = Fx.bpm.delayTaskImmediatelyExecute("62f320a7c6fa24292be4f830");
    if(res.isError() || res.message() != ""){
      log.info(res.message())
    }else{
      log.info("业务流自动节点立即执行成功")
    }
    
    

### # 11\. refreshHandler 重新解析任务处理人

> `Fx.bpm.refreshHandler(<String taskId>)`

**参数说明**

入参格式

参数名称 | object | 描述 | 是否必填  
---|---|---|---  
taskId | String | 任务Id | 是  
  
出参格式

参数名称 | object | 描述  
---|---|---  
isError | Boolean | 是否报错  
data | object |   
message | string |   
  
出参样例
    
    
    {
        "isError": false,
        "data": {},
        "message": ""
    }
    
    

**Groovy 举例**
    
    
    def taskId = "6343e4d780f4841c79cbcae0"
    def res = Fx.bpm.refreshHandler(taskId)
    log.info(res)
    
    

### # 11\. operate操作任务

> `Fx.bpm.operate(<String taskId>, <String type>, <String opinion>)`

**参数说明**

入参格式

参数名称 | object | 描述 | 是否必填  
---|---|---|---  
taskId | String | 任务id | 是  
type | String | 操作类型；suspend——暂停任务；resume——继续任务； | 是  
opinion | String | 意见 | \--  
  
出参格式

参数名称 | APIResult | 描述  
---|---|---  
errorMessage | string | 异常信息  
  
出参样例
    
    
    {
        "errorMessage": "当前任务不能暂停，请刷新页面"
    }
    
    

**Groovy 举例**
    
    
    def taskId = "684ba0ac71dd2917daf12048"
    def type = "suspend"
    
    def(Boolean error, Map data, String errorMessage) = Fx.bpm.operate(taskId, type, null, null)
    if(error) {
      log.info(errorMessage)
    }
    
    

### # 12\. findDelayTask 根据objectId或workflowInstanceId获取等待节点

> `Fx.bpm.findDelayTask(<String objectId>, <String workflowInstanceId>, <Integer pageNumber>, <Integer pageSize>)`

**参数说明**

入参格式

参数名称 | object | 描述 | 是否必填  
---|---|---|---  
objectId | String | 数据Id | 是  
workflowInstanceId | String | 业务流程实例Id | 是  
pageNumber | Integer | 查询页码 | 是  
pageSize | Integer | 查询数量 | 是  
  
出参格式

参数名称 | object | 描述  
---|---|---  
isError | Boolean | 是否报错  
data | Map[object] | 任务列表list  
message | string |   
data | object | 描述  
---|---|---  
id | String | 任务id  
name | String | 任务名称  
state | String | 任务状态  
  
出参样例
    
    
    {
        "isError": false,
        "data": [
            {
                "id": "任务id1",
                "name": "任务1",
                "state": "in_progress"
            },
            {
                "id": "任务id2",
                "name": "任务2",
                "state": "error"
            }
        ],
        "message": ""
    }
    
    

**Groovy 举例**
    
    
    def objectId = "63a403eb314aa80001bd9b82"
    def instanceId = "63a405d45513f84c58c2b66c"
    Integer pageNumber = 1
    Integer pageSize = 3
    //根据数据ID查延迟节点
    def(Boolean err1, Map data1, String msg1) = Fx.bpm.findDelayTask(objectId, null, pageNumber, pageSize)
    if (err1) {
      log.info("error: " + msg1)
    } else {
      log.info(data1)
    }
    //根据实例ID查延迟节点
    def(Boolean err2, Map data2, String msg2) = Fx.bpm.findDelayTask(null, instanceId, pageNumber, pageSize)
    if (err2) {
      log.info("error: " + msg2)
    } else {
      log.info(data2)
    }
    
    

[Fx.approval](../ApprovalAPI/) [Fx.template](../TemplateAPI/)

← [Fx.approval](../ApprovalAPI/) [Fx.template](../TemplateAPI/)→ 

  * 跟随系统 
  * 浅色模式 
  * 深色模式 
  * 阅读模式 


