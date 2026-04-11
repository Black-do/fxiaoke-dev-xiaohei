#  context

### # 获取自定义函数所绑定对象的数据信息

### # context 已支持数据

分类 | 变量名 | 数据 | 备注  
---|---|---|---  
通用 | context.tenantId | 字符串，当前租户id | 所有函数都有该数据  
| context.userId | 字符串，当前用户id | 所有函数都有该数据，-10000 标识以系统身份执行。分为两种情况：（1）通过页面操作直接触发的函数，这里用户 id 为实际操作的 userId；（2）通过系统后台调用的函数，用户 id 为 -10000 标识以系统身份执行  
| context.data | Map，当前操作的主对象数据 | 按钮、流程触发的函数均有该数据；**针对异步处理的字段如统计字段，计算字段，引用字段，可能会不准确，建议通过fql重新查询获取对应值**  
| context.details | Map，当前操作的从对象数据 | debug 调试时只加载 6 条从对象数据，正常运行时加载全量数据；2024.4.1号之后新创建的流程函数不再支持context.details  
| context.dataList | List，当前操作的批量数据 | 批量UI按钮触发的函数会将批量选中数据  
| context.objectIds | List，当前操作的对象数据的 id 列表 | 计划任务绑定对象的函数会有该数据  
| context.arg | Map，业务侧的传递参数 | 部分业务场景下将业务参数通过该属性透传给函数  
互联 | context.outTenantId | 字符串，当前互联外部租户 id | 大于 10,000,000 的数字，仅按钮 EM6 互联请求会有该数据  
| context.outUserId | 字符串，当前互联外部用户 id | 大于 10,000,000 的数字，仅按钮 EM6 互联请求会有该数据  
| context.appId | 字符串，当前互联应用 AppId | 仅按钮 EM6 互联请求会有该数据  
| context.upstreamOwnerId | 字符串，当前下游对应上游企业对接人 |   
| context.thirdType | 字符串，下游登录方式 | 2：纷享；4：微信服务号；5：小程序；6：微信扫码登录；7：第三方登录；8：微信统一登录  
| context.thirdAppId | 第三方登录方式对应的应用id | 例如微信服务号appid  
| context.thirdUserId | 第三方登录方式对应的用户id | 例如微信服务号的open_id  
  
### # 各个场景 context 开放情况

命名空间 | 业务类型 | 使用场景 | 正常运行 context | debug context | 备注  
---|---|---|---|---|---  
按钮/操作 | 自定义业务按钮 | 前验证 | context.data | context.data | 不支持 details  
| （1）自定义业务按钮；（2）自定义UI按钮（单条） | 执行动作 | （1）context.data；（2）context.details；（3）context.arg | （1）context.data；（2）context.details |   
| 自定义UI按钮（批量） | 执行动作 | context.dataList | context.dataList | 这里是对象数据的 list  
| （1）新建保存按钮；（2）编辑保存按钮 | （1）前验证；（2）后动作；（3）跳转动作 | （1）context.data；（2）context.details；（3）context.arg | （1）context.data；（2）context.details |   
| （1）新建UI按钮；（2）编辑UI按钮 | 前验证 | context.data | context.data | 不支持 details  
| 更换负责人 | 前验证 | context.data | context.data | 不支持 details  
| 复制 | 前验证 | context.data | context.data | 不支持 details  
| 锁定 | （1）前验证；（2）后动作 | context.data | context.data | 不支持 details  
| 解锁 | （1）前验证；（2）后动作 | context.data | context.data | 不支持 details  
| 作废 | 前验证 | （1）context.data；（2）context.arg | context.data | 不支持 details  
|  | 后动作 | （1）context.data；（2）context.details；（3）context.arg | （1）context.data；（2）context.details |   
| 打印 | （1）前验证；（2）后动作 | context.data | context.data | 不支持 details  
| 添加相关团队成员 | （1）前验证；（2）后动作 | （1）context.data；（2）context.arg | （1）context.data；（2）context.arg | context.arg 传入的是添加提交的相关团队成员数据  
| 编辑相关团队成员 | （1）前验证；（2）后动作 | （1）context.data；（2）context.arg | （1）context.data；（2）context.arg | context.arg 传入的是编辑提交的相关团队成员数据  
| 移除相关团队成员 | （1）前验证；（2）后动作 | （1）context.data；（2）context.arg | （1）context.data；（2）context.arg | context.arg 传入的是移除提交的相关团队成员数据  
流程 | - | - | （1）context.data；（2）context.details | （1）context.data；（2）context.details | 2024.2.24号之后新创建的流程函数不再支持context.details；使用该字段会有报错  
查找关联数据范围 | 主对象-查找关联字段 | - | context.data，主对象数据 | context.data，主对象数据 |   
| 从对象-查找关联字段 | 主从一起新建 | （1）context.data，主对象数据；（2）context.details，当前触发的从对象数据 | context.data，当前选择的从对象数据 | 此处 debug 与正常运行行为有差别  
|  | 从单独新建 | context.data，当前从对象数据 | context.data，当前从对象数据 | 与主单独新建行为一致  
自增编号 | 主对象-自增编号字段 | - | context.data | context.data | 不支持 details  
| 从对象-自增编号字段 | - | context.data，当前从对象数据 | context.data，当前选择的从对象数据 |   
计划任务 | 绑定对象 | - | context.objectIds，匹配条件的数据id | context.objectIds，当前选择的数据id |   
| 不绑定对象 | - | - | - |   
  
### # 前验证/UI事件中字段为空的差异

  * **web端** ：字段为空是空串 `''`。
  * **移动端/server端** ：字段为空是 `null`。



### # 带来的影响

在前验证/UI事件中获取字段 `value` 时，除了判定 `value != null` 外，还需判定 `value != ''`，否则可能会拿到 `''` 导致后续逻辑错误。

### # Debug 调试与正常运行的差异

  * **context.details** ：debug 调试时只加载 6 条从对象数据，正常运行时加载全量数据。



[Integer类型](../../data-type/Integer/) [Fx.object](../ObjectDataAPI/)

← [Integer类型](../../data-type/Integer/) [Fx.object](../ObjectDataAPI/)→ 

  * 跟随系统 
  * 浅色模式 
  * 深色模式 
  * 阅读模式 


