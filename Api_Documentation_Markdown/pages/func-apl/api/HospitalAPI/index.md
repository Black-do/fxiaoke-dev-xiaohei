#  Fx.hospital

## # Fx.hospital

### # 1\. updateHospital 医院数据清洗

> `Fx.hospital.updateHospital()`

**Groovy 举例**
    
    
    // 医院等级对应含义：
    //0：无等级
    //1：一级
    //2：一级甲等
    //3：一级乙等
    //4：一级丙等
    //5：二级
    //6：二级甲等
    //7：二级乙等
    //8：二级丙等
    //9：三级
    //10：三级甲等
    //11：三级乙等
    //12：三级丙等
    //医院等级映射（医院库等级->crm对象上单选字段）,无需医院等级可不传
     Map levelMappings = [
      "0":"NX0f3im1Q",
      "1":"zbgZAGOF0",
      "2":"BeO329j4c",
      "3":"W3k2ckIcc",
      "4":"pLpRx6sc5",
      "5":"zmGAx3uvr",
      "6":"CrgOr0azE",
      "7":"u4vWS9Sit",
      "8":"f2E34oH61",
      "9":"3sqq01lRy",
      "10":"40vHB1xfa",
      "11":"4kzl2BbpE",
      "12":"sqamVsQ00"
    ]
    //需要清洗的数据集合（最多100条）
    List dataIdList = ["642645d0bca58400013719a3"]
    //   医疗库字段：
    //  name：医院名称
    //  alias：别名
    //  profit_attribute：盈利属性
    //  level：医院等级
    //  province：省份
    //  city：城市
    //  district：县区
    //  address：地址
    //  latitude_and_longitude：经纬度
    //  contact_phone_number：联系电话
    //  official_website：官网
    //  dean：院长
    //  bed_num：床位数
    //  daily_outpatient_num：日门诊量
    //  introduction：简介
    //  type：医院类型
     //医疗库字段->crm对象字段映射
    Map mappings = ["name":"url"]
    //必填字段：objectApiName、isUpdateNull、medicalRegister、mappings
    def(Boolean error, List data, String message) = Fx.hospital.updateHospital("AccountObj",dataIdList,mappings,true,"is_hospital_register",levelMappings)
    if (error) {
      log.info("error :" + message)
    }
    log.info(data)
    
    

**负责人：刘诗林liushilin**

### # 2\. initHospital 初始化医院

> `Fx.hospital.initHospital()`

**Groovy 举例**
    
    
    //  医疗库字段：
    //  name：医院名称
    //  alias：别名
    //  profit_attribute：盈利属性
    //  level：医院等级
    //  province：省份
    //  city：城市
    //  district：县区
    //  address：地址
    //  latitude_and_longitude：经纬度
    //  contact_phone_number：联系电话
    //  official_website：官网
    //  dean：院长
    //  bed_num：床位数
    //  daily_outpatient_num：日门诊量
    //  introduction：简介
    //  type：医院类型
    //医疗库字段->crm对象字段映射
    Map mappings = [
      "level":"field_Zi8Pw__c",
      "latitude_and_longitude":"location",
      "district":"district",
      "city":"city",
      "province":"province",
      "country":"country",
      "contact_phone_number":"tel",
      "official_website":"url",
      "address":"address",
      "name":"name"
    ]
    
    //   医院等级对应含义：
    //  0：无等级
    //  1：一级
    //  2：一级甲等
    //  3：一级乙等
    //  4：一级丙等
    //  5：二级
    //  6：二级甲等
    //  7：二级乙等
    //  8：二级丙等
    //  9：三级
    //  10：三级甲等
    //  11：三级乙等
    //  12：三级丙等
    
    //医院等级映射（医院库等级->crm对象上单选字段）,无需医院等级可不传
    Map levelMappings = [
      "0":"NX0f3im1Q",
      "1":"zbgZAGOF0",
      "2":"BeO329j4c",
      "3":"W3k2ckIcc",
      "4":"pLpRx6sc5",
      "5":"zmGAx3uvr",
      "6":"CrgOr0azE",
      "7":"u4vWS9Sit",
      "8":"f2E34oH61",
      "9":"3sqq01lRy",
      "10":"40vHB1xfa",
      "11":"4kzl2BbpE",
      "12":"4kzl2BbpE"
    ]
    //必填字段：hospitalObjectApiName、recordType、medicalRegister、mappings
    def(Boolean error, Integer data, String message) = Fx.hospital.initHospital("AccountObj","record_PRkkc__c","4","北京市",null,null,null,mappings,"is_hospital_register",levelMappings)
    if (error) {
      log.info("error :" + message)
    }
    log.info(data)
    
    

**负责人：刘诗林liushilin**

### # 3\. initDepartment 初始化科室

> `Fx.hospital.initDepartment()`

**Groovy 举例**
    
    
    // 医疗库科室字段：
    // name:科室名称
    // director:科室主任
    // classification:分类
    // introduction:科室简介
    // 医疗库科室字段->crm对象字段
    Map mappings = [
      "name":"name",
      "classification":"field_56YfM__c"
    ]
    
    //科室分类含义:
    //1:内科
    //2:外科
    //3:骨科
    //4:妇产科
    //5:男科
    //6:儿科
    //7:耳鼻喉头颈外科
    //8:眼科
    //9:口腔科
    //10:肿瘤科
    //11:皮肤性病科
    //12:中医科
    //13:传染病科
    //14:精神心理科
    //15:麻醉医学科
    //16:医学影像科
    //17:其他科室
    //科室分类映射（key:医疗库科室分类，value:crm对象科室分类）
    Map classificationMappings = [
      "0":"0",
      "1":"1",
      "2":"2",
      "3":"3",
      "4":"4",
      "5":"5",
      "6":"6",
      "7":"7",
      "8":"8",
      "9":"9",
      "10":"10",
      "11":"11",
      "13":"13",
      "14":"14",
      "15":"15",
      "16":"16",
      "17":"17",
      "12":"12"
    ]
    //必填字段：hospitalObjectApiName、departmentObjectApiName、recordType、objectId、mappings、medicalRegister、parentApiName
    def(Boolean error, Integer data, String message) = Fx.hospital.initDepartment("AccountObj","AccountObj","record_PRkkc__c","6440f25a8d392e00011ffbfb",null,mappings,"is_hospital_register",classificationMappings,"parent_account_id")
    if (error) {
      log.info("error :" + message)
    }
    log.info(data)
    
    

**负责人：刘诗林liushilin**

[Fx.userGroup](../UserGroupAPI/) [Fx.dataAuth](../DataAuthAPI/)

← [Fx.userGroup](../UserGroupAPI/) [Fx.dataAuth](../DataAuthAPI/)→ 

  * 跟随系统 
  * 浅色模式 
  * 深色模式 
  * 阅读模式 


