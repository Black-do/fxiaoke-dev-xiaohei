#  Fx.tag

## # Fx.tag

### # 1\. findTagDefine 查找对象适用的标签

> `Fx.tag.findTagDefine(<string objectApiName>)`

**参数说明**

入参格式

参数名称 | object | 描述 | 是否必填  
---|---|---|---  
objectApiName | string | 对象apiName | 是  
  
出参格式

参数名称 | APIResult | 描述  
---|---|---  
isError | boolean | 是否错误  
data | QueryResult | 返回的数据  
message | string | 信息  
data | QueryResult | 返回的数据  
---|---|---  
dataList | array[object] |   
size | integer | 数量  
total | integer | 总量  
dataList | object | 标签的描述  
---|---|---  
tagGroup | string | 标签所在分组  
tagGroupId | string | 标签所在分组id  
tagId | string | 标签id  
tagApiName | string | 标签api  
name | string | 标签名称  
tagGroupApiName | string | 标签分组api  
  
出参样例
    
    
    {
        "isError": false,
        "data": {
            "dataList": [
                {
                    "tagGroup": "lzhh-tag",
                    "tagGroupId": "66d981dde18ae10007ce06f3",
                    "tagId": "66d981dde18ae10007ce06f4",
                    "tagApiName": "label_Uj3sC__c",
                    "name": "lzhh标签名称2",
                    "tagGroupApiName": "group_RW66c__c"
                }
            ],
            "size": 1,
            "total": 1
        },
        "message": ""
    }
    
    

**Groovy 举例**
    
    
    APIResult ret  = Fx.tag.findTagDefine("object_76is3__c")
    log.info(ret)
    
    

**参考对象**

  * 参考null



### # 2\. findTagById 查找某条数据上的所有标签

> `Fx.tag.findTagById(<string objectApiName>, <string dataId>)`

**参数说明**

入参格式

参数名称 | object | 描述 | 是否必填  
---|---|---|---  
objectApiName | string |  | 是  
dataId | string |  | 是  
  
出参格式

参数名称 | APIResult | 描述  
---|---|---  
isError | boolean | 是否错误  
data | array[object] | 返回的数据列表  
message | string | 信息  
data | object | 标签信息  
---|---|---  
tagId | string | 标签id  
name | string | 标签名称  
  
出参样例
    
    
    {
        "isError": false,
        "data": [
            {
                "tagId": "642fb2458085c60001d03744",
                "name": "2"
            }
        ],
        "message": ""
    }
    
    

**Groovy 举例**
    
    
    APIResult ret  = Fx.tag.findTagById( "obj_lzhh_pure__c", "66d956ca0410610007694b99")
    log.info(ret)
    
    

### # 3\. update 更新数据的标签

> `Fx.tag.update(<string objectApiName>, <string dataId>, <array tagIdList>)`

**参数说明**

入参格式

参数名称 | object | 描述 | 是否必填  
---|---|---|---  
objectApiName | string |  | 是  
dataId | string |  | 是  
tagIdList | array[string] |  | 是  
  
出参格式

参数名称 | APIResult | 描述  
---|---|---  
isError | boolean | 是否错误  
data | string | 被更新标签的id  
message | string | 信息  
  
出参样例
    
    
    {
        "isError": false,
        "data": "66d956ca0410610007694b99",
        "message": ""
    }
    
    

**Groovy 举例**
    
    
    def (Boolean error,String data,String errorMessage) = Fx.tag.update("obj_lzhh_pure__c", "66d956ca0410610007694b99", [])
    log.info(data)
    
    

**注意事项**

>   * 空list会删除所有标签
>   * 会检查tag和数据是否适配, 不适配回参error=true, 如果错误信息是Error in bulkHangTagForData, 原因大概率是tag不适用当前对象, 可以使用Fx.tag.findTagDefine查找适用的tag
> 


### # 4\. createTag 创建标签

> `Fx.tag.createTag(<string description>, <string groupId>, <string tagApiName>, <string tagName>)`

**参数说明**

入参格式

参数名称 | object | 描述 | 是否必填  
---|---|---|---  
description | string |  | 是  
groupId | string | tag组的id, 必须已经存在 | 是  
tagApiName | string |  | 是  
tagName | string |  | 是  
  
出参格式

参数名称 | APIResult | 描述  
---|---|---  
isError | boolean | 是否错误  
data | string | 生成的标签的id  
message | string | 信息  
  
