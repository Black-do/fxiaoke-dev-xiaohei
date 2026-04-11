#  Fx.netdisk

## # Fx.netdisk

### # 1\. exportNpathByFolderId 导出网盘npath

> `Fx.netdisk.exportNpathByFolderId(<string nodeCategory>, <array folderIDs>, <string employeeId>)`

**参数说明**

入参格式

参数名称 | object | 描述 | 是否必填  
---|---|---|---  
nodeCategory | string | 文件夹类型(公司、个人、共享) | 是  
folderIDs | array[string] | 文件夹ID列表 | 是  
employeeId | string | 员工ID | 是  
  
出参格式

参数名称 | object | 描述  
---|---|---  
isError | boolean | 是否错误  
data | object |   
message | string | 信息  
data | object | 描述  
---|---|---  
fileMessageInfos | object |   
fileMessageInfos | object | 描述  
---|---|---  
FileId | File List[object] | 文件信息列表  
FileId | object | 描述  
---|---|---  
nPath | string | 文件npath  
fileName | string | 文件的名称  
fileSize | integer | 文件的大小  
fileExtension | string | 文件的扩展名  
  
出参样例
    
    
    {
      "isError" : false,
      "data" : {},
      "message" : ""
    }
    
    

**Groovy 举例**
    
    
    def (Boolean error, Map data, String message) = Fx.netdisk.exportNpathByFolderId("Company", ["476d9244b9304c8abfde59d0f8274933","903d7c1172e24d4198136ebfada198a1"], 1000)
    if (error) {
      log.info("error :" + message)
    } else {
      log.info(data['fileMessageInfos'])
    }
    
    

**注意事项**

>   * 文件夹id可输入多个，输出的文件是该文件夹下所有文件的npath
> 


### # 2\. list list该网盘文件夹

