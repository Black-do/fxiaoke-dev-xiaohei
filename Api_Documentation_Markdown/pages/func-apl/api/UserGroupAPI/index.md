#  Fx.userGroup

## # Fx.userGroup

### # 1\. queryGroupByName 通过名字模糊查询用户组list

> `Fx.userGroup.queryGroupByName(<string name>, <integer status>)`

**参数说明**

入参格式

参数名称 | object | 描述 | 是否必填  
---|---|---|---  
name | string | 模糊搜索的用户名 | 是  
status | integer | 用户组状态 //0:启用 ，1:禁用 | 是  
  
**Groovy 举例**
    
    
    String name ="hb"
    int status = 0
    def(boolean error, List data, String message) = Fx.userGroup.queryGroupByName(name, status)
    if (error) {
      log.info("error: " + message)
    } else {
      log.info(data)
    }
    
    

### # 2\. queryGroupMembers 通过用户组ID获取用户组下的用户Ids

> `Fx.userGroup.queryGroupMembers()`

**Groovy 举例**
    
    
    List groupIdList = ["63bf8075028c7a0001058fc4"]
    def(boolean error, Map data, String message) = Fx.userGroup.queryGroupMembers(groupIdList)
    if (error) {
      log.info("error: " + message)
    } else {
      log.info(data)
    }
    
    

**负责人：张佳鑫ZhangJiaxin(已停用)**

### # 3\. insertGroupMem 用户组添加组成员

> `Fx.userGroup.insertGroupMem()`

**Groovy 举例**
    
    
    String groupId = "63bf8075028c7a0001058fc4"
    List userIdsList = ["1004"]
    def(boolean error, boolean data, String message) = Fx.userGroup.insertGroupMem(groupId, userIdsList)
    if (error) {
      log.info("error: " + message)
    } else {
      log.info(data)
    }
    
    

**负责人：张佳鑫ZhangJiaxin(已停用)**

### # 4\. updateGroupMem 用户组更新组成员

> `Fx.userGroup.updateGroupMem()`

**Groovy 举例**
    
    
    String groupId = "63bf8075028c7a0001058fc4"
    List userIdsList = ["1000","1001","1003","1004"]
    def(boolean error, boolean data, String message) = Fx.userGroup.updateGroupMem(groupId, userIdsList)
    if (error) {
      log.info("error: " + message)
    } else {
      log.info(data)
    }
    
    

**负责人：张佳鑫ZhangJiaxin(已停用)**

### # 5\. deleteGroupMem 用户组删除组成员

> `Fx.userGroup.deleteGroupMem()`

**Groovy 举例**
    
    
    String groupId = "63bf8075028c7a0001058fc4"
    List userIdsList = ["1004"]
    def(boolean error, boolean data, String message) = Fx.userGroup.deleteGroupMem(groupId, userIdsList)
    if (error) {
      log.info("error: " + message)
    } else {
      log.info(data)
    }
    
    

**负责人：张佳鑫ZhangJiaxin(已停用)**

[Fx.industry](../IndustryAPI/) [Fx.hospital](../HospitalAPI/)

← [Fx.industry](../IndustryAPI/) [Fx.hospital](../HospitalAPI/)→ 

  * 跟随系统 
  * 浅色模式 
  * 深色模式 
  * 阅读模式 


