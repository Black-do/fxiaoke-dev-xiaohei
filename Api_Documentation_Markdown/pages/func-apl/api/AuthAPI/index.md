#  Fx.auth

## # Fx.auth

### # 1\. getUser 以人员为主语进行查询

> `Fx.auth.getUser()`

#### # 参考函数接口

  * 参考com.fxiaoke.functions.api.AuthUserAPI



### # 2\. getRole 以角色为主语进行查询

> `Fx.auth.getRole()`

#### # 参考函数接口

  * 参考com.fxiaoke.functions.api.AuthRoleAPI



### # 3\. getOuterUser 以外部人员为主语进行查询

> `Fx.auth.getOuterUser()`

#### # 参考函数接口

  * 参考com.fxiaoke.functions.api.AuthOuterUserAPI



## # 参考类 com.fxiaoke.functions.api.AuthUserAPI

### # 1\. getRolesByUsers 以人员为主语，查询所有的角色

> `AuthUserAPI.getRolesByUsers(<string roleSource>, <array userIds>)`

**参数说明**

入参格式

参数名称 | object | 描述 | 是否必填  
---|---|---|---  
roleSource | string | 角色类型，1表示内部角色，2表示外部角色 | 是  
userIds | array[string] | 员工id | 是  
  
出参格式

参数名称 | object | 描述  
---|---|---  
appId | string |   
userId | string |   
roleCode | string |   
majorRole | boolean |   
outerTenantId | string |   
  
出参样例
    
    
    {
        "isError": false,
        "data": {
            
        },
        "message": "success"
    }
    
    

**Groovy 举例**
    
    
    def(boolean error, List data, String message) = Fx.auth.user.getRolesByUsers(1, ["1001"])
    if (error) {
      log.info("error: " + message)
    } else {
      log.info(data)
    }
    
    

### # 2\. getUsersByRoleCodes 以角色为主语，查询所有人员

> `AuthUserAPI.getUsersByRoleCodes(<array roleCodes>)`

**参数说明**

入参格式

参数名称 | object | 描述 | 是否必填  
---|---|---|---  
roleCodes | array[string] |  | 是  
  
出参格式

参数名称 | object | 描述  
---|---|---  
appId | string |   
userId | string |   
roleCode | string |   
majorRole | boolean |   
outerTenantId | string |   
  
出参样例
    
    
    {
        "isError": false,
        "data": {
            
        },
        "message": "success"
    }
    
    

**Groovy 举例**
    
    
    List roleCodes = ["00000000000000000000000000000009"]
    def(boolean error, List data, String message) = Fx.auth.user.getUsersByRoleCodes(roleCodes)
    if (error) {
      log.info("error: " + message)
    } else {
      log.info(data)
    }
    
    

**负责人：斯作益seth**

### # 3\. batchAddUserRole 追加角色

> `AuthUserAPI.batchAddUserRole(<array roleCodes>, <boolean updateMajorRole>, <string majorRole>, <array userIds>)`

**参数说明**

入参格式

参数名称 | object | 描述 | 是否必填  
---|---|---|---  
roleCodes | array[string] |  | 是  
updateMajorRole | boolean |  | 是  
majorRole | string |  | 是  
userIds | array[string] |  | 是  
  
**Groovy 举例**
    
    
    def(boolean error, Map data, String message) = Fx.auth.user.batchAddUserRole(["00000000000000000000000000000009"], true,"00000000000000000000000000000009", ["1069"])
    if (error) {
      log.info("error: " + message)
    } else {
      log.info(data)
    }
    
    

**负责人：斯作益seth**

### # 4\. batchSetUserRoles 设置人员的角色，以提交参数为准

> `AuthUserAPI.batchSetUserRoles(<array userIds>, <array roleCodes>, <string majorRole>)`

**参数说明**

入参格式

参数名称 | object | 描述 | 是否必填  
---|---|---|---  
userIds | array[string] |  | 是  
roleCodes | array[string] |  | 是  
majorRole | string |  | 是  
  
**Groovy 举例**
    
    
    def(boolean error, Map data, String message) = Fx.auth.user.batchSetUserRoles(["00000000000000000000000000000009"],"00000000000000000000000000000014",["1046"])
    if (error) {
      log.info("error: " + message)
    } else {
      log.info(data)
    }
    
    

**负责人：斯作益seth**

### # 5\. deleteByUserIds 以角色为主语，删除人员

> `AuthUserAPI.deleteByUserIds(<string roleCode>, <array userIds>)`

**参数说明**

入参格式

参数名称 | object | 描述 | 是否必填  
---|---|---|---  
roleCode | string |  | 是  
userIds | array[string] |  | 是  
  
出参格式

