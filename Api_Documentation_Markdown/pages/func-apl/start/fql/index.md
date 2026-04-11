#  FQL说明

## # 1\. 什么是FQL

FQL是能够在APL里使用的类SQL查询语句，开发人员能够在APL中使用FQL查询企业中的业务数据

## # 2\. FQL语法
    
    
       SELECT
       字段名1 [, 字段名2 ...]
       [FROM 对象apiName
       [WHERE where_condition]
       [ORDER BY {col_name | expr | position}
       [ASC | DESC], ...]
       [LIMIT {[offset,] row_count | row_count OFFSET offset}]
    

注意项

  * 不支持select *查询所有字段，只能通过select field1, field2...按需查找相关字段
  * limit默认为10，最大值为100，offset默认为0
  * 使用OR条件需要单独开通，请联系销售人员下订单开通产品：【对象列表筛选支持或】



## # 3\. Where条件支持的操作符

  * 与查询：AND


    
    
       - select name from object_227xW__c where (field_rzv5M__c is null and field_rzv5M__c<= 100) order by _id desc limit 10 offset 0;
    

  * 或查询：OR（SQL中AND运算符的优先级高于OR运算符，想要优先执行OR运算符时，需要使用括号）


    
    
    select name from object_227xW__c where (field_rzv5M__c is null or field_rzv5M__c<= 100) order by _id desc limit 10 offset 0;
    

  * 判断相等和不相等：=，!=


    
    
    select _id, field_rzv5M__c, name from object_227xW__c where field_oc43W__c = '13988523405' limit 10 offset 0;
    select _id, field_rzv5M__c, name from object_227xW__c where field_oc43W__c != '13988523405' limit 10 offset 0;
    select _id, field_rzv5M__c, name from object_227xW__c where field_rzv5M__c = 100 limit 10 offset 0;
    select _id, field_rzv5M__c, name from object_227xW__c where field_rzv5M__c != 100 limit 10 offset 0;
    

  * 大于：>，小于：<select _id, field_rzv5M__c, name from object_227xW__c where field_rzv5M__c>100 limit 10 offset 0;


    
    
    select _id, field_rzv5M__c, name from object_227xW__c where field_rzv5M__c<100 limit 10 offset 0;
    

  * 大于或等于：>=，小于或等于：=<select _id, field_rzv5M__c, name from object_227xW__c where field_rzv5M__c>= 100 limit 10 offset 0;


    
    
    select _id, field_rzv5M__c, name from object_227xW__c where field_rzv5M__c<= 100 limit 10 offset 0;
    

  * 模糊查询：like，not like，当 like 'xx' 没有放 %时相当于=


    
    
    select _id, field_rzv5M__c, name from object_227xW__c where field_oc43W__c like '%88523%';
    select _id, field_rzv5M__c, name from object_227xW__c where field_oc43W__c like '%88523';
    select _id, field_rzv5M__c, name from object_227xW__c where field_oc43W__c like '88523%';
    select _id, field_rzv5M__c, name from object_227xW__c where field_oc43W__c not like '%88523%';
    

  * null值判断：is null，is not null


    
    
    select _id, field_rzv5M__c, name from object_227xW__c where field_rzv5M__c is null;
    select _id, field_rzv5M__c, name from object_227xW__c where field_rzv5M__c is not null;
    

  * 数组包含：@>，适用于单选、多选等数据类型为List的字段


    
    
    select _id, field_D8JyW__c, name from object_227xW__c where field_D8JyW__c @>ARRAY['option1', 'option2'];
    

  * 数组有重叠元素：&&，适用于人员多选，部门多选，比如 ARRAY[1,4,3]&&ARRAY[2,1] = true，有重复元素1，ARRAY[1,4,3]&&ARRAY[2] = false 没有重复元素

  * 当查询语句中使用&&和其他操作符的组合时，&&需要加上括号，否则会出现解析错误



    
    
    //例如：
    select _id, name from object_C0vxo__c where create_time>0 and field_7cQ6y__c&&ARRAY[1000]
    //需要改成：
    select _id, name from object_C0vxo__c where create_time>0 and (field_7cQ6y__c&&ARRAY[1000])
    select _id from object_C0vxo__c where field_7cQ6y__c&&ARRAY[1000];
    

  * in语句：IN，NOT IN


    
    
    select _id, field_rzv5M__c, name from object_227xW__c where field_rzv5M__c IN (21, 100);
    select _id, field_rzv5M__c, name from object_227xW__c where field_rzv5M__c not IN (21, 100);
    

  * between语句：BETWEEN AND，NOT BETWEEN AND


    
    
    select _id, field_rzv5M__c, name from object_227xW__c where field_rzv5M__c BETWEEN 21 and 100;
    select _id, field_rzv5M__c, name from object_227xW__c where field_rzv5M__c not BETWEEN 21 and 100;
    

## # 4\. 高级用法

  * 支持字段间的比较，不支持in，between，@>等操作符


    
    
    select name from AccountObj where last_modified_time>create_time;
    select name from AccountObj where name != firstName;
    select name from AccountObj where name = firstName;
    select name from AccountObj where name<= firstName;
    

  * 聚合查询支持聚合函数count/sum/min/max/avg和分组聚合grooup by（不支持having），
  * 聚合函数默认会从ES进行聚合


    
    
    - select count(1) from object_227xW__c where field_qC2yp__c is not null
    select sum(field_rzv5M__c) from object_227xW__c where field_qC2yp__c is not null group by field_qC2yp__c
    select max(field_rzv5M__c) from object_227xW__c where field_qC2yp__c is not null group by field_qC2yp__c
    select min(field_rzv5M__c) from object_227xW__c where field_qC2yp__c is not null group by field_qC2yp__c
    select avg(field_rzv5M__c) from object_227xW__c where field_qC2yp__c is not null group by field_qC2yp__c
    // 多聚合函数和和多group by字段
    select avg(field_rzv5M__c), sum(field_rzv5M__c) from object_227xW__c where field_qC2yp__c is not null group by field_qC2yp__c, record_type
    
    

## # 5\. 代码案例

Fx.object.select

  * 用来普通查询数据时返回值里的data类型是QueryResult，
  * 用来做聚合查询是data的类型是List


    
    
    //普通用法
    String sql = "select _id, field_rzv5M__c, name from object_227xW__c where field_rzv5M__c>100 limit 10 offset 0;"
    def rst = Fx.object.select(sql).result() as QueryResult
    log.info(rst)
    
    //如果需要查询不包含作废数据、返回满足条件的数据总数
    String sql1 = "select _id, field_rzv5M__c, name from object_227xW__c where field_rzv5M__c>100 limit 10 offset 0;"
    SelectAttribute att = SelectAttribute.builder()
    .needInvalid(false)
    .build()
    def rst1 = Fx.object.select(sql1, att).result() as QueryResult
    log.info(rst1)
    

[基础语法](../grammar/)

[基础语法](../grammar/)→ 

  * 跟随系统 
  * 浅色模式 
  * 深色模式 
  * 阅读模式 


