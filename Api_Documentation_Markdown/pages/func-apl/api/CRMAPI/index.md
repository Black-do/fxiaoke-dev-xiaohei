#  Fx.crm

## # Fx.crm

### # 1\. getProduct 产品

> `Fx.crm.getProduct()`

#### # 参考函数接口

  * 参考com.fxiaoke.functions.api.ProductAPI



**负责人：孙得育**

### # 2\. getLeads 线索

> `Fx.crm.getLeads()`

#### # 参考函数接口

  * 参考com.fxiaoke.functions.api.LeadsAPI



**负责人：龚春如**

### # 3\. getAccount 客户

> `Fx.crm.getAccount()`

#### # 参考函数接口

  * 参考com.fxiaoke.functions.api.AccountAPI



**负责人：李坤bruce**

### # 4\. getBom Bom

> `Fx.crm.getBom()`

#### # 参考函数接口

  * 参考com.fxiaoke.functions.api.BomAPI



### # 5\. getEnterpriseByName 通过公司名称模糊查询工商信息

> `Fx.crm.getEnterpriseByName(<String companyName>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
companyName | String | 公司名称/统一社会信用代码/注册号 | 是  
  
出参格式

参数名称 | APIResult | API返回结果的JSON Schema  
---|---|---  
isError | boolean | 是否错误  
data | List | 返回的数据  
message | string | 信息  
  
**Groovy 举例**
    
    
    def(Boolean error, List data, String errorMessage) = Fx.crm.getEnterpriseByName("百度")
    
    

### # 6\. getEnterpriseDetailById 通过companyId查询工商信息

> `Fx.crm.getEnterpriseDetailById(<String companyId>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
companyId | String | 公司名称 | 是  
  
**Groovy 举例**
    
    
    def(Boolean error, Map data, String errorMessage) = Fx.crm.getEnterpriseDetailById("1644990310")
    
    

### # 7\. 自动核销函数

> `Fx.crm.automatch(<String objectDescribeApiName>, <String objectDataId>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
objectDescribeApiName | String | 对象apiName | 是  
objectDataId | String | 对象id | 是  
  
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
      "message" : "success"
    }
    
    

**Groovy 举例**
    
    
    String objectDescribeApiName = "PaymentObj "
    String objectDataId = "1111"
     
    def(boolean error, Map data, String message) = Fx.crm.automatch(objectDescribeApiName, objectDataId)
    if (error) {
      log.info("error: " + message)
    } else {
      log.info(data)
    }
    
    

**注意事项**

>   *     * 注意事项：该函数目前只支持开启自动核销场景下才可以使用
> 


### # 8\. 银行流水识别客户

> `Fx.crm.bankStatement.identifyAccount(<List objectIds>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
objectIds | List | 银行流水id列表 | 是  
  
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
      "message" : "success"
    }
    
    

**Groovy 举例**
    
    
    List<String> objectIds= ["1111"]
     
    def(boolean error, Map data, String message) = Fx.crm.bankStatement.identifyAccount(objectIds)
    if (error) {
      log.info("error: " + message)
    } else {
      log.info(data)
    }
    
    

**注意事项**

>   *     * 注意事项：该函数目前只支持开启开启到款认款场景下才可以使用
> 


### # 9\. 周期性立应收

> `Fx.crm.periodicAccountsReceivable(<String masterDescribeApiName>, <String detailDescribeApiName>, <String detailDataId>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
masterDescribeApiName | String | 主对象apiName | 是  
detailDescribeApiName | String | 从对象apiName | 是  
detailDataId | String | 从对象id | 是  
  
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
      "message" : "success"
    }
    
    

**Groovy 举例**
    
    
    String masterDescribeApiName = "SalesOrderObj"
    String detailDescribeApiName= "SalesOrderProductObj"
    String detailDataId = "1111"
     
    def(boolean error, Map data, String message) = Fx.crm.periodicAccountsReceivable(masterDescribeApiName,detailDescribeApiName, detailDataId)
    if (error) {
      log.info("error: " + message)
    } else {
      log.info(data)
    }
    
    

**注意事项**

>   *     * 注意事项：该函数目前只支持开启开启周期性立应收才可以使用
> 


## # 参考类 com.fxiaoke.functions.api.ProductAPI

### # 1\. shelf 产品上架下架

> `Fx.crm.product.shelf(<String productId>, <Integer status>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
productId | String | 产品id | 是  
status | Integer | status = 1上架，status = 2 下架 | 是  
  
**Groovy 举例**
    
    
    def (Boolean err,Map data,String errorMessage) = Fx.crm.product.shelf("e1e145095f8142c891802fa36fcbd4c6", 1) //上架产品
    def (Boolean err,Map data,String errorMessage) = Fx.crm.product.shelf("e1e145095f8142c891802fa36fcbd4c6",2) //下架产品
    
    

### # 2\. createProductCategory 创建产品分类

> `Fx.crm.product.createProductCategory(<String name>, <String categoryCode>, <String pid>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
name | String | 产品分类名称 | 是  
categoryCode | String | 产品分类编码 | 是  
pid | String | 父类产品Id | \--  
  
**Groovy 举例**
    
    
    def (Boolean err,Map data,String errorMessage) = Fx.crm.product.createProductCategory("产品分类名","产品分类编码",null)
    def (Boolean err,Map data,String errorMessage) = Fx.crm.product.createProductCategory("产品分类名","产品分类编码","123")
    
    

### # 3\. deleteProductCategory 删除产品分类

> `Fx.crm.product.deleteProductCategory(<String id>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
id | String | 产品分类id | 是  
  
**Groovy 举例**
    
    
    def res = (((Fx.object.find("ProductCategoryObj",[["category_code":"111"]],  10,  0)[1]) as QueryResult).dataList[0] as Map)
    def id = (res._id) as String
    def (Boolean error,Map data,String errorMessage) = Fx.crm.product.deleteProductCategory(id)
    log.info(data)
    
    

### # 4\. updateProductCategory 修改产品分类

> `Fx.crm.product.updateProductCategory(<String id>, <Map arg>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
id | String | 产品分类id | 是  
arg | Map | 更新产品分类内容 | 是  
  
**Groovy 举例**
    
    
    def res = (((Fx.object.find("ProductCategoryObj",[["category_code":"111"]], 10, 0)[1]) as QueryResult).dataList[0] as Map)
    def id = (res._id) as String
    Map map = ["name":"111","categoryCode":"222"]
    //修该产品分类
    def (boolean err,Map dataList,String errorMessage) = Fx.crm.product.updateProductCategory(id,map)
    
    

### # 5\. searchCategory 根据字段值查询分类数据

> `Fx.crm.product.searchCategory(<String fieldApiName>, <List values>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
fieldApiName | String | 分类上的字段ApiName，用于根据该字段搜索分类数据，参数：'category_code' | 是  
values | List | 字段值 List，最多20个 | 是  
  
**Groovy 举例**
    
    
    // 字段apiName，支持：“cayegory_code”
    def fieldApiName = "category_code"
    // 搜索的字段值，最大20个
    def values = ["pNxTqSPS"]
    def(boolean error, List data, String message) = Fx.crm.product.searchCategory(fieldApiName, values)
    if (error) {
      log.info("error: " + message)
    } else {
      log.info(data)
    }
    
    

### # 6\. associateAttribute 产品属性关联

> `Fx.crm.product.associateAttribute(<List productIds>, <List attributeIds>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
productIds | List | 产品id数组 | 是  
attributeIds | List | 属性id数组 | 是  
  
**Groovy 举例**
    
    
    // 产品id列表："product_ids"
    def product_ids = ["xxxxx"]
    // 属性id列表
    def attribute_ids= ["xxxxx"]
    def(boolean error, List data, String message) = Fx.crm.product.associateAttribute(product_ids, attribute_ids)
    if (error) {
      log.info("error: " + message)
    } else {
      log.info(data)
    }
    
    

### # 7\. disAssociateAttribute 产品属性解除关联

> `Fx.crm.product.disAssociateAttribute(<List productIds>, <List attributeIds>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
productIds | List | 产品id数组 | 是  
attributeIds | List | 属性id数组 | 是  
  
**Groovy 举例**
    
    
    // 产品id列表："product_ids"
    def product_ids = ["xxxxx"]
    // 属性id列表
    def attribute_ids= ["xxxxx"]
    def(boolean error, List data, String message) = Fx.crm.product.disAssociateAttribute(product_ids, attribute_ids)
    if (error) {
      log.info("error: " + message)
    } else {
      log.info(data)
    }
    
    

## # 参考类 com.fxiaoke.functions.api.LeadsAPI

### # 1\. move 线索转移

> `Fx.crm.leads.move(<String leadsId>, <String leadsPoolId>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
leadsId | String | 线索Id | 是  
leadsPoolId | String | 线索池Id | 是  
  
**Groovy 举例**
    
    
    def (Boolean err,String data,String errorMessage) = Fx.crm.leads.move("05f3f656feb9496abaa4cf50f1fa22ce", "85f454b044894f83a57e1bacfd2f1beb")
    
    

### # 2\. giveBack 线索退回

> `Fx.crm.leads.giveBack(<String leadsIds>, <String leadsPoolId>, <String backReason>, <String otherReason>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
leadsIds | String | 线索ID | 是  
leadsPoolId | String | 线索池ID | 是  
backReason | String | 退回原因，对应对象上退回原因选项值，传选项值的value，默认return by function | \--  
otherReason | String | backReason 如果是other的话，可以在 otherReason 中传其它的详细内容 | \--  
  
**Groovy 举例**
    
    
    Fx.crm.leads.giveBack("05f3f656feb9496abaa4cf50f1fa22ce", "85f454b044894f83a57e1bacfd2f1beb")
    
    

### # 3\. allocate 线索分配

> `Fx.crm.leads.allocate(<List leadsIds>, <String leadsPoolId>, <String ownerld>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
leadsIds | List[String] | 线索ID列表 | 是  
leadsPoolId | String | 线索池ID | 是  
ownerld | String | 用户ID | 是  
  
**Groovy 举例**
    
    
    Fx.crm.leads.allocate(["3ed01dcafbe4402d99d7a521aaa4e9c3"], "85f454b044894f83a57e1bacfd2f1beb", "1025")
    
    

### # 4\. takeBack 线索收回

> `Fx.crm.leads.takeBack(<List leadsIds>, <String leadsPoolId>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
leadsIds | List[String] | 线索ID列表 | 是  
leadsPoolId | String | 线索池ID | 是  
  
**Groovy 举例**
    
    
    def(Boolean err,String rs,String errorMessage)= Fx.crm.leads.takeBack(["3ed01dcafbe4402d99d7a521aaa4e9c3"], "85f454b044894f83a57e1bacfd2f1beb")
      if (err) {
        log.debug("收回失败：" + errorMessage)
      }else{
        log.debug("收回成功" )
      }
    
    

### # 5\. transfer 线索一转三

> `Fx.crm.leads.transfer(<Boolean combineCRMFeed>, <Boolean putTeamMembersIntoCustomer>, <String leadsId>, <Map account>, <Map contact>, <Map newObjectData>, <Map opportunity>)`

**参数说明**

入参格式

参数名称 | 销售线索转换参数 | 描述 | 是否必填  
---|---|---|---  
combineCRMFeed | Boolean | 销售线索的销售记录自动带入客户 | 是  
putTeamMembersIntoCustomer | Boolean | 销售线索的相关团队自动带入客户 | 是  
leadsId | String | 销售线索的id | 是  
account | Map | 客户的Map ， 如果存在_id 则关联旧客户，如果不存在id 则创建新客户 | 是  
contact | Map | 转换成联系人的Map | 是  
newObjectData | Map | 包含新商机数据的对象 | 是  
opportunity | Map | 转换成商机的数据 | 是  
newObjectData | Map | 包含新商机数据的对象 | 是否必填  
---|---|---|---  
object_data | object | 必填。转换成商机2.0的数据 | \--  
  
**Groovy 举例**
    
    
    String leadsId = "05f3f656feb9496abaa4cf50f1fa22ce"
    Map account = [
      "object_describe_api_name": "AccountObj",
      "record_type": "default__c",
      "created_by": [
        "1109"
      ],
      "name": "hello"
    ]
    Map contact = [:]
    Map newOpportunity = [:]
    Map newObjectData = ["object_data": newOpportunity]
    Map opportunity = [:]
    def(boolean error, Object data, String msg) = Fx.crm.leads.transfer(true, true, leadsId, account, contact, newObjectData, opportunity)
    if (error) {
      log.info(data)
    } else {
      log.info(msg)
    }
    
    

## # 参考类 com.fxiaoke.functions.api.AccountAPI

### # 1\. move 客户转移公海

> `Fx.crm.account.move(<String accountId>, <String highSeaId>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
accountId | String | 客户Id | 是  
highSeaId | String | 公海Id | 是  
  
出参格式

参数名称 | APIResult | 描述  
---|---|---  
error | Boolean | 是否错误  
data | String | 返回数据  
message | String | 信息  
  
出参样例
    
    
    {
      "isError" : false,
      "data" : "success",
      "message" : ""
    }
    
    

**Groovy 举例**
    
    
    Fx.crm.account.move("ad14bbbcede240a48dc2f65787a8763d","6c1a6a54617245fe90aae5a162eb191d").result()
    
    

### # 2\. remove 客户移除公海

> `Fx.crm.account.remove(<String accountId>, <String highSeaId>, <String owner>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
accountId | String | 客户Id | 是  
highSeaId | String | 公海Id | 是  
owner | String | 负责人id | 是  
  
出参格式

参数名称 | APIResult | 描述  
---|---|---  
error | Boolean | 是否错误  
data | String | 返回数据  
message | String | 信息  
  
出参样例
    
    
    {
      "isError" : false,
      "data" : "success",
      "message" : ""
    }
    
    

**Groovy 举例**
    
    
    Fx.crm.account.remove("ad14bbbcede240a48dc2f65787a8763d","6c1a6a54617245fe90aae5a162eb191d","1000").result()
    
    

### # 3\. giveBack 客户退回公海

> `Fx.crm.account.giveBack(<String accountId>, <String highSeaId>, <String backReason>, <String otherReason>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
accountId | String | 客户Id | 是  
highSeaId | String | 公海Id | 是  
backReason | String | 退回原因，对应对象上退回原因选项值，传选项值的value，默认为'return by function'，非必填 | \--  
otherReason | String | backReason 如果是other的话，可以在 otherReason 中传其它的详细内容，非必填 | \--  
  
出参格式

参数名称 | APIResult | 描述  
---|---|---  
error | Boolean | 是否错误  
data | String | 返回数据  
message | String | 信息  
  
出参样例
    
    
    {
      "isError" : false,
      "data" : "success",
      "message" : ""
    }
    
    

**Groovy 举例**
    
    
    Fx.crm.account.giveBack("ad14bbbcede240a48dc2f65787a8763d","6c1a6a54617245fe90aae5a162eb191d", "other", "不符合").result()
    
    

### # 4\. takeOut 客户领取

> `Fx.crm.account.takeOut(<List accountIds>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
accountIds | List | 客户Id列表 | 是  
  
出参格式

参数名称 | APIResult | 描述  
---|---|---  
error | Boolean | 是否错误  
data | String | 返回数据  
message | String | 信息  
  
出参样例
    
    
    {
      "isError" : false,
      "data" : "success",
      "message" : ""
    }
    
    

**Groovy 举例**
    
    
    Fx.crm.account.takeOut(["ad14bbbcede240a48dc2f65787a8763d", "6c1a6a54617245fe90aae5a162eb191d"]).result()
    
    

### # 5\. allocate 客户分配

> `Fx.crm.account.allocate(<List accountIds>, <String highSeaId>, <String ownerId>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
accountIds | List | 客户Id列表 | 是  
highSeaId | String | 公海Id | 是  
ownerId | String | 用户Id | 是  
  
出参格式

参数名称 | APIResult | 描述  
---|---|---  
error | Boolean | 是否错误  
data | String | 返回数据  
message | String | 信息  
  
出参样例
    
    
    {
      "isError" : false,
      "data" : "success",
      "message" : ""
    }
    
    

**Groovy 举例**
    
    
    Fx.crm.account.allocate(["cd097b120f584533b627c40239ece7d0"],"0ebc054e55254b8b89f09d7ac7602972","1025").result()
    
    

### # 6\. takeBack 客户收回

> `Fx.crm.account.takeBack(<List accountIds>, <String highSeaId>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
accountIds | List | 客户Id列表 | 是  
highSeaId | String | 公海Id | 是  
  
出参格式

参数名称 | APIResult | 描述  
---|---|---  
error | Boolean | 是否错误  
data | String | 返回数据  
message | String | 信息  
  
出参样例
    
    
    {
      "isError" : false,
      "data" : "success",
      "message" : ""
    }
    
    

**Groovy 举例**
    
    
    Fx.crm.account.takeBack(["cd097b120f584533b627c40239ece7d0"],"0ebc054e55254b8b89f09d7ac7602972").result()
    
    

## # 参考类 com.fxiaoke.functions.api.BomAPI

### # 1\. 保存产品选配明细

> `Fx.crm.bom. bomDeploy(<String rootProductId>, <List nodeList>, <List deletedBomAndGroupList>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
rootProductId | String | 根节点产品id | 是  
nodeList | List | 新增修改数据数组 | \--  
deletedBomAndGroupList | List | 删除数据数组 | \--  
  
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
      "message" : "success"
    }
    
    

**Groovy 举例**
    
    
    // 需要删除的节点数据
    def deletedBomAndGroupList=[]
    // 需要新增和修改的节点数据
    def nodeList = [
      [
        "object_describe_api_name": "ProductGroupObj",
        "name": "分组一",
        "group_options_control": false,
        "min_prod_count": null,
        "max_prod_count": null,
        "children": [
          [
            "record_type": "default__c",
            "object_describe_api_name": "BOMObj",
            "price_editable": true,
            "price_mode": "1",
            "amount": "3",
            "min_amount": "2",
            "selected_by_default": true,
            "increment": "1",
            "is_required": false,
            "life_status": "normal",
            "enabled_status": true,
            "amount_editable": true,
            "max_amount": "5",
            "product_id": "640716930f8b230001378dea",
            "action_type": "create",
            "adjust_price": "3.00"
          ]
        ],
        "action_type": "create",
        "record_type": "default__c"
      ]
    ]
    // 根节点产品id
    def rootProductId="6406f80060c1980001a23560"
    def(boolean error, Map data, String message) = Fx.crm.bom.bomDeploy(rootProductId, nodeList, deletedBomAndGroupList)
    if (error) {
      log.info("error: " + message)
    } else {
      log.info(data)
    }
    
    

### # 2\. 产品组合新建

> `Fx.crm.bom.add(<Map objectData>, <Map details>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
objectData | Map | 主对象数据即字段值 | 是  
details | Map | 从对象数据 | 是  
  
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
      "message" : "success"
    }
    
    

**Groovy 举例**
    
    
    Map masterData = [
            "product_id"              : "6600e02fab2ffd00073faad2",//父项产品，必填，产品ID
            "category"                : "configure",//BOM类型（configure-配置BOM，standard-标准BOM）
            "purpose"                 : "sale", //BOM用途，sale-销售BOM （固定，不要改）
            "object_describe_api_name": "BomCoreObj", //（固定，不要改）
            "owner"                   : ["-10000"],
            "record_type"             : "default__c"
    ];
    
    List details = [];
    Map product1 = [
            "record_type"             : "default__c",
            "object_describe_api_name": "BOMObj", //表示子件
            "product_id"              : "65fd50dd9f9a2d000128c294", //必填
            "amount"                  : "1",//数量
            "price_mode"              : "1",//定价模式 1-配置价格 2-价目表价格
            "adjust_price"            : 200, //定价模式为 价目表价格 时，可以不设置此字段
            "is_required"             : true,//是否必须
            "selected_by_default"     : true,//是否默认选中
            "price_editable"          : false,//价格是否可编辑
            "amount_editable"         : false,//数量是否可编辑
            "increment"               : 1,//增加数量幅度
            "enabled_status"          : true,//启用状态
            "order_field"             : "1",//显示顺序
            "action_type"             : "create",
            "children"                : [] //子件下允许挂子件，如果没有子件，可以不设置
    ];
    details.add(product1);
    
    
    List children = [
            [
                    "action_type"             : "create",
                    "record_type"             : "default__c",
                    "object_describe_api_name": "BOMObj",//必填
                    "product_id"              : "65fd50dd9f9a2d000128c294", //必填
                    "amount"                  : "1",
                    "price_mode"              : "1",
                    "adjust_price"            : 300,
                    "is_required"             : true,
                    "selected_by_default"     : true,
                    "price_editable"          : false,
                    "amount_editable"         : false,
                    "increment"               : 1,
                    "enabled_status"          : true,
                    "order_field"             : "1"
            ],
            [
                    "action_type"             : "create",
                    "record_type"             : "default__c",
                    "object_describe_api_name": "BOMObj", //必填
                    "product_id"              : "6603c02d491f7e00079431ca", //必填
                    "amount"                  : "1",
                    "price_mode"              : "1",
                    "adjust_price"            : 300,
                    "is_required"             : true,
                    "selected_by_default"     : true,
                    "price_editable"          : false,
                    "amount_editable"         : false,
                    "increment"               : 1,
                    "enabled_status"          : true,
                    "order_field"             : "1"
            ]
    ];
    
    
    Map group = [
            "record_type"             : "default__c",
            "object_describe_api_name": "ProductGroupObj",////表示分组
            "name"                    : "测试分组信息",
            "order_field"             : "1",//设置显示顺序
            "group_options_control"   : true,
            "action_type"             : "create",
            "children"                : children //分组下所挂的子件
    ];
    details.add(group);
    Map detailData = [
            "BOMObj": details
    ]
    
    def (boolean error, Map data, String message) = Fx.crm.bom.add(masterData, detailData);
    if (error) {
        log.info("错误信息：" + message);
    } else {
        log.info("返回结果：" + data);
    }
    
    

**注意事项**

>   * 参数说明：
>   * children 代表当前节点的子节点集合
> 


### # 3\. 产品组合编辑

> `Fx.crm.bom.edit(<Map objectData>, <Map details>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
objectData | Map | 主对象数据即字段值 | 是  
details | Map | 从对象数据 | 是  
  
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
      "message" : "success"
    }
    
    

**Groovy 举例**
    
    
    Map masterData = [
            "product_id"              : "6600e02fab2ffd00073faad2",//父项产品，必填，产品ID
            "category"                : "configure",//BOM类型（configure-配置BOM，standard-标准BOM）
            "purpose"                 : "sale", //BOM用途，sale-销售BOM （固定，不要改）
            "object_describe_api_name": "BomCoreObj", //（固定，不要改）
            "owner"                   : ["-10000"],
            "record_type"             : "default__c"
    ];
    
    List details = [];
    Map product1 = [
            "record_type"             : "default__c",
            "object_describe_api_name": "BOMObj", //表示子件
            "product_id"              : "65fd50dd9f9a2d000128c294", //必填
            "amount"                  : "1",//数量
            "price_mode"              : "1",//定价模式 1-配置价格 2-价目表价格
            "adjust_price"            : 200, //定价模式为 价目表价格 时，可以不设置此字段
            "is_required"             : true,//是否必须
            "selected_by_default"     : true,//是否默认选中
            "price_editable"          : false,//价格是否可编辑
            "amount_editable"         : false,//数量是否可编辑
            "increment"               : 1,//增加数量幅度
            "enabled_status"          : true,//启用状态
            "order_field"             : "1",//显示顺序
            "action_type"             : "create",
            "children"                : [] //子件下允许挂子件，如果没有子件，可以不设置
    ];
    details.add(product1);
    
    
    List children = [
            [
                    "action_type"             : "create",
                    "record_type"             : "default__c",
                    "object_describe_api_name": "BOMObj",//必填
                    "product_id"              : "65fd50dd9f9a2d000128c294", //必填
                    "amount"                  : "1",
                    "price_mode"              : "1",
                    "adjust_price"            : 300,
                    "is_required"             : true,
                    "selected_by_default"     : true,
                    "price_editable"          : false,
                    "amount_editable"         : false,
                    "increment"               : 1,
                    "enabled_status"          : true,
                    "order_field"             : "1"
            ],
            [
                    "action_type"             : "create",
                    "record_type"             : "default__c",
                    "object_describe_api_name": "BOMObj", //必填
                    "product_id"              : "6603c02d491f7e00079431ca", //必填
                    "amount"                  : "1",
                    "price_mode"              : "1",
                    "adjust_price"            : 300,
                    "is_required"             : true,
                    "selected_by_default"     : true,
                    "price_editable"          : false,
                    "amount_editable"         : false,
                    "increment"               : 1,
                    "enabled_status"          : true,
                    "order_field"             : "1"
            ]
    ];
    
    
    Map group = [
            "record_type"             : "default__c",
            "object_describe_api_name": "ProductGroupObj",////表示分组
            "name"                    : "测试分组信息",
            "order_field"             : "1",//设置显示顺序
            "group_options_control"   : true,
            "action_type"             : "create",
            "children"                : children //分组下所挂的子件
    ];
    details.add(group);
    Map detailData = [
            "BOMObj": details
    ]
    
    def (boolean error, Map data, String message) = Fx.crm.bom.edit(masterData, detailData);
    if (error) {
        log.info("错误信息：" + message);
    } else {
        log.info("返回结果：" + data);
    }
    
    

**注意事项**

>   * 参数说明：
>   * children 代表当前节点的子节点集合
>   * action_type 代表当前节点的增、改、删传：create、update、delete
> 


### # 5\. 获取产品组合完整结构

> `Fx.crm.bom.queryBomTree(<产品组合ID bom_core_id>, <是否需要返回子BOM数据 need_sub_bom>, <产品组合包的数量，默认为1 bom_amount>, <产品分组如果已删除，是否返回分组下的子件。默认不返回 include_all>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
bom_core_id | 产品组合ID | 产品组合ID | 是  
need_sub_bom | 是否需要返回子BOM数据 | 是否需要返回子BOM数据 | \--  
bom_amount | 产品组合包的数量，默认为1 | 产品组合包的数量，默认为1 | \--  
include_all | 产品分组如果已删除，是否返回分组下的子件。默认不返回 | 产品分组如果已删除，是否返回分组下的子件。默认不返回 | \--  
  
出参格式

参数名称 | APIResult | 描述  
---|---|---  
isError | boolean | 是否错误  
data | 子件List | 返回的数据  
message | String | 信息  
  
出参样例
    
    
    {
      "isError" : false,
      "data" : {},
      "message" : "success"
    }
    
    

**Groovy 举例**
    
    
    def(boolean error, Object data , String message) =  Fx.crm.bom.queryBomTree("67ee3216cf9d1b00014a4af5", true, amount, false);
          Map map = Fx.json.parseObject(data as String,  Map);
          List result = map["dataMapList"] as List;
    
    

[Fx.log](../LogAPI/) [Fx.work](../WorkAPI/)

← [Fx.log](../LogAPI/) [Fx.work](../WorkAPI/)→ 

  * 跟随系统 
  * 浅色模式 
  * 深色模式 
  * 阅读模式 


