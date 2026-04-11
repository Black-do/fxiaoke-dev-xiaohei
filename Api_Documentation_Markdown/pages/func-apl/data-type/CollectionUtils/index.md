#  CollectionUtils类型

# # CollectionUtils类型

处理集合相关的方法

  * CollectionUtils.union(list1,list2): 返回两个list去的并集



举例：
    
    
    def list1 = ["A", "B", "C", "D", "E", "F"]
    def list2 = ["B", "D", "F", "G", "H", "K"]
    def re = CollectionUtils.union(list1, list2)
    log.info(re) // [A, B, C, D, E, F, G, H, K]
    

  * CollectionUtils.intersection(list1,list2): 返回两个list的交集



举例：
    
    
    def list1 = ["A", "B", "C", "D", "E", "F"]
    def list2 = ["B", "D", "F", "G", "H", "K"]
    def re = CollectionUtils.intersection(list1, list2)
    log.info(re) //[B, D, F]
    

  * CollectionUtils.disjunction(list1,list2): 返回两个list的交集的补集（析取）



举例：
    
    
    def list1 = ["A", "B", "C", "D", "E", "F"]
    def list2 = ["B", "D", "F", "G", "H", "K"]
    def re = CollectionUtils.disjunction(list1, list2)
    log.info(re) //[A, C, E, G, H, K]
    

  * CollectionUtils.subtract(list1,list2): 返回两个list的差集（扣除）



举例：
    
    
    def list1 = ["A", "B", "C", "D", "E", "F"]
    def list2 = ["B", "D", "F", "G", "H", "K"]
    def re = CollectionUtils.subtract(list1, list2)
    log.info(re) //[A, C, E]
    

  * CollectionUtils.isEqualCollection(list1,list2): 判断两个集合是否相等



举例：
    
    
    def list1 = ["A", "B", "C", "D", "E", "F"]
    def list2 = ["A", "F", "B", "C", "D", "E"]
    def re = CollectionUtils.isEqualCollection(list1, list2)
    log.info(re) //true
    

  * CollectionUtils.isSubCollection(list1,list2): list1是否为list2的子集



举例：
    
    
    def list1 = ["A", "F"]
    def list2 = ["A", "B", "C", "D", "E", "F"]
    def re = CollectionUtils.isSubCollection(list1, list2)
    log.info(re) //true
    

  * CollectionUtils.cardinality(str,list1): 元素出现的次数



举例：
    
    
    def list1 = ["A", "A", "A", "D", "E", "F"]
    String str = "A"
    def re = CollectionUtils.cardinality(str, list1)
    log.info(re) //3
    

[Math类型](../Math/) [Range类型](../Range/)

← [Math类型](../Math/) [Range类型](../Range/)→ 

  * 跟随系统 
  * 浅色模式 
  * 深色模式 
  * 阅读模式 


