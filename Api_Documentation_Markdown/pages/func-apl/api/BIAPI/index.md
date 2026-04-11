#  Fx.BI

## # Fx.BI

### # 1\. getRules 查询BI统计图目标规则名称和id

> `Fx.BI.getRules(<String viewId>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
viewId | String | 视图ID，用于指定要查询的视图目标规则 | 是  
  
出参格式

参数名称 | 类型 | 描述  
---|---|---  
userFilters | Array[object] | 用户自定义过滤条件  
defaultFilterOptions | Array[Object] | 默认过滤选项列表  
measureFields | Array[Object] | 度量字段列表  
rules | Array[Object] | 规则列表  
defaultFilterOptions | Object | 描述  
---|---|---  
defaultOrNot | Integer | 是否为默认选项，1表示是，0表示否  
optionID | String | 选项ID  
optionName | String | 选项名称  
measureFields | Object | 描述  
---|---|---  
fieldName | String | 字段名称  
fieldID | String | 字段ID  
rules | Object | 描述  
---|---|---  
nodeName | String | 节点名称  
enumId | String | 枚举ID  
optionCode | String | 选项代码  
isSelected | Integer | 是否被选中，0表示未选中  
childList | Array[object] | 子节点列表  
isHaveChild | Integer | 是否有子节点，0表示没有  
parentID | String | 父节点ID  
order | Integer | 排序顺序  
  
出参样例
    
    
    [
        {
            "userFilters": [],
            "defaultFilterOptions": [
                {
                    "defaultOrNot": 1,
                    "optionID": "BI_59a3e59333b39e09b44e9db1",
                    "optionName": "全部"
                },
                {
                    "defaultOrNot": 0,
                    "optionID": "BI_59a3e59333b49e29b04e0db2",
                    "optionName": "上架"
                },
                {
                    "defaultOrNot": 0,
                    "optionID": "BI_59a3e59333b49e29b04e0qb2",
                    "optionName": "下架"
                },
                {
                    "defaultOrNot": 0,
                    "optionID": "BI_59a3e59333b39e09b44e9db2",
                    "optionName": "我负责的"
                },
                {
                    "defaultOrNot": 0,
                    "optionID": "BI_59a3e59333b39e09b44e9db3",
                    "optionName": "我参与的"
                },
                {
                    "defaultOrNot": 0,
                    "optionID": "BI_59a3e59333b39e09b44e9db4",
                    "optionName": "我负责部门的"
                },
                {
                    "defaultOrNot": 0,
                    "optionID": "BI_59a3e59333b39e09b44e9db5",
                    "optionName": "我下属负责的"
                },
                {
                    "defaultOrNot": 0,
                    "optionID": "BI_59a3e59333b39e09b44e9db6",
                    "optionName": "我下属参与的"
                },
                {
                    "defaultOrNot": 0,
                    "optionID": "BI_59a3e59333b39e09b44e9db7",
                    "optionName": "共享给我的"
                }
            ],
            "measureFields": [
                {
                    "fieldName": "月目标值",
                    "fieldID": "BI_a9766b081e45837da44f71c6965bbaf5"
                },
                {
                    "fieldName": "完成值",
                    "fieldID": "BI_d42f1fad5601af69cd6d1a30c54b2fc9"
                }
            ],
            "rules": [
                {
                    "nodeName": "产品多语ces",
                    "enumId": "63bd3a0aa811cf0001ab4b3a",
                    "optionCode": "63bd3a0aa811cf0001ab4b3a",
                    "isSelected": 0,
                    "childList": [],
                    "isHaveChild": 0,
                    "parentID": "-2",
                    "order": 0
                },
                {
                    "nodeName": "产品",
                    "enumId": "63dbd41411782d00018f37cd",
                    "optionCode": "63dbd41411782d00018f37cd",
                    "isSelected": 0,
                    "childList": [],
                    "isHaveChild": 0,
                    "parentID": "-2",
                    "order": 0
                }
            ]
        }
    ]
    
    

**Groovy 举例**
    
    
    def(isError3,data3,errorMsg3) = Fx.BI.getRules("BI_60f787675f32870001714eb8")
    if(!isError3){
      log.info("数据信息:"+data3["page"])
    }else{
      log.info("查询失败:"+errorMsg3)
    }
    
    

**负责人：翟付杰Jeffrey**

### # 2\. getTargetCompletion 获取目标完成率

> `Fx.BI.getTargetCompletion(<String viewId>, <类型 userFilters>, <Array targetIds>, <String optionId>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
viewId | String | 视图ID | 是  
userFilters | 类型 | 用户过滤条件 | 是  
targetIds | Array[String] | 目标ID列表 | 是  
optionId | String | 场景Id | 是  
userFilters | 类型 | 用户过滤条件 | 是否必填  
---|---|---|---  
userFilters | Array[Object] | 用户过滤条件列表 | 是  
ruleFilters | 类型 |  | 是  
isShowDimension | Integer | 是否显示维度，0表示否，1表示是 | 是  
userFilters | Object | 描述 | 是否必填  
---|---|---|---  
fieldId | String | 字段ID | 是  
targetType | Integer | 目标类型：0-个人，1-部门，2-日期 | 是  
value | Array[类型] | 过滤值，根据目标类型不同可能是数字、数组或字符串 | 是  
ruleFilters | 类型 | 描述 | 是否必填  
---|---|---|---  
optionCode | Array[String] | 选项代码列表 | 是  
isChild | Integer | 是否为子项，0表示否，1表示是 | 是  
  
出参格式

参数名称 | 类型 | 描述  
---|---|---  
Param1 | Boolean | 是否发生错误，false表示无错误  
Param2 | Array | 字段数据列表  
Param3 | String | 错误信息，无错误时为空字符串  
  
出参样例
    
    
    [
        false,
        [
            {
                "fieldName": "物料编码",
                "value": [
                    {
                        "formattedValue": "123",
                        "formattedShowValue": "123",
                        "valueCode": "123$$65672428c70f2f00017e0788",
                        "value": "123"
                    },
                    {
                        "formattedValue": "可爱的小dog",
                        "formattedShowValue": "可爱的小dog",
                        "valueCode": "可爱的小dog$$65af8fc7ea1c430007aa6d13",
                        "value": "可爱的小dog"
                    },
                    {
                        "formattedValue": "sy#f00>Feb*",
                        "formattedShowValue": "sy#f00>Feb*",
                        "valueCode": "sy#f00>Feb*",
                        "value": "sy#f00>Feb*"
                    }
                ],
                "fieldId": "BI_5be1388756fc11448c4567d8"
            },
            {
                "fieldName": "负责人",
                "value": [
                    {
                        "formattedValue": "中-bi2",
                        "formattedShowValue": "中-bi2",
                        "valueCode": "1067",
                        "value": "中-bi2"
                    },
                    {
                        "formattedValue": "中-小哈(已停用)",
                        "formattedShowValue": "中-小哈(已停用)",
                        "valueCode": "3264",
                        "value": "中-小哈(已停用)"
                    },
                    {
                        "formattedValue": "sy#f00>Feb*",
                        "formattedShowValue": "sy#f00>Feb*",
                        "valueCode": "sy#f00>Feb*",
                        "value": "sy#f00>Feb*"
                    }
                ],
                "fieldId": "BI_5be1388756fc11448c456809"
            },
            {
                "fieldName": "月目标值",
                "value": [
                    {
                        "formattedValue": "1.20万",
                        "formattedShowValue": "11,988",
                        "valueCode": 11988,
                        "value": 11988
                    },
                    {
                        "formattedValue": "12.00",
                        "formattedShowValue": "12",
                        "valueCode": 12,
                        "value": 12
                    },
                    {
                        "formattedValue": "1.20万",
                        "formattedShowValue": "12,000",
                        "valueCode": 12000.0,
                        "value": 12000.0
                    }
                ],
                "fieldId": "BI_a9766b081e45837da44f71c6965bbaf5"
            },
            {
                "fieldName": "完成值",
                "value": [
                    {
                        "formattedValue": "0.00",
                        "formattedShowValue": "0.00",
                        "valueCode": 0,
                        "value": 0
                    },
                    {
                        "formattedValue": "0.00",
                        "formattedShowValue": "0.00",
                        "valueCode": 0,
                        "value": 0
                    },
                    {
                        "formattedValue": "0.00",
                        "formattedShowValue": "0.00",
                        "valueCode": 0,
                        "value": 0
                    }
                ],
                "fieldId": "BI_d42f1fad5601af69cd6d1a30c54b2fc9"
            }
        ],
        ""
    ]
    
    

**Groovy 举例**
    
    
    Map userFilters = [
            "userFilters"    : [
                    [
                            "fieldId"   : "BI_5bcec12156fc11160c10043d",
                            "targetType": 0,// （0个人，1部门，2日期）
                            "value"     : [1067]
                    ],
                    [
                            "fieldId"   : "BI_5bcec12156fc11160c100443",
                            "targetType": 2,// （0个人，1部门，2日期）
                            "value"     : ["2021-01-01", "2021-02-01"]
                    ]
            ],
            "ruleFilters"    : [
                    "optionCode": ["6079743a2822bb000156541b"],
                    "isChild"   : 0
            ],
            "isShowDimension": 0
    ]
    def rules = Fx.BI.getTargetCompletion("BI_60f787675f32870001714eb8", userFilters, ["BI_nvv76jyhwg6qoojfw9ike31u"], "BI_59a3e59333b39e09b44e9db1")
    Fx.log.info(rules)
    
    

**负责人：翟付杰Jeffrey**

### # 3\. loadViewData 图表数据加载

> `Fx.BI.loadViewData(<String viewId>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
viewId | String | 视图ID，用于指定要查询的视图 | 是  
  
出参格式

参数名称 | 类型 | 描述  
---|---|---  
displayFields | Object[object] | 定义视图中显示的字段信息  
dataSet | Array[array] | 查询结果数据集  
displayFields | object | 描述  
---|---|---  
fieldName | String | 字段显示名称  
viewFieldId | String | 视图字段ID  
fieldId | String | 字段ID  
dataSet | 数据项 | 描述  
---|---|---  
formattedValue | String | 格式化后的值  
formattedShowValue | String | 格式化后的显示值  
valueCode | String | 值编码，可能包含引用ID  
value | String | 原始值  
  
出参样例
    
    
    {
        "displayFields": [
            {
                "fieldName": "客户名称",
                "viewFieldId": "BI_682ae4f89a6d0e000111052f",
                "fieldId": "BI_5bcebcddcab2980001ee22ab"
            },
            {
                "fieldName": "订单金额",
                "viewFieldId": "BI_682ae4f99a6d0e0001110530",
                "fieldId": "BI_5bceda90dedd2c0001c2f54e"
            }
        ],
        "dataSet": [
            [
                {
                    "formattedValue": "多维水果1",
                    "formattedShowValue": "多维水果1",
                    "valueCode": "多维水果1$$60f14d96fd6db100011adaeb",
                    "value": "多维水果1"
                },
                {
                    "formattedValue": "1.53万",
                    "formattedShowValue": "15,300.00",
                    "valueCode": "15300.0",
                    "value": "15300.0"
                }
            ],
            [
                {
                    "formattedValue": "多维水果10",
                    "formattedShowValue": "多维水果10",
                    "valueCode": "多维水果10$$60f14d96fd6db100011adaf9",
                    "value": "多维水果10"
                },
                {
                    "formattedValue": "1.54万",
                    "formattedShowValue": "15,390.00",
                    "valueCode": "15390.0",
                    "value": "15390.0"
                }
            ]
        ]
    }
    
    

**Groovy 举例**
    
    
    def(isError3,data3,errorMsg3) = Fx.BI.loadViewData("BI_673c850d1e4ac70001e4027f")
    if(!isError3){
      log.info("数据信息:"+ Fx.json.toJson(data3))
    }else{
      log.info("查询失败:"+errorMsg3)
    }
    
    

**负责人：翟付杰Jeffrey**

### # 4\. getFiltersResult 获取图表筛选器

> `Fx.BI.getFiltersResult(<String viewId>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
viewId | String | 视图ID，用于指定要查询的视图筛选器 | 是  
  
出参格式

参数名称 | 类型 | 描述  
---|---|---  
data | 类型 |   
data | 类型 | 描述  
---|---|---  
filterGroups | Array[类型] | 过滤器组列表  
labelAndOptions | Array[Object] | 标签和选项列表  
filterGroups | 类型 | 描述  
---|---|---  
filters | Array[类型] |   
filters | 类型 | 描述  
---|---|---  
filterId | String | 过滤器ID  
value1 | String | 过滤条件值1，可能是JSON字符串或日期字符串  
value2 | String | 过滤条件值2，通常用于日期范围的结束日期  
dateRangeId | String | Null  
labelAndOptions | Object | 描述  
---|---|---  
defaultFilterOptionID | String | Null  
defaultFilterOptionType | String | 默认过滤选项类型  
label | String | 标签名称  
defaultFilterOptions | Array[Object] | 默认过滤选项列表  
defaultFilterOptions | Object | 描述  
---|---|---  
optionName | String | 选项名称  
isDefault | Integer | 是否默认选项，1表示是，0表示否  
optionID | String | 选项ID  
  
出参样例
    
    
    "data": {
        "filterGroups": [
          {
            "filters": [
              {
                "filterId": "BI_62174baf180c0b000183a7a9",
                "value1": "[{\"id\":999999,\"type\":\"c\"}]",
                "value2": "",
                "dateRangeId": null
              },
              {
                "filterId": "BI_62174baf180c0b000183a7aa",
                "value1": "2022-01-01",
                "value2": "2022-12-31",
                "dateRangeId": null
              },
              {
                "filterId": "BI_62174baf180c0b000183a7ab",
                "value1": "2022-01-01 00:00",
                "value2": "2022-12-31 23:59",
                "dateRangeId": null
              },
              {
                "filterId": "BI_62174baf180c0b000183a7ac",
                "value1": "[{\"id\":999999,\"type\":\"c\"}]",
                "value2": "",
                "dateRangeId": null
              }
            ]
          }
        ],
        "labelAndOptions": [
          {
            "defaultFilterOptionID": null,
            "defaultFilterOptionType": "UDF",
            "label": "场景",
            "defaultFilterOptions": [
              {
                "optionName": "全部",
                "isDefault": 1,
                "optionID": "BI_59a3e59333b39e09b44e9db1"
              },
              {
                "optionName": "我负责的",
                "isDefault": 0,
                "optionID": "BI_59a3e59333b39e09b44e9db2"
              },
              {
                "optionName": "我联合跟进的",
                "isDefault": 0,
                "optionID": "BI_171714538838884352"
              },
              {
                "optionName": "我服务的",
                "isDefault": 0,
                "optionID": "BI_171714538872438784"
              },
              {
                "optionName": "我参与的",
                "isDefault": 0,
                "optionID": "BI_59a3e59333b39e09b44e9db3"
              },
              {
                "optionName": "我负责部门的",
                "isDefault": 0,
                "optionID": "BI_59a3e59333b39e09b44e9db4"
              },
              {
                "optionName": "我下属负责的",
                "isDefault": 0,
                "optionID": "BI_59a3e59333b39e09b44e9db5"
              },
              {
                "optionName": "我下属联合跟进的",
                "isDefault": 0,
                "optionID": "BI_171714538939547648"
              },
              {
                "optionName": "我下属服务的",
                "isDefault": 0,
                "optionID": "BI_171714538973102080"
              },
              {
                "optionName": "我下属参与的",
                "isDefault": 0,
                "optionID": "BI_59a3e59333b39e09b44e9db6"
              },
              {
                "optionName": "共享给我的",
                "isDefault": 0,
                "optionID": "BI_59a3e59333b39e09b44e9db7"
              }
            ]
          }
        ]
      }
    
    

**Groovy 举例**
    
    
    def(isError5,data5,errorMsg5) = Fx.BI.getFiltersResult("BI_6747dff28443340001454164")
    if(!isError5){
      log.info("筛选器信息:" + Fx.json.toJson(data5))
      /*可根据FilterId修改筛选器值进行查询，值的结构可参考报表运行态传参结构*/
    } else {
        log.info("查询失败:" + errorMsg5)
    }
    
    

**负责人：翟付杰Jeffrey**

### # 5\. pageLoadViewData 图表数据加载

> `Fx.BI.pageLoadViewData(<String viewId>, <Integer pageIndex>, <Integer pageSize>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
viewId | String | 视图ID | 是  
pageIndex | Integer | 页码，从1开始 | 是  
pageSize | Integer | 每页记录数 | 是  
  
出参格式

参数名称 | 类型 | 描述  
---|---|---  
displayFields | Array[object] | 定义视图中显示的字段信息  
dataSet | Array[array] | 查询结果数据集  
displayFields | object | 描述  
---|---|---  
fieldName | String | 字段显示名称  
viewFieldId | String | 视图字段ID  
fieldId | String | 字段ID  
dataSet | 数据项 | 描述  
---|---|---  
formattedValue | String | 格式化后的值  
formattedShowValue | String | 格式化后的显示值  
valueCode | String | 值编码，可能包含引用ID  
value | String | 原始值  
  
出参样例
    
    
    {
        "displayFields": [
            {
                "fieldName": "客户名称",
                "viewFieldId": "BI_682ae4f89a6d0e000111052f",
                "fieldId": "BI_5bcebcddcab2980001ee22ab"
            },
            {
                "fieldName": "订单金额",
                "viewFieldId": "BI_682ae4f99a6d0e0001110530",
                "fieldId": "BI_5bceda90dedd2c0001c2f54e"
            }
        ],
        "dataSet": [
            [
                {
                    "formattedValue": "多维水果1",
                    "formattedShowValue": "多维水果1",
                    "valueCode": "多维水果1$$60f14d96fd6db100011adaeb",
                    "value": "多维水果1"
                },
                {
                    "formattedValue": "1.53万",
                    "formattedShowValue": "15,300.00",
                    "valueCode": "15300.0",
                    "value": "15300.0"
                }
            ],
            [
                {
                    "formattedValue": "多维水果10",
                    "formattedShowValue": "多维水果10",
                    "valueCode": "多维水果10$$60f14d96fd6db100011adaf9",
                    "value": "多维水果10"
                },
                {
                    "formattedValue": "1.54万",
                    "formattedShowValue": "15,390.00",
                    "valueCode": "15390.0",
                    "value": "15390.0"
                }
            ]
        ]
    }
    
    

**Groovy 举例**
    
    
    String viewId = "BI_682ae4f89a6d0e000111052e";
    def (isErrorTmp,dataTmp,errorMsgTmp) = Fx.BI.pageLoadViewData(viewId,1,2)
    if (!isErrorTmp) {
        log.info("数据：" + Fx.json.toJson(dataTmp))
    } else {
        log.info("查询失败:" + errorMsgTmp)
    }
    
    

**负责人：翟付杰Jeffrey**

### # 6\. queryViewData 图表数据查询

> `Fx.BI.queryViewData(<string viewId>, <string dashboardId>, <array filters>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
viewId | string | 视图ID | 是  
dashboardId | string | 场景Id | 是  
filters | array[array] | 查询过滤条件列表 | 是  
filters | object | 描述 | 是否必填  
---|---|---|---  
filterId | string | 过滤器ID | 是  
value1 | string | 过滤条件值 | 是  
  
出参格式

参数名称 | 类型 | 描述  
---|---|---  
displayFields | 显示字段列表[object] | 定义视图中显示的字段信息  
dataSet | Array[array] | 查询结果数据集  
displayFields | object | 描述  
---|---|---  
fieldName | String | 字段显示名称  
viewFieldId | String | 视图字段ID  
fieldId | String | 字段ID  
dataSet | 数据项 | 描述  
---|---|---  
formattedValue | String | 格式化后的值  
formattedShowValue | String | 格式化后的显示值  
valueCode | String | 值编码，可能包含引用ID  
value | String | 原始值  
  
出参样例
    
    
    {
        "displayFields": [
            {
                "fieldName": "客户名称",
                "viewFieldId": "BI_682ae4f89a6d0e000111052f",
                "fieldId": "BI_5bcebcddcab2980001ee22ab"
            },
            {
                "fieldName": "订单金额",
                "viewFieldId": "BI_682ae4f99a6d0e0001110530",
                "fieldId": "BI_5bceda90dedd2c0001c2f54e"
            }
        ],
        "dataSet": [
            [
                {
                    "formattedValue": "多维水果1",
                    "formattedShowValue": "多维水果1",
                    "valueCode": "多维水果1$$60f14d96fd6db100011adaeb",
                    "value": "多维水果1"
                },
                {
                    "formattedValue": "1.53万",
                    "formattedShowValue": "15,300.00",
                    "valueCode": "15300.0",
                    "value": "15300.0"
                }
            ],
            [
                {
                    "formattedValue": "多维水果10",
                    "formattedShowValue": "多维水果10",
                    "valueCode": "多维水果10$$60f14d96fd6db100011adaf9",
                    "value": "多维水果10"
                },
                {
                    "formattedValue": "1.54万",
                    "formattedShowValue": "15,390.00",
                    "valueCode": "15390.0",
                    "value": "15390.0"
                }
            ]
        ]
    }
    
    

**Groovy 举例**
    
    
    List filters = [["filterId":"BI_5f464863fd6d860001ee93da","value1":"张三"]]
    def(isError3,data3,errorMsg3) = Fx.BI.queryViewData("BI_5f27dc882cfb0a0001346786","BI_59a3e59333b39e09b44e9db1",filters)
    if(!isError3){
      log.info("分页信息:"+data3["page"])
      log.info("表头信息:"+data3["displayFields"])
      log.info("数据集:"+data3["dataSet"])
    }else{
      log.info("条件查询失败:"+errorMsg3)
    }
    
    

**负责人：翟付杰Jeffrey**

### # 7\. pageQueryViewData 图表数据查询

> `Fx.BI.pageQueryViewData(<String viewId>, <String或null pageIndex>, <String或null pageSize>, <String objectId>, <String flag>, <Array filters>)`

**参数说明**

入参格式

参数名称 | BI视图分页查询 | 根据条件进行BI视图分页查询 | 是否必填  
---|---|---|---  
viewId | String | 视图ID，例如：BI_5f27dc882cfb0a0001346786 | 是  
pageIndex | String或null | 页码索引，可以为null | \--  
pageSize | String或null | 每页记录数，可以为null | \--  
objectId | String | 对象ID，例如：BI_59a3e59333b39e09b44e9db1 | 是  
flag | String | 标志，例如：1 | 是  
filters | Array[array] | 筛选条件列表 | 是  
filters | object | 描述 | 是否必填  
---|---|---|---  
filterId | String | 过滤器ID | 是  
value1 | String | 过滤值1 | \--  
value2 | String | 过滤值2，用于范围查询 | \--  
dateRangeId | Integer | 日期范围ID | \--  
  
出参格式

参数名称 | BI视图显示数据 | 描述  
---|---|---  
displayFields | 显示字段列表[object] | 定义视图中显示的字段信息  
dataSet | 数据集[array] | 查询结果数据集  
displayFields | object | 描述  
---|---|---  
fieldName | String | 字段显示名称  
viewFieldId | String | 视图字段ID  
fieldId | String | 字段ID  
dataSet | 数据项 | 描述  
---|---|---  
formattedValue | String | 格式化后的值  
formattedShowValue | String | 格式化后的显示值  
valueCode | String | 值编码，可能包含引用ID  
value | String | 原始值  
  
出参样例
    
    
    {
        "displayFields": [
            {
                "fieldName": "客户名称",
                "viewFieldId": "BI_682ae4f89a6d0e000111052f",
                "fieldId": "BI_5bcebcddcab2980001ee22ab"
            },
            {
                "fieldName": "订单金额",
                "viewFieldId": "BI_682ae4f99a6d0e0001110530",
                "fieldId": "BI_5bceda90dedd2c0001c2f54e"
            }
        ],
        "dataSet": [
            [
                {
                    "formattedValue": "多维水果1",
                    "formattedShowValue": "多维水果1",
                    "valueCode": "多维水果1$$60f14d96fd6db100011adaeb",
                    "value": "多维水果1"
                },
                {
                    "formattedValue": "1.53万",
                    "formattedShowValue": "15,300.00",
                    "valueCode": "15300.0",
                    "value": "15300.0"
                }
            ],
            [
                {
                    "formattedValue": "多维水果10",
                    "formattedShowValue": "多维水果10",
                    "valueCode": "多维水果10$$60f14d96fd6db100011adaf9",
                    "value": "多维水果10"
                },
                {
                    "formattedValue": "1.54万",
                    "formattedShowValue": "15,390.00",
                    "valueCode": "15390.0",
                    "value": "15390.0"
                }
            ]
        ]
    }
    
    

**Groovy 举例**
    
    
    List filters = [["filterId":"BI_5f464863fd6d860001ee93da","value1":"张三"]]
    def(isError3,data3,errorMsg3) = Fx.BI.pageQueryViewData("BI_5f27dc882cfb0a0001346786",null,null,"BI_59a3e59333b39e09b44e9db1","1",filters)
    if(!isError3){
      log.info("分页信息:"+data3["page"])
      log.info("表头信息:"+data3["displayFields"])
      log.info("数据集:"+data3["dataSet"])
    }else{
      log.info("条件查询失败:"+errorMsg3)
    }
    
    

**负责人：翟付杰Jeffrey**

### # 8\. queryPivotViewDataById 图表viewId查询数据

> `Fx.BI.queryPivotViewDataById(<String viewId>)`

**参数说明**

入参格式

参数名称 | 根据Id查询 | 描述 | 是否必填  
---|---|---|---  
viewId | String | 视图ID，用于指定要查询的视图 | 是  
  
出参格式

参数名称 | BI数据结果集 | 描述  
---|---|---  
statFields | Array[Object] | 统计字段列表  
summaryDataSet | Object | 汇总数据集  
summaryDisplayFields | Array[Object] | 汇总显示字段列表  
headerFields | Array[Array] | 表头字段列表  
colGroupFields | Array[Object] | 列分组字段列表  
page | Object | 分页信息  
dataSet | Array[Array] | 数据集  
rowGroupFields | Array[Object] | 行分组字段列表  
statFields | Object | 描述  
---|---|---  
fieldName | String | 字段显示名称  
dbObjName | String | 数据库对象名称  
crmObjName | String | CRM对象名称  
dbFieldName | String | 数据库字段名称  
fieldID | String | 字段ID  
crmFieldName | String | CRM字段名称  
summaryDisplayFields | Object | 描述  
---|---|---  
fieldName | String | 字段显示名称  
dbObjName | String | 数据库对象名称  
crmObjName | String | CRM对象名称  
dbFieldName | String | 数据库字段名称  
fieldID | String | 字段ID  
crmFieldName | String | CRM字段名称  
headerFields | Object | 描述  
---|---|---  
fieldName | String | 字段名称  
formattedValue | String | 格式化后的值  
value | String | 原始值  
fieldID | String | 字段ID  
formatStr | String | 格式化字符串  
columnName | String | 列名  
colGroupFields | Object | 描述  
---|---|---  
formatStr | String | 格式化字符串  
fieldName | String | 字段名称  
fieldId | String | 字段ID  
columnName | String | 列名  
page | Object | 分页信息  
---|---|---  
pageCount | Integer | 总页数  
pageNumber | Integer | 当前页码  
pageSize | Integer | 每页记录数  
totalCount | Integer | 总记录数  
dataSet | Object | 描述  
---|---|---  
formattedValue | String | 格式化后的值  
value | String | 原始值  
rowGroupFields | Object | 描述  
---|---|---  
formatStr | String | 格式化字符串  
fieldName | String | 字段名称  
fieldId | String | 字段ID  
columnName | String | 列名  
  
出参样例
    
    
    {
        "statFields": [
            {
                "fieldName": "金额",
                "dbObjName": "object_oz2i0__c",
                "crmObjName": "object_oz2i0__c",
                "dbFieldName": "field_6rfqC__c",
                "fieldID": "BI_0f46eb539465b5746c1798ad9789c83a",
                "crmFieldName": "field_6rfqC__c"
            }
        ],
        "summaryDataSet": {
            "object_oz2i0__c_field_6rfqc__c$0": [
                {
                    "aggTypeCaption": "求和",
                    "aggType": "2",
                    "formattedValue": "10.000",
                    "formattedShowValue": "10.000",
                    "value": "10.0"
                }
            ]
        },
        "summaryDisplayFields": [
            {
                "fieldName": "金额",
                "dbObjName": "object_oz2i0__c",
                "crmObjName": "object_oz2i0__c",
                "dbFieldName": "field_6rfqC__c",
                "fieldID": "BI_0f46eb539465b5746c1798ad9789c83a",
                "crmFieldName": "field_6rfqC__c"
            }
        ],
        "headerFields": [
            [
                {
                    "fieldName": "部门",
                    "formattedValue": "",
                    "value": "",
                    "fieldID": "BI_1416823ffb7298cc11838cedb4b59fdf"
                },
                {
                    "formatStr": "",
                    "fieldName": "部门",
                    "value": "部门",
                    "fieldID": "BI_1416823ffb7298cc11838cedb4b59fdf",
                    "columnName": "object_oz2i0__c_field_6ejpc__c$0"
                },
                {
                    "fieldName": "销售部门",
                    "formattedValue": "销售部门",
                    "value": "1001",
                    "fieldID": "BI_1416823ffb7298cc11838cedb4b59fdf"
                },
                {
                    "fieldName": "总计",
                    "formattedValue": "总计",
                    "value": "总计",
                    "fieldID": "BI_1416823ffb7298cc11838cedb4b59fdf"
                }
            ],
            [
                {
                    "formatStr": "",
                    "fieldName": "负责人主属部门",
                    "value": "负责人主属部门",
                    "fieldID": "BI_a068e508be76af5026880cbde60a8610",
                    "columnName": "object_oz2i0__c_owner_department$0"
                },
                {
                    "formatStr": "",
                    "fieldName": "客户名称",
                    "value": "客户名称",
                    "fieldID": "BI_3f378638510641067008767e02cf6563",
                    "columnName": "object_oz2i0__c_field_21fnw__c$0"
                },
                {
                    "formatStr": "#,##0.000",
                    "fieldName": "金额(求和)",
                    "value": "金额",
                    "fieldID": "BI_0f46eb539465b5746c1798ad9789c83a",
                    "columnName": "object_oz2i0__c_field_6rfqc__c$0"
                },
                {
                    "formatStr": "#,##0.000",
                    "fieldName": "金额(求和)",
                    "value": "金额",
                    "fieldID": "BI_0f46eb539465b5746c1798ad9789c83a",
                    "columnName": "object_oz2i0__c_field_6rfqc__c$0"
                }
            ]
        ],
        "colGroupFields": [
            {
                "formatStr": "",
                "fieldName": "负责人主属部门",
                "fieldId": "BI_a068e508be76af5026880cbde60a8610",
                "columnName": "object_oz2i0__c_owner_department$0"
            },
            {
                "formatStr": "",
                "fieldName": "客户名称",
                "fieldId": "BI_3f378638510641067008767e02cf6563",
                "columnName": "object_oz2i0__c_field_21fnw__c$0"
            }
        ],
        "page": {
            "pageCount": 1,
            "pageNumber": 1,
            "pageSize": 20,
            "totalCount": 3
        },
        "dataSet": [
            [
                {
                    "formattedValue": "中-部门A1",
                    "value": "1002"
                },
                {
                    "formattedValue": "--",
                    "value": "--"
                },
                {
                    "formattedValue": "10.000",
                    "value": "10.0"
                },
                {
                    "formattedValue": "10.000",
                    "value": "10.0"
                }
            ],
            [
                {
                    "formattedValue": "中-部门A1",
                    "value": "1002"
                },
                {
                    "formattedValue": "小计",
                    "value": "小计"
                },
                {
                    "formattedValue": "10.000",
                    "value": "10.0"
                },
                {
                    "formattedValue": "10.000",
                    "value": "10.0"
                }
            ],
            [
                {
                    "formattedValue": "总计",
                    "value": "总计"
                },
                {
                    "formattedValue": "总计",
                    "value": "总计"
                },
                {
                    "formattedValue": "10.000",
                    "value": "10.0"
                },
                {
                    "formattedValue": "10.000",
                    "value": "10.0"
                }
            ]
        ],
        "rowGroupFields": [
            {
                "formatStr": "",
                "fieldName": "部门",
                "fieldId": "BI_1416823ffb7298cc11838cedb4b59fdf",
                "columnName": "object_oz2i0__c_field_6ejpc__c$0"
            }
        ]
    }
    
    

**Groovy 举例**
    
    
    // 通过viewId查询交叉表
    def (isError, data, errorMsg) = Fx.BI.queryPivotViewDataById("BI_62973467376efe000172be38")
    if (!isError) {
        log.info("分页信息:" + data["page"])
        log.info("表头信息:" + data["headerFields"])
        log.info("数据集:" + data["dataSet"])
        log.info("列分组:" + data["colGroupFields"])
        log.info("行分组:" + data["rowGroupFields"])
        log.info("统计列:" + data["statFields"])
        log.info("summaryDataSet:" + data["summaryDataSet"])
        log.info("summaryDisplayFields:" + data["summaryDisplayFields"])
    } else {
        log.info("查询失败:" + errorMsg)
    }
    
    

**负责人：翟付杰Jeffrey**

### # 9\. queryPivotViewDataByPage 通过图表id和自定义分页查询数据

> `Fx.BI.queryPivotViewDataByPage(<String viewId>, <Integer pageIndex>, <Integer pageSize>)`

**参数说明**

入参格式

参数名称 | BI交叉报表分页查询入参 | 描述 | 是否必填  
---|---|---|---  
viewId | String | 视图ID | 是  
pageIndex | Integer | 页码，从1开始 | 是  
pageSize | Integer | 每页记录数 | 是  
  
出参格式

参数名称 | BI数据结果集 | 描述  
---|---|---  
statFields | Array[Object] | 统计字段列表  
summaryDataSet | Object | 汇总数据集  
summaryDisplayFields | Array[Object] | 汇总显示字段列表  
headerFields | Array[Array] | 表头字段列表  
colGroupFields | Array[Object] | 列分组字段列表  
page | Object | 分页信息  
dataSet | Array[Array] | 数据集  
rowGroupFields | Array[Object] | 行分组字段列表  
statFields | Object | 描述  
---|---|---  
fieldName | String | 字段显示名称  
dbObjName | String | 数据库对象名称  
crmObjName | String | CRM对象名称  
dbFieldName | String | 数据库字段名称  
fieldID | String | 字段ID  
crmFieldName | String | CRM字段名称  
summaryDisplayFields | Object | 描述  
---|---|---  
fieldName | String | 字段显示名称  
dbObjName | String | 数据库对象名称  
crmObjName | String | CRM对象名称  
dbFieldName | String | 数据库字段名称  
fieldID | String | 字段ID  
crmFieldName | String | CRM字段名称  
headerFields | Object | 描述  
---|---|---  
fieldName | String | 字段名称  
formattedValue | String | 格式化后的值  
value | String | 原始值  
fieldID | String | 字段ID  
formatStr | String | 格式化字符串  
columnName | String | 列名  
colGroupFields | Object | 描述  
---|---|---  
formatStr | String | 格式化字符串  
fieldName | String | 字段名称  
fieldId | String | 字段ID  
columnName | String | 列名  
page | Object | 分页信息  
---|---|---  
pageCount | Integer | 总页数  
pageNumber | Integer | 当前页码  
pageSize | Integer | 每页记录数  
totalCount | Integer | 总记录数  
dataSet | Object | 描述  
---|---|---  
formattedValue | String | 格式化后的值  
value | String | 原始值  
rowGroupFields | Object | 描述  
---|---|---  
formatStr | String | 格式化字符串  
fieldName | String | 字段名称  
fieldId | String | 字段ID  
columnName | String | 列名  
  
出参样例
    
    
    {
        "statFields": [
            {
                "fieldName": "金额",
                "dbObjName": "object_oz2i0__c",
                "crmObjName": "object_oz2i0__c",
                "dbFieldName": "field_6rfqC__c",
                "fieldID": "BI_0f46eb539465b5746c1798ad9789c83a",
                "crmFieldName": "field_6rfqC__c"
            }
        ],
        "summaryDataSet": {
            "object_oz2i0__c_field_6rfqc__c$0": [
                {
                    "aggTypeCaption": "求和",
                    "aggType": "2",
                    "formattedValue": "10.000",
                    "formattedShowValue": "10.000",
                    "value": "10.0"
                }
            ]
        },
        "summaryDisplayFields": [
            {
                "fieldName": "金额",
                "dbObjName": "object_oz2i0__c",
                "crmObjName": "object_oz2i0__c",
                "dbFieldName": "field_6rfqC__c",
                "fieldID": "BI_0f46eb539465b5746c1798ad9789c83a",
                "crmFieldName": "field_6rfqC__c"
            }
        ],
        "headerFields": [
            [
                {
                    "fieldName": "部门",
                    "formattedValue": "",
                    "value": "",
                    "fieldID": "BI_1416823ffb7298cc11838cedb4b59fdf"
                },
                {
                    "formatStr": "",
                    "fieldName": "部门",
                    "value": "部门",
                    "fieldID": "BI_1416823ffb7298cc11838cedb4b59fdf",
                    "columnName": "object_oz2i0__c_field_6ejpc__c$0"
                },
                {
                    "fieldName": "销售部门",
                    "formattedValue": "销售部门",
                    "value": "1001",
                    "fieldID": "BI_1416823ffb7298cc11838cedb4b59fdf"
                },
                {
                    "fieldName": "总计",
                    "formattedValue": "总计",
                    "value": "总计",
                    "fieldID": "BI_1416823ffb7298cc11838cedb4b59fdf"
                }
            ],
            [
                {
                    "formatStr": "",
                    "fieldName": "负责人主属部门",
                    "value": "负责人主属部门",
                    "fieldID": "BI_a068e508be76af5026880cbde60a8610",
                    "columnName": "object_oz2i0__c_owner_department$0"
                },
                {
                    "formatStr": "",
                    "fieldName": "客户名称",
                    "value": "客户名称",
                    "fieldID": "BI_3f378638510641067008767e02cf6563",
                    "columnName": "object_oz2i0__c_field_21fnw__c$0"
                },
                {
                    "formatStr": "#,##0.000",
                    "fieldName": "金额(求和)",
                    "value": "金额",
                    "fieldID": "BI_0f46eb539465b5746c1798ad9789c83a",
                    "columnName": "object_oz2i0__c_field_6rfqc__c$0"
                },
                {
                    "formatStr": "#,##0.000",
                    "fieldName": "金额(求和)",
                    "value": "金额",
                    "fieldID": "BI_0f46eb539465b5746c1798ad9789c83a",
                    "columnName": "object_oz2i0__c_field_6rfqc__c$0"
                }
            ]
        ],
        "colGroupFields": [
            {
                "formatStr": "",
                "fieldName": "负责人主属部门",
                "fieldId": "BI_a068e508be76af5026880cbde60a8610",
                "columnName": "object_oz2i0__c_owner_department$0"
            },
            {
                "formatStr": "",
                "fieldName": "客户名称",
                "fieldId": "BI_3f378638510641067008767e02cf6563",
                "columnName": "object_oz2i0__c_field_21fnw__c$0"
            }
        ],
        "page": {
            "pageCount": 1,
            "pageNumber": 1,
            "pageSize": 20,
            "totalCount": 3
        },
        "dataSet": [
            [
                {
                    "formattedValue": "中-部门A1",
                    "value": "1002"
                },
                {
                    "formattedValue": "--",
                    "value": "--"
                },
                {
                    "formattedValue": "10.000",
                    "value": "10.0"
                },
                {
                    "formattedValue": "10.000",
                    "value": "10.0"
                }
            ],
            [
                {
                    "formattedValue": "中-部门A1",
                    "value": "1002"
                },
                {
                    "formattedValue": "小计",
                    "value": "小计"
                },
                {
                    "formattedValue": "10.000",
                    "value": "10.0"
                },
                {
                    "formattedValue": "10.000",
                    "value": "10.0"
                }
            ],
            [
                {
                    "formattedValue": "总计",
                    "value": "总计"
                },
                {
                    "formattedValue": "总计",
                    "value": "总计"
                },
                {
                    "formattedValue": "10.000",
                    "value": "10.0"
                },
                {
                    "formattedValue": "10.000",
                    "value": "10.0"
                }
            ]
        ],
        "rowGroupFields": [
            {
                "formatStr": "",
                "fieldName": "部门",
                "fieldId": "BI_1416823ffb7298cc11838cedb4b59fdf",
                "columnName": "object_oz2i0__c_field_6ejpc__c$0"
            }
        ]
    }
    
    

**Groovy 举例**
    
    
    // 通过viewId和分页信息page查询交叉表
    def (isError, data, errorMsg) = Fx.BI.queryPivotViewDataByPage("BI_62973467376efe000172be38", 1, 1)
    if (!isError) {
        log.info("分页信息:" + data["page"])
        log.info("表头信息:" + data["headerFields"])
        log.info("数据集:" + data["dataSet"])
        log.info("列分组:" + data["colGroupFields"])
        log.info("行分组:" + data["rowGroupFields"])
        log.info("统计列:" + data["statFields"])
        log.info("summaryDataSet:" + data["summaryDataSet"])
        log.info("summaryDisplayFields:" + data["summaryDisplayFields"])
    } else {
        log.info("查询失败:" + errorMsg)
    }
    
    

**负责人：翟付杰Jeffrey**

### # 10\. queryPivotViewDataByFilter 通过场景和筛选查询数据

> `Fx.BI.queryPivotViewDataByFilter(<String viewId>, <String optionId>, <Array filters>)`

**参数说明**

入参格式

参数名称 | BI交叉报表过滤查询入参 | 描述 | 是否必填  
---|---|---|---  
viewId | String | 视图ID | 是  
optionId | String | 场景ID | 是  
filters | Array[Array] | 过滤条件列表 | 是  
filters | Object | 描述 | 是否必填  
---|---|---|---  
filterId | String | 过滤器ID | 是  
value1 | String | 过滤条件值1，通常为JSON字符串 | 是  
value2 | String | 过滤条件值2，通常用于日期范围的结束日期 | 是  
  
出参格式

参数名称 | BI数据结果集 | 描述  
---|---|---  
statFields | Array[Object] | 统计字段列表  
summaryDataSet | Object | 汇总数据集  
summaryDisplayFields | Array[Object] | 汇总显示字段列表  
headerFields | Array[Array] | 表头字段列表  
colGroupFields | Array[Object] | 列分组字段列表  
page | Object | 分页信息  
dataSet | Array[Array] | 数据集  
rowGroupFields | Array[Object] | 行分组字段列表  
statFields | Object | 描述  
---|---|---  
fieldName | String | 字段显示名称  
dbObjName | String | 数据库对象名称  
crmObjName | String | CRM对象名称  
dbFieldName | String | 数据库字段名称  
fieldID | String | 字段ID  
crmFieldName | String | CRM字段名称  
summaryDisplayFields | Object | 描述  
---|---|---  
fieldName | String | 字段显示名称  
dbObjName | String | 数据库对象名称  
crmObjName | String | CRM对象名称  
dbFieldName | String | 数据库字段名称  
fieldID | String | 字段ID  
crmFieldName | String | CRM字段名称  
headerFields | Object | 描述  
---|---|---  
fieldName | String | 字段名称  
formattedValue | String | 格式化后的值  
value | String | 原始值  
fieldID | String | 字段ID  
formatStr | String | 格式化字符串  
columnName | String | 列名  
colGroupFields | Object | 描述  
---|---|---  
formatStr | String | 格式化字符串  
fieldName | String | 字段名称  
fieldId | String | 字段ID  
columnName | String | 列名  
page | Object | 分页信息  
---|---|---  
pageCount | Integer | 总页数  
pageNumber | Integer | 当前页码  
pageSize | Integer | 每页记录数  
totalCount | Integer | 总记录数  
dataSet | Object | 描述  
---|---|---  
formattedValue | String | 格式化后的值  
value | String | 原始值  
rowGroupFields | Object | 描述  
---|---|---  
formatStr | String | 格式化字符串  
fieldName | String | 字段名称  
fieldId | String | 字段ID  
columnName | String | 列名  
  
出参样例
    
    
    {
        "statFields": [
            {
                "fieldName": "金额",
                "dbObjName": "object_oz2i0__c",
                "crmObjName": "object_oz2i0__c",
                "dbFieldName": "field_6rfqC__c",
                "fieldID": "BI_0f46eb539465b5746c1798ad9789c83a",
                "crmFieldName": "field_6rfqC__c"
            }
        ],
        "summaryDataSet": {
            "object_oz2i0__c_field_6rfqc__c$0": [
                {
                    "aggTypeCaption": "求和",
                    "aggType": "2",
                    "formattedValue": "10.000",
                    "formattedShowValue": "10.000",
                    "value": "10.0"
                }
            ]
        },
        "summaryDisplayFields": [
            {
                "fieldName": "金额",
                "dbObjName": "object_oz2i0__c",
                "crmObjName": "object_oz2i0__c",
                "dbFieldName": "field_6rfqC__c",
                "fieldID": "BI_0f46eb539465b5746c1798ad9789c83a",
                "crmFieldName": "field_6rfqC__c"
            }
        ],
        "headerFields": [
            [
                {
                    "fieldName": "部门",
                    "formattedValue": "",
                    "value": "",
                    "fieldID": "BI_1416823ffb7298cc11838cedb4b59fdf"
                },
                {
                    "formatStr": "",
                    "fieldName": "部门",
                    "value": "部门",
                    "fieldID": "BI_1416823ffb7298cc11838cedb4b59fdf",
                    "columnName": "object_oz2i0__c_field_6ejpc__c$0"
                },
                {
                    "fieldName": "销售部门",
                    "formattedValue": "销售部门",
                    "value": "1001",
                    "fieldID": "BI_1416823ffb7298cc11838cedb4b59fdf"
                },
                {
                    "fieldName": "总计",
                    "formattedValue": "总计",
                    "value": "总计",
                    "fieldID": "BI_1416823ffb7298cc11838cedb4b59fdf"
                }
            ],
            [
                {
                    "formatStr": "",
                    "fieldName": "负责人主属部门",
                    "value": "负责人主属部门",
                    "fieldID": "BI_a068e508be76af5026880cbde60a8610",
                    "columnName": "object_oz2i0__c_owner_department$0"
                },
                {
                    "formatStr": "",
                    "fieldName": "客户名称",
                    "value": "客户名称",
                    "fieldID": "BI_3f378638510641067008767e02cf6563",
                    "columnName": "object_oz2i0__c_field_21fnw__c$0"
                },
                {
                    "formatStr": "#,##0.000",
                    "fieldName": "金额(求和)",
                    "value": "金额",
                    "fieldID": "BI_0f46eb539465b5746c1798ad9789c83a",
                    "columnName": "object_oz2i0__c_field_6rfqc__c$0"
                },
                {
                    "formatStr": "#,##0.000",
                    "fieldName": "金额(求和)",
                    "value": "金额",
                    "fieldID": "BI_0f46eb539465b5746c1798ad9789c83a",
                    "columnName": "object_oz2i0__c_field_6rfqc__c$0"
                }
            ]
        ],
        "colGroupFields": [
            {
                "formatStr": "",
                "fieldName": "负责人主属部门",
                "fieldId": "BI_a068e508be76af5026880cbde60a8610",
                "columnName": "object_oz2i0__c_owner_department$0"
            },
            {
                "formatStr": "",
                "fieldName": "客户名称",
                "fieldId": "BI_3f378638510641067008767e02cf6563",
                "columnName": "object_oz2i0__c_field_21fnw__c$0"
            }
        ],
        "page": {
            "pageCount": 1,
            "pageNumber": 1,
            "pageSize": 20,
            "totalCount": 3
        },
        "dataSet": [
            [
                {
                    "formattedValue": "中-部门A1",
                    "value": "1002"
                },
                {
                    "formattedValue": "--",
                    "value": "--"
                },
                {
                    "formattedValue": "10.000",
                    "value": "10.0"
                },
                {
                    "formattedValue": "10.000",
                    "value": "10.0"
                }
            ],
            [
                {
                    "formattedValue": "中-部门A1",
                    "value": "1002"
                },
                {
                    "formattedValue": "小计",
                    "value": "小计"
                },
                {
                    "formattedValue": "10.000",
                    "value": "10.0"
                },
                {
                    "formattedValue": "10.000",
                    "value": "10.0"
                }
            ],
            [
                {
                    "formattedValue": "总计",
                    "value": "总计"
                },
                {
                    "formattedValue": "总计",
                    "value": "总计"
                },
                {
                    "formattedValue": "10.000",
                    "value": "10.0"
                },
                {
                    "formattedValue": "10.000",
                    "value": "10.0"
                }
            ]
        ],
        "rowGroupFields": [
            {
                "formatStr": "",
                "fieldName": "部门",
                "fieldId": "BI_1416823ffb7298cc11838cedb4b59fdf",
                "columnName": "object_oz2i0__c_field_6ejpc__c$0"
            }
        ]
    }
    
    

**Groovy 举例**
    
    
    // 通过viewId，filters和defaultFilterOptionId查询交叉表数据
    List filters = [["filterId": "BI_62c68112deef7b0001c1f756", "value1": "[{\"id\":1001,\"type\":\"g\"}]", "value2": ""]]
    def (isError, data, errorMsg) = Fx.BI.queryPivotViewDataByFilter("BI_62973467376efe000172be38", "BI_59a3e59333b39e09b44e9db2", filters)
    if (!isError) {
        log.info("分页信息:" + data["page"])
        log.info("表头信息:" + data["headerFields"])
        log.info("数据集:" + data["dataSet"])
        log.info("列分组:" + data["colGroupFields"])
        log.info("行分组:" + data["rowGroupFields"])
        log.info("统计列:" + data["statFields"])
        log.info("summaryDataSet:" + data["summaryDataSet"])
        log.info("summaryDisplayFields:" + data["summaryDisplayFields"])
    } else {
        log.info("查询失败:" + errorMsg)
    }
    
    

**负责人：翟付杰Jeffrey**

### # 11\. queryPivotReportData 交叉表数据查询

> `Fx.BI.queryPivotReportData(<String reportId>, <Integer pageIndex>, <Integer pageSize>, <String optionId>, <Array filters>)`

**参数说明**

入参格式

参数名称 | BI交叉报表查询入参 | 描述 | 是否必填  
---|---|---|---  
reportId | String | 报表ID | 是  
pageIndex | Integer | 页码，从1开始 | 是  
pageSize | Integer | 每页记录数 | 是  
optionId | String | 选项ID | 是  
filters | Array[Array] | 过滤条件列表 | 是  
filters | Object | 描述 | 是否必填  
---|---|---|---  
filterId | String | 过滤器ID | 是  
value1 | String | 过滤条件值1，通常为JSON字符串 | 是  
value2 | String | 过滤条件值2，通常用于日期范围的结束日期 | 是  
  
出参格式

参数名称 | BI数据结果集 | 描述  
---|---|---  
statFields | Array[Object] | 统计字段列表  
summaryDataSet | Object | 汇总数据集  
summaryDisplayFields | Array[Object] | 汇总显示字段列表  
headerFields | Array[Array] | 表头字段列表  
colGroupFields | Array[Object] | 列分组字段列表  
page | Object | 分页信息  
dataSet | Array[Array] | 数据集  
rowGroupFields | Array[Object] | 行分组字段列表  
statFields | Object | 描述  
---|---|---  
fieldName | String | 字段显示名称  
dbObjName | String | 数据库对象名称  
crmObjName | String | CRM对象名称  
dbFieldName | String | 数据库字段名称  
fieldID | String | 字段ID  
crmFieldName | String | CRM字段名称  
summaryDisplayFields | Object | 描述  
---|---|---  
fieldName | String | 字段显示名称  
dbObjName | String | 数据库对象名称  
crmObjName | String | CRM对象名称  
dbFieldName | String | 数据库字段名称  
fieldID | String | 字段ID  
crmFieldName | String | CRM字段名称  
headerFields | Object | 描述  
---|---|---  
fieldName | String | 字段名称  
formattedValue | String | 格式化后的值  
value | String | 原始值  
fieldID | String | 字段ID  
formatStr | String | 格式化字符串  
columnName | String | 列名  
colGroupFields | Object | 描述  
---|---|---  
formatStr | String | 格式化字符串  
fieldName | String | 字段名称  
fieldId | String | 字段ID  
columnName | String | 列名  
page | Object | 分页信息  
---|---|---  
pageCount | Integer | 总页数  
pageNumber | Integer | 当前页码  
pageSize | Integer | 每页记录数  
totalCount | Integer | 总记录数  
dataSet | Object | 描述  
---|---|---  
formattedValue | String | 格式化后的值  
value | String | 原始值  
rowGroupFields | Object | 描述  
---|---|---  
formatStr | String | 格式化字符串  
fieldName | String | 字段名称  
fieldId | String | 字段ID  
columnName | String | 列名  
  
出参样例
    
    
    {
        "statFields": [
            {
                "fieldName": "金额",
                "dbObjName": "object_oz2i0__c",
                "crmObjName": "object_oz2i0__c",
                "dbFieldName": "field_6rfqC__c",
                "fieldID": "BI_0f46eb539465b5746c1798ad9789c83a",
                "crmFieldName": "field_6rfqC__c"
            }
        ],
        "summaryDataSet": {
            "object_oz2i0__c_field_6rfqc__c$0": [
                {
                    "aggTypeCaption": "求和",
                    "aggType": "2",
                    "formattedValue": "10.000",
                    "formattedShowValue": "10.000",
                    "value": "10.0"
                }
            ]
        },
        "summaryDisplayFields": [
            {
                "fieldName": "金额",
                "dbObjName": "object_oz2i0__c",
                "crmObjName": "object_oz2i0__c",
                "dbFieldName": "field_6rfqC__c",
                "fieldID": "BI_0f46eb539465b5746c1798ad9789c83a",
                "crmFieldName": "field_6rfqC__c"
            }
        ],
        "headerFields": [
            [
                {
                    "fieldName": "部门",
                    "formattedValue": "",
                    "value": "",
                    "fieldID": "BI_1416823ffb7298cc11838cedb4b59fdf"
                },
                {
                    "formatStr": "",
                    "fieldName": "部门",
                    "value": "部门",
                    "fieldID": "BI_1416823ffb7298cc11838cedb4b59fdf",
                    "columnName": "object_oz2i0__c_field_6ejpc__c$0"
                },
                {
                    "fieldName": "销售部门",
                    "formattedValue": "销售部门",
                    "value": "1001",
                    "fieldID": "BI_1416823ffb7298cc11838cedb4b59fdf"
                },
                {
                    "fieldName": "总计",
                    "formattedValue": "总计",
                    "value": "总计",
                    "fieldID": "BI_1416823ffb7298cc11838cedb4b59fdf"
                }
            ],
            [
                {
                    "formatStr": "",
                    "fieldName": "负责人主属部门",
                    "value": "负责人主属部门",
                    "fieldID": "BI_a068e508be76af5026880cbde60a8610",
                    "columnName": "object_oz2i0__c_owner_department$0"
                },
                {
                    "formatStr": "",
                    "fieldName": "客户名称",
                    "value": "客户名称",
                    "fieldID": "BI_3f378638510641067008767e02cf6563",
                    "columnName": "object_oz2i0__c_field_21fnw__c$0"
                },
                {
                    "formatStr": "#,##0.000",
                    "fieldName": "金额(求和)",
                    "value": "金额",
                    "fieldID": "BI_0f46eb539465b5746c1798ad9789c83a",
                    "columnName": "object_oz2i0__c_field_6rfqc__c$0"
                },
                {
                    "formatStr": "#,##0.000",
                    "fieldName": "金额(求和)",
                    "value": "金额",
                    "fieldID": "BI_0f46eb539465b5746c1798ad9789c83a",
                    "columnName": "object_oz2i0__c_field_6rfqc__c$0"
                }
            ]
        ],
        "colGroupFields": [
            {
                "formatStr": "",
                "fieldName": "负责人主属部门",
                "fieldId": "BI_a068e508be76af5026880cbde60a8610",
                "columnName": "object_oz2i0__c_owner_department$0"
            },
            {
                "formatStr": "",
                "fieldName": "客户名称",
                "fieldId": "BI_3f378638510641067008767e02cf6563",
                "columnName": "object_oz2i0__c_field_21fnw__c$0"
            }
        ],
        "page": {
            "pageCount": 1,
            "pageNumber": 1,
            "pageSize": 20,
            "totalCount": 3
        },
        "dataSet": [
            [
                {
                    "formattedValue": "中-部门A1",
                    "value": "1002"
                },
                {
                    "formattedValue": "--",
                    "value": "--"
                },
                {
                    "formattedValue": "10.000",
                    "value": "10.0"
                },
                {
                    "formattedValue": "10.000",
                    "value": "10.0"
                }
            ],
            [
                {
                    "formattedValue": "中-部门A1",
                    "value": "1002"
                },
                {
                    "formattedValue": "小计",
                    "value": "小计"
                },
                {
                    "formattedValue": "10.000",
                    "value": "10.0"
                },
                {
                    "formattedValue": "10.000",
                    "value": "10.0"
                }
            ],
            [
                {
                    "formattedValue": "总计",
                    "value": "总计"
                },
                {
                    "formattedValue": "总计",
                    "value": "总计"
                },
                {
                    "formattedValue": "10.000",
                    "value": "10.0"
                },
                {
                    "formattedValue": "10.000",
                    "value": "10.0"
                }
            ]
        ],
        "rowGroupFields": [
            {
                "formatStr": "",
                "fieldName": "部门",
                "fieldId": "BI_1416823ffb7298cc11838cedb4b59fdf",
                "columnName": "object_oz2i0__c_field_6ejpc__c$0"
            }
        ]
    }
    
    

**Groovy 举例**
    
    
    List filters = [["filterId": "BI_62c68112deef7b0001c1f756", "value1": "[{\"id\":1001,\"type\":\"g\"}]", "value2": ""]]
    def (isError, data, errorMsg) = Fx.BI.queryPivotReportData("BI_62973467376efe000172be38", 1, 1, "BI_59a3e59333b39e09b44e9db2", filters)
    if (!isError) {
        log.info("分页信息:" + data["page"])
        log.info("表头信息:" + data["headerFields"])
        log.info("数据集:" + data["dataSet"])
        log.info("列分组:" + data["colGroupFields"])
        log.info("行分组:" + data["rowGroupFields"])
        log.info("统计列:" + data["statFields"])
        log.info("summaryDataSet:" + data["summaryDataSet"])
        log.info("summaryDisplayFields:" + data["summaryDisplayFields"])
    } else {
        log.info("查询失败:" + errorMsg)
    }
    
    

**负责人：翟付杰Jeffrey**

### # 12\. queryLwtViewData 拼表数据查询

> `Fx.BI.queryLwtViewData(<String viewId>, <Integer pageNumber>, <Integer pageSize>, <Array filterList>)`

**参数说明**

入参格式

参数名称 | BI视图带过滤条件的分页查询 | 描述 | 是否必填  
---|---|---|---  
viewId | String | 视图ID，用于指定要查询的视图 | 是  
pageNumber | Integer | 页码，从1开始 | 是  
pageSize | Integer | 每页记录数 | 是  
filterList | Array[array] | 过滤条件列表 | 是  
filterList | 过滤条件 | 描述 | 是否必填  
---|---|---|---  
filterId | String | 过滤器ID | 是  
value1 | String | 过滤值1 | \--  
value2 | String | 过滤值2，用于范围查询 | \--  
dateRangeId | Integer | 日期范围ID | \--  
  
出参格式

参数名称 | object | 描述  
---|---|---  
page | 类型 |   
displayFields | 类型[array] |   
dataSet | array[array] |   
page | 类型 | 描述  
---|---|---  
pageCount | Integer | 总共的页面数  
pageNumber | Integer | 当前显示的页面编号  
pageSize | Integer | 每页显示的记录数量  
totalCount | Integer | 数据集中的总记录数量  
displayFields | object | 描述  
---|---|---  
fieldName | String | 表头名称  
objName | String | 对象名称  
dbFieldName | String | 字段apiName  
fieldType | String | 字段类型  
columnKey | String | 唯一标识  
fieldId | String | 字段id  
refObjName | String | 关联对象apiName  
dataSet | 类型 | 描述  
---|---|---  
displayValue | String | 用于显示的数据值  
value | String | 实际数据值  
dataFormatStr | String | 数据的格式化字符串  
valueCode | String | 数据值的编码  
  
出参样例
    
    
    {
        "page": {
            "pageCount": 1,
            "pageNumber": 1,
            "pageSize": 20,
            "totalCount": 11
        },
        "displayFields": [
            [
                {
                    "fieldName": "主属性",
                    "objName": "瓜瓜",
                    "dbFieldName": "name",
                    "fieldType": "String",
                    "columnKey": "Bi.Custom.Realtime.LwtHeader.BI_lwt_1746698877573.bJO7v.Label",
                    "fieldId": "BI_61946d085af9d7000104f81c"
                },
                {
                    "fieldName": "创建时间",
                    "objName": "瓜瓜",
                    "dbFieldName": "create_time",
                    "fieldType": "Date",
                    "columnKey": "Bi.Custom.Realtime.LwtHeader.BI_lwt_1746698877573.FyMmk.Label",
                    "fieldId": "BI_61946d085af9d7000104f82b"
                },
                {
                    "refObjName": "org_employee_user",
                    "fieldName": "创建人",
                    "objName": "瓜瓜",
                    "dbFieldName": "created_by",
                    "fieldType": "Circle",
                    "columnKey": "Bi.Custom.Realtime.LwtHeader.BI_lwt_1746698877573.5KE7p.Label",
                    "fieldId": "BI_61946d085af9d7000104f84a"
                },
                {
                    "fieldName": "数字(求和)",
                    "objName": "瓜瓜",
                    "dbFieldName": "field_LKyOt__c",
                    "fieldType": "Number",
                    "columnKey": "Bi.Custom.Realtime.LwtHeader.BI_lwt_1746698877573.K4TdN.Label",
                    "fieldId": "BI_bb08fc7d10b7035b8dce074e4eedf"
                },
                {
                    "fieldName": "主属性(唯一计数)",
                    "objName": "瓜瓜",
                    "dbFieldName": "name",
                    "fieldType": "Number",
                    "columnKey": "Bi.Custom.Realtime.LwtHeader.BI_lwt_1746698877573.FRgFG.Label",
                    "fieldId": "BI_61946d085af9d7000104f81a"
                }
            ]
        ],
        "dataSet": [
            [
                {
                    "displayValue": "20250324-1",
                    "value": "20250324-1$$67e0d9e27258120007546170",
                    "dataFormatStr": ""
                },
                {
                    "displayValue": "20250324",
                    "value": "20250324",
                    "dataFormatStr": ""
                },
                {
                    "displayValue": "中-gua",
                    "value": "1198",
                    "dataFormatStr": ""
                },
                {
                    "displayValue": "1.93亿",
                    "value": "192500000.00000000",
                    "dataFormatStr": ""
                },
                {
                    "displayValue": "1",
                    "valueCode": "1044g",
                    "value": "1.00000000",
                    "dataFormatStr": ""
                }
            ],
            [
                {
                    "displayValue": "20250324-2",
                    "value": "20250324-2$$67e0fbde7258120007557c6e",
                    "dataFormatStr": ""
                },
                {
                    "displayValue": "20250324",
                    "value": "20250324",
                    "dataFormatStr": ""
                },
                {
                    "displayValue": "中-gua",
                    "value": "1198",
                    "dataFormatStr": ""
                },
                {
                    "displayValue": "1.93亿",
                    "value": "192500000.00000000",
                    "dataFormatStr": ""
                },
                {
                    "displayValue": "1",
                    "valueCode": "1044g",
                    "value": "1.00000000",
                    "dataFormatStr": ""
                }
            ]
        ]
    }
    
    

**Groovy 举例**
    
    
    List filterList = [["filterId": "BI_62cb8af6741ac20001debf72", "value1": "", "value2": "", "dateRangeId": 6]];
    def (isError, data, errorMsg) = Fx.BI.queryLwtViewData("BI_lwt_1657506871248", 1, 1, filterList)
    if (!isError) {
        log.info("分页信息:" + data["page"])
        log.info("表头信息:" + data["displayFields"])
        log.info("数据集:" + data["dataSet"])
    } else {
        log.info("查询失败:" + errorMsg)
    }
    
    

**负责人：翟付杰Jeffrey**

### # 13\. queryLwtViewDataById 图表viewId查询数据

> `Fx.BI.queryLwtViewDataById(<String viewId>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
viewId | String | 视图ID，用于指定要查询的视图 | 是  
  
出参格式

参数名称 | object | 描述  
---|---|---  
page | 类型 |   
displayFields | 类型[array] |   
dataSet | array[array] |   
page | 类型 | 描述  
---|---|---  
pageCount | Integer | 总共的页面数  
pageNumber | Integer | 当前显示的页面编号  
pageSize | Integer | 每页显示的记录数量  
totalCount | Integer | 数据集中的总记录数量  
displayFields | object | 描述  
---|---|---  
fieldName | String | 表头名称  
objName | String | 对象名称  
dbFieldName | String | 字段apiName  
fieldType | String | 字段类型  
columnKey | String | 唯一标识  
fieldId | String | 字段id  
refObjName | String | 关联对象apiName  
dataSet | 类型 | 描述  
---|---|---  
displayValue | String | 用于显示的数据值  
value | String | 实际数据值  
dataFormatStr | String | 数据的格式化字符串  
valueCode | String | 数据值的编码  
  
出参样例
    
    
    {
        "page": {
            "pageCount": 1,
            "pageNumber": 1,
            "pageSize": 20,
            "totalCount": 11
        },
        "displayFields": [
            [
                {
                    "fieldName": "主属性",
                    "objName": "瓜瓜",
                    "dbFieldName": "name",
                    "fieldType": "String",
                    "columnKey": "Bi.Custom.Realtime.LwtHeader.BI_lwt_1746698877573.bJO7v.Label",
                    "fieldId": "BI_61946d085af9d7000104f81c"
                },
                {
                    "fieldName": "创建时间",
                    "objName": "瓜瓜",
                    "dbFieldName": "create_time",
                    "fieldType": "Date",
                    "columnKey": "Bi.Custom.Realtime.LwtHeader.BI_lwt_1746698877573.FyMmk.Label",
                    "fieldId": "BI_61946d085af9d7000104f82b"
                },
                {
                    "refObjName": "org_employee_user",
                    "fieldName": "创建人",
                    "objName": "瓜瓜",
                    "dbFieldName": "created_by",
                    "fieldType": "Circle",
                    "columnKey": "Bi.Custom.Realtime.LwtHeader.BI_lwt_1746698877573.5KE7p.Label",
                    "fieldId": "BI_61946d085af9d7000104f84a"
                },
                {
                    "fieldName": "数字(求和)",
                    "objName": "瓜瓜",
                    "dbFieldName": "field_LKyOt__c",
                    "fieldType": "Number",
                    "columnKey": "Bi.Custom.Realtime.LwtHeader.BI_lwt_1746698877573.K4TdN.Label",
                    "fieldId": "BI_bb08fc7d10b7035b8dce074e4eedf"
                },
                {
                    "fieldName": "主属性(唯一计数)",
                    "objName": "瓜瓜",
                    "dbFieldName": "name",
                    "fieldType": "Number",
                    "columnKey": "Bi.Custom.Realtime.LwtHeader.BI_lwt_1746698877573.FRgFG.Label",
                    "fieldId": "BI_61946d085af9d7000104f81a"
                }
            ]
        ],
        "dataSet": [
            [
                {
                    "displayValue": "20250324-1",
                    "value": "20250324-1$$67e0d9e27258120007546170",
                    "dataFormatStr": ""
                },
                {
                    "displayValue": "20250324",
                    "value": "20250324",
                    "dataFormatStr": ""
                },
                {
                    "displayValue": "中-gua",
                    "value": "1198",
                    "dataFormatStr": ""
                },
                {
                    "displayValue": "1.93亿",
                    "value": "192500000.00000000",
                    "dataFormatStr": ""
                },
                {
                    "displayValue": "1",
                    "valueCode": "1044g",
                    "value": "1.00000000",
                    "dataFormatStr": ""
                }
            ],
            [
                {
                    "displayValue": "20250324-2",
                    "value": "20250324-2$$67e0fbde7258120007557c6e",
                    "dataFormatStr": ""
                },
                {
                    "displayValue": "20250324",
                    "value": "20250324",
                    "dataFormatStr": ""
                },
                {
                    "displayValue": "中-gua",
                    "value": "1198",
                    "dataFormatStr": ""
                },
                {
                    "displayValue": "1.93亿",
                    "value": "192500000.00000000",
                    "dataFormatStr": ""
                },
                {
                    "displayValue": "1",
                    "valueCode": "1044g",
                    "value": "1.00000000",
                    "dataFormatStr": ""
                }
            ]
        ]
    }
    
    

**Groovy 举例**
    
    
    def (isError, data, errorMsg) = Fx.BI.queryLwtViewDataById("BI_lwt_1657506871248")
    if (!isError) {
        log.info("分页信息:" + data["page"])
        log.info("表头信息:" + data["displayFields"])
        log.info("数据集:" + data["dataSet"])
    } else {
        log.info("查询失败:" + errorMsg)
    }
    
    

**负责人：翟付杰Jeffrey**

### # 14\. queryLwtViewDataByPage 通过图表id和自定义分页查询数据

> `Fx.BI.queryLwtViewDataByPage(<String viewId>, <Integer pageNumber>, <Integer pageSize>)`

**参数说明**

入参格式

参数名称 | BI视图分页查询 | 描述 | 是否必填  
---|---|---|---  
viewId | String | 视图ID，用于指定要查询的视图 | 是  
pageNumber | Integer | 页码，从1开始 | 是  
pageSize | Integer | 每页记录数 | 是  
  
出参格式

参数名称 | object | 描述  
---|---|---  
page | 类型 |   
displayFields | 类型[array] |   
dataSet | array[array] |   
page | 类型 | 描述  
---|---|---  
pageCount | Integer | 总共的页面数  
pageNumber | Integer | 当前显示的页面编号  
pageSize | Integer | 每页显示的记录数量  
totalCount | Integer | 数据集中的总记录数量  
displayFields | object | 描述  
---|---|---  
fieldName | String | 表头名称  
objName | String | 对象名称  
dbFieldName | String | 字段apiName  
fieldType | String | 字段类型  
columnKey | String | 唯一标识  
fieldId | String | 字段id  
refObjName | String | 关联对象apiName  
dataSet | 类型 | 描述  
---|---|---  
displayValue | String | 用于显示的数据值  
value | String | 实际数据值  
dataFormatStr | String | 数据的格式化字符串  
valueCode | String | 数据值的编码  
  
出参样例
    
    
    {
        "page": {
            "pageCount": 1,
            "pageNumber": 1,
            "pageSize": 20,
            "totalCount": 11
        },
        "displayFields": [
            [
                {
                    "fieldName": "主属性",
                    "objName": "瓜瓜",
                    "dbFieldName": "name",
                    "fieldType": "String",
                    "columnKey": "Bi.Custom.Realtime.LwtHeader.BI_lwt_1746698877573.bJO7v.Label",
                    "fieldId": "BI_61946d085af9d7000104f81c"
                },
                {
                    "fieldName": "创建时间",
                    "objName": "瓜瓜",
                    "dbFieldName": "create_time",
                    "fieldType": "Date",
                    "columnKey": "Bi.Custom.Realtime.LwtHeader.BI_lwt_1746698877573.FyMmk.Label",
                    "fieldId": "BI_61946d085af9d7000104f82b"
                },
                {
                    "refObjName": "org_employee_user",
                    "fieldName": "创建人",
                    "objName": "瓜瓜",
                    "dbFieldName": "created_by",
                    "fieldType": "Circle",
                    "columnKey": "Bi.Custom.Realtime.LwtHeader.BI_lwt_1746698877573.5KE7p.Label",
                    "fieldId": "BI_61946d085af9d7000104f84a"
                },
                {
                    "fieldName": "数字(求和)",
                    "objName": "瓜瓜",
                    "dbFieldName": "field_LKyOt__c",
                    "fieldType": "Number",
                    "columnKey": "Bi.Custom.Realtime.LwtHeader.BI_lwt_1746698877573.K4TdN.Label",
                    "fieldId": "BI_bb08fc7d10b7035b8dce074e4eedf"
                },
                {
                    "fieldName": "主属性(唯一计数)",
                    "objName": "瓜瓜",
                    "dbFieldName": "name",
                    "fieldType": "Number",
                    "columnKey": "Bi.Custom.Realtime.LwtHeader.BI_lwt_1746698877573.FRgFG.Label",
                    "fieldId": "BI_61946d085af9d7000104f81a"
                }
            ]
        ],
        "dataSet": [
            [
                {
                    "displayValue": "20250324-1",
                    "value": "20250324-1$$67e0d9e27258120007546170",
                    "dataFormatStr": ""
                },
                {
                    "displayValue": "20250324",
                    "value": "20250324",
                    "dataFormatStr": ""
                },
                {
                    "displayValue": "中-gua",
                    "value": "1198",
                    "dataFormatStr": ""
                },
                {
                    "displayValue": "1.93亿",
                    "value": "192500000.00000000",
                    "dataFormatStr": ""
                },
                {
                    "displayValue": "1",
                    "valueCode": "1044g",
                    "value": "1.00000000",
                    "dataFormatStr": ""
                }
            ],
            [
                {
                    "displayValue": "20250324-2",
                    "value": "20250324-2$$67e0fbde7258120007557c6e",
                    "dataFormatStr": ""
                },
                {
                    "displayValue": "20250324",
                    "value": "20250324",
                    "dataFormatStr": ""
                },
                {
                    "displayValue": "中-gua",
                    "value": "1198",
                    "dataFormatStr": ""
                },
                {
                    "displayValue": "1.93亿",
                    "value": "192500000.00000000",
                    "dataFormatStr": ""
                },
                {
                    "displayValue": "1",
                    "valueCode": "1044g",
                    "value": "1.00000000",
                    "dataFormatStr": ""
                }
            ]
        ]
    }
    
    

**Groovy 举例**
    
    
    def (isError, data, errorMsg) = Fx.BI.queryLwtViewDataByPage("BI_lwt_1657506871248", 1, 1)
    if (!isError) {
        log.info("分页信息:" + data["page"])
        log.info("表头信息:" + data["displayFields"])
        log.info("数据集:" + data["dataSet"])
    } else {
        log.info("查询失败:" + errorMsg)
    }
    
    

**负责人：翟付杰Jeffrey**

### # 15\. queryLwtViewDataByFilter 通过筛选查询数据

> `Fx.BI.queryLwtViewDataByFilter(<String viewId>, <Array filterList>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
viewId | String | 视图ID，用于指定要查询的视图 | 是  
filterList | Array[array] | 过滤条件列表 | 是  
filterList | 类型 | 描述 | 是否必填  
---|---|---|---  
filterId | String | 过滤器ID | 是  
value1 | String | 过滤值1 | \--  
value2 | String | 过滤值2，用于范围查询 | \--  
dateRangeId | Integer | 日期范围ID | \--  
  
出参格式

参数名称 | object | 描述  
---|---|---  
page | 类型 |   
displayFields | 类型[array] |   
dataSet | array[array] |   
page | 类型 | 描述  
---|---|---  
pageCount | Integer | 总共的页面数  
pageNumber | Integer | 当前显示的页面编号  
pageSize | Integer | 每页显示的记录数量  
totalCount | Integer | 数据集中的总记录数量  
displayFields | object | 描述  
---|---|---  
fieldName | String | 表头名称  
objName | String | 对象名称  
dbFieldName | String | 字段apiName  
fieldType | String | 字段类型  
columnKey | String | 唯一标识  
fieldId | String | 字段id  
refObjName | String | 关联对象apiName  
dataSet | 类型 | 描述  
---|---|---  
displayValue | String | 用于显示的数据值  
value | String | 实际数据值  
dataFormatStr | String | 数据的格式化字符串  
valueCode | String | 数据值的编码  
  
出参样例
    
    
    {
        "page": {
            "pageCount": 1,
            "pageNumber": 1,
            "pageSize": 20,
            "totalCount": 11
        },
        "displayFields": [
            [
                {
                    "fieldName": "主属性",
                    "objName": "瓜瓜",
                    "dbFieldName": "name",
                    "fieldType": "String",
                    "columnKey": "Bi.Custom.Realtime.LwtHeader.BI_lwt_1746698877573.bJO7v.Label",
                    "fieldId": "BI_61946d085af9d7000104f81c"
                },
                {
                    "fieldName": "创建时间",
                    "objName": "瓜瓜",
                    "dbFieldName": "create_time",
                    "fieldType": "Date",
                    "columnKey": "Bi.Custom.Realtime.LwtHeader.BI_lwt_1746698877573.FyMmk.Label",
                    "fieldId": "BI_61946d085af9d7000104f82b"
                },
                {
                    "refObjName": "org_employee_user",
                    "fieldName": "创建人",
                    "objName": "瓜瓜",
                    "dbFieldName": "created_by",
                    "fieldType": "Circle",
                    "columnKey": "Bi.Custom.Realtime.LwtHeader.BI_lwt_1746698877573.5KE7p.Label",
                    "fieldId": "BI_61946d085af9d7000104f84a"
                },
                {
                    "fieldName": "数字(求和)",
                    "objName": "瓜瓜",
                    "dbFieldName": "field_LKyOt__c",
                    "fieldType": "Number",
                    "columnKey": "Bi.Custom.Realtime.LwtHeader.BI_lwt_1746698877573.K4TdN.Label",
                    "fieldId": "BI_bb08fc7d10b7035b8dce074e4eedf"
                },
                {
                    "fieldName": "主属性(唯一计数)",
                    "objName": "瓜瓜",
                    "dbFieldName": "name",
                    "fieldType": "Number",
                    "columnKey": "Bi.Custom.Realtime.LwtHeader.BI_lwt_1746698877573.FRgFG.Label",
                    "fieldId": "BI_61946d085af9d7000104f81a"
                }
            ]
        ],
        "dataSet": [
            [
                {
                    "displayValue": "20250324-1",
                    "value": "20250324-1$$67e0d9e27258120007546170",
                    "dataFormatStr": ""
                },
                {
                    "displayValue": "20250324",
                    "value": "20250324",
                    "dataFormatStr": ""
                },
                {
                    "displayValue": "中-gua",
                    "value": "1198",
                    "dataFormatStr": ""
                },
                {
                    "displayValue": "1.93亿",
                    "value": "192500000.00000000",
                    "dataFormatStr": ""
                },
                {
                    "displayValue": "1",
                    "valueCode": "1044g",
                    "value": "1.00000000",
                    "dataFormatStr": ""
                }
            ],
            [
                {
                    "displayValue": "20250324-2",
                    "value": "20250324-2$$67e0fbde7258120007557c6e",
                    "dataFormatStr": ""
                },
                {
                    "displayValue": "20250324",
                    "value": "20250324",
                    "dataFormatStr": ""
                },
                {
                    "displayValue": "中-gua",
                    "value": "1198",
                    "dataFormatStr": ""
                },
                {
                    "displayValue": "1.93亿",
                    "value": "192500000.00000000",
                    "dataFormatStr": ""
                },
                {
                    "displayValue": "1",
                    "valueCode": "1044g",
                    "value": "1.00000000",
                    "dataFormatStr": ""
                }
            ]
        ]
    }
    
    

**Groovy 举例**
    
    
    List filterList = [["filterId": "BI_62cb8af6741ac20001debf72", "value1": "", "value2": "", "dateRangeId": 6]];
    def (isError, data, errorMsg) = Fx.BI.queryLwtViewDataByFilter("BI_lwt_1657506871248", filterList)
    if (!isError) {
        log.info("分页信息:" + data["page"])
        log.info("表头信息:" + data["displayFields"])
        log.info("数据集:" + data["dataSet"])
    } else {
        log.info("查询失败:" + errorMsg)
    }
    
    

**负责人：翟付杰Jeffrey**

### # 16\. queryMultiDimViewDataById 根据Id查询 多维度/层级统计图

> `Fx.BI.queryMultiDimViewDataById(<String viewId>)`

**参数说明**

入参格式

参数名称 | 根据Id查询 | 描述 | 是否必填  
---|---|---|---  
viewId | String | 视图ID，用于指定要查询的视图 | 是  
  
出参格式

参数名称 | BI视图显示数据 | 描述  
---|---|---  
displayFields | 显示字段列表[object] | 定义视图中显示的字段信息  
dataSet | 数据集[array] | 查询结果数据集  
displayFields | object | 描述  
---|---|---  
fieldName | String | 字段显示名称  
viewFieldId | String | 视图字段ID  
fieldId | String | 字段ID  
dataSet | 数据项 | 描述  
---|---|---  
formattedValue | String | 格式化后的值  
formattedShowValue | String | 格式化后的显示值  
valueCode | String | 值编码，可能包含引用ID  
value | String | 原始值  
  
出参样例
    
    
    {
        "displayFields": [
            {
                "fieldName": "客户名称",
                "viewFieldId": "BI_682ae4f89a6d0e000111052f",
                "fieldId": "BI_5bcebcddcab2980001ee22ab"
            },
            {
                "fieldName": "订单金额",
                "viewFieldId": "BI_682ae4f99a6d0e0001110530",
                "fieldId": "BI_5bceda90dedd2c0001c2f54e"
            }
        ],
        "dataSet": [
            [
                {
                    "formattedValue": "多维水果1",
                    "formattedShowValue": "多维水果1",
                    "valueCode": "多维水果1$$60f14d96fd6db100011adaeb",
                    "value": "多维水果1"
                },
                {
                    "formattedValue": "1.53万",
                    "formattedShowValue": "15,300.00",
                    "valueCode": "15300.0",
                    "value": "15300.0"
                }
            ],
            [
                {
                    "formattedValue": "多维水果10",
                    "formattedShowValue": "多维水果10",
                    "valueCode": "多维水果10$$60f14d96fd6db100011adaf9",
                    "value": "多维水果10"
                },
                {
                    "formattedValue": "1.54万",
                    "formattedShowValue": "15,390.00",
                    "valueCode": "15390.0",
                    "value": "15390.0"
                }
            ]
        ]
    }
    
    

**Groovy 举例**
    
    
    String viewId = "BI_64e9dc157386e90001dfba59";//图表名称-》指定层级带序号-3
    def (Boolean isError, Nap data, String errorMsg) = Fx.BI.queryMultiDimViewDataById(viewId)
    if (!isError) {
        log.info("表头信息:" + data["displayFields"])
        log.info("数据集:" + data["dataSet"])
    } else {
        log.info("查询失败:" + errorMsg)
    }
    
    

**负责人：翟付杰Jeffrey**

### # 17\. queryMultiDimViewDataByFilter 根据筛选器、图表Id 查询多维度/层级统计图

> `Fx.BI.queryMultiDimViewDataByFilter(<String viewId>, <Array filters>)`

**参数说明**

入参格式

参数名称 | BI多维视图数据查询 | 根据过滤条件查询BI多维视图数据 | 是否必填  
---|---|---|---  
viewId | String | 图表ID，例如：BI_64e9dc157386e90001dfba59 | 是  
filters | Array[array] | 筛选条件列表 | 是  
filters | object | 描述 | 是否必填  
---|---|---|---  
filterId | String | 过滤器ID | 是  
value1 | String | 过滤值，可以是JSON字符串，表示复杂的筛选条件 | \--  
value2 | String | 过滤值2，用于范围查询 | \--  
dateRangeId | Integer | 日期范围ID | \--  
  
出参格式

参数名称 | BI视图显示数据 | 描述  
---|---|---  
displayFields | 显示字段列表[object] | 定义视图中显示的字段信息  
dataSet | 数据集[array] | 查询结果数据集  
displayFields | object | 描述  
---|---|---  
fieldName | String | 字段显示名称  
viewFieldId | String | 视图字段ID  
fieldId | String | 字段ID  
dataSet | 数据项 | 描述  
---|---|---  
formattedValue | String | 格式化后的值  
formattedShowValue | String | 格式化后的显示值  
valueCode | String | 值编码，可能包含引用ID  
value | String | 原始值  
  
出参样例
    
    
    {
        "displayFields": [
            {
                "fieldName": "客户名称",
                "viewFieldId": "BI_682ae4f89a6d0e000111052f",
                "fieldId": "BI_5bcebcddcab2980001ee22ab"
            },
            {
                "fieldName": "订单金额",
                "viewFieldId": "BI_682ae4f99a6d0e0001110530",
                "fieldId": "BI_5bceda90dedd2c0001c2f54e"
            }
        ],
        "dataSet": [
            [
                {
                    "formattedValue": "多维水果1",
                    "formattedShowValue": "多维水果1",
                    "valueCode": "多维水果1$$60f14d96fd6db100011adaeb",
                    "value": "多维水果1"
                },
                {
                    "formattedValue": "1.53万",
                    "formattedShowValue": "15,300.00",
                    "valueCode": "15300.0",
                    "value": "15300.0"
                }
            ],
            [
                {
                    "formattedValue": "多维水果10",
                    "formattedShowValue": "多维水果10",
                    "valueCode": "多维水果10$$60f14d96fd6db100011adaf9",
                    "value": "多维水果10"
                },
                {
                    "formattedValue": "1.54万",
                    "formattedShowValue": "15,390.00",
                    "valueCode": "15390.0",
                    "value": "15390.0"
                }
            ]
        ]
    }
    
    

**Groovy 举例**
    
    
    String viewId = "BI_64e9dc157386e90001dfba59"; //图表Id 图标名称：指定层级带序号-3
    List filters = [ //筛选范围
        [
            "filterId":"BI_64e9dc157386e90001dfba60",
            "value1":"[{\"nodeName\":\"负责人主属部门-2\",\"optionCode\":2,\"value\":2,\"type\":\"l\"}]"
        ]
    ]
    def (Boolean isError3, Map data3, String errorMsg3) = Fx.BI.queryMultiDimViewDataByFilter(viewId, filters)
    if(!isError3) {
      log.info("表头信息:" + data3["displayFields"])
      log.info("数据集:" + data3["dataSet"])
    } else {
      log.info("条件查询失败:" + errorMsg3)
    }
    
    

**负责人：翟付杰Jeffrey**

[Fx.template](../TemplateAPI/) [Fx.cache](../CacheAPI/)

← [Fx.template](../TemplateAPI/) [Fx.cache](../CacheAPI/)→ 

  * 跟随系统 
  * 浅色模式 
  * 深色模式 
  * 阅读模式 