出参样例
    
    
    {
        "isError": false,
        "data": {
            
        },
        "message": "success"
    }
    
    

**Groovy 举例**
    
    
    def(boolean error, Map data, String message) = Fx.auth.user.deleteByUserIds("00000000000000000000000000000009", ["1267"])
    if (error) {
      log.info("error: " + message)
    } else {
      log.info(data)
    }
    
    

**负责人：斯作益seth**

### # 6\. queryUsedCRM 查询企业使用crm角色的数量

> `AuthUserAPI.queryUsedCRM()`

**参数说明**

出参格式

参数名称 | object | 描述  
---|---|---  
usedQuotaSize | integer |   
  
出参样例
    
    
    {
        "isError": false,
        "data": {
            
        },
        "message": "success"
    }
    
    

**Groovy 举例**
    
    
    def(boolean error, Map data, String message) = Fx.auth.user.queryUsedCRM()
    if (error) {
      log.info("error: " + message)
    } else {
      log.info(data)
    }
    
    

**负责人：斯作益seth**

### # 7\. getUsersByRoleCodesWithAppId 以角色为主语，查询所有人员

> `AuthUserAPI.getUsersByRoleCodesWithAppId(<string appId>, <array roleCodes>)`

**参数说明**

入参格式

参数名称 | object | 描述 | 是否必填  
---|---|---|---  
appId | string |  | 是  
roleCodes | array[string] |  | 是  
  
出参格式

参数名称 | object | 描述  
---|---|---  
appId | string |   
userId | string |   
roleCode | string |   
majorRole | boolean |   
outerTenantId | string |   
  
出参样例
    
    
    {
        "isError": false,
        "data": {
            
        },
        "message": "success"
    }
    
    

**Groovy 举例**
    
    
    List roleCodes = ["00000000000000000000000000000009"]
    def appId = "facishare-system"
    def(boolean error, List data, String message) = Fx.biz.callAPI("getUsersByRoleCodesWithAppId",appId,roleCodes)
    if (error) {
      log.info("error: " + message)
    } else {
      log.info(data)
    }
    
    

## # 参考类 com.fxiaoke.functions.api.AuthRoleAPI

### # 1\. getRoleList 查询角色列表

> `AuthRoleAPI.getRoleList(<array appIds>, <string roleSource>)`

**参数说明**

入参格式

参数名称 | object | 描述 | 是否必填  
---|---|---|---  
appIds | array[string] |  | 是  
roleSource | string |  | 是  
  
出参格式

参数名称 | object | 描述  
---|---|---  
list | array[object] |   
list | object | 描述  
---|---|---  
groupName | string |   
roleName | string |   
roleCode | string |   
roleType | integer |   
appId | string |   
tenantId | string |   
description | string |   
delFlag | boolean |   
roleOrder | string |   
  
出参样例
    
    
    {
        "isError": false,
        "data": {
            
        },
        "message": "success"
    }
    
    

**Groovy 举例**
    
    
    def(boolean error, List data, String message) = Fx.auth.role.getRoleList(1)
    if (error) {
      log.info("error: " + message)
    } else {
      log.info(data)
    }
    
    

**负责人：斯作益seth**

### # 2\. createAdminRole 添加管理功能权限角色

> `AuthRoleAPI.createAdminRole(<string roleName>, <string description>, <string roleType>, <string sourceRoleCode>, <string appId>, <string licenseCode>)`

**参数说明**

入参格式

参数名称 | object | 描述 | 是否必填  
---|---|---|---  
roleName | string |  | 是  
description | string |  | 是  
roleType | string |  | 是  
sourceRoleCode | string |  | 是  
appId | string |  | 是  
licenseCode | string |  | 是  
  
出参格式

参数名称 | object | 描述  
---|---|---  
roleCode | string |   
errorReason | string |   
  
出参样例
    
    
    {
        "isError": false,
        "data": {
            
        },
        "message": "success"
    }
    
    

**Groovy 举例**
    
    
    String roleName = "自定义管理功能权限"
    String description = "自定义管理功能权限描述"
    def (boolean error, Map returnObj, String message) = Fx.auth.role.createAdminRole(roleName, description)
    if (error){
      log.info('=====' + message)
    } else {
      log.info('returnObj:' + returnObj)
    }
    
    

**负责人：斯作益seth**

### # 3\. createRole 添加角色

> `AuthRoleAPI.createRole(<string appId>, <string roleName>, <array functionCodes>, <string description>)`

**参数说明**

入参格式

参数名称 | object | 描述 | 是否必填  
---|---|---|---  
appId | string |  | 是  
roleName | string |  | 是  
functionCodes | array[string] |  | 是  
description | string |  | 是  
  
出参格式

