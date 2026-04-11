#  Fx.org

## # Fx.org

### # 1\. findUserById 按用户ID查询用户信息

> `Fx.org.findUserById(<String userId>)`

**参数说明**

入参格式

参数名称 | object | 描述 | 是否必填  
---|---|---|---  
userId | String | 用户id | 是  
  
出参格式

参数名称 | object | 描述  
---|---|---  
1001 | Map | APIResult  
1001 | Map | APIResult  
---|---|---  
package | string |   
  
出参样例
    
    
    {
            "1001": {
                "package": "CRM"
            }
        }
    
    

**Groovy 举例**
    
    
    def(Boolean error, Map data, String errorMessage) = Fx.org.findUserById("1001")
    
    if (error) {
        log.error("获取对象异常" + errorMessage)
        //1.使用报错终止执行
        //Fx.message.throwException("获取对象异常"+errorMessage)
        //2.使用return终止执行
        //return;
        //3.继续执行
    }
    //dosomething
    
    

**注意事项**

>   * 参数不能为空
> 


### # 2\. findByUserIds 按用户Id列表查询若干用户信息

> `Fx.org.findByUserIds(<String userIds>)`

**参数说明**

入参格式

参数名称 | object | 描述 | 是否必填  
---|---|---|---  
userIds | String | 用户id列表 | 是  
  
出参格式

参数名称 | APIResult | API返回结果的JSON Schema  
---|---|---  
isError | boolean | 是否错误  
data | Map | 返回的数据  
message | string | 信息  
  
出参样例
    
    
    {
        "isError" : false,
        "data" : {},
        "message" : ""
    }
    
    

**Groovy 举例**
    
    
    def (Boolean error,Map data,String errorMessage) = Fx.org.findByUserIds(["1001","1002"])
    if (error) {
        log.error("获取对象异常" + errorMessage)
        //1.使用报错终止执行
        //Fx.message.throwException("获取对象异常"+errorMessage)
        //2.使用return终止执行
        //return;
        //3.继续执行
    }
    //dosomething
    
    

### # 3\. findEmployeeByDepartmentId 根据部门id查员工信息

> `Fx.org.findEmployeeByDepartmentId(<String id>)`

**参数说明**

入参格式

参数名称 | object | 描述 | 是否必填  
---|---|---|---  
id | String | 部门id | 是  
  
出参格式

参数名称 | object | 描述  
---|---|---  
departmentId | String | 部门id  
name | String | 部门名称  
tenantId | String | 企业id  
ViceDepartmentIds | List | 附属部门  
employee | String | 员工id  
type | integer | 1：内部员工 2：外部员工  
status | integer | 部门状态 1：正常 2：停用 3：删除  
  
出参样例
    
    
    [{"departmentId":"1000","name":"杨紫","tenantId":"85154","ViceDepartmentIds":[],"employee":"1002","type":1,"status":1}]
    
    

**Groovy 举例**
    
    
    def (Boolean error,List data,String errorMessage) = Fx.org.findEmployeeByDepartmentId('1061')
    
    

**注意事项**

>   * 返回的数据类型: List String departmentId：主属部门Id String name 部门名称 String tenantId 企业id List ViceDepartmentIds 附属部门id String employee 员工Id Integer type 员工类型 1：内部员工 2：外部员工 Integer status 部门状态 1：正常 2：停用 3：删除
> 


### # 4\. findDepartmentByIds 根据部门ID列表，查询部门信息

> `Fx.org.findDepartmentByIds(<List id>)`

**参数说明**

入参格式

参数名称 | object | 描述 | 是否必填  
---|---|---|---  
id | List[string] | 部门ids | 是  
  
出参格式

参数名称 | object | 描述  
---|---|---  
owner | List[string] | 负责人  
superordinateDepartmentId | String | 上级部门id  
departmentId | String | 部门id  
name | String | 部门名称  
enterpriseId | String | 企业id  
  
出参样例
    
    
    {"owner":["1000"],"superordinateDepartmentId":"1038","departmentId":"1001","name":"明星部0866111112","enterpriseId":"85154"}
    
    

