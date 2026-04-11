#  Fx.AI

## # Fx.AI

### # 1\. detectPic 图片识别

> `Fx.AI.detectPic(<String modelId>, <String path>)`

**参数说明**

入参格式

参数名称 | object | 描述 | 是否必填  
---|---|---|---  
modelId | String | 物体识别模型唯一ID | 是  
path | String | 图片的nPath | 是  
  
**Groovy 举例**
    
    
    def(boolean error, Map data, String errorMessage) = Fx.AI.detectPic("5dabce96e75d9594e1dc05f6", "N_202006_09_87e2be5f5c364bda9cb5ed61a21ddd25")
    if (error) {
      log.error("detectPic " + errorMessage)
      //1.使用报错终止执行
      //Fx.message.throwException("detectPic " + errorMessage)
      //2.使用return终止执行
      //return;
      //3.继续执行
    } 
    //dosomething
    
    

**注意事项**

>   * 企业有模型才可以使用
> 


### # 2\. invoiceValidation 发票验真

> `Fx.AI.invoiceValidation(<InvoiceData arg>)`

**参数说明**

入参格式

参数名称 | object | 描述 | 是否必填  
---|---|---|---  
arg | InvoiceData | 发票验证实体对象 | 是  
  
出参格式

参数名称 | object | 描述  
---|---|---  
code | integer |   
message | string |   
data | object |   
data | object | 描述  
---|---|---  
N_202308_29_e157da5c641f446f92dbc9e2ba8c8885 | object |   
N_202308_29_e157da5c641f446f92dbc9e2ba8c8885 | object | 描述  
---|---|---  
success | boolean |   
errorCode | string |   
errorMsg | string |   
ocrJson | null |   
ocrType | null |   
  
出参样例
    
    
    {
    	"code": 200,
    	"message": "OK",
    	"data": {
    		"N_202308_29_e157da5c641f446f92dbc9e2ba8c8885": {
    			"success": false,
    			"errorCode": "216630",
    			"errorMsg": "recognize error",
    			"ocrJson": null,
    			"ocrType": null
    		}
    	}
    }
    
    

**Groovy 举例**
    
    
    InvoiceData invoice = InvoiceData.builder()
         .type("elec_normal_invoice")
         .code("011002100511")
         .number("24830566")
         .date("20210620")
         .amount("339.62")
         .checkCode("957725")
         .build()
    
    def(Boolean error, Object data, String errorMessage) = Fx.AI.invoiceValidation(invoice)
    if (error) {
      log.error("detectPic " + errorMessage)
      //1.使用报错终止执行
      //Fx.message.throwException("detectPic " + errorMessage)
      //2.使用return终止执行
      //return;
      //3.继续执行
    } 
    //dosomething
    
    

**参考对象**

  * 参考InvoiceData



### # 3\. queryOcrTypes 获取ocr支持的识别类型

> `Fx.AI.queryOcrTypes()`

**参数说明**

出参格式

参数名称 | object | 描述  
---|---|---  
code | integer |   
message | string |   
data | array[object] |   
data | object | 描述  
---|---|---  
type | string |   
desc | string |   
descKey | string |   
  
出参样例
    
    
    {
        "code": 200,
        "message": "sessage",
        "data":
        [
            {
                "type": "type",
                "desc": "desc",
                "descKey": "descKey"
            }
        ]
    }
    
    

**Groovy 举例**
    
    
    def (ue,ud,uem) = Fx.AI.queryOcrTypes()
    if(ue){
      log.info(uem)
    }
    else{
      log.info(ud)
    }
    
    

### # 4\. ocrImages ocr识别

> `Fx.AI.ocrImages(<string ocrType>, <array paths>)`

**参数说明**

入参格式

参数名称 | object | 描述 | 是否必填  
---|---|---|---  
ocrType | string |  | 是  
paths | array[string] |  | 是  
  
出参格式

参数名称 | object | 描述  
---|---|---  
code | integer |   
message | string |   
data | object |   
data | object | 描述  
---|---|---  
N_202308_29_e157da5c641f446f92dbc9e2ba8c8885 | object |   
N_202308_29_e157da5c641f446f92dbc9e2ba8c8885 | object | 描述  
---|---|---  
success | boolean |   
errorCode | string |   
errorMsg | string |   
ocrJson | null |   
ocrType | null |   
  
出参样例
    
    
    {
    	"code": 200,
    	"message": "OK",
    	"data": {
    		"N_202308_29_e157da5c641f446f92dbc9e2ba8c8885": {
    			"success": false,
    			"errorCode": "216630",
    			"errorMsg": "recognize error",
    			"ocrJson": null,
    			"ocrType": null
    		}
    	}
    }
    
    

