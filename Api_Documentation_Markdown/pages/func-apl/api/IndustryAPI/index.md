#  Fx.industry

## # Fx.industry

### # 1\. queryBidRelationById 查询关联公告

> `Fx.industry.queryBidRelationById(<string tenantId>, <string employeeId>, <string bidId>, <integer bidType>, <integer isInit>, <string source>, <string terminalType>)`

**参数说明**

入参格式

参数名称 | object | 描述 | 是否必填  
---|---|---|---  
tenantId | string | 企业ei | \--  
employeeId | string | 员工id | \--  
bidId | string | 公告id | 是  
bidType | integer | 一级公告类型筛选:1-招标;2-中标 | 是  
isInit | integer | 是否初始化。 0-是,1-不是 | \--  
source | string | 1:知了标讯 | \--  
terminalType | string | 终端类型 | \--  
  
出参格式

参数名称 | object | 描述  
---|---|---  
bidId | string | 公告id  
title | string | 公告标题  
bidType | integer | 一级公告类型 1-招标;2-中标  
bidSubType | integer | 二级公告类型筛选: 招标:10-采购意向,11-预招标,12-招标,13-变更公告,14-废标公告; 中标:21-中标候选人,22-中标结果,23-合同,24-验收公告  
publishTime | string | 公告发布时间 yyyy-MM-dd  
callerName | string | 招标单位名称  
winnerNames | array[string] | 中标单位名称  
budget | number | 招标预算  
winnerAmount | number | 中标金额  
fsProjectId | string | 纷享自定义项目id,该字段不可用,目前只支持数据平台用于区别历史关联公告使用  
sourceCreateTime | string | 第三方收录该条标讯的时间 yyyy-MM-dd HH:mm:ss  
  
出参样例
    
    
    {
      "bidRelationEntities": [
        {
          "bidId": "your_bid_id_value",
          "title": "your_title_value",
          "bidType": 1,
          "bidSubType": 10,
          "publishTime": "2024-11-02",
          "callerName": "your_caller_name_value",
          "winnerNames": [
            "your_winner_name_1",
            "your_winner_name_2"
          ],
          "budget": 10000.00,
          "winnerAmount": 9000.00,
          "fsProjectId": "your_fs_project_id_value",
          "sourceCreateTime": "2024-11-02 10:30:00"
        }
      ]
    }
    
    

**Groovy 举例**
    
    
    String bidId = "660587a82ce05c0a39a87e324efcd09093c171b3"
    Integer bidType = 2
    
    def(boolean error, Map data, String message) = Fx.industry.queryBidRelationById(bidId, bidType)
    if (error) {
      log.info("error: " + message)
    } else {
      log.info(data)
    }
    
    

**注意事项**

>   * 接口收费，请勿频繁调用
> 


### # 2\. getCompanyDetailsByNames 查询工商详情信息

> `Fx.industry.getCompanyDetailsByNames(<array companyName>, <integer argType>)`

**参数说明**

入参格式

参数名称 | object | 描述 | 是否必填  
---|---|---|---  
companyName | array[string] | 公司名称列表 / 统一社会信用代码 | 是  
argType | integer | 0:name 1:统一社会信用码  
| 是  
  
出参格式

参数名称 | object | 描述  
---|---|---  
companyInfoArgs | array[object] |   
companyInfoArgs | object | 描述  
---|---|---  
Key | string |   
Caption | string |   
Value | string |   
  
