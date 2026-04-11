#  Fx.utils

## # Fx.utils

### # 1\. htmlParseText 从html中提取纯文本

> `Fx.utils.htmlParseText(<String html>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
html | String | 提取html内容 | 是  
  
**Groovy 举例**
    
    
    def ret = Fx.utils.htmlParseText('<div class="drop-content-item"><div class="drop-box"><div class="drop-box-item drop-box-item2"style="border: none"> <img class="img-icon"style="width:20px;"src="https://www.fxiaoke.com/ap/wp-content/uploads/2020/05/icon-live.png"><ahref="/ap/live/">直播视频</a></p>RM公开课、CRM使用技巧、数字化转型策略及行业应用最新实践等视频内容</div>').result()
    //直播视频
    //RM公开课、CRM使用技巧、数字化转型策略及行业应用最新实践等视频内容
    log.info(ret)
    
    

### # 2\. toPinyin 汉字转拼音

> `Fx.utils.toPinyin(<String chinese>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
chinese | String | 汉字 | 是  
  
**Groovy 举例**
    
    
    def ret = Fx.utils.toPinyin("测试").result()
    //ceshi
    log.info(ret)
    
    

### # 3\. listPartition 数组拆分

> `Fx.utils.listPartition(<List list>, <Integer size>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
list | List | 需要拆分的数组 | 是  
size | Integer | 拆分后每个数组的长度 | 是  
  
**Groovy 举例**
    
    
    List original = [1,2,3,4,5,6,7,8,9]
    //[[1,2,3],[4,5,6],[7,8,9]]
    List partition = Fx.utils.listPartition(original,3)
    
    

### # 4\. listUnique 数组去重

> `Fx.utils.listUnique(<List list>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
list | List | 需要去重的list | 是  
  
**Groovy 举例**
    
    
    def list = [1,1,1,2,2,3,4,5]
    def ret = Fx.utils.listUnique(list)
    // [1, 2, 3, 4, 5]
    log.info(ret)
    
    

### # 5\. toUTF8Bytes 字符串转字节数组

> `Fx.utils.toUTF8Bytes(<String content>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
content | String | 字符串 | 是  
  
**Groovy 举例**
    
    
    def bytes = Fx.utils.toUTF8Bytes("hello你好")
    String content = Fx.utils.toUTF8String(bytes)
    //hello你好
    log.info(content)
    
    

### # 6\. toUTF8String 字节数据转字符串

> `Fx.utils.toUTF8String(<byte[] bytes>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
bytes | byte[] | 字节数组 | 是  
  
**Groovy 举例**
    
    
    def bytes = Fx.utils.toUTF8Bytes("hello你好")
    String content = Fx.utils.toUTF8String(bytes)
    //hello你好
    log.info(content)
    
    

### # 7\. getLevenshteinDistance 计算字符串之间的差异

> `Fx.utils.getLevenshteinDistance(<String left>, <String right>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
left | String | 对比字符串1 | 是  
right | String | 对比字符串2 | 是  
  
**Groovy 举例**
    
    
    def aa = Fx.utils.getLevenshteinDistance("test1","test2") // 1
    log.info(aa)
    
    def bb = Fx.utils.getLevenshteinDistance("test1","tet") // 2
    log.info(bb)
    
    def cc = Fx.utils.getLevenshteinDistance("test1","stet1") // 2
    log.info(cc)
    
    def dd = Fx.utils.getLevenshteinDistance("test1","test1") // 0
    log.info(dd)
    
    

**注意事项**

>   * 该返回值代表两个输入字符串之间的 Levenshtein 距离，即把一个字符串转换为另一个字符串所需的最少编辑操作次数（插入、删除、替换字符）。
>   * 具体来说：
>   * 如果返回值为 0，表示两个字符串完全相同。
>   * 返回值越大，说明两个字符串的差异越大，需要更多的编辑操作才能将一个转换为另一个。
>   * 如果出现问题，可能返回 -1，这通常意味着发生了错误或无法确定距离。
> 


### # 8\. getRequestSource 获取终端的请求来源

> `Fx.utils.getRequestSource()`

**Groovy 举例**
    
    
    //Android 安卓
    //iOS   iOS
    //DingTalk   钉钉
    //WX   微信
    //CloudHub   云之家
    //FSBrowser   纷享客户端
    //WEB   网页
    //FSBrowser 分享客户端
    //如果查询不到返回空字符串（例如流程后面），目前只能在终端直接触发函数时可以获取到（例如点击按钮）
    //获取函数执行时的来源，返回一个字符串
    String source = Fx.utils.getRequestSource()
    
    

### # 9\. getDeviceType 获取设备类型

> `Fx.utils.getDeviceType()`

**Groovy 举例**
    
    
    def deviceType = Fx.utils.getDeviceType()
    if(deviceType == 'mobile'){
      //移动端场景 dosomething
      log.info("移动端 dosomething")
    } else {
      //非移动端场景 dosomething
      log.info("非移动端 dosomething")
    }
    
    

### # 10\. daysInMonth 返回指定年月的天数

> `Fx.utils.daysInMonth(<Integer year>, <Integer month>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
year | Integer | 年份 | 是  
month | Integer | 月份 | 是  
  
**Groovy 举例**
    
    
    Fx.utils.daysInMonth(2020, 2) //返回29
    
    

### # 11\. isLeapYear 返回指定年是否是闰年

> `Fx.utils.isLeapYear(<Integer year>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
year | Integer | 年份 | 是  
  
**Groovy 举例**
    
    
    Fx.utils.isLeapYear(2020) //返回true
    
    

### # 12\. encodeHex byte数组转16进制字符串

> `Fx.utils.encodeHex(<byte[] bytes>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
bytes | byte[] | 字节数组 | 是  
  
**Groovy 举例**
    
    
    def hex = Fx.utils.encodeHex('testtest'.getBytes())
    log.info(hex)
    
    

### # 13\. decodeHex 16进制字符串转byte数组

> `Fx.utils.decodeHex(<String str>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
str | String | 字符串 | 是  
  
**Groovy 举例**
    
    
    def hex = Fx.utils.encodeHex('testtest'.getBytes())
    log.info(hex) //7465737474657374
    
    def str = Fx.utils.toUTF8String(Fx.utils.decodeHex(hex))
    log.info(str) //testtest
    
    

### # 14\. dataConvert 将map value time 类型 转时间戳  
BigDecimal 类型转换成 String

> `Fx.utils.dataConvert(<Map data>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
data | Map | Map对象 | 是  
  
**Groovy 举例**
    
    
    def map = [
      "date": Date.now(),
      "dateTime": DateTime.now(),
      "time": Time.now(),
      "bigDecimal": BigDecimal.of("123.456")
      ]
    def ret = Fx.utils.dataConvert(map)
    log.info(ret) // {date=1726761600000, dateTime=1726826030045, time=35630056, bigDecimal=123.456}
    
    

### # 15\. amountToEnWords 数字金额转英文大写

> `Fx.utils.amountToEnWords(<String currency>, <BigDecimal bigDecimal>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
currency | String | 货币种类 现支持的有：美元-USD，人民币-CNY，欧元-EUR，港币-HKD | 是  
bigDecimal | BigDecimal | 金额数字 | 是  
  
**Groovy 举例**
    
    
    BigDecimal b = BigDecimal.of("1848.00") // 金额
    //币种：美元-USD，人民币-CNY，欧元-EUR，港币-HKD
    String currType = "CNY"
    String en = Fx.utils.amountToEnWords(currType, b)
    log.info(en)//SAY CNY ONE THOUSAND EIGHT HUNDRED AND FORTY EIGHT ONLY
    
    

### # 16\. getLang 获取当前crm语言

> `Fx.utils.getLang()`

**Groovy 举例**
    
    
    def lang = Fx.utils.getLang()
    //en: 英语，zh-CN：简体中文，zh-TW：繁体中文
    log.info(lang)
    
    

[Fx.function](../FunctionAPI/) [Fx.AI](../AIAPI/)

← [Fx.function](../FunctionAPI/) [Fx.AI](../AIAPI/)→ 

  * 跟随系统 
  * 浅色模式 
  * 深色模式 
  * 阅读模式 