参数名称 | object | 描述  
---|---|---  
roleCode | string |   
  
出参样例
    
    
    {
        "isError": false,
        "data": {
            
        },
        "message": "success"
    }
    
    

**Groovy 举例**
    
    
    String roleName = "自定义管理功能权限"
    String description = "自定义管理功能权限描述"
    String roleGroupCode = "roleGroupCode1"
    def (boolean error, Map returnObj, String message) = Fx.auth.role.createRole(roleName, description, roleGroupCode)
    if (error){
      log.info('=====' + message)
    } else {
      log.info('returnObj:' + returnObj)
    }
    
    

**负责人：斯作益seth**

### # 4\. deleteRole 删除角色

> `AuthRoleAPI.deleteRole(<string roleCode>, <boolean isManagement>)`

**参数说明**

入参格式

参数名称 | object | 描述 | 是否必填  
---|---|---|---  
roleCode | string |  | 是  
isManagement | boolean |  | 是  
  
出参格式

参数名称 | object | 描述  
---|---|---  
roleCode | string |   
  
出参样例
    
    
    {
        "isError": false,
        "data": {
            
        },
        "message": "success"
    }
    
    

**Groovy 举例**
    
    
    String roleCode = "1234"
    def (boolean error, Map returnObj, String message) = Fx.auth.role.deleteRole(roleCode)
    if (error){
      log.info('=====' + message)
    } else {
      log.info('returnObj:' + returnObj)
    }
    
    

**负责人：斯作益seth**

### # 5\. updateRole 更新角色

> `AuthRoleAPI.updateRole(<string roleCode>, <string roleName>, <string description>, <string roleGroupCode>)`

**参数说明**

入参格式

参数名称 | object | 描述 | 是否必填  
---|---|---|---  
roleCode | string |  | 是  
roleName | string |  | 是  
description | string |  | 是  
roleGroupCode | string |  | 是  
  
出参格式

参数名称 | object | 描述  
---|---|---  
roleCode | string |   
  
出参样例
    
    
    {
        "isError": false,
        "data": {
            
        },
        "message": "success"
    }
    
    

**Groovy 举例**
    
    
    String roleCode = "1234"
    String roleName = "自定义管理功能权限"
    String description = "自定义管理功能权限描述"
    String roleGroupCode = "roleGroupCode1"
    def (boolean error, Map returnObj, String message) = Fx.auth.role.updateRole(roleCode, roleName, description, roleGroupCode)
    if (error){
      log.info('=====' + message)
    } else {
      log.info('returnObj:' + returnObj)
    }
    
    

**负责人：斯作益seth**

### # 6\. replicateRole 复制角色,不能复制CRM管理员的角色

> `AuthRoleAPI.replicateRole(<string fromRoleCode>, <string roleName>, <string description>, <string roleGroupCode>, <boolean isManagement>)`

**参数说明**

入参格式

参数名称 | object | 描述 | 是否必填  
---|---|---|---  
fromRoleCode | string |  | 是  
roleName | string |  | 是  
description | string |  | 是  
roleGroupCode | string |  | 是  
isManagement | boolean |  | 是  
  
**Groovy 举例**
    
    
    String fromRoleCode = "1234"
    String roleName = "自定义管理功能权限"
    String description = "自定义管理功能权限描述"
    String roleGroupCode = "roleGroupCode1"
    def (boolean error, Map returnObj, String message) = Fx.auth.role.replicateRole(fromRoleCode, roleName, description, roleGroupCode)
    if (error){
      log.info('=====' + message)
    } else {
      log.info('returnObj:' + returnObj)
    }
    
    

**负责人：斯作益seth**

### # 7\. deleteAdminRole 删除管理功能权限角色

> `AuthRoleAPI.deleteAdminRole(<string appId>, <string roleCode>)`

**参数说明**

入参格式

参数名称 | object | 描述 | 是否必填  
---|---|---|---  
appId | string |  | 是  
roleCode | string |  | 是  
  
出参格式

参数名称 | object | 描述  
---|---|---  
error | string |   
roleCode | string |   
  
出参样例
    
    
    {
        "isError": false,
        "data": {
        },
        "message": "success"
    }
    
    

**Groovy 举例**
    
    
    String roleCode = "1234"
    def (boolean error, Map returnObj, String message) = Fx.auth.role.deleteAdminRole(roleCode)
    if (error){
      log.info('=====' + message)
    } else {
      log.info('returnObj:' + returnObj)
    }
    
    

**负责人：斯作益seth**

### # 8\. updateAdminRole 修改管理功能权限角色

> `AuthRoleAPI.updateAdminRole(<string appId>, <string roleCode>, <string roleName>, <string description>)`

