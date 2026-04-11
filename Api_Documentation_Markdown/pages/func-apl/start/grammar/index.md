#  基础语法

# # 基础语法

## # 1\. 自定义函数基本语法和通用计算机语言语法一致

如： <数据类型> <变量> = <表达式>

语法构成 | 说明  
---|---  
数据类型 | 在自定义函数中提供12大数据类型，具体可参考数据类型章节（区分大小写）  
变量 | 即该数据的名称，用于在之后逻辑中的调用，可自定义设置（不可和数据类型一样）  
表达式 | 即该变量被赋予的值，可以是被直接定义的也可为一个表达式（如果是表达式请注意表达式返回值类型要与数据类型一致，否则报错）  
  
**注：在自定义函数中可用 def 表示数据类型，编译时自动识别数据类型**

举例：
    
    
        String str = "fxiaoke" //被直接定义
    
        Boolean boo = ["red", "blue", "green", "yellow"].isEmpty() //表达式定义
    
        def result = ["red", "blue", "green", "yellow"].isEmpty() //def表示数据类型
    

## # 2\. switch

用来判定所给定的条件是否满足，根据判定的结果（真或假）决定执行哪个操作

### # 2.1 定义
    
    
            switch(<key>){
    
               case <value-1>: statements-1; break;
    
               case <value-2>: statements-2; break;
    
               default: statements-3; break;
    
           }
    
           //执行顺序：当key值和value-1的值一样时，执行statements-1并结束；如果key和value-1值不等，但等于value-2时，执行statements-2并结束；...;如果都不相等，则执行statements-3并结束
    

注
    
    
    1.case语句可以存在多个；
    2.可以没有default语句，但为防止因未在case语句中匹配到与key值相等的value报错，尽量存在一个（最多一个）default语句；
    3.在每个case和default语句后可以没有break;语句，表示不结束switch语句，继续执行，如在上例中没有break语句，假设key和value-2相等，则在执行完statements-2后会再执行statements-3
    

### # 2.2 举例
    
    
            Integer = 3
            switch (day) {
    
                case 0:   x="Today it's Sunday";    break;
    
                case 1:   x="Today it's Monday";    break;
    
                case 2:   x="Today it's Tuesday";   break;
    
                case 3:   x="Today it's Wednesday"; break;
    
                case 4:   x="Today it's Thursday";  break;
    
                case 5:   x="Today it's Friday";    break;
    
                case 6:   x="Today it's Saturday";  break;
    
           }//最终结果 Today it's Wednesday
    

## # 3\. if-else

用来判定所给定的条件是否满足，根据判定的结果（真或假）决定执行哪个操作

### # 3.1 定义
    
    
            if(条件1) {
    
               如果条件1为真，则执行这里
    
           }else if(条件2){
    
               如果条件2为真，则执行这里
    
           }else {
    
               如果条件1和条件2都不为真，则执行这里
    
           }
    

注：在if控制语句中必须存在if和else控制语句，else if可以有0个或多个，根据实际场景使用

### # 3.2 举例
    
    
            String str = "fxiaoke"
    
           if(str.contains("s")) {
    
               str = "hello"
    
           }else if(str.contains("f")){
    
               str = "welcome"
    
           }else {
    
               str = "hi"
    
           }//最终结果 str=welcome
    

[FQL说明](../fql/) [函数平台限制](../limit/)

← [FQL说明](../fql/) [函数平台限制](../limit/)→ 

  * 跟随系统 
  * 浅色模式 
  * 深色模式 
  * 阅读模式 


