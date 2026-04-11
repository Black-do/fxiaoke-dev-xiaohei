#  Fx.checkins

## # Fx.checkins

### # 1\. 新建外勤计划

> `Fx.checkins.createPlan(<CreatePlanArg arg>)`

**参数说明**

入参格式

参数名称 | 参数类型 | 描述 | 是否必填  
---|---|---|---  
arg | CreatePlanArg |  | 是  
arg | CreatePlanArg | 描述 | 是否必填  
---|---|---|---  
executorId | string | 外勤的执行人 | 是  
planTime | integer | 外勤计划时间 | 是  
checkTypeId | string | 外勤类型Id | 是  
mainObjList | List[ObjectInfo] | 外勤的主对象 | \--  
userId | string | 创建人信息 | 是  
assistantIds | List[integer] | 协防人列表 | \--  
referenceObject | List[ObjectInfo] | 外勤的从对象 | \--  
extFields | Map | 自定义字段的APiName以及value | \--  
mainObjList | ObjectInfo | 描述 | 是否必填  
---|---|---|---  
dataId | string | 对象的id | 是  
apiName | string | 对象apiName | 是  
name | string | 对象名称 | 是  
info | string | 地址 | \--  
objName | string | 主属性 | 是  
recordType | string | 业务类型APIName | \--  
recordTypeName | string | 业务类型名称 | \--  
showRecordTypeName | string | 显示业务类型 | \--  
referenceObject | ObjectInfo | 描述 | 是否必填  
---|---|---|---  
dataId | string | 对象的id | 是  
apiName | string | 对象apiName | 是  
name | string | 对象名称 | 是  
info | string | 地址 | \--  
objName | string | 主属性 | 是  
  
出参格式

参数名称 | object | 描述  
---|---|---  
checkinId | string | 外勤的Id  
  
出参样例
    
    
    {
        "checkinId":""
    }
    
    

**Groovy 举例**
    
    
    List userId = context.data.owner as List //客户负责人
    String accountId = context.data._id as String //客户ID
    String name = context.data.name as String //客户名称
    String location = context.data.location as String //客户详细地址 其他对象可以不传
    //拜访时间 当前时间+5天  这个可以添加任意未来的时间
    DateTime nowDate=DateTime.now()+5.days  
    // 构造外勤主对象数据
    Map mainObject=[:]
    mainObject.put("dataId",  accountId)          //数据id
    mainObject.put("apiName",  "AccountObj")      //对象apiName
    mainObject.put("objName",  "客户")            //对象的名称
    mainObject.put("name",  name)                 //对象的主属性
    mainObject.put("info",  location)             //客户地址
    mainObject.put("remark",  "按计划拜访客户")   //外勤计划描述
    mainObject.put("recordType",  "default__c")   //业务类型APIName
    mainObject.put("recordTypeName",  "预设业务类型")   //业务类型名称
    mainObject.put("showRecordTypeName",  true)   //显示业务类型
    List mainObjList = [mainObject]
    // 构造外勤从对象数据 具体看实际业务场景 如果没有外勤类型中没有从对象  这个字段不需要赋值
    Map referenceObject=[:]
    referenceObject.put("dataId",  "6218471c80406d000163b57e")         //数据id
    referenceObject.put("apiName",  "object_CE1O0__c")                 //对象apiName
    referenceObject.put("objName",  "海子函数模板库")                  //  对象名称
    referenceObject.put("name", "asaas")                               //  主属性
    List referenceObjectList = [referenceObject]                       //
    Map paramField=[:] //入参
    paramField.put("userId",  userId[0])                               //创建人id
    paramField.put("checkTypeId",  "62173855e0eff651e2253c86")         //外勤类型id （default_check_type_id 代表是普通外勤  高级外勤需要F12抓下参数取到typeId）
    paramField.put("planTime",  nowDate.toTimestamp())                 //计划执行时间的时间戳
    paramField.put("executorId",   userId[0])                          //执行人id
    paramField.put("assistantIds", [])                                 //协访人idList (非必填)
    paramField.put("mainObjList",  mainObjList)
    paramField.put("referenceObject",  referenceObjectList)
    Map extFields = [:]
    extFields.put("field_4K9Zd__c","自定义字段的值") //自定义字段赋值 不需要的话 不用传
    paramField.put("extFields",extFields)
    
    log.info("新建外勤计划参数："+paramField)
    
    def (Boolean createPlan_error,Map createPlan_data,String createPlan_errorMessage) = Fx.checkins.createPlan(paramField)
    if(!createPlan_error){
      log.info("创建成功，外勤Id为：" + createPlan_data["checkinId"] as String)
    }else{
      log.info("创建失败，原因为：" + createPlan_errorMessage)
    }
    
    

**注意事项**

>   * ObjectInfo中的info字段参考：116.331642#%$39.97884#%$北京市海淀区中关村东路
> 


### # 2\. 删除高级外勤

> `Fx.checkins.delCheckins(<string checkinsId>)`

**参数说明**

入参格式

参数名称 | object | 描述 | 是否必填  
---|---|---|---  
checkinsId | string | 外勤类型Id | 是  
  
**Groovy 举例**
    
    
    def (boolean error,String data,String errorMessage) = Fx.checkins.delCheckins("外勤Id");
    if(error){
      log.info("delCheckins is error Response:" + errorMessage)
    }else{
      log.info("delCheckins is success")
    }
    
    

### # 3\. 更新高级外勤自定义字段

> `Fx.checkins.editExtFields(<int operatorUserId>, <string checkinsId>, <Map extFieldMap>)`

**参数说明**

入参格式

参数名称 | object | 描述 | 是否必填  
---|---|---|---  
operatorUserId | int | 操作用户Id | 是  
checkinsId | string | 外勤Id | 是  
extFieldMap | Map | 要更新的字段以及其value 仅支持自定义字段 | 是  
  
