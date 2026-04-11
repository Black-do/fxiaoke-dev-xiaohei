#  Fx.lock

## # Fx.lock

### # 1\. lock 使用redisson 的分布式锁，解锁为FxLock.unLock();

> `Fx.lock.lockData(<String apiName>, <String dataId>, <Integer expireTime>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
apiName | String | 对象的apiname | 是  
dataId | String | 数据ID | 是  
expireTime | Integer | 失效时间 | 是  
  
**Groovy 举例**
    
    
    //加锁一定要细粒度，防止锁竞争等待
    FxLock lock = Fx.lock.lockData("Account","dataId", 2)
    
    // 需要加锁的函数代码
    // do something
    
    lock.unlock()
    
    

**注意事项**

>   * 错误示例：如lock("prepareData")这样，这种锁粒度过粗，反而会影响业务；
>   * 要使用细粒度的锁，如数据id，针对某个数据加锁，防止并发产生问题
> 


[Fx.stage](../StageAPI/) [Fx.mq](../MqAPI/)

← [Fx.stage](../StageAPI/) [Fx.mq](../MqAPI/)→ 

  * 跟随系统 
  * 浅色模式 
  * 深色模式 
  * 阅读模式 