出参样例
    
    
    {
      "companyInfoArgs": [
        {
          "Key": "KeyNo",
          "Caption": "公司标识",
          "Value": "30079848"
        },
        {
          "Key": "Name",
          "Caption": "企业名称",
          "Value": "北京纷扬科技有限责任公司"
        },
        {
          "Key": "CreditCode",
          "Caption": "统一社会信用代码",
          "Value": "911101010648937416"
        },
        {
          "Key": "No",
          "Caption": "工商注册号",
          "Value": "110000450231294"
        },
        {
          "Key": "Status",
          "Caption": "企业状态",
          "Value": "存续（在营、开业、在册）"
        },
        {
          "Key": "EconKind",
          "Caption": "公司类型",
          "Value": "有限责任公司(台港澳法人独资)"
        },
        {
          "Key": "OperName",
          "Caption": "法定代表人",
          "Value": "罗旭"
        },
        {
          "Key": "RegistCapi",
          "Caption": "注册资本",
          "Value": "30000万美元"
        },
        {
          "Key": "TermDate",
          "Caption": "营业期限起止日期",
          "Value": "2013-04-10 至 2043-04-09"
        },
        {
          "Key": "BelongOrg",
          "Caption": "登记机关",
          "Value": "北京市东城区市场监督管理局"
        },
        {
          "Key": "CheckDate",
          "Caption": "核准日期",
          "Value": "2020-09-28"
        },
        {
          "Key": "Scope",
          "Caption": "经营范围",
          "Value": "研究、开发计算机软件、网路通信软件；提供计算机技术培训、技术咨询、技术开发、技术转让、技术服务；计算机系统服务；计算机维修；销售计算机、软件及辅助设备；图文设计；设计、制作、代理、发布广告；软件开发；销售通讯设备。（市场主体依法自主选择经营项目，开展经营活动；依法须经批准的项目，经相关部门批准后依批准的内容开展经营活动；不得从事国家和本市产业政策禁止和限制类项目的经营活动。）"
        },
        {
          "Key": "Address",
          "Caption": "企业地址",
          "Value": "北京市东城区和平里东街11号8号楼一层1-B10号"
        },
        {
          "Key": "Province",
          "Caption": "注册省份",
          "Value": "北京市"
        },
        {
          "Key": "StartDate",
          "Caption": "成立日期",
          "Value": "2013-04-10"
        },
        {
          "Key": "EndDate",
          "Caption": "注销日期",
          "Value": "2043-04-09"
        },
        {
          "Key": "UpdateDate ",
          "Caption": "更新日期",
          "Value": "2021-04-01"
        },
        {
          "Key": "PhoneNumber ",
          "Caption": "联系电话",
          "Value": "15001072681"
        },
        {
          "Key": "Email",
          "Caption": "邮箱",
          "Value": "lixj@fxiaoke.com"
        },
        {
          "Key": "WebSiteName",
          "Caption": "网站名称",
          "Value": "北京纷扬科技有限责任公司"
        },
        {
          "Key": "WebSiteUrl ",
          "Caption": "公司网站",
          "Value": "www.fxiaoke.com"
        },
        {
          "Key": "ShortStatus",
          "Caption": "经营状态",
          "Value": ""
        },
        {
          "Key": "industryName",
          "Caption": "行业",
          "Value": "科技推广和应用服务业"
        },
        {
          "Key": "city",
          "Caption": "注册城市",
          "Value": "市辖区"
        },
        {
          "Key": "district",
          "Caption": "注册区县",
          "Value": "东城区"
        },
        {
          "Key": "orgNumber",
          "Caption": "组织机构代码",
          "Value": "064893741"
        }
      ]
    }
    
    

**Groovy 举例**
    
    
    List companyName = ["北京百度网讯科技有限公司"]
    Integer argType = 0
    
    def(boolean error, Map data, String message) = Fx.industry.getCompanyDetailsByNames(companyName, argType)
    if (error) {
      log.info("error: " + message)
    } else {
      log.info(data)
    }
    
    

#### # 参考函数接口

  * 参考无



**注意事项**

>   * 接口收费，需要开通产品【批量工商信息查询函数调用包】
>   * 参数使用企业名称时需要使用完整企业名称
>   * argType=0或不传时companyName 传名称
>   * argType=2时companyName 传统一社会信用代码
>   * 单次函数调用最多查询50个企业信息
> 


### # 3\. getTempCacheData 邓白氏-查询企业查看缓存数据

> `Fx.industry.getTempCacheData(<string company_name>)`

**参数说明**

入参格式

参数名称 | object | 描述 | 是否必填  
---|---|---|---  
company_name | string |  | 是  
  
出参格式

参数名称 | object | 描述  
---|---|---  
KeyNo | string | 自定义编号  
TermStart | string | 回填：TermDate【营业期限起止日期】 （TermStart 至 TermEnd）  
TermEnd | string | 回填：TermDate【营业期限起止日期】 （TermStart 至 TermEnd）  
CheckDate | string | 核准日期  
Name | string | 公司名称  
No | string | 注册号  
BelongOrg | string | 登记机关  
OperName | string | 法定代表人  
StartDate | string | 回填中显示为【营业期间自】 实际为 成立日期 ，但是回填中有成立日期 CompanyStartDate （取StartDate，若为空则取 termStart），回填的描述中需要废弃该字段  
EndDate | string | 回填中显示为【营业期限至】 实际为 空 ， （回填中取的规则是 EndDate，若为空则取 termEnd），回填的描述中需要废弃该字段  
CompanyStartDate | string | 企业成立日期  
Status | string | 登记状态  
Province | string | 注册省份  
UpdatedDate | string | 更新日期  
CreditCode | string | 统一社会信用代码  
RegistCapi | string | 注册资本  
RegistCapiDesc | string | 注册资本描述  
EconKind | string | 类型  
Address | string | 企业地址  
Scope | string | 经营范围  
ContactInfo | object |   
industryName | string | 所属行业  
industryL1Name | string | 所属行业层级1名称  
industryL2Name | string | 所属行业层级3名称  
industryL3Name | string | 所属行业层级4名称  
industryL4Name | string | 所属行业层级4名称  
city | string | 注册城市  
district | string | 注册区县  
orgNumber | string | 组织机构代码  
expendSource | string | 经费来源  
regUnit | string | 举办单位  
actualCapi | string | 实缴资本  
actualCapiDesc | string | 实缴资本描述  
socialSecurityNumber | string | 职工参保人数  
historyName | string | 曾用名  
qualificationType | string | 纳税人资质  
employNumber | string | 人员规模  
nameEn | string | 英文名  
identificationNumber | string | 纳税人识别号  
provinceCode | string | 注册省份（新）  
cityCode | string | 注册城市（新）  
districtCode | string | 注册区县（新）  
countryCode | string | 注册国家  
dunsCode | string | 邓式编码  
principalName | string | 负责人名字  
principalJob | string | 负责人职务  
sales | string | 销售额  
salesUnit | string | 销售额单位  
entityType | string | 实体类型  
logo | string | 企业标志图片链接  
listingStatus | string | 上市状态  
stockType | string | 股票类型 type  
cancelDate | string | 注销日期 cancel_date  
revokeDate | string | 吊销日期 revoke_date  
dataSource | string | 数据来源  
shortName | string | 简称  
postalCode | string | 邮政编码  
principalInfos | array[object] | 高管信息  
stockInfos | array[object] | 上市信息  
assessmentInfos | array[object] | 第三方评价  
familyTreeInfos | array[object] | 公司家族树  
impMatters | string | 重要事项  
ContactInfo | object | 描述  
---|---|---  
phone | string | 联系电话  
email | string | 电子邮箱  
fax | string | 传真  
principalInfos | object | 描述  
---|---|---  
name | string | 高管姓名  
job | string | 高管职务  
department | string | 高管所在部门  
stockInfos | object | 描述  
---|---|---  
stockSymbol | string | 股票代码  
exchange | string | 交易所  
price | string | 股票价格  
assessmentInfos | object | 描述  
---|---|---  
rating | string | 评级  
agency | string | 评级机构  
familyTreeInfos | object | 描述  
---|---|---  
parentCompany | string | 母公司名称  
subsidiaries | array[string] | 子公司列表  
  