**Groovy 举例**
    
    
    def (ue,ud,uem) = Fx.AI.ocrImages("MultipleInvoice",["N_202311_28_8c3e4c6e652748eb9c52142a32d2bcce"])
    if(ue){
      log.info(uem)
    }
    else{
      log.info(ud)
    }
    
    

### # 5\. chatCompletions 调用大模型chatCompletions接口

> `Fx.AI.chatCompletions(<Map map>)`

**参数说明**

入参格式

参数名称 | object | 描述 | 是否必填  
---|---|---|---  
map | Map | 调用大模型chatCompletions接口Map参数 | 是  
map | Map | 调用大模型chatCompletions接口Map参数 | 是否必填  
---|---|---|---  
model | String | 调用那个大模型，例如ERNIE-Bot，qwen-turbo | 是  
messages | List[object] | 和AI对话历史消息 | 是  
temperature | BigDecimal | temperature是一个控制模型预测可信度的值，当降低temperature时，模型预测的结果更加准确和确定，但可能缺乏创意；当提高temperature时，会得到更多种类的补全结果，但也会出现不太准确或创意不足的情况，范围0-1，默认值为0.7 | \--  
messages | object | 描述 | 是否必填  
---|---|---|---  
role | String | 对话使用的角色，有system 系统，assistant 大模型，user 用户 | 是  
content | String | 对话的消息内容 | 是  
  
出参格式

参数名称 | object | 描述  
---|---|---  
finish_reason | String | 模型停止生成文本的原因  
message | String | 大模型生成的文本内容  
  
出参样例
    
    
    {
        "finish_reason": "normal",
        "message": "当然可以。以下是一份简短的日记示例：\n\n---\n\n2023年4月15日 星期五 晴\n\n今天的心情像窗外的阳光一样明媚。早晨，我迎着第一缕阳光慢跑，感觉整个人都充满了活力。下午，和朋友们在咖啡馆相聚，谈笑间时间悄悄流逝。晚上，独自坐在书桌前，翻阅着喜欢的书籍，内心宁静而满足。简单的一天，却满载着幸福与温馨。\n\n---\n\n希望这份日记能够符合您的要求。"
    }
    
    

**Groovy 举例**
    
    
    //model: 大模型model现在接入的有
    //文心一言：ERNIE-Bot，ERNIE-Bot4.0
    //科大讯飞：generalv2, generalv3
    //阿里通义千问：qwen-turbo, qwen-plus
    //腾讯混元大模型: hunyuan-pro，hunyuan-standard
    //字节豆包：ep-20240618123932-5zk5j（Doubao-pro-4k），ep-20240618123950-llzrs（Doubao-pro-32k）
    //
    //messages：和模型对话的消息有，List类型 role, content两个字段
    //- role：角色
    //system 系统设定的上下文
    //assistant  大模型返回的内容
    //user 用户发出的内容
    //- content: 具体内容文本
    //
    //temperature：temperature是一个控制模型预测可信度的值，当降低temperature时，模型预测的结果更加准确和确定，但可能缺乏创意；当提高temperature时，会得到更多种类的补全结果，但也会出现不太准确或创意不足的情况，范围0-1
    
    Map request = [
      "model": "ERNIE-Bot",
      "messages": [
        [
          "role": "user",
          "content": "你好，文心一言，可以给我生成一份100字左右的日记吗"
        ]
      ],
      "temperature": 0.7
    ]
    
    def(boolean error, Map data, String errorMessage) = Fx.AI.chatCompletions(request)
    if (error) {
      log.error("chatCompletions " + errorMessage)
      //1.使用报错终止执行
      //Fx.message.throwException("chatCompletions " + errorMessage)
      //2.使用return终止执行
      //return;
      //3.继续执行
    }
    log.info(data)
    //dosomething
    
    

**注意事项**

>   * AI能力需要购买资源包：【AI产品资源包】
> 


### # 6\. completionsByPrompt 通过提示模板调用大模型生成接口

> `Fx.AI.completionsByPrompt(<String promptApiName>, <Map objectData>, <String bingObjectDataId>, <List otherObjectData>, <Map sceneVariables>)`

**参数说明**

入参格式

参数名称 | object | 描述 | 是否必填  
---|---|---|---  
promptApiName | String | 提示模板apiName | 是  
objectData | Map | 绑定主对象数据 | \--  
bingObjectDataId | String | 绑定主对象数据id，和objectData两个参数二选一，两个都不为空时，objectData优先 | \--  
otherObjectData | List[object] | 提示模板中用到的其他对象数据，objectApinName对象apiName，dataId是数据id | \--  
sceneVariables | Map | 提示模板自定义场景变量，key要和提示模板那边对应上 | \--  
otherObjectData | object | 描述 | 是否必填  
---|---|---|---  
objectApinName | List | 对象apiName | 是  
dataId | List | 是数据id | 是  
  
