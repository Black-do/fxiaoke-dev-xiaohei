#  String类型

# # String类型

String - 字符串类型，使用时用""封装，中间可写任意字符（中文、英文、符号等）

  * 定义String：String string = ""



例：
    
    
    String string = "张三"
    

  * String类型的方法：



string.contains(<String str>)：判断字符串中是否包含特定序列或字符 返回值类型：Boolean

例：
    
    
    "fx is great".contains("fx") //返回：true
    

  * string.startsWith(<String str>)：检测是否以特定字符串开头 返回值类型：Boolean



例：
    
    
    "fx is great".startsWith("fx") //返回：true
    

  * string.endsWith(<String str>)：检测是否以特定字符串结尾 返回值类型：Boolean



例：
    
    
    "fx is great".endsWith("fx") //返回：false
    

  * string.concat(<String str>)：将制定的字符串加在此字符串的末尾 返回值类型：String



例：
    
    
    "fx is great".concat("fx") //返回：fx is greatfx
    

  * string.isEmpty()：判断是否为空 返回值类型：Boolean



例：
    
    
    "fx ".isEmpty() //返回：false
    

  * string.trim()：返回字符串的副本，忽略前导空白和尾部空白 返回值类型：String



例：
    
    
    "  Welcome to fxiaoke Creator ".trim() //返回：Welcome to fxiaoke Creator
    

  * string.replace(<String searchString>,<String replacement>)：使用给定的参数replacement替换字符串所有匹配给定的searchString的子字符串 返回值类型：String



例：
    
    
    "Red,Green,Green".replace("Green","Blue") //返回：Red,Blue,Blue
    

  * string.replaceAll(<String regex>,<String replacement>)：使用给定的参数replacement替换字符串所有匹配给定的regex(正则表达式)的子字符串 返回值类型：String



例：
    
    
    "Red,Green,Green".replaceAll("Green","Blue") //返回：Red,Blue,Blue
    

  * string.substring(<Integer startIndex>,<Integer endIndex>)：返回一个新字符串，它是此字符串中的一个子字符串 返回值类型：String



例：
    
    
    "www.fxiaoke.com".substring(4,11) //返回：fxiaoke
    

注：在程序语言中，是从第0位开始的，所以上例中的第四位是f；最终返回的结果中包含startIndex，不包含endIndex

  * string.split(<String regex>) 或 string.split(<String regex>,<Integer limit>)根据匹配给定的正则表达式来拆分字符串 返回值类型：String[]



例：
    
    
    "www-fxiaoke-com".split("-") //返回：["www","fxiaoke","com"]
    "www-fxiaoke-com".split("-","2") //返回：["www","fxiaoke-com"]
    

注：在string.split(<String regex>,<Integer limit>)中limit表示将该字符串最多拆分成几个字符串

  * string.length()返回此字符串的长度 返回值类型：BigDecimal



例：
    
    
    "www.fxiaoke.com".length() //返回：15
    

  * string.indexOf(<String subString>)返回指定子字符串在此字符串中第一次出现处的索引，从指定的索引处开始（默认从0开始） 或string.indexOf(<String subString>,<SBigDecimal fromIndex>)返回指定子字符串在此字符串中从fromIndex后第一次出现处的索引，从指定的索引处开始（默认从0开始）



返回值类型：BigDecimal

例：
    
    
    "www.fxiaoke.com".indexOf("o") //返回：8
    "www.fxiaoke.com".indexOf("o"，9) //返回：13
    

  * string.lastIndexOf(<String subString>)返回指定子字符串在此字符串中最后一次出现处的索引，从指定的索引处开始反向搜索 或 string.lastIndexOf(<String subString>,<BigDecimal fromIndex>)返回指定子字符串在此字符串中在lastIndexOf前最后一次出现处的索引，从指定的索引处开始反向搜索



返回值类型：BigDecimal

例：
    
    
    "www.fxiaoke.com".indexOf("o") //返回：13
    "www.fxiaoke.com".indexOf("o",9) //返回：8
    

  * string.toUpperCase()：转换为大写字母 返回值类型：String



例：
    
    
    "abc".toUpperCase() //返回：ABC
    

  * string.toLowerCase()：转换为小写字母 返回值类型：String



例：
    
    
    "ABC".toLowerCase() //返回：abc
    

[BigDecimal类型](../BigDecimal/) [Integer类型](../Integer/)

← [BigDecimal类型](../BigDecimal/) [Integer类型](../Integer/)→ 

  * 跟随系统 
  * 浅色模式 
  * 深色模式 
  * 阅读模式 