出参样例
    
    
    {
      "Result": {
        "entityType": null,
        "postalCode": "94025-1452",
        "principalInfos": [
          {
            "fullName": "SUSAN LI",
            "jobTitle": "Chief Financial Officer"
          },
          {
            "fullName": "JAVIER OLIVAN",
            "jobTitle": "Chief Operating Officer"
          },
          {
            "fullName": "ANDREW BOSWORTH",
            "jobTitle": "Chief Technology Officer"
          },
          {
            "fullName": "JENNIFER G NEWSTEAD",
            "jobTitle": "Officer"
          },
          {
            "fullName": "DAVID WEHNER",
            "jobTitle": "Officer"
          },
          {
            "fullName": "CHRISTOPHER K COX",
            "jobTitle": "Officer"
          }
        ],
        "stockInfos": [
          {
            "tickerName": "NASDAQ:META",
            "exchangeName": "NASDAQ",
            "country": "USA",
            "primary": true
          },
          {
            "tickerName": "Santiago:METACL",
            "exchangeName": "Santiago",
            "country": "Chile",
            "primary": false
          },
          {
            "tickerName": "Italian:FB",
            "exchangeName": "Italian",
            "country": "Italy",
            "primary": false
          },
          {
            "tickerName": "XETRA:FB2A",
            "exchangeName": "XETRA",
            "country": "Germany",
            "primary": false
          },
          {
            "tickerName": "Munich:FB20",
            "exchangeName": "Munich",
            "country": "Germany",
            "primary": false
          },
          {
            "tickerName": "Frankfurt:FB20",
            "exchangeName": "Frankfurt",
            "country": "Germany",
            "primary": false
          },
          {
            "tickerName": "Lima:META",
            "exchangeName": "Lima",
            "country": "Peru",
            "primary": false
          },
          {
            "tickerName": "Munich:FB2A",
            "exchangeName": "Munich",
            "country": "Germany",
            "primary": false
          },
          {
            "tickerName": "Frankfurt:FB2A",
            "exchangeName": "Frankfurt",
            "country": "Germany",
            "primary": false
          },
          {
            "tickerName": "Ukrainian:FB",
            "exchangeName": "Ukrainian",
            "country": "Ukraine",
            "primary": false
          },
          {
            "tickerName": "Berlin:FB20",
            "exchangeName": "Berlin",
            "country": "Germany",
            "primary": false
          },
          {
            "tickerName": "Buenos Aires:META",
            "exchangeName": "Buenos Aires",
            "country": "Argentina",
            "primary": false
          },
          {
            "tickerName": "Vienna:META",
            "exchangeName": "Vienna",
            "country": "Austria",
            "primary": false
          },
          {
            "tickerName": "Berlin:FB2A",
            "exchangeName": "Berlin",
            "country": "Germany",
            "primary": false
          },
          {
            "tickerName": "Stuttgart:FB2A",
            "exchangeName": "Stuttgart",
            "country": "Germany",
            "primary": false
          },
          {
            "tickerName": "Bulgarian:FB2A",
            "exchangeName": "Bulgarian",
            "country": "Bulgaria",
            "primary": false
          },
          {
            "tickerName": "Dusseldorf:FB2A",
            "exchangeName": "Dusseldorf",
            "country": "Germany",
            "primary": false
          },
          {
            "tickerName": "KASE (Kazakhstan):META_KZ",
            "exchangeName": "KASE (Kazakhstan)",
            "country": "Kazakhstan",
            "primary": false
          },
          {
            "tickerName": "NEO Exchange:META",
            "exchangeName": "NEO Exchange",
            "country": "Canada",
            "primary": false
          },
          {
            "tickerName": "Hamburg:FB2A",
            "exchangeName": "Hamburg",
            "country": "Germany",
            "primary": false
          },
          {
            "tickerName": "Hannover:FB2A",
            "exchangeName": "Hannover",
            "country": "Germany",
            "primary": false
          },
          {
            "tickerName": "San Paulo:M1TA34",
            "exchangeName": "San Paulo",
            "country": "Brazil",
            "primary": false
          },
          {
            "tickerName": "London:0QZI",
            "exchangeName": "London",
            "country": "Great Britain",
            "primary": false
          },
          {
            "tickerName": "Mexican:META",
            "exchangeName": "Mexican",
            "country": "Mexico",
            "primary": false
          }
        ],
        "assessmentInfos": [
          {
            "name": "Fortune 1000 Revenue Rank",
            "value": "31",
            "assessmentDate": "2023"
          },
          {
            "name": "Fortune 500",
            "value": "31",
            "assessmentDate": "2023"
          }
        ],
        "familyTreeInfos": [
          {
            "type": "globalUltimate",
            "address": "United States-California-Menlo Park-1601 Willow Rd",
            "dunsCode": "196337864",
            "name": "Meta Platforms, Inc.",
            "postalCode": "94025-1452"
          },
          {
            "type": "domesticUltimate",
            "address": "United States-California-Menlo Park-1601 Willow Rd",
            "dunsCode": "196337864",
            "name": "Meta Platforms, Inc.",
            "postalCode": "94025-1452"
          }
        ],
        "KeyNo": "196337864",
        "TermStart": "2004",
        "TeamEnd": "--",
        "CheckDate": null,
        "Name": "Meta Platforms, Inc.",
        "No": null,
        "BelongOrg": null,
        "OperName": "Mark Zuckerberg",
        "StartDate": "2004",
        "EndDate": "--",
        "Status": "Active",
        "Province": null,
        "UpdatedDate": null,
        "CreditCode": null,
        "RegistCapi": null,
        "RegistCapiDesc": null,
        "EconKind": "Corporation",
        "Address": "United States-California-Menlo Park-1601 Willow Rd",
        "Scope": "Information retrieval services",
        "ContactInfo": {
          "PhoneNumber": "6505434800",
          "Email": null,
          "WebSite": [
            {
              "Url": "www.facebook.com",
              "Name": "facebook.com"
            }
          ]
        },
        "industryName": "Information retrieval services",
        "city": null,
        "district": null,
        "orgNumber": null,
        "expendSource": null,
        "regUnit": null,
        "actualCapi": null,
        "actualCapiDesc": null,
        "socialSecurityNumber": null,
        "historyName": null,
        "qualificationType": null,
        "employNumber": "86482",
        "nameEn": null,
        "identificationNumber": null,
        "provinceCode": null,
        "cityCode": null,
        "districtCode": null,
        "countryCode": null,
        "dunsCode": "196337864",
        "principalName": "Mark Zuckerberg",
        "principalJob": "Chairman of the Board, Chief Executive Officer",
        "sales": "116609000000",
        "salesUnit": "USD",
        "listingStatus": "NormalListing",
        "stockType": null,
        "cancelDate": null,
        "revokeDate": null,
        "dataSource": null
      },
      "Paging": null
    }
    
    

