#  Fx.crypto

## # Fx.crypto

### # 1\. getMD5 MD5

> `Fx.crypto.getMD5()`

#### # 参考函数接口

  * 参考com.fxiaoke.functions.api.MD5API



### # 2\. getDESede DESede

> `Fx.crypto.getDESede()`

#### # 参考函数接口

  * 参考com.fxiaoke.functions.api.DESedeAPI



### # 3\. getBase64 Base64

> `Fx.crypto.getBase64()`

#### # 参考函数接口

  * 参考com.fxiaoke.functions.api.Base64API



### # 4\. getSHA1 SHA1

> `Fx.crypto.getSHA1()`

#### # 参考函数接口

  * 参考com.fxiaoke.functions.api.SHA1API



### # 5\. getURL URL编码解码

> `Fx.crypto.getURL()`

#### # 参考函数接口

  * 参考com.fxiaoke.functions.api.URLAPI



### # 6\. getSHA SHA

> `Fx.crypto.getSHA()`

#### # 参考函数接口

  * 参考com.fxiaoke.functions.api.SHAAPI



### # 7\. getECC ECC算法

> `Fx.crypto.getECC()`

#### # 参考函数接口

  * 参考com.fxiaoke.functions.api.ECCAPI



### # 8\. getRSA RSA算法

> `Fx.crypto.getRSA()`

#### # 参考函数接口

  * 参考com.fxiaoke.functions.api.RSAAPI



### # 9\. getHex HEX

> `Fx.crypto.getHex()`

#### # 参考函数接口

  * 参考com.fxiaoke.functions.api.HexAPI



### # 10\. getHmac HMAC

> `Fx.crypto.getHmac()`

#### # 参考函数接口

  * 参考com.fxiaoke.functions.api.HmacAPI



### # 11\. getSymmetry 对称算法集合

> `Fx.crypto.getSymmetry()`

#### # 参考函数接口

  * 参考com.fxiaoke.functions.api.SymmetryAPI



### # 12\. getSM4 SM4中国对称加密算法

> `Fx.crypto.getSM4()`

#### # 参考函数接口

  * 参考com.fxiaoke.functions.api.SM4API



### # 13\. getSM2 SM2中国非对称加密算法

> `Fx.crypto.getSM2()`

#### # 参考函数接口

  * 参考com.fxiaoke.functions.api.SM2API



### # 14\. getSM3 SM3中国数据签名算法

> `Fx.crypto.getSM3()`

#### # 参考函数接口

  * 参考com.fxiaoke.functions.api.SM3API



## # 参考类 com.fxiaoke.functions.api.MD5API

### # 1\. encode 对输入字节进行MD5摘要运算，并对byte[]运算结果进行16进制转字符串编码