> `Fx.netdisk.list(<String nodeCategory>, <String dir>, <String order>, <Integer desc>, <Integer start>, <Integer limit>, <Integer folder>, <Integer showEmpty>, <String employeeId>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
nodeCategory | String | 文件夹类型(公司、个人、共享) | 是  
dir | String | 文件夹名称 | 是  
order | String | 排序字段(name,time,size默认为name) | 是  
desc | Integer | 默认为升序,设置为1实现降序 | 是  
start | Integer | 分页起始位置,从0开始 | 是  
limit | Integer | 查询数目，默认为1000，建议最大不超过1000 | 是  
folder | Integer | 是否只返回文件夹，0 返回所有，1 只返回文件夹，且属性只返回path字段 | 是  
showEmpty | Integer | 是否返回dir_empty属性，0 不返回，1 返回 | 是  
employeeId | String | 员工ID | 是  
  
出参格式

参数名称 | APIResult | 描述  
---|---|---  
isError | boolean | 是否存在错误  
data | object | 返回的数据  
message | string | 信息  
data | object | 返回的数据  
---|---|---  
emptyDir | boolean | 是否为空文件夹  
fileMessageInfos | array[object] | 文件信息列表  
folderMessageInfos | array[object] | 文件夹信息列表  
fileMessageInfos | object | 描述  
---|---|---  
fileExtension | string | 文件扩展名  
fileName | string | 文件名  
fileSize | integer | 文件大小  
nPath | string | 文件的路径  
folderMessageInfos | object | 描述  
---|---|---  
fileSize | integer | 文件夹大小  
folderName | string | 文件夹名  
  
出参样例
    
    
    {
        "isError": false,
        "data": {
            "emptyDir": false,
            "fileMessageInfos": [
                {
                    "fileExtension": "txt",
                    "fileName": "example.txt",
                    "fileSize": 2048,
                    "nPath": "/files/example.txt"
                },
                {
                    "fileExtension": "jpg",
                    "fileName": "image.jpg",
                    "fileSize": 4096,
                    "nPath": "/files/image.jpg"
                }
            ],
            "folderMessageInfos": [
                {
                    "fileSize": 0,
                    "folderName": "Documents"
                },
                {
                    "fileSize": 0,
                    "folderName": "Images"
                }
            ]
        },
        "message": "success"
    }
    
    

**Groovy 举例**
    
    
    String nodeCategory = "Company"
    String dir = "阿里巴巴Java开发手册"
    String orderField = "name"
    Integer desc = 1
    Integer start = 0
    Integer limit = 10
    Integer folder = 0
    Integer showEmpty = 1
    Integer employeeId = 1017
    
    def(Boolean error, Map data, String message) = Fx.netdisk.list(nodeCategory, dir, orderField, desc, start, limit, folder, showEmpty, employeeId)
    if (error) {
      log.info("error:" + message)
    } else {
      List fileMessageInfos = data["fileMessageInfos"] as List
      log.debug(fileMessageInfos)
    }
    
    

**注意事项**

>   * 用户对该文件夹需要有访问权限
> 


### # 3\. saveFileToDir 将文件保存到网盘指定文件夹

> `Fx.netdisk.saveFileToDir(<array departmentIds>, <string path>, <string fileName>, <integer category>, <string folderPath>, <boolean autoCreateDir>, <boolean allowReName>, <boolean takeOwnership>)`

**参数说明**

入参格式

参数名称 | 类型 | 描述 | 是否必填  
---|---|---|---  
departmentIds | array[string] | 用户所属部门编号 | 是  
path | string | 要保存到网盘的文件路径，目前仅支持企业文件类型 | 是  
fileName | string | 文件名，需要携带后缀 | 是  
category | integer | 网盘文件夹类型：1公司，2个人，3共享（共享暂不支持） | 是  
folderPath | string | 网盘文件夹路径，以/开头以文件夹名称结尾 | 是  
autoCreateDir | boolean | 是否自动迭代创建缺失文件路径 | 是  
allowReName | boolean | 是否允许以增量形式重命名文件名称 | 是  
takeOwnership | boolean | 越权操作，获取网盘管理员权限 | 是  
  
出参格式

参数名称 | APIResult | 描述  
---|---|---  
isError | boolean | 是否发生错误  
data | object |   
message | string | 响应消息  
data | object | 描述  
---|---|---  
fileName | string | 文件名  
ei | string | 企业Id  
employeeId | integer | 员工ID  
ea | string | 企业account  
allowReName | boolean | 是否允许重命名  
folderId | string | 文件夹ID  
fileId | string | 文件ID  
  
出参样例
    
    
    {
        "isError": false,
        "data": {
            "fileName": "sonar-project",
            "ei": "90325",
            "employeeId": 1000,
            "ea": "90325",
            "allowReName": true,
            "folderId": "339cf3396af84405bd9171947cd0b5ef",
            "fileId": "3e2beed837e04df185e1683b43cbf17b"
        },
        "message": "success"
    }
    
    

**Groovy 举例**
    
    
    // 用户所属部门编号（可以为空，普通用户需要保存到部门文件夹时使用）
     List<Integer>departmentIds;
    // 需要保存到网盘的文件path（目前只支持企业文件，即以N_或TN_开头的文件）
     String path="N_202304_10_f438201727394b018e62e0ba48b6f349.pdf";
    // 文件名 （需要携带文件类型扩展名,文件名总长度不允许超过128,扩展名长度不允许超过20）
     String fileName="test15.pdf";
    // 网盘文件夹类型 （1 公司 2 个人 3 分享，目前暂不支持保存到分享文件夹）
     Integer category=1;
    // 文件路径 (绝对路径,必须以/ 开始 以文件名结束，最大支持嵌套层级 9)
     String folderPath="/2023/04/10/合同";
    // 是否自动迭代创建缺失文件路径 (默认false)
     Boolean autoCreateDir=true;
    // 是否允许以增量形式重命名文件名称 (例如：test.pdf->test(1).pdf 依次递增，默认 false)
     Boolean allowReName=true;
    // 越权操作，获取网盘管理员权限 （用于普通用户将文件保存到公司文件夹下 慎用！！！）
     Boolean takeOwnership=false;
    
    def (boolean error,Map data,String message) = Fx.netdisk.saveFileToDir(departmentIds, path, fileName, category, folderPath, autoCreateDir, allowReName, takeOwnership);
    
    if (error) {
      log.info("error:" + message)
    } else {
      log.info("data:" + data)
    }
    
    

[Fx.auth](../AuthAPI/) [Fx.industry](../IndustryAPI/)

← [Fx.auth](../AuthAPI/) [Fx.industry](../IndustryAPI/)→ 

  * 跟随系统 
  * 浅色模式 
  * 深色模式 
  * 阅读模式 