**Groovy 举例**
    
    
    String companyName = "百度"
    def(boolean error, Map data, String message) = Fx.industry.getTempCacheData(companyName)
    if (error) {
      log.info("error: " + message)
    } else {
      log.info(data)
    }
    
    

#### # 参考函数接口

  * 参考无



**注意事项**

>   * 接口收费，请勿频繁调用，即使保存接口数据
> 


### # 4\. getInvestInfoByNames 查询企业对外投资信息

> `Fx.industry.getInvestInfoByNames(<array companyName>, <integer argType>)`

**参数说明**

入参格式

参数名称 | object | 描述 | 是否必填  
---|---|---|---  
companyName | array[string] | 公司名称列表 / 统一社会信用代码 | 是  
argType | integer | 0:name 1:统一社会信用码  
| 是  
  
出参格式

参数名称 | object | 描述  
---|---|---  
itemId | string |   
capital | string |   
companyId | string |   
money | string |   
companyType | string |   
companyName | string |   
operName | string |   
businessScope | string |   
stockProportion | number |   
started | string |   
status | string |   
  
出参样例
    
    
    {
      "message": "成功",
      "result": {
        "北京百度网讯科技有限公司": [
          {
            "itemId": "d98d5602fd6652f5e0032cf9879dd067",
            "companyId": "d98d5602fd6652f5e0032cf9879dd067",
            "money": "80.0万元",
            "companyName": "河南沸点网络科技有限公司",
            "operName": "李刚",
            "started": "2010-08-23",
            "source_type": "investment",
            "status": "存续（在营、开业、在册）"
          },
          {
            "itemId": "29c6091476e59c766acfd8b629cb6a89",
            "capital": "10.000000万人民币",
            "companyId": "29c6091476e59c766acfd8b629cb6a89",
            "money": "0.411043万元",
            "companyType": "有限责任公司(自然人投资或控股)",
            "companyName": "厦门千万时科技有限公司",
            "operName": "傅旭天",
            "businessScope": "许可项目：出版物零售；广播电视节目制作经营。（依法须经批准的项目，经相关部门批准后方可开展经营活动，具体经营项目以相关部门批准文件或许可证件为准）一般项目：科技推广和应用服务；教育咨询服务（不含涉许可审批的教育培训活动）；技术服务、技术开发、技术咨询、技术交流、技术转让、技术推广；人力资源服务（不含职业中介活动、劳务派遣服务）；技术推广服务；信息咨询服务（不含许可类信息咨询服务）；日用品销售；互联网销售（除销售需要许可的商品）；玩具销售；体育用品及器材零售；日用杂品销售；办公用品销售；日用百货销售；文具用品零售；文具用品批发；广告制作；品牌管理；广告发布；市场营销策划；劳务服务（不含劳务派遣）；软件销售；数字内容制作服务（不含出版发行）。（除依法须经批准的项目外，凭营业执照依法自主开展经营活动）。",
            "stockProportion": 0.041104,
            "started": "2022-04-01",
            "status": "存续（在营、开业、在册）"
          },
          {
            "itemId": "7dbc1ce570f2b2d249c2f0d96c0f6725",
            "capital": "100.000000万人民币",
            "companyId": "7dbc1ce570f2b2d249c2f0d96c0f6725",
            "money": "10.0万元",
            "companyType": "有限责任公司(自然人投资或控股)",
            "companyName": "沈阳分分钟企业管理有限公司",
            "operName": "王永强",
            "businessScope": "企业管理咨询。（依法须经批准的项目，经相关部门批准后方可开展经营活动。）",
            "stockProportion": 0.1,
            "started": "2010-12-06",
            "status": "注销"
          }
        ]
      },
      "status": 200
    }
    
    