出参样例
    
    
    {
        "isError": false,
        "data": "66da75ab6a3bb50007ad52de",
        "message": ""
    }
    
    

**Groovy 举例**
    
    
    def arg = TagArg.builder()
            .groupId("5ea3b0e5e1a70b0001e2f65b")
            .tagApiName("tag_scDwW_tesat2__c")
            .tagName("函数创建标签1-aafj-test2")
            .description("test001")
            .build();
    APIResult ret  = Fx.tag.createTag(arg)
    log.info(ret)
    
    

**参考对象**

  * 参考TagArg



**注意事项**

>   * tag组必须已经存在
> 


### # 5\. updateTag 更新标签

> `Fx.tag.updateTag(<string description>, <string groupId>, <string tagId>, <string tagName>)`

**参数说明**

入参格式

参数名称 | object | 描述 | 是否必填  
---|---|---|---  
description | string |  | 是  
groupId | string |  | 是  
tagId | string |  | 是  
tagName | string |  | 是  
  
出参格式

参数名称 | APIResult | 描述  
---|---|---  
isError | boolean | 是否错误  
data | null |   
message | string | 信息  
  
出参样例
    
    
    {
        "isError": false,
        "data": null,
        "message": ""
    }
    
    

**Groovy 举例**
    
    
    def arg = TagArg.builder()
           .groupId("5ea3b0e5e1a70b0001e2f65b")
           .tagId("66da75ab6a3bb50007ad52de")
           .tagName("函数签03-f--asas---j")
           .description("更新标签3")
           .build()
    def result = Fx.tag.updateTag(arg)
    
    

**参考对象**

  * 参考TagArg



**注意事项**

>   * 更新是异步进行的, 所以这函数没有返回值, 可以通过Fx.tag.findTagByTagIds来查看是否修改成功
> 


### # 6\. createTagGroup 创建标签分组