**参数说明**

入参格式

参数名称 | object | 描述 | 是否必填  
---|---|---|---  
appId | string |  | 是  
roleCode | string |  | 是  
roleName | string |  | 是  
description | string |  | 是  
  
出参格式

参数名称 | object | 描述  
---|---|---  
roleCode | string |   
error | string |   
  
出参样例
    
    
    {
        "isError": false,
        "data": {
            
        },
        "message": "success"
    }
    
    

**Groovy 举例**
    
    
    String roleCode = "1234"
    String roleName = "自定义管理功能权限"
    String description = "自定义管理功能权限描述"
    def (boolean error, Map returnObj, String message) = Fx.auth.role.updateAdminRole(roleCode, roleName, description)
    if (error){
      log.info('=====' + message)
    } else {
      log.info('returnObj:' + returnObj)
    }
    
    

**负责人：斯作益seth**

### # 9\. replicateAdminRole 复制角色,不能复制CRM管理员的角色

> `AuthRoleAPI.replicateAdminRole(<string roleName>, <string description>, <integer roleType>, <string sourceRoleCode>, <string appId>, <string licenseCode>)`

**参数说明**

入参格式

参数名称 | object | 描述 | 是否必填  
---|---|---|---  
roleName | string |  | 是  
description | string |  | 是  
roleType | integer |  | 是  
sourceRoleCode | string |  | 是  
appId | string |  | 是  
licenseCode | string |  | 是  
  
出参格式

参数名称 | object | 描述  
---|---|---  
roleCode | string |   
errorReason | string |   
  
出参样例
    
    
    {
        "isError": false,
        "data": {
            
        },
        "message": "success"
    }
    
    

**Groovy 举例**
    
    
    String roleName = "自定义管理功能权限"
    String description = "自定义管理功能权限描述"
    String sourceRoleCode = "sourceRoleCode1"
    def (boolean error, Map returnObj, String message) = Fx.auth.role.replicateAdminRole(roleName, description, sourceRoleCode)
    if (error){
      log.info('=====' + message)
    } else {
      log.info('returnObj:' + returnObj)
    }
    
    

**负责人：斯作益seth**

### # 10\. addRoleWithDepartmentToEmployeesByAppId 给人员分配管理角色，可分配crm管理员

> `AuthRoleAPI.addRoleWithDepartmentToEmployeesByAppId()`

**Groovy 举例**
    
    
    List employeeIds = [1000]
    def currentEmployeeId = 1000
    def roleCodeAndDepartmentIds = [
        "roleCode":"31",
        "departmentIds":[999999]
    ]
    def(boolean error, List data, String message) = Fx.auth.role.addRoleWithDepartmentToEmployeesByAppId(currentEmployeeId, employeeIds, roleCodeAndDepartmentIds)
    
    

**负责人：斯作益seth**

## # 参考类 com.fxiaoke.functions.api.AuthOuterUserAPI

### # 1\. deleteByUserIds 以角色为主语，删除互联人员

> `AuthOuterUserAPI.deleteByUserIds(<array userIds>, <string roleCode>)`

**参数说明**

入参格式

参数名称 | object | 描述 | 是否必填  
---|---|---|---  
userIds | array[string] |  | 是  
roleCode | string |  | 是  
  
**Groovy 举例**
    
    
    def (boolean error, Map returnObj, String message) = Fx.auth.outerUser.deleteByUserIds("CRM", "323376297","00000000000000000000000000000009", ["1000"])
    
    if (error){
       log.info('error: ' + message)
    } else {
       log.info('returnObj:' + returnObj)
    }
    
    

**负责人：斯作益seth**

### # 2\. updateRoles 覆盖更新互联用户的所有角色

> `AuthOuterUserAPI.updateRoles(<array userIds>, <string majorRole>, <array roleCodes>)`

**参数说明**

入参格式

参数名称 | object | 描述 | 是否必填  
---|---|---|---  
userIds | array[string] |  | 是  
majorRole | string |  | 是  
roleCodes | array[string] |  | 是  
  
**Groovy 举例**
    
    
    def (boolean error, Map returnObj, String message) = Fx.auth.outerUser.updateRoles(["300383629"],"5b6817bbe4b066655a6397e4", ["5b6817bbe4b066655a6397e4"])
    
    if (error){
      log.info('error: ' + message)
    } else {
      log.info('returnObj:' + returnObj)
    }
    
    

[Fx.sign](../SignAPI/) [Fx.netdisk](../NetdiskAPI/)

← [Fx.sign](../SignAPI/) [Fx.netdisk](../NetdiskAPI/)→ 

  * 跟随系统 
  * 浅色模式 
  * 深色模式 
  * 阅读模式 