**Groovy 举例**
    
    
    List companyName = ["北京百度网讯科技有限公司"]
    Integer argType = 0
    
    def(boolean error, Map data, String message) = Fx.industry.getInvestInfoByNames(companyName, argType)
    if (error) {
      log.info("error: " + message)
    } else {
      log.info(data)
    }
    
    

**注意事项**

>   * 接口收费，需要开通产品【工商信息函数-获取企业对外投资信息】
>   * 参数使用企业名称时需要使用完整企业名称
>   * argType=0或不传时companyName 传名称
>   * argType=1时companyName 传统一社会信用代码
>   * 单次函数调用最多查询50个企业信息
> 


**负责人：赵正豪zhenghao**

### # 5\. getCompanyBaseInfo 企业工商信息Action

> `Fx.industry.getCompanyBaseInfo(<string companyName>)`

**参数说明**

入参格式

参数名称 | object | 描述 | 是否必填  
---|---|---|---  
companyName | string | 企业名称/统一社会信用代码/组织机构代码/企业注册号 | 是  
  
出参格式

参数名称 | object | 企业基础信息响应实体  
---|---|---  
companyAbbreviation | string | 企业简称  
companyId | string | 企业ID  
companyName | string | 企业名称  
companyProfile | string | 企业简介  
industryL1Name | string | 一级行业  
industryL2Name | string | 二级行业  
industryL3Name | string | 三级行业  
industryL4Name | string | 四级行业  
stockExchange | string | 上市交易所  
stockName | string | 股票简称  
stockStatus | string | 上市状态 (上市,未上市)  
  
