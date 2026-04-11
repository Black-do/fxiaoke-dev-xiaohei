#  Fx.location

## # Fx.location

### # 1\. findByMobile 查询单个号码归属地

> `Fx.location.findByMobile()`

**Groovy 举例**
    
    
    def(Boolean error, Map result, String errroMessage) = Fx.location.findByMobile("11111111111")
    //返回值新增两个参数
    //province_code  String 类型，省份的地区码
    //city_code String 类型，市的地区码
    
    

**负责人：吕杰lvjie**

### # 2\. findByMobiles 批量查询号码归属地

> `Fx.location.findByMobiles()`

**Groovy 举例**
    
    
    def(Boolean error, Map result, String errroMessage) = Fx.location.findByMobiles(["11111111111", "12252225222"])
    
    

**负责人：吕杰lvjie**

### # 3\. distance 根据经纬度，计算两点间的距离

> `Fx.location.distance()`

**Groovy 举例**
    
    
    BigDecimal longitude1 = 116.374409 //地点1的精度
    BigDecimal latitude1 = 39.942939//地点1的纬度
    BigDecimal longitude2 = 116.375721//地点2的精度
    BigDecimal latitude2 = 39.942925 //地点2的纬度
    def (Boolean error,Long result,String errorMessage) = Fx.location.distance(longitude1,latitude1,longitude2,latitude2)
    if( error ){
        Fx.log.info("计算错误 : "  + errorMessage)
    }else{
        Fx.log.info(result)
    }
    
    

**负责人：吕杰lvjie**

### # 4\. findCountryAreaLabel 根据地区码，查询地区省市中文

> `Fx.location.findCountryAreaLabel()`

**Groovy 举例**
    
    
    String label = Fx.location.findCountryAreaLabel("249","province")
    
    

**负责人：吕杰lvjie**

### # 5\. findCountryAreaCode 根据地区省市中文，查询地区码

> `Fx.location.findCountryAreaCode()`

**Groovy 举例**
    
    
    String provinceCode = Fx.location.findCountryAreaCode("黑龙江","province")
    
    

**负责人：吕杰lvjie**

### # 6\. getCountryAreaOptions 查询国家省市区

> `Fx.location.getCountryAreaOptions()`

**Groovy 举例**
    
    
    def(Boolean error, Map data, String mesage) = Fx.location.getCountryAreaOptions()
    if (error) {
      log.info("error: " + mesage)
    }
    log.info(data['country'])
    log.info(data['province'])
    log.info(data['city'])
    log.info(data['district'])
    
    

**负责人：吕杰lvjie**

### # 7\. getZoningCodeByLabel 根据省市区的Label查标准行政区划编码

> `Fx.location.getZoningCodeByLabel()`

**Groovy 举例**
    
    
    def(Boolean error, Map data, String mesage) = Fx.location.getZoningCodeByLabel("city", "北京市")
    if (error) {
      log.info("error: " + mesage)
    }
    log.info(data)
    
    

**负责人：吕杰lvjie**

[Fx.json](../JsonAPI/) [Fx.message](../MessageAPI/)

← [Fx.json](../JsonAPI/) [Fx.message](../MessageAPI/)→ 

  * 跟随系统 
  * 浅色模式 
  * 深色模式 
  * 阅读模式 


