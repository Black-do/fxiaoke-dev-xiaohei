#  Fx.approval

## # Fx.approval

### # 1\. findInstances 返回指定对象和指定数据（可选）的所有审批实例

> `Fx.approval.findInstances(<String entityId>, <List<String> state>, <String objectId>, <Integer limit>, <Integer skip>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
entityId | String | 所属对象 | 是  
state | `List<String>` | 流程状态.in_progress:进行中;pass:已完成;cancel:撤回;reject:驳回 | 是  
objectId | String | 数据id | 是  
limit | Integer | 需要多少条数据 | 是  
skip | Integer | 从第几条开始获取 | 是  
  
出参格式

参数名称 | object | 描述  
---|---|---  
error | boolean | 是否存在异常  
data | object | 结果  
errorMessage | string | 存在异常时返回异常信息  
data | object | 结果  
---|---|---  
size | integer | 本次返回数据数  
total | integer | 总数据数  
dataList | array[object] | 结果集  
dataList | object | 描述  
---|---|---  
owner | array[string] | 流程发起人  
submitter | array[string] | 流程提交人  
instanceId | string | 实例id  
dataId | string | 数据id  
createTime | integer | 流程发起时间  
approvalApiName | string | 流程定义主版本  
approvalName | string | 流程定义名称  
endTime | integer | 流程结束时间  
  
出参样例
    
    
    {
        "error": false,
        "data": {
            "size": 1,
            "total": 1,
            "dataList": [
                {
                    "owner": [
                        "1002"
                    ],
                    "submitter": [
                        "1002"
                    ],
                    "instanceId": "66f2a4856b07ab1b4ebad7e5",
                    "dataId": "66f2a484928b280007aa6dd8",
                    "createTime": 1727177862204,
                    "approvalApiName": "apprZVJ6E46RHG__crmappr",
                    "approvalName": "审批流-子流程使用",
                    "endTime": 0
                }
            ]
        },
        "errorMessage": ""
    }
    
    

**Groovy 举例**
    
    
    QueryResult queryResult = Fx.approval.findInstances((String) context.data.object_describe_api_name, ["in_progress"], (String) context.data._id, 10, 0)[1];
    log.info(queryResult)
    
    if (queryResult != null) {
        //获取进行中的审批流实例,默认情况下只会有一条进行中的流程实例
        List dataList = (List) queryResult["dataList"]
        def instance = dataList[0]
        log.info("instance:" + instance)
    
    } else {
        log.info("未查询到当前数据存在审批流实例,请检查设置参数")
    }
    
    

### # 2\. findInstances 查询对象上的审批实例（查询并不是实时的，有延迟，实时查询可以参考乐享文章：实时查询审批流的函数）

> `Fx.approval.findInstances(<String entityId>, <List<String> state>, <String objectId>, <Integer limit>, <Integer skip>, <ActionAttribute attribute>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
entityId | String | 所属对象 | 是  
state | `List<String>` | 流程状态.in_progress:进行中;pass:已完成;cancel:撤回;reject:驳回 | 是  
objectId | String | 数据id | 是  
limit | Integer | 需要多少条数据 | 是  
skip | Integer | 从第几条开始获取 | 是  
attribute | ActionAttribute | 本次操作的属性设置 | \--  
attribute | ActionAttribute | 本次操作的属性设置 | 是否必填  
---|---|---|---  
forceQueryFromDB | Boolean | 是否强制从数据库中查询，默认为false | \--  
  
出参格式

参数名称 | object | 描述  
---|---|---  
error | boolean | 是否存在异常  
data | object | 结果  
errorMessage | string | 存在异常时返回异常信息  
data | object | 结果  
---|---|---  
size | integer | 本次返回数据数  
total | integer | 总数据数  
dataList | array[object] | 结果集  
dataList | object | 描述  
---|---|---  
owner | array[string] | 流程发起人  
submitter | array[string] | 流程提交人  
instanceId | string | 实例id  
dataId | string | 数据id  
createTime | integer | 流程发起时间  
approvalApiName | string | 流程定义主版本  
approvalName | string | 流程定义名称  
endTime | integer | 流程结束时间  
  
出参样例
    
    
    {
        "error": false,
        "data": {
            "size": 1,
            "total": 1,
            "dataList": [
                {
                    "owner": [
                        "1002"
                    ],
                    "submitter": [
                        "1002"
                    ],
                    "instanceId": "66f2a4856b07ab1b4ebad7e5",
                    "dataId": "66f2a484928b280007aa6dd8",
                    "createTime": 1727177862204,
                    "approvalApiName": "apprZVJ6E46RHG__crmappr",
                    "approvalName": "审批流-子流程使用",
                    "endTime": 0
                }
            ]
        },
        "errorMessage": ""
    }
    
    

**Groovy 举例**
    
    
    ActionAttribute attribute = ActionAttribute.build {
        forceQueryFromDB = false
    }
    
    
    QueryResult queryResult = Fx.approval.findInstances((String) context.data.object_describe_api_name, ["in_progress"], (String) context.data._id, 10, 0, attribute)[1];
    log.info(queryResult)
    
    if (queryResult != null) {
        //获取进行中的审批流实例,默认情况下只会有一条进行中的流程实例
        List dataList = (List) queryResult["dataList"]
        def instance = dataList[0]
        log.info("instance:" + instance)
    
    } else {
        log.info("未查询到当前数据存在审批流实例,请检查设置参数")
    }
    
    

### # 3\. findInstances 查询对象上的审批实例

> `Fx.approval.findInstances(<string entityId>, <integer limit>, <integer skip>)`

**参数说明**

入参格式

参数名称 | object | 描述 | 是否必填  
---|---|---|---  
entityId | string | 所属对象 | 是  
limit | integer | 需要多少条数据 | 是  
skip | integer | 从第几条开始获取 | 是  
  
出参格式

参数名称 | object | 描述  
---|---|---  
error | boolean | 是否存在异常  
data | object | 结果  
errorMessage | string | 存在异常时返回异常信息  
data | object | 结果  
---|---|---  
size | integer | 本次返回数据数  
total | integer | 总数据数  
dataList | array[object] | 结果集  
dataList | object | 描述  
---|---|---  
owner | array[string] | 流程发起人  
submitter | array[string] | 流程提交人  
instanceId | string | 实例id  
dataId | string | 数据id  
createTime | integer | 流程发起时间  
approvalApiName | string | 流程定义主版本  
approvalName | string | 流程定义名称  
endTime | integer | 流程结束时间  
  
出参样例
    
    
    {
        "error": false,
        "data": {
            "size": 1,
            "total": 1,
            "dataList": [
                {
                    "owner": [
                        "1002"
                    ],
                    "submitter": [
                        "1002"
                    ],
                    "instanceId": "66f2a4856b07ab1b4ebad7e5",
                    "dataId": "66f2a484928b280007aa6dd8",
                    "createTime": 1727177862204,
                    "approvalApiName": "apprZVJ6E46RHG__crmappr",
                    "approvalName": "审批流-子流程使用",
                    "endTime": 0
                }
            ]
        },
        "errorMessage": ""
    }
    
    

**Groovy 举例**
    
    
    QueryResult queryResult = Fx.approval.findInstances((String) context.data.object_describe_api_name, 10, 0)[1];
    log.info(queryResult)
    
    

**注意事项**

>   * 限制查询条数，每次查询最大100条
> 


### # 4\. findTasks 查询一个审批实例下的所有审批任务节点(查询并不是实时的，有延迟)

> `Fx.approval.findTasks(<string instanceId>)`

**参数说明**

入参格式

参数名称 | object | 描述 | 是否必填  
---|---|---|---  
instanceId | string | 实例id | 是  
  
出参格式

参数名称 | object | 结果  
---|---|---  
error | boolean | 是否错误  
result | array[object] | 结果集  
errorMessage | string | 异常信息  
result | object | 任务列表  
---|---|---  
taskId | string | 任务id  
dataId | string | 数据id  
objectApiName | string | 对象api名称  
createTime | integer | 创建时间  
duration | integer | 任务耗时  
userIds | array[string] | 任务待处理人,此字段不会随任务处理而发生变化,只有修改处理人时此字段才会变化  
type | string | 任务类型.one_pass或single:单人/多人审批;all_pass:会签审批;  
state | string | 任务状态.pass:通过,reject:驳回;cancel:撤回;error:异常  
opinions | array[object] | 审批意见  
task_name | string | 任务名称  
dealed_persons | array[string] | 已处理人,任务处理后,此字段会发生变化.如果是会签节点,没处理一次,此字段会变更一次  
workflow_instance_id | string | 实例id  
submitter | array[string] | 数据提交人  
workflow_id | string | 流程子版本Id  
is_timeout | boolean | 是否超时,默认为null  
opinions | object | 描述  
---|---|---  
userId | integer | 处理人  
actionType | string | 处理结果.agree:同意;reject:驳回;cancel:撤回;addTag:前加签;retrieve:取回重审;auto_pass或auto_agree:自动通过;tagAfter:后加签;skip_task_validate:跳过任务完成条件及任务后动作  
opinion | string | 审批意见  
replyTime | integer | 处理时间  
  
出参样例
    
    
    {
      "error": false,
      "result": [
        {
          "taskId": "66f656c1deb560342dbd4381",
          "dataId": "66f656c125255b00077a168c",
          "objectApiName": "object_RlhY0__c",
          "createTime": 1727420105143,
          "duration": 6769,
          "userIds": [
            "1007"
          ],
          "type": "one_pass",
          "state": "pass",
          "opinions": [
            {
              "userId": 1007,
              "actionType": "agree",
              "opinion": "同意。",
              "replyTime": 1727335044325
            }
          ],
          "task_name": "A",
          "dealed_persons": [
            "1007"
          ],
          "workflow_instance_id": "66f656c10cf87e114caaa80a",
          "submitter": [
            "1007"
          ],
          "workflow_id": "66f655490cf87e114caaa7fd",
          "is_timeout": false
        }
      ],
      "errorMessage": ""
    }
    
    

**Groovy 举例**
    
    
    String entityId = (String) context.data.object_describe_api_name
    String objectId = (String) context.data._id
    
    
    
    def instanceId = Fx.approval.existsInstance(entityId, objectId).result()
    log.info("instanceId:"+instanceId)
    
    def tasks = Fx.approval.findTasks((String)instanceId)
    log.info(tasks)
    
    

### # 5\. cancelApproval 指定对象和数据id, 撤回正在进行的审批

> `Fx.approval.cancelApproval(<String entityId>, <String objectId>, <String cancelReason>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
entityId | String | 所属对象 | 是  
objectId | String | 所属数据 | 是  
cancelReason | String | 撤回原因 | \--  
  
出参格式

参数名称 | APIResult | 描述  
---|---|---  
error | Boolean | 是否异常  
data | void | 无返回  
errorMessage | String | 异常信息  
  
出参样例
    
    
    {
    "error":false,
    "data":null,
    "errorMessage":""
    }
    
    

**Groovy 举例**
    
    
    String entity_id = context.data.object_describe_api_name
    String object_id = context.data._id
    log.info(entity_id + ":" + object_id)
    def ret = Fx.approval.cancelApproval(entity_id, object_id, "撤回审批流程")
    log.info(ret)
    
    

### # 6\. approvalAction 对审批任务节点进行操作

> `Fx.approval.approvalAction(<string taskId>, <string actionType>, <string opinion>, <string userId>)`

**参数说明**

入参格式

参数名称 | object | 描述 | 是否必填  
---|---|---|---  
taskId | string | 任务Id | 是  
actionType | string | 操作类型.agree:同意;reject:驳回 | 是  
opinion | string | 审批意见 | \--  
userId | string | 任意审批处理人 | 是  
  
出参格式

参数名称 | object | 描述  
---|---|---  
error | boolean | 是否存在异常  
result | object | 无返回结果  
errorMessage | string | 异常信息  
  
出参样例
    
    
    {
      "error": false,
      "result": "66f656c10cf87e114caaa80a",
      "errorMessage": ""
    }
    
    

**Groovy 举例**
    
    
    // 流程设置为:  单人审批A-> 单人审批B -> 单人审批C
    // 案例中,已审批到 单人审批C
    
    String entityId = (String) context.data.object_describe_api_name
    String objectId = (String) context.data._id
    
    
    def instanceId = Fx.approval.existsInstance(entityId, objectId).result()
    log.info("instanceId:"+instanceId)
    
    
    def tasks = Fx.approval.findTasks((String)instanceId)
    //log.info(tasks)
    
    
    def taskList = tasks.get(1) as List
    
    
    //获取其中一个任务
    Map task = taskList[0] as Map
    
    log.info(task)
    
    String taskId = task["taskId"]
    List candidateIds = task["userIds"]
    //  agree 或者 reject
    def ret = Fx.approval.approvalAction(taskId, "agree", "同意", (String)candidateIds[0])
    
    

**注意事项**

>   * 如果任务中有流程布局或者自定义布局,不推荐使用此方法,因为此方法无法正常去处理表单中的数据,推荐只有没有表单信息时使用
> 


### # 7\. setApprovalIds 更换审批任务节点的审批人

> `Fx.approval.setApprovalIds(<string taskId>, <array candidateIds>)`

**参数说明**

入参格式

参数名称 | object | 描述 | 是否必填  
---|---|---|---  
taskId | string | 任务ID | 是  
candidateIds | array[string] | 任务处理人 | 是  
  
出参格式

参数名称 | object | 描述  
---|---|---  
error | boolean | 是否存在异常  
result | object | 无返回结果  
errorMessage | string | 异常信息  
  
出参样例
    
    
    {
      "error": false,
      "result": null,
      "errorMessage": ""
    }
    
    

**Groovy 举例**
    
    
    String entityId = (String) context.data.object_describe_api_name
    String objectId = (String) context.data._id
    
    
    def instanceId = Fx.approval.existsInstance(entityId, objectId).result()
    log.info("instanceId:"+instanceId)
    
    
    def tasks = Fx.approval.findTasks((String)instanceId)
    log.info(tasks)
    
    
    def taskList = tasks.get(1) as List
    
    
    //获取其中一个任务
    Map task = taskList[0] as Map
    
    log.info(task)
    
    String taskId = task["taskId"]
    log.info(taskId)
    
    //更换任务处理人
    def result = Fx.approval.setApprovalIds(taskId, ["1000","1011","1012"])
    log.info(result)
    
    

**注意事项**

>   * 更换处理人都是以系统的身份(-10000)去执行更换,故更换完后,在任务处理人修改记录中会显示由系统更换了处理人
> 


### # 8\. getCanRefuseTasks 通过当前实例查询可以驳回到的任务节点信息

> `Fx.approval.getCanRefuseTasks(<string instanceId>)`

**参数说明**

入参格式

参数名称 | object | 描述 | 是否必填  
---|---|---|---  
instanceId | string | 实例Id | 是  
  
出参格式

参数名称 | object | 结果集  
---|---|---  
taskId | string | 任务Id  
taskFullName | string | 任务名称  
enableMoveToCurrentActivityWhenReject | boolean | 930新增字段.如果驳回到此任务,此任务处理后,是否直接回到驳回前的节点,如果此字段为true,则可以驳回到前置节点,前置节点处理后回到原节点  
  
出参样例
    
    
    [
      {
        "taskId": "66f52985deb560342dbd3e21",
        "taskFullName": "A",
        "enableMoveToCurrentActivityWhenReject": false
      }
    ]
    
    

**Groovy 举例**
    
    
    String entityId = (String) context.data.object_describe_api_name
    String objectId = (String) context.data._id
    
    
    def instanceId = Fx.approval.existsInstance(entityId, objectId).result()
    log.info("instanceId:" + instanceId)
    
    
    def canRefuseTasks = Fx.approval.getCanRefuseTasks((String) instanceId)
    log.info(canRefuseTasks)
    
    

**注意事项**

>   * 如果是并行网关下,同时存在多个进行中的任务,如果不传递任务id,则默认随机获取任意一个任务可以驳回到的节点,推荐使用Fx.approval.getCanRefuseTasks(instanceId,task)获取
> 


### # 9\. getCanRefuseTasks 通过当前实例查询可以驳回到的任务节点信息

> `Fx.approval.getCanRefuseTasks(<string instanceId>, <string taskId>)`

**参数说明**

入参格式

参数名称 | object | 描述 | 是否必填  
---|---|---|---  
instanceId | string | 实例Id | 是  
taskId | string | 任务Id | 是  
  
出参格式

参数名称 | object | 结果集  
---|---|---  
taskId | string | 任务Id  
taskFullName | string | 任务名称  
enableMoveToCurrentActivityWhenReject | boolean | 930新增字段.如果驳回到此任务,此任务处理后,是否直接回到驳回前的节点,如果此字段为true,则可以驳回到前置节点,前置节点处理后回到原节点  
  
出参样例
    
    
    [
      {
        "taskId": "66f52985deb560342dbd3e21",
        "taskFullName": "A",
        "enableMoveToCurrentActivityWhenReject": false
      }
    ]
    
    

**Groovy 举例**
    
    
    String entityId = (String) context.data.object_describe_api_name
    String objectId = (String) context.data._id
    
    
    
    def instanceId = Fx.approval.existsInstance(entityId, objectId).result()
    log.info("instanceId:"+instanceId)
    
    String taskId = "66f656f7deb560342dbd4394"
    
    def canRefuseTasks = Fx.approval.getCanRefuseTasks((String)instanceId,taskId)
    log.info(canRefuseTasks)
    
    

### # 10\. getDetailChange 获取从对象变更详情

> `Fx.approval.getDetailChange(<string instanceId>, <string detailEntityId>)`

**参数说明**

入参格式

参数名称 | object | 描述 | 是否必填  
---|---|---|---  
instanceId | string | 实例Id | 是  
detailEntityId | string | 从对象ApiName | 是  
  
出参格式

参数名称 | object | 描述  
---|---|---  
data | object |   
describe | object | 从对象描述  
detailDisplayName | string | 从对象名称  
describeExt | object | 从对象描述扩展信息  
data | object | 描述  
---|---|---  
Add | array | 新增的从对象数据,整体数据集合  
Delete | array[object] | 删除从对象数据  
Edit | array[object] | 增加了几条从数据  
Delete | object | 描述  
---|---|---  
detailDataId | string | 从对象数据Id  
detailDataName | string | 从对象名称-从对象主属性  
recordType | string | 业务类型  
Edit | object | 描述  
---|---|---  
detailDataId | string | 从对象数据id,如果新增可能不存在数据  
detailDataName | string | 业务类型_从对象中文名称_从对象主属性  
recordType | string | 业务类型  
fieldChangeDetail | array[object] |   
fieldChangeDetail | object | 描述  
---|---|---  
newValue | string | 编辑从数据,之前的字段值  
fieldApiName | string | 字段apiName  
oldValue | string | 编辑从数据,变更后的值  
  
出参样例
    
    
    {
      "data": {
        "Add": [
          {
            "tenant_id": "71557",
            "lock_rule": "default_lock_rule",
            "data_own_organization": [
              "999999"
            ],
            "data_own_organization__l": [
              {
                "deptName": "全集团",
                "leaderUserId": "1034",
                "deptId": "999999",
                "deptType": "org",
                "status": 0
              }
            ],
            "__new_data__": true,
            "mc_exchange_rate": "1.000000",
            "field_gM81p__c__r": {
              "deptName": "测试二级部门",
              "leaderUserId": "1099",
              "deptId": "1027",
              "deptType": "dept",
              "parentId": "1026",
              "status": 0
            },
            "created_by__r": {
              "picAddr": "N_201907_10_5ba561a111724c3c8232b68bed4c2077",
              "description": "",
              "dept": "1017",
              "empNum": "1007",
              "modifyTime": 1726824651698,
              "post": "研发工程师",
              "createTime": 1524219762800,
              "phone": "01090102910",
              "name": "崔永旭-CN",
              "nickname": "崔永旭-CN",
              "tenantId": "71557",
              "id": "1007",
              "email": "cuiyx@fxiaoke.com",
              "status": 0
            },
            "field_C38fh__c": "444",
            "data_own_organization__r": {
              "deptName": "全集团",
              "leaderUserId": "1034",
              "deptId": "999999",
              "deptType": "org",
              "status": 0
            },
            "dataIndex": 3,
            "field_5zo7k__c": "4444",
            "object_describe_api_name": "object_p2Eps__c",
            "owner__l": [
              {
                "picAddr": "N_201907_10_5ba561a111724c3c8232b68bed4c2077",
                "description": "",
                "dept": "1017",
                "modifyTime": 1726824651698,
                "empNum": "1007",
                "post": "研发工程师",
                "phone": "01090102910",
                "createTime": 1524219762800,
                "tenantId": "71557",
                "name": "崔永旭-CN",
                "nickname": "崔永旭-CN",
                "id": "1007",
                "email": "cuiyx@fxiaoke.com",
                "status": 0
              }
            ],
            "field_QwvF2__c": "66f66d5725255b0007876946",
            "field_QwvF2__c__r": "如来-2024-09-27279",
            "mc_functional_currency": "CNY",
            "owner__r": {
              "picAddr": "N_201907_10_5ba561a111724c3c8232b68bed4c2077",
              "description": "",
              "dept": "1017",
              "empNum": "1007",
              "modifyTime": 1726824651698,
              "post": "研发工程师",
              "createTime": 1524219762800,
              "phone": "01090102910",
              "name": "崔永旭-CN",
              "nickname": "崔永旭-CN",
              "tenantId": "71557",
              "id": "1007",
              "email": "cuiyx@fxiaoke.com",
              "status": 0
            },
            "__tbIndex": 4,
            "field_j2w1H__c": "33",
            "field_gM81p__c__l": [
              {
                "deptName": "测试二级部门",
                "leaderUserId": "1099",
                "deptId": "1027",
                "deptType": "dept",
                "parentId": "1026",
                "status": 0
              }
            ],
            "owner": [
              "1007"
            ],
            "field_289O2__c": "33",
            "lock_status": "0",
            "data_own_department__r": {
              "deptName": "七级部门",
              "leaderUserId": "1007",
              "deptId": "1017",
              "deptType": "dept",
              "parentId": "1016",
              "status": 0
            },
            "create_time": 1727425931205,
            "field_gM81p__c": [
              "1027"
            ],
            "life_status": "in_change",
            "last_modified_by__l": [
              {
                "picAddr": "N_201907_10_5ba561a111724c3c8232b68bed4c2077",
                "description": "",
                "dept": "1017",
                "modifyTime": 1726824651698,
                "empNum": "1007",
                "post": "研发工程师",
                "phone": "01090102910",
                "createTime": 1524219762800,
                "tenantId": "71557",
                "name": "崔永旭-CN",
                "nickname": "崔永旭-CN",
                "id": "1007",
                "email": "cuiyx@fxiaoke.com",
                "status": 0
              }
            ],
            "created_by__l": [
              {
                "picAddr": "N_201907_10_5ba561a111724c3c8232b68bed4c2077",
                "description": "",
                "dept": "1017",
                "modifyTime": 1726824651698,
                "empNum": "1007",
                "post": "研发工程师",
                "phone": "01090102910",
                "createTime": 1524219762800,
                "tenantId": "71557",
                "name": "崔永旭-CN",
                "nickname": "崔永旭-CN",
                "id": "1007",
                "email": "cuiyx@fxiaoke.com",
                "status": 0
              }
            ],
            "last_modified_by": [
              "1007"
            ],
            "display_name": "default__c____",
            "__operateWidth": 88,
            "created_by": [
              "1007"
            ],
            "mc_currency": "CNY",
            "record_type": "default__c",
            "field_7s7Gg__c": "33",
            "last_modified_by__r": {
              "picAddr": "N_201907_10_5ba561a111724c3c8232b68bed4c2077",
              "description": "",
              "dept": "1017",
              "empNum": "1007",
              "modifyTime": 1726824651698,
              "post": "研发工程师",
              "createTime": 1524219762800,
              "phone": "01090102910",
              "name": "崔永旭-CN",
              "nickname": "崔永旭-CN",
              "tenantId": "71557",
              "id": "1007",
              "email": "cuiyx@fxiaoke.com",
              "status": 0
            },
            "rowId": "17274259128251754",
            "data_own_department": [
              "1017"
            ],
            "field_sg0sY__c": "33",
            "object_describe_id": "5b8e55a7a5083d5ecf5d8b66",
            "name": "数据1",
            "order_by": 40,
            "mc_exchange_rate_version": "1716450563496",
            "_id": "66f66d8b25255b000787c759",
            "data_own_department__l": [
              {
                "deptName": "七级部门",
                "leaderUserId": "1007",
                "deptId": "1017",
                "deptType": "dept",
                "parentId": "1016",
                "status": 0
              }
            ]
          }
        ],
        "Delete": [
          {
            "detailDataId": "66f66d5725255b0007876949",
            "detailDataName": "孙悟空-2024-09-272445",
            "recordType": "default__c"
          }
        ],
        "Edit": [
          {
            "detailDataId": "66f66d5725255b0007876947",
            "detailDataName": "default__c____孙悟空-2024-09-272443",
            "recordType": "default__c",
            "fieldChangeDetail": [
              {
                "newValue": "5555",
                "fieldApiName": "field_289O2__c",
                "oldValue": "77"
              }
            ]
          }
        ]
      },
      "describe": {
        "description": "描述太大,此处省略"
      },
      "detailDisplayName": "孙悟空(INAG)",
      "describeExt": {
        "description": "描述太大,此处省略"
      }
    }
    
    

**Groovy 举例**
    
    
    String entityId = (String) context.data.object_describe_api_name
    String objectId = (String) context.data._id
    
    
    def instanceId = Fx.approval.existsInstance(entityId, objectId).result()
    log.info("instanceId:"+instanceId)
    
    //从对象apiname
    String detailEntityId= "object_p2Eps__c"
    
    
    def detailDatas  = Fx.approval.getDetailChange((String)instanceId,detailEntityId)
    log.info(detailDatas)
    
    

**注意事项**

>   * 仅编辑触发可以获取到从对象的变更信息
> 


### # 11\. rejectToBeforeTask 驳回至的任意节点(当前节点之前的节点)

> `Fx.approval.rejectToBeforeTask(<string currentTaskId>, <string beforeTaskId>, <string userId>, <string opinion>, <boolean enableMoveToCurrentActivityWhenReject>)`

**参数说明**

入参格式

参数名称 | object | 描述 | 是否必填  
---|---|---|---  
currentTaskId | string | 当前任务Id | 是  
beforeTaskId | string | 要驳回到哪个任务,需要使用Fx.approval.getCanRefuseTasks(instanceId,taskId)接口返回的任务,不能随意指定 | 是  
userId | string | 当前任务的任意处理人 | 是  
opinion | string | 驳回意见 | \--  
enableMoveToCurrentActivityWhenReject | boolean | 此值为true, 则可以自行选择,驳回到前置节点, 前置节点处理后,回到当前节点.如果为false,则前置节点处理后,依次向后处理 |   
此值需要依据Fx.approval.getCanRefuseTasks(instanceId,taskId)接口中返回的enableMoveToCurrentActivityWhenReject作为依据,如果enableMoveToCurrentActivityWhenReject返回的是false,则调用Fx.approval.rejectToBeforeTask时,即使传递true也不会生效,只有enableMoveToCurrentActivityWhenReject返回结果为true时,才可以自行选择驳回到前置节点, 前置节点处理后,回到当前节点 | 是 |  |   
  
出参格式

参数名称 | object | 描述  
---|---|---  
error | boolean | 是否存在异常  
result | object | 无返回结果  
errorMessage | string | 异常信息  
  
出参样例
    
    
    {
      "error": false,
      "result": "66f656c10cf87e114caaa80a",
      "errorMessage": ""
    }
    
    

**Groovy 举例**
    
    
    // 流程设置为:  单人审批A-> 单人审批B -> 单人审批C
    // 案例中,已审批到 单人审批C
    
    String entityId = (String) context.data.object_describe_api_name
    String objectId = (String) context.data._id
    
    
    def instanceId = Fx.approval.existsInstance(entityId, objectId).result()
    log.info("instanceId:"+instanceId)
    
    
    def tasks = Fx.approval.findTasks((String)instanceId)
    //log.info(tasks)
    
    
    def taskList = tasks.get(1) as List
    
    
    //获取其中一个任务
    Map task = taskList[0] as Map
    
    log.info(task)
    
    String taskId = task["taskId"]
    List candidateIds = task["userIds"]
    
    List<Map<String,Object>> canRefuseTasks = Fx.approval.getCanRefuseTasks((String)instanceId,taskId).result() as List
    //log.info(canRefuseTasks)
    
    Map<String,Object> beforeTask = [:]
    
    canRefuseTasks.each{
      item->
      if(item["taskFullName"]=="单人审批A"){
        beforeTask= item
      }
    }
    log.info(beforeTask)
    String beforeTaskId = beforeTask["taskId"]
    
    // enableMoveToCurrentActivityWhenReject:如果驳回到`单人审批A``, 当`单人审批A`处理后,是否回到当前节点
    // 如果此值为false,则`单人审批A`处理后,是无法回到当前节点,即使传递true,也不会生效
    // 如果此值为true, 则可以自行选择,`单人审批A`处理后,是否需要回到当前节点
    boolean enableMoveToCurrentActivityWhenReject = beforeTask["enableMoveToCurrentActivityWhenReject"]
    
    
    
    Fx.approval.rejectToBeforeTask( taskId, beforeTaskId,  (String)candidateIds[0],  "驳回到前置节点 单人审批A",  enableMoveToCurrentActivityWhenReject)
    
    

**注意事项**

>   * 如果任务节点设置了完成条件,目前不会返回异常信息,看到的现象是,虽然执行了驳回,但是任务没有处理,此接口需要与Fx.approval.getCanRefuseTasks(instanceId,taskId)联合使用
> 


### # 12\. skipValidateAndCompleteTask 支持全流程事件配置, 完成任务, 并跳过校验及后动作执行落

> `Fx.approval.skipValidateAndCompleteTask(<string taskId>, <string opinion>, <string userId>)`

**参数说明**

入参格式

参数名称 | object | 描述 | 是否必填  
---|---|---|---  
taskId | string | 任务id | \--  
opinion | string | 处理意见 | \--  
userId | string | 从待处理人中任意获取其中一位,用作校验当前人是否属于任务处理人,跳过身份验证 | \--  
  
出参格式

参数名称 | object | 描述  
---|---|---  
error | boolean | 是否存在异常  
result | object | 无返回结果  
errorMessage | string | 异常信息  
  
出参样例
    
    
    {
      "error": false,
      "result": null,
      "errorMessage": ""
    }
    
    

**Groovy 举例**
    
    
    String entityId = (String) context.data.object_describe_api_name
    String objectId = (String) context.data._id
    
    
    def instanceId = Fx.approval.existsInstance(entityId, objectId).result()
    log.info("instanceId:"+instanceId)
    
    
    def tasks = Fx.approval.findTasks((String)instanceId)
    log.info(tasks)
    
    
    def taskList = tasks.get(1) as List
    
    
    //获取其中一个任务
    Map task = taskList[0] as Map
    
    log.info(task)
    
    String taskId = task["taskId"]
    //获取任务处理人
    List candidateIds = task["userIds"]
    
    
    //以系统身份 ,跳过完成条件 及 任务的后动作,需要传递任意一位任务待处理人
    def result = Fx.approval.skipValidateAndCompleteTask( taskId, "跳过当前任务", (String)candidateIds[0])
    log.info(result)
    
    

**注意事项**

>   * 以系统身份 ,跳过任务的完成条件 及 任务的后动作
> 


### # 13\. delayTaskImmediatelyExecute 审批流等待节点立即执行

> `Fx.approval.delayTaskImmediatelyExecute(<string operationType>, <string taskId>, <string type>)`

**参数说明**

入参格式

参数名称 | object | 描述 | 是否必填  
---|---|---|---  
operationType | string | 操作类型.reflush:刷新(等待时长为字段时,如果解析等待时长异常时,可以调用);execute:立即执行 | 是  
taskId | string | 任务Id | 是  
type | string | 流程类型,传递approvalflow即可 | 是  
  
出参格式

参数名称 | APIResult | 描述  
---|---|---  
error | Boolean | 是否异常  
data | void | 无返回  
errorMessage | String | 异常信息  
  
出参样例
    
    
    {
    "error":false,
    "data":null,
    "errorMessage":""
    }
    
    

**Groovy 举例**
    
    
    def res = Fx.approval.delayTaskImmediatelyExecute("62f3217ac6fa24292be4f833").result() as Map;
    
    

### # 14\. existsInstance 审批流是否存在实例, 存在这返回实例id

> `Fx.approval.existsInstance(<string entityId>, <string objectId>)`

**参数说明**

入参格式

参数名称 | object | 描述 | 是否必填  
---|---|---|---  
entityId | string | 所属对象 | 是  
objectId | string | 数据Id | 是  
  
出参格式

参数名称 | object | 结果  
---|---|---  
error | boolean | 是否有异常  
result | string | 如果有正在运行的实例,则返回实例id  
errorMessage | string | 如果有异常,则返回错误信息  
  
出参样例
    
    
    {
      "error": false,
      "result": "66f656c10cf87e114caaa80a",
      "errorMessage": ""
    }
    
    

**Groovy 举例**
    
    
    String entityId = (String) context.data.object_describe_api_name
    String objectId = (String) context.data._id
    
    log.info(entityId)
    log.info(objectId)
    
    def rst = Fx.approval.existsInstance(entityId, objectId).result()
    log.info("instanceId:"+rst)
    
    

### # 15\. refreshHandler 重新解析任务处理人

> `Fx.approval.refreshHandler(<string taskId>)`

**参数说明**

入参格式

参数名称 | object | 重新解析审批流任务处理人 | 是否必填  
---|---|---|---  
taskId | string | 任务处理人 | 是  
  
出参格式

参数名称 | APIResult | 描述  
---|---|---  
error | Boolean | 是否异常  
data | void | 无返回  
errorMessage | String | 异常信息  
  
出参样例
    
    
    {
    "error":false,
    "data":null,
    "errorMessage":""
    }
    
    

**Groovy 举例**
    
    
    def res = Fx.approval.refreshHandler("66f29d016b07ab1b4ebad554")
    log.info(res)
    
    

**注意事项**

>   * 如果任务存在处理人,调用此接口,仍然会二次解析,并且会存在处理人的修改记录
> 


### # 16\. findDelayTask 根据objectId或审批InstanceId查询等待节点

> `Fx.approval.findDelayTask(<string objectId>, <string workflowInstanceId>, <integer pageNumber>, <integer pageSize>)`

**参数说明**

入参格式

参数名称 | object | 描述 | 是否必填  
---|---|---|---  
objectId | string | 数据Id,如果objectId不为空,workflowInstanceId可不传递 | \--  
workflowInstanceId | string | 流程实例Id,如果workflowInstanceId不为空,objectId可不传递 | \--  
pageNumber | integer | 页码,从1开始 | 是  
pageSize | integer | 每页大小,默认20 | 是  
  
出参格式

参数名称 | object | 结果  
---|---|---  
error | boolean | 是否错误  
data | array[object] | 数据  
errorMessage | string | 错误信息  
data | object | 等待节点结果集  
---|---|---  
id | string | 任务ID  
tenantId | string | 当前企业Id  
appId | string | 默认CRM  
name | string | 任务名称  
workflowId | string | 流程定义子版本id  
workflowInstanceId | string | 流程实例id  
activityId | string | 任务的节点id  
activityInstanceId | string | 任务节点实例id  
createTime | integer | 创建时间  
modifyTime | integer | 修改时间  
state | string | 任务状态.pass:通过,cancel:撤回;error:异常  
type | string | 默认:executionTask  
taskType | string | 默认:executionTask  
actionType | string | 预留  
description | string | 任务描述  
executionList | array[object] | 等待节点后动作列表  
entityId | string | 所属对象  
objectId | string | 所属数据id  
latencyTime | string | 等待时长  
latencyUnit | string | 时间类型,1:表示天;2:表示小时;3:表示分钟  
sourceWorkflowId | string | 流程主版本号  
executeTime | integer | 执行时间  
finishedTime | integer | 具体执行时间  
executor | string | 执行人.默认为系统(-10000),如果有人点击立即执行,则是具体人  
delay | boolean | true表示等待节点  
errMsg | string | 异常信息,如果state为error时有值  
executionList | object | 等待节点后动作执行项集合  
---|---|---  
requestId | string | 幂等表示  
taskType | string | 具体后动作类型.custom_function:执行APL代码;send_qixin:CRM提醒;updates:后动作更新;send_sms:短信提醒;send_email:邮件提醒;external_message_v2:外部通知新版;external_message:外部通知老版本;edit_team_member:添加团队成员;custom_variable_evaluation:变量赋值  
async | boolean | 是否为异步执行,目前仅APL代码支持异步执行  
type | string | 默认approvalflow  
rowNo | integer | 后动作执行顺序  
executionState | string | 执行结果;success:执行成功;error:执行失败  
actionErrorMsg | string | executionState为error时,会下发执行失败原因  
userId | string | 执行人,默认为系统(-10000)执行,如果异常,由人重试或忽略,此值为具体人  
modifyTime | integer | 后动作执行结束时间  
createTime | integer | 后动作执行开始时间  
sender | string | 邮件发送人,仅邮件提醒时有值  
recipients | object | 短信提醒,邮件提醒,CRM通知等,所选择的人员,部门,用户组,角色等信息  
ccRecipients | object | 抄送人,仅邮件提醒时有值  
bccRecipients | object | 密送人,仅邮件提醒时有值  
emailAddress | object | 管理员所设置的邮件接收人,仅邮件提醒时有值  
title | string | 标题,例如CRM提醒会使用到  
content | string | 内容,例如CRM提醒内容,短信内容,日程,销售记录,任务所设置的内容信息  
template | string | 模板,例如邮件提醒,短信提醒,可能会使用到固定模板  
updateFieldJson | string | 字段更新时,存储数据结构  
customVariables | object | 变量赋值,数据结构定义  
  
出参样例
    
    
    {
      "error": false,
      "data": [
        {
          "id": "66f5298c0cf87e114caaa5e2",
          "tenantId": "71557",
          "appId": "CRM",
          "name": "等待节点1",
          "workflowId": "66f5297b0cf87e114caaa5dd",
          "workflowInstanceId": "66f529850cf87e114caaa5e0",
          "activityId": "1727342883785",
          "activityInstanceId": "4",
          "createTime": 1727342988334,
          "modifyTime": 1727343031792,
          "state": "pass",
          "type": "executionTask",
          "taskType": "executionTask",
          "actionType": null,
          "description": "",
          "executionList": [
            {
              "requestId": "66f529b767042a00019402d1",
              "tenantId": "71557",
              "appId": "CRM",
              "taskType": "updates",
              "async": null,
              "type": "approvalflow",
              "rowNo": 0,
              "variables": {
                "action": "agree"
              },
              "task": null,
              "executionState": "success",
              "actionErrorMsg": null,
              "activityId": null,
              "userId": "-10000",
              "modifyTime": 1727343031646,
              "createTime": 0,
              "sender": null,
              "recipients": null,
              "ccRecipients": null,
              "bccRecipients": null,
              "emailAddress": null,
              "title": null,
              "content": null,
              "template": null,
              "afterActionDefinitionId": null,
              "afterActionMappingId": null,
              "actionMapping": null,
              "actionParams": null,
              "fieldMapping": null,
              "updateFieldJson": "[{\"isCalculate\":false,\"key\":\"${object_RlhY0__c.field_Xxb9v__c}\",\"value\":0,\"defaultValue\":\"\"}]",
              "updateFieldObject": null,
              "triggerParam": null,
              "workflowMap": {
                "workflowName": "有等待节点",
                "entityId": "object_RlhY0__c",
                "type": "approvalflow",
                "activityId": "1727342883785",
                "sourceWorkflowId": "apprGA9M4NQ562__crmappr",
                "appId": "CRM",
                "tenantId": "71557",
                "applicantId": "1007",
                "workflowInstanceId": "66f529850cf87e114caaa5e0",
                "workflowId": "66f5297b0cf87e114caaa5dd",
                "objectId": "66f5298425255b0007c68360"
              },
              "customVariables": null,
              "useRelated": false,
              "relatedObjectId": null,
              "relatedEntityId": null
            }
          ],
          "entityId": "object_RlhY0__c",
          "objectId": "66f5298425255b0007c68360",
          "latencyTime": "1.0",
          "latencyUnit": "3",
          "timeType": null,
          "eventExtension": null,
          "sourceWorkflowId": null,
          "bpmExtension": null,
          "taskExecuteState": "",
          "executeTime": 1727343048367,
          "finishedTime": 1727343031634,
          "executor": "-10000",
          "delay": true,
          "errMsg": null
        }
      ],
      "errorMessage": ""
    }
    
    

**Groovy 举例**
    
    
    /**
     * 以下提供了两种查询方式,可以通过数据id或者实例id去查询,如果上下文中有数据ID,则优先使用数据ID查询,否则使用实例ID查询
     */
    Integer pageNumber = 1
    Integer pageSize = 20
    
    
    //根据数据ID查延迟节点
    def rst = Fx.approval.findDelayTask((String) context.data._id, null, pageNumber, pageSize)
    log.info(rst)
    
    //--------------------------------------------------------------------------------
    
    //根据实例ID查延迟节点,如果函数上下文中有实例id,可以
    def instanceId = "66f529850cf87e114caaa5e0"
    def rst2 = Fx.approval.findDelayTask(null, instanceId, pageNumber, pageSize)
    log.info(rst2)
    
    

### # 17\. 获取审批流实例详情(实时查询)

> `Fx.approval.getInstance(<string instanceId>)`

**参数说明**

入参格式

参数名称 | object | 描述 | 是否必填  
---|---|---|---  
instanceId | string | 实例Id | 是  
  
出参格式

参数名称 | object | 描述  
---|---|---  
error | boolean | 是否错误  
data | object | 结果  
errorMessage | string |   
data | object | 结果  
---|---|---  
instance | object | 实例信息  
tasks | array[object] | 任务信息  
instance | object | 实例信息  
---|---|---  
instanceId | string | 实例id  
instanceName | string | 流程名称及流程触发时间的组合  
objectId | string | 流程发起对象数据id  
triggerType | string | 触发类型  
applicantId | integer | 发起人Id  
state | string | 流程状态.pass:通过,reject:驳回;cancel:撤回;error:异常  
createTime | integer | 流程发起时间  
endTime | integer | 流程结束时间,如果流程没有结束,此值为空或0  
lastModifyTime | integer | 流程最后修改时间  
apiName | string | 流程主版本号  
cancelTime | integer | 流程取消时间,如果流程没有取消,此值为空或0  
entityId | string | 流程发起对象  
triggerData | object | 触发数据  
triggerTypeName | string | 触发类型中文  
linkAppName | string | 关联应用名称,非互联流程,此值为空  
linkApp | string | 关联应用名称,非互联流程,此值为空  
linkAppEnable | boolean | 当前流程是否为互联流程  
linkAppType | integer | 互联属性,可忽略  
superWorkflowInstanceId | string | 如果当前流程为子流程,返回父流程实例id  
triggerData | object | 触发数据  
---|---|---  
data | null | 触发数据,流程不做解析  
callbackData | object | 触发数据,流程不做解析  
extraData | object | 触发数据,流程不做解析  
tasks | object | 集合信息  
---|---|---  
id | string | 任务Id  
type | string | 任务类型.one_pass或single:单人/多人审批;all_pass:会签审批;  
state | string | 任务状态.pass:通过,reject:驳回;cancel:撤回;error:异常  
opinions | array[object] | 审批意见  
errMsg | string | 任务异常是返回,如果后动作异常或者解析处理人异常  
apiName | string | 流程主版本号  
createTime | integer | 任务创建时间  
modifyTime | integer | 任务最后修改时间  
endTime | integer | 任务结束时间,如果任务没有结束,此值为空或0,930之后支持此字段  
completePersons | array[integer] | 已处理人  
unCompletePersons | array[integer] | 未处理人  
linkAppName | string | 关联应用名称,非互联流程,此值为空  
linkApp | string | 关联应用名称,非互联流程,此值为空  
linkAppEnable | boolean | 当前流程是否为互联流程  
linkAppType | integer | 互联属性,可忽略  
taskName | string | 任务名称  
opinions | object | 集合信息  
---|---|---  
userId | integer | 处理人  
actionType | string | 处理结果.agree:同意;reject:驳回;cancel:撤回;addTag:前加签;retrieve:取回重审;auto_pass或auto_agree:自动通过;tagAfter:后加签;skip_task_validate:跳过任务完成条件及任务后动作  
opinion | string | 审批意见  
replyTime | integer | 处理时间  
  
出参样例
    
    
    {
      "error": false,
      "data": {
        "instance": {
          "instanceId": "66f50a6f0cf87e114caaa435",
          "instanceName": "新建2024-09-26-1850（2024-09-2615:17）",
          "objectId": "66f50a6e25255b0007b64ca0",
          "triggerType": "Create",
          "applicantId": 1007,
          "state": "in_progress",
          "createTime": 1727335023418,
          "endTime": 0,
          "lastModifyTime": 1727335044456,
          "apiName": "apprZVJ6E46RHG__crmappr",
          "cancelTime": 0,
          "entityId": "object_RlhY0__c",
          "triggerData": {
            "data": null,
            "callbackData": {
              "_triggerActionCode": "Add",
              "optionInfo": {
                "extendsLogInfo": {},
                "fromApiName": "object_RlhY0__c",
                "fromClone": true,
                "fromDraft": false,
                "fromId": "66f50a4b25255b0007b5f8fd",
                "fromImport": false,
                "fromMapping": false,
                "fromReferenceCreate": false,
                "fromTransform": false,
                "skipFuncValidate": false,
                "supportValidationResult": true
              }
            },
            "extraData": {
              "stage": null,
              "detailChange": null,
              "useSnapshotForApproval": false,
              "newLifeStatus": null,
              "detailEntities": null
            }
          },
          "triggerTypeName": "新建",
          "linkAppName": null,
          "linkApp": null,
          "linkAppEnable": false,
          "linkAppType": 0,
          "superWorkflowInstanceId": null
        },
        "tasks": [
          {
            "id": "66f50a6fdeb560342dbd3d0d",
            "type": "one_pass",
            "state": "pass",
            "opinions": [
              {
                "userId": 1007,
                "actionType": "agree",
                "opinion": "同意。",
                "replyTime": 1727335044325
              }
            ],
            "errMsg": null,
            "apiName": "apprZVJ6E46RHG__crmappr",
            "createTime": 1727335023423,
            "modifyTime": 1727335044325,
            "endTime": 1727335044325,
            "completePersons": [
              1007
            ],
            "unCompletePersons": [],
            "linkAppName": null,
            "linkApp": null,
            "linkAppEnable": false,
            "linkAppType": 0,
            "taskName": "A"
          },
          {
            "id": "66f50a840cf87e114caaa437",
            "type": "one_pass",
            "state": "in_progress",
            "opinions": [],
            "errMsg": null,
            "apiName": "apprZVJ6E46RHG__crmappr",
            "createTime": 1727335044364,
            "modifyTime": 1727335044377,
            "endTime": 0,
            "completePersons": [],
            "unCompletePersons": [
              1007
            ],
            "linkAppName": null,
            "linkApp": null,
            "linkAppEnable": false,
            "linkAppType": 0,
            "taskName": "B1"
          }
        ]
      },
      "errorMessage": ""
    }
    
    

**Groovy 举例**
    
    
    //此接口非实时查询
    QueryResult queryResult = Fx.approval.findInstances((String) context.data.object_describe_api_name, ["in_progress"], (String) context.data._id, 10, 0)[1];
    
    if (queryResult != null) {
        List dataList = (List) queryResult["dataList"]
        def instance = dataList[0]
        String instanceId = instance["instanceId"]
        // 实时查询流程实例信息
        Map rst = Fx.approval.getInstance(instanceId).result()
        log.info("instanceDetail:" + rst)
    } else {
        log.info("未查询到数据")
    }
    
    

### # 18\. getInstanceProgress 查询流程实例详情进展

> `Fx.approval.getInstanceProgress(<string entityId>, <string objectId>)`

**参数说明**

入参格式

参数名称 | object | 描述 | 是否必填  
---|---|---|---  
entityId | string | 所属对象 | 是  
objectId | string | 数据id | 是  
  
出参格式

参数名称 | object | 描述  
---|---|---  
error | boolean | 是否错误  
data | object | 结果集  
errorMessage | string |   
data | object | 结果集  
---|---|---  
id | string | 流程实例id  
subState | string | 流程正常时为normal;,如果state=error,BuildTaskException:生成下一节点异常;CallBackException:流程结束后回调对象异常;CallBackWaiting:流程结束回调对象侧,数据状态不正确,轮训重试  
triggerType | string | 触发类型  
state | string | 流程状态  
objectId | string | 数据id  
entityId | string | 发起流程的对象  
applicantId | string | 审批提交人  
workflowName | string | 流程名称  
workflowId | string | 流程版本id  
sourceWorkflowId | string | 流程主版本id  
triggerData | object | 审批流触发时数据  
allTasks | array[object] | 所有任务  
triggerData | object | 审批流触发时数据  
---|---|---  
callbackData | object | 触发数据,流程不做解析和处理  
extraData | object | 触发数据,流程不做解析和处理  
allTasks | object | 集合信息  
---|---|---  
id | string | 任务id  
taskName | string | 任务名称  
type | string | 任务类型.one_pass或single:单人/多人审批;all_pass:会签审批;  
state | string | 任务状态.pass:通过,reject:驳回;cancel:撤回;error:异常  
opinions | array[object] | 审批意见  
errMsg | string | 任务异常是返回,如果后动作异常或者解析处理人异常  
linkAppName | string | 关联应用名称,非互联流程,此值为空  
linkApp | string | 关联应用名称,非互联流程,此值为空  
linkAppEnable | boolean | 当前流程是否为互联流程  
linkAppType | integer | 互联属性,可忽略  
opinions | object | 描述  
---|---|---  
userId | string | 处理人  
actionType | string | 处理结果.agree:同意;reject:驳回;cancel:撤回;addTag:前加签;retrieve:取回重审;auto_pass或auto_agree:自动通过;tagAfter:后加签;skip_task_validate:跳过任务完成条件及任务后动作  
opinion | string | 审批意见  
replyTime | integer | 处理时间  
  
出参样例
    
    
    {
      "error": false,
      "data": {
        "id": "66f50a6f0cf87e114caaa435",
        "subState": null,
        "triggerType": "Create",
        "state": "in_progress",
        "objectId": "66f50a6e25255b0007b64ca0",
        "entityId": "object_RlhY0__c",
        "applicantId": "1007",
        "workflowName": "并行驳回再驳回",
        "workflowId": "66f50a680cf87e114caaa430",
        "sourceWorkflowId": "apprZVJ6E46RHG__crmappr",
        "triggerData": {
          "data": null,
          "callbackData": {
            "_triggerActionCode": "Add",
            "optionInfo": {
              "extendsLogInfo": {},
              "fromApiName": "object_RlhY0__c",
              "fromClone": true,
              "fromDraft": false,
              "fromId": "66f50a4b25255b0007b5f8fd",
              "fromImport": false,
              "fromMapping": false,
              "fromReferenceCreate": false,
              "fromTransform": false,
              "skipFuncValidate": false,
              "supportValidationResult": true
            }
          },
          "extraData": {
            "stage": null,
            "detailChange": null,
            "useSnapshotForApproval": false,
            "newLifeStatus": null,
            "detailEntities": null
          }
        },
        "allTasks": [
          {
            "id": "66f50a6fdeb560342dbd3d0d",
            "taskName": "A",
            "type": "one_pass",
            "state": "pass",
            "opinions": [
              {
                "userId": "1007",
                "actionType": "agree",
                "opinion": "同意。",
                "replyTime": 1727335044325
              }
            ],
            "errMsg": null,
            "linkAppName": null,
            "linkApp": null,
            "linkAppEnable": false,
            "linkAppType": 0
          },
          {
            "id": "66f50a840cf87e114caaa437",
            "taskName": "B1",
            "type": "one_pass",
            "state": "in_progress",
            "opinions": [],
            "errMsg": null,
            "linkAppName": null,
            "linkApp": null,
            "linkAppEnable": false,
            "linkAppType": 0
          },
          {
            "id": "66f50a840cf87e114caaa438",
            "taskName": "C1",
            "type": "one_pass",
            "state": "in_progress",
            "opinions": [],
            "errMsg": null,
            "linkAppName": null,
            "linkApp": null,
            "linkAppEnable": false,
            "linkAppType": 0
          }
        ]
      },
      "errorMessage": ""
    }
    
    

**Groovy 举例**
    
    
    APIResult data = Fx.approval.getInstanceProgress((String) context.data.object_describe_api_name, (String) context.data._id);
    log.info(data)
    
    

### # 19\. getTriggerDataByInstanceId 查询固定审批流, 自由审批流实例相关的triggerData

> `Fx.approval.getTriggerDataByInstanceId(<string instanceId>)`

**参数说明**

入参格式

参数名称 | object | 描述 | 是否必填  
---|---|---|---  
instanceId | string | 流程实例Id | 是  
  
出参格式

参数名称 | object | 描述  
---|---|---  
error | boolean | 是否异常  
data | object | 结果  
errorMessage | string | 有异常时返回异常信息  
data | object | 结果  
---|---|---  
extraData | object | 触发时的扩展信息,流程不做解析及处理  
data | object | 触发时的扩展信息,流程不做解析及处理  
callbackData | object | 触发时的扩展信息,流程不做解析及处理  
  
出参样例
    
    
    {
      "error": false,
      "data": {
        extraData: {
          "detailChange": {},
          "useSnapshotForApproval": false
        },
        callbackData: {
          "_triggerActionCode": "Add",
          "optionInfo": {
            "fromMapping": false,
            "fromReferenceCreate": false,
            "skipFuncValidate": false,
            "fromClone": false,
            "fromImport": false,
            "fromDraft": false,
            "supportValidationResult": true,
            "fromTransform": false
          }
        }
      },
      "errorMessage": ""
    }
    
    

**Groovy 举例**
    
    
    Fx.approval.getTriggerDataByInstanceId("618b44e04dfcf72fe16ea6cd").result()
    
    

[Fx.tag](../TagAPI/) [Fx.bpm](../BpmAPI/)

← [Fx.tag](../TagAPI/) [Fx.bpm](../BpmAPI/)→ 

  * 跟随系统 
  * 浅色模式 
  * 深色模式 
  * 阅读模式 