> `MD5API.encode(<String data>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
data | String | 需要运算的数据 | 是  
  
**Groovy 举例**
    
    
    def str = "testtest"
    def encode1 = Fx.crypto.MD5.encode(str)
    log.info(encode1)//05A671C66AEFEA124CC08B76EA6D30BB
    
    def encode = Fx.crypto.MD5.encode(str.getBytes())
    log.info(encode) //05A671C66AEFEA124CC08B76EA6D30BB
    
    def encodeByte = Fx.crypto.MD5.encode2Bytes(str.getBytes())
    log.info(encodeByte)
    
    

### # 2\. encode2Bytes 对输入内容进行MD5摘要运算

> `MD5API.encode2Bytes(<byte[] data>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
data | byte[] | 需要运算的数据 | 是  
  
**Groovy 举例**
    
    
    def str = "testtest"
    def encode1 = Fx.crypto.MD5.encode(str)
    log.info(encode1)//05A671C66AEFEA124CC08B76EA6D30BB
    
    def encode = Fx.crypto.MD5.encode(str.getBytes())
    log.info(encode) //05A671C66AEFEA124CC08B76EA6D30BB
    
    def encodeByte = Fx.crypto.MD5.encode2Bytes(str.getBytes())
    log.info(encodeByte)
    
    

### # 3\. encode 对输入的字符串进行MD5摘要运算，并对byte[]运算结果进行16进制转字符串编码

> `MD5API.encode(<String data>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
data | String | 需要运算的数据 | 是  
  
**Groovy 举例**
    
    
    def str = "testtest"
    def encode1 = Fx.crypto.MD5.encode(str)
    log.info(encode1)//05A671C66AEFEA124CC08B76EA6D30BB
    
    def encode = Fx.crypto.MD5.encode(str.getBytes())
    log.info(encode) //05A671C66AEFEA124CC08B76EA6D30BB
    
    def encodeByte = Fx.crypto.MD5.encode2Bytes(str.getBytes())
    log.info(encodeByte)
    
    

## # 参考类 com.fxiaoke.functions.api.DESedeAPI

### # 1\. encode DESede加密

> `DESedeAPI.encode(<byte[] key>, <byte[] data>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
key | byte[] | 加密秘钥，24位以上 | 是  
data | byte[] | 需要编码的数据 | 是  
  
**Groovy 举例**
    
    
    def key = "12345678123456781234567812" //秘钥长度>=24位
    def iv = "12345678"//8位iv
    
    def data = "testtest"//加密数据
    def encode = Fx.crypto.DESede.encode(Strings.toUTF8Bytes(key) ,iv, data.getBytes())
    log.info(encode) 
    
    def decode = Fx.crypto.DESede.decode(Strings.toUTF8Bytes(key), iv, encode)
    log.info(Strings.toUTF8String(decode))//testtest
    
    

**注意事项**

>   * 加解密的数据如果参数是byte[]类型的，需要注意数据是Base64、Hex、还是普通字符串，对应转为byte[]的方式是不一样的；
> 


**负责人：斯作益seth**

### # 2\. decode DESede解密

> `DESedeAPI.decode(<byte[] key>, <byte[] data>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
key | byte[] | 加密秘钥，24位以上 | 是  
data | byte[] | 需要解码的数据 | 是  
  
**Groovy 举例**
    
    
    def key = "12345678123456781234567812" //秘钥长度>=24位
    def iv = "12345678"//8位iv
    
    def data = "testtest"//加密数据
    def encode = Fx.crypto.DESede.encode(Strings.toUTF8Bytes(key) ,iv, data.getBytes())
    log.info(encode) 
    
    def decode = Fx.crypto.DESede.decode(Strings.toUTF8Bytes(key), iv, encode)
    log.info(Strings.toUTF8String(decode))//testtest
    
    

**注意事项**

>   * 加解密的数据如果参数是byte[]类型的，需要注意数据是Base64、Hex、还是普通字符串，对应转为byte[]的方式是不一样的；
> 


**负责人：斯作益seth**

## # 参考类 com.fxiaoke.functions.api.Base64API

### # 1\. encode Base64编码

> `Base64API.encode(<byte[] data>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
data | byte[] | 需要编码的数据 | 是  
  
**Groovy 举例**
    
    
    def str = "testtest"
    def encode = Fx.crypto.base64.encode(str.getBytes())
    log.info(encode) //dGVzdHRlc3Q=
    
    def decode = Fx.crypto.base64.decode(encode)
    log.info(StringUtils.toUTF8String(decode)) //testtest
    
    def decode2 = Fx.crypto.base64.decode(encode.getBytes())
    log.info(StringUtils.toUTF8String(decode2)) //testtest
    
    

### # 2\. decode Base64解码

> `Base64API.decode(<String data>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
data | String | 需要解码的数据 | 是  
  
**Groovy 举例**
    
    
    def str = "testtest"
    def encode = Fx.crypto.base64.encode(str.getBytes())
    log.info(encode) //dGVzdHRlc3Q=
    
    def decode = Fx.crypto.base64.decode(encode)
    log.info(StringUtils.toUTF8String(decode)) //testtest
    
    def decode2 = Fx.crypto.base64.decode(encode.getBytes())
    log.info(StringUtils.toUTF8String(decode2)) //testtest
    
    

### # 3\. decode Base64解码

> `Base64API.decode(<byte[] data>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
data | byte[] | 需要解码的数据 | 是  
  
**Groovy 举例**
    
    
    def str = "testtest"
    def encode = Fx.crypto.base64.encode(str.getBytes())
    log.info(encode) //dGVzdHRlc3Q=
    
    def decode = Fx.crypto.base64.decode(encode)
    log.info(StringUtils.toUTF8String(decode)) //testtest
    
    def decode2 = Fx.crypto.base64.decode(encode.getBytes())
    log.info(StringUtils.toUTF8String(decode2)) //testtest
    
    

## # 参考类 com.fxiaoke.functions.api.SHA1API

### # 1\. encode sha1运算

> `SHA1API.encode()`

**Groovy 举例**
    
    
    Fx.crypto.SHA1.encode([1, 2] as byte[])
    
    

**注意事项**

>   * 加解密的数据如果参数是byte[]类型的，需要注意数据是Base64、Hex、还是普通字符串，对应转为byte[]的方式是不一样的；
> 


**负责人：斯作益seth**

### # 2\. encode sha1运算

> `SHA1API.encode()`

**Groovy 举例**
    
    
    Fx.crypto.SHA1.encode("data")
    
    

**注意事项**

>   * 加解密的数据如果参数是byte[]类型的，需要注意数据是Base64、Hex、还是普通字符串，对应转为byte[]的方式是不一样的；
> 


**负责人：斯作益seth**

### # 3\. hex sha1运算，并对结果追加hex编码

> `SHA1API.hex()`

**Groovy 举例**
    
    
    Fx.crypto.SHA1.hex([1, 2] as byte[])
    
    

**负责人：斯作益seth**

### # 4\. hex sha1运算，并对结果追加hex编码

> `SHA1API.hex()`

**Groovy 举例**
    
    
    Fx.crypto.SHA1.hex("data")
    
    

**负责人：斯作益seth**

### # 5\. hmacSHA1 hmacSHA1运算

> `SHA1API.hmacSHA1()`

**Groovy 举例**
    
    
    Fx.crypto.SHA1.hmacSHA1("123", "hello")
    
    

**负责人：斯作益seth**

## # 参考类 com.fxiaoke.functions.api.URLAPI

### # 1\. encode url编码

> `URLAPI.encode(<String data>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
data | String | 需要编码的数据 | 是  
  
**Groovy 举例**
    
    
    def str = 'name=Ichabod+Crane&gender=male&status=missing'
    String encode = Fx.crypto.URL.encode(str).result()
    log.info(encode) //name%3DIchabod%2BCrane%26gender%3Dmale%26status%3Dmissing
    String decode = Fx.crypto.URL.decode(encode).result()
    log.info(decode) //name%3DIchabod%2BCrane%26gender%3Dmale%26status%3Dmissing
    
    

### # 2\. decode url解码

> `URLAPI.decode(<String data>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
data | String | 需要解码的数据 | 是  
  
**Groovy 举例**
    
    
    def str = 'name=Ichabod+Crane&gender=male&status=missing'
    String encode = Fx.crypto.URL.encode(str).result()
    log.info(encode) //name%3DIchabod%2BCrane%26gender%3Dmale%26status%3Dmissing
    String decode = Fx.crypto.URL.decode(encode).result()
    log.info(decode) //name%3DIchabod%2BCrane%26gender%3Dmale%26status%3Dmissing
    
    

**负责人：斯作益seth**

## # 参考类 com.fxiaoke.functions.api.SHAAPI

### # 1\. sha256 sha256运算

> `SHAAPI.sha256(<byte[] data>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
data | byte[] | 需要运算的数据 | 是  
  
**Groovy 举例**
    
    
    def str = 'testtest'
    byte[] sha1 = Fx.crypto.SHA.sha256(str)
    byte[] sha2 = Fx.crypto.SHA.sha256(str.getBytes())
    
    

**注意事项**

>   * 加解密的数据如果参数是byte[]类型的，需要注意数据是Base64、Hex、还是普通字符串，对应转为byte[]的方式是不一样的；
> 


### # 2\. sha256 sha256运算

> `SHAAPI.sha256(<String data>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
data | String | 需要运算的数据 | 是  
  
**Groovy 举例**
    
    
    def str = 'testtest'
    byte[] sha1 = Fx.crypto.SHA.sha256(str)
    byte[] sha2 = Fx.crypto.SHA.sha256(str.getBytes())
    
    

**注意事项**

>   * 加解密的数据如果参数是byte[]类型的，需要注意数据是Base64、Hex、还是普通字符串，对应转为byte[]的方式是不一样的；
> 


### # 3\. sha256HMAC HmacSHA256运算

> `SHAAPI.sha256HMAC(<String secret>, <String data>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
secret | String | 秘钥 | 是  
data | String | 需要运算的数据 | 是  
  
**Groovy 举例**
    
    
    def secret = '12345678'
    def str = 'testtest'
    byte[] sha1 = Fx.crypto.SHA.sha256HMAC(secret, str)
    byte[] sha2 = Fx.crypto.SHA.sha256HMAC(secret.getBytes(), str)
    
    

### # 4\. sha256HMAC HmacSHA256运算

> `SHAAPI.sha256HMAC(<byte[] secret>, <String data>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
secret | byte[] | 秘钥 | 是  
data | String | 需要运算的数据 | 是  
  
**Groovy 举例**
    
    
    def secret = '12345678'
    def str = 'testtest'
    byte[] sha1 = Fx.crypto.SHA.sha256HMAC(secret, str)
    byte[] sha2 = Fx.crypto.SHA.sha256HMAC(secret.getBytes(), str)
    
    

### # 5\. sha256Hex sha256运算，并对加密结果做Hex编码

> `SHAAPI.sha256Hex(<String data>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
data | String | 需要运算的数据 | 是  
  
**Groovy 举例**
    
    
    def str = 'testtest'
    def hex1 = Fx.crypto.SHA.sha256Hex(str)
    log.info(hex1) //37268335dd6931045bdcdf92623ff819a64244b53d0e746d438797349d4da578
    def hex2 = Fx.crypto.SHA.sha256Hex(str)
    log.info(hex2) //37268335dd6931045bdcdf92623ff819a64244b53d0e746d438797349d4da578
    
    

### # 6\. sha256Hex 并对运算结果做Hex编码

> `SHAAPI.sha256Hex(<byte[] data>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
data | byte[] | 需要运算的数据 | 是  
  
**Groovy 举例**
    
    
    def str = 'testtest'
    def hex1 = Fx.crypto.SHA.sha256Hex(str)
    log.info(hex1) //37268335dd6931045bdcdf92623ff819a64244b53d0e746d438797349d4da578
    def hex2 = Fx.crypto.SHA.sha256Hex(str)
    log.info(hex2) //37268335dd6931045bdcdf92623ff819a64244b53d0e746d438797349d4da578
    
    

## # 参考类 com.fxiaoke.functions.api.ECCAPI

### # 1\. encrypt ECC加密

> `ECCAPI.encrypt(<String publicKey>, <String data>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
publicKey | String | 加密公钥，生成的算法为ECC，格式为Base64，X.509标准存储 | 是  
data | String | 需要加密的数据 | 是  
  
**Groovy 举例**
    
    
    String publicKey = "MFYwEAYHKoZIzj0CAQYFK4EEAAoDQgAEwGWFaJ9DfFEOerfs9ONP9nPozdJmpQ+tTy2xUknp8YVJnx/93dWXbRI6oGEwAVY26zWMcNPLtd8ekbPWbfSjUA=="
    String str = "testtest";
    String encryptData = Fx.crypto.ECC.encrypt(publicKey, str); 
    log.debug(encryptData) //dGVzdHRlc3Q=
    
    String privateKey = "MD4CAQAwEAYHKoZIzj0CAQYFK4EEAAoEJzAlAgEBBCA1IMt9uJOEdW7kB69aTDmSRdxbpESSDUhNd9/d8hM5lw=="
    String decryptData = Fx.crypto.ECC.decrypt(privateKey, encryptData);
    log.info(decryptData) //testtest
    
    

**注意事项**

>   * 公钥与私钥成对使用
> 


### # 2\. decrypt ECC解密

> `ECCAPI.decrypt(<String privateKey>, <String data>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
privateKey | String | 解密私钥，生成的算法为ECC，格式为Base64， PKCS8标准存储 | 是  
data | String | 需要加密的数据 | 是  
  
**Groovy 举例**
    
    
    String publicKey = "MFYwEAYHKoZIzj0CAQYFK4EEAAoDQgAEwGWFaJ9DfFEOerfs9ONP9nPozdJmpQ+tTy2xUknp8YVJnx/93dWXbRI6oGEwAVY26zWMcNPLtd8ekbPWbfSjUA=="
    String str = "testtest";
    String encryptData = Fx.crypto.ECC.encrypt(publicKey, str); 
    log.debug(encryptData) //dGVzdHRlc3Q=
    
    String privateKey = "MD4CAQAwEAYHKoZIzj0CAQYFK4EEAAoEJzAlAgEBBCA1IMt9uJOEdW7kB69aTDmSRdxbpESSDUhNd9/d8hM5lw=="
    String decryptData = Fx.crypto.ECC.decrypt(privateKey, encryptData);
    log.info(decryptData) //testtest
    
    

**注意事项**

>   * 公钥私钥成对使用
> 


### # 3\. sign ECC签名

> `ECCAPI.sign(<String privateKey>, <String data>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
privateKey | String | 签名私钥，生成的算法为ECC，格式为Base64， PKCS8标准存储 | 是  
data | String | 需要加密的数据 | 是  
  
**Groovy 举例**
    
    
    String publicKey = "MFYwEAYHKoZIzj0CAQYFK4EEAAoDQgAEwGWFaJ9DfFEOerfs9ONP9nPozdJmpQ+tTy2xUknp8YVJnx/93dWXbRI6oGEwAVY26zWMcNPLtd8ekbPWbfSjUA=="
    String privateKey = "MD4CAQAwEAYHKoZIzj0CAQYFK4EEAAoEJzAlAgEBBCA1IMt9uJOEdW7kB69aTDmSRdxbpESSDUhNd9/d8hM5lw=="
    String data = "testtest"
    
    String sign = Fx.crypto.ECC.sign(privateKey, data);
    
    boolean verifySign = Fx.crypto.ECC.verifySign(publicKey, sign, data)
    log.info(verifySign);
    
    

### # 4\. verifySign ECC验签

> `ECCAPI.verifySign(<String publicKey>, <String sign>, <String data>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
publicKey | String | 验签公钥，生成的算法为ECC，格式为Base64，X.509标准存储 | 是  
sign | String | 签名后的内容 | 是  
data | String | 原始内容 | 是  
  
**Groovy 举例**
    
    
    String publicKey = "MFYwEAYHKoZIzj0CAQYFK4EEAAoDQgAEwGWFaJ9DfFEOerfs9ONP9nPozdJmpQ+tTy2xUknp8YVJnx/93dWXbRI6oGEwAVY26zWMcNPLtd8ekbPWbfSjUA=="
    String privateKey = "MD4CAQAwEAYHKoZIzj0CAQYFK4EEAAoEJzAlAgEBBCA1IMt9uJOEdW7kB69aTDmSRdxbpESSDUhNd9/d8hM5lw=="
    String data = "testtest"
    
    String sign = Fx.crypto.ECC.sign(privateKey, data);
    
    boolean verifySign = Fx.crypto.ECC.verifySign(publicKey, sign, data)
    log.info(verifySign);
    
    

## # 参考类 com.fxiaoke.functions.api.RSAAPI

### # 1\. encrypt RSA加密

> `RSAAPI.encrypt(<String publicKey>, <String data>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
publicKey | String | 公钥 | 是  
data | String | 需要加密的数据 | 是  
  
**Groovy 举例**
    
    
    String publicKey =
    "MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAyVTOYRGyEZ2gjY+N4bsH" +
    "suSjy/WevRi5X7MXklwpcyHdIYGrw8si+PoGnGivMhL/tfmOAglAeVviF+QeebDs" +
    "6kKXwHB/PacSgx82Q4yQFS2UNfLOG6WQNIlPHZ1094cDFlVdcjxCSYcvgoBLZaws" +
    "GelKmnjk1cBUhleeZElKLPj7mF3yq4hehNewUv5W/eByUCZ0CUqnWFnKPJ/xUYqX" +
    "Fuvqx20cNYKhjAPKgDcKbNBGCKJW2uu1MMyDrxr5MKkn5gsDZ/P7AI0yy4UVbQ5C" +
    "qG4rfuAJZ/WZ7fx9PrGEUBYt0NX33tcXAO/denOwMp9N5HgJlJGlJzJ7esx/ex3K" +
    "wwIDAQAB"
    String originalContent = "testtest"
    String text = Fx.crypto.RSA.encrypt(publicKey,originalContent)
    log.info(text) 
    
    String privateKey =
        "MIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQDJVM5hEbIRnaCN" +
        "j43huwey5KPL9Z69GLlfsxeSXClzId0hgavDyyL4+gacaK8yEv+1+Y4CCUB5W+IX" +
        "5B55sOzqQpfAcH89pxKDHzZDjJAVLZQ18s4bpZA0iU8dnXT3hwMWVV1yPEJJhy+C" +
        "gEtlrCwZ6UqaeOTVwFSGV55kSUos+PuYXfKriF6E17BS/lb94HJQJnQJSqdYWco8" +
        "n/FRipcW6+rHbRw1gqGMA8qANwps0EYIolba67UwzIOvGvkwqSfmCwNn8/sAjTLL" +
        "hRVtDkKobit+4Aln9Znt/H0+sYRQFi3Q1ffe1xcA7916c7Ayn03keAmUkaUnMnt6" +
        "zH97HcrDAgMBAAECggEASEA9/AncrIOz3Xl6AlsbTTDOM2DHAbeAtv5PZD/cxCuP" +
        "7vlZCd+5gj4/5xuOW9sDl2uiccqeL68wuUAtS6CZtQwG55G3qAlwFEw8LgugnWkI" +
        "+j9ThgppcOEh2k/qbPYvvnEOIvPLGhYAj8W4yRj7jqTxF/RwsuDdtIR3HChNDUv+" +
        "DX4SNWbAeyjceT4k/2bnO/+nFnylxLj9j+DajKy869APQk+4wmT8o/lEC/+MX2Uy" +
        "IlC3YBGGwABJBIetAhj0RJi+6yjMk4GBnSGVPH1ehGy+cGTC6pFIupK+xYsGbd6S" +
        "/XJo+3GEfnpUq8E9ZrCpPym0wjFJYIeL6sztaJnKgQKBgQDnGJU3XJYAdh7EpIHQ" +
        "+yMtJPNIKZrZy4MZhWAPZRz6jwPocWlzg2B/jF4jydOlmccyXRGzqNyhSpYOxq7W" +
        "uawVk2XEfqMCBnWBt/3j452gTQXkq1UQ/jLT/qZRvvzhbCun3uX9OdBWS3V4em6E" +
        "yYi4SECaaGcdBY1jA5P6kElygwKBgQDfBxS+XKPpMvcOHrlSzXWQol47FA50Wx6S" +
        "DgIE+lBmp+sylZe8ONBdnX0jQO9Ce75x3J/eY7dsnZxRC2B7ZW6H6pjt7ex0RBNk" +
        "EfVjK7ykjttlXh2CX+WiT3oeY/DOz8pAU1deiUPAgIwR4ffbEgfhNQo1bf88lPhp" +
        "+nMnR8XSwQKBgEA4EJ9F11lhecNjg7+zSl8tOX4AMcv8Rf49ligxDRCD1a4udgNn" +
        "qtVHCJIhb/NA/J3+RwEKF+WqeHC6vbNl/XAxecJU/q99ZAIcQy2k/xSg0tZs1kLW" +
        "oQFQbp+g1109VhRcWMU5369bYNWOEFBOQPQU//7orF7gQB4XzHOAzShJAoGAcUj+" +
        "f2c9FvH9Td3LUsTsJ6hh5u5cHTw/ff7BhdfDyTEYJdyYc1IEfNjHPIX6QjHq3Zks" +
        "V2EdRX2VbhEyU9uE1mMShSCqT7BYjScWFuabbpbl2EqDALtHQDfQluk640HmwN/U" +
        "bD+a+4gQHfFC3bL976XqZpNV52bf+6zsmxI46MECgYA7auynp1+IUSrzF4sFtKfd" +
        "YaPGn82p+PdDVKoA6hnjrIwnC5k6nR7XfSRyVt2n9myQYufoZs9WHwwme9FXEPYd" +
        "qzJTqkMMtqh4jsGK1Uz95uUm3F0wZtvd0W17CrL9eR6My00oKXGcEMWJ+iGg7BSo" +
        "JvxtK9uvc7rTlcbqxqD3dw==";
    String decrypt = Fx.crypto.getRSA().decrypt(privateKey, text);
    log.info(decrypt);//testtest
    
    

### # 2\. decrypt RSA解密

> `RSAAPI.decrypt(<String privateKey>, <String data>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
privateKey | String | 私钥 | 是  
data | String | 需要解密的数据 | 是  
  
**Groovy 举例**
    
    
    String publicKey =
    "MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAyVTOYRGyEZ2gjY+N4bsH" +
    "suSjy/WevRi5X7MXklwpcyHdIYGrw8si+PoGnGivMhL/tfmOAglAeVviF+QeebDs" +
    "6kKXwHB/PacSgx82Q4yQFS2UNfLOG6WQNIlPHZ1094cDFlVdcjxCSYcvgoBLZaws" +
    "GelKmnjk1cBUhleeZElKLPj7mF3yq4hehNewUv5W/eByUCZ0CUqnWFnKPJ/xUYqX" +
    "Fuvqx20cNYKhjAPKgDcKbNBGCKJW2uu1MMyDrxr5MKkn5gsDZ/P7AI0yy4UVbQ5C" +
    "qG4rfuAJZ/WZ7fx9PrGEUBYt0NX33tcXAO/denOwMp9N5HgJlJGlJzJ7esx/ex3K" +
    "wwIDAQAB"
    String originalContent = "testtest"
    String text = Fx.crypto.RSA.encrypt(publicKey,originalContent)
    log.info(text) 
    
    String privateKey =
        "MIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQDJVM5hEbIRnaCN" +
        "j43huwey5KPL9Z69GLlfsxeSXClzId0hgavDyyL4+gacaK8yEv+1+Y4CCUB5W+IX" +
        "5B55sOzqQpfAcH89pxKDHzZDjJAVLZQ18s4bpZA0iU8dnXT3hwMWVV1yPEJJhy+C" +
        "gEtlrCwZ6UqaeOTVwFSGV55kSUos+PuYXfKriF6E17BS/lb94HJQJnQJSqdYWco8" +
        "n/FRipcW6+rHbRw1gqGMA8qANwps0EYIolba67UwzIOvGvkwqSfmCwNn8/sAjTLL" +
        "hRVtDkKobit+4Aln9Znt/H0+sYRQFi3Q1ffe1xcA7916c7Ayn03keAmUkaUnMnt6" +
        "zH97HcrDAgMBAAECggEASEA9/AncrIOz3Xl6AlsbTTDOM2DHAbeAtv5PZD/cxCuP" +
        "7vlZCd+5gj4/5xuOW9sDl2uiccqeL68wuUAtS6CZtQwG55G3qAlwFEw8LgugnWkI" +
        "+j9ThgppcOEh2k/qbPYvvnEOIvPLGhYAj8W4yRj7jqTxF/RwsuDdtIR3HChNDUv+" +
        "DX4SNWbAeyjceT4k/2bnO/+nFnylxLj9j+DajKy869APQk+4wmT8o/lEC/+MX2Uy" +
        "IlC3YBGGwABJBIetAhj0RJi+6yjMk4GBnSGVPH1ehGy+cGTC6pFIupK+xYsGbd6S" +
        "/XJo+3GEfnpUq8E9ZrCpPym0wjFJYIeL6sztaJnKgQKBgQDnGJU3XJYAdh7EpIHQ" +
        "+yMtJPNIKZrZy4MZhWAPZRz6jwPocWlzg2B/jF4jydOlmccyXRGzqNyhSpYOxq7W" +
        "uawVk2XEfqMCBnWBt/3j452gTQXkq1UQ/jLT/qZRvvzhbCun3uX9OdBWS3V4em6E" +
        "yYi4SECaaGcdBY1jA5P6kElygwKBgQDfBxS+XKPpMvcOHrlSzXWQol47FA50Wx6S" +
        "DgIE+lBmp+sylZe8ONBdnX0jQO9Ce75x3J/eY7dsnZxRC2B7ZW6H6pjt7ex0RBNk" +
        "EfVjK7ykjttlXh2CX+WiT3oeY/DOz8pAU1deiUPAgIwR4ffbEgfhNQo1bf88lPhp" +
        "+nMnR8XSwQKBgEA4EJ9F11lhecNjg7+zSl8tOX4AMcv8Rf49ligxDRCD1a4udgNn" +
        "qtVHCJIhb/NA/J3+RwEKF+WqeHC6vbNl/XAxecJU/q99ZAIcQy2k/xSg0tZs1kLW" +
        "oQFQbp+g1109VhRcWMU5369bYNWOEFBOQPQU//7orF7gQB4XzHOAzShJAoGAcUj+" +
        "f2c9FvH9Td3LUsTsJ6hh5u5cHTw/ff7BhdfDyTEYJdyYc1IEfNjHPIX6QjHq3Zks" +
        "V2EdRX2VbhEyU9uE1mMShSCqT7BYjScWFuabbpbl2EqDALtHQDfQluk640HmwN/U" +
        "bD+a+4gQHfFC3bL976XqZpNV52bf+6zsmxI46MECgYA7auynp1+IUSrzF4sFtKfd" +
        "YaPGn82p+PdDVKoA6hnjrIwnC5k6nR7XfSRyVt2n9myQYufoZs9WHwwme9FXEPYd" +
        "qzJTqkMMtqh4jsGK1Uz95uUm3F0wZtvd0W17CrL9eR6My00oKXGcEMWJ+iGg7BSo" +
        "JvxtK9uvc7rTlcbqxqD3dw==";
    String decrypt = Fx.crypto.getRSA().decrypt(privateKey, text);
    log.info(decrypt);//testtest
    
    

### # 3\. sign RSA签名

> `RSAAPI.sign(<String algorithm>, <String privateKey>, <String data>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
algorithm | String | RSA算法，映射信息SHA1->SHA1WithRSA,SHA256->SHA256WithRSA,MD5->MD5withRSA | 是  
privateKey | String | 私钥 | 是  
data | String | 需要签名的数据 | 是  
  
**Groovy 举例**
    
    
    String privateKey =
    "MIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQDJVM5hEbIRnaCN" +
    "j43huwey5KPL9Z69GLlfsxeSXClzId0hgavDyyL4+gacaK8yEv+1+Y4CCUB5W+IX" +
    "5B55sOzqQpfAcH89pxKDHzZDjJAVLZQ18s4bpZA0iU8dnXT3hwMWVV1yPEJJhy+C" +
    "gEtlrCwZ6UqaeOTVwFSGV55kSUos+PuYXfKriF6E17BS/lb94HJQJnQJSqdYWco8" +
    "n/FRipcW6+rHbRw1gqGMA8qANwps0EYIolba67UwzIOvGvkwqSfmCwNn8/sAjTLL" +
    "hRVtDkKobit+4Aln9Znt/H0+sYRQFi3Q1ffe1xcA7916c7Ayn03keAmUkaUnMnt6" +
    "zH97HcrDAgMBAAECggEASEA9/AncrIOz3Xl6AlsbTTDOM2DHAbeAtv5PZD/cxCuP" +
    "7vlZCd+5gj4/5xuOW9sDl2uiccqeL68wuUAtS6CZtQwG55G3qAlwFEw8LgugnWkI" +
    "+j9ThgppcOEh2k/qbPYvvnEOIvPLGhYAj8W4yRj7jqTxF/RwsuDdtIR3HChNDUv+" +
    "DX4SNWbAeyjceT4k/2bnO/+nFnylxLj9j+DajKy869APQk+4wmT8o/lEC/+MX2Uy" +
    "IlC3YBGGwABJBIetAhj0RJi+6yjMk4GBnSGVPH1ehGy+cGTC6pFIupK+xYsGbd6S" +
    "/XJo+3GEfnpUq8E9ZrCpPym0wjFJYIeL6sztaJnKgQKBgQDnGJU3XJYAdh7EpIHQ" +
    "+yMtJPNIKZrZy4MZhWAPZRz6jwPocWlzg2B/jF4jydOlmccyXRGzqNyhSpYOxq7W" +
    "uawVk2XEfqMCBnWBt/3j452gTQXkq1UQ/jLT/qZRvvzhbCun3uX9OdBWS3V4em6E" +
    "yYi4SECaaGcdBY1jA5P6kElygwKBgQDfBxS+XKPpMvcOHrlSzXWQol47FA50Wx6S" +
    "DgIE+lBmp+sylZe8ONBdnX0jQO9Ce75x3J/eY7dsnZxRC2B7ZW6H6pjt7ex0RBNk" +
    "EfVjK7ykjttlXh2CX+WiT3oeY/DOz8pAU1deiUPAgIwR4ffbEgfhNQo1bf88lPhp" +
    "+nMnR8XSwQKBgEA4EJ9F11lhecNjg7+zSl8tOX4AMcv8Rf49ligxDRCD1a4udgNn" +
    "qtVHCJIhb/NA/J3+RwEKF+WqeHC6vbNl/XAxecJU/q99ZAIcQy2k/xSg0tZs1kLW" +
    "oQFQbp+g1109VhRcWMU5369bYNWOEFBOQPQU//7orF7gQB4XzHOAzShJAoGAcUj+" +
    "f2c9FvH9Td3LUsTsJ6hh5u5cHTw/ff7BhdfDyTEYJdyYc1IEfNjHPIX6QjHq3Zks" +
    "V2EdRX2VbhEyU9uE1mMShSCqT7BYjScWFuabbpbl2EqDALtHQDfQluk640HmwN/U" +
    "bD+a+4gQHfFC3bL976XqZpNV52bf+6zsmxI46MECgYA7auynp1+IUSrzF4sFtKfd" +
    "YaPGn82p+PdDVKoA6hnjrIwnC5k6nR7XfSRyVt2n9myQYufoZs9WHwwme9FXEPYd" +
    "qzJTqkMMtqh4jsGK1Uz95uUm3F0wZtvd0W17CrL9eR6My00oKXGcEMWJ+iGg7BSo" +
    "JvxtK9uvc7rTlcbqxqD3dw=="
    String str  = "testtest"
    def sign = Fx.crypto.RSA.sign("SHA256",privateKey,str)
    
    String publicKey =
    "MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAyVTOYRGyEZ2gjY+N4bsH" +
    "suSjy/WevRi5X7MXklwpcyHdIYGrw8si+PoGnGivMhL/tfmOAglAeVviF+QeebDs" +
    "6kKXwHB/PacSgx82Q4yQFS2UNfLOG6WQNIlPHZ1094cDFlVdcjxCSYcvgoBLZaws" +
    "GelKmnjk1cBUhleeZElKLPj7mF3yq4hehNewUv5W/eByUCZ0CUqnWFnKPJ/xUYqX" +
    "Fuvqx20cNYKhjAPKgDcKbNBGCKJW2uu1MMyDrxr5MKkn5gsDZ/P7AI0yy4UVbQ5C" +
    "qG4rfuAJZ/WZ7fx9PrGEUBYt0NX33tcXAO/denOwMp9N5HgJlJGlJzJ7esx/ex3K" +
    "wwIDAQAB"
    def ret = Fx.crypto.RSA.verifySign("SHA256", publicKey, sign, str)
    log.info(ret)//true
    
    

### # 4\. verifySign RSA验签

> `RSAAPI.verifySign(<String algorithm>, <String publicKey>, <String sign>, <String data>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
algorithm | String | RSA算法，映射信息SHA1->SHA1WithRSA,SHA256->SHA256WithRSA,MD5->MD5withRSA | 是  
publicKey | String | 公钥 | 是  
sign | String | 签名后的内容 | 是  
data | String | 原数据 | 是  
  
**Groovy 举例**
    
    
    String privateKey =
    "MIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQDJVM5hEbIRnaCN" +
    "j43huwey5KPL9Z69GLlfsxeSXClzId0hgavDyyL4+gacaK8yEv+1+Y4CCUB5W+IX" +
    "5B55sOzqQpfAcH89pxKDHzZDjJAVLZQ18s4bpZA0iU8dnXT3hwMWVV1yPEJJhy+C" +
    "gEtlrCwZ6UqaeOTVwFSGV55kSUos+PuYXfKriF6E17BS/lb94HJQJnQJSqdYWco8" +
    "n/FRipcW6+rHbRw1gqGMA8qANwps0EYIolba67UwzIOvGvkwqSfmCwNn8/sAjTLL" +
    "hRVtDkKobit+4Aln9Znt/H0+sYRQFi3Q1ffe1xcA7916c7Ayn03keAmUkaUnMnt6" +
    "zH97HcrDAgMBAAECggEASEA9/AncrIOz3Xl6AlsbTTDOM2DHAbeAtv5PZD/cxCuP" +
    "7vlZCd+5gj4/5xuOW9sDl2uiccqeL68wuUAtS6CZtQwG55G3qAlwFEw8LgugnWkI" +
    "+j9ThgppcOEh2k/qbPYvvnEOIvPLGhYAj8W4yRj7jqTxF/RwsuDdtIR3HChNDUv+" +
    "DX4SNWbAeyjceT4k/2bnO/+nFnylxLj9j+DajKy869APQk+4wmT8o/lEC/+MX2Uy" +
    "IlC3YBGGwABJBIetAhj0RJi+6yjMk4GBnSGVPH1ehGy+cGTC6pFIupK+xYsGbd6S" +
    "/XJo+3GEfnpUq8E9ZrCpPym0wjFJYIeL6sztaJnKgQKBgQDnGJU3XJYAdh7EpIHQ" +
    "+yMtJPNIKZrZy4MZhWAPZRz6jwPocWlzg2B/jF4jydOlmccyXRGzqNyhSpYOxq7W" +
    "uawVk2XEfqMCBnWBt/3j452gTQXkq1UQ/jLT/qZRvvzhbCun3uX9OdBWS3V4em6E" +
    "yYi4SECaaGcdBY1jA5P6kElygwKBgQDfBxS+XKPpMvcOHrlSzXWQol47FA50Wx6S" +
    "DgIE+lBmp+sylZe8ONBdnX0jQO9Ce75x3J/eY7dsnZxRC2B7ZW6H6pjt7ex0RBNk" +
    "EfVjK7ykjttlXh2CX+WiT3oeY/DOz8pAU1deiUPAgIwR4ffbEgfhNQo1bf88lPhp" +
    "+nMnR8XSwQKBgEA4EJ9F11lhecNjg7+zSl8tOX4AMcv8Rf49ligxDRCD1a4udgNn" +
    "qtVHCJIhb/NA/J3+RwEKF+WqeHC6vbNl/XAxecJU/q99ZAIcQy2k/xSg0tZs1kLW" +
    "oQFQbp+g1109VhRcWMU5369bYNWOEFBOQPQU//7orF7gQB4XzHOAzShJAoGAcUj+" +
    "f2c9FvH9Td3LUsTsJ6hh5u5cHTw/ff7BhdfDyTEYJdyYc1IEfNjHPIX6QjHq3Zks" +
    "V2EdRX2VbhEyU9uE1mMShSCqT7BYjScWFuabbpbl2EqDALtHQDfQluk640HmwN/U" +
    "bD+a+4gQHfFC3bL976XqZpNV52bf+6zsmxI46MECgYA7auynp1+IUSrzF4sFtKfd" +
    "YaPGn82p+PdDVKoA6hnjrIwnC5k6nR7XfSRyVt2n9myQYufoZs9WHwwme9FXEPYd" +
    "qzJTqkMMtqh4jsGK1Uz95uUm3F0wZtvd0W17CrL9eR6My00oKXGcEMWJ+iGg7BSo" +
    "JvxtK9uvc7rTlcbqxqD3dw=="
    String str  = "testtest"
    def sign = Fx.crypto.RSA.sign("SHA256",privateKey,str)
    
    String publicKey =
    "MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAyVTOYRGyEZ2gjY+N4bsH" +
    "suSjy/WevRi5X7MXklwpcyHdIYGrw8si+PoGnGivMhL/tfmOAglAeVviF+QeebDs" +
    "6kKXwHB/PacSgx82Q4yQFS2UNfLOG6WQNIlPHZ1094cDFlVdcjxCSYcvgoBLZaws" +
    "GelKmnjk1cBUhleeZElKLPj7mF3yq4hehNewUv5W/eByUCZ0CUqnWFnKPJ/xUYqX" +
    "Fuvqx20cNYKhjAPKgDcKbNBGCKJW2uu1MMyDrxr5MKkn5gsDZ/P7AI0yy4UVbQ5C" +
    "qG4rfuAJZ/WZ7fx9PrGEUBYt0NX33tcXAO/denOwMp9N5HgJlJGlJzJ7esx/ex3K" +
    "wwIDAQAB"
    def ret = Fx.crypto.RSA.verifySign("SHA256", publicKey, sign, str)
    log.info(ret)//true
    
    

## # 参考类 com.fxiaoke.functions.api.HexAPI

### # 1\. encode Hex编码

> `HexAPI.encode(<String data>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
data | String | 需要编码的数据 | 是  
  
**Groovy 举例**
    
    
    def str = 'testtest'
    def encode = Fx.crypto.hex.encode(Strings.toUTF8Bytes(str))
    log.info(encode) //7465737474657374
    
    def decode = Fx.crypto.hex.decode(encode)
    log.info(StringUtils.toUTF8String(decode)) //testtest
    
    

**注意事项**

>   * 加解密的数据如果参数是byte[]类型的，需要注意数据是Base64、Hex、还是普通字符串，对应转为byte[]的方式是不一样的；
> 


### # 2\. decode Hex编码

> `HexAPI.decode(<String data>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
data | String | 需要解码的数据 | 是  
  
**Groovy 举例**
    
    
    def str = 'testtest'
    def encode = Fx.crypto.hex.encode(Strings.toUTF8Bytes(str))
    log.info(encode) //7465737474657374
    
    def decode = Fx.crypto.hex.decode(encode)
    log.info(StringUtils.toUTF8String(decode)) //testtest
    
    

**注意事项**

>   * 加解密的数据如果参数是byte[]类型的，需要注意数据是Base64、Hex、还是普通字符串，对应转为byte[]的方式是不一样的；
> 


## # 参考类 com.fxiaoke.functions.api.HmacAPI

### # 1\. encrypt Hmac加密

> `HmacAPI.encrypt(<String algorithm>, <String secret>, <String data>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
algorithm | String | 加密算法，支持的加密算法 HmacMD5,HmacSHA1,HmacSHA256,HmacSHA384,HmacSHA512 | 是  
secret | String | 秘钥 | 是  
data | String | 需要加密码的数据 | 是  
  
**Groovy 举例**
    
    
    String algorithm = "HmacMD5"
    String secret = 'secret'
    String content = 'testtest'
    byte[] data1 = Fx.crypto.hmac.encrypt(algorithm, secret, content)
    byte[] data2 = Fx.crypto.hmac.encrypt(algorithm, secret.getBytes(), content)
    
    

**注意事项**

>   * 支持的加密算法 HmacMD5,HmacSHA1,HmacSHA256,HmacSHA384,HmacSHA512
>   * 加解密的数据如果参数是byte[]类型的，需要注意数据是Base64、Hex、还是普通字符串，对应转为byte[]的方式是不一样的；
> 


### # 2\. encrypt Hmac加密

> `HmacAPI.encrypt(<String algorithm>, <byte[] secret>, <String data>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
algorithm | String | 加密算法，支持的加密算法 HmacMD5,HmacSHA1,HmacSHA256,HmacSHA384,HmacSHA512 | 是  
secret | byte[] | 秘钥 | 是  
data | String | 需要加密码的数据 | 是  
  
**Groovy 举例**
    
    
    String algorithm = "HmacMD5"
    String secret = 'secret'
    String content = 'testtest'
    byte[] data1 = Fx.crypto.hmac.encrypt(algorithm, secret, content)
    byte[] data2 = Fx.crypto.hmac.encrypt(algorithm, secret.getBytes(), content)
    
    

**注意事项**

>   * 支持的加密算法 HmacMD5,HmacSHA1,HmacSHA256,HmacSHA384,HmacSHA512
>   * 加解密的数据如果参数是byte[]类型的，需要注意数据是Base64、Hex、还是普通字符串，对应转为byte[]的方式是不一样的；
> 


## # 参考类 com.fxiaoke.functions.api.SymmetryAPI

### # 1\. encrypt 对称加密，iv类型为String

> `SymmetryAPI.encrypt(<String algorithm>, <byte[] privateKey>, <byte[] data>, <byte[] iv>, <String mode>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
algorithm | String | 对称加密算法，支持算法AES->AES/ECB/PKCS5Padding，DES->DES/ECB/PKCS5Padding，DESede->DESede/ECB/PKCS5Padding | 是  
privateKey | byte[] | 秘钥，秘钥长度16/24/32个字节，对应AES 128/192/256位密钥长度 | 是  
data | byte[] | 需要加密码的数据 | 是  
iv | byte[] | 可选参数，向量 | \--  
mode | String | 可选参数， 加密与填充模式 | \--  
  
**Groovy 举例**
    
    
    byte[] input = Strings.toUTF8Bytes("testtest")
    byte[] key1 = Strings.toUTF8Bytes("1234567812345678") //秘钥长度16/24/32个字节，对应AES 128/192/256位密钥长度
    
    byte[] encrypt1 = Fx.crypto.symmetry.encrypt("AES", key1, input)
    //使用指定iv+填充模式
    byte[] encrypt2 = Fx.crypto.getSymmetry().encrypt("AES", key1, input, '1234567812345678', "AES/CBC/PKCS5Padding");
    byte[] encrypt3 = Fx.crypto.getSymmetry().encrypt("AES", key1, input, '1234567812345678'.getBytes(), "AES/CBC/PKCS5Padding");
    
    

**注意事项**

>   * 支持的加密算法 AES\DES\3DES
>   * 加解密的数据如果参数是byte[]类型的，需要注意数据是Base64、Hex、还是普通字符串，对应转为byte[]的方式是不一样的；
> 


### # 2\. encrypt 对称加密，iv类型为byte[]

> `SymmetryAPI.encrypt(<String algorithm>, <byte[] privateKey>, <byte[] data>, <String iv>, <String mode>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
algorithm | String | 对称加密算法，支持算法AES->AES/ECB/PKCS5Padding，DES->DES/ECB/PKCS5Padding，DESede->DESede/ECB/PKCS5Padding | 是  
privateKey | byte[] | 秘钥，秘钥长度16/24/32个字节，对应AES 128/192/256位密钥长度 | 是  
data | byte[] | 需要加密码的数据 | 是  
iv | String | 可选参数，向量 | \--  
mode | String | 可选参数， 加密与填充模式 | \--  
  
**Groovy 举例**
    
    
    byte[] input = Strings.toUTF8Bytes("testtest")
    byte[] key1 = Strings.toUTF8Bytes("1234567812345678") //秘钥长度16/24/32个字节，对应AES 128/192/256位密钥长度
    
    byte[] encrypt1 = Fx.crypto.symmetry.encrypt("AES", key1, input)
    //使用指定iv+填充模式
    byte[] encrypt2 = Fx.crypto.getSymmetry().encrypt("AES", key1, input, '1234567812345678', "AES/CBC/PKCS5Padding");
    
    

**注意事项**

>   * 加解密的数据如果参数是byte[]类型的，需要注意数据是Base64、Hex、还是普通字符串，对应转为byte[]的方式是不一样的；
> 


### # 3\. decrypt 对称解密，iv类型为String

> `SymmetryAPI.decrypt(<String algorithm>, <byte[] privateKey>, <byte[] data>, <String iv>, <String mode>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
algorithm | String | 对称加密算法，支持算法AES->AES/ECB/PKCS5Padding，DES->DES/ECB/PKCS5Padding，DESede->DESede/ECB/PKCS5Padding | 是  
privateKey | byte[] | 秘钥，秘钥长度16/24/32个字节，对应AES 128/192/256位密钥长度 | 是  
data | byte[] | 需要解密的数据 | 是  
iv | String | 可选参数，向量 | \--  
mode | String | 可选参数， 加密与填充模式 | \--  
  
**Groovy 举例**
    
    
    byte[] input = Strings.toUTF8Bytes("原始内容12341")
    String iv = "NIfb&95GUY86Gfgh"
    String mode = "AES/CBC/PKCS5Padding"
    byte[] key1 = Strings.toUTF8Bytes("1234567890abcdef") //秘钥，秘钥长度16/24/32个字节，对应AES 128/192/256位密钥长度
    byte[] e1 = Fx.crypto.symmetry.encrypt("AES", key1, input, iv, mode)
    byte[] d1 = Fx.crypto.symmetry.decrypt("AES", key1, e1, iv, mode)
    log.info(Strings.toUTF8String(d1))
    
    

**注意事项**

>   * 加解密的数据如果参数是byte[]类型的，需要注意数据是Base64、Hex、还是普通字符串，对应转为byte[]的方式是不一样的；
> 


### # 4\. decrypt 对称解密，iv类型为byte[]

> `SymmetryAPI.decrypt(<String algorithm>, <byte[] privateKey>, <byte[] data>, <byte[] iv>, <String mode>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
algorithm | String | 对称加密算法，支持算法AES->AES/ECB/PKCS5Padding，DES->DES/ECB/PKCS5Padding，DESede->DESede/ECB/PKCS5Padding | 是  
privateKey | byte[] | 秘钥，秘钥长度16/24/32个字节，对应AES 128/192/256位密钥长度 | 是  
data | byte[] | 需要解密的数据 | 是  
iv | byte[] | 可选参数，向量 | \--  
mode | String | 可选参数， 加密与填充模式 | \--  
  
**Groovy 举例**
    
    
    byte[] input = Strings.toUTF8Bytes("原始内容12341")
    byte[] iv = [18, 52, 86, 120, -112, -85, -51, -17, 18, 52, 86, 120, -112, -85, -51, -17]
    String mode = "AES/CBC/PKCS5Padding"
    byte[] key1 = Strings.toUTF8Bytes("1234567890abcdef") //秘钥，秘钥长度16/24/32个字节，对应AES 128/192/256位密钥长度
    byte[] e1 = Fx.crypto.symmetry.encrypt("AES", key1, input, iv, mode)
    byte[] d1 = Fx.crypto.symmetry.decrypt("AES", key1, e1, iv, mode)
    log.info(Strings.toUTF8String(d1))
    
    

**注意事项**

>   * 加解密的数据如果参数是byte[]类型的，需要注意数据是Base64、Hex、还是普通字符串，对应转为byte[]的方式是不一样的；
> 


## # 参考类 com.fxiaoke.functions.api.SM4API

### # 1\. encrypt SM4加密

> `SM4API.encrypt(<String key>, <string data>, <String mode>, <String iv>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
key | String | 秘钥 | 是  
data | string | 需要加密的数据 | 是  
mode | String | 加密与填充模式 | 是  
iv | String | 可选参数，向量 | 是  
  
**Groovy 举例**
    
    
    def key = "1234567812345678" 
    def data = "testtest"
    def mode = "SM4/CBC/PKCS5Padding"
    def iv = "1234567812345678" //16位
    def encrypt = Fx.crypto.SM4.encrypt(key, data, mode, iv)
    
    def decrypt = Fx.crypto.SM4.decrypt(key, encrypt, mode, iv)
    log.info(StringUtils.toUTF8String(decrypt))//testtest
    
    

**注意事项**

>   * 支持的加密算法 AES\DES\3DES
>   * 加解密的数据如果参数是byte[]类型的，需要注意数据是Base64、Hex、还是普通字符串，对应转为byte[]的方式是不一样的；
> 


### # 2\. decrypt SM4解密

> `SM4API.decrypt(<String key>, <byte data>, <String mode>, <String iv>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
key | String | 秘钥 | 是  
data | byte | 需要解密的数据 | 是  
mode | String | 加密与填充模式 | 是  
iv | String | 可选参数，向量 | 是  
  
**Groovy 举例**
    
    
    def key = "1234567812345678" 
    def data = "testtest"
    def mode = "SM4/CBC/PKCS5Padding"
    def iv = "1234567812345678" //16位
    def encrypt = Fx.crypto.SM4.encrypt(key, data, mode, iv)
    
    def decrypt = Fx.crypto.SM4.decrypt(key, encrypt, mode, iv)
    log.info(StringUtils.toUTF8String(decrypt))//testtest
    
    

**注意事项**

>   * 加解密的数据如果参数是byte[]类型的，需要注意数据是Base64、Hex、还是普通字符串，对应转为byte[]的方式是不一样的；
> 


## # 参考类 com.fxiaoke.functions.api.SM2API

### # 1\. encode SM2加密

> `SM2API.encode(<String input>, <byte pubKey>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
input | String | 需要加密的数据 | 是  
pubKey | byte | 加密的公钥（Hex格式） | 是  
  
**Groovy 举例**
    
    
    def str = 'testtest'
    def pubKey = "04e02df2e298eb9f1069905e6fd9f73bb74a2fe7c7d3a74952b7d3929a6ff7992f2d91e36ccb3c2b6a0860945ecfe68ffca181558e823280ab8fd9356893832c97"
    String encode = Fx.crypto.getSM2().encode(str, pubKey);
    log.debug(encode)//BMm7yAGdIYra3YFNftcqpP557b46CrqblXRxrXFHSv8AX1rc7UjqLQrWpZZfQeH/fViF/SLjPBqHAQCfVI1l3uV8M94F/IjxWqYhG01jXmyEGXUZ7hHrpMFyLhOUCZpJNkekHiQvRIdk
    String decode = Fx.crypto.SM2.decode(encode, "2e8b0080a153226d5e01903def442677ba6667e15732334619d22a3591f1869c")
    log.debug(decode)//testtest
    
    

**注意事项**

>   * 加解密的数据如果参数是byte[]类型的，需要注意数据是Base64、Hex、还是普通字符串，对应转为byte[]的方式是不一样的；
> 


### # 2\. decode SM2解密

> `SM2API.decode(<String input>, <byte prvKey>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
input | String | 要解密的数据（Base64格式） | 是  
prvKey | byte | 加密的私钥（Hex格式） | 是  
  
**Groovy 举例**
    
    
    def str = 'testtest'
    def pubKey = "04e02df2e298eb9f1069905e6fd9f73bb74a2fe7c7d3a74952b7d3929a6ff7992f2d91e36ccb3c2b6a0860945ecfe68ffca181558e823280ab8fd9356893832c97"
    String encode = Fx.crypto.getSM2().encode(str, pubKey);
    log.debug(encode)//BMm7yAGdIYra3YFNftcqpP557b46CrqblXRxrXFHSv8AX1rc7UjqLQrWpZZfQeH/fViF/SLjPBqHAQCfVI1l3uV8M94F/IjxWqYhG01jXmyEGXUZ7hHrpMFyLhOUCZpJNkekHiQvRIdk
    String decode = Fx.crypto.SM2.decode(encode, "2e8b0080a153226d5e01903def442677ba6667e15732334619d22a3591f1869c")
    log.debug(decode)//testtest
    
    

**注意事项**

>   * 加解密的数据如果参数是byte[]类型的，需要注意数据是Base64、Hex、还是普通字符串，对应转为byte[]的方式是不一样的；
> 


### # 3\. sign SM2加签

> `SM2API.sign(<String privteKey>, <String body>, <String mode>, <String userId>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
privteKey | String | 私钥（Hex格式） | 是  
body | String | 需要加签的字符串 | 是  
mode | String | 签名算法模式 | 是  
userId | String | 国密要求，要求加入签名者id | 是  
  
**Groovy 举例**
    
    
    def privteKey = '00a5c420b11eb7d6324ae2dcfee96e626d8f5e2e3ff9ae17d657ee3907803e33a6'
    def str = 'test'
    def mode = 'SM3withSM2' //密文 （当mode为SM3withSM2时是Hex格式，为SM2时是Base64格式）
    def userId = '1234567812345678'
    
    //String 签名后的数据（当mode为SM3withSM2时是Hex格式，为SM2时是Base64格式）
    String sign = Fx.crypto.SM2.sign(privteKey, str, mode, userId)
    log.debug(sign)
    
    def publicKeyStr = '04483a5548e42bcac3bacaa1997ef26cfe9240c313fd570a613e8184f2a11af5f41107b75060778f93b422e396cf47926ccb1a149cdb516d89fdfe325605b3752d' 
    
    boolean success = Fx.crypto.SM2.verify(publicKeyStr, str, sign, mode, userId)
    log.debug(success) //true
    
    

**注意事项**

>   * 支持加签的算法支持 SM3withSM2, SM2两种
>   * 加解密的数据如果参数是byte[]类型的，需要注意数据是Base64、Hex、还是普通字符串，对应转为byte[]的方式是不一样的；
> 


### # 4\. verify SM2验签

> `SM2API.verify(<String publicKeyStr>, <String body>, <String signatureStr>, <String mode>, <String userId>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
publicKeyStr | String | 公钥（Hex格式字符串） | 是  
body | String | 需要加签的字符串 | 是  
signatureStr | String | 密文 （当mode为SM3withSM2时是Hex格式，为SM2时是Base64格式） | 是  
mode | String | 签名算法模式 | 是  
userId | String | 国密要求，要求加入签名者id | 是  
  
**Groovy 举例**
    
    
    def privteKey = '00a5c420b11eb7d6324ae2dcfee96e626d8f5e2e3ff9ae17d657ee3907803e33a6'
    def str = 'test'
    def mode = 'SM3withSM2' //密文 （当mode为SM3withSM2时是Hex格式，为SM2时是Base64格式）
    def userId = '1234567812345678'
    
    //String 签名后的数据（当mode为SM3withSM2时是Hex格式，为SM2时是Base64格式）
    String sign = Fx.crypto.SM2.sign(privteKey, str, mode, userId)
    log.debug(sign)
    
    def publicKeyStr = '04483a5548e42bcac3bacaa1997ef26cfe9240c313fd570a613e8184f2a11af5f41107b75060778f93b422e396cf47926ccb1a149cdb516d89fdfe325605b3752d' 
    
    boolean success = Fx.crypto.SM2.verify(publicKeyStr, str, sign, mode, userId)
    log.debug(success) //true
    
    

**注意事项**

>   * 验签支持SM2,SM3withSM2两种模式,支持加签的算法支持 SM3withSM2, SM2两种
>   * 加解密的数据如果参数是byte[]类型的，需要注意数据是Base64、Hex、还是普通字符串，对应转为byte[]的方式是不一样的；
> 


## # 参考类 com.fxiaoke.functions.api.SM3API

### # 1\. encrypt sm3加签

> `SM3API.encrypt(<String str>, <String key>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
str | String | 需要加密数据 | 是  
key | String | 秘钥，可选参数 | 是  
  
**Groovy 举例**
    
    
    def str = 'testtest'
    String encrypt = Fx.crypto.SM3.encrypt("testtest")
    log.debug(encrypt)//6cdfdbc1f5b70b1dd580db3b44ba12f3e0070d8eea439573fc9f22aaaf6a073c
    boolean verify = Fx.crypto.SM3.verify("testtest", encrypt)
    log.debug(verify)//true
    
    

**注意事项**

>   * 加解密的数据如果参数是byte[]类型的，需要注意数据是Base64、Hex、还是普通字符串，对应转为byte[]的方式是不一样的；
> 


### # 2\. verify sm3验签

> `SM3API.verify(<String str>, <String hexString>, <String key>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
str | String | 之前数据 | 是  
hexString | String | 加密后数据 | 是  
key | String | 秘钥，可选参数 | 是  
  
**Groovy 举例**
    
    
    def str = 'testtest'
    String encrypt = Fx.crypto.SM3.encrypt("testtest")
    log.debug(encrypt)//6cdfdbc1f5b70b1dd580db3b44ba12f3e0070d8eea439573fc9f22aaaf6a073c
    boolean verify = Fx.crypto.SM3.verify("testtest", encrypt)
    log.debug(verify)//true
    
    

**注意事项**

>   * 加解密的数据如果参数是byte[]类型的，需要注意数据是Base64、Hex、还是普通字符串，对应转为byte[]的方式是不一样的；
> 


[Fx.random](../RandomAPI/) [Fx.json](../JsonAPI/)

← [Fx.random](../RandomAPI/) [Fx.json](../JsonAPI/)→ 

  * 跟随系统 
  * 浅色模式 
  * 深色模式 
  * 阅读模式 


