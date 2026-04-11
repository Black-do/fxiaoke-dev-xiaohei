#  Fx.file

## # Fx.file

### # 1\. uploadFile 文件上传

> `Fx.file.uploadFile(<String extensionName>, <Integer fileSize>, <byte[] fileBytes>, <Integer userId>)`

**参数说明**

入参格式

参数名称 | object | 描述 | 是否必填  
---|---|---|---  
extensionName | String | 拓展名 | 是  
fileSize | Integer | 文件大小 | 是  
fileBytes | byte[] | 文件内容byte数组 | 是  
userId | Integer | 用户名 | \--  
  
出参格式

参数名称 | APIResult | 描述  
---|---|---  
isError | Boolean | 是否错误  
data | Map |   
message | String | 信息  
data | Map | 描述  
---|---|---  
extensionName | String | 拓展名  
path | String | NPath  
size | Integer | 文件大小  
  
出参样例
    
    
    {
        "isError": false,
        "data": {
            "extensionName": ".xlsx",
            "path": "N_202411_11_f20d33d4520e49738be560448001b451",
            "size": 25
        },
        "message": ""
    }
    
    

**Groovy 举例**
    
    
    def text = "aaa" as String
    def byteData = Strings.toUTF8Bytes(text)
    def ret = Fx.file.uploadFile(".txt", byteData.size(), byteData, 1000)
    def data = ret.data
    log.info(data)
    log.info(data['path'])
    log.info(data['size'])
    log.info(data['extensionName'])
    
    

**注意事项**

>   * 该接口对结果处理时，要使用def来接收，且不能as Map
> 


### # 2\. uploadFileByStream 把外部接口的文件上传