**Groovy 举例**
    
    
    def (Boolean error,List data,String errorMessage) = Fx.org.findDepartmentByIds(['1016'])
    
    

**注意事项**

>   * 由于下游企业在上游企业组织架构里，相当于是一个部门，所以也可用该函数查询下游企业的对接人，此时 owner 表示：下游企业的对接人
> 


### # 5\. findSuperordinateDepartments 根据部门id查上级部门信息

> `Fx.org.findSuperordinateDepartments(<String id>, <Boolean recursion>)`

**参数说明**

入参格式

参数名称 | object | 描述 | 是否必填  
---|---|---|---  
id | String | 部门id | 是  
recursion | Boolean | 是否递归 | 是  
  
出参格式

参数名称 | object | 描述  
---|---|---  
owner | List[string] | 负责人  
superordinateDepartmentId | String | 上级部门id  
departmentId | String | 部门id  
name | String | 部门名称  
enterpriseId | String | 企业id  
  
出参样例
    
    
    {"1001":{"owner":["1000"],"superordinateDepartmentId":"1038","departmentId":"1001","name":"明星部0866111112","enterpriseId":"85154"}}
    
    

**Groovy 举例**
    
    
    def (Boolean error,Map data,String errorMessage) = Fx.org.findSuperordinateDepartments('1016', true)
    
    

### # 6\. findSubordinateDepartments 根据部门id查下级部门信息

> `Fx.org.findSubordinateDepartments(<String id>, <Boolean recursion>)`

**参数说明**

入参格式

参数名称 | object | 描述 | 是否必填  
---|---|---|---  
id | String | 部门id | 是  
recursion | Boolean | 是否递归 | 是  
  
出参格式

参数名称 | object | 描述  
---|---|---  
owner | List[string] | 负责人  
superordinateDepartmentId | String | 上级部门id  
departmentId | String | 部门id  
name | String | 部门名称  
enterpriseId | String | 企业id  
  
出参样例
    
    
    {"1001":{"owner":["1000"],"superordinateDepartmentId":"1038","departmentId":"1001","name":"明星部0866111112","enterpriseId":"85154"}}
    
    

**Groovy 举例**
    
    
    def (Boolean error,Map data,String errorMessage) = Fx.org.findSubordinateDepartments('1016',true)
    
    

**注意事项**

>   * 根据参数 recursion 是否递归
> 


### # 7\. findOutUserById 查询外部人员信息

> `Fx.org.findOutUserById()`

**Groovy 举例**
    
    
    def (boolean error,Map result,String errorMessage) = Fx.org.findOutUserById("300090724")
    
    

**负责人：尚壬鹏ShawnRennPenn**

### # 8\. findOutUserByIds 批量查询外部人员信息

> `Fx.org.findOutUserByIds()`

**Groovy 举例**
    
    
    def (boolean error,Map result,String errorMessage)  = Fx.org.findOutUserByIds(["300090724"])
    
    

**注意事项**

>   * 查询外部人员信息。
> 


**负责人：尚壬鹏ShawnRennPenn**

### # 9\. getCompanyInfo 获得企业信息

> `Fx.org.getCompanyInfo()`

**参数说明**

出参格式

参数名称 | object | 描述  
---|---|---  
tenantType | String | 企业类型  
defaultLanguage | String | 默认语言  
defaultTimeZone | String | 默认时区  
companyName | String | 公司名称  
tenantId | String | 企业Id  
isSandbox | String | 是否为沙盒企业  
  
出参样例
    
    
    {
        "tenantType": "enterprise_edition",
        "defaultLanguage": "zh-CN",
        "defaultTimeZone": "Asia/Shanghai",
        "companyName": "Java函数开发专用",
        "tenantId": "83740",
        "isSandbox": false
    }
    
    

**Groovy 举例**
    
    
    def (boolean error,Map result,String errorMessage)  = Fx.org.getCompanyInfo()
    
    

[Fx.object](../ObjectDataAPI/) [Fx.http](../HttpAPI/)

← [Fx.object](../ObjectDataAPI/) [Fx.http](../HttpAPI/)→ 

  * 跟随系统 
  * 浅色模式 
  * 深色模式 
  * 阅读模式 