**Groovy 举例**
    
    
    Map extFieldMap = ["field_cM25i__c":5.6]  // 要更新的字段以及其value  仅支持自定义字段
    def (boolean error, Map data, String message) = Fx.checkins.editExtFields(1000,"67d3dd964036d37c62ac4e75",extFieldMap);
    if(error){
      log.info("editExtFields is error respone:" + message)
    }else{
      log.info("editExtFields is success")
    }
    
    

### # 4\. 批量更新高级外勤自定义字段

> `Fx.checkins.batchUpdateFields(<List checkinsIds>, <Map extFields>)`

**参数说明**

入参格式

参数名称 | object | 描述 | 是否必填  
---|---|---|---  
checkinsIds | List[string] |  | 是  
extFields | Map |  | 是  
  
**Groovy 举例**
    
    
    Map extFieldMap = ["field_cM25i__c":5.8]  //要更新的字段以及其value  仅支持自定义字段
    List checkIds = ["67d3dd964036d37c62ac4e75","67d3dd544036d37c62ac4e6d"]
    def (boolean error, Map data, String message) = Fx.checkins.batchUpdateFields(checkIds,extFieldMap);
    if(error){
      log.info("batchUpdateFields is error respone:" + message)
    }else{
      log.info("batchUpdateFields is success")
    }
    
    

**注意事项**

>   * 不同步到高级外勤对象，只在外勤日历有效果，想要同步到对象，请使用单条更新的函数。
> 


### # 5\. 查询员工外勤记录

> `Fx.checkins.getCheckinsDataList(<integer pageNum>, <integer pageSize>, <long startTime>, <long endTime>, <List userIds>)`

**参数说明**

入参格式

参数名称 | object | 描述 | 是否必填  
---|---|---|---  
pageNum | integer | 第N页 | 是  
pageSize | integer | 每页数量 | 是  
startTime | long | 开始时间 传入毫秒 | 是  
endTime | long | 结束时间 传入毫秒 | 是  
userIds | List[integer] | 人员Id | 是  
  
出参格式

参数名称 | CheckData | 描述  
---|---|---  
total | integer |   
checkDatas | List[CheckDataDetail] |   
checkDatas | CheckDataDetail | 描述  
---|---|---  
ownerAccount | string | 负责人 E.ea.员工Id  
checkinsId | string | 外勤id  
checkinsTimeStamp | integer | 签到时间戳  
checkinsLon | number | 签到坐标Lon  
checkinsLat | number | 签到坐标Lat  
feedId | integer | feedId  
checkinsAddressDesc | string | 签到位置名称.描述  
ruleId | string | 签到规则id  
contentText | string | 签到内容  
newCustomerId | string | 关联客户的Id  
checkinsDistnace | integer | 关联客户距离  
cheatRisk | integer | 作弊风险, 0- 正常、1- IOS越狱、2- Android 作弊软件、3- Android 伪造地址  
cheatRiskDesc | string | 设备风险描述  
distanceRisk | boolean | 距离异常  
deviceRisk | boolean | 设备异常  
checkOutTime | integer | 签退时间  
checkOutLat | number | 签退坐标Lat  
checkOutLon | number | 签退坐标Lon  
checkOutAddressDesc | string | 签退位置名称.描述  
mainObjectInfo | object | 主对象信息  
checkTypeId | string | 外勤类型Id  
deviceId | string | 设备Id  
imageFiles | array[object] | 图片信息  
  
**Groovy 举例**
    
    
    def (Boolean error,Map data,String errorMessage) =  Fx.checkins.getCheckinsDataList(1,20,1645750400000,1741944322442,[1000])
    if(error){
      log.info("getCheckOfficeDataList is error Response:" + errorMessage)
    }else{
      log.info(data)
    }
    
    

### # 6\. 查询高级外勤主子对象信息

> `Fx.checkins.getVisitObjInfoById(<string checkId>)`

**参数说明**

入参格式

参数名称 | object | 描述 | 是否必填  
---|---|---|---  
checkId | string | 外勤Id | 是  
  
出参格式

参数名称 | object | 描述  
---|---|---  
mainObjInfo | ObjectInfo |   
referenceObject | List[ObjectInfo] |   
  
**Groovy 举例**
    
    
    def(Boolean error,Map data,String errorMessage) = Fx.checkins.getVisitObjInfoById("67d3dd544036d37c62ac4e6d")
    
    if(!error){
      log.info("ret:" + data)
    }else{
      log.info("函数执行异常:" + errorMessage)
    }
    
    

### # 7\. 重新同步高级外勤数据

> `Fx.checkins.syncCheckins(<List checkIdList>, <boolean isInterconnect>, <string syncMode>)`

**参数说明**

入参格式

参数名称 | object | 描述 | 是否必填  
---|---|---|---  
checkIdList | List[string] |  | 是  
isInterconnect | boolean | 是否为互联 | 是  
syncMode | string | 同步方式,不填写默认为check_obj_add | \--  
  
**Groovy 举例**
    
    
    List checkIds = ["67d3dd964036d37c62ac4e75"]
    def (Boolean error,List data,String errorMessage) = Fx.checkins.syncCheckins(checkIds,false)
    if(error){
      log.info("syncCheckinsData is error Response: " + errorMessage)
    }else{
      log.info(data)
    }
    
    

**注意事项**

>   * syncMode 参数取值范围
>   * check_obj_add 新增
>   * check_obj_edit 编辑
>   * check_finish 完成
> 


[Fx.dataAuth](../DataAuthAPI/)

← [Fx.dataAuth](../DataAuthAPI/)

  * 跟随系统 
  * 浅色模式 
  * 深色模式 
  * 阅读模式 


