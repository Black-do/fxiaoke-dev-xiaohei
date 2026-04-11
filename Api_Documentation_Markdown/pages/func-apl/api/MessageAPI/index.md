#  Fx.message

## # Fx.message

### # 1\. send 发送文本消息

> `Fx.message.send()`

**Groovy 举例**
    
    
    Channel channel = Channel.Service("FSAID_bebd374")
    List receiverIds = [1000] //消息接收用户
    def (error,date,errorMessage) = Fx.message.send("这是一条文本消息",receiverIds,channel)
    
    

**参考对象**

  * 参考Channel



### # 2\. send 发送卡片消息

> `Fx.message.send(<String card>, <List receiverIds>, <Channel channel>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
card | String | 卡片消息。结构较复杂，请使用ObjectCard.builder 去构建 | 是  
receiverIds | List[Integer] | 接收人id列表 | 是  
channel | Channel | 不要自己定义，请使用参考类com.fxiaoke.functions.model.Channel, Channel channel = Channel.Service("appiD"); //发送服务号, Channel channel = Channel.ObjectSession("AccountObj", "61848edfd9007e00019ee222") //发送客群 | 是  
card | String | 卡片消息。结构较复杂，请使用ObjectCard.builder 去构建 | 是否必填  
---|---|---|---  
head | Head | 卡片标题 | \--  
body | Body | 卡片内容 | \--  
foot | Foot | 卡片底部 | \--  
objectApiName | String | 卡片关联对象详情，所需到对象apiname和objectId一起使用，可替代下面到链接地址，可选 | \--  
objectId | String | 卡片关联对象详情，所需到对象objectId和apiname一起使用，可替代下面到链接地址，可选 | \--  
innerDirectWebUrl | String | 卡片在纷享内的web跳转地址，可选 | \--  
innerDirectMobileUrl | String | 卡片在纷享内的移动的跳转地址，无则使用web地址，可选 | \--  
outerDirectUrl | String | 卡片推出到外部平台的跳转地址，可选 | \--  
head | Head | 卡片标题 | 是否必填  
---|---|---|---  
title | String | 卡片标题(必填) | \--  
body | Body | 卡片内容 | 是否必填  
---|---|---|---  
content | String | 卡片标题(必填) | \--  
entries | Map | 卡片表格(可选) | \--  
foot | Foot | 卡片底部 | 是否必填  
---|---|---|---  
title | String | 卡片标题(必填) | \--  
  
**Groovy 举例**
    
    
    def card = ObjectCard.builder {
      head {
        title = "head title" //卡片标题(必填)
      }
      foot {
        title = "foot title" //卡片底部(必填)
      }
      body {
        content = "body content" //卡片内容(必填)
        entries = [key: "value"] //卡片表格(可选)
      }
      objectApiName = "AccountObj" //跳转对象的APIName(必填)
      objectId = "5cbd28e47cfed9ea0cca09e4" //跳转对象的id(必填)
    }
    Channel channel = Channel.Service("DSTX")
    List receiverIds = [1000]
    def (error,date,errorMessage) = Fx.message.send(card,receiverIds,channel)
    
    

### # 3\. sendNotice 发送CRM通知

> `Fx.message.sendNotice(<String title>, <String content>, <List receiverIds>, <Notice notice>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
title | String | CRM通知标题 | 是  
content | String | CRM通知内容 | 是  
receiverIds | List[Integer] | 接收人id列表 | 是  
notice | Notice | 通知的类型，现有：defaultNotice：普通通知，Notice notice = Notice.defaultNotice() objectNotice：带对象详情页链接的crm通知，需要传对象的apiName和数据Id ,Notice notice = Notice.objectNotice(String apiName, String dataId) | 是  
  
**Groovy 举例**
    
    
    List receiverIds = ['1000', '1001']
    Notice objectNotify = Notice.objectNotice("AccountObj","5fa4de2f832a9d00012868b8")
    def (Boolean error, String data, String errorMessage) = Fx.message.sendNotice("这也是一个标题","这个是提醒的内容",receiverIds, objectNotify)
    if (error) {
    log.info(errorMessage)
    } else {
    log.info(data)
    }
    
    

### # 3\. sendNotice 发送CRM通知,可不关联数据

> `Fx.message.sendNotice(<String title>, <String content>, <List receiverIds>, <String entityId>, <String objectId>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
title | String | CRM通知标题 | 是  
content | String | CRM通知内容 | 是  
receiverIds | List[Integer] | 接收人id列表 | 是  
entityId | String | 对象apiName | \--  
objectId | String | 对象数据id | \--  
  
**Groovy 举例**
    
    
    Map data = context.data
    String entityId = data.get("object_describe_api_name")
    String objectId = data.get("_id")
    
    log.info(entityId+":"+objectId)
    
    //标题,内容,接收人,对象apiname(选填),对象数据id(选填)
    //如果对象apiname和对象数据id 不填,则发出的消息不会跳转到数据详情页,只有填充了对象apiname和数据id,
    //发出的消息才会跳转到数据详情页
    
    Fx.message.sendNotice( "标题",  "内容", ["1007"], "","")
    
    

### # 4\. throwErrorMessage 抛出异常信息，已知的确定的异常，主要作用为中断；在函数列表页面展示结果为成功；

> `Fx.message.throwErrorMessage()`

**Groovy 举例**
    
    
    Fx.message.throwErrorMessage(" 函数中断 ")
    
    

### # 5\. throwException 抛出异常信息，未知的不确定的异常，主要作用为抛错；在函数列表页面展示结果为失败；

> `Fx.message.throwException()`

**Groovy 举例**
    
    
    Fx.message.throwException(" 函数异常 ")
    
    

### # 6\. createTrustGroup 创建企信业务群

> `Fx.message.createTrustGroup(<String apiName>, <String dataId>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
apiName | String | 对象apiName | 是  
dataId | String | 对象数据Id | 是  
  
**Groovy 举例**
    
    
    def (Boolean error, Map data, String errorMessage) = Fx.message.createTrustGroup('object_94QeC__c', '5dae6f48a5083da25946e68c')
    if(error) {
        log.info(errorMessage)
    } else {
        log.info(data)
    }
    
    

**注意事项**

>   * 使用该函数时需到管理后台的企信管理中开启该对象的业务群功能并做好相关配置
> 


### # 7\. sendEmail 发送邮件

> `Fx.message.sendEmail(<List toList>, <String subject>, <String content>, <boolean useSystemSend>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
toList | List[String] | 收件人邮箱地址列表 | 是  
subject | String | 邮件主题 | 是  
content | String | 邮件正文 | 是  
useSystemSend | boolean | 是否用系统身份发送（传true应该是使用系统邮件地址去发件，传false的话是使用触发函数执行人员绑定的纷享又邮件地址去发件） | 是  
  
出参格式

参数名称 | object | 描述  
---|---|---  
error | boolean | 是否执行异常  
data | object |   
errorMessage | String | 异常提示信息  
data | object | 描述  
---|---|---  
toList | List[String] | 收件人邮箱地址列表  
subject | String | 邮件主题  
content | String | 邮件正文  
  
出参样例
    
    
    {
      "error": false,
      "data": {
        "toList": ["admin01@fxiaoke.com"],
        "subject": "这是主题",
        "content": "这是正文"
      },
      "errorMessage": ""
    }
    
    

**Groovy 举例**
    
    
    // 邮件主题
    String subject = "Jaime Enrique Garcia Lopez, Senior Software Development Manager at Capital One"
    String content = "“At the time, no single team member knew Go, but within a month, everyone was writing in Go and we were building out the endpoints. It was the flexibility, how easy it was to use, and the really cool concept behind Go (how Go handles native concurrency, garbage collection, and of course safety+speed.) that helped engage us during the build. Also, who can beat that cute mascot!”"
    
    // 收件人邮箱
    List toList = ["admin01@fxiaoke.com"]
    // 使用系统邮箱发送
    boolean useSystemSend = true
    
    def(error, data, errorMessage) = Fx.message.sendEmail(toList, subject, content, true)
    
    if (error) {
      log.info(errorMessage)
    } else {
      log.info(data)
    }
    
    

### # 8\. sendEmail 发送邮件，支持抄送和密送

> `Fx.message.sendEmail(<EmailAttribute attribute>)`

**参数说明**

入参格式

参数名称 | object | 描述 | 是否必填  
---|---|---|---  
attribute | EmailAttribute | 邮件相关信息 | 是  
  
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
    
    
    // 邮件主题
    String subject = 'go1.22.3.windows-amd64.zip'
    String content = 'cab2af6951a6e2115824263f6df13ff069c47270f5788714fa1d776f7f60cb39'
    // 邮件附件
    // 对象附件字段值数据结构和邮件附件结构不同，需要如下转换
    
    // 获取数据上的附件字段
    def attachmentVaule = context.data.field_fCuoH__c
    // 邮件附件内容
    def attachments = []
    
    // 转换逻辑
    // emailAttachement ⇄ fieldValue
    // index ⇄ index
    // name ⇄ filename
    // fileId ⇄ path
    // size ⇄ size
    attachmentVaule.eachWithIndex { item, index ->
        attachments << [
                'index': index,
                'name': item['filename'],
                'fileId': item['path'],
                'size': item['size']
        ]
    }
    
    // 收件人邮箱
    List toList = ['admin01@fxiaoke.com']
    // 抄送人邮箱
    List ccList = ['admin02@fxiaoke.com']
    // 密送人邮箱
    List bccList = ['admin02@fxiaoke.com']
    // 使用系统邮箱发送
    boolean useSystemSend = false
    // 发件人地址（必须是后台管理配置过的系统邮箱）
    String sender = 'system@fxiaoke.com'
    
    EmailAttribute attribute = EmailAttribute.builder()
      .toList(toList)
      .ccList(ccList)
      .bccList(bccList)
      .subject(subject)
      .content(content)
      .sender(sender)
      .attachments(attachments)
      .useSystemSend(useSystemSend)
      .build()
    
    def(error, data, errorMessage) = Fx.message.sendEmail(attribute)
    
    if (error) {
        log.info(errorMessage)
    } else {
        log.info(data)
    }
    
    

**参考对象**

  * 参考EmailAttribute

  * 参考Email




**注意事项**

>   * 请注意 attachment 数据结构，不要直接把数据中的附件字段的值拿过来直接用，这是错误的。
>   * 具体转换逻辑参考样例。
> 


### # 9\. sendEmailByTemplate 使用邮件模板和数据发送邮件

> `Fx.message.sendEmailByTemplate(<String templateId>, <String objectId>, <String toList>, <boolean userSystemSend>)`

**参数说明**

入参格式

参数名称 | object | 描述 | 是否必填  
---|---|---|---  
templateId | String | 模板id | 是  
objectId | String | 对象数据id | 是  
toList | String[String] | 收件人邮箱地址列表 | 是  
userSystemSend | boolean | 是否使用系统邮箱地址（true：使用系统邮箱去发件，false：使用函数触发人员绑定的纷享邮箱地址去发件） | 是  
  
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
    
    
    // 邮件模版Id
    String templateId = "64fecf9677e6c00ba21ac99e"
    // 对象数据Id
    String dataId = "663dd7ea96f31400079c210e"
    // 收件人邮箱
    List toList = ["admin01@fxiaoke.com"]
    // 使用系统邮箱发送
    boolean useSystemSend = true
    
    def (error, data, errorMessage) = Fx.message.sendEmailByTemplate(templateId, dataId, toList, useSystemSend)
    
    if(error){
      log.info(errorMessage)
    } else {
      log.info(data)
    }
    
    

### # 10\. sendEmailByTemplate 使用邮件模板和数据发送邮件，支持抄送和密送

> `Fx.message.sendEmailByTemplate(<EmailAttribute attribute>)`

**参数说明**

入参格式

参数名称 | object | 描述 | 是否必填  
---|---|---|---  
attribute | EmailAttribute | 邮件相关信息 | 是  
  
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
    
    
    // 邮件模版Id
    String templateId = "64fecf9677e6c00ba21ac99e"
    // 对象数据Id
    String dataId = "663dd7ea96f31400079c210e"
    // 邮件附件
    Map attachment = [
      "index": 0,
      "name": "go1.22.3.windows-amd64.zip",
      "fileId": "N_202409_12_e18599a6fc724e9e8502a94d0a5775cd.zip",
      "size": 76246156
    ]
    // 邮件附件
    // 对象附件字段值数据结构和邮件附件结构不同，需要如下转换
    
    // 获取数据上的附件字段
    def attachmentVaule = context.data.field_fCuoH__c
    // 邮件附件内容
    def attachments = []
    
    // 转换逻辑
    // emailAttachement ⇄ fieldValue
    // index ⇄ index
    // name ⇄ filename
    // fileId ⇄ path
    // size ⇄ size
    attachmentVaule.eachWithIndex { item, index ->
        attachments << [
                'index': index,
                'name': item['filename'],
                'fileId': item['path'],
                'size': item['size']
        ]
    }
    
    // 收件人邮箱
    List toList = ["admin01@fxiaoke.com"]
    // 抄送人邮箱
    List ccList = ["admin02@fxiaoke.com"]
    // 密送人邮箱
    List bccList = ["admin02@fxiaoke.com"]
    // 使用系统邮箱发送
    boolean useSystemSend = true
    
    EmailAttribute attribute = EmailAttribute.builder()
      .toList(toList)
      .ccList(ccList)
      .bccList(bccList)
      .templateId(templateId)
      .objectId(dataId)
      .attachments(attachments)
      .useSystemSend(useSystemSend)
      .build();
    
    def (error, data, errorMessage) = Fx.message.sendEmailByTemplate(attribute)
    
    if(error){
      log.info(errorMessage)
    } else {
      log.info(data)
    }
    
    

**参考对象**

  * 参考EmailAttribute

  * 参考Email




**注意事项**

>   * 请注意 attachment 数据结构，不要直接把数据中的附件字段的值拿过来直接用，这是错误的。
>   * 具体转换逻辑参考样例。
> 


### # 11\. sendIMMessage 通用企信IM发送消息接口

> `Fx.message.sendIMMessage(<String sessionId>, <String messageType>, <String messageContent>, <Integer env>, <String employeeId>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
sessionId | String | 需要发送到的会话id, 操作者企业需要有这个会话，并且非系统操作者需要在群内 | 是  
messageType | String | 消息类型，常用消息类型，文本：T，图片：I，图文：MIX，文件：D，高级文本：AT，通用模板消息：UGT | 是  
messageContent | String | 消息内容，文本为字符串，其他为对应的json格式，可以参考企信已经存在的消息格式 | 是  
env | Integer | 是否互联，0：企业内，1：互联 | 是  
employeeId | String | 发送者信息，格式 E.企业账号.员工id | 是  
  
**Groovy 举例**
    
    
    String content = "大家好"
    String employeeId = "E.78810.1004"
    def(boolean error, Map data, String message) = Fx.message.sendIMMessage("d5a3f0ba6dff4c488069efdd6d00a747", "T", content, 0, employeeId)
    if (error) {
      log.info("error: " + message)
    } else {
      log.info(data)
    }
    
    

## # 参考类 com.fxiaoke.functions.model.Channel

### # 字段说明

参数名称 | object | 描述  
---|---|---  
  
### # 1\. Service 企信服务号通道

> `Channel.Service()`

**Groovy 举例**
    
    
    Channel channel = Channel.Service("appiD") //发送服务号
    
    

**负责人：斯作益seth**

### # 2\. ObjectSession 客群通道

> `Channel.ObjectSession()`

**Groovy 举例**
    
    
    Channel channel = Channel.ObjectSession("AccountObj", "61848edfd9007e00019ee222") //发送客群
    
    

**负责人：斯作益seth**

## # 参考类 com.fxiaoke.functions.model.EmailAttribute

### # 字段说明

参数名称 | object | 描述  
---|---|---  
useSystemSend | java.lang.Boolean | 是否用系统身份发送（传true应该是使用系统邮箱去发件，传false的话是使用函数触发人员绑定的纷享邮箱去发件），默认为true  
attachments | java.util.List | 附件  
sender | java.lang.String | 指定发送人邮箱（必须是后台邮件管理配置过的系统邮箱）  
subject | java.lang.String | 邮箱题目  
bccList | java.util.List | 密送邮箱列表  
ccList | java.util.List | 抄送邮箱列表  
attachmentZipList | java.util.List | 附件下载链接  
toList | java.util.List | 接收人邮箱列表  
templateId | java.lang.String | 模板id  
objectId | java.lang.String | 对象数据id  
content | java.lang.String | 邮箱正文  
  
## # 参考类 com.facishare.function.impl.dto.SendEmail.Email

### # 字段说明

参数名称 | object | 描述  
---|---|---  
toList | array[String] |   
subject | String | 邮件主题  
content | String | 邮件正文  
sender | String | 指定发件人邮箱（必须是后台邮件管理配置过的系统邮箱）  
ccList | List[String] | 抄送人地址列表  
bccList | List[String] | 密送人地址列表  
attachments | List[Object] | 附件列表  
attachmentZipList | List[Object] | 附件地址列表  
crmObjApiName | String | 绑定的对象，邮箱那边做记录用  
crmObjDataId | String | 绑定的数据，邮箱那边做记录用  
  
字段样例
    
    
    {
      "toList": [
        "admin01@fxiaoke.com"
      ],
      "subject": "subject_570f35483d97",
      "content": "content_ab8286a1a8ff",
      "sender": "sender_eeeaaca45e0c",
      "ccList": [
        "admin02@fxiaoke.com"
      ],
      "bccList": [
        "admin03@fxiaoke.com"
      ],
      "attachments": [
        {}
      ],
      "attachmentZipList": [
        {}
      ],
      "crmObjApiName": "crmObjApiName_52b29fd536de",
      "crmObjDataId": "crmObjDataId_4999c93ed3dd"
    }
    
    

[Fx.location](../LocationAPI/) [Fx.file](../FileAPI/)

← [Fx.location](../LocationAPI/) [Fx.file](../FileAPI/)→ 

  * 跟随系统 
  * 浅色模式 
  * 深色模式 
  * 阅读模式 