出参格式

参数名称 | object | 描述  
---|---|---  
message | String | 大模型的输出结果  
  
出参样例
    
    
    {
        "message": "{\n \"outputLanguage\": \"英语\",\n \"outText\": \"Hello\"\n}"
    }
    
    

**Groovy 举例**
    
    
    // 提示模板apiName
    String promptApiName = 'prompt_GrQPP__c'
    // 绑定主对象数据完整信息
    Map objectData = [
      "name": "客户数据123",
      "object_describe_api_name": "AccountObj"
    ]
    // 绑定主对象数据id，和objectData两个参数二选一，两个都不为空时，objectData优先
    String bingObjectDataId = "63b6b583b6b41e00018ae21d"
    // 提示模板中用到的其他对象数据，objectApinName对象apiName，dataId是数据id
    List otherObjectData = [
      [
        "objectApinName": "LeadsObj",
        "dataId": "62a9b7c16d5aad00017bff4f"
      ],
      [
        "objectApinName": "SalesOrderObj",
        "dataId": "62a9b7c16d5aad00017bff4f"
      ]
    ]
    // 提示模板自定义场景变量，key要和提示模板那边对应上
    Map sceneVariables = [
      "content": "你好",
      "targetLanguage": "英语"
    ]
    
    def(boolean error, Map data, String errorMessage) = Fx.AI.completionsByPrompt(promptApiName, objectData, bingObjectDataId, otherObjectData, sceneVariables)
    if (error) {
      log.error("completionsByPrompt " + errorMessage)
      //1.使用报错终止执行
      //Fx.message.throwException("completionsByPrompt " + errorMessage)
      //2.使用return终止执行
      //return;
      //3.继续执行
    }
    log.info(data)
    //dosomething
    
    

**注意事项**

>   * AI能力需要购买资源包：【AI产品资源包】
> 


### # 7\. 通过语义检索内容

> `Fx.AI.RAGRetrieval(<String ragApiName>, <String query>)`

**参数说明**

入参格式

参数名称 | 知识库 | 描述 | 是否必填  
---|---|---|---  
ragApiName | String | 语义检索索引apiName | 是  
query | String | 用户问题 | 是  
  
出参格式

参数名称 | object | 描述  
---|---|---  
scoreThreshold | BigDecimal | 参考阈值  
hits | List[object] |   
hits | object | 描述  
---|---|---  
objectApiName | String | 对象apiName  
id | String | 对象数据id  
content | String | 文章内容  
retrievalType | String | 召回类型  
score | BigDecimal | 得分  
  
出参样例
    
    
    {
        "scoreThreshold": 2.0,
        "hits": [
            {
                "objectApiName": "ServiceKnowledgeObj",
                "id": "6718e6c45bc3550001a216e7",
                "content": "RocketMQ，MySQL知识点\n\n\nmysql.docx文件内容如下:\n面试官：请详细说说RocketMQ的消息确认机制？xxx",
                "score": 0.009232215
            },
            {
                "objectApiName": "ServiceKnowledgeObj",
                "id": "66bad2bd0a62fe00018dbd0b",
                "content": "海量数据定时工作流分析及优化专题xxx",
                "score": 0.0058653383
            }
        ]
    }
    
    

**Groovy 举例**
    
    
    // ragAPIname 在管理后台【AI平台管理】中【语义检索索引】中新建的数据
    String ragAPIName = "rag_service_knowledge__c"
    
    // 需要检索的内容
    String query = "对接天润"
    
    def(boolean error, Map data, String message) = Fx.AI.RAGRetrieval(ragAPIName, query)
    if (error) {
      log.error("chatCompletions " + errorMessage)
      //1.使用报错终止执行
      //Fx.message.throwException("chatCompletions " + errorMessage)
      //2.使用return终止执行
      //return;
      //3.继续执行
    }
    log.info(data)
    //dosomething
    
    

**注意事项**

>   * 这属于AI能力的一部分，需要购买资源包：【AI产品资源包】
> 


**负责人：韩统武(已停用)**

## # 参考类 com.fxiaoke.functions.model.InvoiceData

### # 字段说明

参数名称 | object | 描述  
---|---|---  
date | java.lang.String | 发票日期：  
number | java.lang.String | 发票号码  
amount | java.lang.String | 发票金额（不含税）  
code | java.lang.String | 发票代码  
type | java.lang.String | 发票类型  
checkCode | java.lang.String | 发票校验码（后6位），非必填  
  
[Fx.utils](../UtilsAPI/) [Fx.tag](../TagAPI/)

← [Fx.utils](../UtilsAPI/) [Fx.tag](../TagAPI/)→ 

  * 跟随系统 
  * 浅色模式 
  * 深色模式 
  * 阅读模式 