出参样例
    
    
    {
        "companyAbbreviation": "百度网讯",
        "companyId": "dd872327d13418fcc8cff2a726e613fc",
        "companyName": "北京百度网讯科技有限公司",
        "companyProfile": "北京百度网讯科技有限公司，2001-06-05日成立，经营范围包括一般项目：技术服务、技术开发、技术咨询、技术交流、技术转让、技术推广；计算机软硬件及辅助设备零售；软件开发；计算机系统服务；信息系统集成服务；数据处理服务；数字内容制作服务（不含出版发行）；软件销售；计算机软硬件及辅助设备批发；电子产品销售；电子元器件批发；电子元器件零售；机械设备租赁；广告制作；广告发布；广告设计、代理；专业设计服务；市场营销策划；会议及展览服务；信息技术咨询服务；企业管理咨询；家用电器销售；机械设备销售；五金产品批发；五金产品零售；玩具、动漫及游艺用品销售；游艺用品及室内游艺器材销售；照相机及器材销售；化妆品批发；化妆品零售；个人卫生用品销售；体育用品及器材批发；体育用品及器材零售；针纺织品销售；服装服饰零售；服装服饰批发；鞋帽零售；鞋帽批发；日用品销售；日用品批发；珠宝首饰零售；珠宝首饰批发；工艺美术品及礼仪用品销售（象牙及其制品除外）；工艺美术品及收藏品批发（象牙及其制品除外）；钟表销售；眼镜销售（不含隐形眼镜）；玩具销售；办公用品销售；摩托车及零配件零售；摩托车及零配件批发；仪器仪表销售；家具销售；塑料制品销售；建筑材料销售；通讯设备销售；食品销售（仅销售预包装食品）；保健食品（预包装）销售；货物进出口；技术进出口；进出口代理；汽车零部件及配件制造；汽车零配件零售；汽车零配件批发；汽车销售；健康咨询服务（不含诊疗服务）；票务代理服务；翻译服务；第一类医疗器械销售；第二类医疗器械销售；法律咨询（不含依法须律师事务所执业许可的业务）。（除依法须经批准的项目外，凭营业执照依法自主开展经营活动）许可项目：基础电信业务；第一类增值电信业务；第二类增值电信业务；网络文化经营；出版物零售；出版物批发；演出经纪；职业中介活动；广播电视节目制作经营；信息网络传播视听节目；互联网新闻信息服务；测绘服务。（依法须经批准的项目，经相关部门批准后方可开展经营活动，具体经营项目以相关部门批准文件或许可证件为准）（不得从事国家和本市产业政策禁止和限制类项目的经营活动。）",
        "industryL1Name": "科学研究和技术服务业",
        "industryL2Name": "科技推广和应用服务业",
        "industryL3Name": "其他科技推广服务业",
        "industryL4Name": "其他科技推广服务业",
        "stockExchange": "",
        "stockName": "",
        "stockStatus": "未上市"
      }
    
    

**Groovy 举例**
    
    
    List companyName = "北京百度网讯科技有限公司"
    
    def(boolean error, Map data, String message) = Fx.industry.getCompanyBaseInfo(companyName)
    if (error) {
      log.info("error: " + message)
    } else {
      log.info(data)
    }
    
    

**注意事项**

>   * 参数使用企业名称时需要使用完整企业名称 / 统一社会信用代码 / 企业注册号 / 组织机构代码
> 


**负责人：赵正豪zhenghao**

### # 6\. getCompanyOperationInfo 企业经营信息Action

> `Fx.industry.getCompanyOperationInfo(<string companyName>)`

**参数说明**

入参格式

参数名称 | object | 描述 | 是否必填  
---|---|---|---  
companyName | string | 企业名称/统一社会信用代码/组织机构代码/企业注册号 | 是  
  
出参格式

参数名称 | object | 企业经营信息响应实体  
---|---|---  
companyId | String | 企业工商数据唯一标识  
companyName | String | 企业名称  
reportAssetInfoList | Array[object] | 企业年报资产信息  
productInfoList | Array[object] | 企业产品信息  
competitiveProductInfoList | Array[object] | 企业竞品信息  
financingHistoryInfoList | Array[object] | 企业融资历史信息  
companyCustomerVOList | Array[object] | 企业主要客户及销售占比  
reportAssetInfoList | object | 描述  
---|---|---  
reportYear | integer | 年报年份  
totalAmount | string | 资产总额  
equityAmount | string | 所有者权益合计  
businessIncome | string | 销售总额(营业总收入)  
totalProfitAmount | string | 利润总额  
profitAmount | string | 净利润  
taxAmount | string | 纳税总额  
productInfoList | object | 描述  
---|---|---  
product | string | 产品名称  
yewu | string | 产品介绍  
hangye | string | 产品行业  
portraySearch | string | 搜索用产品画像标签  
competitiveProductInfoList | object | 描述  
---|---|---  
jingpinProduct | string | 竞品名称  
jingpinYewu | string | 竞品简介  
jingpinCompanyName | string | 竞品所属企业名称  
financingHistoryInfoList | object | 描述  
---|---|---  
round | string | 融资轮次  
realTime | string | 融资日期  
money | string | 融资金额  
investorName | string | 投资方  
value | string | 估值  
newsTitle | string | 新闻标题  
newsUrl | string | 新闻链接  
companyCustomerVOList | object | 描述  
---|---|---  
announcementDate | string | 时间戳  
amt | string | 销售金额（万元）  
logo | string | logo URL  
alias | string | 简称  
clientGraphId | integer | 客户 ID  
relationship | string | 关联关系  
clientName | string | 客户名称  
dataSource | string | 数据来源  
ratio | string | 销售占比  
  