> `Fx.tag.createTagGroup(<String api_name>, <String tag_group_name>, <String describe_api_names>, <String is_applied_to_all>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
api_name | String | 分组apiName | 是  
tag_group_name | String | 分组名称 | 是  
describe_api_names | String[string] | 适用对象列表 | 是  
is_applied_to_all | String | 是否适用全部对象 | 是  
  
出参格式

参数名称 | 类型 | 描述  
---|---|---  
tagDescribe | object |   
tagDescribe | object | 描述  
---|---|---  
createTime | Interger | 创建时间  
deleted | Boolean | 是否删除  
isActive | Boolean | 是否禁用  
apiName | String | 分组apiName  
lastModifiedBy | String | 最后修改人  
tagRange | List[string] | 适用对象列表  
isAll | Boolean | 是否适用所有对象  
tagDefineType | String | 类型  
groupDescription | String | 分组描述  
tenantId | String | 企业id  
createdBy | String | 创建人  
id | String | 分组id  
type | String | 分组名称  
lastModifiedTime | Integer | 最后修改时间  
  
出参样例
    
    
    {
        "createTime": 1728649707933,
        "deleted": false,
        "isActive": true,
        "apiName": "group_YpkQ3__c",
        "lastModifiedBy": "1000",
        "tagRange": [
            "MarketingKeywordObj",
            "EnterpriseInfoObj"
        ],
        "isAll": false,
        "tagDefineType": "custom",
        "groupDescription": "实打实打算",
        "tenantId": "78057",
        "createdBy": "1000",
        "id": "670919eb4306ff0007bf397f",
        "type": "测试",
        "lastModifiedTime": 1728649707933,
        "containerDocument": {
            "_id": "670919eb4306ff0007bf397f",
            "tenant_id": "78057",
            "type": "测试",
            "is_deleted": false,
            "tag_define_type": "custom",
            "describe_api_name": null,
            "created_by": "1000",
            "last_modified_by": "1000",
            "create_time": 1728649707933,
            "last_modified_time": 1728649707933,
            "tag_range": [
                "MarketingKeywordObj",
                "EnterpriseInfoObj"
            ],
            "is_all": false,
            "api_name": "group_YpkQ3__c",
            "is_mutex": null,
            "is_active": true,
            "group_description": "实打实打算"
        }
    }
    
    

**Groovy 举例**
    
    
    def (String message,Map data,Boolean error) = Fx.tag.createTagGroup(["AccountObj"],"group_ceshi11__c",false,"测试分组名称123")
    
    

### # 7\. updateTagGroup 修改标签分组

> `Fx.tag.updateTagGroup(<String api_name>, <String id>, <List describe_api_names>, <Boolean is_applied_to_all>, <String tag_group_name>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
api_name | String | 标签分组apiName | 是  
id | String | 标签分组id | 是  
describe_api_names | List[String] | 该标签分组适用的对象列表 | 是  
is_applied_to_all | Boolean | 是否适用全部对象 | 是  
tag_group_name | String | 分组名称 | 是  
  
出参格式

参数名称 | object | 描述  
---|---|---  
Result | object |   
Value | object |   
Result | object | 描述  
---|---|---  
FailureCode | integer |   
StatusCode | integer |   
UserInfo | object |   
UserInfo | object | 描述  
---|---|---  
EmployeeID | integer |   
EnterpriseAccount | string |   
Value | object | 描述  
---|---|---  
tagDescribe | object |   
tagDescribe | object | 描述  
---|---|---  
createTime | Integer | 创建时间  
isActive | Boolean | 分组状态  
deleted | Boolean | 是否删除  
tagRange | List[string] | 适用对象范围  
isAll | Boolean | 是否适用全部对象  
isMutex | Boolean | 是否互斥  
apiName | String | 分组apiName  
tagDefineType | String | 标签分类类型  
groupDescription | String | 分组描述  
lastModifiedBy | String | 最后修改人  
createdBy | String | 创建人  
tenantId | String | 企业id  
id | String | 分组id  
range | Object | 人员适用范围  
type | String | 分组名称  
lastModifiedTime | Integer | 最后修改时间  
  
出参样例
    
    
    {
        "Result": {
            "FailureCode": 0,
            "StatusCode": 0,
            "UserInfo": {
                "EmployeeID": 1000,
                "EnterpriseAccount": "74255"
            }
        },
        "Value": {
            "tagDescribe": {
                "createTime": 1587785957907,
                "isActive": true,
                "deleted": false,
                "tagRange": [
                    "AccountFinInfoObj"
                ],
                "isAll": false,
                "isMutex": false,
                "apiName": "ceshi002__c",
                "tagDefineType": "custom",
                "groupDescription": "测试数据描述",
                "lastModifiedBy": "1000",
                "createdBy": "1000",
                "tenantId": "74255",
                "id": "5ea3b0e5e1a70b0001e2f65b",
                "range": {},
                "type": "测试数据",
                "lastModifiedTime": 1728565061702
            }
        }
    }
    
    

**Groovy 举例**
    
    
    def(String message,Map data,Boolean error) = Fx.tag.updateTagGroup("group_ceshi11__c","624272c1babe24000101d2e5",[],true,"更改测试名")
    if
    
    

**注意事项**

>   * 1.参数api_name限制：（1）不能为空，（2）不能修改
>   * 2.参数tag_group_name：（1）不能为空，（2）数量不能大于10个字符
> 


### # 8\. deleteTagGroup 删除标签分组

> `Fx.tag.deleteTagGroup(<String api_name>, <String id>)`

**参数说明**

入参格式

参数名称 | object | 描述 | 是否必填  
---|---|---|---  
api_name | String | 标签分组apiName | 是  
id | String | 标签分组id | 是  
  
**Groovy 举例**
    
    
    def(String message,Map data,Boolean error) = Fx.tag.deleteTagGroup("624272c1babe24000101d2e5")
    
    

### # 9\. enableTag 启用标签

> `Fx.tag.enableTag(<String tag_group_id>, <String tag_group_api_name>, <String tag_id>, <String tag_api_name>)`

**参数说明**

入参格式

参数名称 | object | 描述 | 是否必填  
---|---|---|---  
tag_group_id | String | 标签分组id | 是  
tag_group_api_name | String | 标签分组apiName | 是  
tag_id | String | 标签id | 是  
tag_api_name | String | 标签apiName | 是  
  
**Groovy 举例**
    
    
    def result = Fx.tag.enableTag("tag_scDwW__c","group_ceshi11__c","62427820babe24000101d80d","6242784d06e1bf00015f33ec")
    
    

### # 10\. disableTag 禁用标签

> `Fx.tag.disableTag(<string tag_group_id>, <string tag_group_api_name>, <string tag_id>, <string tag_api_name>)`

**参数说明**

入参格式

参数名称 | object | 描述 | 是否必填  
---|---|---|---  
tag_group_id | string |  | 是  
tag_group_api_name | string |  | 是  
tag_id | string |  | 是  
tag_api_name | string |  | 是  
  
**Groovy 举例**
    
    
    def result = Fx.tag.disableTag("tag_scDwW__c","group_ceshi11__c","62427820babe24000101d80d","6242784d06e1bf00015f33ec")
    
    

### # 11\. deleteTag 删除标签

> `Fx.tag.deleteTag(<String tag_group_id>, <String tag_group_api_name>, <String tag_id>, <String tag_api_name>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
tag_group_id | String | 标签分组id | 是  
tag_group_api_name | String | 标签分组apiName | 是  
tag_id | String | 标签id | 是  
tag_api_name | String | 标签apiName | 是  
  
**Groovy 举例**
    
    
    def result = Fx.tag.deleteTag("tag_scDwW__c","group_ceshi11__c","62427820babe24000101d80d","6242784d06e1bf00015f33ec")
    
    

### # 12\. findTagGroup 根据apiName查找标签分组及其适用对象

> `Fx.tag.findTagGroup(<String group_api_name>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
group_api_name | String | 标签分组ApiName | 是  
  
出参格式

参数名称 | 类型 | 描述  
---|---|---  
name | String | 分组名称  
apiNameList | List[string] | 适用对象范围  
isAppliedToAll | Boolean | 是否使用全部对象  
tagGroupId | String | 标签分组id  
  
出参样例
    
    
    {
        "name":"分组名称",
        "apiNameList":["AccountObj"],
        "isAppliedToAll":true,
        "tagGroupId":"5e981b91ee56e5446723dd1e"
    }
    
    

**Groovy 举例**
    
    
    def (String message,Map data ,Boolean error) = Fx.tag.findTagGroup("group_ceshi11__c")
    
    

### # 13\. findTagByTagIds 根据标签id批量查询标签描述

> `Fx.tag.findTagByTagIds(<array apiNames>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
apiNames | array[string] |  | 是  
  
出参格式

参数名称 | APIResult | 描述  
---|---|---  
isError | boolean | 是否错误  
data | object | 返回的数据  
message | string | 信息  
data | object | 返回的数据  
---|---|---  
tagList | array[object] | 返回的数据列表  
tagList | object | 标签描述  
---|---|---  
last_modified_time | number | 最后修改时间  
is_active | boolean | 是否启用  
create_time | number | 创建时间  
tag_group_id | string | 标签所属组  
name | string | 标签名称  
description | string | 标签描述  
tag_api_name | string | 标签apiName  
id | string | 标签id  
create_user | string | 创建用户  
  
出参样例
    
    
    {
        "isError": false,
        "data": {
            "tagList": [
                {
                    "last_modified_time": 1723431673765,
                    "is_active": true,
                    "create_time": 1588770951196,
                    "tag_group_id": "5ea3b0e5e1a70b0001e2f65b",
                    "name": "测试222222",
                    "description": "",
                    "tag_api_name": "label_ntys8__c",
                    "id": "5eb2b887d653e40001369112",
                    "create_user": "1000"
                },
                {
                    "last_modified_time": 1722323037015,
                    "is_active": false,
                    "create_time": 1606540721016,
                    "tag_group_id": "5fc1dd880680680001fc1900",
                    "name": "上海活动",
                    "description": "",
                    "tag_api_name": "tag_nyMWk__c",
                    "id": "5fc1ddb10680680001fc1906",
                    "create_user": "1000"
                }
            ]
        },
        "message": ""
    }
    
    

**Groovy 举例**
    
    
    List tagIds = ["5fc1dd990680680001fc1903"]
    def(Boolean error, Map data, String message) = Fx.tag.findTagByTagIds(tagIds)
    if (error) {
        log.info("error:" + message)
    }
    log.info(data)
    
    

## # 参考类 com.fxiaoke.functions.model.QueryResult

## # 参考类 com.fxiaoke.functions.model.TagArg

### # 字段说明

参数名称 | object | 描述  
---|---|---  
tagId | java.lang.String | 标签id  
tagApiName | java.lang.String | 标签apiName  
groupApiName | java.lang.String | 可选参数，  
groupId | java.lang.String | 标签组id  
description | java.lang.String | 描述  
tagName | java.lang.String | 标签名称  
  
[Fx.AI](../AIAPI/) [Fx.approval](../ApprovalAPI/)

← [Fx.AI](../AIAPI/) [Fx.approval](../ApprovalAPI/)→ 

  * 跟随系统 
  * 浅色模式 
  * 深色模式 
  * 阅读模式 


