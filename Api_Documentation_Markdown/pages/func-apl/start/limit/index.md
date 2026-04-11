#  函数平台限制

# # 函数平台限制

类 | 限制类别 | 限制值 | 限制范围 | 备注  
---|---|---|---|---  
函数编写限制 | 不能在闭包里使用的变量名称 | owner；this；delegate | 全网 | Range.each 或者 list.foreach 闭包内有该限制  
函数调用外部 HttpAPI 限制 | 超时时间限制 | connectTimeout，默认；2sreadTimeout，5s，最大 120s | 全网 |   
| 重试次数 | connectTimeout，默认重试 3 次，参数可改；readTimeout，默认不重试，参数可改；重试最大次数，3 次（以上两种 both) | 全网 |   
| Post 数据最大限制 | 5M | 全网 |   
函数调用内部 API 限制 | Fx.object 调用次数限制 | 300(每个函数) | 新企业 |   
| Fx.object.editTeamMember；Fx.object.addTeamMember；Fx.object.addOutTeamMember；Fx.object.deleteTeamMember；Fx.object.changeOwner；Fx.object.batchChangeOwner | 100(每个函数) | 全网 |   
| Fx.function 调用次数限制 | 50(每个函数) | 新企业 |   
| Fx.http | 50(每个函数) | 新企业 |   
| Fx.message | 50(每个函数) | 新企业 |   
| Fx.crm；Fx.work；Fx.file；Fx.AI；Fx.tag；Fx.approval | 100(每个函数) | 新企业 |   
函数执行限制 | 单个函数单条数据单位时间执行限制 | 一分钟限制100次 | 全网 | 超过执行次数限制函数执行报错  
| 单个企业同时执行函数 | 同时执行次数限制35个 | 全网 |   
计划任务执行限制 | 绑定对象 - 每日执行数据条数限制 | 专业版，无；旗舰版，10w；无限版，30w | 全网 | 可单独购买资源包扩展  
| 不绑定对象 - 每日执行时长限制 | 专业版，无；旗舰版，半个小时；无限版，1.5个小时 | 全网 | 可单独购买资源包扩展  
执行时间限制 | 新函数会根据命名空间进行运行时长限制 | 按钮 20s   
流程 5min   
自定义控制器 5min   
计划任务 10min   
电子签 180s   
认证提供商 180s   
互联数据同步60s   
校验函数 50s   
数据集成 300s  
事件监听 5min   
ERP集成平台 180s   
debug执行 120s  
其他默认15s | 所有函数 | 详见下文  
内存限制 | 函数会计算整个执行过程中使用的内存情况，对函数单次执行的内存信息进行限制 | 老函数：512m新函数：256m | 2024/1/1为时间分割线，区分新新函数 |   
  
**新企业指2021年2月4号以后开通的企业**

APL函数执行时间限制详细信息

表头 | 表头  
---|---  
命名空间 | 限制值  
debug执行 | 120s  
按钮 | 20s  
流程 | 300s  
自定义控制器 | 300s  
计划任务 | 600s  
电子签 | 180s  
认证提供商 | 180s  
互联数据同步 | 60s  
校验函数 | 50s  
数据集成 | 300s  
事件监听 | 300s  
ERP集成平台 | 180s  
默认 | 15s  
  
[基础语法](../grammar/) [数据类型介绍](../../data-type/DataType/)

← [基础语法](../grammar/) [数据类型介绍](../../data-type/DataType/)→ 

  * 跟随系统 
  * 浅色模式 
  * 深色模式 
  * 阅读模式 