出参样例
    
    
    {
        "companyCustomerVOList": [
          {
            "alias": "人寿保险",
            "amt": "",
            "announcementDate": "2025-05-23",
            "clientGraphId": 25556781,
            "clientName": "太平人寿保险有限公司",
            "dataSource": "招投标公告",
            "logo": "https://img5.tianyancha.com/logo/lll/70db9c452bb53d4052343d9da68999b8.png@!f_200x200",
            "ratio": "",
            "relationship": ""
          },
          {
            "alias": "",
            "amt": "0.00",
            "announcementDate": "2025-05-22",
            "clientGraphId": 0,
            "clientName": "吉林大学后勤服务集团",
            "dataSource": "招投标公告",
            "logo": "",
            "ratio": "",
            "relationship": ""
          },
          {
            "alias": "大学",
            "amt": "0.00",
            "announcementDate": "2025-05-22",
            "clientGraphId": 3225529490,
            "clientName": "吉林大学",
            "dataSource": "招投标公告",
            "logo": "",
            "ratio": "",
            "relationship": ""
          }
        ],
        "companyId": "dd872327d13418fcc8cff2a726e613fc",
        "companyName": "北京百度网讯科技有限公司",
        "competitiveProductInfoList": [
          {
            "jingpinCompanyName": "常州礼创网络科技有限公司",
            "jingpinProduct": "智慧聊天",
            "jingpinYewu": "智能聊天软件"
          }
        ],
        "financingHistoryInfoList": [
          {
            "investorName": "['红杉资本中国', '完美世界']",
            "money": "8亿人民币",
            "newsTitle": "百度文学再融 8 亿做价 40 亿 网文平台变身 IP 孵化器就能玩转资本市场？",
            "newsUrl": "https://www.chinaventure.com.cn/cmsmodel/news/detail/314273.shtml",
            "realTime": "2017-05-24",
            "round": "A轮",
            "value": "40亿人民币"
          }
        ],
        "productInfoList": [
          {
            "hangye": "",
            "portraySearch": "人工智能;高新技术企业;新基建;AI基础设施;社交与工具;聊天;工具类;日常应用;人工智能基础技术",
            "product": "小侃星球",
            "yewu": "聊天虚拟人应用"
          },
          {
            "hangye": "",
            "portraySearch": "文娱传媒;短视频平台;短视频;有专利;3C认证;高端招聘多;研发投入多;移动应用表现好;环境管理体系认证;内容创作;高新技术企业;视频平台;视频;文学;智能产品;2022中国VR50强企业榜单",
            "product": "百度Nani",
            "yewu": "短视频平台"
          }
        ],
        "reportAssetInfoList": [
          {
            "businessIncome": "企业选择不公示",
            "equityAmount": "企业选择不公示",
            "profitAmount": "企业选择不公示",
            "reportYear": 2022,
            "taxAmount": "企业选择不公示",
            "totalAmount": "企业选择不公示",
            "totalProfitAmount": "企业选择不公示"
          }
        ]
      }
    
    

**Groovy 举例**
    
    
    List companyName = "北京百度网讯科技有限公司"
    
    def(boolean error, Map data, String message) = Fx.industry.getCompanyOperationInfo(companyName)
    if (error) {
      log.info("error: " + message)
    } else {
      log.info(data)
    }
    
    

**注意事项**

>   * 参数使用企业名称时需要使用完整企业名称 / 统一社会信用代码 / 企业注册号 / 组织机构代码
> 


**负责人：赵正豪zhenghao**

### # 7\. getCompanyBidInfo 企业招投标信息Action

> `Fx.industry.getCompanyBidInfo(<string companyName>)`

**参数说明**

入参格式

参数名称 | object | 描述 | 是否必填  
---|---|---|---  
companyName | string | 企业名称/统一社会信用代码/组织机构代码/企业注册号 | 是  
  
出参格式

参数名称 | object | 企业招投标信息响应实体  
---|---|---  
companyId | String | 企业ID  
companyName | String | 企业名称  
bidInfoList | Array[object] | 招投标信息列表  
bidInfoList | object | 描述  
---|---|---  
purchaser | string | 招标人  
abs | string | 摘要信息  
link | string | 链接  
content | string | 正文存储路径  
involvingMoney | string | 涉及金额  
title | string | 标题  
publishTime | string | 发布时间  
noticeType | string | 公告类型  
  
出参样例
    
    
    {
        "bidInfoList": [
          {
            "abs": "",
            "content": "bid/7e/93/7e93238167ebb2ff53a261fc355fe7a1.html",
            "involvingMoney": "",
            "link": "http://www.ggzy.gov.cn/information/html/a/440000/0104/202312/29/00448045a74012cb41458212261e8d6a3b4f.shtml",
            "publishTime": "2023-12-29",
            "purchaser": "广东省高速公路发展股份有限公司佛开分公司",
            "title": "基于雷达卡口视频的异常事件感知和车流数字化服务采购项目"
          },
          {
            "abs": "",
            "content": "bid/5a/05/5a057345e8d4575d9589366c85bf87ca.html",
            "involvingMoney": "[[1, \"中标价\", 1060000.0], [2, \"投标报价\", 1060000.0]]",
            "link": "https://bulletin.cebpubservice.com/resultBulletin/2023-12-28/11783492.html",
            "publishTime": "2023-12-28",
            "purchaser": "北京银行股份有限公司",
            "title": "北京银行智库平台智能化能力升级项目成交结果公示"
          }
        ],
        "companyId": "dd872327d13418fcc8cff2a726e613fc",
        "companyName": "北京百度网讯科技有限公司"
      }
    
    

