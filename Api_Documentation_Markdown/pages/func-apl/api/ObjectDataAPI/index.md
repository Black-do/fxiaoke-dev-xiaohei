#  Fx.object

## # Fx.object

### # 1\. create 主从对象同时入库

> `Fx.object.create(<String apiName>, <Map objectData>, <Map details>, <CreateAttribute createAttribute>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
apiName | String | 对象ApiName | 是  
objectData | Map | 主对象数据即字段值 | 是  
details | Map | 从对象数据 | 是  
createAttribute | CreateAttribute | 创建属性设置 | 是  
  
出参格式

参数名称 | APIResult | 描述  
---|---|---  
error | Boolean | 是否错误  
data | Map | 返回的数据  
message | String | 信息  
  
出参样例
    
    
    {
      "isError" : false,
      "data" : {},
      "message" : "success"
    }
    
    

**Groovy 举例**
    
    
    Map masterData = [
            "name"          : "主从同时新建1",  //主属性是String类型
            "owner"         : ['1000'],       //人员字段是List类型
            //附件，人员字段是List，有filename，path，size，ext四个字段
            "field_4zWog__c": [
                    [
                            "filename": "新建选择业务类型.png",
                            "path"    : "N_202302_16_4acf04c3eb5046c08316e6e5da78ddfa",
                            "size"    : 80848,
                            "ext"     : "png"
                    ]
            ],
    
            "field_p1M7F__c": Date.now().toTimestamp(), //日期，时间和日期时间字段都是时间戳Long
            "field_6Lol2__c": Time.now().toTimestamp(),
            //各种特殊字段都需要做举例
    ]
    Map detailData = [
            "object_detail1__c": [["name": "张三1", "customFiled__c": "test1"], ["name": "李四1", "customField__c": "test2"]],
            "object_detail2__c": [["name": "张三2", "customFiled__c": "test1"], ["name": "李四2", "customField__c": "test2"]]
    ]
    
    def (Boolean error, Map data, String errorMessage) = Fx.object.create("object_1yO4J__c", masterData, detailData, CreateAttribute.builder().build())
    if (error) {
        // 注意：查重阻断也会走到此逻辑，重复的数据可从 data 中取出
        log.error("获取对象异常" + errorMessage)
        //1.使用报错终止执行
        //Fx.message.throwException("获取对象异常"+errorMessage)
        //2.使用return终止执行
        //return;
        //3.继续执行
    }
    //dosomething
    
    

**参考对象**

  * 参考CreateAttribute



**注意事项**

>   * 参数 Details 为空时，表示不创建从对象
> 


### # 2\. batchCreate 最多支持500行一批的批量创建数据

> `Fx.object.batchCreate(<String apiName>, <List objects>, <CreateAttribute attribute>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
apiName | String | 对象的api名称 | 是  
objects | List[object] | 对象数据即字段值 | 是  
attribute | CreateAttribute | 创建属性设置 | 是  
  
出参格式

参数名称 | APIResult | 描述  
---|---|---  
isError | Boolean | 是否错误  
data | List[Map] | 返回的数据  
message | String | 信息  
  
出参样例
    
    
    {
      "isError" : false,
      "data" : [
        {}
      ],
      "message" : ""
    }
    
    

**Groovy 举例**
    
    
    List dataList = [
            [
                    "name"          : "主属性",
                    "owner"         : ['1000'],
                    "field_p1M7F__c": Date.now().toTimestamp(),
                    "field_6Lol2__c": Time.now().toTimestamp(),
            ]
    ]
    
    def (Boolean error, List<Map> data, String errorMessage) = Fx.object.batchCreate("AccountObj", dataList, CreateAttribute.builder().build())
    if (error) {
    
        log.error("获取对象异常" + errorMessage)
    
        //1.使用报错终止执行
        //Fx.message.throwException("获取对象异常"+errorMessage)
    
    
        //2.使用return终止执行
        //return;
    
        //3.继续执行
    } else {
        data.each {
            e ->
                //dosomething，将示例逻辑细化至业务数据层
                def map = e as Map
                def id = map['_id']
                def name = map['name']
                log.info(name)
        }
    }
    
    

**参考对象**

  * 参考CreateAttribute



### # 3\. update IncrementUpdate更新数据对象

> `Fx.object.update(<String apiName>, <String objectId>, <Map updateFields>, <UpdateAttribute attribute>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
apiName | String | 对象的api名称 | 是  
objectId | String | 数据ID | 是  
updateFields | Map | 对象数据即字段值 | 是  
attribute | UpdateAttribute | 可选参数 | \--  
  
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
      "message" : "success"
    }
    
    

**Groovy 举例**
    
    
    String objectAPIName = 'object_s82CA__c'
    String dataId = '64b1113e87ec1c0001bfc102'
    Map updateData = [
            "name":"sss"
    ]
    def (Boolean error, Map data, String errorMessage) =  Fx.object.update(objectAPIName, dataId, updateData, UpdateAttribute.builder().triggerWorkflow(true).build())
    if (error) {
    
        log.error("获取对象异常" + errorMessage)
    
        // 1.使用报错终止执行
        // Fx.message.throwException("获取对象异常"+errorMessage)
        
        // 2.使用return终止执行
        // return;
    
        // 3.继续执行
    } else {
        // dosomething，将示例逻辑细化至业务数据层
        def map = data as Map
        def id = map['_id']
        def name = map['name']
        log.info(name)
    }
    
    

**参考对象**

  * 参考UpdateAttribute



**注意事项**

>   * 该更新不会校验数据的锁定状态
>   * 该更新不会触发编辑按钮的前验证后动作以及验证规则
>   * 不支持更新的字段
>   * owner 负责人
>   * mc_currency不能将币种、汇率更新为空
>   * mc_exchange_rate 不能将币种、汇率更新为空
>   * mc_exchange_rate_version 不能将币种、汇率更新为空
>   * mc_functional_currency不能将币种、汇率更新为空
>   * formula计算字段
>   * count统计字段
> 


### # 4\. update Edit主从《覆盖》更新，如果从对象给空则会清空从对象。

> `Fx.object.update(<String apiName>, <String objectId>, <Map updateFields>, <Map detailData>, <ActionAttribute actionAttribute>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
apiName | String | 对象的api名称 | 是  
objectId | String | 对象数据id | 是  
updateFields | Map | 对象数据即字段值 | 是  
detailData | Map | 从对象数据 | \--  
actionAttribute | ActionAttribute | 可选参数 | \--  
  
出参格式

参数名称 | APIResult | 描述  
---|---|---  
error | Boolean | 是否错误  
data | Map | 返回的数据  
message | String | 信息  
  
出参样例
    
    
    {
        "error": false,
        "data": {
            "objectData": {
                "name": "校验2",
                "_id": "6708dc09167d290001b33a6d",
                "tenant_id": "590064",
                "object_describe_api_name": "object_HKjsx__c",
                "field_bool_value_filled_label__c": true,
                "mc_exchange_rate": "1.000000",
                "mc_functional_currency": "CNY",
                "field_1UAV1__c": true,
                "last_modified_time": 1728650434133,
                "lock_status": "0",
                "package": "CRM",
                "relevant_team": [
                    {
                        "teamMemberEmployee": [
                            "1040"
                        ],
                        "teamMemberType": "0",
                        "teamMemberRole": "4",
                        "teamMemberPermissionType": "1",
                        "teamMemberDeptCascade": "0"
                    },
                    {
                        "teamMemberEmployee": [
                            "1041"
                        ],
                        "teamMemberType": "0",
                        "teamMemberRole": "4",
                        "teamMemberPermissionType": "1",
                        "teamMemberDeptCascade": "0"
                    },
                    {
                        "teamMemberEmployee": [
                            "308093721"
                        ],
                        "teamMemberType": "0",
                        "sourceType": "2",
                        "outTenantId": "200158833",
                        "teamMemberRole": "4",
                        "teamMemberPermissionType": "1",
                        "teamMemberDeptCascade": "0"
                    },
                    {
                        "teamMemberEmployee": [
                            "310588453"
                        ],
                        "teamMemberType": "0",
                        "sourceType": "2",
                        "outTenantId": "200158833",
                        "teamMemberRole": "4",
                        "teamMemberPermissionType": "1",
                        "teamMemberDeptCascade": "0"
                    },
                    {
                        "teamMemberEmployee": [
                            "1045"
                        ],
                        "teamMemberType": "0",
                        "teamMemberRole": "4",
                        "teamMemberPermissionType": "2",
                        "teamMemberDeptCascade": "0"
                    }
                ],
                "data_own_department": [
                    "1123"
                ]
            },
            "isDuplicate": false,
            "triggerApproval": false,
            "newObjectData": {
                "object_5d7H7__c": [
                    {
                        "name": "我是从对象11，我被函数更改了",
                        "tenant_id": "590064",
                        "object_describe_api_name": "object_5d7H7__c",
                        "order_by": 10,
                        "created_by": [
                            "-10000"
                        ],
                        "last_modified_by": [
                            "-10000"
                        ],
                        "create_time": 1728650522846,
                        "lock_status": "0",
                        "life_status": "normal",
                        "record_type": "default__c",
                        "data_own_department": [
                            "1123"
                        ],
                        "data_own_organization": [
                            "999999"
                        ],
                        "field_111zM__c": "6708dc09167d290001b33a6d",
                        "field_2GC4y__c": 1728650434133,
                        "field_Qm7t1__c": "0.00",
                        "mc_currency": "CNY",
                        "mc_exchange_rate": "1.000000",
                        "mc_exchange_rate_version": "1608693355946",
                        "mc_functional_currency": "CNY",
                        "_id": "67091d1a6d8f270001de7720",
                        "field_oz7a9__c": "fby-276-word",
                        "is_deleted": false,
                        "package": "CRM",
                        "field_hpnw1__c": "",
                        "last_modified_time": 1728650522846
                    }
                ],
                "object_1iV1z__c": [
                    {
                        "name": "我是从对象22，我被函数更改了",
                        "tenant_id": "590064",
                        "object_describe_api_name": "object_1iV1z__c",
                        "order_by": 10,
                        "created_by": [
                            "-10000"
                        ],
                        "last_modified_by": [
                            "-10000"
                        ],
                        "create_time": 1728650522910,
                        "lock_status": "0",
                        "life_status": "normal",
                        "record_type": "default__c",
                        "data_own_department": [
                            "1123"
                        ],
                        "data_own_organization": [
                            "999999"
                        ],
                        "field_59vM0__c": "6708dc09167d290001b33a6d",
                        "mc_currency": "CNY",
                        "mc_exchange_rate": "1.000000",
                        "mc_exchange_rate_version": "1608693355946",
                        "mc_functional_currency": "CNY",
                        "_id": "67091d1a6d8f270001de7721",
                        "is_deleted": false,
                        "package": "CRM",
                        "owner_department": "",
                        "field_05lsb__c": "",
                        "version": 1,
                        "last_modified_time": 1728650522910
                    }
                ]
            }
        },
        "message": "success"
    }
    
    

**Groovy 举例**
    
    
    String objectApiName = "object_qs2nb__c"
    String objectId = "607d5e3dd02b9f00016507d8"
    def objectMap = ["name":"校验"]
    def detailMap = [
                     "object1":[["name": "我是从对象1，我被函数更改了"]],
                     "object2":[["name": "我是从对象2，我被函数更改了"]]
                     ]
    
    def (Boolean error, Map data, String errorMessage) = Fx.object.update(objectApiName, objectId, objectMap, detailMap, ActionAttribute.create())
    if (error) {
        log.error("获取对象异常" + errorMessage)
        //1.使用报错终止执行
        //Fx.message.throwException("获取对象异常"+errorMessage)
        //2.使用return终止执行
        //return;
        //3.继续执行
    }
    //dosomething
    
    

**参考对象**

  * 参考ActionAttribute



**注意事项**

>   * 如不想更新从对象，则detailData参数给null，如果传空数组，则会清空从对象,该全量更新接口无法更新锁定的数据，如需更新，可以使用增量更新接口
> 


### # 5\. update 按照查询条件批量更新数据，该功能灰度中，请申请灰度后使用

> `Fx.object.update(<String apiName>, <QueryTemplate template>, <Map updateFields>, <UpdateAttribute attribute>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
apiName | String | 对象的api名称 | 是  
template | QueryTemplate | 查询条件，详见QueryTemplate说明 | \--  
updateFields | Map | 需要更新的字段，例如：["field__c": "test"] | 是  
attribute | UpdateAttribute | 本次更新的设置 | \--  
  
出参格式

参数名称 | APIResult | 描述  
---|---|---  
error | Boolean | 是否错误  
data | Map | 返回的数据  
message | String | 信息  
  
出参样例
    
    
    {
      "error" : false,
      "data" : {},
      "message" : "success"
    }
    
    

**Groovy 举例**
    
    
    String objectApiName = "object_1yO4J__c"
    QueryTemplate query = QueryTemplate.AND(
      ["name":QueryOperator.EQ("主从同时新建1")]
    )
    def (Boolean error, Object result,String errorMessage) =  Fx.object.update(objectApiName, query, ["field__c": "test"], UpdateAttribute.builder().build())
    if (error) {
        log.error("获取对象异常" + errorMessage)
        //1.使用报错终止执行
        //Fx.message.throwException("获取对象异常"+errorMessage)
        //2.使用return终止执行
        //return;
        //3.继续执行
    }
    //dosomething
    
    

**参考对象**

  * 参考QueryOperator

  * 参考UpdateAttribute




**注意事项**

>   * 默认上限更新1000条件数据，如果需要更新1000条以上数据，请设置isAllUpdate为true,此批量更新耗时较大，1000条数据大约3分钟,此接口更新默认调用到业务团队，以保证业务的完整性,如果需刷库，可以将runBusiness为false时，请谨慎使用
> 


### # 6\. duplicateSearch 获取查重结果

> `Fx.object.duplicateSearch(<String apiName>, <String type>, <Map data>, <String relatedApiName>, <Integer pageNumber>, <Integer pageSize>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
apiName | String | 对象apiName | \--  
type | String | 查重类型，其中新建、编辑时为'NEW'，查重工具时为'TOOL' | \--  
data | Map | 更新、新建数据 | \--  
relatedApiName | String | 有查找关联关系的对象apiName（注：查本对象时不用传） | \--  
pageNumber | Integer | 显示页数 | \--  
pageSize | Integer | 每页条数 | \--  
  
出参格式

参数名称 | APIResult | 描述  
---|---|---  
error | Boolean | 是否错误  
data | Map | 返回的数据  
message | String | 信息  
  
出参样例
    
    
    {
        "error": false,
        "data": {
            "dataList": [
                {
                    "tenant_id": "590064",
                    "data_own_organization": [
                        "1039"
                    ],
                    "mc_exchange_rate": "1.000000",
                    "is_deleted": false,
                    "field_619D3__c": "123",
                    "object_describe_api_name": "object_zPSCw__c",
                    "owner_department_id": "1123",
                    "owner_department": "第三方平台主属部门",
                    "relevant_team__r": "admin01",
                    "mc_functional_currency": "CNY",
                    "create_time": 1693993617349,
                    "life_status": "normal",
                    "last_modified_by": [
                        "1045"
                    ],
                    "mc_currency": "CNY",
                    "version": "2",
                    "created_by": [
                        "1045"
                    ],
                    "record_type": "default__c"
                }
            ],
            "matchType": "PRECISE",
            "keepSave": false
        },
        "message": "success"
    }
    
    

**Groovy 举例**
    
    
    Map objectData = ["object_describe_api_name":"object_zPSCw__c","field_619D3__c":"123"]
    def (Boolean error, Map data, String errorMessage) = Fx.object.duplicateSearch("object_zPSCw__c", "NEW", objectData, null, 1, 20)
    if (error) {
        log.error("获取对象异常" + errorMessage)
        //1.使用报错终止执行
        //Fx.message.throwException("获取对象异常"+errorMessage)
        //2.使用return终止执行
        //return;
        //3.继续执行
    }
    //dosomething
    
    

### # 7\. batchUpdate 批量更新某个字段的内容

> `Fx.object.batchUpdate(<String apiName>, <Map objects>, <List fields>, <BatchUpdateAttribute attribute>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
apiName | String | 对象的api名称 | 是  
objects | Map[Map] | 批量更新的数据信息 | 是  
fields | List[string] | 批量更新的字段列表 | 是  
attribute | BatchUpdateAttribute | 批量更新属性 | 是  
  
出参格式

参数名称 | APIResult | 描述  
---|---|---  
error | Boolean | 是否错误  
data | List | 返回的数据  
message | String | 信息  
  
出参样例
    
    
    {
        "error": false,
        "data": [
            {
                "tenant_id": "590064",
                "is_deleted": false,
                "object_describe_api_name": "object_6YgjB__c",
                "field_bVch6__c": "test1",
                "_id": "65aa17a9f318b90001726517",
                "last_modified_by": [
                    "-10000"
                ]
            },
            {
                "tenant_id": "590064",
                "is_deleted": false,
                "object_describe_api_name": "object_6YgjB__c",
                "field_bVch6__c": "test2",
                "_id": "630f109f10b94300018b593a",
                "last_modified_by": [
                    "-10000"
                ]
            }
        ],
        "message": "success"
    }
    
    

**Groovy 举例**
    
    
    //批量更新的数据
    Map batch = [ '60acc4a2d040a70001886739': [ 'field_bVch6__c': 'test1' ], '60acc482d040a70001886582': [ 'field_bVch6__c': 'test2' ] ]
    //指定更新的字段
    List fields = ['field_bVch6__c']
    
    def (Boolean error, List result,String errorMessage) = Fx.object.batchUpdate('object_8N0H2__c', batch, fields, BatchUpdateAttribute.builder().build())
    if (error) {
        log.error("获取对象异常" + errorMessage)
        //1.使用报错终止执行
        //Fx.message.throwException("获取对象异常"+errorMessage)
        //2.使用return终止执行
        //return;
        //3.继续执行
    }
    //dosomething
    
    

**参考对象**

  * 参考BatchUpdateAttribute



**注意事项**

>   * 自定义对象：
>   * 最多支持500条数据。
>   * 该接口属于底层接口，相当于直接更新数据库。默认会触发工作流。
>   * fields里面指定的字段必须在objects里存在，如不存在，则表示清空
>   * 该接口更新计算、统计、引用字段可能会与后台的计算服务发生并发覆盖的问题，导致计算结果错误，因此不要在fields中指定计算、统计、引用字段更新
>   * 使用场景：自定义对象批量更新对象自定义字段。
>   * **使用此接口刷数据时一定要充分验证后再上线。**
>   *   * 预制对象需要转单条操作（由于对象有较多业务逻辑处理）：
>   * 参考BatchUpdateAttribute convert2SingleOperation方法说明；
>   * 底层是循环调用上文中的《IncrementUpdate更新数据对象》方法；
>   * 数据量少的情况建议代码中直接循环调用update方法，可自主控制方法参数；
> 


### # 8\. directDelete 直接删除数据库数据，不可恢复，这是一个非常危险的操作，谨慎使用

> `Fx.object.directDelete(<String apiName>, <String dataId>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
apiName | String | 对象的apiname | 是  
dataId | String | 数据ID | 是  
  
出参格式

参数名称 | APIResult | 描述  
---|---|---  
error | Boolean | 是否错误  
message | String | 信息  
  
出参样例
    
    
    {
      "error" : false,
      "message" : "success"
    }
    
    

**Groovy 举例**
    
    
    def (Boolean error, Object result,String errorMessage) = Fx.object.directDelete("AccountObj","60057c76a3836900012xxxx")
    if (error) {
        log.error("获取对象异常" + errorMessage)
        //1.使用报错终止执行
        //Fx.message.throwException("获取对象异常"+errorMessage)
        //2.使用return终止执行
        //return;
        //3.继续执行
    }
    //dosomething
    
    

### # 9\. batchDelete 批量删除数据

> `Fx.object.batchDelete(<String apiName>, <List objectIds>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
apiName | String | 对象的apiname | 是  
objectIds | List[string] | 数据ID列表 | 是  
  
出参格式

参数名称 | APIResult | 描述  
---|---|---  
error | Boolean | 是否错误  
data | Object | 返回null  
message | String | 信息  
  
出参样例
    
    
    {
      "error" : false,
      "message" : "success!"
    }
    
    

**Groovy 举例**
    
    
    def (Boolean error, Map data, String errorMessage) = Fx.object.batchDelete("object_HKjsx__c",["6708dc09167d290001b33a6d"])
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

>   * 该接口不区分对象是否作废，直接批量彻底删除
> 


### # 10\. find FQL查询

> `Fx.object.find(<String apiName>, <FQLAttribute fqlAttribute>, <SelectAttribute selectAttribute>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
apiName | String | 对象ApiName | 是  
fqlAttribute | FQLAttribute | 查询条件，详细说明参考FQLAttribute对象 | 是  
selectAttribute | SelectAttribute | 查询属性，非必填，详细说明参考SelectAttribute | \--  
  
出参格式

参数名称 | APIResult | 描述  
---|---|---  
error | Boolean | 是否错误  
data | QueryResult | 返回的数据  
message | String | 信息  
data | QueryResult | 返回的数据  
---|---|---  
size | Integer | 本次返回的数据条数  
total | Integer | 符合条件的数据总条数  
dataList | List | 对象数据列表  
  
出参样例
    
    
    {
        "error" : false,
        "data" : {
            "size" : 1,
            "total" : 2,
            "dataList" : [
                {
                    "_id" : "6177cde7a0cb410001930ad0",
                    "name" : "account1"
                }
            ]
        },
        "message" : ""
    }
    
    

**Groovy 举例**
    
    
    def (Boolean error, QueryResult queryResult, String errorMessage) = Fx.object.find("AccountObj", //对象apiName
            FQLAttribute.builder()
                    .columns(["_id", "name"]) //需要返回的字段
                    .queryTemplate(QueryTemplate.AND(["_id": QueryOperator.EQ("6177cde7a0cb410001930ad0")])) //查询条件
                    .build(),
           SelectAttribute.builder()
                    .needCalculate(true) //是否实时处理计算字段，默认true
                    .needQuote(true) //是否实时处理引用字段，默认true
                    .calculateCount(true) //是否实时处理统计字段，默认true
                    .fillExtendInfo(false) //是否补充字段扩展信息，比如查找关联字段的主属性、人员部门名称等，以${字段apiName}__r返回，默认false
                    .needOptionLabel(false) //是否返回单选、多选字段的label，以${字段apiName}__r返回，默认false
                    .convertQuoteForView(false) //引用字段是否返回label，如果为true，引用字段的value通过${字段apiName}__v返回，默认false
                    .needInvalid(false) //是否返回已作废的数据，默认false
                    .needRelevantTeam(false) //是否返回相关团队，默认false
                    .build())
    if (error) {
        log.error("获取对象异常" + errorMessage)
    
        //1.使用报错终止执行
        //Fx.message.throwException("获取对象异常"+errorMessage)
    
        //2.使用return终止执行
        //return;
    
        //3.继续执行
    } else {
        def dataList = queryResult.dataList as List //数据列表
        def total = queryResult.total //符合条件的数据总条数
        def size = queryResult.size  //本次返回的数据条数
        dataList.each {
            e ->
                //dosomething，将示例逻辑细化至业务数据层
                def map = e as Map
                def id = map['_id']
                def name = map['name']
                log.info(name)
        }
    }
    
    

**参考对象**

  * 参考SelectAttribute

  * 参考QueryOperator

  * 参考FQLAttribute




### # 11\. findOne FQL查询单条数据，推荐使用该方式进行数据查询

> `Fx.object.findOne(<String apiName>, <FQLAttribute fqlAttribute>, <SelectAttribute selectAttribute>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
apiName | String | 对象ApiName | 是  
fqlAttribute | FQLAttribute | 查询条件，详细说明参考FQLAttribute对象 | 是  
selectAttribute | SelectAttribute | 查询属性，非必填，详细说明参考SelectAttribute | \--  
  
出参格式

参数名称 | APIResult | 描述  
---|---|---  
error | Boolean | 是否错误  
data | Map | 返回的数据  
message | String | 信息  
  
出参样例
    
    
    {
        "error": false,
        "data": {
            "_id": "6177cde7a0cb410001930ad0",
            "name": "account1"
        },
        "message": ""
    }
    
    

**Groovy 举例**
    
    
    def (Boolean error, Map data, String errorMessage) = Fx.object.findOne("AccountObj", //对象apiName
            FQLAttribute.builder()
                    .columns(["_id", "name"]) //需要返回的字段
                    .queryTemplate(QueryTemplate.AND(["_id": QueryOperator.NE("6177cde7a0cb410001930ad0")])) //查询条件
                    .build(),
           SelectAttribute.builder()
                    .needCalculate(true) //是否实时处理计算字段，默认true
                    .needQuote(true) //是否实时处理引用字段，默认true
                    .calculateCount(true) //是否实时处理统计字段，默认true
                    .fillExtendInfo(false) //是否补充字段扩展信息，比如查找关联字段的主属性、人员部门名称等，以${字段apiName}__r返回，默认false
                    .needOptionLabel(false) //是否返回单选、多选字段的label，以${字段apiName}__r返回，默认false
                    .convertQuoteForView(false) //引用字段是否返回label，如果为true，引用字段的value通过${字段apiName}__v返回，默认false
                    .needInvalid(false) //是否返回已作废的数据，默认false
                    .needRelevantTeam(false) //是否返回相关团队，默认false
                    .build())
    if (error) {
        log.error("获取对象异常" + errorMessage)
    
        //1.使用报错终止执行
        //Fx.message.throwException("获取对象异常"+errorMessage)
    
        //2.使用return终止执行
        //return;
    
        //3.继续执行
    } else {
            //dosomething，将示例逻辑细化至业务数据层
            def map = data as Map
            def id = map['_id']
            def name = map['name']
            log.info(name)
    }
    
    

**参考对象**

  * 参考SelectAttribute

  * 参考QueryOperator

  * 参考FQLAttribute




### # 12\. findById FQL查询单条数据Id

> `Fx.object.findById(<String apiName>, <String id>, <FQLAttribute fqlAttribute>, <SelectAttribute selectAttribute>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
apiName | String | 对象ApiName | 是  
id | String | 数据id | 是  
fqlAttribute | FQLAttribute | 查询条件，详细说明参考FQLAttribute对象 | 是  
selectAttribute | SelectAttribute | 查询属性，非必填，详细说明参考SelectAttribute | 是  
  
出参格式

参数名称 | APIResult | 描述  
---|---|---  
error | Boolean | 是否错误  
data | Map | 返回的数据  
message | String | 信息  
  
出参样例
    
    
    {
        "error": false,
        "data": {
            "_id": "6177cde7a0cb410001930ad0",
            "name": "account1"
        },
        "message": ""
    }
    
    

**Groovy 举例**
    
    
    def (Boolean error,Map data,String errorMessage) = Fx.object.findById("AccountObj", //对象apiName
                 "6177cde7a0cb410001930ad0", //数据id
                 FQLAttribute.builder()
                    .columns(["_id","name"]) //需要返回的字段
                    .build(),
                 SelectAttribute.builder()
                    .needCalculate(true) //是否实时处理计算字段，默认true
                    .needQuote(true) //是否实时处理引用字段，默认true
                    .calculateCount(true) //是否实时处理统计字段，默认true
                    .fillExtendInfo(false) //是否补充字段扩展信息，比如查找关联字段的主属性、人员部门名称等，以${字段apiName}__r返回，默认false
                    .needOptionLabel(false) //是否返回单选、多选字段的label，以${字段apiName}__r返回，默认false
                    .convertQuoteForView(false) //引用字段是否返回label，如果为true，引用字段的value通过${字段apiName}__v返回，默认false
                    .needInvalid(false) //是否返回已作废的数据，默认false
                    .needRelevantTeam(false) //是否返回相关团队，默认false
                    .build())
    if(error) {
        log.error("find data failed:"+errorMessage)
        //1.使用报错终止执行
        //Fx.message.throwException("获取对象异常"+errorMessage)
        //2.使用return终止执行
        //return;
        //3.继续执行
    } else {
        Map map = data as Map
        String name = map["name"] as String
        log.info("name="+name)
    }
    
    

**参考对象**

  * 参考SelectAttribute

  * 参考FQLAttribute




### # 13\. findByIds FQL查询数据id匹配的数据集

> `Fx.object.findByIds(<String apiName>, <List ids>, <FQLAttribute fqlAttribute>, <SelectAttribute selectAttribute>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
apiName | String | 对象ApiName | 是  
ids | List | 数据id列表 | 是  
fqlAttribute | FQLAttribute | 查询条件，详细说明参考FQLAttribute对象 | 是  
selectAttribute | SelectAttribute | 查询属性，非必填，详细说明参考SelectAttribute | 是  
  
出参格式

参数名称 | APIResult | 描述  
---|---|---  
error | Boolean | 是否错误  
data | List | 返回的数据  
message | String | 信息  
  
出参样例
    
    
    {
        "error": false,
        "data": [
            {
                "_id": "6177cde7a0cb410001930ad0",
                "name": "account1"
            }
        ],
        "message": ""
    }
    
    

**Groovy 举例**
    
    
    def (Boolean error,List data,String errorMessage) = Fx.object.findByIds("AccountObj", //对象apiName
                 ["6177cde7a0cb410001930ad0"], //数据id列表
                 FQLAttribute.builder()
                    .columns(["_id","name"]) //需要返回的字段
                    .build(),
                 SelectAttribute.builder()
                    .needCalculate(true) //是否实时处理计算字段，默认true
                    .needQuote(true) //是否实时处理引用字段，默认true
                    .calculateCount(true) //是否实时处理统计字段，默认true
                    .fillExtendInfo(false) //是否补充字段扩展信息，比如查找关联字段的主属性、人员部门名称等，以${字段apiName}__r返回，默认false
                    .needOptionLabel(false) //是否返回单选、多选字段的label，以${字段apiName}__r返回，默认false
                    .convertQuoteForView(false) //引用字段是否返回label，如果为true，引用字段的value通过${字段apiName}__v返回，默认false
                    .needInvalid(false) //是否返回已作废的数据，默认false
                    .needRelevantTeam(false) //是否返回相关团队，默认false
                    .build())
    if(error) {
        log.error("find data failed:"+errorMessage)
        //1.使用报错终止执行
        //Fx.message.throwException("获取对象异常"+errorMessage)
        //2.使用return终止执行
        //return;
        //3.继续执行
    } else {
        (data as List).each{item->
            Map map = item as Map
            String name = map["name"] as String
            log.info("name="+name)
        }
    }
    
    

**参考对象**

  * 参考SelectAttribute

  * 参考QueryOperator

  * 参考FQLAttribute




### # 14\. select 通过SQL语句查询数据，可以设置是否从db查询，是否查询总数，是否查相关团队等参数

> `Fx.object.select(<String sql>, <SelectAttribute selectAttribute>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
sql | String | 需要查询的sql语句 | 是  
selectAttribute | SelectAttribute | 查询属性，非必填，详细说明参考SelectAttribute | 是  
  
出参格式

参数名称 | APIResult | 描述  
---|---|---  
error | Boolean | 是否错误  
message | String | 信息  
  
出参样例
    
    
    {
        "error": false,
        "message": "success!"
    }
    
    

**Groovy 举例**
    
    
    //fql语法详见API Reference/入门/FQL说明
    //普通用法
    String sql = "select _id, field_rzv5M__c, name from object_227xW__c where field_rzv5M__c>100 limit 10 offset 0;"
    def rst = Fx.object.select(sql).result() as QueryResult
    log.info(rst)
    
    //如果需要查询不包含作废数据、返回满足条件的数据总数
    String sql1 = "select _id, field_rzv5M__c, name from object_227xW__c where field_rzv5M__c>100 limit 10 offset 0;"
    SelectAttribute att = SelectAttribute.builder()
      .needInvalid(false)
      .build()
    def rst1 = Fx.object.select(sql1, att).result() as QueryResult
    log.info(rst1)
    
    

**参考对象**

  * 参考SelectAttribute



**注意事项**

>   * 该方法有聚合查询结果以及查询数据两种格式的结果；
>   * 对应返回体，1.数据查询(QueryResult) 2.聚合查询(List)
> 


### # 15\. select 使用SQL查询大量数据，并做好了分页处理(适用于查全量数据，不支持order by limit操作)

> `Fx.object.select(<String sql>, <SelectAttribute selectAttribute>, <Closure consumer>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
sql | String | 需要查询的sql语句 | 是  
selectAttribute | SelectAttribute | 查询属性，非必填，详细说明参考SelectAttribute | 是  
consumer | Closure | 闭包接口，用于处理一批数据 | 是  
  
出参格式

参数名称 | APIResult | 描述  
---|---|---  
error | Boolean | 是否错误  
message | String | 信息  
  
出参样例
    
    
    {
        "error": false,
        "message": "success!"
    }
    
    

**Groovy 举例**
    
    
    //fql语法详见API Reference/入门/FQL说明
    def objectName = 'object_227xW__c' //对象apiName
    def searchValue = 100 //查询条件
    def sql = "select _id, field_rzv5M__c, name from ${objectName} where field_rzv5M__c>${searchValue}" //需要执行的sql
    Fx.object.select(sql, SelectAttribute.builder().build(), { list->
        list.each{item->
            Map map = item as Map
            String field_rzv5M__c = map["field_rzv5M__c"] as String
            log.info("field_rzv5M__c="+field_rzv5M__c)
        }
    }).result();
    
    

**参考对象**

  * 参考SelectAttribute



**注意事项**

>   * 该函数适用于查符合条件的全量数据的场景,该函数不支持order by操作，不支持limit操作
> 


### # 16\. findWithRelated 该函数可以通过查找关联或主从关系，查询相关数据，并且一起返回

> `Fx.object.findWithRelated(<String apiName>, <String relatedField>, <List criteria>, <Map orderBy>, <Integer limit>, <Integer skip>, <ActionAttribute attribute>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
apiName | String | 相关对象或从对象ApiName | 是  
relatedField | String | 查找关联或主从字段的ApiName | 是  
criteria | List | 查询条件 | 是  
orderBy | Map | 排序字段 | 是  
limit | Integer | 返回的数据条数限制 | 是  
skip | Integer | 分页查询的起始点位 | 是  
attribute | ActionAttribute | 可选属性 | \--  
  
出参格式

参数名称 | APIResult | 描述  
---|---|---  
error | Boolean | 是否错误  
data | List | 返回的数据  
message | String | 信息  
  
出参样例
    
    
    {
        "error": false,
        "data": [
            {
                "object_0uyAd__c": {
                    "_id": "60868215965b1900014c0d35",
                    "name": "相关对象数据"
                },
                "master_object__c": {
                    "_id": "78787865676787868uuyds",
                    "name": "主对象数据"
                }
            }
        ],
        "message": ""
    }
    
    

**Groovy 举例**
    
    
    def attribute = ActionAttribute.build {
        forceQueryFromDB = false
     }
    def (Boolean error, QueryResult queryResult, String errorMessage) = Fx.object.findWithRelated(
            "object_0uyAd__c", //相关对象或从对象的ApiName 
            "field_YjJ6d__c", //查找关联字段或主从关系字段
            [["_id":"60868215965b1900014c0d35"]], //查询条件
            ["create_time":1],  //排序字段，1-正序；0-倒序
            10, //返回的数据条数限制
            0, //分页查询的起始点位
            attribute //可选属性，比如forceQueryFromDB=true表示强制从数据库中查询
    )
    if (error) {
        log.error("获取对象异常" + errorMessage)
    
        //1.使用报错终止执行
        //Fx.message.throwException("获取对象异常"+errorMessage)
    
        //2.使用return终止执行
        //return;
    
        //3.继续执行
    } else {
        QueryResult result = queryResult as QueryResult
        List dataMapList = result.data as List
        dataMapList.each {
            e->
                Map dataMap = e as Map
                Map relateData = dataMap["object_0uyAd__c"] as Map //相关对象数据
                Map masterData = dataMap["master_object__c"] as Map //主对象数据
                //dosomething
        }
    }
    
    

**参考对象**

  * 参考ActionAttribute



**注意事项**

>   * 使用该函数做关联对象查询时，ApiName给的是相关对象的ApiName，并且relatedField是查找关联字段，使用该函数做主从查询时，ApiName给的是从对象的ApiName，并且relatedField是主从关系对字段。
> 


### # 17\. remove 作废数据，将数据放入回收站

> `Fx.object.remove(<String apiName>, <String id>)`

**参数说明**

入参格式

参数名称 | object | 描述 | 是否必填  
---|---|---|---  
apiName | String | 对象apiName | 是  
id | String | 数据id | 是  
  
**Groovy 举例**
    
    
    def rst = Fx.object.remove("AccountObj","ed47841898054749a2ec9be9e6e5d728").result() as Map
    
    

### # 18\. batchRemove 批量作废业务数据，将数据放入回收站

> `Fx.object.batchRemove(<String apiName>, <List objectIds>, <RemoveAttribute attribute>)`

**参数说明**

入参格式

参数名称 | object | 描述 | 是否必填  
---|---|---|---  
apiName | String | 对象APIName | 是  
objectIds | List[String] | 数据Id列表 | 是  
attribute | RemoveAttribute | 可选参数 | 是  
  
出参格式

参数名称 | APIResult | 参数列表  
---|---|---  
error | boolean | 是否执行异常  
data | Email | 返回结果  
errorMessage | String | 异常提示信息  
  
出参样例
    
    
    {
      "error": false,
      "data": {},
      "errorMessage": ""
    }
    
    

**Groovy 举例**
    
    
    // 对象APIName
    String objApi = "object_kFc8w__c"
    // 数据Id列表
    List < String > dataIdList = ["664dd6c2f7239000076e133f"]
    // 可选属性
    RemoveAttribute attr = RemoveAttribute
      .builder()
      .triggerApprovalFlow(false)
      .triggerWorkflow(false)
      .skipFunctionAction(true)
      .useCurrentIdentity(false)
      .skipButtonConditions(true)
      .build()
    
    def(error, data, errorMessage) = Fx.object.batchRemove(objApi, dataIdList, attr)
    
    if (error) {
      log.info(errorMessage)
    } else {
      log.info(data)
    }
    
    

**参考对象**

  * 参考RemoveAttribute



**注意事项**

>   * 只有生命状态为正常的数据才能被作废
> 


### # 19\. editTeamMember 覆盖编辑对象团队成员

> `Fx.object.editTeamMember(<string apiName>, <string dataId>, <List teamMembers>, <boolean ignoreSendingRemind>)`

**参数说明**

入参格式

参数名称 | object | 描述 | 是否必填  
---|---|---|---  
apiName | string | 对象apiName | 是  
dataId | string | 数据id | 是  
teamMembers | List[object] |  | 是  
ignoreSendingRemind | boolean | 可选参数，是否不发送提醒，true为不发送，不填时为发送 | \--  
teamMembers | object | 描述 | 是否必填  
---|---|---|---  
userId | string | 团队成员id | \--  
permission | integer | 读写权限:1代表只读,2代表读写 | \--  
role | integer | 相关团队角色:4代表普通成员,1代表负责人 | \--  
type | integer | 相关团队成员类型:0代表人员，1代表用户组，2代表部门，4代表角色，5代表下游企业，6代表下游企业组 | \--  
  
**Groovy 举例**
    
    
    def result = Fx.object.editTeamMember("AccountObj","36fd270a986842529445bf3d252cca9b",[["userId":"1058","role":4,"permission":1],["userId":"1057","role":3,"permission":2]]).result() as Map
    
    

**注意事项**

>   * 只能修改内部相关团队
> 


### # 20\. replaceOutTeamMember 全量替换所有外部成员

> `Fx.object.replaceOutTeamMember(<string apiName>, <string objectId>, <object outTeamMembers>, <boolean ignoreSendingRemind>)`

**参数说明**

入参格式

参数名称 | object | 描述 | 是否必填  
---|---|---|---  
apiName | string | 对象apiName | 是  
objectId | string | 数据id | 是  
outTeamMembers | object[object] |  | \--  
ignoreSendingRemind | boolean | 可选参数，是否不发送提醒，true为不发送，不填时为发送 | \--  
outTeamMembers | object | 外部成员信息，如何创建可参考示例 | 是否必填  
---|---|---|---  
memberType | object | 相关团队成员类型:0代表人员，1代表用户组，2代表部门，4代表角色，5代表下游企业，6代表下游企业组 | \--  
permission | object | 读写权限:1代表只读,2代表读写 | \--  
teamMemberList | List[object] |  | \--  
teamMemberList | object | 描述 | 是否必填  
---|---|---|---  
userId | string | 外部人员id | 是  
outTenantId | string | 外部企业id | 是  
  
**Groovy 举例**
    
    
    def teamMemberEmployee = TeamMemberEmployee.builder()
             .userId("309175511")
             .outTenantId("301185430")
             .build()
    
    OutTeamMemberAttribute outEmployTeamMember = OutTeamMemberAttribute.createEmployMember([teamMemberEmployee], TeamMemberEnum.Permission.READANDWRITE)
    
    def result=Fx.object.replaceOutTeamMember("object_qep6N__c","61848edfd9007e00019ee222", [outEmployTeamMember])
    
    

**参考对象**

  * 参考OutTeamMemberAttribute



**注意事项**

>   * 替换外部相关团队成员信息，不可替换外部负责人
> 


### # 21\. addTeamMember 添加内部团队成员

> `Fx.object.addTeamMember(<string apiName>, <string objectId>, <object teamMemberAttribute>)`

**参数说明**

入参格式

参数名称 | object | 描述 | 是否必填  
---|---|---|---  
apiName | string | 对象apiName | 是  
objectId | string | 数据id | 是  
teamMemberAttribute | object[object] |  | 是  
teamMemberAttribute | object | 内部成员信息，如何创建可参考示例 | 是否必填  
---|---|---|---  
memberType | object | 相关团队成员类型:0代表人员，1代表用户组，2代表部门，4代表角色，5代表下游企业，6代表下游企业组 | \--  
permission | object | 读写权限:1代表只读,2代表读写 | \--  
role | object | 相关团队角色:4代表普通成员,1代表负责人 | \--  
teamMembers | List[string] |  | \--  
ignoreSendingRemind | boolean | 可选参数，是否不发送提醒，true为不发送，不填时为发送 | \--  
teamMembers | string | 描述 | 是否必填  
---|---|---|---  
userId | string | 人员id | 是  
  
**Groovy 举例**
    
    
    // 添加人员
    def employTeamMember = TeamMemberAttribute.createEmployMember(["1027"],
                                         TeamMemberEnum.Role.NORMAL_STAFF,
                                         TeamMemberEnum.Permission.READONLY)
    Fx.object.addTeamMember("object_qep6N__c","61848edfd9007e00019ee222", employTeamMember).result()
    
    // 添加用户组
    def groupTeamMember = TeamMemberAttribute.createGroupMember(["6152bd0de3e51c0001ec4de3"],
                                        TeamMemberEnum.Role.NORMAL_STAFF,
                                        TeamMemberEnum.Permission.READONLY)
    Fx.object.addTeamMember("object_qep6N__c","61848edfd9007e00019ee222", groupTeamMember).result()
    
    // 添加部门
    def deptTeamMember = TeamMemberAttribute.createDepartmentMember(["1008"],
                                            TeamMemberEnum.Role.NORMAL_STAFF,
                                            TeamMemberEnum.Permission.READONLY)
    Fx.object.addTeamMember("object_qep6N__c","61848edfd9007e00019ee222", deptTeamMember).result()
    
    // 添加角色
    def roleTeamMember = TeamMemberAttribute.createRoleMember(["00000000000000000000000000000009"],
                                            TeamMemberEnum.Role.NORMAL_STAFF,
                                            TeamMemberEnum.Permission.READONLY)
    Fx.object.addTeamMember("object_qep6N__c","61848edfd9007e00019ee222", roleTeamMember).result()
    
    

**参考对象**

  * 参考TeamMemberAttribute



**注意事项**

>   * 不能添加负责人；如果添加的成员包括负责人，则不会修改负责人数据；如果添加的成员在原系统中有重复的则更新该成员
> 


### # 22\. addOutTeamMember 添加外部团队成员

> `Fx.object.addOutTeamMember(<string apiName>, <string objectId>, <object outTeamMemberAttribute>)`

**参数说明**

入参格式

参数名称 | object | 描述 | 是否必填  
---|---|---|---  
apiName | string | 对象apiName | 是  
objectId | string | 数据id | 是  
outTeamMemberAttribute | object[object] |  | 是  
outTeamMemberAttribute | object | 外部成员信息，如何创建可参考示例 | 是否必填  
---|---|---|---  
memberType | object | 相关团队成员类型:0代表人员，1代表用户组，2代表部门，4代表角色，5代表下游企业，6代表下游企业组 | \--  
permission | object | 读写权限:1代表只读,2代表读写 | \--  
outTeamMembers | List[object] |  | \--  
ignoreSendingRemind | boolean | 可选参数，是否不发送提醒，true为不发送，不填时为发送 | \--  
outTeamMembers | object | 描述 | 是否必填  
---|---|---|---  
userId | string | 下游企业人员id | 是  
outTenantId | string | 下游企业id | 是  
  
**Groovy 举例**
    
    
    // 添加外部人员
    def teamMemberEmployee = TeamMemberEmployee.builder()
         .userId("309175511")
         .outTenantId("301185430")
         .build()
    def outEmployTeamMember = OutTeamMemberAttribute.createEmployMember([teamMemberEmployee], TeamMemberEnum.Permission.READANDWRITE)
    Fx.object.addOutTeamMember("object_qep6N__c","61848edfd9007e00019ee222", outEmployTeamMember).result()
    
    // 添加下游企业
    def outTenant = TeamMemberEmployee.builder()
         .userId("300012805")
         .outTenantId("300012805")
         .build()
    def outTenantTeamMember = OutTeamMemberAttribute.createOutTenantMember([outTenant], TeamMemberEnum.Permission.READANDWRITE)
    Fx.object.addOutTeamMember("object_qep6N__c","61848edfd9007e00019ee222", outTenantTeamMember).result()
    
    // 添加外部角色
    def outRoleTeamMember = OutTeamMemberAttribute.createRoleMember(["5d1f28eee4b0896efc933508"], TeamMemberEnum.Permission.READANDWRITE)
    Fx.object.addOutTeamMember("object_qep6N__c","61848edfd9007e00019ee222", outRoleTeamMember).result()
    
    // 添加下游企业组
    def outTenantGroupTeamMember = OutTeamMemberAttribute.createOutTenantGroupMember(["613880213ed24b000150a713"], TeamMemberEnum.Permission.READANDWRITE)
    Fx.object.addOutTeamMember("object_qep6N__c","61848edfd9007e00019ee222", outTenantGroupTeamMember).result()
    
    

**参考对象**

  * 参考OutTeamMemberAttribute



### # 23\. deleteTeamMember 删除相关团队

> `Fx.object.deleteTeamMember(<string apiName>, <List objectIds>, <List teamMembers>, <List outTeamMemberEmployee>, <string ignoreSendingRemind>)`

**参数说明**

入参格式

参数名称 | object | 描述 | 是否必填  
---|---|---|---  
apiName | string | 对象apiName | 是  
objectIds | List | 数据id集合 | 是  
teamMembers | List | 删除的人员id集合 | 是  
outTeamMemberEmployee | List[object] | 删除的外部人员集合 | 是  
ignoreSendingRemind | string | 可选参数，是否不发送提醒，true为不发送，不填时为发送 | \--  
outTeamMemberEmployee | object | 描述 | 是否必填  
---|---|---|---  
userId | string | 下游企业人员id | 是  
outTenantId | string | 下游企业id | 是  
  
**Groovy 举例**
    
    
    Fx.object.deleteTeamMember("object_qep6N__c",["61848edfd9007e00019ee222"],[],[["userId":"300012805","outTenantId":""]]).result()
    
    

### # 24\. getTeamMember 获取团队成员

> `Fx.object.getTeamMember(<string apiName>, <string dataID>)`

**参数说明**

入参格式

参数名称 | string | 描述 | 是否必填  
---|---|---|---  
apiName | string | 对象apiName | 是  
dataID | string | 数据id | 是  
  
出参格式

参数名称 | object | 描述  
---|---|---  
teamMemberInfos | array[object] |   
teamMemberInfos | object | 描述  
---|---|---  
deptCascaded | boolean | 部门是否级联  
innerDepartmentMember | boolean | 是否是内部部门  
innerEmployeeMember | boolean | 是否是内部成员  
outTeamMember | boolean | 是否是外部成员  
teamMemberEmployee | List | 内部成员id  
teamMemberRole | string | 角色  
teamMemberRoleList | List | 角色集合  
teamMemberPermissionType | string | 成员权限  
outTenantId | string | 下游企业id  
sourceType | string | 是否是外部成员  
teamMemberType | string | 相关团队成员类型  
teamMemberName | string | 团队成员名字  
teamMemberDeptCascade | string | 是否级联上级部门  
teamMemberRoleNames | string | 角色名称  
  
**Groovy 举例**
    
    
    def rst = Fx.object.getTeamMember("AccountObj","83cf73d957924284a96e9c44ebb333ec").result() as List
    log.info(rst)
    
    

### # 25\. changeOwner 更换数据的负责人

> `Fx.object.changeOwner(<String apiName>, <String dataId>, <String ownerId>, <ActionAttribute attribute>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
apiName | String | 对象的apiName | 是  
dataId | String | 数据ID | 是  
ownerId | String | 负责人ID | 是  
attribute | ActionAttribute | 本次操作的属性设置 | \--  
attribute | ActionAttribute | 本次操作的属性设置 | 是否必填  
---|---|---|---  
triggerApprovalFlow | Boolean | 是否触发审批流，默认为true | \--  
triggerWorkflow | Boolean | 是否触发工作流，默认为true | \--  
skipFunctionAction | Boolean | 是否跳过前后动作函数，默认为false不跳过 | \--  
  
**Groovy 举例**
    
    
    Fx.object.changeOwner("AccountObj","ed47841898054749a2ec9be9e6e5d728","1001").result()
    
    

### # 26\. batchChangeOwner 批量更换负责人

> `Fx.object.batchChangeOwner(<String apiName>, <List changeData>, <ActionAttribute attribute>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
apiName | String | 对象的api名称 | 是  
changeData | List[object] | 要变更的负责人的数据ID和用户ID | 是  
attribute | ActionAttribute | 本次操作的属性设置 | \--  
changeData | object | 描述 | 是否必填  
---|---|---|---  
dataId | String | 数据ID | 是  
userId | String | 用户ID | 是  
attribute | ActionAttribute | 本次操作的属性设置 | 是否必填  
---|---|---|---  
triggerApprovalFlow | Boolean | 是否触发审批流，默认为true | \--  
triggerWorkflow | Boolean | 是否触发工作流，默认为true | \--  
skipFunctionAction | Boolean | 是否跳过前后动作函数，默认为false不跳过 | \--  
  
**Groovy 举例**
    
    
    Map changeData1 = [
      "objectId":"5f86b47b1bdac00001f2c300",
      "ownerId":["-10000"]
    ]
    Map changeData2 = [
      "objectId":"5f86b4a71bdac00001f2d232",
      "ownerId":["-10000"]
    ]
    List arg = [changeData1,changeData2]
    Fx.object.batchChangeOwner("object_i66LR__c", arg, ActionAttribute.create()).result()
    
    

**参考对象**

  * 参考ActionAttribute



### # 27\. getOptionName 获取单选/多选业务名称/选项名称

> `Fx.object.getOptionName(<String objectAPIName>, <String filedAPIName>, <String value>)`

**参数说明**

入参格式

参数名称 | object | 描述 | 是否必填  
---|---|---|---  
objectAPIName | String | 对象APIName | 是  
filedAPIName | String | 字段APIName | 是  
value | String | 单选/多选的值 | 是  
  
出参格式

参数名称 | APIResult | 参数列表  
---|---|---  
error | boolean | 是否执行异常  
data | Email | 返回结果  
errorMessage | String | 异常提示信息  
  
出参样例
    
    
    {
      "error": false,
      "data": {},
      "errorMessage": ""
    }
    
    

**Groovy 举例**
    
    
    // 对象APIName
    String objApi = "object_kFc8w__c"
    // 字段APIName
    String fieldApi = "mc_currency"
    // 选项值
    String value = "CNY"
    
    def(error, data, errorMessage) = Fx.object.getOptionName(objApi, fieldApi, value)
    
    if (error) {
      log.info(errorMessage)
    } else {
      log.info(data)
    }
    
    

### # 28\. copyByRule 根据映射规则创建数据

> `Fx.object.copyByRule(<String sourceApiName>, <String sourceId>, <String ruleApiName>, <Map masterPlus>, <Map detailPlus>)`

**参数说明**

入参格式

参数名称 | object | 描述 | 是否必填  
---|---|---|---  
sourceApiName | String | 被映射的对象Api Name | 是  
sourceId | String | 被映射的对象实例的ID | 是  
ruleApiName | String | 映射规则API Name | 是  
masterPlus | Map | 可选参数，主对象数据参数 | \--  
detailPlus | Map | 可选参数，从对象数据参数 | \--  
  
出参格式

参数名称 | APIResult | 描述  
---|---|---  
error | Boolean | 是否错误  
data | Map | 返回的数据  
message | String | 信息  
  
出参样例
    
    
    {
        "error": false,
        "data": {
            "objectData": {
                "name": "测试流程编辑委屈委屈",
                "object_describe_api_name": "object_dwdtj__c",
                "created_by": [
                    "-10000"
                ],
                "owner": [
                    "-10000"
                ],
                "object_describe_id": "5cef84d3ec347f0001503b07",
                "is_deleted": false,
                "field_7wjo1__c": "测试流程编辑委屈委屈",
                "tenant_id": "590064",
                "_id": "671109f6dfad5d0001e0d659",
                "last_modified_by": [
                    "-10000"
                ],
                "create_time": 1729169910220,
                "lock_status": "0",
                "life_status": "normal",
                "record_type": "default__c",
                "mc_currency": "CNY",
                "relevant_team": [],
                "data_own_department": [
                    "999999"
                ],
                "data_own_organization": [
                    "999999"
                ],
                "field_wbYI0__c": "函数填充11",
                "version": 1,
                "last_modified_time": 1729169910220
            },
            "details": {
                "object_snpWU__c": [
                    {
                        "name": "测试主从修改记录",
                        "record_type": "default__c",
                        "object_describe_api_name": "object_snpWU__c",
                        "life_status": "ineffective",
                        "created_by": [
                            "-10000"
                        ],
                        "owner": [
                            "-10000"
                        ],
                        "object_describe_id": "5cef868578d46b00018a8468",
                        "is_deleted": false,
                        "field_c62Tz__c": "",
                        "field_a72ov__c": "data1填充内容",
                        "tenant_id": "590064",
                        "order_by": 10,
                        "field_A5k2e__c": "671109f6dfad5d0001e0d659",
                        "_id": "671109f6dfad5d0001e0d65a",
                        "last_modified_by": [
                            "-10000"
                        ],
                        "create_time": 1729169910323,
                        "lock_status": "0",
                        "data_own_department": [
                            "999999"
                        ],
                        "data_own_organization": [
                            "999999"
                        ],
                        "package": "CRM",
                        "life_status_before_invalid": "",
                        "owner_department": "",
                        "field_kEy24__c": "",
                        "field_c7F38__c": "",
                        "version": 1,
                        "last_modified_time": 1729169910323,
                        "field_kql81__c": "",
                        "field_kql81__c__r": ""
                    }
                ]
            },
            "success": true
        },
        "message": "success"
    }
    
    

**Groovy 举例**
    
    
    Map masterPlus = ["field_wbYI0__c": "函数填充11"]
    List detailFillValueList = [["field_a72ov__c": "data1填充内容"]]
    Map detailPlus = ["object_snpWU__c": detailFillValueList]
    def (Boolean error, Object result, String errorMessage) =  Fx.object.copyByRule('object_pbx98__c', '66d827e45c1ac90001ede05c', 'map_y5iy4__c', masterPlus, detailPlus)
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

>   * 使用本方法创建的数据，可以触发审批流以及工作流
> 


### # 29\. lock 对数据进行锁定操作

> `Fx.object.lock(<String apiName>, <String dataId>, <Boolean cascadeDetail>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
apiName | String | 对象的apiname | 是  
dataId | String | 数据ID | 是  
cascadeDetail | Boolean | 是否锁定从对象 | 是  
  
出参格式

参数名称 | APIResult | 描述  
---|---|---  
error | Boolean | 是否错误  
message | String | 信息  
  
出参样例
    
    
    {
      "error" : false,
      "message" : "success"
    }
    
    

**Groovy 举例**
    
    
    def (Boolean error, Object result,String errorMessage) = Fx.object.lock('AccountObj','e6a338ae8a944cdfb2bae737db1aa12f', true)
    if (error) {
        log.error("获取对象异常" + errorMessage)
        //1.使用报错终止执行
        //Fx.message.throwException("获取对象异常"+errorMessage)
        //2.使用return终止执行
        //return;
        //3.继续执行
    }
    //dosomething
    
    

### # 30\. unlock 对数据进行解锁操作

> `Fx.object.unlock(<String apiName>, <String dataId>, <Boolean cascadeDetail>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
apiName | String | 对象的apiname | 是  
dataId | String | 数据ID | 是  
cascadeDetail | Boolean | 是否解锁从对象 | 是  
  
出参格式

参数名称 | APIResult | 描述  
---|---|---  
error | Boolean | 是否错误  
message | String | 信息  
  
出参样例
    
    
    {
      "error" : false,
      "message" : "success"
    }
    
    

**Groovy 举例**
    
    
    def (Boolean error, Object result,String errorMessage) = Fx.object.unlock('AccountObj','e6a338ae8a944cdfb2bae737db1aa12f', true)
    if (error) {
        log.error("获取对象异常" + errorMessage)
        //1.使用报错终止执行
        //Fx.message.throwException("获取对象异常"+errorMessage)
        //2.使用return终止执行
        //return;
        //3.继续执行
    }
    //dosomething
    
    

### # 31\. batchLock 对数据进行批量的锁定

> `Fx.object.batchLock(<String apiName>, <List objectIds>, <Boolean cascadeDetail>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
apiName | String | 对象的apiname | 是  
objectIds | List[string] | 数据id集合 | 是  
cascadeDetail | Boolean | 是否解锁从对象 | 是  
  
出参格式

参数名称 | APIResult | 描述  
---|---|---  
error | Boolean | 是否错误  
message | String | 信息  
  
出参样例
    
    
    {
      "error" : false,
      "message" : "success"
    }
    
    

**Groovy 举例**
    
    
    def (Boolean error, Object result,String errorMessage) = Fx.object.batchLock('AccountObj',['e6a338ae8a944cdfb2bae737db1aa12f'], true)
    if (error) {
        log.error("获取对象异常" + errorMessage)
        //1.使用报错终止执行
        //Fx.message.throwException("获取对象异常"+errorMessage)
        //2.使用return终止执行
        //return;
        //3.继续执行
    }
    //dosomething
    
    

### # 32\. batchUnlock 对数据进行批量的解锁

> `Fx.object.batchUnlock(<String apiName>, <List objectIds>, <Boolean cascadeDetail>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
apiName | String | 对象的apiname | 是  
objectIds | List[string] | 数据id集合 | 是  
cascadeDetail | Boolean | 是否解锁从对象 | 是  
  
出参格式

参数名称 | APIResult | 描述  
---|---|---  
error | Boolean | 是否错误  
message | String | 信息  
  
出参样例
    
    
    {
      "error" : false,
      "message" : "success"
    }
    
    

**Groovy 举例**
    
    
    def (Boolean error, Object result,String errorMessage) = Fx.object.batchUnlock('AccountObj',['e6a338ae8a944cdfb2bae737db1aa12f'], true)
    if (error) {
        log.error("获取对象异常" + errorMessage)
        //1.使用报错终止执行
        //Fx.message.throwException("获取对象异常"+errorMessage)
        //2.使用return终止执行
        //return;
        //3.继续执行
    }
    //dosomething
    
    

### # 33\. merge 对象合并(只支持客户和线索对象)

> `Fx.object.merge()`

**Groovy 举例**
    
    
    String apiName = "LeadsObj"
    String targetDataId = "61b9aed9a3c69e0001351a87"
    List sourceDataIds = ["61b9af07a3c69e000135213f"]
    Map objectData = [
                 "name": "测试合并10",
                 "mobile": "18840934501",
                 "tel": "18840934501",
                 "url": "www.ceshi44.com",
                 "remark": "测试销售线索1",
                 "source": "2",
                 "marketing_event_id": "618a2e8b869433000198ef41",
                 "leads_pool_id": "2876c6af7815475893bea6092bbffd02",
                 "record_type": "default__c",
                 "close_reason": "",
                 "back_reason": "",
                 "data_own_department": [
                 "1001"
             ],
             "mc_exchange_rate": "1.000000",
             "is_duplicated": false,
             "data_own_organization": [
                 "999999"
             ],
             "leads_stage_changed_time": 1636873294913,
             ]
    Fx.object.merge(apiName, targetDataId, sourceDataIds, objectData).result()
    
    

**负责人：陈金典Kimd**

### # 34\. aggregate 对某一字段进行聚合，聚合函数默认会从ES进行聚合，如果对数据一致性有所要求，建议从DB进行聚合（forceQueryFromDB=true）

> `Fx.object.aggregate(<String apiName>, <Aggregate type>, <List criteria>, <String groupByField>, <FindAttribute attribute>)`

**参数说明**

入参格式

参数名称 | object | 描述 | 是否必填  
---|---|---|---  
apiName | String | 对象的api名称 | 是  
type | Aggregate | 计算类型； Aggregate.SUM(String fieldApiName) 求和 Aggregate.COUNT() 计算数量 Aggregate.MAX(StringfieldApiName) 最大值 Aggregate.MIN(String fieldApiName) 最小值 Aggregate.AVG(String fieldApiName)平均值 | 是  
criteria | List | 查询条件（和find查询条件使用一样） | 是  
groupByField | String | 聚合条件 | 是  
attribute | FindAttribute | 聚合的属性设置,详见 FindAttribute | 是  
  
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
    
    
    def (Boolean error, List data,String errorMessage) = Fx.object.aggregate("object_227xW__c", Aggregate.MAX("field_rzv5M__c"), [["field_rzv5M__c":Operator.GT(10)]], 'field_qC2yp__c') //最大值
    
    if (error) {
        log.error("获取对象异常" + errorMessage)
        //1.使用报错终止执行
        //Fx.message.throwException("获取对象异常"+errorMessage)
        //2.使用return终止执行
        //return;
        //3.继续执行
    }
    //dosomething
    
    

**参考对象**

  * 参考FindAttribute



### # 35\. aggregate 按照条件进行聚合函数，聚合函数默认会从ES进行聚合，如果对数据一致性有所要求，建议从DB进行聚合（forceQueryFromDB=true）

> `Fx.object.aggregate(<String apiName>, <Aggregate type>, <Integer decimalScale>, <List criteria>, <FindAttribute attribute>)`

**参数说明**

入参格式

参数名称 | object | 描述 | 是否必填  
---|---|---|---  
apiName | String | 对象的api名称 | 是  
type | Aggregate | 计算类型； Aggregate.SUM(String fieldApiName) 求和 Aggregate.COUNT() 计算数量 Aggregate.MAX(StringfieldApiName) 最大值 Aggregate.MIN(String fieldApiName) 最小值 Aggregate.AVG(String fieldApiName)平均值 | 是  
decimalScale | Integer | 对象的api名称 | 是  
criteria | List | 查询条件（和find查询条件使用一样） | 是  
attribute | FindAttribute | 聚合的属性设置,详见 FindAttribute | 是  
  
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
    
    
    def (Boolean error, Object result, String errorMessage) = Fx.object.aggregate("object_m4S5S__c", Aggregate.AVG("field_k2y2d__c"), 2, [["field_Oo1K2__c":Operator.GT("200")]], FindAttribute.getDefaultFindAttribute())
    
    if (error) {
        log.error("获取对象异常" + errorMessage)
        //1.使用报错终止执行
        //Fx.message.throwException("获取对象异常"+errorMessage)
        //2.使用return终止执行
        //return;
        //3.继续执行
    }
    //dosomething
    
    

**参考对象**

  * 参考FindAttribute



### # 36\. findDescribe 查询对象描述信息，例如字段、单选信息等

> `Fx.object.findDescribe()`

**Groovy 举例**
    
    
    def rst = Fx.object.findDescribe('object_qep6N__c').result() as Map
    log.info(data)
    
    

**参考对象**

  * 参考null



### # 37\. getOptionInfo 查询单选、多选、业务类型对应的value

> `Fx.object.getOptionInfo(<String apiName>, <String fieldAPIName>)`

**参数说明**

入参格式

参数名称 | object | 描述 | 是否必填  
---|---|---|---  
apiName | String | 对象的apiname | 是  
fieldAPIName | String | 对象的字段apiname，可以是单选、多选、或者业务类型 | 是  
  
出参格式

参数名称 | APIResult | 描述  
---|---|---  
isError | boolean | 是否错误  
data | Map | 返回的数据,选中的key和value会互换生成两个键值对加入map中，例如单选的值为01：有限责任公司，则返回两个键值对“有限责任公司”:“01”,“01”:”有限责任公司“,  
message | String | 信息  
  
出参样例
    
    
    {
        "isError": false,
        "data": {
            "10": "普通合伙",
            "个体工商户": "06"
        },
        "message": ""
    }
    
    

**Groovy 举例**
    
    
    def rst = Fx.object.getOptionInfo("EnterpriseInfoObj","enterprise_type");
    log.info( Fx.json.toJson(rst))
    
    

### # 38\. bulkDelete 批量将回收站数据（状态是已作废）的数据进行删除，该操作无法恢复数据，请谨慎使用

> `Fx.object.bulkDelete(<string apiName>, <List objectIds>)`

**参数说明**

入参格式

参数名称 | object | 描述 | 是否必填  
---|---|---|---  
apiName | string | 对象的apiname | 是  
objectIds | List[string] | 数据IDList | 是  
  
出参格式

参数名称 | APIResult | 描述  
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
    
    
    def rst = Fx.object.bulkDelete("object_c6584__c", ["6707d19a8b6d28000716bb05"]);
    log.info( Fx.json.toJson(rst))
    
    

**注意事项**

>   * 批量操作建议一次不要超过20条
> 


### # 39\. bulkRecover 恢复已作废的数据

> `Fx.object.bulkRecover(<string apiName>, <List objectIds>)`

**参数说明**

入参格式

参数名称 | object | 描述 | 是否必填  
---|---|---|---  
apiName | string | 对象的apiname | 是  
objectIds | List[string] | 数据IDList | 是  
  
出参格式

参数名称 | APIResult | 描述  
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
    
    
    def rst = Fx.object.bulkRecover("object_c6584__c", ["6707d19a8b6d28000716bb05"]);
    log.info( Fx.json.toJson(rst))
    
    

**注意事项**

>   * 批量操作建议一次不要超过20条
> 


### # 40\. delete 将回收站数据（状态是已作废）的数据进行删除，该操作无法恢复数据，请谨慎使用

> `Fx.object.delete(<String apiName>, <String objectId>)`

**参数说明**

入参格式

参数名称 | object | 描述 | 是否必填  
---|---|---|---  
apiName | String | 对象的apiname | 是  
objectId | String | 数据ID | 是  
  
出参格式

参数名称 | APIResult | 描述  
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
    
    
    def rst = Fx.object.delete("object_c6584__c", "643e44dc770bf20001d2622b");
    log.info(rst)
    
    

### # 41\. getMappingRule 查询映射信息描述

> `Fx.object.getMappingRule(<String mappingRuleApiName>)`

**参数说明**

入参格式

参数名称 | object | 描述 | 是否必填  
---|---|---|---  
mappingRuleApiName | String | 映射规则API名称 | 是  
  
出参格式

参数名称 | object | 描述  
---|---|---  
isError | boolean | 是否错误  
data | List | 返回的数据  
message | String | 信息  
data | List | 返回的数据  
---|---|---  
ruleList | array[object] |   
ruleList | object | 描述  
---|---|---  
sourceApiName | String | 来源对象ApiName  
targetApiName | String | 目标对象ApiName  
ruleName | String | 映射规则名称  
fieldMapping | List[object] | 字段规则名称  
fieldMapping | object | 描述  
---|---|---  
sourceFieldApiName | String | 来源字段ApiName  
targetFieldApiName | String | 目标字段ApiName  
  
出参样例
    
    
    {
        "isError": false,
        "data": {
            "ruleList": [
                {
                    "sourceApiName": "EnterpriseInfoObj",
                    "targetApiName": "MarketingEventObj",
                    "ruleName": "测试-12121221",
                    "fieldMapping": [
                        {
                            "sourceFieldApiName": "field_SaCBW__c",
                            "targetFieldApiName": "field_rA1ck__c"
                        }
                    ]
                }
            ]
        },
        "message": ""
    }
    
    

**Groovy 举例**
    
    
    def rst = Fx.object.getMappingRule("map_ri5oc__c").result() as Map;
    log.info(rst)
    
    

### # 42\. getCascadeOption 获取单选级联关系配置

> `Fx.object.getCascadeOption(<String apiName>, <String fieldApiName>, <String optionValue>)`

**参数说明**

入参格式

参数名称 | object | 描述 | 是否必填  
---|---|---|---  
apiName | String | 对象ApiName | 是  
fieldApiName | String | 父单选字段apiName | 是  
optionValue | String | 可选参数，父单选选项值 | 是  
  
出参格式

参数名称 | object | 描述  
---|---|---  
isError | boolean | 是否错误  
data | Map | 单选级联关系配置  
message | string |   
  
出参样例
    
    
    {
        "isError": false,
        "data": {
            "a83f96e093f3496d87ce878d2e2fa4f9": {
                "industry_level2": [
                    "b7bbfdcfe9a5452c882c4a270be94139",
                    "0b2a26a653ab436bb9894e381ba118b2",
                    "63d646c2d75c4ce39b76f79fb59c11db"
                ]
            }
        },
        "message": ""
    }
    
    

**Groovy 举例**
    
    
    def optionAttribute = OptionAttribute.builder()
         .apiName("object_qep6N__c")
         .fieldApiName("field_16Yl4__c")
         .optionValue("C3mG8ou09")
    .build()
    
    def rst = Fx.object.getCascadeOption(optionAttribute).result() as Map
    log.info(rst)OptionAttribute optionAttribute = OptionAttribute.builder()
         .apiName("object_qep6N__c")
         .fieldApiName("field_16Yl4__c")
         .optionValue("C3mG8ou09")
    .build();
    
    Map rst = Fx.object.getCascadeOption(optionAttribute).result();
    log.info(rst);
    
    

**参考对象**

  * 参考OptionAttribute



## # 参考类 com.fxiaoke.functions.tools.FindAttribute

### # 字段说明

参数名称 | object | 描述  
---|---|---  
returnRelatedValue | java.lang.Boolean | 是否返回相关数据id对应的value值（默认false）  
extendFieldApiNames | java.util.List[String] | 需要补充__r的字段apiName  
forceQueryFromDB | java.lang.Boolean | 是否从DB查询数据（默认false）  
  
## # 参考类 com.fxiaoke.functions.tools.RemoveAttribute

### # 字段说明

参数名称 | object | 描述  
---|---|---  
triggerWorkflow | java.lang.Boolean | 是否触发工作流 ,默认触发  
useCurrentIdentity | java.lang.Boolean | 是否使用当前用户身份查询数据（默认falses使用系统）  
skipFunctionAction | java.lang.Boolean | 是否跳过前后动作函数，目前不分前后动作  
skipButtonConditions | java.lang.Boolean | 跳过按钮显示条件校验  
triggerApprovalFlow | java.lang.Boolean | 是否触发审批流, 默认触发  
  
## # 参考类 com.facishare.paas.appframework.core.predef.service.dto.objectDescribe.FindDescribe

### # 字段说明

字段样例
    
    
    {
        "describeApiName": "xxx_api_name",
        "includeDetails": true,
        "sourceInfo":"xxx_sourceInfo"
    }
    
    

## # 参考类 com.fxiaoke.functions.tools.BatchUpdateAttribute

### # 字段说明

参数名称 | object | 描述  
---|---|---  
triggerWorkflow | boolean | 是否触发工作流, 默认触发  
convert2SingleOperation | boolean | 预制对象存在特殊业务逻辑不支持批量更新，可以通设置参数convert2SingleOperation为true，转为循环单条更新来处理（速度会比较慢）；默认false，不转为单条更新；仅预制对象可转为单条更新  
  
## # 参考类 com.fxiaoke.functions.tools.TeamMemberAttribute

### # 字段说明

参数名称 | object | 团队成员属性  
---|---|---  
  
### # 1\. createEmployMember 添加内部成员

> `TeamMemberAttribute.createEmployMember()`

**Groovy 举例**
    
    
    def employTeamMember = TeamMemberAttribute.createEmployMember(["1027"], TeamMemberEnum.Role.NORMAL_STAFF, TeamMemberEnum.Permission.READONLY)
    //employTeamMember.setIgnoreSendingRemind(true) // 可选参数，是否忽略发送CRM提醒。默认false
    //employTeamMember.setRealtime(true) // 可选参数，是否实时生效。默认false
    def employTeamResult = Fx.object.addTeamMember("object_qep6N__c","61848edfd9007e00019ee222", employTeamMember)
    log.info(employTeamResult)
    
    

**负责人：斯作益seth**

### # 2\. createGroupMember 添加用户组成员

> `TeamMemberAttribute.createGroupMember()`

**Groovy 举例**
    
    
    def employTeamMember = TeamMemberAttribute.createEmployMember(["1027"], TeamMemberEnum.Role.NORMAL_STAFF, TeamMemberEnum.Permission.READONLY)
    //employTeamMember.setIgnoreSendingRemind(true) // 可选参数，是否忽略发送CRM提醒。默认false
    //employTeamMember.setRealtime(true) // 可选参数，是否实时生效。默认false
    def employTeamResult = Fx.object.addTeamMember("object_qep6N__c","61848edfd9007e00019ee222", employTeamMember)
    log.info(employTeamResult)
    
    

**负责人：斯作益seth**

### # 3\. createDepartmentMember 添加部门成员

> `TeamMemberAttribute.createDepartmentMember()`

**Groovy 举例**
    
    
    def deptTeamMember = TeamMemberAttribute.createDepartmentMember(["1008"], TeamMemberEnum.Role.NORMAL_STAFF, TeamMemberEnum.Permission.READONLY)
    //deptTeamMember.setIgnoreSendingRemind(true) // 可选参数，是否忽略发送CRM提醒。默认false
    //deptTeamMember.setRealtime(true) // 可选参数，是否实时生效。默认false
    def deptTeamResult = Fx.object.addTeamMember("object_qep6N__c","61848edfd9007e00019ee222", deptTeamMember)
    log.info(deptTeamResult)
    
    

**负责人：斯作益seth**

### # 4\. createRoleMember 添加角色成员

> `TeamMemberAttribute.createRoleMember()`

**Groovy 举例**
    
    
    def roleTeamMember = TeamMemberAttribute.createRoleMember(["00000000000000000000000000000009"], TeamMemberEnum.Role.NORMAL_STAFF, TeamMemberEnum.Permission.READONLY)
    //roleTeamMember.setIgnoreSendingRemind(true) // 可选参数，是否忽略发送CRM提醒。默认false
    //roleTeamMember.setRealtime(true) // 可选参数，是否实时生效。默认false
    def roleTeamResult = Fx.object.addTeamMember("object_qep6N__c","61848edfd9007e00019ee222", roleTeamMember)
    log.info(roleTeamResult)
    
    

**负责人：斯作益seth**

## # 参考类 com.fxiaoke.functions.tools.ActionAttribute

### # 字段说明

参数名称 | object | 描述  
---|---|---  
fillOutOwner | boolean | 是否填充外部负责人，默认为false  
designatedCreatedBy | boolean | 是否指定创建人（包含所有从对象都是指定创建人），默认是系统，可以在参数objectData中指定的 `key: created_by (List<String>)` ，传入人员的id可以设置创建人  
specifyTime | boolean | 指定创建时间，仅创建接口使用，默认为false  
skipAfterFunction | boolean | 在create、update控制是否跳过后动作函数，默认为false  
triggerWorkflow | boolean | 是否触发工作流 ,默认触发  
duplicateSearch | boolean | 是否查重，默认为true  
modifiedBySelf | boolean | 是否指定当前用户为修改人，仅更新接口使用；默认为false代表系统更新，更新人是系统；设置为true代表当前用户更新，更新人是当前用户；可能存在数据权限不足更新失败的情况；不是所有场景都可以获取到当前用户，此时也会默认系统  
skipFunctionAction | boolean | 在create、update只控制是否跳过前验证函数，其他的如bulkRemove、changeOwner、batchChangeOwner同时控制跳过前后函数。  
skipImmutableFieldValidate | boolean | 是否跳过不可变字段验证，默认false；主要应用于上游数据同步到下游时，下游是否可对锁定字段编辑；  
forceQueryFromDB | boolean | 是否强制从数据库中查询，默认为false  
triggerApprovalFlow | boolean | 是否触发审批流, 默认触发  
  
### # 1\. create 快速构造方式，所有属性都是默认值

> `ActionAttribute.create()`

**参数说明**

出参格式

参数名称 | 类型 | 描述  
---|---|---  
actionAttribute | com.fxiaoke.functions.tools.ActionAttribute |   
  
**Groovy 举例**
    
    
    ActionAttribute attribute = ActionAttribute.create()
    
    

**负责人：斯作益seth**

### # 2\. build 构建器构造属性，在闭包中进行属性赋值

> `ActionAttribute.build(<groovy.lang.Closure closure>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
closure | groovy.lang.Closure |  | 是  
  
出参格式

参数名称 | 类型 | 描述  
---|---|---  
actionAttribute | com.fxiaoke.functions.tools.ActionAttribute |   
  
**Groovy 举例**
    
    
    ActionAttribute.build {
          forceQueryFromDB = false
    }
    
    

**负责人：斯作益seth**

## # 参考类 com.fxiaoke.functions.tools.OutTeamMemberAttribute

### # 字段说明

参数名称 | object | 外部团队成员属性  
---|---|---  
  
### # 1\. createEmployMember 添加外部成员

> `OutTeamMemberAttribute.createEmployMember(<List teamMemberList>, <Permission permission>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
teamMemberList | List[object] | 添加外部人员列表 | 是  
permission | Permission | TeamMemberEnum.Permission.READONLY //只读TeamMemberEnum.Permission.READANDWRITE //读写 TeamMemberEnum.Permission.NO_PERMISSION //无权限 | 是  
  
出参格式

参数名称 | 类型 | 描述  
---|---|---  
outTeamMemberAttribute | OutTeamMemberAttribute |   
  
**Groovy 举例**
    
    
    def teamMemberEmployee = TeamMemberEmployee.builder()
             .userId("309175511")
             .outTenantId("301185430")
             .build()
    OutTeamMemberAttribute outEmployTeamMember = OutTeamMemberAttribute.createEmployMember([teamMemberEmployee], TeamMemberEnum.Permission.READANDWRITE)
    def outEmployTeamResult = Fx.object.addOutTeamMember("object_qep6N__c","61848edfd9007e00019ee222", outEmployTeamMember)
    log.info(outEmployTeamResult)
    
    

**负责人：斯作益seth**

### # 2\. createOutTenantMember 添加下游企业

> `OutTeamMemberAttribute.createOutTenantMember()`

**Groovy 举例**
    
    
    def outTenant = TeamMemberEmployee.builder()
    .userId("300012805")
    .outTenantId("300012805")
    .build()
    OutTeamMemberAttribute outTenantTeamMember = OutTeamMemberAttribute.createOutTenantMember([outTenant], TeamMemberEnum.Permission.READANDWRITE)
    def outTenantTeamResult = Fx.object.addOutTeamMember("object_qep6N__c","61848edfd9007e00019ee222", outTenantTeamMember)
    log.info(outTenantTeamResult)
    
    

**负责人：斯作益seth**

### # 3\. createRoleMember 添加外部角色

> `OutTeamMemberAttribute.createRoleMember()`

**Groovy 举例**
    
    
    OutTeamMemberAttribute outRoleTeamMember = OutTeamMemberAttribute.createRoleMember(["5d1f28eee4b0896efc933508"], TeamMemberEnum.Permission.READANDWRITE)
    def outRoleTeamResult = Fx.object.addOutTeamMember("object_qep6N__c","61848edfd9007e00019ee222", outRoleTeamMember)
    log.info(outRoleTeamResult)
    
    

**负责人：斯作益seth**

### # 4\. createOutTenantGroupMember 添加下游企业组

> `OutTeamMemberAttribute.createOutTenantGroupMember()`

**Groovy 举例**
    
    
    OutTeamMemberAttribute outTenantGroupTeamMember = OutTeamMemberAttribute.createOutTenantGroupMember(["613880213ed24b000150a713"], TeamMemberEnum.Permission.READANDWRITE)
    def outTenantGroupResult = Fx.object.addOutTeamMember("object_qep6N__c","61848edfd9007e00019ee222", outTenantGroupTeamMember)
    log.info(outTenantGroupResult)
    
    

**负责人：斯作益seth**

## # 参考类 com.fxiaoke.functions.tools.QueryOperator

### # 字段说明

参数名称 | object |   
---|---|---  
  
### # 1\. EQ 查询与条件相等的数据

> `QueryOperator.EQ()`

**Groovy 举例**
    
    
    List criteria = [["name": Operator.EQ("测试")]]
    
    

**负责人：斯作益seth**

### # 2\. NE 查询与条件不相等的数据

> `QueryOperator.NE()`

**Groovy 举例**
    
    
    List criteria = [["name": Operator.NE("测试")]]
    
    

**负责人：斯作益seth**

### # 3\. GT 查询比条件大的数据

> `QueryOperator.GT()`

**Groovy 举例**
    
    
    List criteria = [["create_time": Operator.GT(1645427372658)]]
    
    

**负责人：斯作益seth**

### # 4\. LT 查询比条件小的数据

> `QueryOperator.LT()`

**Groovy 举例**
    
    
    List criteria = [["create_time": Operator.LT(1645427372658)]]
    
    

**负责人：斯作益seth**

### # 5\. GTE 查询大于等于条件的数据

> `QueryOperator.GTE()`

**Groovy 举例**
    
    
    List criteria = [["create_time": Operator.GTE(1645427372658)]]
    
    

**负责人：斯作益seth**

### # 6\. LTE 查询小于等于条件的数据

> `QueryOperator.LTE()`

**Groovy 举例**
    
    
    List criteria = [["create_time": Operator.LTE(1645427372658)]]
    
    

**负责人：斯作益seth**

### # 7\. LIKE 模糊匹配字符串内容

> `QueryOperator.LIKE()`

**Groovy 举例**
    
    
    List criteria = [["name": Operator.LIKE("易动纷享")]]
    
    

**负责人：斯作益seth**

### # 8\. NLIKE 除模糊匹配字符串内容

> `QueryOperator.NLIKE()`

**Groovy 举例**
    
    
    List criteria = [["name": Operator.NLIKE("易动纷享")]]
    
    

**负责人：斯作益seth**

### # 9\. IN 查询有交集的数据

如数据是[1,2,3]，查询条件是[1,4] 则返回（因为有1） 如数据是[1,2,3]，查询条件是[4,5] 则不返回

> `QueryOperator.IN()`

**Groovy 举例**
    
    
    List criteria = [["name": Operator.IN(["易动", "纷享"])]]
    
    

**负责人：斯作益seth**

### # 10\. NIN 查询无交集的数据

> `QueryOperator.NIN()`

**Groovy 举例**
    
    
    List criteria = [["name": Operator.NIN(["易动", "纷享"])]]
    
    

**负责人：斯作益seth**

### # 11\. CONTAINS 查询数据的数组字段匹配输入条件的子集

如数据是[1,2,3],查询条件是[1,2] 则返回 如数据是[1,2,3],查询条件是[3,4] 则不返回

> `QueryOperator.CONTAINS()`

**Groovy 举例**
    
    
    List criteria = [["name": Operator.CONTAINS(["易动", "纷享"])]]
    
    

**负责人：斯作益seth**

### # 12\. NCONTAINS 查询数据的数组字段匹配输入条件的子集之外的数据

如数据是[1,2,3],查询条件是[1,2] 则不返回 如数据是[1,2,3],查询条件是[3,4] 则返回

> `QueryOperator.NCONTAINS()`

**Groovy 举例**
    
    
    List criteria = [["name": Operator.NCONTAINS(["易动", "纷享"])]]
    
    

**负责人：斯作益seth**

### # 13\. HASANYOF 查询任何匹配数组任一内容的数据

> `QueryOperator.HASANYOF()`

**Groovy 举例**
    
    
    List criteria = [["name": Operator.HASANYOF(["易动", "纷享"])]]
    
    

**负责人：斯作益seth**

### # 14\. NHASANYOF 查询都不在数组内的数据

> `QueryOperator.NHASANYOF()`

**Groovy 举例**
    
    
    List criteria = [["name": Operator.NHASANYOF(["易动", "纷享"])]]
    
    

**负责人：斯作益seth**

### # 15\. EXISTS 查询数据字段（是/否）存在内容的数据

> `QueryOperator.EXISTS()`

**Groovy 举例**
    
    
    List criteria = [["name": Operator.EXISTS(true)]]
    
    

**负责人：斯作益seth**

### # 16\. STARTWITH 查询以...为开始的数据

> `QueryOperator.STARTWITH()`

**Groovy 举例**
    
    
    List criteria = [["name": Operator.STARTWITH("易动")]]
    
    

**负责人：斯作益seth**

### # 17\. ENDWITH 查询以...为结束的数据

> `QueryOperator.ENDWITH()`

**Groovy 举例**
    
    
    List criteria = [["name": Operator.ENDWITH("易动")]]
    
    

**负责人：斯作益seth**

### # 18\. BETWEEN 查询在...范围内的数据

> `QueryOperator.BETWEEN()`

**Groovy 举例**
    
    
    List criteria = [["name": Operator.BETWEEN([154542372658, 1645427372658])]]
    
    

**负责人：斯作益seth**

## # 参考类 com.fxiaoke.functions.model.FQLAttribute

### # 字段说明

参数名称 | object | 描述  
---|---|---  
queryTemplate | com.fxiaoke.functions.model.QueryTemplate | WHERE [查询条件]，详见QueryTemplate说明  
columns | java.util.List[java.lang.String] | SELECT [字段]  
limit | java.lang.Integer | LIMIT [查询数量] 默认10，上限100  
orderBy | java.util.Map | ORDER BY [排序字段] 例如 ["_id":1] 1升序 -1降序  
skip | java.lang.Integer | SKIP [翻页条目]  
  
## # 参考类 com.fxiaoke.functions.tools.UpdateAttribute

### # 字段说明

参数名称 | object | 描述  
---|---|---  
isAllUpdate | boolean | 是否更新所有数据, 当为false的时候最多只更新1000条数据，为true的时候不做数量限制, 默认为false  
triggerWorkflow | boolean | 是否触发工作流, 默认触发；不支持触发审批流；  
duplicateSearch | boolean | 是否查重, 默认查重  
modifiedBySelf | boolean | 是否指定当前用户为修改人；默认为false代表系统更新，更新人也是系统；设置为true代表当前用户更新，更新人是当前用户；可能存在数据权限不足更新失败的情况；不是所有场景都可以获取到当前用户，此时也会默认系统  
skipImmutableFieldValidate | boolean | 是否跳过不可变字段验证，默认false；主要应用于上游数据同步到下游时，下游是否可对锁定字段编辑；  
applyDataPrivilegeCheck | boolean | 是否校验数据权限，默认不校验  
  
## # 参考类 com.fxiaoke.functions.model.SelectAttribute

### # 字段说明

参数名称 | object | 描述  
---|---|---  
needRelevantTeam | java.lang.Boolean | 是否需要相关团队，默认否  
needQuote | java.lang.Boolean | 是否实时计算引用字段，默认是  
paginationOptimization | java.lang.Boolean | 是否执行分页优化，默认否，当需要大量数据分页操作时可以设置为true  
fillExtendInfo | java.lang.Boolean | 是否需要自动填充__r字段，例如人员信息，默认不填充  
needCount | java.lang.Boolean | 是否返回匹配条件的数量总数，默认否  
validateFilterField | java.lang.Boolean | 是否校验筛选字段，7.6日前默认为false不校验(可手动改为true校验)，7.6后默认为true校验（修改为false不生效）；  
calculateCount | java.lang.Boolean | 是否实时计算统计字段，默认是  
searchRichTextExtra | java.lang.Boolean | 是否返回完整的富文本/协同富文本/长文本，默认否  
filterByDataRight | java.lang.Boolean | 是否根据数据权限过滤数据（默认false）  
needCalculate | java.lang.Boolean | 查询时是否执行计算字段，默认是  
needInvalid | java.lang.Boolean | 是否返回已作废的数据，默认否  
convertQuoteForView | java.lang.Boolean | 是否以页面展示的格式返回引用字段（默认false），该参数主要针对引用单选、多选、布尔、业务类型的字段，默认返回value，设置为true以后，返回的是label，并通过${字段apiName}__v返回value，以及${字段apiName}__o返回其他选项。  
needOptionLabel | java.lang.Boolean | 是否返回选项名称，默认否，该参数为true会补充单选多选label 放到${字段apiName}__r中  
  
## # 参考类 com.fxiaoke.functions.tools.CreateAttribute

### # 字段说明

参数名称 | object | 描述  
---|---|---  
calculateDefaultValue | boolean | 是否计算默认值，默认为false  
fillOutOwner | boolean | 是否填充外部负责人, 业务逻辑接口使用, 元数据接口不使用, 默认否  
designatedCreatedBy | boolean | 是否指定创建人（包含所有从对象都是指定创建人），默认是系统，可以在参数objectData中指定的 `key: created_by (List <String> )` ，传入人员的id可以设置创建人  
specifyTime | boolean | 指定创建时间, 一般使用当前时间, 默认否  
skipAfterFunction | boolean | 是否跳过后动作函数, 业务逻辑接口使用, 元数据接口不使用, 默认为false  
triggerWorkflow | boolean | 是否触发工作流 ,默认触发  
duplicateSearch | boolean | 是否查重, 元数据接口不使用该字段, 因为元数据底层有实现查重, 默认查重  
enableRealTimeCalculateDataAuth | boolean | 是否实时计算数据权限，默认为false  
skipFunctionAction | boolean | 是否跳过前验证函数，默认为false不跳过  
forceQueryFromDB | boolean | 是否强制从数据库中查询, 和老接口对齐, 暂时不区分  
triggerApprovalFlow | boolean | 是否触发审批流, 默认触发  
  
## # 参考类 com.fxiaoke.functions.model.OptionAttribute

### # 字段说明

参数名称 | object | 描述  
---|---|---  
apiName | java.lang.String | 对象apiName  
optionValue | java.lang.String | 父单选选项值  
fieldApiName | java.lang.String | 父单选字段apiName  
  
[context](../context/) [Fx.org](../OrganizationAPI/)

← [context](../context/) [Fx.org](../OrganizationAPI/)→ 

  * 跟随系统 
  * 浅色模式 
  * 深色模式 
  * 阅读模式 


