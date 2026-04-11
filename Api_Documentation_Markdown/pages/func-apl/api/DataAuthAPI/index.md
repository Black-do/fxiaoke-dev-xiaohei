#  Fx.dataAuth

## # Fx.dataAuth

### # 1\. 批量解除临时权限

> `Fx.dataAuth.batchDeleteTemporaryPrivilege(<List userIds>, <List outUserIds>, <List describeApiNames>, <List scenes>, <List dataIds>, <Map createTimeRange>)`

**参数说明**

入参格式

参数名称 | object | 描述 | 是否必填  
---|---|---|---  
userIds | List[string] | 授权人员ID集合 | \--  
outUserIds | List[string] | 外部授权人员ID集合 | \--  
describeApiNames | List[string] | 所属对象apiName集合 | \--  
scenes | List[string] | 所属流程集合。可填写的值：approval（审批流）、bpm（业务流）、stage（阶段推进器）、freeflow（自由流程）、free_approvalflow（自由审批流）、QIXIN（转发企信）、CALL_CENTER（呼叫中心） | \--  
dataIds | List[string] | 数据ID集合 | \--  
createTimeRange | Map | 授权开始时间条件组合。目前支持的比较运算符：EQ、N、LT、GT、LTE、GTE、BETWEEN。可以选择填写一个或多个条件，多个条件之间是 且 的关系。 | \--  
createTimeRange | Map | 授权开始时间条件组合。目前支持的比较运算符：EQ、N、LT、GT、LTE、GTE、BETWEEN。可以选择填写一个或多个条件，多个条件之间是 且 的关系。 | 是否必填  
---|---|---|---  
EQ | Map | 等于，queryTime是必填项 | \--  
N | Map | 不等于，queryTime是必填项 | \--  
LT | Map | 早于，endTime是必填项 | \--  
GT | Map | 晚于，startTime是必填项 | \--  
LTE | Map | 早于等于，endTime是必填项 | \--  
GTE | Map | 晚于等于，startTime是必填项 | \--  
BETWEEN | Map | 时间段，startTime和endTime是必填项 | \--  
EQ | Map | 等于，queryTime是必填项 | 是否必填  
---|---|---|---  
queryTime | integer |  | \--  
N | Map | 不等于，queryTime是必填项 | 是否必填  
---|---|---|---  
queryTime | integer |  | \--  
LT | Map | 早于，endTime是必填项 | 是否必填  
---|---|---|---  
endTime | integer |  | \--  
GT | Map | 晚于，startTime是必填项 | 是否必填  
---|---|---|---  
startTime | integer |  | \--  
LTE | Map | 早于等于，endTime是必填项 | 是否必填  
---|---|---|---  
endTime | integer |  | \--  
GTE | Map | 晚于等于，startTime是必填项 | 是否必填  
---|---|---|---  
startTime | integer |  | \--  
BETWEEN | Map | 时间段，startTime和endTime是必填项 | 是否必填  
---|---|---|---  
startTime | integer |  | \--  
endTime | integer |  | \--  
  
**Groovy 举例**
    
    
    List userIds = [
      "1000"
    ]
    
    List outUserIds = [
      "300090116"
    ]
    
    List describeApiNames = [
      "MarketingEventObj"
    ]
    
    List scenes = [
      "approval"
    ]
    
    List dataIds = [
      "67c947edf40e650007e814e0"
    ]
    
    Map createTimeRange = [
      "EQ": [
        "queryTime":1741244398760
      ]
    ]
    
    def(boolean error, Map data, String message) = Fx.dataAuth.batchDeleteTemporaryPrivilege(userIds, outUserIds, describeApiNames, scenes, dataIds, createTimeRange)
    
    if (error) {
      log.info("error: " + message)
    } else {
      log.info(data)
    }
    
    

**注意事项**

>   * 授权人员ID集合（授权人员ID 或者 外部授权人员ID）、所属对象apiName集合、所属流程集合、数据ID集合、授权开始时间条件组合 不能同时为空。
> 


**负责人：杨华国YHG**

[Fx.hospital](../HospitalAPI/) [Fx.checkins](../CheckinsAPI/)

← [Fx.hospital](../HospitalAPI/) [Fx.checkins](../CheckinsAPI/)→ 

  * 跟随系统 
  * 浅色模式 
  * 深色模式 
  * 阅读模式 