> `Fx.file.uploadFileByStream(<Request request>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
request | Request | 请求体 | 是  
  
出参格式

参数名称 | APIResult | 描述  
---|---|---  
isError | Boolean | 是否错误  
data | Map |   
message | String | 信息  
data | Map | 描述  
---|---|---  
extensionName | String | 拓展名  
fileName | String | 文件名  
path | String | NPath  
size | Integer | 文件大小  
  
出参样例
    
    
    {
        "isError": false,
        "data": {
            "extensionName": ".xlsx",
            "fileName": "123tom.xlsx",
            "path": "N_202411_11_f20d33d4520e49738be560448001b451",
            "size": 25
        },
        "message": ""
    }
    
    

**Groovy 举例**
    
    
    Map map = ["id": "123", "name": "tom"]
    StringBody body = StringBody.builder().content(map).build()
    
    Request request = Request.builder()
    .method("POST")
    .url('http://www.baidu.com/image/download')
    .timeout(7000)
    .retryCount(0)
    .header("Content-Type", "application/json")
    .body(body)
    .build()
    
    def res = Fx.file.uploadFileByStream(request)
    log.info(res.data)
    //path=N_202411_11_8ae08f8997c84e1f984bf7515ad6a1be, size=25, extensionName=.xlsx, fileName=123tom.xlsx
    
    

**参考对象**

  * 参考Request



**注意事项**

>   * 如果对方返回header中包含Content-Length，包含文件的大小，通过文件流处理不会进行文件大小校验；如果不包含则会校验文件大小，不可超过5m；
>   * .header('Transfer-Encoding', 'gzip').header('Accept-Encoding','identity') --增加这两个header部分场景对方服务header会返回Content-Length
> 


### # 3\. downloadFile 文件下载返回byte[]

> `Fx.file.downloadFile(<String path>)`

**参数说明**

入参格式

参数名称 | object | 描述 | 是否必填  
---|---|---|---  
path | String | Npath | 是  
  
出参格式

参数名称 | APIResult | 描述  
---|---|---  
isError | Boolean | 是否错误  
data | FileDownloadData |   
message | String | 信息  
data | FileDownloadData | 描述  
---|---|---  
extensionName | String | 拓展名  
fileName | String | 文件名  
fileData | byte[] | 文件内容  
fileSize | Integer | 文件大小  
  
出参样例
    
    
    {
        "isError": false,
        "data": {
            "extensionName": ".xlsx",
            "fileName": "123tom.xlsx",
            "fileSize": 25
        },
        "message": ""
    }
    
    

**Groovy 举例**
    
    
    def ret = Fx.file.downloadFile("N_202007_12_001731386ccf40698523c39744b0161c")
    def fileDowloadData = ret[1]
    def fileData = fileDowloadData['fileData'] as byte[]
    def str = Strings.toUTF8String(fileData) as String
    
    

**参考对象**

  * 参考FileDownloadData



**注意事项**

>   * 下载文件有10m限制
> 


### # 4\. downloadStream 文件下载返回InputStream

> `Fx.file.downloadStream(<String path>)`

**参数说明**

入参格式

参数名称 | object | 描述 | 是否必填  
---|---|---|---  
path | String | Npath | 是  
  
出参格式

参数名称 | APIResult | 描述  
---|---|---  
isError | Boolean | 是否错误  
data | FileDownloadData |   
message | String | 信息  
data | FileDownloadData | 描述  
---|---|---  
extensionName | String | 拓展名  
fileName | String | 文件名  
inputStream | InputStream | 文件流  
fileSize | Integer | 文件大小  
  
出参样例
    
    
    {
        "isError": false,
        "data": {
            "extensionName": ".xlsx",
            "fileName": "123tom.xlsx",
            "fileSize": 25
        },
        "message": ""
    }
    
    

**Groovy 举例**
    
    
    def(Boolean err, Object fileData, String msg) = Fx.file.downloadStream("N_202111_29_6eb71dca766944c582b87e6a5213f3a3.docx")
    if (err) {
      log.info("downloadStream error :" + msg)
    } else {
      log.info("file data :" + fileData)
    }
    InputStream inputStream = fileData['inputStream'] as InputStream
    log.info(fileData)
    
    

**参考对象**

  * 参考FileDownloadData



### # 5\. packedFile 将文件列表的文件打包为一个压缩包并返回下载地址码

> `Fx.file.packedFile(<List files>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
files | List | 文件path列表 | 是  
  
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
    
    
    List files = [
         [
             "Name":"888.jpg",
             "Path":"N_202201_24_db48abc2723d4d978f240f0fb9bf35ac.webp"
         ]
    ]
    def (Boolean error, Map data, String message) = Fx.file.packedFile(files)
    if (error) {
      log.info("error :" + message)
    } else {
      log.info(data)
    }
    
    

**注意事项**

>   * 返回的数据类型: Map {"status":0, "token":"xxxxx"}, status为0表示成功，token为下载地址码, status为1表示超时，没有生成下载地址码
> 


### # 6\. packedFile 文件打包发送给指定用户

> `Fx.file.packedFile(<List files>, <List userIds>)`

**参数说明**

入参格式

参数名称 | object | 描述 | 是否必填  
---|---|---|---  
files | List[string] | 文件列表 | 是  
userIds | List[string] | 发送用户列表 | 是  
  
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
    
    
    //定义需要打包发送的文件，参数分别为：打包后的文件名、对象下的文件路径（通过find函数可查询到）、文件后缀、文件打包后的包内存放路径
    UserFile file = UserFile.of("文件1","N_201907_31_57a33fb0c999447bb93fa1e4cc6e649d","jpg","/image")
    List packFileList = []
    packFileList.add(file)
    //把fileList中的文件打包后，通过人员id参数发送给指定人
    final APIResult result = Fx.file.packedFile(packFileList, Lists.newArrayList("1000"));
    
    

### # 7\. createFileShareTokens 无权限文件下载，获取文件下载token

> `Fx.file.createFileShareTokens(<List paths>, <String expireMinute>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
paths | List[string] | 文件nPath列表 | 是  
expireMinute | String | 过期时间，以分钟为单位,最大支持15分钟 | 是  
  
出参格式

参数名称 | APIResult | 描述  
---|---|---  
isError | Boolean | 是否错误  
data | object | 响应数据  
message | String | 消息  
  
出参样例
    
    
    {
        "isError": false,
        "data": {
            
        },
        "message": "success"
    }
    
    

**Groovy 举例**
    
    
    //获取无权限文件的shareToken
    List paths = ['N_202102_03_54c5ede542154b748c6f9381d96a1956']
    //获取无权限文件的shareToken
    def(boolean error, Map data, String  errorMessage)  = Fx.file.createFileShareTokens(5, paths)
    if (error) {
        log.info(errorMessage)
    } else {
        log.info(data)
    }
    //获取到shareToken后用下列链接下载文件：
    //http://www.fxiaoke.com/FSC/N/FileShare/DownloadFileBySharedTokenV2?sharedToken=6AA905C78D85C91D796261356AF7467E53719536C4515B3328F7D65FC8476DC777DE783881DF4588EB6B9F0AEEF0F46060EA5D49185941B59C4531F5967FA07B7424EDF8BF20F11F6AE89573CF7F96735EC0284E1F637AE3&name=111.jpg
    
    

### # 8\. getPresignedUrl 获取附件预签名url（仅文件专属企业可用）

> `Fx.file.getPresignedUrl(<List paths>, <Integer expire>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
paths | List[string] | 文件path集合 | 是  
expire | Integer | 过期时间(秒) | 是  
  
出参格式

参数名称 | APIResult | 描述  
---|---|---  
isError | Boolean | 是否错误  
data | array[object] | 响应数据  
message | String | 消息  
data | object | 描述  
---|---|---  
path | String | 文件路径  
url | String | 文件的URL  
  
出参样例
    
    
    {
        "isError": false,
        "data": [
            {
                "path": "N_202410_22_a981ae9fe95c43bea8ee8aaebc0c9490.pdf",
                "url": ""
            }
        ],
        "message": ""
    }
    
    

**Groovy 举例**
    
    
    List npaths = ["N_202207_06_2b51df0dd11043ee9c0ad341742f95bb"]
    int expire = 100
    def(boolean error, List data, String message) = Fx.file.getPresignedUrl(npaths, expire)
    if (error) {
      log.info("error: " + message)
    } else {
      log.info(data)
    }
    
    

**注意事项**

>   * 无需携带后缀
> 


### # 9\. convertPath 转换为无权限npath

> `Fx.file.convertPath(<String path>, <String extension_name>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
path | String | 文件的路径 | 是  
extension_name | String | 文件的扩展名 | 是  
  
出参格式

参数名称 | APIResult | 描述  
---|---|---  
isError | Boolean | 是否错误  
data | array[object] | 响应数据  
message | String | 消息  
data | object | 描述  
---|---|---  
path | 文件路径 | 文件的路径  
extension_name | 文件扩展名 | 文件的扩展名  
  
出参样例
    
    
    {
        "isError": false,
        "data": [
            {
                "path": "N_202411_05_3df5da66c3d548a48792d75ed4bc7582",
                "extension_name": "pdf"
            }
        ],
        "message": ""
    }
    
    

**Groovy 举例**
    
    
    def (Boolean error, Map data, String message) = Fx.file.convertPath("N_202208_01_3628e0ba470b4086aa04dd8f3e93ed5a")
    if (error) {
      log.info("error :" + message)
    } else {
      log.info(data)
    }
    
    

**注意事项**

>   * 用户需要对输入的Npath对应的文件有权限
> 


### # 10\. wordToPdf 将纷享上的word文件转成pdf

> `Fx.file.wordToPdf(<String npath>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
npath | String | 文件npath | 是  
  
出参格式

参数名称 | APIResult | 描述  
---|---|---  
isError | Boolean | 指示是否发生错误  
data | List | 响应数据  
message | String | 信息  
data | List | 响应数据  
---|---|---  
pageCount | Integer | 页面数量  
employeeId | Integer | 员工ID  
ea | Integer | ea  
npaths | List[String] | npath List  
fileType | String | 文件类型  
  
出参样例
    
    
    {
        "isError": false,
        "data": {
            "pageCount": 1,
            "employeeId": -10000,
            "ea": 90325,
            "npaths": [
                "TN_c50f77531989492aba2765f2247371d5"
            ],
            "fileType": "pdf"
        },
        "message": "操作成功"
    }
    
    

**Groovy 举例**
    
    
    // 文件的NPath需要加上后缀名，新板文件NPath都是自带后缀的就不要再补了，老的NPath不带后缀名，需要拼上后缀
    def (Boolean error, Map data, String message) = Fx.file.wordToPdf("N_202303_08_e11c1c5bb1c0486d83c5a6ece65a902f.docx")
    if (error) {
      log.info("error :" + message)
    } else {
      log.info(data)
    }
    
    

**注意事项**

>   * 用户需对文件有权限
> 


### # 11\. getPdfMetaInfo 获取PDF文件的页码

> `Fx.file.getPdfMetaInfo(<String npath>)`

**参数说明**

入参格式

参数名称 | String | 描述 | 是否必填  
---|---|---|---  
npath | String | 文件path,支持A、N、TA、TN文件Path,必须携带扩展名 | 是  
  
出参格式

参数名称 | APIResult | 描述  
---|---|---  
isError | Boolean | 是否错误  
data | object | 响应数据  
message | String | 消息  
data | object | 响应数据  
---|---|---  
pageCount | Integer | 页面数量  
employeeId | Integer | 员工ID  
  
出参样例
    
    
    {
        "isError": false,
        "data": {
            "pageCount": 8,
            "employeeId": 0
        },
        "message": ""
    }
    
    

**Groovy 举例**
    
    
    String npath ="N_202211_22_42918a541aed45038f3ab7cfdfb99aeb.pdf";
    def(boolean error, Map data, String message) = Fx.file.getPdfMetaInfo(npath);
    Integer pageCount = 0
    if(error){
      log.info("error:"+message);
    }else{
      log.info("PDF文档信息："+data);
      pageCount = (Integer) data.pageCount;
      log.info("PDF文档页码：" + pageCount);
    }
    
    

### # 12\. mergerPdf 按集合的顺序追加合并PDF

> `Fx.file.mergerPdf(<List npaths>, <String documentType>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
npaths | List[string] | 要合并的文件npaths | 是  
documentType | String | 要合并的文件类型后缀（不加.) | 是  
  
出参格式

参数名称 | APIResponse | 描述  
---|---|---  
isError | Boolean | 指示请求是否发生错误  
data | object | 响应数据  
message | String | 请求结果信息  
data | object | 响应数据  
---|---|---  
employeeId | Integer | 员工id  
ea | Integer | 企业account  
npaths | List[string] | npath集合  
fileType | String | 文件的类型  
  
出参样例
    
    
    {
        "isError": false,
        "data": {
            "employeeId": 1000,
            "ea": 90325,
            "npaths": [
                "TN_fcdc479583414586a36fde4a6c2fed9a"
            ],
            "fileType": "pdf"
        },
        "message": "success"
    }
    
    

**Groovy 举例**
    
    
    List<String>npaths = Lists.newArrayList(
      "N_202410_21_093c72730bdd41e1b02d98510729330b.pdf",
      "N_202410_22_a981ae9fe95c43bea8ee8aaebc0c9490.pdf"
    )
    String documentType="pdf";
    def (boolean error, Map data, String message) = Fx.file.mergerPdf(npaths, documentType);
    if(error) {
      log.info("error:"+message);
    } else {
      log.info("合并后文件的信息："+data);
      List mergerNpaths = data.npaths as List;
      String masterNpath = mergerNpaths[0];
      log.info("合并后的PDF文件path:"+ masterNpath);
    }
    
    

### # 13\. getBigFilePresignedUrl 获取大文件签名url

> `Fx.file.getBigFilePresignedUrl(<String filePath>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
filePath | String | 大文件ALI_OSS Path | 是  
  
出参格式

参数名称 | APIResult | 描述  
---|---|---  
isError | Boolean | 指示请求是否发生错误  
data | object | 返回的数据  
message | Message | 请求结果信息  
data | object | 返回的数据  
---|---|---  
url | String | 文件的下载链接  
  
出参样例
    
    
    {
        "isError": false,
        "data": {
            "url": ""
        },
        "message": "请求成功，文件可下载"
    }
    
    

**Groovy 举例**
    
    
    def (Boolean error, Map data, String message) = Fx.file.getBigFilePresignedUrl("ALIOSS_851a3c46b81f4adaba45c2965892dd09")
    if (error) {
      log.info("error :" + message)
    } else {
      log.info(data)
    }
    
    

**注意事项**

>   * 注意区分大文件和普通文件，大文件是以 ALIOSS_ 开头的文件！！！
> 


### # 14\. generateQRCode 将文本生成二维码或者条形码，并以Cpath或Npath的形式返回

> `Fx.file.generateQRCode(<string content>, <String fileName>, <Integer size>, <Boolean encode>, <Boolean needCdn>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
content | string | 需要转换为QRCode的内容,非空 | 是  
fileName | String | 下载时默认的源文件名称,默认为QRCode | 是  
size | Integer | 图片大小,默认为400 | 是  
encode | Boolean | content是否使用base64编码,默认为false,使用URL编码 | 是  
needCdn | Boolean | 是否需要CDN加速,如果为true返回Cpath,默认为false返回Npath | 是  
  
出参格式

参数名称 | APIResult | 描述  
---|---|---  
isError | boolean | 指示请求是否出错，false表示请求成功  
data | object | 包含请求返回的主要数据  
message | string | 请求的结果消息，通常用于提示用户  
data | object | 包含请求返回的主要数据  
---|---|---  
encode | boolean | 指示内容是否使用base64编码，false表示使用URL编码  
path | string | 生成的二维码或条形码图片 path  
fileName | string | 下载时默认的源文件名称，默认为QRCode  
needCdn | boolean | 指示是否需要CDN加速，true表示需要  
size | string | 二维码或条形码的大小  
employeeId | integer | 员工id  
ea | integer | ea  
content | string | 转换为二维码或条形码的内容  
  
出参样例
    
    
    {
        "isError": false,
        "data": {
            "encode": false,
            "path": "N_202411_05_c71f3e81b6344eb9a823d10cbe3fe554",
            "fileName": "QRCode",
            "needCdn": false,
            "size": "400*400",
            "employeeId": 1000,
            "ea": 90325,
            "content": "http://weixin.qq.com/q/02Z6nOpuoT8__1jyGaNA1Q"
        },
        "message": "请求成功，文件可下载"
    }
    
    

**Groovy 举例**
    
    
    // 需要转换的QRCode的内容（非空）
    String content = "http%3A%2F%2Fweixin.qq.com%2Fq%2F02Z6nOpuoT8__1jyGaNA1Q";
    // 生成QRCode Image后,使用Npath或Cpath,通过文件服务下载时默认生成的保存文件名 默认QRcode
    String fileName = "QRCode";
    // 生成的图片的大小, 默认400.
    Integer size=400;
    // 是否使用Base64对content内容进行了编码,默认false(URL 编码)
    // 为什么需要编码？ 一些特殊符号,会导致请求失败或者在生成QRCode时失败
    boolean encode = false;
    // 是否需要CDN加速？ true 返回Cpath 默认false 返回Npath
    boolean needCdn = false;
    def(boolean error, Map data, String message) = Fx.file.generateQRCode(content, fileName, size, encode, needCdn);
    if (error) {
      log.info("error:" + message)
    } else {
      log.info("data:" + data)
    }
    
    

**注意事项**

>   *     1. 注意encode是true还是false
>   *     2. 如果您有创建条形码的需求，请使用 【Fx.file.generateBarCode】 这个函数， 当前函数只能生成二维码（待下线）， generateBarCode 可生成二维码或条形码，建议您使用新函数。
> 


### # 15\. asyncPackageFile 异步批量打包文件，发送CRM通知给操作人和需要通知的用户

> `Fx.file.asyncPackageFile(<List notifies>, <Map queryParam>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
notifies | List[object] | 通知用户的 userId集合 | 是  
queryParam | Map | 打包参数 | 是  
notifies | object | 描述 | 是否必填  
---|---|---|---  
userId | String | 用户Id | 是  
queryParam | Map | 打包参数 | 是否必填  
---|---|---|---  
documents | List | 打包文件的信息 | 是  
skipDuplicatedFile | Boolean | 是否跳过重复的文件， true:跳过，false：保留重复文件 | 是  
securityGroup | String | 文件的安全组，如果是网盘文件，需带上XiaoKeNetDisk | \--  
fileName | 文件名 | 打包文件的名称,需带.zip 后缀 | 是  
documents | List | 打包文件的信息 | 是否必填  
---|---|---|---  
files | List[object] | 文件信息List | 是  
files | object | 描述 | 是否必填  
---|---|---|---  
Name | String | 文件的完整名称，需带文件后缀 | 是  
Path | String | Npath | 是  
  
出参格式

参数名称 | APIResult | 描述  
---|---|---  
isError | boolean | 是否错误  
data | Map | 返回的任务数据  
errorMessage | string | 信息  
data | Map | 返回的任务数据  
---|---|---  
id | string | 任务ID  
status | integer | 任务状态，0 表示任务提交成功  
  
出参样例
    
    
    {
        "isError": false,
        "data": {
            "id": "67385e8385210a0007797c74",
            "status": 0
        },
        "message": ""
    }
    
    

**Groovy 举例**
    
    
    List notifies = [
        [userId: "1000"],
        [userId: "1002"]
    ]
    Map queryParam = [
        documents: [
            files: [
                [
                    Name: "青浦.zip",
                    Path: "N_202410_15_c545828e983e4c20aabd5aba8510ebae.zip"
                ]
            ]
        ],
        skipDuplicatedFile : false,
        securityGroup: "XiaoKeNetDisk",
        fileName: "打包文件测试.zip"
    ]
    
    
    def (Boolean error, Map data, String errorMessage) = Fx.biz.callAPI("Fx.file.asyncPackageFile",notifies,queryParam)
    if (error) {
      log.info("error :" + message)
    } else {
      log.info(data.status)
      log.info(message)
      log.info(error)
    }
    
    

**注意事项**

>   *     1. 下载网盘文件需设置参数 securityGroup: "XiaoKeNetDisk"
>   *     2. 自定义下载文件名需加.zip后缀
>   *     3. 必选参数必须携带！！
> 


### # 16\. 将文本生成二维码或者条形码，并以Cpath或Npath的形式返回

> `Fx.file.generateBarCode(<string content>, <String fileName>, <String size>, <Boolean encode>, <Boolean needCdn>, <String codeModel>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
content | string | 需要转换为Code的内容,非空 | 是  
fileName | String | 下载时默认的源文件名称 | 是  
size | String | 生成的图片的大小,单位:像素;如果是二维码,参数设置如400 _400(数字之间用“_ ”间隔),二维码最大限制为700 _700,最小限制宽高皆为0,推荐400_ 400,尽量保持宽高大小一致;如果是条形码,不需要输入,默认450*150. | 是  
encode | Boolean | content是否使用base64编码,默认为false,使用URL编码 | 是  
needCdn | Boolean | 是否需要CDN加速,如果为true返回Cpath,默认为false返回Npath | 是  
codeModel | String | 所需二维码的类型,BarCode 条形码,QRCode 二维码，此值必填，无默认类型，如果不选择会报错. | 是  
  
出参格式

参数名称 | APIResult | 描述  
---|---|---  
isError | boolean | 指示请求是否出错，false表示请求成功  
data | object | 包含请求返回的主要数据  
message | string | 请求的结果消息，通常用于提示用户  
data | object | 包含请求返回的主要数据  
---|---|---  
encode | boolean | 指示内容是否使用base64编码，false表示使用URL编码  
path | string | 生成的二维码或条形码图片 path  
fileName | string | 下载时默认的源文件名称，默认为QRCode  
needCdn | boolean | 指示是否需要CDN加速，true表示需要  
size | string | 二维码或条形码的大小  
employeeId | integer | 员工id  
ea | integer | ea  
content | string | 转换为二维码或条形码的内容  
  
出参样例
    
    
    {
        "isError": false,
        "data": {
            "encode": false,
            "path": "N_202411_05_c71f3e81b6344eb9a823d10cbe3fe554",
            "fileName": "QRCode",
            "needCdn": false,
            "size": "400*400",
            "employeeId": 1000,
            "ea": 90325,
            "content": "http://weixin.qq.com/q/02Z6nOpuoT8__1jyGaNA1Q"
        },
        "message": "请求成功，文件可下载"
    }
    
    

**Groovy 举例**
    
    
    // 需要转换的QRCode的内容，如果您选择的是条形码(BarCode),那么限定内容大小100字符.（非空）
    String content = "http%3A%2F%2Fweixin.qq.com%2Fq%2F02Z6nOpuoT8__1jyGaNA1Q";
    // 生成QRCode Image后,使用Npath或Cpath,通过文件服务下载时默认生成的保存文件名 默认QRcode
    String fileName = "QRCode";
    // 生成的图片的大小,单位:像素;如果是二维码,参数设置如400*400(数字之间用“*”间隔),二维码最大限制为700*700,最小限制宽高皆为0,推荐400*400,尽量保持宽高大小一致;如果是条形码,不需要输入,默认450*150.
    String size="400*400";
    // 是否使用Base64对content内容进行了编码,默认false(URL 编码)
    // 为什么需要编码？ 一些特殊符号,会导致请求失败或者在生成QRCode时失败
    boolean encode = false;
    // 是否需要CDN加速？ true 返回Cpath 默认false 返回Npath
    boolean needCdn = false;
    // 所需二维码的类型,BarCode 条形码,QRCode 二维码，此值必填，无默认类型，如果不选择会报错.
    String codeModel="QRCode";
    def(boolean error, Map data, String message) = Fx.biz.callAPI("Fx.file.generateBarCode",content, fileName, size, encode, needCdn, codeModel);
    if (error) {
      log.info("error:" + message)
    } else {
      log.info("data:" + data)
    }
    
    

**注意事项**

>   * 注意encode是true还是false
> 


### # 17\. 通过大附件path删除大附件

> `Fx.file.deleteBigFile(<string path>)`

**参数说明**

入参格式

参数名称 | String | 描述 | 是否必填  
---|---|---|---  
path | string | 大附件path | 是  
  
出参格式

参数名称 | object | 描述  
---|---|---  
code | integer | 表示请求处理状态  
data | 类型 | 请求返回数据  
success | boolean | 是否成功  
message | string | 请求处理信息  
  
出参样例
    
    
    {
        "code": 200,
        "data": true,
        "success": true,
        "message": "请求成功"
    }
    
    

**Groovy 举例**
    
    
    String path= "ALIOSS_338bdf957ef64507b457168c821d4f72"
    def (Boolean error, Map data, String errorMessage) = Fx.biz.callAPI("Fx.file.deleteBigFile", path)
    if (error) {
      log.info("error :" + message)
    } else {
      log.info(data)
    }
    
    

**注意事项**

>   * 删除后文件将无法访问
> 


### # 18\. 查询异步打包任务状态

> `Fx.file.queryBatchStatus(<string jobId>)`

**参数说明**

入参格式

参数名称 | object | 描述 | 是否必填  
---|---|---|---  
jobId | string | 任务Id | 是  
  
出参格式

参数名称 | object | 描述  
---|---|---  
id | string | jobId  
fileExt | string | 文件扩展名，例如 zip  
url | string | 文件的完整 下载URL 地址(base64加密)  
status | integer | 状态码，表示任务的状态  
  
出参样例
    
    
    {
      "id": "jobId",
      "fileExt": "zip",
      "url": "base64 加密后的下载url",
      "status": 2
    }
    
    

**Groovy 举例**
    
    
    def (Boolean error, Map data, String errorMessage) = Fx.biz.callAPI("Fx.file.queryBatchStatus", "yourJobId")
    if (error) {
      log.info("error :" + message)
    } else {
      log.info(data)
    }
    
    

**注意事项**

>   * 状态码 | 状态名称（中文）
>   * \------|-------------
>   * 0 | 等待中
>   * 1 | 运行中
>   * 2 | 成功
>   * 3 | 失败
>   * 4 | 错误
>   * 5 | 取消中
>   * 6 | 已取消
>   * 7 | 请求取消
>   * 8 | 未知状态
>   *   *   * 只能查询Fx.file.asyncPackageFile返回的JobId
> 


### # 18\. 解析excel，通过consumer自定义处理逻辑

> `Fx.file.parseExcel(<String nPath>, <String sheet>, <Integer startRow>, <Consumer<Map> consumer>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
nPath | String | 文件npath | 是  
sheet | String | sheet名称，不匹配则不会处理 | 是  
startRow | Integer | <=0都为0处理，0代表标题行，以此往后推算行数，传null默认为1 | 是  
consumer | `Consumer<Map>` | 自定义处理逻辑 | 是  
  
出参格式

参数名称 | APIResult | 描述  
---|---|---  
error | Boolean | 是否错误  
data | Map | 返回的数据  
message | String | 信息  
  
出参样例
    
    
    {
        "isError": false,
        "data": {},
        "message": ""
    }
    
    

**Groovy 举例**
    
    
    String npath = "N_202408_05_4210a63c2d5440809b4fad72884f3ef6.xlsx"
    String sheet = "Sheet1"
    Integer startRow = 0
    def ret = Fx.file.parseExcel(npath, sheet, startRow, { e ->
         Fx.object.create("object_1yO4J__c", e, , CreateAttribute.builder().build()).result()
    })
    log.info(ret)
    
    

**注意事项**

>   * 不支持大附件
> 


**负责人：斯作益seth**

## # 参考类 com.fxiaoke.functions.http.Request

### # 字段说明

参数名称 | object | 描述  
---|---|---  
headers | `java.util.Map<java.lang.String,java.util.List<java.lang.String>>` | 请求的header  
method | java.lang.String | 请求的方法POST/GET/PUT...  
retryCount | java.lang.Integer | 重试次数，0表示不重试，最大3次重试  
insecure | java.lang.Boolean | 是否绕过SSl验证，默认为false，不绕过SSL  
body | com.fxiaoke.functions.http.RequestBody | 请求的body  
timeout | java.lang.Integer | 超时时间，最大120s  
url | java.lang.String | 请求的url地址  
  
## # 参考类 com.fxiaoke.functions.model.FileDownloadData

### # 字段说明

参数名称 | object | 描述  
---|---|---  
extensionName | java.lang.String | 文件拓展名  
fileName | java.lang.String | 文件名  
fileSize | long | 文件大小  
fileData | byte[] | 文件byte数组  
  
[Fx.message](../MessageAPI/) [Fx.function](../FunctionAPI/)

← [Fx.message](../MessageAPI/) [Fx.function](../FunctionAPI/)→ 

  * 跟随系统 
  * 浅色模式 
  * 深色模式 
  * 阅读模式 