**Groovy 举例**
    
    
    List companyName = "北京百度网讯科技有限公司"
    
    def(boolean error, Map data, String message) = Fx.industry.getCompanyBidInfo(companyName)
    if (error) {
      log.info("error: " + message)
    } else {
      log.info(data)
    }
    
    

**注意事项**

>   * 参数使用企业名称时需要使用完整企业名称 / 统一社会信用代码 / 企业注册号 / 组织机构代码
> 


**负责人：赵正豪zhenghao**

### # 8\. getCompanyNewsInfo 企业新闻动态信息Action

> `Fx.industry.getCompanyNewsInfo(<string companyName>)`

**参数说明**

入参格式

参数名称 | object | 描述 | 是否必填  
---|---|---|---  
companyName | string | 企业名称/统一社会信用代码/组织机构代码/企业注册号 | 是  
  
出参格式

参数名称 | object | 描述  
---|---|---  
message | string |   
result | object |   
status | integer |   
result | object | 描述  
---|---|---  
companyId | string |   
companyName | string |   
honorList | array[object] |   
newsList | array[object] |   
topList | array[object] |   
honorList | object | 描述  
---|---|---  
city | string |   
endDate | string |   
honorClass | string |   
honorName | string |   
honorNo | string |   
honorType | string |   
province | string |   
publishDate | string |   
publishOrg | string |   
publishYear | string |   
sourceTitle | string |   
sourceUrl | string |   
startDate | string |   
newsList | object | 描述  
---|---|---  
abstracts | string |   
docid | string |   
emotion | integer |   
rtm | integer |   
tags | array[string] |   
title | string |   
uri | string |   
website | string |   
topList | object | 描述  
---|---|---  
name | string |   
nameIn | string |   
precedence | integer |   
releaseDate | string |   
source | string |   
type | string |   
  
出参样例
    
    
    {
      "message": "查询成功",
      "result": {
        "companyId": "dd872327d13418fcc8cff2a726e613fc",
        "companyName": "北京百度网讯科技有限公司",
        "honorList": [
          {
            "city": "北京市",
            "endDate": "2025-08-08T16:00:00",
            "honorClass": "国家级",
            "honorName": "高新技术企业",
            "honorNo": "20232010610301",
            "honorType": "科技型企业",
            "province": "北京市",
            "publishDate": "2023-08-08T16:00:00",
            "publishOrg": "北京市科学技术委员会,中关村科技园区管理委员会",
            "publishYear": "2023",
            "sourceTitle": "中关村高新技术企业库（截止2023年7月）",
            "sourceUrl": "",
            "startDate": "2023-08-08T16:00:00"
          }
        ],
        "newsList": [
          {
            "abstracts": "金融界2025年6月6日消息，国家知识产权局信息显示，北京百度网讯科技有限公司申请一项名为“一种基于大语言模型的文本与对象之间的转换方法及装置”的专利，公开号CN120104132A，申请日期为2023年12月。专利摘要显示，本公开提供了一种基于大语言模型的文本与对象之间的转换方法及装置，涉及软件开发技术领域，尤其涉及自然语言处理和人工智能技术领域。具体实现方案为：获取待转换文本以及用户设置的第一解析协议，其中第一解析协议包括待转换文本的文本字段与待转换对象的成员变量之间的第一映射关系。然后针对待转换文本包括的文本字段，按照第一映射关系，确定该文本字段对应的成员变量的成员变量名，并将确定的成员",
            "docid": "g9n8f0rskg",
            "emotion": 0,
            "rtm": 1749175527000,
            "tags": [
              "合作经营",
              "成果奖项"
            ],
            "title": "百度申请基于大语言模型的文本与对象转换方法及装置专利，提高了文本与对象之间的转换灵活性",
            "uri": "https://c.m.163.com/news/a/K1C456CD0519QIKK.html",
            "website": "网易号"
          }
        ],
        "topList": [
          {
            "name": "2025多模态AI大模型排行",
            "nameIn": "百度",
            "precedence": 8,
            "releaseDate": "2025-05-26 00:00:00",
            "source": "硅谷动力",
            "type": "品牌产品榜"
          }
        ]
      },
      "status": 200
    }
    
    

**Groovy 举例**
    
    
    List companyName = "北京百度网讯科技有限公司"
    
    def(boolean error, Map data, String message) = Fx.industry.getCompanyNewsInfo(companyName)
    if (error) {
      log.info("error: " + message)
    } else {
      log.info(data)
    }
    
    

**注意事项**

>   * 参数使用企业名称时需要使用完整企业名称 / 统一社会信用代码 / 企业注册号 / 组织机构代码
> 


**负责人：赵正豪zhenghao**

## # 参考类 无

## # 参考类 无

[Fx.netdisk](../NetdiskAPI/) [Fx.userGroup](../UserGroupAPI/)

← [Fx.netdisk](../NetdiskAPI/) [Fx.userGroup](../UserGroupAPI/)→ 

  * 跟随系统 
  * 浅色模式 
  * 深色模式 
  * 阅读模式 


