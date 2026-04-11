#  Fx.http

## # Fx.http

### # 1\. execute HTTP请求，通过构造Request请求

> `Fx.http.execute(<Request request>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
request | Request | 请求体 | 是  
  
**Groovy 举例**
    
    
    //一共4种body构建方式，根据场景选择具体的构建方式
    
    //方式一、application/json 的body请求格式，标准的json格式
    Map map = ["a": 1, "b": 2]
    StringBody body = StringBody.builder().content(map).build()
    
    
    //方式二、multipart/form-data 的body请求格式，可以用来传输文件
    
    // 先下载文件的InputStream调用第三方接口上传到客户系统
    // def(Boolean err, Object fileData, String msg) = Fx.file.downloadStream("N_202111_29_6eb71dca766944c582b87e6a5213f3a3.docx")
    // if (err) {
    //   log.info("downloadStream error :" + msg)
    //   Fx.message.throwException("downloadStream error :" + msg)
    // }
    // InputStream inputStream = fileData['inputStream'] as InputStream
    // MultipartBody body = MultipartBody.builder()
    //   .addPart("name", "tom")
    //   .addPart("id", "1234")
    //   .addPart("file", inputStream, '测试附件.docx', 'application/octet-stream')
    //   .build();
    
    
    //方式三、使用InputStreamBody传输文件
    //InputStreamBody body = InputStreamBody.builder()
    //  .content(inputStream)
    //  .build()
    
    
    //方式四、 application/x-www-form-urlencoded 的body请求格式
    // FormBody body = FormBody.builder()
    //   .field("a", "qweasd")
    //   .field("b", 12423)
    //   .field("c", "hello")
    //   .build()
    
    Request request = Request.builder()
      .method("POST")
      .url('http://httpbin.org/post')
      .timeout(7000)
      .retryCount(0)
      .header("Content-Type", "multipart/form-data")
      .body(body)
      .build()
    
    def(Boolean error, HttpResult result, String message) = Fx.http.execute(request)
    if (error || result.statusCode != 200) {
        //可以增加打印请求参数
        log.error("http request error: "+ error +" errorMessage: " + errorMessage + " result: " + result)
        //1.使用报错终止执行
        //Fx.message.throwException("http.get error")
    
        //2.使用return终止执行
        //return;
    
        //3.继续执行
    } else {
      def content = result.content //函数封装的结果，一般使用这个即可
      def byte[] bytes = result.bytes //原始的二进制结果数据，如果上边方式获取结果有问题/文件等非数据信息，可以使用这个
     //dosomething 
    }
    
    

**参考对象**

  * 参考HttpResult

  * 参考Request




**注意事项**

>   * 支持application/json，application/octet-stream，application/x-www-form-urlencoded和multipart/form-data
>   * HttpResult中的content默认是String，但如果response header中context-type=application/json会转成Object;
>   * 默认5m大小限制
> 


### # 1\. postSoap soap请求发送, 返回参数体

> `Fx.http.postSoap(<SoapRequest request>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
request | SoapRequest | 请求体 | 是  
  
**Groovy 举例**
    
    
    // 旧方式的调用方法
    // String content = '<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope" xmlns:tem="http://tempuri.org/"><soap:Header/><soap:Body><tem:CalcPrecoFAC><tem:nCdServico>41106</tem:nCdServico><tem:nVlPeso>10</tem:nVlPeso><tem:strDataCalculo>22/11/2018</tem:strDataCalculo></tem:CalcPrecoFAC></soap:Body></soap:Envelope>'
    // String url = 'http://ws.correios.com.br/calculador/CalcPrecoPrazo.asmx?wsdl'
    // def(Boolean error, HttpResult result, String message) = Fx.http.post(url, ["Content-Type": "application/soap+xml"], content)
    // if (error) {
    //   log.info("error :" + message)
    // } else {
    //   log.info(result)
    // }
    
    // 返回结果是个也是个xml需要自己解析内容
    // 结果：<?xml version="1.0" encoding="utf-8"?><soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema"><soap:Body><CalcPrecoFACResponse xmlns="http://tempuri.org/"><CalcPrecoFACResult><Servicos><cServico><Codigo>41106</Codigo><Valor>0</Valor><Erro>-1</Erro><MsgErro>Codigo de servico invalido.</MsgErro></cServico></Servicos></CalcPrecoFACResult></CalcPrecoFACResponse></soap:Body></soap:Envelope>// 新的方式不需要自己解析Repsone Body
    // 新方式一：
    Map map = [
      "nCdServico":"41106",
      "nVlPeso":"10",
      "strDataCalculo":"22/11/2018"
    ]
    SoapRequest request = SoapRequest.builder()
      .url("http://ws.correios.com.br/calculador/CalcPrecoPrazo.asmx?wsdl")
      .namespace("http://tempuri.org/")
      .localPart("CalcPrecoFAC")
      .prefix("tem")
      .bodyParams(map)
      .build();
    def(Boolean error, HttpResult result, String message) = Fx.http.postSoap(request)
    if (error || result.statusCode != 200) {
      log.info("error :" + result)
    } else {
      log.info(result.getContent())
    }
    
    // 新方式二：
    String xml = '''<soap:Envelope
        xmlns:soap="http://www.w3.org/2003/05/soap-envelope"
        xmlns:tem="http://tempuri.org/"><soap:Header/><soap:Body><tem:CalcPrecoFAC><tem:nCdServico>41106</tem:nCdServico><tem:nVlPeso>10</tem:nVlPeso><tem:strDataCalculo>22/11/2018</tem:strDataCalculo></tem:CalcPrecoFAC></soap:Body></soap:Envelope>'''
    SoapRequest request = SoapRequest.builder()
      .url("http://ws.correios.com.br/calculador/CalcPrecoPrazo.asmx?wsdl")
      .fromXml(xml)
      .build();
    def(Boolean error, HttpResult result, String message) = Fx.http.postSoap(request)
    if (error || result.statusCode != 200) {
      log.info("error :" + result)
    } else {
      log.info(result.getContent())
    }
    //结果： {CalcPrecoFACResponse={CalcPrecoFACResult={Servicos={cServico={MsgErro=Codigo de servico invalido., Codigo=41106, Erro=-1, Valor=0}}}}}
    
    

**参考对象**

  * 参考SoapRequest

  * 参考HttpResult




**注意事项**

>   * 默认5m大小限制
>   * version字段作用为指定header中Content-Type对应值，默认为text/xml，当指定version为SOAP_1_2对应application/soap+xml；
> 


### # 2\. get HTTP GET请求

> `Fx.http.get(<String url>, <Map headers>, <Integer timeout>, <Integer retry>, <Integer retryCount>, <Boolean ignoreSSL>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
url | String | 请求的url | 是  
headers | Map | 可选参数，请求header | 是  
timeout | Integer | 可选参数，scoketTimeOut超时时间，单位ms，最大120s ，1s=1000ms | \--  
retry | Integer | 可选参数，scoketTimeOut超时是否重试；连接超时一定会进行重试，这个参数决定了timeout是否重试；设置为true时，可能会造成重复提交--已废弃 | \--  
retryCount | Integer | 可选参数，重试次数，最多3次--已废弃 | \--  
ignoreSSL | Boolean | 可选参数，绕过SSl验证 | \--  
  
**Groovy 举例**
    
    
    def (Boolean error, HttpResult result, String errorMessage) = Fx.http.get("http://www.fxiaoke.com", ["X-token":"myToken"], 2000, true, 2, false)
    if (error || result.statusCode != 200) {
        //可以增加打印请求参数
        log.error("http request error: "+ error +" errorMessage: " + errorMessage + " result: " + result)
        //1.使用报错终止执行
        //Fx.message.throwException("http.get error")
    
        //2.使用return终止执行
        //return;
    
        //3.继续执行
    } else {
      def content = result.content //函数封装的结果，一般使用这个即可
      def byte[] bytes = result.bytes //原始的二进制结果数据，如果上边方式获取结果有问题/文件等非数据信息，可以使用这个
     //dosomething 
    }
    
    

**参考对象**

  * 参考HttpResult



**注意事项**

>   * 默认5m大小限制；
>   * 推荐使用execute替换该方法；
>   * 重试已作废，不再支持；
> 


### # 3\. post HTTP POST请求

> `Fx.http.post(<String url>, <Map headers>, <Map data>, <Integer timeout>, <Integer retry>, <Integer retryCount>, <Boolean ignoreSSL>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
url | String | 请求的url | 是  
headers | Map | 可选参数，请求header | 是  
data | Map | 请求体 | \--  
timeout | Integer | 可选参数，scoketTimeOut超时时间，单位ms，最大120s ，1s=1000ms | \--  
retry | Integer | 可选参数，scoketTimeOut超时是否重试；连接超时一定会进行重试，这个参数决定了timeout是否重试；设置为true时，可能会造成重复提交--已废弃 | \--  
retryCount | Integer | 可选参数，重试次数，最多3次--已废弃 | \--  
ignoreSSL | Boolean | 可选参数，绕过SSl验证 | \--  
  
**Groovy 举例**
    
    
    def (Boolean error,HttpResult result,String errorMessage) = Fx.http.post("http://www.fxiaoke.com", ["X-token":"myToken"], ["id":1], 2000, true, 2, false)
    if (error || result.statusCode != 200) {
        //可以增加打印请求参数
        log.error("http request error: "+ error +" errorMessage: " + errorMessage + " result: " + result)
        //1.使用报错终止执行
        //Fx.message.throwException("http.get error")
    
        //2.使用return终止执行
        //return;
    
        //3.继续执行
    } else {
      def content = result.content //函数封装的结果，一般使用这个即可
      def byte[] bytes = result.bytes //原始的二进制结果数据，如果上边方式获取结果有问题/文件等非数据信息，可以使用这个
     //dosomething 
    }
    
    

**参考对象**

  * 参考HttpResult



**注意事项**

>   * 默认5m大小限制
> 


### # 4\. options HTTP OPTIONS请求

> `Fx.http.options(<String url>, <Map headers>, <Integer timeout>, <Integer retry>, <Integer retryCount>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
url | String | 请求的url | 是  
headers | Map | 可选参数，请求header | 是  
timeout | Integer | 可选参数，scoketTimeOut超时时间，单位ms，最大120s ，1s=1000ms | \--  
retry | Integer | 可选参数，scoketTimeOut超时是否重试；连接超时一定会进行重试，这个参数决定了timeout是否重试；设置为true时，可能会造成重复提交--已废弃 | \--  
retryCount | Integer | 可选参数，重试次数，最多3次--已废弃 | \--  
  
**Groovy 举例**
    
    
    def (Boolean error, HttpResult result, String errorMessage) = Fx.http.options("http://www.fxiaoke.com", ["X-token":"myToken"], 2000, true, 2)
    if (error || result.statusCode != 200) {
        //可以增加打印请求参数
        log.error("http request error: "+ error +" errorMessage: " + errorMessage + " result: " + result)
        //1.使用报错终止执行
        //Fx.message.throwException("http.get error")
    
        //2.使用return终止执行
        //return;
    
        //3.继续执行
    } else {
      def content = result.content //函数封装的结果，一般使用这个即可
      def byte[] bytes = result.bytes //原始的二进制结果数据，如果上边方式获取结果有问题/文件等非数据信息，可以使用这个
     //dosomething 
    }
    
    

**参考对象**

  * 参考HttpResult



**注意事项**

>   * 默认5m大小限制
> 


### # 5\. put HTTP PUT请求

> `Fx.http.put(<String url>, <Map headers>, <Map data>, <Integer timeout>, <Integer retry>, <Integer retryCount>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
url | String | 请求的url | 是  
headers | Map | 可选参数，请求header | 是  
data | Map | 请求体 | \--  
timeout | Integer | 可选参数，scoketTimeOut超时时间，单位ms，最大120s ，1s=1000ms | \--  
retry | Integer | 可选参数，scoketTimeOut超时是否重试；连接超时一定会进行重试，这个参数决定了timeout是否重试；设置为true时，可能会造成重复提交--已废弃 | \--  
retryCount | Integer | 可选参数，重试次数，最多3次--已废弃 | \--  
  
**Groovy 举例**
    
    
    def (Boolean error, HttpResult result, String errorMessage) = Fx.http.put("http://www.fxiaoke.com", ["X-token":"myToken"], ["id":1], 2000, true, 2)
    if (error || result.statusCode != 200) {
        //可以增加打印请求参数
        log.error("http request error: "+ error +" errorMessage: " + errorMessage + " result: " + result)
        //1.使用报错终止执行
        //Fx.message.throwException("http.get error")
    
        //2.使用return终止执行
        //return;
    
        //3.继续执行
    } else {
      def content = result.content //函数封装的结果，一般使用这个即可
      def byte[] bytes = result.bytes //原始的二进制结果数据，如果上边方式获取结果有问题/文件等非数据信息，可以使用这个
     //dosomething 
    }
    
    

**参考对象**

  * 参考HttpResult



**注意事项**

>   * 默认5m大小限制
> 


### # 6\. delete HTTP DELETE请求

> `Fx.http.delete(<String url>, <Map headers>, <Map data>, <Integer timeout>, <Integer retry>, <Integer retryCount>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
url | String | 请求的url | 是  
headers | Map | 可选参数，请求header | 是  
data | Map | 请求体 | \--  
timeout | Integer | 可选参数，scoketTimeOut超时时间，单位ms，最大120s ，1s=1000ms | \--  
retry | Integer | 可选参数，scoketTimeOut超时是否重试；连接超时一定会进行重试，这个参数决定了timeout是否重试；设置为true时，可能会造成重复提交--已废弃 | \--  
retryCount | Integer | 可选参数，重试次数，最多3次--已废弃 | \--  
  
**Groovy 举例**
    
    
    def (Boolean error, HttpResult result, String errorMessage) = Fx.http.delete("http://www.fxiaoke.com", ["X-token":"myToken"], ["id":1], 2000, true, 2)
    if (error || result.statusCode != 200) {
        //可以增加打印请求参数
        log.error("http request error: "+ error +" errorMessage: " + errorMessage + " result: " + result)
        //1.使用报错终止执行
        //Fx.message.throwException("http.get error")
    
        //2.使用return终止执行
        //return;
    
        //3.继续执行
    } else {
      def content = result.content //函数封装的结果，一般使用这个即可
      def byte[] bytes = result.bytes //原始的二进制结果数据，如果上边方式获取结果有问题/文件等非数据信息，可以使用这个
     //dosomething 
    }
    
    

**参考对象**

  * 参考HttpResult



**注意事项**

>   * 默认5m大小限制
> 


### # 7\. patch HTTP PATCH请求

> `Fx.http.patch(<String url>, <Map headers>, <Map data>, <Integer timeout>, <Integer retry>, <Integer retryCount>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
url | String | 请求的url | 是  
headers | Map | 可选参数，请求header | 是  
data | Map | 请求体 | \--  
timeout | Integer | 可选参数，scoketTimeOut超时时间，单位ms，最大120s ，1s=1000ms | \--  
retry | Integer | 可选参数，scoketTimeOut超时是否重试；连接超时一定会进行重试，这个参数决定了timeout是否重试；设置为true时，可能会造成重复提交--已废弃 | \--  
retryCount | Integer | 可选参数，重试次数，最多3次--已废弃 | \--  
  
**Groovy 举例**
    
    
    def (Boolean error, HttpResult result, String errorMessage) = Fx.http.patch("http://www.fxiaoke.com", ["X-token":"myToken"], ["id":1], 2000, true, 2)
    if (error || result.statusCode != 200) {
        //可以增加打印请求参数
        log.error("http request error: "+ error +" errorMessage: " + errorMessage + " result: " + result)
        //1.使用报错终止执行
        //Fx.message.throwException("http.get error")
    
        //2.使用return终止执行
        //return;
    
        //3.继续执行
    } else {
      def content = result.content //函数封装的结果，一般使用这个即可
      def byte[] bytes = result.bytes //原始的二进制结果数据，如果上边方式获取结果有问题/文件等非数据信息，可以使用这个
     //dosomething 
    }
    
    

**参考对象**

  * 参考HttpResult



**注意事项**

>   * 默认5m大小限制
> 


## # 参考类 com.fxiaoke.functions.http.HttpResult

### # 字段说明

参数名称 | object |   
---|---|---  
headers | java.util.Map | HTTP响应的header内容  
bytes | byte[] | HTTP请求原始二进制数据  
content | java.lang.Object | HTTP响应的Payload内容  
statusCode | int | HTTP响应状态码  
  
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
  
## # 参考类 com.fxiaoke.functions.http.SoapRequest

### # 字段说明

参数名称 | object | 描述  
---|---|---  
headers | `java.util.Map<java.lang.String,java.util.List<java.lang.String>>` | 请求头  
prefix | java.lang.String | 前缀  
retryCount | java.lang.Integer | 重试次数，0表示不重试，最大3次重试,默认为不重试  
localPart | java.lang.String | 发送消息的localPart  
bodyParams | `java.util.Map<java.lang.String,java.lang.Object>` | 参数列表，可以层级包含  
namespace | java.lang.String | 发送消息的命名空间  
version | java.lang.String | version，现有1.1版本值为 SOAP_1_1 1.2版本值为 SOAP_1_2 默认为1.1  
fromXml | java.lang.String | 直接通过xml请求  
timeout | java.lang.Integer | 超时时间, 默认15秒，最大120s  
url | java.lang.String | 请求的url地址  
  
[Fx.org](../OrganizationAPI/) [Fx.log](../LogAPI/)

← [Fx.org](../OrganizationAPI/) [Fx.log](../LogAPI/)→ 

  * 跟随系统 
  * 浅色模式 
  * 深色模式 
  * 阅读模式 


