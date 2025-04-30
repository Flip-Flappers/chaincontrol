# Swagger API


**简介**:Swagger API


**HOST**:localhost:8086


**联系人**:


**Version**:


**接口路径**:/v2/api-docs?group=Swagger API


[TOC]






# dynamic-route-controller


## 插件注册新的http接口


**接口地址**:`/plugin/http/dynamic/register`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|request|request|body|true|||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 插件注销http接口


**接口地址**:`/plugin/http/dynamic/unregister`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|request|request|body|true|||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


暂无


**响应示例**:
```javascript

```


# modbus


## 新建ModbusInfo


**接口地址**:`/modbus/add`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": {
    "createBy": 0,
    "createDept": 0,
    "createTime": "",
    "id": 0,
    "name": "",
    "productKey": "",
    "remark": "",
    "updateBy": 0,
    "updateTime": ""
  },
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|request|request|body|true|Request«ModbusInfoBo»|Request«ModbusInfoBo»|
|&emsp;&emsp;data|||false|ModbusInfoBo|ModbusInfoBo|
|&emsp;&emsp;&emsp;&emsp;createBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createDept|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createTime|||false|string||
|&emsp;&emsp;&emsp;&emsp;id|id||false|integer||
|&emsp;&emsp;&emsp;&emsp;name|产品名称||false|string||
|&emsp;&emsp;&emsp;&emsp;productKey|产品Key||false|string||
|&emsp;&emsp;&emsp;&emsp;remark|说明||false|string||
|&emsp;&emsp;&emsp;&emsp;updateBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;updateTime|||false|string||
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|ModbusInfoVo|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|createAt|创建时间|integer(int64)|integer(int64)|
|id|id|integer(int64)|integer(int64)|
|name|产品名称|string||
|productKey|产品Key|string||
|remark|说明|string||
|updateAt|修改时间|integer(int64)|integer(int64)|


**响应示例**:
```javascript
{
	"createAt": 0,
	"id": 0,
	"name": "",
	"productKey": "",
	"remark": "",
	"updateAt": 0
}
```


## 删除ModbusInfo


**接口地址**:`/modbus/deleteModbus`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": 0,
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|request|request|body|true|Request«long»|Request«long»|
|&emsp;&emsp;data|||false|integer(int64)||
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 编辑ModbusInfo


**接口地址**:`/modbus/edit`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": {
    "createBy": 0,
    "createDept": 0,
    "createTime": "",
    "id": 0,
    "name": "",
    "productKey": "",
    "remark": "",
    "updateBy": 0,
    "updateTime": ""
  },
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|request|request|body|true|Request«ModbusInfoBo»|Request«ModbusInfoBo»|
|&emsp;&emsp;data|||false|ModbusInfoBo|ModbusInfoBo|
|&emsp;&emsp;&emsp;&emsp;createBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createDept|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createTime|||false|string||
|&emsp;&emsp;&emsp;&emsp;id|id||false|integer||
|&emsp;&emsp;&emsp;&emsp;name|产品名称||false|string||
|&emsp;&emsp;&emsp;&emsp;productKey|产品Key||false|string||
|&emsp;&emsp;&emsp;&emsp;remark|说明||false|string||
|&emsp;&emsp;&emsp;&emsp;updateBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;updateTime|||false|string||
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 下载点位模版


**接口地址**:`/modbus/exportData`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


暂无


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 查看ModbusInfo详情


**接口地址**:`/modbus/getDetail`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": 0,
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|request|request|body|true|Request«long»|Request«long»|
|&emsp;&emsp;data|||false|integer(int64)||
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|ModbusInfoVo|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|createAt|创建时间|integer(int64)|integer(int64)|
|id|id|integer(int64)|integer(int64)|
|name|产品名称|string||
|productKey|产品Key|string||
|remark|说明|string||
|updateAt|修改时间|integer(int64)|integer(int64)|


**响应示例**:
```javascript
{
	"createAt": 0,
	"id": 0,
	"name": "",
	"productKey": "",
	"remark": "",
	"updateAt": 0
}
```


## 查看点位物模型


**接口地址**:`/modbus/getThingModelByProductKey`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": "",
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|request|request|body|true|Request«string»|Request«string»|
|&emsp;&emsp;data|||false|string||
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|ModbusThingModelVo|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|id|主键|string||
|model|模型内容|Model_1|Model_1|
|&emsp;&emsp;events||array|Event_1|
|&emsp;&emsp;&emsp;&emsp;identifier||string||
|&emsp;&emsp;&emsp;&emsp;name||string||
|&emsp;&emsp;&emsp;&emsp;outputData||array|Parameter_1|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;dataType||DataType|DataType|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;specs||object||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;type||string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;identifier||string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;name||string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;required||boolean||
|&emsp;&emsp;properties||array|Property_1|
|&emsp;&emsp;&emsp;&emsp;accessMode||string||
|&emsp;&emsp;&emsp;&emsp;dataType||DataType_1|DataType_1|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;specs||object||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;type||string||
|&emsp;&emsp;&emsp;&emsp;description||string||
|&emsp;&emsp;&emsp;&emsp;identifier||string||
|&emsp;&emsp;&emsp;&emsp;name||string||
|&emsp;&emsp;&emsp;&emsp;processor||string||
|&emsp;&emsp;&emsp;&emsp;regAddr||integer||
|&emsp;&emsp;&emsp;&emsp;regNum||integer||
|&emsp;&emsp;&emsp;&emsp;regType||string||
|&emsp;&emsp;&emsp;&emsp;sort||string||
|&emsp;&emsp;&emsp;&emsp;unit||string||
|&emsp;&emsp;services||array|Service_1|
|&emsp;&emsp;&emsp;&emsp;identifier||string||
|&emsp;&emsp;&emsp;&emsp;inputData||array|Parameter_1|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;dataType||DataType|DataType|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;specs||object||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;type||string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;identifier||string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;name||string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;required||boolean||
|&emsp;&emsp;&emsp;&emsp;name||string||
|&emsp;&emsp;&emsp;&emsp;outputData||array|Parameter_1|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;dataType||DataType|DataType|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;specs||object||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;type||string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;identifier||string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;name||string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;required||boolean||
|productKey|产品key|string||
|updateAt|更新时间|integer(int64)|integer(int64)|


**响应示例**:
```javascript
{
	"id": "",
	"model": {
		"events": [
			{
				"identifier": "",
				"name": "",
				"outputData": [
					{
						"dataType": {
							"specs": {},
							"type": ""
						},
						"identifier": "",
						"name": "",
						"required": true
					}
				]
			}
		],
		"properties": [
			{
				"accessMode": "",
				"dataType": {
					"specs": {},
					"type": ""
				},
				"description": "",
				"identifier": "",
				"name": "",
				"processor": "",
				"regAddr": 0,
				"regNum": 0,
				"regType": "",
				"sort": "",
				"unit": ""
			}
		],
		"services": [
			{
				"identifier": "",
				"inputData": [
					{}
				],
				"name": "",
				"outputData": [
					{}
				]
			}
		]
	},
	"productKey": "",
	"updateAt": 0
}
```


## 导入点位模型


**接口地址**:`/modbus/importData`


**请求方式**:`POST`


**请求数据类型**:`multipart/form-data`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|file|file|formData|true|file||
|productKey|productKey|query|true|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## ModbusInfo模版列表


**接口地址**:`/modbus/list`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:<p>设备列表</p>



**请求示例**:


```javascript
{
  "data": {
    "createBy": 0,
    "createDept": 0,
    "createTime": "",
    "id": 0,
    "name": "",
    "productKey": "",
    "remark": "",
    "updateBy": 0,
    "updateTime": ""
  },
  "pageNum": 0,
  "pageSize": 0,
  "requestId": "",
  "sortMap": {}
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|request|request|body|true|PageRequest«ModbusInfoBo»|PageRequest«ModbusInfoBo»|
|&emsp;&emsp;data|||false|ModbusInfoBo|ModbusInfoBo|
|&emsp;&emsp;&emsp;&emsp;createBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createDept|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createTime|||false|string||
|&emsp;&emsp;&emsp;&emsp;id|id||false|integer||
|&emsp;&emsp;&emsp;&emsp;name|产品名称||false|string||
|&emsp;&emsp;&emsp;&emsp;productKey|产品Key||false|string||
|&emsp;&emsp;&emsp;&emsp;remark|说明||false|string||
|&emsp;&emsp;&emsp;&emsp;updateBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;updateTime|||false|string||
|&emsp;&emsp;pageNum|||false|integer(int32)||
|&emsp;&emsp;pageSize|||false|integer(int32)||
|&emsp;&emsp;requestId|||false|string||
|&emsp;&emsp;sortMap|||false|object||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|Paging«ModbusInfoVo»|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|rows||array|ModbusInfoVo|
|&emsp;&emsp;createAt|创建时间|integer(int64)||
|&emsp;&emsp;id|id|integer(int64)||
|&emsp;&emsp;name|产品名称|string||
|&emsp;&emsp;productKey|产品Key|string||
|&emsp;&emsp;remark|说明|string||
|&emsp;&emsp;updateAt|修改时间|integer(int64)||
|total||integer(int64)|integer(int64)|


**响应示例**:
```javascript
{
	"rows": [
		{
			"createAt": 0,
			"id": 0,
			"name": "",
			"productKey": "",
			"remark": "",
			"updateAt": 0
		}
	],
	"total": 0
}
```


## 同步点位物模型到产品


**接口地址**:`/modbus/syncToProduct`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": {
    "createBy": 0,
    "createDept": 0,
    "createTime": "",
    "model": "",
    "productKey": "",
    "updateBy": 0,
    "updateTime": ""
  },
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|request|request|body|true|Request«ModbusThingModelBo»|Request«ModbusThingModelBo»|
|&emsp;&emsp;data|||false|ModbusThingModelBo|ModbusThingModelBo|
|&emsp;&emsp;&emsp;&emsp;createBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createDept|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createTime|||false|string||
|&emsp;&emsp;&emsp;&emsp;model|模型内容||false|string||
|&emsp;&emsp;&emsp;&emsp;productKey|产品key||false|string||
|&emsp;&emsp;&emsp;&emsp;updateBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;updateTime|||false|string||
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 保存点位物模型


**接口地址**:`/modbus/thingModel/save`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": {
    "createBy": 0,
    "createDept": 0,
    "createTime": "",
    "model": "",
    "productKey": "",
    "updateBy": 0,
    "updateTime": ""
  },
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|request|request|body|true|Request«ModbusThingModelBo»|Request«ModbusThingModelBo»|
|&emsp;&emsp;data|||false|ModbusThingModelBo|ModbusThingModelBo|
|&emsp;&emsp;&emsp;&emsp;createBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createDept|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createTime|||false|string||
|&emsp;&emsp;&emsp;&emsp;model|模型内容||false|string||
|&emsp;&emsp;&emsp;&emsp;productKey|产品key||false|string||
|&emsp;&emsp;&emsp;&emsp;updateBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;updateTime|||false|string||
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


暂无


**响应示例**:
```javascript

```


# openapi-基础


## token获取


**接口地址**:`/openapi/v1/getToken`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:<p>token获取</p>



**请求示例**:


```javascript
{
  "data": {
    "appid": "",
    "identifier": "",
    "tenantId": 0,
    "timestamp": ""
  },
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|request|request|body|true|Request«TokenVerifyBo»|Request«TokenVerifyBo»|
|&emsp;&emsp;data|||false|TokenVerifyBo|TokenVerifyBo|
|&emsp;&emsp;&emsp;&emsp;appid|appid||false|string||
|&emsp;&emsp;&emsp;&emsp;identifier|标识符||false|string||
|&emsp;&emsp;&emsp;&emsp;tenantId|租户ID||false|integer||
|&emsp;&emsp;&emsp;&emsp;timestamp|时间戳||false|string||
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|InvokeResult|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|requestId||string||
|time||integer(int64)|integer(int64)|


**响应示例**:
```javascript
{
	"requestId": "",
	"time": 0
}
```


# openapi-设备


## 单个设备删除


**接口地址**:`/openapi/device/v1/deleteDevice`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": {
    "deviceName": "",
    "parentId": "",
    "productKey": ""
  },
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|bo|bo|body|true|Request«OpenapiDeviceBo»|Request«OpenapiDeviceBo»|
|&emsp;&emsp;data|||false|OpenapiDeviceBo|OpenapiDeviceBo|
|&emsp;&emsp;&emsp;&emsp;deviceName|产品名称||false|string||
|&emsp;&emsp;&emsp;&emsp;parentId|父级ID||false|string||
|&emsp;&emsp;&emsp;&emsp;productKey|产品key||false|string||
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 查询单个设备详情


**接口地址**:`/openapi/device/v1/detail`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": {
    "deviceName": "",
    "parentId": "",
    "productKey": ""
  },
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|bo|bo|body|true|Request«OpenapiDeviceBo»|Request«OpenapiDeviceBo»|
|&emsp;&emsp;data|||false|OpenapiDeviceBo|OpenapiDeviceBo|
|&emsp;&emsp;&emsp;&emsp;deviceName|产品名称||false|string||
|&emsp;&emsp;&emsp;&emsp;parentId|父级ID||false|string||
|&emsp;&emsp;&emsp;&emsp;productKey|产品key||false|string||
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|DeviceInfo|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|createAt||integer(int64)|integer(int64)|
|createBy||integer(int64)|integer(int64)|
|createDept||integer(int64)|integer(int64)|
|createTime||string(date-time)|string(date-time)|
|deviceId||string||
|deviceName||string||
|group||Group|Group|
|&emsp;&emsp;id||string||
|&emsp;&emsp;name||string||
|id||string||
|locate||Locate|Locate|
|&emsp;&emsp;latitude||string||
|&emsp;&emsp;longitude||string||
|model||string||
|online||boolean||
|parentId||string||
|productKey||string||
|property||object||
|secret||string||
|state||State|State|
|&emsp;&emsp;offlineTime||integer(int64)||
|&emsp;&emsp;online||boolean||
|&emsp;&emsp;onlineTime||integer(int64)||
|subUid||array||
|tag||Tag|Tag|
|&emsp;&emsp;id||string||
|&emsp;&emsp;name||string||
|&emsp;&emsp;value||string||
|tenantId||integer(int64)|integer(int64)|
|uid||string||
|updateBy||integer(int64)|integer(int64)|
|updateTime||string(date-time)|string(date-time)|


**响应示例**:
```javascript
{
	"createAt": 0,
	"createBy": 0,
	"createDept": 0,
	"createTime": "",
	"deviceId": "",
	"deviceName": "",
	"group": {
		"additionalProperties1": {
			"id": "",
			"name": ""
		}
	},
	"id": "",
	"locate": {
		"latitude": "",
		"longitude": ""
	},
	"model": "",
	"online": true,
	"parentId": "",
	"productKey": "",
	"property": {},
	"secret": "",
	"state": {
		"offlineTime": 0,
		"online": true,
		"onlineTime": 0
	},
	"subUid": [],
	"tag": {
		"additionalProperties1": {
			"id": "",
			"name": "",
			"value": ""
		}
	},
	"tenantId": 0,
	"uid": "",
	"updateBy": 0,
	"updateTime": ""
}
```


## 查询指定设备的属性快照


**接口地址**:`/openapi/device/v1/queryDevicePropertyStatus`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": {
    "deviceName": "",
    "parentId": "",
    "productKey": ""
  },
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|bo|bo|body|true|Request«OpenapiDeviceBo»|Request«OpenapiDeviceBo»|
|&emsp;&emsp;data|||false|OpenapiDeviceBo|OpenapiDeviceBo|
|&emsp;&emsp;&emsp;&emsp;deviceName|产品名称||false|string||
|&emsp;&emsp;&emsp;&emsp;parentId|父级ID||false|string||
|&emsp;&emsp;&emsp;&emsp;productKey|产品key||false|string||
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|OpenDevicePropertyVo|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|id|主键|string||
|model|模型内容|Model|Model|
|&emsp;&emsp;events||array|Event|
|&emsp;&emsp;&emsp;&emsp;identifier||string||
|&emsp;&emsp;&emsp;&emsp;name||string||
|&emsp;&emsp;&emsp;&emsp;outputData||array|Parameter|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;dataType||DataType|DataType|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;specs||object||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;type||string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;description||string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;identifier||string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;name||string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;required||boolean||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;unit||string||
|&emsp;&emsp;properties||array|Property|
|&emsp;&emsp;&emsp;&emsp;accessMode||string||
|&emsp;&emsp;&emsp;&emsp;dataType||DataType|DataType|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;specs||object||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;type||string||
|&emsp;&emsp;&emsp;&emsp;description||string||
|&emsp;&emsp;&emsp;&emsp;icon||Icon|Icon|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;createBy||integer||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;createDept||integer||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;createTime||string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;iconContent||string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;iconName||string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;iconTypeId||integer||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;id||integer||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;tenantId||integer||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;updateBy||integer||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;updateTime||string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;version||string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;viewBox||string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;xmlns||string||
|&emsp;&emsp;&emsp;&emsp;iconId||integer||
|&emsp;&emsp;&emsp;&emsp;identifier||string||
|&emsp;&emsp;&emsp;&emsp;name||string||
|&emsp;&emsp;&emsp;&emsp;proData||string||
|&emsp;&emsp;&emsp;&emsp;unit||string||
|&emsp;&emsp;services||array|Service|
|&emsp;&emsp;&emsp;&emsp;identifier||string||
|&emsp;&emsp;&emsp;&emsp;inputData||array|Parameter|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;dataType||DataType|DataType|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;specs||object||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;type||string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;description||string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;identifier||string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;name||string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;required||boolean||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;unit||string||
|&emsp;&emsp;&emsp;&emsp;name||string||
|&emsp;&emsp;&emsp;&emsp;outputData||array|Parameter|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;dataType||DataType|DataType|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;specs||object||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;type||string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;description||string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;identifier||string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;name||string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;required||boolean||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;unit||string||
|productKey|产品key|string||
|property|设备属性|array|OpenPropertyVo|
|&emsp;&emsp;accessMode||string||
|&emsp;&emsp;dataType||DataType|DataType|
|&emsp;&emsp;&emsp;&emsp;specs||object||
|&emsp;&emsp;&emsp;&emsp;type||string||
|&emsp;&emsp;description||string||
|&emsp;&emsp;identifier||string||
|&emsp;&emsp;name||string||
|&emsp;&emsp;time||string||
|&emsp;&emsp;unit||string||
|&emsp;&emsp;value||string||


**响应示例**:
```javascript
{
	"id": "",
	"model": {
		"events": [
			{
				"identifier": "",
				"name": "",
				"outputData": [
					{
						"dataType": {
							"specs": {},
							"type": ""
						},
						"description": "",
						"identifier": "",
						"name": "",
						"required": true,
						"unit": ""
					}
				]
			}
		],
		"properties": [
			{
				"accessMode": "",
				"dataType": {
					"specs": {},
					"type": ""
				},
				"description": "",
				"icon": {
					"createBy": 0,
					"createDept": 0,
					"createTime": "",
					"iconContent": "",
					"iconName": "",
					"iconTypeId": 0,
					"id": 0,
					"tenantId": 0,
					"updateBy": 0,
					"updateTime": "",
					"version": "",
					"viewBox": "",
					"xmlns": ""
				},
				"iconId": 0,
				"identifier": "",
				"name": "",
				"proData": "",
				"unit": ""
			}
		],
		"services": [
			{
				"identifier": "",
				"inputData": [
					{}
				],
				"name": "",
				"outputData": [
					{}
				]
			}
		]
	},
	"productKey": "",
	"property": [
		{
			"accessMode": "",
			"dataType": {
				"specs": {},
				"type": ""
			},
			"description": "",
			"identifier": "",
			"name": "",
			"time": "",
			"unit": "",
			"value": ""
		}
	]
}
```


## 单个设备注册


**接口地址**:`/openapi/device/v1/registerDevice`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": {
    "deviceName": "",
    "parentId": "",
    "productKey": ""
  },
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|bo|bo|body|true|Request«OpenapiDeviceBo»|Request«OpenapiDeviceBo»|
|&emsp;&emsp;data|||false|OpenapiDeviceBo|OpenapiDeviceBo|
|&emsp;&emsp;&emsp;&emsp;deviceName|产品名称||false|string||
|&emsp;&emsp;&emsp;&emsp;parentId|父级ID||false|string||
|&emsp;&emsp;&emsp;&emsp;productKey|产品key||false|string||
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|OpenDeviceInfoVo|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|createAt||integer(int64)|integer(int64)|
|deviceId||string||
|deviceName||string||
|id||string||
|model||string||
|parentId||string||
|productKey||string||
|secret||string||
|uid||string||


**响应示例**:
```javascript
{
	"createAt": 0,
	"deviceId": "",
	"deviceName": "",
	"id": "",
	"model": "",
	"parentId": "",
	"productKey": "",
	"secret": "",
	"uid": ""
}
```


## 设置设备的属性


**接口地址**:`/openapi/device/v1/setDeviceProperty`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:<p>设置设备的属性</p>



**请求示例**:


```javascript
{
  "data": {
    "args": "",
    "deviceName": "",
    "productKey": ""
  },
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|request|request|body|true|Request«OpenapiSetDeviceServicePropertyBo»|Request«OpenapiSetDeviceServicePropertyBo»|
|&emsp;&emsp;data|||false|OpenapiSetDeviceServicePropertyBo|OpenapiSetDeviceServicePropertyBo|
|&emsp;&emsp;&emsp;&emsp;args|参数||false|string||
|&emsp;&emsp;&emsp;&emsp;deviceName|产品名称||false|string||
|&emsp;&emsp;&emsp;&emsp;productKey|产品key||false|string||
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|InvokeResult|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|requestId||string||
|time||integer(int64)|integer(int64)|


**响应示例**:
```javascript
{
	"requestId": "",
	"time": 0
}
```


# ota升级管理


## 设备升级结果查询


**接口地址**:`/ota/device/detail`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": {
    "createBy": 0,
    "createDept": 0,
    "createTime": "",
    "deviceId": "",
    "deviceName": "",
    "otaInfoId": 0,
    "productKey": "",
    "updateBy": 0,
    "updateTime": "",
    "version": ""
  },
  "pageNum": 0,
  "pageSize": 0,
  "requestId": "",
  "sortMap": {}
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|request|request|body|true|PageRequest«DeviceOtaDetailBo»|PageRequest«DeviceOtaDetailBo»|
|&emsp;&emsp;data|||false|DeviceOtaDetailBo|DeviceOtaDetailBo|
|&emsp;&emsp;&emsp;&emsp;createBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createDept|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createTime|||false|string||
|&emsp;&emsp;&emsp;&emsp;deviceId|||false|string||
|&emsp;&emsp;&emsp;&emsp;deviceName|||false|string||
|&emsp;&emsp;&emsp;&emsp;otaInfoId|||false|integer||
|&emsp;&emsp;&emsp;&emsp;productKey|||false|string||
|&emsp;&emsp;&emsp;&emsp;updateBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;updateTime|||false|string||
|&emsp;&emsp;&emsp;&emsp;version|||false|string||
|&emsp;&emsp;pageNum|||false|integer(int32)||
|&emsp;&emsp;pageSize|||false|integer(int32)||
|&emsp;&emsp;requestId|||false|string||
|&emsp;&emsp;sortMap|||false|object||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|Paging«DeviceOtaDetailVo»|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|rows||array|DeviceOtaDetailVo|
|&emsp;&emsp;desc||string||
|&emsp;&emsp;deviceId||string||
|&emsp;&emsp;deviceName||string||
|&emsp;&emsp;id||integer(int64)||
|&emsp;&emsp;module||string||
|&emsp;&emsp;otaInfoId||integer(int64)||
|&emsp;&emsp;productKey||string||
|&emsp;&emsp;step||integer(int32)||
|&emsp;&emsp;taskId||string||
|&emsp;&emsp;version||string||
|total||integer(int64)|integer(int64)|


**响应示例**:
```javascript
{
	"rows": [
		{
			"desc": "",
			"deviceId": "",
			"deviceName": "",
			"id": 0,
			"module": "",
			"otaInfoId": 0,
			"productKey": "",
			"step": 0,
			"taskId": "",
			"version": ""
		}
	],
	"total": 0
}
```


## 设备升级批次查询


**接口地址**:`/ota/device/info`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": {
    "createBy": 0,
    "createDept": 0,
    "createTime": "",
    "deviceId": "",
    "deviceName": "",
    "id": 0,
    "packageId": 0,
    "productKey": "",
    "taskId": "",
    "updateBy": 0,
    "updateTime": "",
    "version": ""
  },
  "pageNum": 0,
  "pageSize": 0,
  "requestId": "",
  "sortMap": {}
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|request|request|body|true|PageRequest«DeviceOtaInfoBo»|PageRequest«DeviceOtaInfoBo»|
|&emsp;&emsp;data|||false|DeviceOtaInfoBo|DeviceOtaInfoBo|
|&emsp;&emsp;&emsp;&emsp;createBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createDept|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createTime|||false|string||
|&emsp;&emsp;&emsp;&emsp;deviceId|||false|string||
|&emsp;&emsp;&emsp;&emsp;deviceName|||false|string||
|&emsp;&emsp;&emsp;&emsp;id|||false|integer||
|&emsp;&emsp;&emsp;&emsp;packageId|||false|integer||
|&emsp;&emsp;&emsp;&emsp;productKey|||false|string||
|&emsp;&emsp;&emsp;&emsp;taskId|||false|string||
|&emsp;&emsp;&emsp;&emsp;updateBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;updateTime|||false|string||
|&emsp;&emsp;&emsp;&emsp;version|||false|string||
|&emsp;&emsp;pageNum|||false|integer(int32)||
|&emsp;&emsp;pageSize|||false|integer(int32)||
|&emsp;&emsp;requestId|||false|string||
|&emsp;&emsp;sortMap|||false|object||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|Paging«DeviceOtaInfoVo»|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|rows||array|DeviceOtaInfoVo|
|&emsp;&emsp;createAt||integer(int64)||
|&emsp;&emsp;desc||string||
|&emsp;&emsp;fail||integer(int32)||
|&emsp;&emsp;id||integer(int64)||
|&emsp;&emsp;module||string||
|&emsp;&emsp;packageId||integer(int64)||
|&emsp;&emsp;productKey||string||
|&emsp;&emsp;success||integer(int32)||
|&emsp;&emsp;total||integer(int32)||
|&emsp;&emsp;version||string||
|total||integer(int64)|integer(int64)|


**响应示例**:
```javascript
{
	"rows": [
		{
			"createAt": 0,
			"desc": "",
			"fail": 0,
			"id": 0,
			"module": "",
			"packageId": 0,
			"productKey": "",
			"success": 0,
			"total": 0,
			"version": ""
		}
	],
	"total": 0
}
```


## OTA升级


**接口地址**:`/ota/device/upgrade`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": {
    "createBy": 0,
    "createDept": 0,
    "createTime": "",
    "deviceIds": [],
    "otaId": 0,
    "updateBy": 0,
    "updateTime": ""
  },
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|request|request|body|true|Request«DeviceUpgradeBo»|Request«DeviceUpgradeBo»|
|&emsp;&emsp;data|||false|DeviceUpgradeBo|DeviceUpgradeBo|
|&emsp;&emsp;&emsp;&emsp;createBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createDept|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createTime|||false|string||
|&emsp;&emsp;&emsp;&emsp;deviceIds|||false|array|string|
|&emsp;&emsp;&emsp;&emsp;otaId|||false|integer||
|&emsp;&emsp;&emsp;&emsp;updateBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;updateTime|||false|string||
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|DeviceUpgradeVo|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|result||string||


**响应示例**:
```javascript
{
	"result": ""
}
```


## 新增升级包


**接口地址**:`/ota/package/add`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": {
    "createBy": 0,
    "createDept": 0,
    "createTime": "",
    "desc": "",
    "extData": "",
    "isDiff": true,
    "md5": "",
    "module": "",
    "name": "",
    "productKey": "",
    "sign": "",
    "signMethod": "",
    "size": 0,
    "updateBy": 0,
    "updateTime": "",
    "url": "",
    "version": ""
  },
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|request|request|body|true|Request«OtaPackageBo»|Request«OtaPackageBo»|
|&emsp;&emsp;data|||false|OtaPackageBo|OtaPackageBo|
|&emsp;&emsp;&emsp;&emsp;createBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createDept|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createTime|||false|string||
|&emsp;&emsp;&emsp;&emsp;desc|||false|string||
|&emsp;&emsp;&emsp;&emsp;extData|||false|string||
|&emsp;&emsp;&emsp;&emsp;isDiff|||false|boolean||
|&emsp;&emsp;&emsp;&emsp;md5|||false|string||
|&emsp;&emsp;&emsp;&emsp;module|||false|string||
|&emsp;&emsp;&emsp;&emsp;name|||false|string||
|&emsp;&emsp;&emsp;&emsp;productKey|||false|string||
|&emsp;&emsp;&emsp;&emsp;sign|||false|string||
|&emsp;&emsp;&emsp;&emsp;signMethod|||false|string||
|&emsp;&emsp;&emsp;&emsp;size|||false|integer||
|&emsp;&emsp;&emsp;&emsp;updateBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;updateTime|||false|string||
|&emsp;&emsp;&emsp;&emsp;url|||false|string||
|&emsp;&emsp;&emsp;&emsp;version|||false|string||
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|OtaPackage|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|createAt||integer(int64)|integer(int64)|
|createBy||integer(int64)|integer(int64)|
|createDept||integer(int64)|integer(int64)|
|createTime||string(date-time)|string(date-time)|
|desc||string||
|extData||string||
|id||integer(int64)|integer(int64)|
|isDiff||boolean||
|md5||string||
|module||string||
|name||string||
|productKey||string||
|sign||string||
|signMethod||string||
|size||integer(int64)|integer(int64)|
|tenantId||integer(int64)|integer(int64)|
|updateBy||integer(int64)|integer(int64)|
|updateTime||string(date-time)|string(date-time)|
|url||string||
|version||string||


**响应示例**:
```javascript
{
	"createAt": 0,
	"createBy": 0,
	"createDept": 0,
	"createTime": "",
	"desc": "",
	"extData": "",
	"id": 0,
	"isDiff": true,
	"md5": "",
	"module": "",
	"name": "",
	"productKey": "",
	"sign": "",
	"signMethod": "",
	"size": 0,
	"tenantId": 0,
	"updateBy": 0,
	"updateTime": "",
	"url": "",
	"version": ""
}
```


## 删除升级包


**接口地址**:`/ota/package/delById`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": 0,
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|request|request|body|true|Request«long»|Request«long»|
|&emsp;&emsp;data|||false|integer(int64)||
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 升级包列表


**接口地址**:`/ota/package/getList`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": {
    "createAt": 0,
    "createBy": 0,
    "createDept": 0,
    "createTime": "",
    "desc": "",
    "extData": "",
    "id": 0,
    "isDiff": true,
    "md5": "",
    "module": "",
    "name": "",
    "productKey": "",
    "sign": "",
    "signMethod": "",
    "size": 0,
    "tenantId": 0,
    "updateBy": 0,
    "updateTime": "",
    "url": "",
    "version": ""
  },
  "pageNum": 0,
  "pageSize": 0,
  "requestId": "",
  "sortMap": {}
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|request|request|body|true|PageRequest«OtaPackage»|PageRequest«OtaPackage»|
|&emsp;&emsp;data|||false|OtaPackage|OtaPackage|
|&emsp;&emsp;&emsp;&emsp;createAt|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createDept|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createTime|||false|string||
|&emsp;&emsp;&emsp;&emsp;desc|||false|string||
|&emsp;&emsp;&emsp;&emsp;extData|||false|string||
|&emsp;&emsp;&emsp;&emsp;id|||false|integer||
|&emsp;&emsp;&emsp;&emsp;isDiff|||false|boolean||
|&emsp;&emsp;&emsp;&emsp;md5|||false|string||
|&emsp;&emsp;&emsp;&emsp;module|||false|string||
|&emsp;&emsp;&emsp;&emsp;name|||false|string||
|&emsp;&emsp;&emsp;&emsp;productKey|||false|string||
|&emsp;&emsp;&emsp;&emsp;sign|||false|string||
|&emsp;&emsp;&emsp;&emsp;signMethod|||false|string||
|&emsp;&emsp;&emsp;&emsp;size|||false|integer||
|&emsp;&emsp;&emsp;&emsp;tenantId|||false|integer||
|&emsp;&emsp;&emsp;&emsp;updateBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;updateTime|||false|string||
|&emsp;&emsp;&emsp;&emsp;url|||false|string||
|&emsp;&emsp;&emsp;&emsp;version|||false|string||
|&emsp;&emsp;pageNum|||false|integer(int32)||
|&emsp;&emsp;pageSize|||false|integer(int32)||
|&emsp;&emsp;requestId|||false|string||
|&emsp;&emsp;sortMap|||false|object||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|Paging«OtaPackage»|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|rows||array|OtaPackage|
|&emsp;&emsp;createAt||integer(int64)||
|&emsp;&emsp;createBy||integer(int64)||
|&emsp;&emsp;createDept||integer(int64)||
|&emsp;&emsp;createTime||string(date-time)||
|&emsp;&emsp;desc||string||
|&emsp;&emsp;extData||string||
|&emsp;&emsp;id||integer(int64)||
|&emsp;&emsp;isDiff||boolean||
|&emsp;&emsp;md5||string||
|&emsp;&emsp;module||string||
|&emsp;&emsp;name||string||
|&emsp;&emsp;productKey||string||
|&emsp;&emsp;sign||string||
|&emsp;&emsp;signMethod||string||
|&emsp;&emsp;size||integer(int64)||
|&emsp;&emsp;tenantId||integer(int64)||
|&emsp;&emsp;updateBy||integer(int64)||
|&emsp;&emsp;updateTime||string(date-time)||
|&emsp;&emsp;url||string||
|&emsp;&emsp;version||string||
|total||integer(int64)|integer(int64)|


**响应示例**:
```javascript
{
	"rows": [
		{
			"createAt": 0,
			"createBy": 0,
			"createDept": 0,
			"createTime": "",
			"desc": "",
			"extData": "",
			"id": 0,
			"isDiff": true,
			"md5": "",
			"module": "",
			"name": "",
			"productKey": "",
			"sign": "",
			"signMethod": "",
			"size": 0,
			"tenantId": 0,
			"updateBy": 0,
			"updateTime": "",
			"url": "",
			"version": ""
		}
	],
	"total": 0
}
```


## 升级包上传


**接口地址**:`/ota/package/upload`


**请求方式**:`POST`


**请求数据类型**:`multipart/form-data`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|file|file|formData|true|file||
|requestId|requestId|formData|true|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|OtaPackageUploadVo|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|md5||string||
|originalName||string||
|ossId||integer(int64)|integer(int64)|
|size||integer(int64)|integer(int64)|
|url||string||


**响应示例**:
```javascript
{
	"md5": "",
	"originalName": "",
	"ossId": 0,
	"size": 0,
	"url": ""
}
```


## ota升级测试


**接口地址**:`/ota/testStartUpgrade`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|request|request|body|true|Request«Void»|Request«Void»|
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


暂无


**响应示例**:
```javascript

```


# sys-app-controller


## 新增应用信息


**接口地址**:`/system/app/add`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": {
    "appId": "",
    "appName": "",
    "appSecret": "",
    "appType": "",
    "createBy": 0,
    "createDept": 0,
    "createTime": "",
    "id": 0,
    "remark": "",
    "updateBy": 0,
    "updateTime": ""
  },
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|request|request|body|true|Request«SysAppBo»|Request«SysAppBo»|
|&emsp;&emsp;data|||false|SysAppBo|SysAppBo|
|&emsp;&emsp;&emsp;&emsp;appId|appId||true|string||
|&emsp;&emsp;&emsp;&emsp;appName|应用名称||true|string||
|&emsp;&emsp;&emsp;&emsp;appSecret|appSecret||true|string||
|&emsp;&emsp;&emsp;&emsp;appType|应用类型||true|string||
|&emsp;&emsp;&emsp;&emsp;createBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createDept|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createTime|||false|string||
|&emsp;&emsp;&emsp;&emsp;id|id||true|integer||
|&emsp;&emsp;&emsp;&emsp;remark|备注||true|string||
|&emsp;&emsp;&emsp;&emsp;updateBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;updateTime|||false|string||
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 删除应用信息


**接口地址**:`/system/app/delete`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": 0,
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|query|query|body|true|Request«long»|Request«long»|
|&emsp;&emsp;data|||false|integer(int64)||
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 修改应用信息


**接口地址**:`/system/app/edit`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": {
    "appId": "",
    "appName": "",
    "appSecret": "",
    "appType": "",
    "createBy": 0,
    "createDept": 0,
    "createTime": "",
    "id": 0,
    "remark": "",
    "updateBy": 0,
    "updateTime": ""
  },
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|request|request|body|true|Request«SysAppBo»|Request«SysAppBo»|
|&emsp;&emsp;data|||false|SysAppBo|SysAppBo|
|&emsp;&emsp;&emsp;&emsp;appId|appId||true|string||
|&emsp;&emsp;&emsp;&emsp;appName|应用名称||true|string||
|&emsp;&emsp;&emsp;&emsp;appSecret|appSecret||true|string||
|&emsp;&emsp;&emsp;&emsp;appType|应用类型||true|string||
|&emsp;&emsp;&emsp;&emsp;createBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createDept|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createTime|||false|string||
|&emsp;&emsp;&emsp;&emsp;id|id||true|integer||
|&emsp;&emsp;&emsp;&emsp;remark|备注||true|string||
|&emsp;&emsp;&emsp;&emsp;updateBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;updateTime|||false|string||
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 导出应用信息列表


**接口地址**:`/system/app/export`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|appId|appId|query|true|string||
|appName|应用名称|query|true|string||
|appSecret|appSecret|query|true|string||
|appType|应用类型|query|true|string||
|id|id|query|true|integer(int64)||
|remark|备注|query|true|string||
|createBy||query|false|integer(int64)||
|createDept||query|false|integer(int64)||
|createTime||query|false|string(date-time)||
|updateBy||query|false|integer(int64)||
|updateTime||query|false|string(date-time)||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 获取应用信息详细信息


**接口地址**:`/system/app/getDetail`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": 0,
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|request|request|body|true|Request«long»|Request«long»|
|&emsp;&emsp;data|||false|integer(int64)||
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|SysAppVo|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|appId|appId|string||
|appName|应用名称|string||
|appSecret|appSecret|string||
|appType|应用类型|string||
|id|id|integer(int64)|integer(int64)|
|remark|备注|string||
|tenantId|租户id|integer(int64)|integer(int64)|


**响应示例**:
```javascript
{
	"appId": "",
	"appName": "",
	"appSecret": "",
	"appType": "",
	"id": 0,
	"remark": "",
	"tenantId": 0
}
```


## 查询应用信息列表


**接口地址**:`/system/app/list`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|data.appId|appId|query|true|string||
|data.appName|应用名称|query|true|string||
|data.appSecret|appSecret|query|true|string||
|data.appType|应用类型|query|true|string||
|data.id|id|query|true|integer(int64)||
|data.remark|备注|query|true|string||
|data.createBy||query|false|integer(int64)||
|data.createDept||query|false|integer(int64)||
|data.createTime||query|false|string(date-time)||
|data.updateBy||query|false|integer(int64)||
|data.updateTime||query|false|string(date-time)||
|offset||query|false|integer(int32)||
|pageNum||query|false|integer(int32)||
|pageSize||query|false|integer(int32)||
|requestId||query|false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|Paging«SysAppVo»|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|rows||array|SysAppVo|
|&emsp;&emsp;appId|appId|string||
|&emsp;&emsp;appName|应用名称|string||
|&emsp;&emsp;appSecret|appSecret|string||
|&emsp;&emsp;appType|应用类型|string||
|&emsp;&emsp;id|id|integer(int64)||
|&emsp;&emsp;remark|备注|string||
|&emsp;&emsp;tenantId|租户id|integer(int64)||
|total||integer(int64)|integer(int64)|


**响应示例**:
```javascript
{
	"rows": [
		{
			"appId": "",
			"appName": "",
			"appSecret": "",
			"appType": "",
			"id": 0,
			"remark": "",
			"tenantId": 0
		}
	],
	"total": 0
}
```


# sys-dept-controller


## 新增部门


**接口地址**:`/system/dept/add`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": {
    "createBy": 0,
    "createDept": 0,
    "createTime": "",
    "deptName": "",
    "email": "",
    "id": 0,
    "leader": "",
    "orderNum": 0,
    "parentId": 0,
    "phone": "",
    "status": "",
    "updateBy": 0,
    "updateTime": ""
  },
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|bo|bo|body|true|Request«SysDeptBo»|Request«SysDeptBo»|
|&emsp;&emsp;data|||false|SysDeptBo|SysDeptBo|
|&emsp;&emsp;&emsp;&emsp;createBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createDept|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createTime|||false|string||
|&emsp;&emsp;&emsp;&emsp;deptName|||false|string||
|&emsp;&emsp;&emsp;&emsp;email|||false|string||
|&emsp;&emsp;&emsp;&emsp;id|||false|integer||
|&emsp;&emsp;&emsp;&emsp;leader|||false|string||
|&emsp;&emsp;&emsp;&emsp;orderNum|||false|integer||
|&emsp;&emsp;&emsp;&emsp;parentId|||false|integer||
|&emsp;&emsp;&emsp;&emsp;phone|||false|string||
|&emsp;&emsp;&emsp;&emsp;status|||false|string||
|&emsp;&emsp;&emsp;&emsp;updateBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;updateTime|||false|string||
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 删除部门


**接口地址**:`/system/dept/delete`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": 0,
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|bo|bo|body|true|Request«long»|Request«long»|
|&emsp;&emsp;data|||false|integer(int64)||
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 修改部门


**接口地址**:`/system/dept/edit`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": {
    "createBy": 0,
    "createDept": 0,
    "createTime": "",
    "deptName": "",
    "email": "",
    "id": 0,
    "leader": "",
    "orderNum": 0,
    "parentId": 0,
    "phone": "",
    "status": "",
    "updateBy": 0,
    "updateTime": ""
  },
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|bo|bo|body|true|Request«SysDeptBo»|Request«SysDeptBo»|
|&emsp;&emsp;data|||false|SysDeptBo|SysDeptBo|
|&emsp;&emsp;&emsp;&emsp;createBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createDept|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createTime|||false|string||
|&emsp;&emsp;&emsp;&emsp;deptName|||false|string||
|&emsp;&emsp;&emsp;&emsp;email|||false|string||
|&emsp;&emsp;&emsp;&emsp;id|||false|integer||
|&emsp;&emsp;&emsp;&emsp;leader|||false|string||
|&emsp;&emsp;&emsp;&emsp;orderNum|||false|integer||
|&emsp;&emsp;&emsp;&emsp;parentId|||false|integer||
|&emsp;&emsp;&emsp;&emsp;phone|||false|string||
|&emsp;&emsp;&emsp;&emsp;status|||false|string||
|&emsp;&emsp;&emsp;&emsp;updateBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;updateTime|||false|string||
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 根据部门编号获取详细信息


**接口地址**:`/system/dept/getInfo`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": 0,
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|bo|bo|body|true|Request«long»|Request«long»|
|&emsp;&emsp;data|||false|integer(int64)||
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|SysDeptVo|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|ancestors||string||
|createTime||string(date-time)|string(date-time)|
|deptName||string||
|email||string||
|id||integer(int64)|integer(int64)|
|leader||string||
|orderNum||integer(int32)|integer(int32)|
|parentId||integer(int64)|integer(int64)|
|parentName||string||
|phone||string||
|status||string||


**响应示例**:
```javascript
{
	"ancestors": "",
	"createTime": "",
	"deptName": "",
	"email": "",
	"id": 0,
	"leader": "",
	"orderNum": 0,
	"parentId": 0,
	"parentName": "",
	"phone": "",
	"status": ""
}
```


## 获取部门列表


**接口地址**:`/system/dept/list`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": {
    "createBy": 0,
    "createDept": 0,
    "createTime": "",
    "deptName": "",
    "email": "",
    "id": 0,
    "leader": "",
    "orderNum": 0,
    "parentId": 0,
    "phone": "",
    "status": "",
    "updateBy": 0,
    "updateTime": ""
  },
  "pageNum": 0,
  "pageSize": 0,
  "requestId": "",
  "sortMap": {}
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|dept|dept|body|true|PageRequest«SysDeptBo»|PageRequest«SysDeptBo»|
|&emsp;&emsp;data|||false|SysDeptBo|SysDeptBo|
|&emsp;&emsp;&emsp;&emsp;createBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createDept|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createTime|||false|string||
|&emsp;&emsp;&emsp;&emsp;deptName|||false|string||
|&emsp;&emsp;&emsp;&emsp;email|||false|string||
|&emsp;&emsp;&emsp;&emsp;id|||false|integer||
|&emsp;&emsp;&emsp;&emsp;leader|||false|string||
|&emsp;&emsp;&emsp;&emsp;orderNum|||false|integer||
|&emsp;&emsp;&emsp;&emsp;parentId|||false|integer||
|&emsp;&emsp;&emsp;&emsp;phone|||false|string||
|&emsp;&emsp;&emsp;&emsp;status|||false|string||
|&emsp;&emsp;&emsp;&emsp;updateBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;updateTime|||false|string||
|&emsp;&emsp;pageNum|||false|integer(int32)||
|&emsp;&emsp;pageSize|||false|integer(int32)||
|&emsp;&emsp;requestId|||false|string||
|&emsp;&emsp;sortMap|||false|object||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|SysDeptVo|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|ancestors||string||
|createTime||string(date-time)|string(date-time)|
|deptName||string||
|email||string||
|id||integer(int64)|integer(int64)|
|leader||string||
|orderNum||integer(int32)|integer(int32)|
|parentId||integer(int64)|integer(int64)|
|parentName||string||
|phone||string||
|status||string||


**响应示例**:
```javascript
[
	{
		"ancestors": "",
		"createTime": "",
		"deptName": "",
		"email": "",
		"id": 0,
		"leader": "",
		"orderNum": 0,
		"parentId": 0,
		"parentName": "",
		"phone": "",
		"status": ""
	}
]
```


## 查询部门列表（排除节点）


**接口地址**:`/system/dept/list/exclude`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": 0,
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|request|request|body|true|Request«long»|Request«long»|
|&emsp;&emsp;data|||false|integer(int64)||
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|SysDeptVo|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|ancestors||string||
|createTime||string(date-time)|string(date-time)|
|deptName||string||
|email||string||
|id||integer(int64)|integer(int64)|
|leader||string||
|orderNum||integer(int32)|integer(int32)|
|parentId||integer(int64)|integer(int64)|
|parentName||string||
|phone||string||
|status||string||


**响应示例**:
```javascript
[
	{
		"ancestors": "",
		"createTime": "",
		"deptName": "",
		"email": "",
		"id": 0,
		"leader": "",
		"orderNum": 0,
		"parentId": 0,
		"parentName": "",
		"phone": "",
		"status": ""
	}
]
```


# sys-dict-data-controller


## 新增字典类型


**接口地址**:`/system/dict/data/add`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:<p>新增字典类型</p>



**请求示例**:


```javascript
{
  "data": {
    "createBy": 0,
    "createDept": 0,
    "createTime": "",
    "cssClass": "",
    "dictLabel": "",
    "dictSort": 0,
    "dictType": "",
    "dictValue": "",
    "id": 0,
    "isDefault": "",
    "listClass": "",
    "remark": "",
    "status": "",
    "updateBy": 0,
    "updateTime": ""
  },
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|bo|bo|body|true|Request«SysDictDataBo»|Request«SysDictDataBo»|
|&emsp;&emsp;data|||false|SysDictDataBo|SysDictDataBo|
|&emsp;&emsp;&emsp;&emsp;createBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createDept|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createTime|||false|string||
|&emsp;&emsp;&emsp;&emsp;cssClass|||false|string||
|&emsp;&emsp;&emsp;&emsp;dictLabel|||false|string||
|&emsp;&emsp;&emsp;&emsp;dictSort|||false|integer||
|&emsp;&emsp;&emsp;&emsp;dictType|||false|string||
|&emsp;&emsp;&emsp;&emsp;dictValue|||false|string||
|&emsp;&emsp;&emsp;&emsp;id|||false|integer||
|&emsp;&emsp;&emsp;&emsp;isDefault|||false|string||
|&emsp;&emsp;&emsp;&emsp;listClass|||false|string||
|&emsp;&emsp;&emsp;&emsp;remark|||false|string||
|&emsp;&emsp;&emsp;&emsp;status|||false|string||
|&emsp;&emsp;&emsp;&emsp;updateBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;updateTime|||false|string||
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 删除字典类型


**接口地址**:`/system/dict/data/delete`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:<p>删除字典类型</p>



**请求示例**:


```javascript
{
  "data": [],
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|bo|bo|body|true|Request«Array«long»»|Request«Array«long»»|
|&emsp;&emsp;data|||false|array|integer|
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 修改保存字典类型


**接口地址**:`/system/dict/data/edit`


**请求方式**:`PUT`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:<p>修改保存字典类型</p>



**请求示例**:


```javascript
{
  "data": {
    "createBy": 0,
    "createDept": 0,
    "createTime": "",
    "cssClass": "",
    "dictLabel": "",
    "dictSort": 0,
    "dictType": "",
    "dictValue": "",
    "id": 0,
    "isDefault": "",
    "listClass": "",
    "remark": "",
    "status": "",
    "updateBy": 0,
    "updateTime": ""
  },
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|bo|bo|body|true|Request«SysDictDataBo»|Request«SysDictDataBo»|
|&emsp;&emsp;data|||false|SysDictDataBo|SysDictDataBo|
|&emsp;&emsp;&emsp;&emsp;createBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createDept|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createTime|||false|string||
|&emsp;&emsp;&emsp;&emsp;cssClass|||false|string||
|&emsp;&emsp;&emsp;&emsp;dictLabel|||false|string||
|&emsp;&emsp;&emsp;&emsp;dictSort|||false|integer||
|&emsp;&emsp;&emsp;&emsp;dictType|||false|string||
|&emsp;&emsp;&emsp;&emsp;dictValue|||false|string||
|&emsp;&emsp;&emsp;&emsp;id|||false|integer||
|&emsp;&emsp;&emsp;&emsp;isDefault|||false|string||
|&emsp;&emsp;&emsp;&emsp;listClass|||false|string||
|&emsp;&emsp;&emsp;&emsp;remark|||false|string||
|&emsp;&emsp;&emsp;&emsp;status|||false|string||
|&emsp;&emsp;&emsp;&emsp;updateBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;updateTime|||false|string||
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 导出字典数据列表


**接口地址**:`/system/dict/data/export`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:<p>导出字典数据列表</p>



**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|createBy||query|false|integer(int64)||
|createDept||query|false|integer(int64)||
|createTime||query|false|string(date-time)||
|cssClass||query|false|string||
|dictLabel||query|false|string||
|dictSort||query|false|integer(int32)||
|dictType||query|false|string||
|dictValue||query|false|string||
|id||query|false|integer(int64)||
|isDefault||query|false|string||
|listClass||query|false|string||
|remark||query|false|string||
|status||query|false|string||
|updateBy||query|false|integer(int64)||
|updateTime||query|false|string(date-time)||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 查询字典数据详细


**接口地址**:`/system/dict/data/getDetail`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:<p>查询字典数据详细</p>



**请求示例**:


```javascript
{
  "data": 0,
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|bo|bo|body|true|Request«long»|Request«long»|
|&emsp;&emsp;data|||false|integer(int64)||
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|SysDictDataVo|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|createTime||string(date-time)|string(date-time)|
|cssClass||string||
|dictLabel||string||
|dictSort||integer(int32)|integer(int32)|
|dictType||string||
|dictValue||string||
|id||integer(int64)|integer(int64)|
|isDefault||string||
|listClass||string||
|remark||string||
|status||string||


**响应示例**:
```javascript
{
	"createTime": "",
	"cssClass": "",
	"dictLabel": "",
	"dictSort": 0,
	"dictType": "",
	"dictValue": "",
	"id": 0,
	"isDefault": "",
	"listClass": "",
	"remark": "",
	"status": ""
}
```


## 查询字典数据列表


**接口地址**:`/system/dict/data/list`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:<p>查询字典数据列表</p>



**请求示例**:


```javascript
{
  "data": {
    "createBy": 0,
    "createDept": 0,
    "createTime": "",
    "cssClass": "",
    "dictLabel": "",
    "dictSort": 0,
    "dictType": "",
    "dictValue": "",
    "id": 0,
    "isDefault": "",
    "listClass": "",
    "remark": "",
    "status": "",
    "updateBy": 0,
    "updateTime": ""
  },
  "pageNum": 0,
  "pageSize": 0,
  "requestId": "",
  "sortMap": {}
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|query|query|body|true|PageRequest«SysDictDataBo»|PageRequest«SysDictDataBo»|
|&emsp;&emsp;data|||false|SysDictDataBo|SysDictDataBo|
|&emsp;&emsp;&emsp;&emsp;createBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createDept|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createTime|||false|string||
|&emsp;&emsp;&emsp;&emsp;cssClass|||false|string||
|&emsp;&emsp;&emsp;&emsp;dictLabel|||false|string||
|&emsp;&emsp;&emsp;&emsp;dictSort|||false|integer||
|&emsp;&emsp;&emsp;&emsp;dictType|||false|string||
|&emsp;&emsp;&emsp;&emsp;dictValue|||false|string||
|&emsp;&emsp;&emsp;&emsp;id|||false|integer||
|&emsp;&emsp;&emsp;&emsp;isDefault|||false|string||
|&emsp;&emsp;&emsp;&emsp;listClass|||false|string||
|&emsp;&emsp;&emsp;&emsp;remark|||false|string||
|&emsp;&emsp;&emsp;&emsp;status|||false|string||
|&emsp;&emsp;&emsp;&emsp;updateBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;updateTime|||false|string||
|&emsp;&emsp;pageNum|||false|integer(int32)||
|&emsp;&emsp;pageSize|||false|integer(int32)||
|&emsp;&emsp;requestId|||false|string||
|&emsp;&emsp;sortMap|||false|object||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|Paging«SysDictDataVo»|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|rows||array|SysDictDataVo|
|&emsp;&emsp;createTime||string(date-time)||
|&emsp;&emsp;cssClass||string||
|&emsp;&emsp;dictLabel||string||
|&emsp;&emsp;dictSort||integer(int32)||
|&emsp;&emsp;dictType||string||
|&emsp;&emsp;dictValue||string||
|&emsp;&emsp;id||integer(int64)||
|&emsp;&emsp;isDefault||string||
|&emsp;&emsp;listClass||string||
|&emsp;&emsp;remark||string||
|&emsp;&emsp;status||string||
|total||integer(int64)|integer(int64)|


**响应示例**:
```javascript
{
	"rows": [
		{
			"createTime": "",
			"cssClass": "",
			"dictLabel": "",
			"dictSort": 0,
			"dictType": "",
			"dictValue": "",
			"id": 0,
			"isDefault": "",
			"listClass": "",
			"remark": "",
			"status": ""
		}
	],
	"total": 0
}
```


## 根据字典类型查询字典数据信息


**接口地址**:`/system/dict/data/type`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:<p>根据字典类型查询字典数据信息</p>



**请求示例**:


```javascript
{
  "data": "",
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|bo|bo|body|true|Request«string»|Request«string»|
|&emsp;&emsp;data|||false|string||
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|SysDictDataVo|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|createTime||string(date-time)|string(date-time)|
|cssClass||string||
|dictLabel||string||
|dictSort||integer(int32)|integer(int32)|
|dictType||string||
|dictValue||string||
|id||integer(int64)|integer(int64)|
|isDefault||string||
|listClass||string||
|remark||string||
|status||string||


**响应示例**:
```javascript
[
	{
		"createTime": "",
		"cssClass": "",
		"dictLabel": "",
		"dictSort": 0,
		"dictType": "",
		"dictValue": "",
		"id": 0,
		"isDefault": "",
		"listClass": "",
		"remark": "",
		"status": ""
	}
]
```


# sys-dict-type-controller


## 新增字典类型


**接口地址**:`/system/dict/type/add`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:<p>新增字典类型</p>



**请求示例**:


```javascript
{
  "data": {
    "createBy": 0,
    "createDept": 0,
    "createTime": "",
    "dictName": "",
    "dictType": "",
    "id": 0,
    "remark": "",
    "status": "",
    "updateBy": 0,
    "updateTime": ""
  },
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|dict|dict|body|true|Request«SysDictTypeBo»|Request«SysDictTypeBo»|
|&emsp;&emsp;data|||false|SysDictTypeBo|SysDictTypeBo|
|&emsp;&emsp;&emsp;&emsp;createBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createDept|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createTime|||false|string||
|&emsp;&emsp;&emsp;&emsp;dictName|||false|string||
|&emsp;&emsp;&emsp;&emsp;dictType|||false|string||
|&emsp;&emsp;&emsp;&emsp;id|||false|integer||
|&emsp;&emsp;&emsp;&emsp;remark|||false|string||
|&emsp;&emsp;&emsp;&emsp;status|||false|string||
|&emsp;&emsp;&emsp;&emsp;updateBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;updateTime|||false|string||
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 删除字典类型


**接口地址**:`/system/dict/type/delete`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:<p>删除字典类型</p>



**请求示例**:


```javascript
{
  "data": [],
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|dictIds|dictIds|body|true|Request«List«long»»|Request«List«long»»|
|&emsp;&emsp;data|||false|array|integer|
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 修改字典类型


**接口地址**:`/system/dict/type/edit`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:<p>修改字典类型</p>



**请求示例**:


```javascript
{
  "data": {
    "createBy": 0,
    "createDept": 0,
    "createTime": "",
    "dictName": "",
    "dictType": "",
    "id": 0,
    "remark": "",
    "status": "",
    "updateBy": 0,
    "updateTime": ""
  },
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|dict|dict|body|true|Request«SysDictTypeBo»|Request«SysDictTypeBo»|
|&emsp;&emsp;data|||false|SysDictTypeBo|SysDictTypeBo|
|&emsp;&emsp;&emsp;&emsp;createBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createDept|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createTime|||false|string||
|&emsp;&emsp;&emsp;&emsp;dictName|||false|string||
|&emsp;&emsp;&emsp;&emsp;dictType|||false|string||
|&emsp;&emsp;&emsp;&emsp;id|||false|integer||
|&emsp;&emsp;&emsp;&emsp;remark|||false|string||
|&emsp;&emsp;&emsp;&emsp;status|||false|string||
|&emsp;&emsp;&emsp;&emsp;updateBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;updateTime|||false|string||
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 导出字典类型列表


**接口地址**:`/system/dict/type/export`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:<p>导出字典类型列表</p>



**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|createBy||query|false|integer(int64)||
|createDept||query|false|integer(int64)||
|createTime||query|false|string(date-time)||
|dictName||query|false|string||
|dictType||query|false|string||
|id||query|false|integer(int64)||
|remark||query|false|string||
|status||query|false|string||
|updateBy||query|false|integer(int64)||
|updateTime||query|false|string(date-time)||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 查询字典类型详细


**接口地址**:`/system/dict/type/getById`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:<p>查询字典类型详细</p>



**请求示例**:


```javascript
{
  "data": {
    "createBy": 0,
    "createDept": 0,
    "createTime": "",
    "dictName": "",
    "dictType": "",
    "id": 0,
    "remark": "",
    "status": "",
    "updateBy": 0,
    "updateTime": ""
  },
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|bo|bo|body|true|Request«SysDictTypeBo»|Request«SysDictTypeBo»|
|&emsp;&emsp;data|||false|SysDictTypeBo|SysDictTypeBo|
|&emsp;&emsp;&emsp;&emsp;createBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createDept|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createTime|||false|string||
|&emsp;&emsp;&emsp;&emsp;dictName|||false|string||
|&emsp;&emsp;&emsp;&emsp;dictType|||false|string||
|&emsp;&emsp;&emsp;&emsp;id|||false|integer||
|&emsp;&emsp;&emsp;&emsp;remark|||false|string||
|&emsp;&emsp;&emsp;&emsp;status|||false|string||
|&emsp;&emsp;&emsp;&emsp;updateBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;updateTime|||false|string||
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|SysDictTypeVo|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|createTime||string(date-time)|string(date-time)|
|dictName||string||
|dictType||string||
|id||integer(int64)|integer(int64)|
|remark||string||
|status||string||


**响应示例**:
```javascript
{
	"createTime": "",
	"dictName": "",
	"dictType": "",
	"id": 0,
	"remark": "",
	"status": ""
}
```


## 查询字典类型列表


**接口地址**:`/system/dict/type/list`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:<p>查询字典类型列表</p>



**请求示例**:


```javascript
{
  "data": {
    "createBy": 0,
    "createDept": 0,
    "createTime": "",
    "dictName": "",
    "dictType": "",
    "id": 0,
    "remark": "",
    "status": "",
    "updateBy": 0,
    "updateTime": ""
  },
  "pageNum": 0,
  "pageSize": 0,
  "requestId": "",
  "sortMap": {}
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|query|query|body|true|PageRequest«SysDictTypeBo»|PageRequest«SysDictTypeBo»|
|&emsp;&emsp;data|||false|SysDictTypeBo|SysDictTypeBo|
|&emsp;&emsp;&emsp;&emsp;createBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createDept|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createTime|||false|string||
|&emsp;&emsp;&emsp;&emsp;dictName|||false|string||
|&emsp;&emsp;&emsp;&emsp;dictType|||false|string||
|&emsp;&emsp;&emsp;&emsp;id|||false|integer||
|&emsp;&emsp;&emsp;&emsp;remark|||false|string||
|&emsp;&emsp;&emsp;&emsp;status|||false|string||
|&emsp;&emsp;&emsp;&emsp;updateBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;updateTime|||false|string||
|&emsp;&emsp;pageNum|||false|integer(int32)||
|&emsp;&emsp;pageSize|||false|integer(int32)||
|&emsp;&emsp;requestId|||false|string||
|&emsp;&emsp;sortMap|||false|object||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|Paging«SysDictTypeVo»|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|rows||array|SysDictTypeVo|
|&emsp;&emsp;createTime||string(date-time)||
|&emsp;&emsp;dictName||string||
|&emsp;&emsp;dictType||string||
|&emsp;&emsp;id||integer(int64)||
|&emsp;&emsp;remark||string||
|&emsp;&emsp;status||string||
|total||integer(int64)|integer(int64)|


**响应示例**:
```javascript
{
	"rows": [
		{
			"createTime": "",
			"dictName": "",
			"dictType": "",
			"id": 0,
			"remark": "",
			"status": ""
		}
	],
	"total": 0
}
```


## 获取字典选择框列表


**接口地址**:`/system/dict/type/optionselect`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:<p>获取字典选择框列表</p>



**请求参数**:


暂无


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|SysDictTypeVo|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|createTime||string(date-time)|string(date-time)|
|dictName||string||
|dictType||string||
|id||integer(int64)|integer(int64)|
|remark||string||
|status||string||


**响应示例**:
```javascript
[
	{
		"createTime": "",
		"dictName": "",
		"dictType": "",
		"id": 0,
		"remark": "",
		"status": ""
	}
]
```


## 刷新字典缓存


**接口地址**:`/system/dict/type/refreshCache`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:<p>刷新字典缓存</p>



**请求参数**:


暂无


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


暂无


**响应示例**:
```javascript

```


# sys-menu-controller


## 新增菜单


**接口地址**:`/system/menu/add`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": {
    "component": "",
    "createBy": 0,
    "createDept": 0,
    "createTime": "",
    "icon": "",
    "id": 0,
    "isCache": "",
    "isFrame": "",
    "menuName": "",
    "menuType": "",
    "orderNum": 0,
    "parentId": 0,
    "path": "",
    "perms": "",
    "queryParam": "",
    "remark": "",
    "status": "",
    "updateBy": 0,
    "updateTime": "",
    "visible": ""
  },
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|bo|bo|body|true|Request«SysMenuBo»|Request«SysMenuBo»|
|&emsp;&emsp;data|||false|SysMenuBo|SysMenuBo|
|&emsp;&emsp;&emsp;&emsp;component|||false|string||
|&emsp;&emsp;&emsp;&emsp;createBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createDept|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createTime|||false|string||
|&emsp;&emsp;&emsp;&emsp;icon|||false|string||
|&emsp;&emsp;&emsp;&emsp;id|||false|integer||
|&emsp;&emsp;&emsp;&emsp;isCache|||false|string||
|&emsp;&emsp;&emsp;&emsp;isFrame|||false|string||
|&emsp;&emsp;&emsp;&emsp;menuName|||false|string||
|&emsp;&emsp;&emsp;&emsp;menuType|||false|string||
|&emsp;&emsp;&emsp;&emsp;orderNum|||false|integer||
|&emsp;&emsp;&emsp;&emsp;parentId|||false|integer||
|&emsp;&emsp;&emsp;&emsp;path|||false|string||
|&emsp;&emsp;&emsp;&emsp;perms|||false|string||
|&emsp;&emsp;&emsp;&emsp;queryParam|||false|string||
|&emsp;&emsp;&emsp;&emsp;remark|||false|string||
|&emsp;&emsp;&emsp;&emsp;status|||false|string||
|&emsp;&emsp;&emsp;&emsp;updateBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;updateTime|||false|string||
|&emsp;&emsp;&emsp;&emsp;visible|||false|string||
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 删除菜单


**接口地址**:`/system/menu/delete`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": 0,
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|bo|bo|body|true|Request«long»|Request«long»|
|&emsp;&emsp;data|||false|integer(int64)||
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 获取路由信息


**接口地址**:`/system/menu/getRouters`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


暂无


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|RouterVo|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|alwaysShow||boolean||
|children||array|RouterVo|
|&emsp;&emsp;alwaysShow||boolean||
|&emsp;&emsp;children||array|RouterVo|
|&emsp;&emsp;component||string||
|&emsp;&emsp;hidden||boolean||
|&emsp;&emsp;meta||MetaVo|MetaVo|
|&emsp;&emsp;&emsp;&emsp;icon||string||
|&emsp;&emsp;&emsp;&emsp;link||string||
|&emsp;&emsp;&emsp;&emsp;noCache||boolean||
|&emsp;&emsp;&emsp;&emsp;title||string||
|&emsp;&emsp;name||string||
|&emsp;&emsp;path||string||
|&emsp;&emsp;query||string||
|&emsp;&emsp;redirect||string||
|component||string||
|hidden||boolean||
|meta||MetaVo|MetaVo|
|&emsp;&emsp;icon||string||
|&emsp;&emsp;link||string||
|&emsp;&emsp;noCache||boolean||
|&emsp;&emsp;title||string||
|name||string||
|path||string||
|query||string||
|redirect||string||


**响应示例**:
```javascript
[
	{
		"alwaysShow": true,
		"children": [
			{
				"alwaysShow": true,
				"children": [],
				"component": "",
				"hidden": true,
				"meta": "",
				"name": "",
				"path": "",
				"query": "",
				"redirect": ""
			}
		],
		"component": "",
		"hidden": true,
		"meta": {
			"icon": "",
			"link": "",
			"noCache": true,
			"title": ""
		},
		"name": "",
		"path": "",
		"query": "",
		"redirect": ""
	}
]
```


## 获取菜单列表


**接口地址**:`/system/menu/list`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": {
    "component": "",
    "createBy": 0,
    "createDept": 0,
    "createTime": "",
    "icon": "",
    "id": 0,
    "isCache": "",
    "isFrame": "",
    "menuName": "",
    "menuType": "",
    "orderNum": 0,
    "parentId": 0,
    "path": "",
    "perms": "",
    "queryParam": "",
    "remark": "",
    "status": "",
    "updateBy": 0,
    "updateTime": "",
    "visible": ""
  },
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|bo|bo|body|true|Request«SysMenuBo»|Request«SysMenuBo»|
|&emsp;&emsp;data|||false|SysMenuBo|SysMenuBo|
|&emsp;&emsp;&emsp;&emsp;component|||false|string||
|&emsp;&emsp;&emsp;&emsp;createBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createDept|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createTime|||false|string||
|&emsp;&emsp;&emsp;&emsp;icon|||false|string||
|&emsp;&emsp;&emsp;&emsp;id|||false|integer||
|&emsp;&emsp;&emsp;&emsp;isCache|||false|string||
|&emsp;&emsp;&emsp;&emsp;isFrame|||false|string||
|&emsp;&emsp;&emsp;&emsp;menuName|||false|string||
|&emsp;&emsp;&emsp;&emsp;menuType|||false|string||
|&emsp;&emsp;&emsp;&emsp;orderNum|||false|integer||
|&emsp;&emsp;&emsp;&emsp;parentId|||false|integer||
|&emsp;&emsp;&emsp;&emsp;path|||false|string||
|&emsp;&emsp;&emsp;&emsp;perms|||false|string||
|&emsp;&emsp;&emsp;&emsp;queryParam|||false|string||
|&emsp;&emsp;&emsp;&emsp;remark|||false|string||
|&emsp;&emsp;&emsp;&emsp;status|||false|string||
|&emsp;&emsp;&emsp;&emsp;updateBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;updateTime|||false|string||
|&emsp;&emsp;&emsp;&emsp;visible|||false|string||
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|SysMenuVo|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|children||array|SysMenuVo|
|&emsp;&emsp;children||array|SysMenuVo|
|&emsp;&emsp;component||string||
|&emsp;&emsp;createDept||integer(int64)||
|&emsp;&emsp;createTime||string(date-time)||
|&emsp;&emsp;icon||string||
|&emsp;&emsp;id||integer(int64)||
|&emsp;&emsp;isCache||string||
|&emsp;&emsp;isFrame||string||
|&emsp;&emsp;menuName||string||
|&emsp;&emsp;menuType||string||
|&emsp;&emsp;orderNum||integer(int32)||
|&emsp;&emsp;parentId||integer(int64)||
|&emsp;&emsp;path||string||
|&emsp;&emsp;perms||string||
|&emsp;&emsp;queryParam||string||
|&emsp;&emsp;remark||string||
|&emsp;&emsp;status||string||
|&emsp;&emsp;visible||string||
|component||string||
|createDept||integer(int64)|integer(int64)|
|createTime||string(date-time)|string(date-time)|
|icon||string||
|id||integer(int64)|integer(int64)|
|isCache||string||
|isFrame||string||
|menuName||string||
|menuType||string||
|orderNum||integer(int32)|integer(int32)|
|parentId||integer(int64)|integer(int64)|
|path||string||
|perms||string||
|queryParam||string||
|remark||string||
|status||string||
|visible||string||


**响应示例**:
```javascript
[
	{
		"children": [
			{
				"children": [],
				"component": "",
				"createDept": 0,
				"createTime": "",
				"icon": "",
				"id": 0,
				"isCache": "",
				"isFrame": "",
				"menuName": "",
				"menuType": "",
				"orderNum": 0,
				"parentId": 0,
				"path": "",
				"perms": "",
				"queryParam": "",
				"remark": "",
				"status": "",
				"visible": ""
			}
		],
		"component": "",
		"createDept": 0,
		"createTime": "",
		"icon": "",
		"id": 0,
		"isCache": "",
		"isFrame": "",
		"menuName": "",
		"menuType": "",
		"orderNum": 0,
		"parentId": 0,
		"path": "",
		"perms": "",
		"queryParam": "",
		"remark": "",
		"status": "",
		"visible": ""
	}
]
```


## 加载对应角色菜单列表树


**接口地址**:`/system/menu/roleMenuTreeselectByRoleId`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": 0,
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|bo|bo|body|true|Request«long»|Request«long»|
|&emsp;&emsp;data|||false|integer(int64)||
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|MenuTreeSelectVo|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|checkedKeys||array||
|menus||array|Tree«long»|
|&emsp;&emsp;additionalProperty1||Tree«long»|Tree«long»|


**响应示例**:
```javascript
{
	"checkedKeys": [],
	"menus": [
		{}
	]
}
```


## 获取菜单下拉树列表


**接口地址**:`/system/menu/treeselect`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": {
    "component": "",
    "createBy": 0,
    "createDept": 0,
    "createTime": "",
    "icon": "",
    "id": 0,
    "isCache": "",
    "isFrame": "",
    "menuName": "",
    "menuType": "",
    "orderNum": 0,
    "parentId": 0,
    "path": "",
    "perms": "",
    "queryParam": "",
    "remark": "",
    "status": "",
    "updateBy": 0,
    "updateTime": "",
    "visible": ""
  },
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|menu|menu|body|true|Request«SysMenuBo»|Request«SysMenuBo»|
|&emsp;&emsp;data|||false|SysMenuBo|SysMenuBo|
|&emsp;&emsp;&emsp;&emsp;component|||false|string||
|&emsp;&emsp;&emsp;&emsp;createBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createDept|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createTime|||false|string||
|&emsp;&emsp;&emsp;&emsp;icon|||false|string||
|&emsp;&emsp;&emsp;&emsp;id|||false|integer||
|&emsp;&emsp;&emsp;&emsp;isCache|||false|string||
|&emsp;&emsp;&emsp;&emsp;isFrame|||false|string||
|&emsp;&emsp;&emsp;&emsp;menuName|||false|string||
|&emsp;&emsp;&emsp;&emsp;menuType|||false|string||
|&emsp;&emsp;&emsp;&emsp;orderNum|||false|integer||
|&emsp;&emsp;&emsp;&emsp;parentId|||false|integer||
|&emsp;&emsp;&emsp;&emsp;path|||false|string||
|&emsp;&emsp;&emsp;&emsp;perms|||false|string||
|&emsp;&emsp;&emsp;&emsp;queryParam|||false|string||
|&emsp;&emsp;&emsp;&emsp;remark|||false|string||
|&emsp;&emsp;&emsp;&emsp;status|||false|string||
|&emsp;&emsp;&emsp;&emsp;updateBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;updateTime|||false|string||
|&emsp;&emsp;&emsp;&emsp;visible|||false|string||
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|Tree«long»|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


暂无


**响应示例**:
```javascript
[
	null
]
```


# sys-notice-controller


## 新增通知公告


**接口地址**:`/system/notice/add`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:<p>新增通知公告</p>



**请求示例**:


```javascript
{
  "data": {
    "createBy": 0,
    "createByName": "",
    "createDept": 0,
    "createTime": "",
    "id": 0,
    "noticeContent": "",
    "noticeTitle": "",
    "noticeType": "",
    "remark": "",
    "status": "",
    "updateBy": 0,
    "updateTime": ""
  },
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|bo|bo|body|true|Request«SysNoticeBo»|Request«SysNoticeBo»|
|&emsp;&emsp;data|||false|SysNoticeBo|SysNoticeBo|
|&emsp;&emsp;&emsp;&emsp;createBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createByName|||false|string||
|&emsp;&emsp;&emsp;&emsp;createDept|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createTime|||false|string||
|&emsp;&emsp;&emsp;&emsp;id|||false|integer||
|&emsp;&emsp;&emsp;&emsp;noticeContent|||false|string||
|&emsp;&emsp;&emsp;&emsp;noticeTitle|||false|string||
|&emsp;&emsp;&emsp;&emsp;noticeType|||false|string||
|&emsp;&emsp;&emsp;&emsp;remark|||false|string||
|&emsp;&emsp;&emsp;&emsp;status|||false|string||
|&emsp;&emsp;&emsp;&emsp;updateBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;updateTime|||false|string||
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 删除通知公告


**接口地址**:`/system/notice/delete`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:<p>删除通知公告</p>



**请求示例**:


```javascript
{
  "data": [],
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|bo|bo|body|true|Request«List«long»»|Request«List«long»»|
|&emsp;&emsp;data|||false|array|integer|
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 根据通知公告编号获取详细信息


**接口地址**:`/system/notice/getDetail`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:<p>根据通知公告编号获取详细信息</p>



**请求示例**:


```javascript
{
  "data": 0,
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|bo|bo|body|true|Request«long»|Request«long»|
|&emsp;&emsp;data|||false|integer(int64)||
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|SysNoticeVo|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|createBy||integer(int64)|integer(int64)|
|createByName||string||
|createTime||string(date-time)|string(date-time)|
|id||integer(int64)|integer(int64)|
|noticeContent||string||
|noticeTitle||string||
|noticeType||string||
|remark||string||
|status||string||


**响应示例**:
```javascript
{
	"createBy": 0,
	"createByName": "",
	"createTime": "",
	"id": 0,
	"noticeContent": "",
	"noticeTitle": "",
	"noticeType": "",
	"remark": "",
	"status": ""
}
```


## 获取通知公告列表


**接口地址**:`/system/notice/list`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:<p>获取通知公告列表</p>



**请求示例**:


```javascript
{
  "data": {
    "createBy": 0,
    "createByName": "",
    "createDept": 0,
    "createTime": "",
    "id": 0,
    "noticeContent": "",
    "noticeTitle": "",
    "noticeType": "",
    "remark": "",
    "status": "",
    "updateBy": 0,
    "updateTime": ""
  },
  "pageNum": 0,
  "pageSize": 0,
  "requestId": "",
  "sortMap": {}
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|query|query|body|true|PageRequest«SysNoticeBo»|PageRequest«SysNoticeBo»|
|&emsp;&emsp;data|||false|SysNoticeBo|SysNoticeBo|
|&emsp;&emsp;&emsp;&emsp;createBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createByName|||false|string||
|&emsp;&emsp;&emsp;&emsp;createDept|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createTime|||false|string||
|&emsp;&emsp;&emsp;&emsp;id|||false|integer||
|&emsp;&emsp;&emsp;&emsp;noticeContent|||false|string||
|&emsp;&emsp;&emsp;&emsp;noticeTitle|||false|string||
|&emsp;&emsp;&emsp;&emsp;noticeType|||false|string||
|&emsp;&emsp;&emsp;&emsp;remark|||false|string||
|&emsp;&emsp;&emsp;&emsp;status|||false|string||
|&emsp;&emsp;&emsp;&emsp;updateBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;updateTime|||false|string||
|&emsp;&emsp;pageNum|||false|integer(int32)||
|&emsp;&emsp;pageSize|||false|integer(int32)||
|&emsp;&emsp;requestId|||false|string||
|&emsp;&emsp;sortMap|||false|object||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|Paging«SysNoticeVo»|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|rows||array|SysNoticeVo|
|&emsp;&emsp;createBy||integer(int64)||
|&emsp;&emsp;createByName||string||
|&emsp;&emsp;createTime||string(date-time)||
|&emsp;&emsp;id||integer(int64)||
|&emsp;&emsp;noticeContent||string||
|&emsp;&emsp;noticeTitle||string||
|&emsp;&emsp;noticeType||string||
|&emsp;&emsp;remark||string||
|&emsp;&emsp;status||string||
|total||integer(int64)|integer(int64)|


**响应示例**:
```javascript
{
	"rows": [
		{
			"createBy": 0,
			"createByName": "",
			"createTime": "",
			"id": 0,
			"noticeContent": "",
			"noticeTitle": "",
			"noticeType": "",
			"remark": "",
			"status": ""
		}
	],
	"total": 0
}
```


# sys-oss-config-controller


## 修改对象存储配置


**接口地址**:`/resource/oss/config`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:<p>修改对象存储配置</p>



**请求示例**:


```javascript
{
  "data": {
    "accessKey": "",
    "accessPolicy": "",
    "bucketName": "",
    "configKey": "",
    "createBy": 0,
    "createDept": 0,
    "createTime": "",
    "domain": "",
    "endpoint": "",
    "ext1": "",
    "id": 0,
    "isHttps": "",
    "prefix": "",
    "region": "",
    "remark": "",
    "secretKey": "",
    "status": "",
    "updateBy": 0,
    "updateTime": ""
  },
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|bo|bo|body|true|Request«SysOssConfigBo»|Request«SysOssConfigBo»|
|&emsp;&emsp;data|||false|SysOssConfigBo|SysOssConfigBo|
|&emsp;&emsp;&emsp;&emsp;accessKey|||false|string||
|&emsp;&emsp;&emsp;&emsp;accessPolicy|||false|string||
|&emsp;&emsp;&emsp;&emsp;bucketName|||false|string||
|&emsp;&emsp;&emsp;&emsp;configKey|||false|string||
|&emsp;&emsp;&emsp;&emsp;createBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createDept|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createTime|||false|string||
|&emsp;&emsp;&emsp;&emsp;domain|||false|string||
|&emsp;&emsp;&emsp;&emsp;endpoint|||false|string||
|&emsp;&emsp;&emsp;&emsp;ext1|||false|string||
|&emsp;&emsp;&emsp;&emsp;id|||false|integer||
|&emsp;&emsp;&emsp;&emsp;isHttps|||false|string||
|&emsp;&emsp;&emsp;&emsp;prefix|||false|string||
|&emsp;&emsp;&emsp;&emsp;region|||false|string||
|&emsp;&emsp;&emsp;&emsp;remark|||false|string||
|&emsp;&emsp;&emsp;&emsp;secretKey|||false|string||
|&emsp;&emsp;&emsp;&emsp;status|||false|string||
|&emsp;&emsp;&emsp;&emsp;updateBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;updateTime|||false|string||
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 新增对象存储配置


**接口地址**:`/resource/oss/config/add`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:<p>新增对象存储配置</p>



**请求示例**:


```javascript
{
  "data": {
    "accessKey": "",
    "accessPolicy": "",
    "bucketName": "",
    "configKey": "",
    "createBy": 0,
    "createDept": 0,
    "createTime": "",
    "domain": "",
    "endpoint": "",
    "ext1": "",
    "id": 0,
    "isHttps": "",
    "prefix": "",
    "region": "",
    "remark": "",
    "secretKey": "",
    "status": "",
    "updateBy": 0,
    "updateTime": ""
  },
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|bo|bo|body|true|Request«SysOssConfigBo»|Request«SysOssConfigBo»|
|&emsp;&emsp;data|||false|SysOssConfigBo|SysOssConfigBo|
|&emsp;&emsp;&emsp;&emsp;accessKey|||false|string||
|&emsp;&emsp;&emsp;&emsp;accessPolicy|||false|string||
|&emsp;&emsp;&emsp;&emsp;bucketName|||false|string||
|&emsp;&emsp;&emsp;&emsp;configKey|||false|string||
|&emsp;&emsp;&emsp;&emsp;createBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createDept|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createTime|||false|string||
|&emsp;&emsp;&emsp;&emsp;domain|||false|string||
|&emsp;&emsp;&emsp;&emsp;endpoint|||false|string||
|&emsp;&emsp;&emsp;&emsp;ext1|||false|string||
|&emsp;&emsp;&emsp;&emsp;id|||false|integer||
|&emsp;&emsp;&emsp;&emsp;isHttps|||false|string||
|&emsp;&emsp;&emsp;&emsp;prefix|||false|string||
|&emsp;&emsp;&emsp;&emsp;region|||false|string||
|&emsp;&emsp;&emsp;&emsp;remark|||false|string||
|&emsp;&emsp;&emsp;&emsp;secretKey|||false|string||
|&emsp;&emsp;&emsp;&emsp;status|||false|string||
|&emsp;&emsp;&emsp;&emsp;updateBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;updateTime|||false|string||
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 状态修改


**接口地址**:`/resource/oss/config/changeStatus`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:<p>状态修改</p>



**请求示例**:


```javascript
{
  "data": {
    "accessKey": "",
    "accessPolicy": "",
    "bucketName": "",
    "configKey": "",
    "createBy": 0,
    "createDept": 0,
    "createTime": "",
    "domain": "",
    "endpoint": "",
    "ext1": "",
    "id": 0,
    "isHttps": "",
    "prefix": "",
    "region": "",
    "remark": "",
    "secretKey": "",
    "status": "",
    "updateBy": 0,
    "updateTime": ""
  },
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|bo|bo|body|true|Request«SysOssConfigBo»|Request«SysOssConfigBo»|
|&emsp;&emsp;data|||false|SysOssConfigBo|SysOssConfigBo|
|&emsp;&emsp;&emsp;&emsp;accessKey|||false|string||
|&emsp;&emsp;&emsp;&emsp;accessPolicy|||false|string||
|&emsp;&emsp;&emsp;&emsp;bucketName|||false|string||
|&emsp;&emsp;&emsp;&emsp;configKey|||false|string||
|&emsp;&emsp;&emsp;&emsp;createBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createDept|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createTime|||false|string||
|&emsp;&emsp;&emsp;&emsp;domain|||false|string||
|&emsp;&emsp;&emsp;&emsp;endpoint|||false|string||
|&emsp;&emsp;&emsp;&emsp;ext1|||false|string||
|&emsp;&emsp;&emsp;&emsp;id|||false|integer||
|&emsp;&emsp;&emsp;&emsp;isHttps|||false|string||
|&emsp;&emsp;&emsp;&emsp;prefix|||false|string||
|&emsp;&emsp;&emsp;&emsp;region|||false|string||
|&emsp;&emsp;&emsp;&emsp;remark|||false|string||
|&emsp;&emsp;&emsp;&emsp;secretKey|||false|string||
|&emsp;&emsp;&emsp;&emsp;status|||false|string||
|&emsp;&emsp;&emsp;&emsp;updateBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;updateTime|||false|string||
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 删除对象存储配置


**接口地址**:`/resource/oss/config/delete`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:<p>删除对象存储配置</p>



**请求示例**:


```javascript
{
  "data": [],
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|bo|bo|body|true|Request«List«long»»|Request«List«long»»|
|&emsp;&emsp;data|||false|array|integer|
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 获取对象存储配置详细信息


**接口地址**:`/resource/oss/config/getDetail`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:<p>获取对象存储配置详细信息</p>



**请求示例**:


```javascript
{
  "data": 0,
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|bo|bo|body|true|Request«long»|Request«long»|
|&emsp;&emsp;data|||false|integer(int64)||
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|SysOssConfigVo|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|accessKey||string||
|accessPolicy||string||
|bucketName||string||
|configKey||string||
|domain||string||
|endpoint||string||
|ext1||string||
|id||integer(int64)|integer(int64)|
|isHttps||string||
|prefix||string||
|region||string||
|remark||string||
|secretKey||string||
|status||string||


**响应示例**:
```javascript
{
	"accessKey": "",
	"accessPolicy": "",
	"bucketName": "",
	"configKey": "",
	"domain": "",
	"endpoint": "",
	"ext1": "",
	"id": 0,
	"isHttps": "",
	"prefix": "",
	"region": "",
	"remark": "",
	"secretKey": "",
	"status": ""
}
```


## 查询对象存储配置列表


**接口地址**:`/resource/oss/config/list`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:<p>查询对象存储配置列表</p>



**请求示例**:


```javascript
{
  "data": {
    "accessKey": "",
    "accessPolicy": "",
    "bucketName": "",
    "configKey": "",
    "createBy": 0,
    "createDept": 0,
    "createTime": "",
    "domain": "",
    "endpoint": "",
    "ext1": "",
    "id": 0,
    "isHttps": "",
    "prefix": "",
    "region": "",
    "remark": "",
    "secretKey": "",
    "status": "",
    "updateBy": 0,
    "updateTime": ""
  },
  "pageNum": 0,
  "pageSize": 0,
  "requestId": "",
  "sortMap": {}
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|query|query|body|true|PageRequest«SysOssConfigBo»|PageRequest«SysOssConfigBo»|
|&emsp;&emsp;data|||false|SysOssConfigBo|SysOssConfigBo|
|&emsp;&emsp;&emsp;&emsp;accessKey|||false|string||
|&emsp;&emsp;&emsp;&emsp;accessPolicy|||false|string||
|&emsp;&emsp;&emsp;&emsp;bucketName|||false|string||
|&emsp;&emsp;&emsp;&emsp;configKey|||false|string||
|&emsp;&emsp;&emsp;&emsp;createBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createDept|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createTime|||false|string||
|&emsp;&emsp;&emsp;&emsp;domain|||false|string||
|&emsp;&emsp;&emsp;&emsp;endpoint|||false|string||
|&emsp;&emsp;&emsp;&emsp;ext1|||false|string||
|&emsp;&emsp;&emsp;&emsp;id|||false|integer||
|&emsp;&emsp;&emsp;&emsp;isHttps|||false|string||
|&emsp;&emsp;&emsp;&emsp;prefix|||false|string||
|&emsp;&emsp;&emsp;&emsp;region|||false|string||
|&emsp;&emsp;&emsp;&emsp;remark|||false|string||
|&emsp;&emsp;&emsp;&emsp;secretKey|||false|string||
|&emsp;&emsp;&emsp;&emsp;status|||false|string||
|&emsp;&emsp;&emsp;&emsp;updateBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;updateTime|||false|string||
|&emsp;&emsp;pageNum|||false|integer(int32)||
|&emsp;&emsp;pageSize|||false|integer(int32)||
|&emsp;&emsp;requestId|||false|string||
|&emsp;&emsp;sortMap|||false|object||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|Paging«SysOssConfigVo»|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|rows||array|SysOssConfigVo|
|&emsp;&emsp;accessKey||string||
|&emsp;&emsp;accessPolicy||string||
|&emsp;&emsp;bucketName||string||
|&emsp;&emsp;configKey||string||
|&emsp;&emsp;domain||string||
|&emsp;&emsp;endpoint||string||
|&emsp;&emsp;ext1||string||
|&emsp;&emsp;id||integer(int64)||
|&emsp;&emsp;isHttps||string||
|&emsp;&emsp;prefix||string||
|&emsp;&emsp;region||string||
|&emsp;&emsp;remark||string||
|&emsp;&emsp;secretKey||string||
|&emsp;&emsp;status||string||
|total||integer(int64)|integer(int64)|


**响应示例**:
```javascript
{
	"rows": [
		{
			"accessKey": "",
			"accessPolicy": "",
			"bucketName": "",
			"configKey": "",
			"domain": "",
			"endpoint": "",
			"ext1": "",
			"id": 0,
			"isHttps": "",
			"prefix": "",
			"region": "",
			"remark": "",
			"secretKey": "",
			"status": ""
		}
	],
	"total": 0
}
```


# sys-oss-controller


## 删除OSS对象存储


**接口地址**:`/resource/oss/delete`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:<p>删除OSS对象存储</p>



**请求示例**:


```javascript
{
  "data": [],
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|bo|bo|body|true|Request«List«long»»|Request«List«long»»|
|&emsp;&emsp;data|||false|array|integer|
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 下载OSS对象


**接口地址**:`/resource/oss/downloadById`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:<p>下载OSS对象</p>



**请求示例**:


```javascript
{
  "data": 0,
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|bo|bo|body|true|Request«long»|Request«long»|
|&emsp;&emsp;data|||false|integer(int64)||
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|StreamingResponseBody|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


暂无


**响应示例**:
```javascript
null
```


## 查询OSS对象存储列表


**接口地址**:`/resource/oss/list`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:<p>查询OSS对象存储列表</p>



**请求示例**:


```javascript
{
  "data": {
    "createBy": 0,
    "createDept": 0,
    "createTime": "",
    "fileName": "",
    "fileSuffix": "",
    "id": 0,
    "originalName": "",
    "service": "",
    "updateBy": 0,
    "updateTime": "",
    "url": ""
  },
  "pageNum": 0,
  "pageSize": 0,
  "requestId": "",
  "sortMap": {}
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|query|query|body|true|PageRequest«SysOssBo»|PageRequest«SysOssBo»|
|&emsp;&emsp;data|||false|SysOssBo|SysOssBo|
|&emsp;&emsp;&emsp;&emsp;createBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createDept|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createTime|||false|string||
|&emsp;&emsp;&emsp;&emsp;fileName|||false|string||
|&emsp;&emsp;&emsp;&emsp;fileSuffix|||false|string||
|&emsp;&emsp;&emsp;&emsp;id|||false|integer||
|&emsp;&emsp;&emsp;&emsp;originalName|||false|string||
|&emsp;&emsp;&emsp;&emsp;service|||false|string||
|&emsp;&emsp;&emsp;&emsp;updateBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;updateTime|||false|string||
|&emsp;&emsp;&emsp;&emsp;url|||false|string||
|&emsp;&emsp;pageNum|||false|integer(int32)||
|&emsp;&emsp;pageSize|||false|integer(int32)||
|&emsp;&emsp;requestId|||false|string||
|&emsp;&emsp;sortMap|||false|object||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|Paging«SysOssVo»|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|rows||array|SysOssVo|
|&emsp;&emsp;createBy||integer(int64)||
|&emsp;&emsp;createByName||string||
|&emsp;&emsp;createTime||string(date-time)||
|&emsp;&emsp;fileName||string||
|&emsp;&emsp;fileSuffix||string||
|&emsp;&emsp;id||integer(int64)||
|&emsp;&emsp;originalName||string||
|&emsp;&emsp;service||string||
|&emsp;&emsp;url||string||
|total||integer(int64)|integer(int64)|


**响应示例**:
```javascript
{
	"rows": [
		{
			"createBy": 0,
			"createByName": "",
			"createTime": "",
			"fileName": "",
			"fileSuffix": "",
			"id": 0,
			"originalName": "",
			"service": "",
			"url": ""
		}
	],
	"total": 0
}
```


## 查询OSS对象基于id串


**接口地址**:`/resource/oss/listByIds`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:<p>查询OSS对象基于id串</p>



**请求示例**:


```javascript
{
  "data": [],
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|bo|bo|body|true|Request«List«long»»|Request«List«long»»|
|&emsp;&emsp;data|||false|array|integer|
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|SysOssVo|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|createBy||integer(int64)|integer(int64)|
|createByName||string||
|createTime||string(date-time)|string(date-time)|
|fileName||string||
|fileSuffix||string||
|id||integer(int64)|integer(int64)|
|originalName||string||
|service||string||
|url||string||


**响应示例**:
```javascript
[
	{
		"createBy": 0,
		"createByName": "",
		"createTime": "",
		"fileName": "",
		"fileSuffix": "",
		"id": 0,
		"originalName": "",
		"service": "",
		"url": ""
	}
]
```


## 上传OSS对象存储


**接口地址**:`/resource/oss/upload`


**请求方式**:`POST`


**请求数据类型**:`multipart/form-data`


**响应数据类型**:`*/*`


**接口描述**:<p>上传OSS对象存储</p>



**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|file|file|formData|true|file||
|requestId|requestId|formData|true|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|SysOssUploadVo|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|fileName||string||
|ossId||string||
|url||string||


**响应示例**:
```javascript
{
	"fileName": "",
	"ossId": "",
	"url": ""
}
```


# sys-profile-controller


## 头像上传


**接口地址**:`/system/user/profile/avatar`


**请求方式**:`POST`


**请求数据类型**:`multipart/form-data`


**响应数据类型**:`*/*`


**接口描述**:<p>头像上传</p>



**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|avatarfile|avatarfile|formData|true|file||
|requestId|requestId|formData|true|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|AvatarVo|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|imgUrl||string||


**响应示例**:
```javascript
{
	"imgUrl": ""
}
```


## 个人信息


**接口地址**:`/system/user/profile/getDetail`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:<p>个人信息</p>



**请求参数**:


暂无


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|ProfileVo|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|postGroup||string||
|roleGroup||string||
|user||SysUserVo|SysUserVo|
|&emsp;&emsp;avatar||integer(int64)||
|&emsp;&emsp;createTime||string(date-time)||
|&emsp;&emsp;dept||SysDeptVo|SysDeptVo|
|&emsp;&emsp;&emsp;&emsp;ancestors||string||
|&emsp;&emsp;&emsp;&emsp;createTime||string||
|&emsp;&emsp;&emsp;&emsp;deptName||string||
|&emsp;&emsp;&emsp;&emsp;email||string||
|&emsp;&emsp;&emsp;&emsp;id||integer||
|&emsp;&emsp;&emsp;&emsp;leader||string||
|&emsp;&emsp;&emsp;&emsp;orderNum||integer||
|&emsp;&emsp;&emsp;&emsp;parentId||integer||
|&emsp;&emsp;&emsp;&emsp;parentName||string||
|&emsp;&emsp;&emsp;&emsp;phone||string||
|&emsp;&emsp;&emsp;&emsp;status||string||
|&emsp;&emsp;deptId||integer(int64)||
|&emsp;&emsp;email||string||
|&emsp;&emsp;id||integer(int64)||
|&emsp;&emsp;loginDate||string(date-time)||
|&emsp;&emsp;loginIp||string||
|&emsp;&emsp;nickName||string||
|&emsp;&emsp;password||string||
|&emsp;&emsp;phonenumber||string||
|&emsp;&emsp;postIds||array|integer|
|&emsp;&emsp;remark||string||
|&emsp;&emsp;roleId||integer(int64)||
|&emsp;&emsp;roleIds||array|integer|
|&emsp;&emsp;roles||array|SysRoleVo|
|&emsp;&emsp;&emsp;&emsp;createTime||string||
|&emsp;&emsp;&emsp;&emsp;dataScope||string||
|&emsp;&emsp;&emsp;&emsp;deptCheckStrictly||boolean||
|&emsp;&emsp;&emsp;&emsp;flag||boolean||
|&emsp;&emsp;&emsp;&emsp;id||integer||
|&emsp;&emsp;&emsp;&emsp;menuCheckStrictly||boolean||
|&emsp;&emsp;&emsp;&emsp;remark||string||
|&emsp;&emsp;&emsp;&emsp;roleKey||string||
|&emsp;&emsp;&emsp;&emsp;roleName||string||
|&emsp;&emsp;&emsp;&emsp;roleSort||integer||
|&emsp;&emsp;&emsp;&emsp;status||string||
|&emsp;&emsp;&emsp;&emsp;superAdmin||boolean||
|&emsp;&emsp;sex||string||
|&emsp;&emsp;status||string||
|&emsp;&emsp;tenantId||integer(int64)||
|&emsp;&emsp;userName||string||
|&emsp;&emsp;userType||string||


**响应示例**:
```javascript
{
	"postGroup": "",
	"roleGroup": "",
	"user": {
		"avatar": 0,
		"createTime": "",
		"dept": {
			"ancestors": "",
			"createTime": "",
			"deptName": "",
			"email": "",
			"id": 0,
			"leader": "",
			"orderNum": 0,
			"parentId": 0,
			"parentName": "",
			"phone": "",
			"status": ""
		},
		"deptId": 0,
		"email": "",
		"id": 0,
		"loginDate": "",
		"loginIp": "",
		"nickName": "",
		"password": "",
		"phonenumber": "",
		"postIds": [],
		"remark": "",
		"roleId": 0,
		"roleIds": [],
		"roles": [
			{
				"createTime": "",
				"dataScope": "",
				"deptCheckStrictly": true,
				"flag": true,
				"id": 0,
				"menuCheckStrictly": true,
				"remark": "",
				"roleKey": "",
				"roleName": "",
				"roleSort": 0,
				"status": "",
				"superAdmin": true
			}
		],
		"sex": "",
		"status": "",
		"tenantId": 0,
		"userName": "",
		"userType": ""
	}
}
```


## 修改用户


**接口地址**:`/system/user/profile/updateProfile`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:<p>修改用户</p>



**请求示例**:


```javascript
{
  "data": {
    "createBy": 0,
    "createDept": 0,
    "createTime": "",
    "email": "",
    "id": 0,
    "nickName": "",
    "phonenumber": "",
    "sex": "",
    "updateBy": 0,
    "updateTime": ""
  },
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|bo|bo|body|true|Request«SysUserProfileBo»|Request«SysUserProfileBo»|
|&emsp;&emsp;data|||false|SysUserProfileBo|SysUserProfileBo|
|&emsp;&emsp;&emsp;&emsp;createBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createDept|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createTime|||false|string||
|&emsp;&emsp;&emsp;&emsp;email|||false|string||
|&emsp;&emsp;&emsp;&emsp;id|||false|integer||
|&emsp;&emsp;&emsp;&emsp;nickName|||false|string||
|&emsp;&emsp;&emsp;&emsp;phonenumber|||false|string||
|&emsp;&emsp;&emsp;&emsp;sex|||false|string||
|&emsp;&emsp;&emsp;&emsp;updateBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;updateTime|||false|string||
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 重置密码


**接口地址**:`/system/user/profile/updatePwd`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:<p>重置密码</p>



**请求示例**:


```javascript
{
  "data": {
    "createBy": 0,
    "createDept": 0,
    "createTime": "",
    "newPassword": "",
    "oldPassword": "",
    "updateBy": 0,
    "updateTime": ""
  },
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|bo|bo|body|true|Request«SysChangePwdBo»|Request«SysChangePwdBo»|
|&emsp;&emsp;data|||false|SysChangePwdBo|SysChangePwdBo|
|&emsp;&emsp;&emsp;&emsp;createBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createDept|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createTime|||false|string||
|&emsp;&emsp;&emsp;&emsp;newPassword|新密码||false|string||
|&emsp;&emsp;&emsp;&emsp;oldPassword|旧密码||false|string||
|&emsp;&emsp;&emsp;&emsp;updateBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;updateTime|||false|string||
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


暂无


**响应示例**:
```javascript

```


# sys-role-controller


## 新增角色


**接口地址**:`/system/role/add`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:<p>新增角色</p>



**请求示例**:


```javascript
{
  "data": {
    "createBy": 0,
    "createDept": 0,
    "createTime": "",
    "dataScope": "",
    "deptCheckStrictly": true,
    "deptIds": [],
    "id": 0,
    "menuCheckStrictly": true,
    "menuIds": [],
    "remark": "",
    "roleKey": "",
    "roleName": "",
    "roleSort": 0,
    "status": "",
    "updateBy": 0,
    "updateTime": ""
  },
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|bo|bo|body|true|Request«SysRoleBo»|Request«SysRoleBo»|
|&emsp;&emsp;data|||false|SysRoleBo|SysRoleBo|
|&emsp;&emsp;&emsp;&emsp;createBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createDept|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createTime|||false|string||
|&emsp;&emsp;&emsp;&emsp;dataScope|||false|string||
|&emsp;&emsp;&emsp;&emsp;deptCheckStrictly|||false|boolean||
|&emsp;&emsp;&emsp;&emsp;deptIds|||false|array|integer|
|&emsp;&emsp;&emsp;&emsp;id|||false|integer||
|&emsp;&emsp;&emsp;&emsp;menuCheckStrictly|||false|boolean||
|&emsp;&emsp;&emsp;&emsp;menuIds|||false|array|integer|
|&emsp;&emsp;&emsp;&emsp;remark|||false|string||
|&emsp;&emsp;&emsp;&emsp;roleKey|||false|string||
|&emsp;&emsp;&emsp;&emsp;roleName|||false|string||
|&emsp;&emsp;&emsp;&emsp;roleSort|||false|integer||
|&emsp;&emsp;&emsp;&emsp;status|||false|string||
|&emsp;&emsp;&emsp;&emsp;updateBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;updateTime|||false|string||
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 查询已分配用户角色列表


**接口地址**:`/system/role/authUser/allocatedList`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:<p>查询已分配用户角色列表</p>



**请求示例**:


```javascript
{
  "data": {
    "createBy": 0,
    "createDept": 0,
    "createTime": "",
    "deptId": 0,
    "email": "",
    "id": 0,
    "nickName": "",
    "password": "",
    "phonenumber": "",
    "postIds": [],
    "remark": "",
    "roleId": 0,
    "roleIds": [],
    "sex": "",
    "status": "",
    "updateBy": 0,
    "updateTime": "",
    "userName": "",
    "userType": ""
  },
  "pageNum": 0,
  "pageSize": 0,
  "requestId": "",
  "sortMap": {}
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|query|query|body|true|PageRequest«SysUserBo»|PageRequest«SysUserBo»|
|&emsp;&emsp;data|||false|SysUserBo|SysUserBo|
|&emsp;&emsp;&emsp;&emsp;createBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createDept|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createTime|||false|string||
|&emsp;&emsp;&emsp;&emsp;deptId|||false|integer||
|&emsp;&emsp;&emsp;&emsp;email|||false|string||
|&emsp;&emsp;&emsp;&emsp;id|||false|integer||
|&emsp;&emsp;&emsp;&emsp;nickName|||false|string||
|&emsp;&emsp;&emsp;&emsp;password|||false|string||
|&emsp;&emsp;&emsp;&emsp;phonenumber|||false|string||
|&emsp;&emsp;&emsp;&emsp;postIds|||false|array|integer|
|&emsp;&emsp;&emsp;&emsp;remark|||false|string||
|&emsp;&emsp;&emsp;&emsp;roleId|||false|integer||
|&emsp;&emsp;&emsp;&emsp;roleIds|||false|array|integer|
|&emsp;&emsp;&emsp;&emsp;sex|||false|string||
|&emsp;&emsp;&emsp;&emsp;status|||false|string||
|&emsp;&emsp;&emsp;&emsp;updateBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;updateTime|||false|string||
|&emsp;&emsp;&emsp;&emsp;userName|||false|string||
|&emsp;&emsp;&emsp;&emsp;userType|||false|string||
|&emsp;&emsp;pageNum|||false|integer(int32)||
|&emsp;&emsp;pageSize|||false|integer(int32)||
|&emsp;&emsp;requestId|||false|string||
|&emsp;&emsp;sortMap|||false|object||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|Paging«SysUserVo»|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|rows||array|SysUserVo|
|&emsp;&emsp;avatar||integer(int64)||
|&emsp;&emsp;createTime||string(date-time)||
|&emsp;&emsp;dept||SysDeptVo|SysDeptVo|
|&emsp;&emsp;&emsp;&emsp;ancestors||string||
|&emsp;&emsp;&emsp;&emsp;createTime||string||
|&emsp;&emsp;&emsp;&emsp;deptName||string||
|&emsp;&emsp;&emsp;&emsp;email||string||
|&emsp;&emsp;&emsp;&emsp;id||integer||
|&emsp;&emsp;&emsp;&emsp;leader||string||
|&emsp;&emsp;&emsp;&emsp;orderNum||integer||
|&emsp;&emsp;&emsp;&emsp;parentId||integer||
|&emsp;&emsp;&emsp;&emsp;parentName||string||
|&emsp;&emsp;&emsp;&emsp;phone||string||
|&emsp;&emsp;&emsp;&emsp;status||string||
|&emsp;&emsp;deptId||integer(int64)||
|&emsp;&emsp;email||string||
|&emsp;&emsp;id||integer(int64)||
|&emsp;&emsp;loginDate||string(date-time)||
|&emsp;&emsp;loginIp||string||
|&emsp;&emsp;nickName||string||
|&emsp;&emsp;password||string||
|&emsp;&emsp;phonenumber||string||
|&emsp;&emsp;postIds||array|integer|
|&emsp;&emsp;remark||string||
|&emsp;&emsp;roleId||integer(int64)||
|&emsp;&emsp;roleIds||array|integer|
|&emsp;&emsp;roles||array|SysRoleVo|
|&emsp;&emsp;&emsp;&emsp;createTime||string||
|&emsp;&emsp;&emsp;&emsp;dataScope||string||
|&emsp;&emsp;&emsp;&emsp;deptCheckStrictly||boolean||
|&emsp;&emsp;&emsp;&emsp;flag||boolean||
|&emsp;&emsp;&emsp;&emsp;id||integer||
|&emsp;&emsp;&emsp;&emsp;menuCheckStrictly||boolean||
|&emsp;&emsp;&emsp;&emsp;remark||string||
|&emsp;&emsp;&emsp;&emsp;roleKey||string||
|&emsp;&emsp;&emsp;&emsp;roleName||string||
|&emsp;&emsp;&emsp;&emsp;roleSort||integer||
|&emsp;&emsp;&emsp;&emsp;status||string||
|&emsp;&emsp;&emsp;&emsp;superAdmin||boolean||
|&emsp;&emsp;sex||string||
|&emsp;&emsp;status||string||
|&emsp;&emsp;tenantId||integer(int64)||
|&emsp;&emsp;userName||string||
|&emsp;&emsp;userType||string||
|total||integer(int64)|integer(int64)|


**响应示例**:
```javascript
{
	"rows": [
		{
			"avatar": 0,
			"createTime": "",
			"dept": {
				"ancestors": "",
				"createTime": "",
				"deptName": "",
				"email": "",
				"id": 0,
				"leader": "",
				"orderNum": 0,
				"parentId": 0,
				"parentName": "",
				"phone": "",
				"status": ""
			},
			"deptId": 0,
			"email": "",
			"id": 0,
			"loginDate": "",
			"loginIp": "",
			"nickName": "",
			"password": "",
			"phonenumber": "",
			"postIds": [],
			"remark": "",
			"roleId": 0,
			"roleIds": [],
			"roles": [
				{
					"createTime": "",
					"dataScope": "",
					"deptCheckStrictly": true,
					"flag": true,
					"id": 0,
					"menuCheckStrictly": true,
					"remark": "",
					"roleKey": "",
					"roleName": "",
					"roleSort": 0,
					"status": "",
					"superAdmin": true
				}
			],
			"sex": "",
			"status": "",
			"tenantId": 0,
			"userName": "",
			"userType": ""
		}
	],
	"total": 0
}
```


## 取消授权用户


**接口地址**:`/system/role/authUser/cancel`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:<p>取消授权用户</p>



**请求示例**:


```javascript
{
  "data": {
    "createBy": 0,
    "createDept": 0,
    "createTime": "",
    "id": 0,
    "roleId": 0,
    "tenantId": 0,
    "updateBy": 0,
    "updateTime": "",
    "userId": 0
  },
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|bo|bo|body|true|Request«SysUserRole»|Request«SysUserRole»|
|&emsp;&emsp;data|||false|SysUserRole|SysUserRole|
|&emsp;&emsp;&emsp;&emsp;createBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createDept|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createTime|||false|string||
|&emsp;&emsp;&emsp;&emsp;id|||false|integer||
|&emsp;&emsp;&emsp;&emsp;roleId|||false|integer||
|&emsp;&emsp;&emsp;&emsp;tenantId|||false|integer||
|&emsp;&emsp;&emsp;&emsp;updateBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;updateTime|||false|string||
|&emsp;&emsp;&emsp;&emsp;userId|||false|integer||
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 批量取消授权用户


**接口地址**:`/system/role/authUser/cancelAll`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:<p>批量取消授权用户</p>



**请求示例**:


```javascript
{
  "data": {
    "createBy": 0,
    "createDept": 0,
    "createTime": "",
    "roleId": 0,
    "updateBy": 0,
    "updateTime": "",
    "userIds": []
  },
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|bo|bo|body|true|Request«SysRoleAuthBo»|Request«SysRoleAuthBo»|
|&emsp;&emsp;data|||false|SysRoleAuthBo|SysRoleAuthBo|
|&emsp;&emsp;&emsp;&emsp;createBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createDept|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createTime|||false|string||
|&emsp;&emsp;&emsp;&emsp;roleId|角色ID||false|integer||
|&emsp;&emsp;&emsp;&emsp;updateBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;updateTime|||false|string||
|&emsp;&emsp;&emsp;&emsp;userIds|用户ID列表||false|array|integer|
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 批量选择用户授权


**接口地址**:`/system/role/authUser/selectAll`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:<p>批量选择用户授权</p>



**请求示例**:


```javascript
{
  "data": {
    "createBy": 0,
    "createDept": 0,
    "createTime": "",
    "roleId": 0,
    "updateBy": 0,
    "updateTime": "",
    "userIds": []
  },
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|bo|bo|body|true|Request«SysRoleAuthBo»|Request«SysRoleAuthBo»|
|&emsp;&emsp;data|||false|SysRoleAuthBo|SysRoleAuthBo|
|&emsp;&emsp;&emsp;&emsp;createBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createDept|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createTime|||false|string||
|&emsp;&emsp;&emsp;&emsp;roleId|角色ID||false|integer||
|&emsp;&emsp;&emsp;&emsp;updateBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;updateTime|||false|string||
|&emsp;&emsp;&emsp;&emsp;userIds|用户ID列表||false|array|integer|
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 查询未分配用户角色列表


**接口地址**:`/system/role/authUser/unallocatedList`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:<p>查询未分配用户角色列表</p>



**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|data.createBy||query|false|integer(int64)||
|data.createDept||query|false|integer(int64)||
|data.createTime||query|false|string(date-time)||
|data.deptId||query|false|integer(int64)||
|data.email||query|false|string||
|data.id||query|false|integer(int64)||
|data.nickName||query|false|string||
|data.password||query|false|string||
|data.phonenumber||query|false|string||
|data.postIds||query|false|array|integer|
|data.remark||query|false|string||
|data.roleId||query|false|integer(int64)||
|data.roleIds||query|false|array|integer|
|data.sex||query|false|string||
|data.status||query|false|string||
|data.superAdmin||query|false|boolean||
|data.updateBy||query|false|integer(int64)||
|data.updateTime||query|false|string(date-time)||
|data.userName||query|false|string||
|data.userType||query|false|string||
|offset||query|false|integer(int32)||
|pageNum||query|false|integer(int32)||
|pageSize||query|false|integer(int32)||
|requestId||query|false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|Paging«SysUserVo»|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|rows||array|SysUserVo|
|&emsp;&emsp;avatar||integer(int64)||
|&emsp;&emsp;createTime||string(date-time)||
|&emsp;&emsp;dept||SysDeptVo|SysDeptVo|
|&emsp;&emsp;&emsp;&emsp;ancestors||string||
|&emsp;&emsp;&emsp;&emsp;createTime||string||
|&emsp;&emsp;&emsp;&emsp;deptName||string||
|&emsp;&emsp;&emsp;&emsp;email||string||
|&emsp;&emsp;&emsp;&emsp;id||integer||
|&emsp;&emsp;&emsp;&emsp;leader||string||
|&emsp;&emsp;&emsp;&emsp;orderNum||integer||
|&emsp;&emsp;&emsp;&emsp;parentId||integer||
|&emsp;&emsp;&emsp;&emsp;parentName||string||
|&emsp;&emsp;&emsp;&emsp;phone||string||
|&emsp;&emsp;&emsp;&emsp;status||string||
|&emsp;&emsp;deptId||integer(int64)||
|&emsp;&emsp;email||string||
|&emsp;&emsp;id||integer(int64)||
|&emsp;&emsp;loginDate||string(date-time)||
|&emsp;&emsp;loginIp||string||
|&emsp;&emsp;nickName||string||
|&emsp;&emsp;password||string||
|&emsp;&emsp;phonenumber||string||
|&emsp;&emsp;postIds||array|integer|
|&emsp;&emsp;remark||string||
|&emsp;&emsp;roleId||integer(int64)||
|&emsp;&emsp;roleIds||array|integer|
|&emsp;&emsp;roles||array|SysRoleVo|
|&emsp;&emsp;&emsp;&emsp;createTime||string||
|&emsp;&emsp;&emsp;&emsp;dataScope||string||
|&emsp;&emsp;&emsp;&emsp;deptCheckStrictly||boolean||
|&emsp;&emsp;&emsp;&emsp;flag||boolean||
|&emsp;&emsp;&emsp;&emsp;id||integer||
|&emsp;&emsp;&emsp;&emsp;menuCheckStrictly||boolean||
|&emsp;&emsp;&emsp;&emsp;remark||string||
|&emsp;&emsp;&emsp;&emsp;roleKey||string||
|&emsp;&emsp;&emsp;&emsp;roleName||string||
|&emsp;&emsp;&emsp;&emsp;roleSort||integer||
|&emsp;&emsp;&emsp;&emsp;status||string||
|&emsp;&emsp;&emsp;&emsp;superAdmin||boolean||
|&emsp;&emsp;sex||string||
|&emsp;&emsp;status||string||
|&emsp;&emsp;tenantId||integer(int64)||
|&emsp;&emsp;userName||string||
|&emsp;&emsp;userType||string||
|total||integer(int64)|integer(int64)|


**响应示例**:
```javascript
{
	"rows": [
		{
			"avatar": 0,
			"createTime": "",
			"dept": {
				"ancestors": "",
				"createTime": "",
				"deptName": "",
				"email": "",
				"id": 0,
				"leader": "",
				"orderNum": 0,
				"parentId": 0,
				"parentName": "",
				"phone": "",
				"status": ""
			},
			"deptId": 0,
			"email": "",
			"id": 0,
			"loginDate": "",
			"loginIp": "",
			"nickName": "",
			"password": "",
			"phonenumber": "",
			"postIds": [],
			"remark": "",
			"roleId": 0,
			"roleIds": [],
			"roles": [
				{
					"createTime": "",
					"dataScope": "",
					"deptCheckStrictly": true,
					"flag": true,
					"id": 0,
					"menuCheckStrictly": true,
					"remark": "",
					"roleKey": "",
					"roleName": "",
					"roleSort": 0,
					"status": "",
					"superAdmin": true
				}
			],
			"sex": "",
			"status": "",
			"tenantId": 0,
			"userName": "",
			"userType": ""
		}
	],
	"total": 0
}
```


## 状态修改


**接口地址**:`/system/role/changeStatus`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:<p>状态修改</p>



**请求示例**:


```javascript
{
  "data": {
    "createBy": 0,
    "createDept": 0,
    "createTime": "",
    "dataScope": "",
    "deptCheckStrictly": true,
    "deptIds": [],
    "id": 0,
    "menuCheckStrictly": true,
    "menuIds": [],
    "remark": "",
    "roleKey": "",
    "roleName": "",
    "roleSort": 0,
    "status": "",
    "updateBy": 0,
    "updateTime": ""
  },
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|bo|bo|body|true|Request«SysRoleBo»|Request«SysRoleBo»|
|&emsp;&emsp;data|||false|SysRoleBo|SysRoleBo|
|&emsp;&emsp;&emsp;&emsp;createBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createDept|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createTime|||false|string||
|&emsp;&emsp;&emsp;&emsp;dataScope|||false|string||
|&emsp;&emsp;&emsp;&emsp;deptCheckStrictly|||false|boolean||
|&emsp;&emsp;&emsp;&emsp;deptIds|||false|array|integer|
|&emsp;&emsp;&emsp;&emsp;id|||false|integer||
|&emsp;&emsp;&emsp;&emsp;menuCheckStrictly|||false|boolean||
|&emsp;&emsp;&emsp;&emsp;menuIds|||false|array|integer|
|&emsp;&emsp;&emsp;&emsp;remark|||false|string||
|&emsp;&emsp;&emsp;&emsp;roleKey|||false|string||
|&emsp;&emsp;&emsp;&emsp;roleName|||false|string||
|&emsp;&emsp;&emsp;&emsp;roleSort|||false|integer||
|&emsp;&emsp;&emsp;&emsp;status|||false|string||
|&emsp;&emsp;&emsp;&emsp;updateBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;updateTime|||false|string||
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 修改保存数据权限


**接口地址**:`/system/role/dataScope`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:<p>修改保存数据权限</p>



**请求示例**:


```javascript
{
  "data": {
    "createBy": 0,
    "createDept": 0,
    "createTime": "",
    "dataScope": "",
    "deptCheckStrictly": true,
    "deptIds": [],
    "id": 0,
    "menuCheckStrictly": true,
    "menuIds": [],
    "remark": "",
    "roleKey": "",
    "roleName": "",
    "roleSort": 0,
    "status": "",
    "updateBy": 0,
    "updateTime": ""
  },
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|bo|bo|body|true|Request«SysRoleBo»|Request«SysRoleBo»|
|&emsp;&emsp;data|||false|SysRoleBo|SysRoleBo|
|&emsp;&emsp;&emsp;&emsp;createBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createDept|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createTime|||false|string||
|&emsp;&emsp;&emsp;&emsp;dataScope|||false|string||
|&emsp;&emsp;&emsp;&emsp;deptCheckStrictly|||false|boolean||
|&emsp;&emsp;&emsp;&emsp;deptIds|||false|array|integer|
|&emsp;&emsp;&emsp;&emsp;id|||false|integer||
|&emsp;&emsp;&emsp;&emsp;menuCheckStrictly|||false|boolean||
|&emsp;&emsp;&emsp;&emsp;menuIds|||false|array|integer|
|&emsp;&emsp;&emsp;&emsp;remark|||false|string||
|&emsp;&emsp;&emsp;&emsp;roleKey|||false|string||
|&emsp;&emsp;&emsp;&emsp;roleName|||false|string||
|&emsp;&emsp;&emsp;&emsp;roleSort|||false|integer||
|&emsp;&emsp;&emsp;&emsp;status|||false|string||
|&emsp;&emsp;&emsp;&emsp;updateBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;updateTime|||false|string||
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 删除角色


**接口地址**:`/system/role/delete`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:<p>删除角色</p>



**请求示例**:


```javascript
{
  "data": [],
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|bo|bo|body|true|Request«List«long»»|Request«List«long»»|
|&emsp;&emsp;data|||false|array|integer|
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 获取对应角色部门树列表


**接口地址**:`/system/role/deptTreeByRoleId`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:<p>获取对应角色部门树列表</p>



**请求示例**:


```javascript
{
  "data": 0,
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|bo|bo|body|true|Request«long»|Request«long»|
|&emsp;&emsp;data|||false|integer(int64)||
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|DeptTreeSelectVo|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|checkedKeys||array||
|depts||array|Tree«long»|
|&emsp;&emsp;additionalProperty1||Tree«long»|Tree«long»|


**响应示例**:
```javascript
{
	"checkedKeys": [],
	"depts": [
		{}
	]
}
```


## 修改保存角色


**接口地址**:`/system/role/edit`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:<p>修改保存角色</p>



**请求示例**:


```javascript
{
  "data": {
    "createBy": 0,
    "createDept": 0,
    "createTime": "",
    "dataScope": "",
    "deptCheckStrictly": true,
    "deptIds": [],
    "id": 0,
    "menuCheckStrictly": true,
    "menuIds": [],
    "remark": "",
    "roleKey": "",
    "roleName": "",
    "roleSort": 0,
    "status": "",
    "updateBy": 0,
    "updateTime": ""
  },
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|bo|bo|body|true|Request«SysRoleBo»|Request«SysRoleBo»|
|&emsp;&emsp;data|||false|SysRoleBo|SysRoleBo|
|&emsp;&emsp;&emsp;&emsp;createBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createDept|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createTime|||false|string||
|&emsp;&emsp;&emsp;&emsp;dataScope|||false|string||
|&emsp;&emsp;&emsp;&emsp;deptCheckStrictly|||false|boolean||
|&emsp;&emsp;&emsp;&emsp;deptIds|||false|array|integer|
|&emsp;&emsp;&emsp;&emsp;id|||false|integer||
|&emsp;&emsp;&emsp;&emsp;menuCheckStrictly|||false|boolean||
|&emsp;&emsp;&emsp;&emsp;menuIds|||false|array|integer|
|&emsp;&emsp;&emsp;&emsp;remark|||false|string||
|&emsp;&emsp;&emsp;&emsp;roleKey|||false|string||
|&emsp;&emsp;&emsp;&emsp;roleName|||false|string||
|&emsp;&emsp;&emsp;&emsp;roleSort|||false|integer||
|&emsp;&emsp;&emsp;&emsp;status|||false|string||
|&emsp;&emsp;&emsp;&emsp;updateBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;updateTime|||false|string||
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 导出角色信息列表


**接口地址**:`/system/role/export`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:<p>导出角色信息列表</p>



**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|createBy||query|false|integer(int64)||
|createDept||query|false|integer(int64)||
|createTime||query|false|string(date-time)||
|dataScope||query|false|string||
|deptCheckStrictly||query|false|boolean||
|deptIds||query|false|array|integer|
|id||query|false|integer(int64)||
|menuCheckStrictly||query|false|boolean||
|menuIds||query|false|array|integer|
|remark||query|false|string||
|roleKey||query|false|string||
|roleName||query|false|string||
|roleSort||query|false|integer(int32)||
|status||query|false|string||
|superAdmin||query|false|boolean||
|updateBy||query|false|integer(int64)||
|updateTime||query|false|string(date-time)||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 根据角色编号获取详细信息


**接口地址**:`/system/role/getInfo`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:<p>根据角色编号获取详细信息</p>



**请求示例**:


```javascript
{
  "data": 0,
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|bo|bo|body|true|Request«long»|Request«long»|
|&emsp;&emsp;data|||false|integer(int64)||
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|SysRoleVo|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|createTime||string(date-time)|string(date-time)|
|dataScope||string||
|deptCheckStrictly||boolean||
|flag||boolean||
|id||integer(int64)|integer(int64)|
|menuCheckStrictly||boolean||
|remark||string||
|roleKey||string||
|roleName||string||
|roleSort||integer(int32)|integer(int32)|
|status||string||
|superAdmin||boolean||


**响应示例**:
```javascript
{
	"createTime": "",
	"dataScope": "",
	"deptCheckStrictly": true,
	"flag": true,
	"id": 0,
	"menuCheckStrictly": true,
	"remark": "",
	"roleKey": "",
	"roleName": "",
	"roleSort": 0,
	"status": "",
	"superAdmin": true
}
```


## 获取角色信息列表


**接口地址**:`/system/role/list`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:<p>获取角色信息列表,根据查询条件分页</p>



**请求示例**:


```javascript
{
  "data": {
    "createBy": 0,
    "createDept": 0,
    "createTime": "",
    "dataScope": "",
    "deptCheckStrictly": true,
    "deptIds": [],
    "id": 0,
    "menuCheckStrictly": true,
    "menuIds": [],
    "remark": "",
    "roleKey": "",
    "roleName": "",
    "roleSort": 0,
    "status": "",
    "updateBy": 0,
    "updateTime": ""
  },
  "pageNum": 0,
  "pageSize": 0,
  "requestId": "",
  "sortMap": {}
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|query|query|body|true|PageRequest«SysRoleBo»|PageRequest«SysRoleBo»|
|&emsp;&emsp;data|||false|SysRoleBo|SysRoleBo|
|&emsp;&emsp;&emsp;&emsp;createBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createDept|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createTime|||false|string||
|&emsp;&emsp;&emsp;&emsp;dataScope|||false|string||
|&emsp;&emsp;&emsp;&emsp;deptCheckStrictly|||false|boolean||
|&emsp;&emsp;&emsp;&emsp;deptIds|||false|array|integer|
|&emsp;&emsp;&emsp;&emsp;id|||false|integer||
|&emsp;&emsp;&emsp;&emsp;menuCheckStrictly|||false|boolean||
|&emsp;&emsp;&emsp;&emsp;menuIds|||false|array|integer|
|&emsp;&emsp;&emsp;&emsp;remark|||false|string||
|&emsp;&emsp;&emsp;&emsp;roleKey|||false|string||
|&emsp;&emsp;&emsp;&emsp;roleName|||false|string||
|&emsp;&emsp;&emsp;&emsp;roleSort|||false|integer||
|&emsp;&emsp;&emsp;&emsp;status|||false|string||
|&emsp;&emsp;&emsp;&emsp;updateBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;updateTime|||false|string||
|&emsp;&emsp;pageNum|||false|integer(int32)||
|&emsp;&emsp;pageSize|||false|integer(int32)||
|&emsp;&emsp;requestId|||false|string||
|&emsp;&emsp;sortMap|||false|object||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|Paging«SysRoleVo»|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|rows||array|SysRoleVo|
|&emsp;&emsp;createTime||string(date-time)||
|&emsp;&emsp;dataScope||string||
|&emsp;&emsp;deptCheckStrictly||boolean||
|&emsp;&emsp;flag||boolean||
|&emsp;&emsp;id||integer(int64)||
|&emsp;&emsp;menuCheckStrictly||boolean||
|&emsp;&emsp;remark||string||
|&emsp;&emsp;roleKey||string||
|&emsp;&emsp;roleName||string||
|&emsp;&emsp;roleSort||integer(int32)||
|&emsp;&emsp;status||string||
|&emsp;&emsp;superAdmin||boolean||
|total||integer(int64)|integer(int64)|


**响应示例**:
```javascript
{
	"rows": [
		{
			"createTime": "",
			"dataScope": "",
			"deptCheckStrictly": true,
			"flag": true,
			"id": 0,
			"menuCheckStrictly": true,
			"remark": "",
			"roleKey": "",
			"roleName": "",
			"roleSort": 0,
			"status": "",
			"superAdmin": true
		}
	],
	"total": 0
}
```


## 获取角色选择框列表


**接口地址**:`/system/role/optionselect`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:<p>获取角色选择框列表</p>



**请求参数**:


暂无


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|SysRoleVo|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|createTime||string(date-time)|string(date-time)|
|dataScope||string||
|deptCheckStrictly||boolean||
|flag||boolean||
|id||integer(int64)|integer(int64)|
|menuCheckStrictly||boolean||
|remark||string||
|roleKey||string||
|roleName||string||
|roleSort||integer(int32)|integer(int32)|
|status||string||
|superAdmin||boolean||


**响应示例**:
```javascript
[
	{
		"createTime": "",
		"dataScope": "",
		"deptCheckStrictly": true,
		"flag": true,
		"id": 0,
		"menuCheckStrictly": true,
		"remark": "",
		"roleKey": "",
		"roleName": "",
		"roleSort": 0,
		"status": "",
		"superAdmin": true
	}
]
```


# sys-tenant-package-controller


## 新增租户套餐


**接口地址**:`/system/tenant/package/add`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": {
    "createBy": 0,
    "createDept": 0,
    "createTime": "",
    "menuCheckStrictly": true,
    "menuIds": [],
    "packageId": 0,
    "packageName": "",
    "remark": "",
    "status": "",
    "updateBy": 0,
    "updateTime": ""
  },
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|bo|bo|body|true|Request«SysTenantPackageBo»|Request«SysTenantPackageBo»|
|&emsp;&emsp;data|||false|SysTenantPackageBo|SysTenantPackageBo|
|&emsp;&emsp;&emsp;&emsp;createBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createDept|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createTime|||false|string||
|&emsp;&emsp;&emsp;&emsp;menuCheckStrictly|||false|boolean||
|&emsp;&emsp;&emsp;&emsp;menuIds|||false|array|integer|
|&emsp;&emsp;&emsp;&emsp;packageId|||false|integer||
|&emsp;&emsp;&emsp;&emsp;packageName|||false|string||
|&emsp;&emsp;&emsp;&emsp;remark|||false|string||
|&emsp;&emsp;&emsp;&emsp;status|||false|string||
|&emsp;&emsp;&emsp;&emsp;updateBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;updateTime|||false|string||
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 状态修改


**接口地址**:`/system/tenant/package/changeStatus`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": {
    "createBy": 0,
    "createDept": 0,
    "createTime": "",
    "menuCheckStrictly": true,
    "menuIds": [],
    "packageId": 0,
    "packageName": "",
    "remark": "",
    "status": "",
    "updateBy": 0,
    "updateTime": ""
  },
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|bo|bo|body|true|Request«SysTenantPackageBo»|Request«SysTenantPackageBo»|
|&emsp;&emsp;data|||false|SysTenantPackageBo|SysTenantPackageBo|
|&emsp;&emsp;&emsp;&emsp;createBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createDept|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createTime|||false|string||
|&emsp;&emsp;&emsp;&emsp;menuCheckStrictly|||false|boolean||
|&emsp;&emsp;&emsp;&emsp;menuIds|||false|array|integer|
|&emsp;&emsp;&emsp;&emsp;packageId|||false|integer||
|&emsp;&emsp;&emsp;&emsp;packageName|||false|string||
|&emsp;&emsp;&emsp;&emsp;remark|||false|string||
|&emsp;&emsp;&emsp;&emsp;status|||false|string||
|&emsp;&emsp;&emsp;&emsp;updateBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;updateTime|||false|string||
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 删除租户套餐


**接口地址**:`/system/tenant/package/delete`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": [],
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|bo|bo|body|true|Request«List«long»»|Request«List«long»»|
|&emsp;&emsp;data|||false|array|integer|
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 修改租户套餐


**接口地址**:`/system/tenant/package/edit`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": {
    "createBy": 0,
    "createDept": 0,
    "createTime": "",
    "menuCheckStrictly": true,
    "menuIds": [],
    "packageId": 0,
    "packageName": "",
    "remark": "",
    "status": "",
    "updateBy": 0,
    "updateTime": ""
  },
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|bo|bo|body|true|Request«SysTenantPackageBo»|Request«SysTenantPackageBo»|
|&emsp;&emsp;data|||false|SysTenantPackageBo|SysTenantPackageBo|
|&emsp;&emsp;&emsp;&emsp;createBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createDept|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createTime|||false|string||
|&emsp;&emsp;&emsp;&emsp;menuCheckStrictly|||false|boolean||
|&emsp;&emsp;&emsp;&emsp;menuIds|||false|array|integer|
|&emsp;&emsp;&emsp;&emsp;packageId|||false|integer||
|&emsp;&emsp;&emsp;&emsp;packageName|||false|string||
|&emsp;&emsp;&emsp;&emsp;remark|||false|string||
|&emsp;&emsp;&emsp;&emsp;status|||false|string||
|&emsp;&emsp;&emsp;&emsp;updateBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;updateTime|||false|string||
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 导出租户套餐列表


**接口地址**:`/system/tenant/package/export`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|createBy||query|false|integer(int64)||
|createDept||query|false|integer(int64)||
|createTime||query|false|string(date-time)||
|menuCheckStrictly||query|false|boolean||
|menuIds||query|false|array|integer|
|packageId||query|false|integer(int64)||
|packageName||query|false|string||
|remark||query|false|string||
|status||query|false|string||
|updateBy||query|false|integer(int64)||
|updateTime||query|false|string(date-time)||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 获取租户套餐详细信息


**接口地址**:`/system/tenant/package/getInfo`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": 0,
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|bo|bo|body|true|Request«long»|Request«long»|
|&emsp;&emsp;data|||false|integer(int64)||
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|SysTenantPackageVo|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|id||integer(int64)|integer(int64)|
|menuCheckStrictly||boolean||
|menuIds||string||
|packageName||string||
|remark||string||
|status||string||


**响应示例**:
```javascript
{
	"id": 0,
	"menuCheckStrictly": true,
	"menuIds": "",
	"packageName": "",
	"remark": "",
	"status": ""
}
```


## 查询租户套餐列表


**接口地址**:`/system/tenant/package/list`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|data.createBy||query|false|integer(int64)||
|data.createDept||query|false|integer(int64)||
|data.createTime||query|false|string(date-time)||
|data.menuCheckStrictly||query|false|boolean||
|data.menuIds||query|false|array|integer|
|data.packageId||query|false|integer(int64)||
|data.packageName||query|false|string||
|data.remark||query|false|string||
|data.status||query|false|string||
|data.updateBy||query|false|integer(int64)||
|data.updateTime||query|false|string(date-time)||
|offset||query|false|integer(int32)||
|pageNum||query|false|integer(int32)||
|pageSize||query|false|integer(int32)||
|requestId||query|false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|Paging«SysTenantPackageVo»|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|rows||array|SysTenantPackageVo|
|&emsp;&emsp;id||integer(int64)||
|&emsp;&emsp;menuCheckStrictly||boolean||
|&emsp;&emsp;menuIds||string||
|&emsp;&emsp;packageName||string||
|&emsp;&emsp;remark||string||
|&emsp;&emsp;status||string||
|total||integer(int64)|integer(int64)|


**响应示例**:
```javascript
{
	"rows": [
		{
			"id": 0,
			"menuCheckStrictly": true,
			"menuIds": "",
			"packageName": "",
			"remark": "",
			"status": ""
		}
	],
	"total": 0
}
```


## 查询租户套餐下拉选列表


**接口地址**:`/system/tenant/package/selectList`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


暂无


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|SysTenantPackageVo|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|id||integer(int64)|integer(int64)|
|menuCheckStrictly||boolean||
|menuIds||string||
|packageName||string||
|remark||string||
|status||string||


**响应示例**:
```javascript
[
	{
		"id": 0,
		"menuCheckStrictly": true,
		"menuIds": "",
		"packageName": "",
		"remark": "",
		"status": ""
	}
]
```


# 产品


## 新建


**接口地址**:`/product/add`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": {
    "category": "",
    "createAt": 0,
    "createBy": 0,
    "createDept": 0,
    "createTime": "",
    "iconId": 0,
    "id": 0,
    "img": "",
    "isOpenLocate": true,
    "keepAliveTime": 0,
    "locateUpdateType": "",
    "name": "",
    "nodeType": 0,
    "productKey": "",
    "productSecret": "",
    "transparent": true,
    "uid": "",
    "updateBy": 0,
    "updateTime": ""
  },
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|request|request|body|true|Request«ProductBo»|Request«ProductBo»|
|&emsp;&emsp;data|||false|ProductBo|ProductBo|
|&emsp;&emsp;&emsp;&emsp;category|品类||false|string||
|&emsp;&emsp;&emsp;&emsp;createAt|创建时间||false|integer||
|&emsp;&emsp;&emsp;&emsp;createBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createDept|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createTime|||false|string||
|&emsp;&emsp;&emsp;&emsp;iconId|产品图标ID||false|integer||
|&emsp;&emsp;&emsp;&emsp;id|id||false|integer||
|&emsp;&emsp;&emsp;&emsp;img|图片||false|string||
|&emsp;&emsp;&emsp;&emsp;isOpenLocate|是否开启设备定位,true/false||false|boolean||
|&emsp;&emsp;&emsp;&emsp;keepAliveTime|保活时长||false|integer||
|&emsp;&emsp;&emsp;&emsp;locateUpdateType|定位更新方式||false|string||
|&emsp;&emsp;&emsp;&emsp;name|产品名称||false|string||
|&emsp;&emsp;&emsp;&emsp;nodeType|节点类型||false|integer||
|&emsp;&emsp;&emsp;&emsp;productKey|productKey||false|string||
|&emsp;&emsp;&emsp;&emsp;productSecret|产品密钥||false|string||
|&emsp;&emsp;&emsp;&emsp;transparent|是否透传,true/false||false|boolean||
|&emsp;&emsp;&emsp;&emsp;uid|用户ID||false|string||
|&emsp;&emsp;&emsp;&emsp;updateBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;updateTime|||false|string||
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|ProductVo|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|category|品类|string||
|createAt|创建时间|integer(int64)|integer(int64)|
|icon|产品图标信息|Icon|Icon|
|&emsp;&emsp;createBy||integer(int64)||
|&emsp;&emsp;createDept||integer(int64)||
|&emsp;&emsp;createTime||string(date-time)||
|&emsp;&emsp;iconContent||string||
|&emsp;&emsp;iconName||string||
|&emsp;&emsp;iconTypeId||integer(int64)||
|&emsp;&emsp;id||integer(int64)||
|&emsp;&emsp;tenantId||integer(int64)||
|&emsp;&emsp;updateBy||integer(int64)||
|&emsp;&emsp;updateTime||string(date-time)||
|&emsp;&emsp;version||string||
|&emsp;&emsp;viewBox||string||
|&emsp;&emsp;xmlns||string||
|iconId|产品图标ID|integer(int64)|integer(int64)|
|id|产品id|integer(int64)|integer(int64)|
|img|图片|string||
|isOpenLocate|是否开启设备定位,true/false|boolean||
|keepAliveTime|保活时长（秒）|integer(int64)|integer(int64)|
|locateUpdateType|定位更新方式|string||
|name|产品名称|string||
|nodeType|节点类型|integer(int32)|integer(int32)|
|productKey|产品id|string||
|productSecret|产品密钥|string||
|transparent|是否透传,true/false|boolean||
|uid|用户ID|string||


**响应示例**:
```javascript
{
	"category": "",
	"createAt": 0,
	"icon": {
		"createBy": 0,
		"createDept": 0,
		"createTime": "",
		"iconContent": "",
		"iconName": "",
		"iconTypeId": 0,
		"id": 0,
		"tenantId": 0,
		"updateBy": 0,
		"updateTime": "",
		"version": "",
		"viewBox": "",
		"xmlns": ""
	},
	"iconId": 0,
	"id": 0,
	"img": "",
	"isOpenLocate": true,
	"keepAliveTime": 0,
	"locateUpdateType": "",
	"name": "",
	"nodeType": 0,
	"productKey": "",
	"productSecret": "",
	"transparent": true,
	"uid": ""
}
```


## 删除品类


**接口地址**:`/product/category/delete`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": "",
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|req|req|body|true|Request«string»|Request«string»|
|&emsp;&emsp;data|||false|string||
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 品类编辑


**接口地址**:`/product/category/edit`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": {
    "createAt": 0,
    "createBy": 0,
    "createDept": 0,
    "createTime": "",
    "id": "",
    "name": "",
    "updateBy": 0,
    "updateTime": ""
  },
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|req|req|body|true|Request«CategoryBo»|Request«CategoryBo»|
|&emsp;&emsp;data|||false|CategoryBo|CategoryBo|
|&emsp;&emsp;&emsp;&emsp;createAt|分类描述||false|integer||
|&emsp;&emsp;&emsp;&emsp;createBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createDept|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createTime|||false|string||
|&emsp;&emsp;&emsp;&emsp;id|id||false|string||
|&emsp;&emsp;&emsp;&emsp;name|分类名称||false|string||
|&emsp;&emsp;&emsp;&emsp;updateBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;updateTime|||false|string||
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 产品品类展示


**接口地址**:`/product/category/getAll`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


暂无


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|CategoryVo|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|createAt|分类描述|integer(int64)|integer(int64)|
|id|分类id|string||
|name|分类名称|string||


**响应示例**:
```javascript
[
	{
		"createAt": 0,
		"id": "",
		"name": ""
	}
]
```


## 产品品类分页展示


**接口地址**:`/product/category/list`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": {
    "createAt": 0,
    "createBy": 0,
    "createDept": 0,
    "createTime": "",
    "id": "",
    "name": "",
    "updateBy": 0,
    "updateTime": ""
  },
  "pageNum": 0,
  "pageSize": 0,
  "requestId": "",
  "sortMap": {}
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|request|request|body|true|PageRequest«CategoryBo»|PageRequest«CategoryBo»|
|&emsp;&emsp;data|||false|CategoryBo|CategoryBo|
|&emsp;&emsp;&emsp;&emsp;createAt|分类描述||false|integer||
|&emsp;&emsp;&emsp;&emsp;createBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createDept|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createTime|||false|string||
|&emsp;&emsp;&emsp;&emsp;id|id||false|string||
|&emsp;&emsp;&emsp;&emsp;name|分类名称||false|string||
|&emsp;&emsp;&emsp;&emsp;updateBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;updateTime|||false|string||
|&emsp;&emsp;pageNum|||false|integer(int32)||
|&emsp;&emsp;pageSize|||false|integer(int32)||
|&emsp;&emsp;requestId|||false|string||
|&emsp;&emsp;sortMap|||false|object||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|Paging«CategoryVo»|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|rows||array|CategoryVo|
|&emsp;&emsp;createAt|分类描述|integer(int64)||
|&emsp;&emsp;id|分类id|string||
|&emsp;&emsp;name|分类名称|string||
|total||integer(int64)|integer(int64)|


**响应示例**:
```javascript
{
	"rows": [
		{
			"createAt": 0,
			"id": "",
			"name": ""
		}
	],
	"total": 0
}
```


## 删除产品


**接口地址**:`/product/deleteProduct`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": "",
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|request|request|body|true|Request«string»|Request«string»|
|&emsp;&emsp;data|||false|string||
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 编辑产品


**接口地址**:`/product/edit`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": {
    "category": "",
    "createAt": 0,
    "createBy": 0,
    "createDept": 0,
    "createTime": "",
    "iconId": 0,
    "id": 0,
    "img": "",
    "isOpenLocate": true,
    "keepAliveTime": 0,
    "locateUpdateType": "",
    "name": "",
    "nodeType": 0,
    "productKey": "",
    "productSecret": "",
    "transparent": true,
    "uid": "",
    "updateBy": 0,
    "updateTime": ""
  },
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|request|request|body|true|Request«ProductBo»|Request«ProductBo»|
|&emsp;&emsp;data|||false|ProductBo|ProductBo|
|&emsp;&emsp;&emsp;&emsp;category|品类||false|string||
|&emsp;&emsp;&emsp;&emsp;createAt|创建时间||false|integer||
|&emsp;&emsp;&emsp;&emsp;createBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createDept|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createTime|||false|string||
|&emsp;&emsp;&emsp;&emsp;iconId|产品图标ID||false|integer||
|&emsp;&emsp;&emsp;&emsp;id|id||false|integer||
|&emsp;&emsp;&emsp;&emsp;img|图片||false|string||
|&emsp;&emsp;&emsp;&emsp;isOpenLocate|是否开启设备定位,true/false||false|boolean||
|&emsp;&emsp;&emsp;&emsp;keepAliveTime|保活时长||false|integer||
|&emsp;&emsp;&emsp;&emsp;locateUpdateType|定位更新方式||false|string||
|&emsp;&emsp;&emsp;&emsp;name|产品名称||false|string||
|&emsp;&emsp;&emsp;&emsp;nodeType|节点类型||false|integer||
|&emsp;&emsp;&emsp;&emsp;productKey|productKey||false|string||
|&emsp;&emsp;&emsp;&emsp;productSecret|产品密钥||false|string||
|&emsp;&emsp;&emsp;&emsp;transparent|是否透传,true/false||false|boolean||
|&emsp;&emsp;&emsp;&emsp;uid|用户ID||false|string||
|&emsp;&emsp;&emsp;&emsp;updateBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;updateTime|||false|string||
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 查看详情


**接口地址**:`/product/getDetail`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": "",
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|request|request|body|true|Request«string»|Request«string»|
|&emsp;&emsp;data|||false|string||
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|ProductVo|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|category|品类|string||
|createAt|创建时间|integer(int64)|integer(int64)|
|icon|产品图标信息|Icon|Icon|
|&emsp;&emsp;createBy||integer(int64)||
|&emsp;&emsp;createDept||integer(int64)||
|&emsp;&emsp;createTime||string(date-time)||
|&emsp;&emsp;iconContent||string||
|&emsp;&emsp;iconName||string||
|&emsp;&emsp;iconTypeId||integer(int64)||
|&emsp;&emsp;id||integer(int64)||
|&emsp;&emsp;tenantId||integer(int64)||
|&emsp;&emsp;updateBy||integer(int64)||
|&emsp;&emsp;updateTime||string(date-time)||
|&emsp;&emsp;version||string||
|&emsp;&emsp;viewBox||string||
|&emsp;&emsp;xmlns||string||
|iconId|产品图标ID|integer(int64)|integer(int64)|
|id|产品id|integer(int64)|integer(int64)|
|img|图片|string||
|isOpenLocate|是否开启设备定位,true/false|boolean||
|keepAliveTime|保活时长（秒）|integer(int64)|integer(int64)|
|locateUpdateType|定位更新方式|string||
|name|产品名称|string||
|nodeType|节点类型|integer(int32)|integer(int32)|
|productKey|产品id|string||
|productSecret|产品密钥|string||
|transparent|是否透传,true/false|boolean||
|uid|用户ID|string||


**响应示例**:
```javascript
{
	"category": "",
	"createAt": 0,
	"icon": {
		"createBy": 0,
		"createDept": 0,
		"createTime": "",
		"iconContent": "",
		"iconName": "",
		"iconTypeId": 0,
		"id": 0,
		"tenantId": 0,
		"updateBy": 0,
		"updateTime": "",
		"version": "",
		"viewBox": "",
		"xmlns": ""
	},
	"iconId": 0,
	"id": 0,
	"img": "",
	"isOpenLocate": true,
	"keepAliveTime": 0,
	"locateUpdateType": "",
	"name": "",
	"nodeType": 0,
	"productKey": "",
	"productSecret": "",
	"transparent": true,
	"uid": ""
}
```


## 查看物模型


**接口地址**:`/product/getThingModelByProductKey`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": "",
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|request|request|body|true|Request«string»|Request«string»|
|&emsp;&emsp;data|||false|string||
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|ThingModelVo|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|id|主键|string||
|model|模型内容|Model|Model|
|&emsp;&emsp;events||array|Event|
|&emsp;&emsp;&emsp;&emsp;identifier||string||
|&emsp;&emsp;&emsp;&emsp;name||string||
|&emsp;&emsp;&emsp;&emsp;outputData||array|Parameter|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;dataType||DataType|DataType|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;specs||object||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;type||string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;description||string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;identifier||string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;name||string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;required||boolean||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;unit||string||
|&emsp;&emsp;properties||array|Property|
|&emsp;&emsp;&emsp;&emsp;accessMode||string||
|&emsp;&emsp;&emsp;&emsp;dataType||DataType|DataType|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;specs||object||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;type||string||
|&emsp;&emsp;&emsp;&emsp;description||string||
|&emsp;&emsp;&emsp;&emsp;icon||Icon|Icon|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;createBy||integer||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;createDept||integer||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;createTime||string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;iconContent||string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;iconName||string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;iconTypeId||integer||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;id||integer||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;tenantId||integer||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;updateBy||integer||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;updateTime||string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;version||string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;viewBox||string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;xmlns||string||
|&emsp;&emsp;&emsp;&emsp;iconId||integer||
|&emsp;&emsp;&emsp;&emsp;identifier||string||
|&emsp;&emsp;&emsp;&emsp;name||string||
|&emsp;&emsp;&emsp;&emsp;proData||string||
|&emsp;&emsp;&emsp;&emsp;unit||string||
|&emsp;&emsp;services||array|Service|
|&emsp;&emsp;&emsp;&emsp;identifier||string||
|&emsp;&emsp;&emsp;&emsp;inputData||array|Parameter|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;dataType||DataType|DataType|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;specs||object||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;type||string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;description||string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;identifier||string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;name||string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;required||boolean||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;unit||string||
|&emsp;&emsp;&emsp;&emsp;name||string||
|&emsp;&emsp;&emsp;&emsp;outputData||array|Parameter|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;dataType||DataType|DataType|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;specs||object||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;type||string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;description||string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;identifier||string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;name||string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;required||boolean||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;unit||string||
|productKey|产品key|string||


**响应示例**:
```javascript
{
	"id": "",
	"model": {
		"events": [
			{
				"identifier": "",
				"name": "",
				"outputData": [
					{
						"dataType": {
							"specs": {},
							"type": ""
						},
						"description": "",
						"identifier": "",
						"name": "",
						"required": true,
						"unit": ""
					}
				]
			}
		],
		"properties": [
			{
				"accessMode": "",
				"dataType": {
					"specs": {},
					"type": ""
				},
				"description": "",
				"icon": {
					"createBy": 0,
					"createDept": 0,
					"createTime": "",
					"iconContent": "",
					"iconName": "",
					"iconTypeId": 0,
					"id": 0,
					"tenantId": 0,
					"updateBy": 0,
					"updateTime": "",
					"version": "",
					"viewBox": "",
					"xmlns": ""
				},
				"iconId": 0,
				"identifier": "",
				"name": "",
				"proData": "",
				"unit": ""
			}
		],
		"services": [
			{
				"identifier": "",
				"inputData": [
					{}
				],
				"name": "",
				"outputData": [
					{}
				]
			}
		]
	},
	"productKey": ""
}
```


## 删除图标


**接口地址**:`/product/icon/deleteIcon`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": 0,
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|request|request|body|true|Request«long»|Request«long»|
|&emsp;&emsp;data|||false|integer(int64)||
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 删除图标分类


**接口地址**:`/product/icon/deleteIconType`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": 0,
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|request|request|body|true|Request«long»|Request«long»|
|&emsp;&emsp;data|||false|integer(int64)||
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 图标分页展示


**接口地址**:`/product/icon/getAllIcon`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": {
    "createBy": 0,
    "createDept": 0,
    "createTime": "",
    "iconContent": "",
    "iconName": "",
    "iconTypeId": 0,
    "id": 0,
    "updateBy": 0,
    "updateTime": "",
    "version": "",
    "viewBox": "",
    "xmlns": ""
  },
  "pageNum": 0,
  "pageSize": 0,
  "requestId": "",
  "sortMap": {}
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|request|request|body|true|PageRequest«IconBo»|PageRequest«IconBo»|
|&emsp;&emsp;data|||false|IconBo|IconBo|
|&emsp;&emsp;&emsp;&emsp;createBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createDept|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createTime|||false|string||
|&emsp;&emsp;&emsp;&emsp;iconContent|图标内容||false|string||
|&emsp;&emsp;&emsp;&emsp;iconName|图标名称||false|string||
|&emsp;&emsp;&emsp;&emsp;iconTypeId|图标分类id||false|integer||
|&emsp;&emsp;&emsp;&emsp;id|id||false|integer||
|&emsp;&emsp;&emsp;&emsp;updateBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;updateTime|||false|string||
|&emsp;&emsp;&emsp;&emsp;version|版本||false|string||
|&emsp;&emsp;&emsp;&emsp;viewBox|视窗缩放||false|string||
|&emsp;&emsp;&emsp;&emsp;xmlns|命名空间||false|string||
|&emsp;&emsp;pageNum|||false|integer(int32)||
|&emsp;&emsp;pageSize|||false|integer(int32)||
|&emsp;&emsp;requestId|||false|string||
|&emsp;&emsp;sortMap|||false|object||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|Paging«IconVo»|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|rows||array|IconVo|
|&emsp;&emsp;iconContent|图标内容|string||
|&emsp;&emsp;iconName|图标名称|string||
|&emsp;&emsp;iconTypeId|图标分类id|integer(int64)||
|&emsp;&emsp;id|id|integer(int64)||
|&emsp;&emsp;version|版本|string||
|&emsp;&emsp;viewBox|视窗缩放|string||
|&emsp;&emsp;xmlns|命名空间|string||
|total||integer(int64)|integer(int64)|


**响应示例**:
```javascript
{
	"rows": [
		{
			"iconContent": "",
			"iconName": "",
			"iconTypeId": 0,
			"id": 0,
			"version": "",
			"viewBox": "",
			"xmlns": ""
		}
	],
	"total": 0
}
```


## 图标分类列表


**接口地址**:`/product/icon/getAllIconType`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


暂无


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|IconTypeVo|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|id|id|integer(int64)|integer(int64)|
|typeDescribe|分类描述|string||
|typeName|分类名称|string||


**响应示例**:
```javascript
[
	{
		"id": 0,
		"typeDescribe": "",
		"typeName": ""
	}
]
```


## 保存图标


**接口地址**:`/product/icon/saveIcon`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": {
    "createBy": 0,
    "createDept": 0,
    "createTime": "",
    "iconContent": "",
    "iconName": "",
    "iconTypeId": 0,
    "id": 0,
    "updateBy": 0,
    "updateTime": "",
    "version": "",
    "viewBox": "",
    "xmlns": ""
  },
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|request|request|body|true|Request«IconBo»|Request«IconBo»|
|&emsp;&emsp;data|||false|IconBo|IconBo|
|&emsp;&emsp;&emsp;&emsp;createBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createDept|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createTime|||false|string||
|&emsp;&emsp;&emsp;&emsp;iconContent|图标内容||false|string||
|&emsp;&emsp;&emsp;&emsp;iconName|图标名称||false|string||
|&emsp;&emsp;&emsp;&emsp;iconTypeId|图标分类id||false|integer||
|&emsp;&emsp;&emsp;&emsp;id|id||false|integer||
|&emsp;&emsp;&emsp;&emsp;updateBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;updateTime|||false|string||
|&emsp;&emsp;&emsp;&emsp;version|版本||false|string||
|&emsp;&emsp;&emsp;&emsp;viewBox|视窗缩放||false|string||
|&emsp;&emsp;&emsp;&emsp;xmlns|命名空间||false|string||
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 保存图标分类


**接口地址**:`/product/icon/saveIconType`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": {
    "createBy": 0,
    "createDept": 0,
    "createTime": "",
    "id": 0,
    "typeDescribe": "",
    "typeName": "",
    "updateBy": 0,
    "updateTime": ""
  },
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|request|request|body|true|Request«IconTypeBo»|Request«IconTypeBo»|
|&emsp;&emsp;data|||false|IconTypeBo|IconTypeBo|
|&emsp;&emsp;&emsp;&emsp;createBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createDept|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createTime|||false|string||
|&emsp;&emsp;&emsp;&emsp;id|id||false|integer||
|&emsp;&emsp;&emsp;&emsp;typeDescribe|分类描述||false|string||
|&emsp;&emsp;&emsp;&emsp;typeName|分类名称||false|string||
|&emsp;&emsp;&emsp;&emsp;updateBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;updateTime|||false|string||
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 列表


**接口地址**:`/product/list`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": {
    "category": "",
    "createAt": 0,
    "createBy": 0,
    "createDept": 0,
    "createTime": "",
    "iconId": 0,
    "id": 0,
    "img": "",
    "isOpenLocate": true,
    "keepAliveTime": 0,
    "locateUpdateType": "",
    "name": "",
    "nodeType": 0,
    "productKey": "",
    "productSecret": "",
    "transparent": true,
    "uid": "",
    "updateBy": 0,
    "updateTime": ""
  },
  "pageNum": 0,
  "pageSize": 0,
  "requestId": "",
  "sortMap": {}
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|request|request|body|true|PageRequest«ProductBo»|PageRequest«ProductBo»|
|&emsp;&emsp;data|||false|ProductBo|ProductBo|
|&emsp;&emsp;&emsp;&emsp;category|品类||false|string||
|&emsp;&emsp;&emsp;&emsp;createAt|创建时间||false|integer||
|&emsp;&emsp;&emsp;&emsp;createBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createDept|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createTime|||false|string||
|&emsp;&emsp;&emsp;&emsp;iconId|产品图标ID||false|integer||
|&emsp;&emsp;&emsp;&emsp;id|id||false|integer||
|&emsp;&emsp;&emsp;&emsp;img|图片||false|string||
|&emsp;&emsp;&emsp;&emsp;isOpenLocate|是否开启设备定位,true/false||false|boolean||
|&emsp;&emsp;&emsp;&emsp;keepAliveTime|保活时长||false|integer||
|&emsp;&emsp;&emsp;&emsp;locateUpdateType|定位更新方式||false|string||
|&emsp;&emsp;&emsp;&emsp;name|产品名称||false|string||
|&emsp;&emsp;&emsp;&emsp;nodeType|节点类型||false|integer||
|&emsp;&emsp;&emsp;&emsp;productKey|productKey||false|string||
|&emsp;&emsp;&emsp;&emsp;productSecret|产品密钥||false|string||
|&emsp;&emsp;&emsp;&emsp;transparent|是否透传,true/false||false|boolean||
|&emsp;&emsp;&emsp;&emsp;uid|用户ID||false|string||
|&emsp;&emsp;&emsp;&emsp;updateBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;updateTime|||false|string||
|&emsp;&emsp;pageNum|||false|integer(int32)||
|&emsp;&emsp;pageSize|||false|integer(int32)||
|&emsp;&emsp;requestId|||false|string||
|&emsp;&emsp;sortMap|||false|object||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|Paging«ProductVo»|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|rows||array|ProductVo|
|&emsp;&emsp;category|品类|string||
|&emsp;&emsp;createAt|创建时间|integer(int64)||
|&emsp;&emsp;icon|产品图标信息|Icon|Icon|
|&emsp;&emsp;&emsp;&emsp;createBy||integer||
|&emsp;&emsp;&emsp;&emsp;createDept||integer||
|&emsp;&emsp;&emsp;&emsp;createTime||string||
|&emsp;&emsp;&emsp;&emsp;iconContent||string||
|&emsp;&emsp;&emsp;&emsp;iconName||string||
|&emsp;&emsp;&emsp;&emsp;iconTypeId||integer||
|&emsp;&emsp;&emsp;&emsp;id||integer||
|&emsp;&emsp;&emsp;&emsp;tenantId||integer||
|&emsp;&emsp;&emsp;&emsp;updateBy||integer||
|&emsp;&emsp;&emsp;&emsp;updateTime||string||
|&emsp;&emsp;&emsp;&emsp;version||string||
|&emsp;&emsp;&emsp;&emsp;viewBox||string||
|&emsp;&emsp;&emsp;&emsp;xmlns||string||
|&emsp;&emsp;iconId|产品图标ID|integer(int64)||
|&emsp;&emsp;id|产品id|integer(int64)||
|&emsp;&emsp;img|图片|string||
|&emsp;&emsp;isOpenLocate|是否开启设备定位,true/false|boolean||
|&emsp;&emsp;keepAliveTime|保活时长（秒）|integer(int64)||
|&emsp;&emsp;locateUpdateType|定位更新方式|string||
|&emsp;&emsp;name|产品名称|string||
|&emsp;&emsp;nodeType|节点类型|integer(int32)||
|&emsp;&emsp;productKey|产品id|string||
|&emsp;&emsp;productSecret|产品密钥|string||
|&emsp;&emsp;transparent|是否透传,true/false|boolean||
|&emsp;&emsp;uid|用户ID|string||
|total||integer(int64)|integer(int64)|


**响应示例**:
```javascript
{
	"rows": [
		{
			"category": "",
			"createAt": 0,
			"icon": {
				"createBy": 0,
				"createDept": 0,
				"createTime": "",
				"iconContent": "",
				"iconName": "",
				"iconTypeId": 0,
				"id": 0,
				"tenantId": 0,
				"updateBy": 0,
				"updateTime": "",
				"version": "",
				"viewBox": "",
				"xmlns": ""
			},
			"iconId": 0,
			"id": 0,
			"img": "",
			"isOpenLocate": true,
			"keepAliveTime": 0,
			"locateUpdateType": "",
			"name": "",
			"nodeType": 0,
			"productKey": "",
			"productSecret": "",
			"transparent": true,
			"uid": ""
		}
	],
	"total": 0
}
```


## 删除产品型号


**接口地址**:`/product/productModel/delete`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": "",
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|id|id|body|true|Request«string»|Request«string»|
|&emsp;&emsp;data|||false|string||
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 编辑产品型号


**接口地址**:`/product/productModel/edit`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": {
    "createBy": 0,
    "createDept": 0,
    "createTime": "",
    "id": "",
    "model": "",
    "modifyAt": 0,
    "name": "",
    "productKey": "",
    "script": "",
    "state": "",
    "type": "",
    "updateBy": 0,
    "updateTime": ""
  },
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|bo|bo|body|true|Request«ProductModelBo»|Request«ProductModelBo»|
|&emsp;&emsp;data|||false|ProductModelBo|ProductModelBo|
|&emsp;&emsp;&emsp;&emsp;createBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createDept|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createTime|||false|string||
|&emsp;&emsp;&emsp;&emsp;id|id||false|string||
|&emsp;&emsp;&emsp;&emsp;model|型号||false|string||
|&emsp;&emsp;&emsp;&emsp;modifyAt|修改时间||false|integer||
|&emsp;&emsp;&emsp;&emsp;name|名称||false|string||
|&emsp;&emsp;&emsp;&emsp;productKey|产品Key||false|string||
|&emsp;&emsp;&emsp;&emsp;script|脚本内容||false|string||
|&emsp;&emsp;&emsp;&emsp;state|脚本状态||false|string||
|&emsp;&emsp;&emsp;&emsp;type|脚本类型||false|string||
|&emsp;&emsp;&emsp;&emsp;updateBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;updateTime|||false|string||
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 删除物模型


**接口地址**:`/product/thingModel/delete`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": 0,
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|id|id|body|true|Request«long»|Request«long»|
|&emsp;&emsp;data|||false|integer(int64)||
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 保存物模型


**接口地址**:`/product/thingModel/save`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": {
    "createBy": 0,
    "createDept": 0,
    "createTime": "",
    "model": "",
    "productKey": "",
    "updateBy": 0,
    "updateTime": ""
  },
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|request|request|body|true|Request«ThingModelBo»|Request«ThingModelBo»|
|&emsp;&emsp;data|||false|ThingModelBo|ThingModelBo|
|&emsp;&emsp;&emsp;&emsp;createBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createDept|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createTime|||false|string||
|&emsp;&emsp;&emsp;&emsp;model|模型内容||false|string||
|&emsp;&emsp;&emsp;&emsp;productKey|产品key||false|string||
|&emsp;&emsp;&emsp;&emsp;updateBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;updateTime|||false|string||
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 上传产品图片


**接口地址**:`/product/uploadImg/{productKey}`


**请求方式**:`POST`


**请求数据类型**:`multipart/form-data`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|file|file|formData|true|file||
|productKey|productKey|path|true|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


暂无


**响应示例**:
```javascript

```


# 参数配置 信息操作处理


## 新增参数配置


**接口地址**:`/system/config/add`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": {
    "configKey": "",
    "configName": "",
    "configType": "",
    "configValue": "",
    "createBy": 0,
    "createDept": 0,
    "createTime": "",
    "id": 0,
    "remark": "",
    "updateBy": 0,
    "updateTime": ""
  },
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|request|request|body|true|Request«SysConfigBo»|Request«SysConfigBo»|
|&emsp;&emsp;data|||false|SysConfigBo|SysConfigBo|
|&emsp;&emsp;&emsp;&emsp;configKey|||false|string||
|&emsp;&emsp;&emsp;&emsp;configName|||false|string||
|&emsp;&emsp;&emsp;&emsp;configType|||false|string||
|&emsp;&emsp;&emsp;&emsp;configValue|||false|string||
|&emsp;&emsp;&emsp;&emsp;createBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createDept|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createTime|||false|string||
|&emsp;&emsp;&emsp;&emsp;id|||false|integer||
|&emsp;&emsp;&emsp;&emsp;remark|||false|string||
|&emsp;&emsp;&emsp;&emsp;updateBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;updateTime|||false|string||
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 删除参数配置


**接口地址**:`/system/config/delete`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": [],
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|request|request|body|true|Request«List«long»»|Request«List«long»»|
|&emsp;&emsp;data|||false|array|integer|
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 修改参数配置


**接口地址**:`/system/config/edit`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": {
    "configKey": "",
    "configName": "",
    "configType": "",
    "configValue": "",
    "createBy": 0,
    "createDept": 0,
    "createTime": "",
    "id": 0,
    "remark": "",
    "updateBy": 0,
    "updateTime": ""
  },
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|request|request|body|true|Request«SysConfigBo»|Request«SysConfigBo»|
|&emsp;&emsp;data|||false|SysConfigBo|SysConfigBo|
|&emsp;&emsp;&emsp;&emsp;configKey|||false|string||
|&emsp;&emsp;&emsp;&emsp;configName|||false|string||
|&emsp;&emsp;&emsp;&emsp;configType|||false|string||
|&emsp;&emsp;&emsp;&emsp;configValue|||false|string||
|&emsp;&emsp;&emsp;&emsp;createBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createDept|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createTime|||false|string||
|&emsp;&emsp;&emsp;&emsp;id|||false|integer||
|&emsp;&emsp;&emsp;&emsp;remark|||false|string||
|&emsp;&emsp;&emsp;&emsp;updateBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;updateTime|||false|string||
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 导出参数配置列表


**接口地址**:`/system/config/export`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|configKey||query|false|string||
|configName||query|false|string||
|configType||query|false|string||
|configValue||query|false|string||
|createBy||query|false|integer(int64)||
|createDept||query|false|integer(int64)||
|createTime||query|false|string(date-time)||
|id||query|false|integer(int64)||
|remark||query|false|string||
|updateBy||query|false|integer(int64)||
|updateTime||query|false|string(date-time)||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 导出系统数据


**接口地址**:`/system/config/exportSysData`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


暂无


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 根据参数键名查询参数值


**接口地址**:`/system/config/getConfigKey`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": "",
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|request|request|body|true|Request«string»|Request«string»|
|&emsp;&emsp;data|||false|string||
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 根据参数编号获取详细信息


**接口地址**:`/system/config/getDetail`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": 0,
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|request|request|body|true|Request«long»|Request«long»|
|&emsp;&emsp;data|||false|integer(int64)||
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|SysConfigVo|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|configKey||string||
|configName||string||
|configType||string||
|configValue||string||
|createTime||string(date-time)|string(date-time)|
|id||integer(int64)|integer(int64)|
|remark||string||


**响应示例**:
```javascript
{
	"configKey": "",
	"configName": "",
	"configType": "",
	"configValue": "",
	"createTime": "",
	"id": 0,
	"remark": ""
}
```


## 获取参数配置列表


**接口地址**:`/system/config/list`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": {
    "configKey": "",
    "configName": "",
    "configType": "",
    "configValue": "",
    "createBy": 0,
    "createDept": 0,
    "createTime": "",
    "id": 0,
    "remark": "",
    "updateBy": 0,
    "updateTime": ""
  },
  "pageNum": 0,
  "pageSize": 0,
  "requestId": "",
  "sortMap": {}
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|query|query|body|true|PageRequest«SysConfigBo»|PageRequest«SysConfigBo»|
|&emsp;&emsp;data|||false|SysConfigBo|SysConfigBo|
|&emsp;&emsp;&emsp;&emsp;configKey|||false|string||
|&emsp;&emsp;&emsp;&emsp;configName|||false|string||
|&emsp;&emsp;&emsp;&emsp;configType|||false|string||
|&emsp;&emsp;&emsp;&emsp;configValue|||false|string||
|&emsp;&emsp;&emsp;&emsp;createBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createDept|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createTime|||false|string||
|&emsp;&emsp;&emsp;&emsp;id|||false|integer||
|&emsp;&emsp;&emsp;&emsp;remark|||false|string||
|&emsp;&emsp;&emsp;&emsp;updateBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;updateTime|||false|string||
|&emsp;&emsp;pageNum|||false|integer(int32)||
|&emsp;&emsp;pageSize|||false|integer(int32)||
|&emsp;&emsp;requestId|||false|string||
|&emsp;&emsp;sortMap|||false|object||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|Paging«SysConfigVo»|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|rows||array|SysConfigVo|
|&emsp;&emsp;configKey||string||
|&emsp;&emsp;configName||string||
|&emsp;&emsp;configType||string||
|&emsp;&emsp;configValue||string||
|&emsp;&emsp;createTime||string(date-time)||
|&emsp;&emsp;id||integer(int64)||
|&emsp;&emsp;remark||string||
|total||integer(int64)|integer(int64)|


**响应示例**:
```javascript
{
	"rows": [
		{
			"configKey": "",
			"configName": "",
			"configType": "",
			"configValue": "",
			"createTime": "",
			"id": 0,
			"remark": ""
		}
	],
	"total": 0
}
```


## 刷新参数缓存


**接口地址**:`/system/config/refreshCache`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


暂无


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 根据参数键名修改参数配置


**接口地址**:`/system/config/updateByKey`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": {
    "configKey": "",
    "configName": "",
    "configType": "",
    "configValue": "",
    "createBy": 0,
    "createDept": 0,
    "createTime": "",
    "id": 0,
    "remark": "",
    "updateBy": 0,
    "updateTime": ""
  },
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|request|request|body|true|Request«SysConfigBo»|Request«SysConfigBo»|
|&emsp;&emsp;data|||false|SysConfigBo|SysConfigBo|
|&emsp;&emsp;&emsp;&emsp;configKey|||false|string||
|&emsp;&emsp;&emsp;&emsp;configName|||false|string||
|&emsp;&emsp;&emsp;&emsp;configType|||false|string||
|&emsp;&emsp;&emsp;&emsp;configValue|||false|string||
|&emsp;&emsp;&emsp;&emsp;createBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createDept|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createTime|||false|string||
|&emsp;&emsp;&emsp;&emsp;id|||false|integer||
|&emsp;&emsp;&emsp;&emsp;remark|||false|string||
|&emsp;&emsp;&emsp;&emsp;updateBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;updateTime|||false|string||
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


暂无


**响应示例**:
```javascript

```


# 告警中心


## 新增告警中心配置


**接口地址**:`/alert/createAlertConfig`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": {
    "createAt": 0,
    "createBy": 0,
    "createDept": 0,
    "createTime": "",
    "description": "",
    "enable": true,
    "id": 0,
    "level": "",
    "messageTemplateId": 0,
    "name": "",
    "ruleInfoId": "",
    "tenantId": 0,
    "uid": "",
    "updateBy": 0,
    "updateTime": ""
  },
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|request|request|body|true|Request«AlertConfig»|Request«AlertConfig»|
|&emsp;&emsp;data|||false|AlertConfig|AlertConfig|
|&emsp;&emsp;&emsp;&emsp;createAt|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createDept|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createTime|||false|string||
|&emsp;&emsp;&emsp;&emsp;description|||false|string||
|&emsp;&emsp;&emsp;&emsp;enable|||false|boolean||
|&emsp;&emsp;&emsp;&emsp;id|||false|integer||
|&emsp;&emsp;&emsp;&emsp;level|||false|string||
|&emsp;&emsp;&emsp;&emsp;messageTemplateId|||false|integer||
|&emsp;&emsp;&emsp;&emsp;name|||false|string||
|&emsp;&emsp;&emsp;&emsp;ruleInfoId|||false|string||
|&emsp;&emsp;&emsp;&emsp;tenantId|||false|integer||
|&emsp;&emsp;&emsp;&emsp;uid|||false|string||
|&emsp;&emsp;&emsp;&emsp;updateBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;updateTime|||false|string||
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|AlertConfig|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|createAt||integer(int64)|integer(int64)|
|createBy||integer(int64)|integer(int64)|
|createDept||integer(int64)|integer(int64)|
|createTime||string(date-time)|string(date-time)|
|description||string||
|enable||boolean||
|id||integer(int64)|integer(int64)|
|level||string||
|messageTemplateId||integer(int64)|integer(int64)|
|name||string||
|ruleInfoId||string||
|tenantId||integer(int64)|integer(int64)|
|uid||string||
|updateBy||integer(int64)|integer(int64)|
|updateTime||string(date-time)|string(date-time)|


**响应示例**:
```javascript
{
	"createAt": 0,
	"createBy": 0,
	"createDept": 0,
	"createTime": "",
	"description": "",
	"enable": true,
	"id": 0,
	"level": "",
	"messageTemplateId": 0,
	"name": "",
	"ruleInfoId": "",
	"tenantId": 0,
	"uid": "",
	"updateBy": 0,
	"updateTime": ""
}
```


## 删除告警中心配置


**接口地址**:`/alert/deleteAlertConfigById`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": 0,
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|request|request|body|true|Request«long»|Request«long»|
|&emsp;&emsp;data|||false|integer(int64)||
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 查询告警中心配置分页


**接口地址**:`/alert/selectAlertConfigPage`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": {
    "createAt": 0,
    "createBy": 0,
    "createDept": 0,
    "createTime": "",
    "description": "",
    "enable": true,
    "id": 0,
    "level": "",
    "messageTemplateId": 0,
    "name": "",
    "ruleInfoId": "",
    "tenantId": 0,
    "uid": "",
    "updateBy": 0,
    "updateTime": ""
  },
  "pageNum": 0,
  "pageSize": 0,
  "requestId": "",
  "sortMap": {}
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|request|request|body|true|PageRequest«AlertConfig»|PageRequest«AlertConfig»|
|&emsp;&emsp;data|||false|AlertConfig|AlertConfig|
|&emsp;&emsp;&emsp;&emsp;createAt|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createDept|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createTime|||false|string||
|&emsp;&emsp;&emsp;&emsp;description|||false|string||
|&emsp;&emsp;&emsp;&emsp;enable|||false|boolean||
|&emsp;&emsp;&emsp;&emsp;id|||false|integer||
|&emsp;&emsp;&emsp;&emsp;level|||false|string||
|&emsp;&emsp;&emsp;&emsp;messageTemplateId|||false|integer||
|&emsp;&emsp;&emsp;&emsp;name|||false|string||
|&emsp;&emsp;&emsp;&emsp;ruleInfoId|||false|string||
|&emsp;&emsp;&emsp;&emsp;tenantId|||false|integer||
|&emsp;&emsp;&emsp;&emsp;uid|||false|string||
|&emsp;&emsp;&emsp;&emsp;updateBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;updateTime|||false|string||
|&emsp;&emsp;pageNum|||false|integer(int32)||
|&emsp;&emsp;pageSize|||false|integer(int32)||
|&emsp;&emsp;requestId|||false|string||
|&emsp;&emsp;sortMap|||false|object||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|Paging«AlertConfig»|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|rows||array|AlertConfig|
|&emsp;&emsp;createAt||integer(int64)||
|&emsp;&emsp;createBy||integer(int64)||
|&emsp;&emsp;createDept||integer(int64)||
|&emsp;&emsp;createTime||string(date-time)||
|&emsp;&emsp;description||string||
|&emsp;&emsp;enable||boolean||
|&emsp;&emsp;id||integer(int64)||
|&emsp;&emsp;level||string||
|&emsp;&emsp;messageTemplateId||integer(int64)||
|&emsp;&emsp;name||string||
|&emsp;&emsp;ruleInfoId||string||
|&emsp;&emsp;tenantId||integer(int64)||
|&emsp;&emsp;uid||string||
|&emsp;&emsp;updateBy||integer(int64)||
|&emsp;&emsp;updateTime||string(date-time)||
|total||integer(int64)|integer(int64)|


**响应示例**:
```javascript
{
	"rows": [
		{
			"createAt": 0,
			"createBy": 0,
			"createDept": 0,
			"createTime": "",
			"description": "",
			"enable": true,
			"id": 0,
			"level": "",
			"messageTemplateId": 0,
			"name": "",
			"ruleInfoId": "",
			"tenantId": 0,
			"uid": "",
			"updateBy": 0,
			"updateTime": ""
		}
	],
	"total": 0
}
```


## 查询告警消息分页


**接口地址**:`/alert/selectAlertRecordPage`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": {
    "alertTime": 0,
    "createBy": 0,
    "createDept": 0,
    "createTime": "",
    "details": "",
    "id": 0,
    "level": "",
    "name": "",
    "readFlg": true,
    "tenantId": 0,
    "uid": "",
    "updateBy": 0,
    "updateTime": ""
  },
  "pageNum": 0,
  "pageSize": 0,
  "requestId": "",
  "sortMap": {}
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|request|request|body|true|PageRequest«AlertRecord»|PageRequest«AlertRecord»|
|&emsp;&emsp;data|||false|AlertRecord|AlertRecord|
|&emsp;&emsp;&emsp;&emsp;alertTime|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createDept|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createTime|||false|string||
|&emsp;&emsp;&emsp;&emsp;details|||false|string||
|&emsp;&emsp;&emsp;&emsp;id|||false|integer||
|&emsp;&emsp;&emsp;&emsp;level|||false|string||
|&emsp;&emsp;&emsp;&emsp;name|||false|string||
|&emsp;&emsp;&emsp;&emsp;readFlg|||false|boolean||
|&emsp;&emsp;&emsp;&emsp;tenantId|||false|integer||
|&emsp;&emsp;&emsp;&emsp;uid|||false|string||
|&emsp;&emsp;&emsp;&emsp;updateBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;updateTime|||false|string||
|&emsp;&emsp;pageNum|||false|integer(int32)||
|&emsp;&emsp;pageSize|||false|integer(int32)||
|&emsp;&emsp;requestId|||false|string||
|&emsp;&emsp;sortMap|||false|object||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|Paging«AlertRecord»|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|rows||array|AlertRecord|
|&emsp;&emsp;alertTime||integer(int64)||
|&emsp;&emsp;createBy||integer(int64)||
|&emsp;&emsp;createDept||integer(int64)||
|&emsp;&emsp;createTime||string(date-time)||
|&emsp;&emsp;details||string||
|&emsp;&emsp;id||integer(int64)||
|&emsp;&emsp;level||string||
|&emsp;&emsp;name||string||
|&emsp;&emsp;readFlg||boolean||
|&emsp;&emsp;tenantId||integer(int64)||
|&emsp;&emsp;uid||string||
|&emsp;&emsp;updateBy||integer(int64)||
|&emsp;&emsp;updateTime||string(date-time)||
|total||integer(int64)|integer(int64)|


**响应示例**:
```javascript
{
	"rows": [
		{
			"alertTime": 0,
			"createBy": 0,
			"createDept": 0,
			"createTime": "",
			"details": "",
			"id": 0,
			"level": "",
			"name": "",
			"readFlg": true,
			"tenantId": 0,
			"uid": "",
			"updateBy": 0,
			"updateTime": ""
		}
	],
	"total": 0
}
```


## 编辑告警中心配置


**接口地址**:`/alert/updateAlertConfig`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": {
    "createAt": 0,
    "createBy": 0,
    "createDept": 0,
    "createTime": "",
    "description": "",
    "enable": true,
    "id": 0,
    "level": "",
    "messageTemplateId": 0,
    "name": "",
    "ruleInfoId": "",
    "tenantId": 0,
    "uid": "",
    "updateBy": 0,
    "updateTime": ""
  },
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|request|request|body|true|Request«AlertConfig»|Request«AlertConfig»|
|&emsp;&emsp;data|||false|AlertConfig|AlertConfig|
|&emsp;&emsp;&emsp;&emsp;createAt|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createDept|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createTime|||false|string||
|&emsp;&emsp;&emsp;&emsp;description|||false|string||
|&emsp;&emsp;&emsp;&emsp;enable|||false|boolean||
|&emsp;&emsp;&emsp;&emsp;id|||false|integer||
|&emsp;&emsp;&emsp;&emsp;level|||false|string||
|&emsp;&emsp;&emsp;&emsp;messageTemplateId|||false|integer||
|&emsp;&emsp;&emsp;&emsp;name|||false|string||
|&emsp;&emsp;&emsp;&emsp;ruleInfoId|||false|string||
|&emsp;&emsp;&emsp;&emsp;tenantId|||false|integer||
|&emsp;&emsp;&emsp;&emsp;uid|||false|string||
|&emsp;&emsp;&emsp;&emsp;updateBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;updateTime|||false|string||
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|AlertConfig|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|createAt||integer(int64)|integer(int64)|
|createBy||integer(int64)|integer(int64)|
|createDept||integer(int64)|integer(int64)|
|createTime||string(date-time)|string(date-time)|
|description||string||
|enable||boolean||
|id||integer(int64)|integer(int64)|
|level||string||
|messageTemplateId||integer(int64)|integer(int64)|
|name||string||
|ruleInfoId||string||
|tenantId||integer(int64)|integer(int64)|
|uid||string||
|updateBy||integer(int64)|integer(int64)|
|updateTime||string(date-time)|string(date-time)|


**响应示例**:
```javascript
{
	"createAt": 0,
	"createBy": 0,
	"createDept": 0,
	"createTime": "",
	"description": "",
	"enable": true,
	"id": 0,
	"level": "",
	"messageTemplateId": 0,
	"name": "",
	"ruleInfoId": "",
	"tenantId": 0,
	"uid": "",
	"updateBy": 0,
	"updateTime": ""
}
```


# 岗位信息


## 新增岗位


**接口地址**:`/system/post/add`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": {
    "createBy": 0,
    "createDept": 0,
    "createTime": "",
    "id": 0,
    "postCode": "",
    "postName": "",
    "postSort": 0,
    "remark": "",
    "status": "",
    "updateBy": 0,
    "updateTime": ""
  },
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|post|post|body|true|Request«SysPostBo»|Request«SysPostBo»|
|&emsp;&emsp;data|||false|SysPostBo|SysPostBo|
|&emsp;&emsp;&emsp;&emsp;createBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createDept|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createTime|||false|string||
|&emsp;&emsp;&emsp;&emsp;id|||false|integer||
|&emsp;&emsp;&emsp;&emsp;postCode|||false|string||
|&emsp;&emsp;&emsp;&emsp;postName|||false|string||
|&emsp;&emsp;&emsp;&emsp;postSort|||false|integer||
|&emsp;&emsp;&emsp;&emsp;remark|||false|string||
|&emsp;&emsp;&emsp;&emsp;status|||false|string||
|&emsp;&emsp;&emsp;&emsp;updateBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;updateTime|||false|string||
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 删除岗位


**接口地址**:`/system/post/delete`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": [],
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|postIds|postIds|body|true|Request«List«long»»|Request«List«long»»|
|&emsp;&emsp;data|||false|array|integer|
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 修改岗位


**接口地址**:`/system/post/edit`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": {
    "createBy": 0,
    "createDept": 0,
    "createTime": "",
    "id": 0,
    "postCode": "",
    "postName": "",
    "postSort": 0,
    "remark": "",
    "status": "",
    "updateBy": 0,
    "updateTime": ""
  },
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|post|post|body|true|Request«SysPostBo»|Request«SysPostBo»|
|&emsp;&emsp;data|||false|SysPostBo|SysPostBo|
|&emsp;&emsp;&emsp;&emsp;createBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createDept|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createTime|||false|string||
|&emsp;&emsp;&emsp;&emsp;id|||false|integer||
|&emsp;&emsp;&emsp;&emsp;postCode|||false|string||
|&emsp;&emsp;&emsp;&emsp;postName|||false|string||
|&emsp;&emsp;&emsp;&emsp;postSort|||false|integer||
|&emsp;&emsp;&emsp;&emsp;remark|||false|string||
|&emsp;&emsp;&emsp;&emsp;status|||false|string||
|&emsp;&emsp;&emsp;&emsp;updateBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;updateTime|||false|string||
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 导出岗位列表


**接口地址**:`/system/post/export`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|createBy||query|false|integer(int64)||
|createDept||query|false|integer(int64)||
|createTime||query|false|string(date-time)||
|id||query|false|integer(int64)||
|postCode||query|false|string||
|postName||query|false|string||
|postSort||query|false|integer(int32)||
|remark||query|false|string||
|status||query|false|string||
|updateBy||query|false|integer(int64)||
|updateTime||query|false|string(date-time)||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 根据岗位编号获取详细信息


**接口地址**:`/system/post/getInfo`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": 0,
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|postId|postId|body|true|Request«long»|Request«long»|
|&emsp;&emsp;data|||false|integer(int64)||
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|SysPostVo|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|createTime||string(date-time)|string(date-time)|
|id||integer(int64)|integer(int64)|
|postCode||string||
|postName||string||
|postSort||integer(int32)|integer(int32)|
|remark||string||
|status||string||


**响应示例**:
```javascript
{
	"createTime": "",
	"id": 0,
	"postCode": "",
	"postName": "",
	"postSort": 0,
	"remark": "",
	"status": ""
}
```


## 获取岗位列表


**接口地址**:`/system/post/list`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": {
    "createBy": 0,
    "createDept": 0,
    "createTime": "",
    "id": 0,
    "postCode": "",
    "postName": "",
    "postSort": 0,
    "remark": "",
    "status": "",
    "updateBy": 0,
    "updateTime": ""
  },
  "pageNum": 0,
  "pageSize": 0,
  "requestId": "",
  "sortMap": {}
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|query|query|body|true|PageRequest«SysPostBo»|PageRequest«SysPostBo»|
|&emsp;&emsp;data|||false|SysPostBo|SysPostBo|
|&emsp;&emsp;&emsp;&emsp;createBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createDept|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createTime|||false|string||
|&emsp;&emsp;&emsp;&emsp;id|||false|integer||
|&emsp;&emsp;&emsp;&emsp;postCode|||false|string||
|&emsp;&emsp;&emsp;&emsp;postName|||false|string||
|&emsp;&emsp;&emsp;&emsp;postSort|||false|integer||
|&emsp;&emsp;&emsp;&emsp;remark|||false|string||
|&emsp;&emsp;&emsp;&emsp;status|||false|string||
|&emsp;&emsp;&emsp;&emsp;updateBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;updateTime|||false|string||
|&emsp;&emsp;pageNum|||false|integer(int32)||
|&emsp;&emsp;pageSize|||false|integer(int32)||
|&emsp;&emsp;requestId|||false|string||
|&emsp;&emsp;sortMap|||false|object||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|Paging«SysPostVo»|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|rows||array|SysPostVo|
|&emsp;&emsp;createTime||string(date-time)||
|&emsp;&emsp;id||integer(int64)||
|&emsp;&emsp;postCode||string||
|&emsp;&emsp;postName||string||
|&emsp;&emsp;postSort||integer(int32)||
|&emsp;&emsp;remark||string||
|&emsp;&emsp;status||string||
|total||integer(int64)|integer(int64)|


**响应示例**:
```javascript
{
	"rows": [
		{
			"createTime": "",
			"id": 0,
			"postCode": "",
			"postName": "",
			"postSort": 0,
			"remark": "",
			"status": ""
		}
	],
	"total": 0
}
```


## 获取岗位选择框列表


**接口地址**:`/system/post/optionselect`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


暂无


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|SysPostVo|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|createTime||string(date-time)|string(date-time)|
|id||integer(int64)|integer(int64)|
|postCode||string||
|postName||string||
|postSort||integer(int32)|integer(int32)|
|remark||string||
|status||string||


**响应示例**:
```javascript
[
	{
		"createTime": "",
		"id": 0,
		"postCode": "",
		"postName": "",
		"postSort": 0,
		"remark": "",
		"status": ""
	}
]
```


# 插件管理


## 添加插件


**接口地址**:`/plugin/add`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": {
    "config": "",
    "createBy": 0,
    "createDept": 0,
    "createTime": "",
    "deployType": "",
    "id": 0,
    "name": "",
    "protocol": "",
    "script": "",
    "state": "",
    "type": "",
    "updateBy": 0,
    "updateTime": ""
  },
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|request|request|body|true|Request«PluginInfoBo»|Request«PluginInfoBo»|
|&emsp;&emsp;data|||false|PluginInfoBo|PluginInfoBo|
|&emsp;&emsp;&emsp;&emsp;config|||false|string||
|&emsp;&emsp;&emsp;&emsp;createBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createDept|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createTime|||false|string||
|&emsp;&emsp;&emsp;&emsp;deployType|||false|string||
|&emsp;&emsp;&emsp;&emsp;id|||false|integer||
|&emsp;&emsp;&emsp;&emsp;name|||false|string||
|&emsp;&emsp;&emsp;&emsp;protocol|||false|string||
|&emsp;&emsp;&emsp;&emsp;script|||false|string||
|&emsp;&emsp;&emsp;&emsp;state|||false|string||
|&emsp;&emsp;&emsp;&emsp;type|||false|string||
|&emsp;&emsp;&emsp;&emsp;updateBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;updateTime|||false|string||
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 修改插件状态


**接口地址**:`/plugin/changeState`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": {
    "config": "",
    "createBy": 0,
    "createDept": 0,
    "createTime": "",
    "deployType": "",
    "id": 0,
    "name": "",
    "protocol": "",
    "script": "",
    "state": "",
    "type": "",
    "updateBy": 0,
    "updateTime": ""
  },
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|request|request|body|true|Request«PluginInfoBo»|Request«PluginInfoBo»|
|&emsp;&emsp;data|||false|PluginInfoBo|PluginInfoBo|
|&emsp;&emsp;&emsp;&emsp;config|||false|string||
|&emsp;&emsp;&emsp;&emsp;createBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createDept|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createTime|||false|string||
|&emsp;&emsp;&emsp;&emsp;deployType|||false|string||
|&emsp;&emsp;&emsp;&emsp;id|||false|integer||
|&emsp;&emsp;&emsp;&emsp;name|||false|string||
|&emsp;&emsp;&emsp;&emsp;protocol|||false|string||
|&emsp;&emsp;&emsp;&emsp;script|||false|string||
|&emsp;&emsp;&emsp;&emsp;state|||false|string||
|&emsp;&emsp;&emsp;&emsp;type|||false|string||
|&emsp;&emsp;&emsp;&emsp;updateBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;updateTime|||false|string||
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 删除插件


**接口地址**:`/plugin/delete`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": 0,
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|request|request|body|true|Request«long»|Request«long»|
|&emsp;&emsp;data|||false|integer(int64)||
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 插件详情


**接口地址**:`/plugin/detail`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": 0,
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|request|request|body|true|Request«long»|Request«long»|
|&emsp;&emsp;data|||false|integer(int64)||
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|PluginInfoVo|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|config||string||
|configSchema||string||
|createTime||string(date-time)|string(date-time)|
|deployType||string||
|description||string||
|file||string||
|id||integer(int64)|integer(int64)|
|name||string||
|pluginId||string||
|protocol||string||
|script||string||
|state||string||
|type||string||
|version||string||


**响应示例**:
```javascript
{
	"config": "",
	"configSchema": "",
	"createTime": "",
	"deployType": "",
	"description": "",
	"file": "",
	"id": 0,
	"name": "",
	"pluginId": "",
	"protocol": "",
	"script": "",
	"state": "",
	"type": "",
	"version": ""
}
```


## 修改插件


**接口地址**:`/plugin/edit`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": {
    "config": "",
    "createBy": 0,
    "createDept": 0,
    "createTime": "",
    "deployType": "",
    "id": 0,
    "name": "",
    "protocol": "",
    "script": "",
    "state": "",
    "type": "",
    "updateBy": 0,
    "updateTime": ""
  },
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|request|request|body|true|Request«PluginInfoBo»|Request«PluginInfoBo»|
|&emsp;&emsp;data|||false|PluginInfoBo|PluginInfoBo|
|&emsp;&emsp;&emsp;&emsp;config|||false|string||
|&emsp;&emsp;&emsp;&emsp;createBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createDept|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createTime|||false|string||
|&emsp;&emsp;&emsp;&emsp;deployType|||false|string||
|&emsp;&emsp;&emsp;&emsp;id|||false|integer||
|&emsp;&emsp;&emsp;&emsp;name|||false|string||
|&emsp;&emsp;&emsp;&emsp;protocol|||false|string||
|&emsp;&emsp;&emsp;&emsp;script|||false|string||
|&emsp;&emsp;&emsp;&emsp;state|||false|string||
|&emsp;&emsp;&emsp;&emsp;type|||false|string||
|&emsp;&emsp;&emsp;&emsp;updateBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;updateTime|||false|string||
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 获取插件列表


**接口地址**:`/plugin/list`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": {
    "config": "",
    "createBy": 0,
    "createDept": 0,
    "createTime": "",
    "deployType": "",
    "id": 0,
    "name": "",
    "protocol": "",
    "script": "",
    "state": "",
    "type": "",
    "updateBy": 0,
    "updateTime": ""
  },
  "pageNum": 0,
  "pageSize": 0,
  "requestId": "",
  "sortMap": {}
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|query|query|body|true|PageRequest«PluginInfoBo»|PageRequest«PluginInfoBo»|
|&emsp;&emsp;data|||false|PluginInfoBo|PluginInfoBo|
|&emsp;&emsp;&emsp;&emsp;config|||false|string||
|&emsp;&emsp;&emsp;&emsp;createBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createDept|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createTime|||false|string||
|&emsp;&emsp;&emsp;&emsp;deployType|||false|string||
|&emsp;&emsp;&emsp;&emsp;id|||false|integer||
|&emsp;&emsp;&emsp;&emsp;name|||false|string||
|&emsp;&emsp;&emsp;&emsp;protocol|||false|string||
|&emsp;&emsp;&emsp;&emsp;script|||false|string||
|&emsp;&emsp;&emsp;&emsp;state|||false|string||
|&emsp;&emsp;&emsp;&emsp;type|||false|string||
|&emsp;&emsp;&emsp;&emsp;updateBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;updateTime|||false|string||
|&emsp;&emsp;pageNum|||false|integer(int32)||
|&emsp;&emsp;pageSize|||false|integer(int32)||
|&emsp;&emsp;requestId|||false|string||
|&emsp;&emsp;sortMap|||false|object||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|Paging«PluginInfoVo»|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|rows||array|PluginInfoVo|
|&emsp;&emsp;config||string||
|&emsp;&emsp;configSchema||string||
|&emsp;&emsp;createTime||string(date-time)||
|&emsp;&emsp;deployType||string||
|&emsp;&emsp;description||string||
|&emsp;&emsp;file||string||
|&emsp;&emsp;id||integer(int64)||
|&emsp;&emsp;name||string||
|&emsp;&emsp;pluginId||string||
|&emsp;&emsp;protocol||string||
|&emsp;&emsp;script||string||
|&emsp;&emsp;state||string||
|&emsp;&emsp;type||string||
|&emsp;&emsp;version||string||
|total||integer(int64)|integer(int64)|


**响应示例**:
```javascript
{
	"rows": [
		{
			"config": "",
			"configSchema": "",
			"createTime": "",
			"deployType": "",
			"description": "",
			"file": "",
			"id": 0,
			"name": "",
			"pluginId": "",
			"protocol": "",
			"script": "",
			"state": "",
			"type": "",
			"version": ""
		}
	],
	"total": 0
}
```


## 上传Jar包


**接口地址**:`/plugin/uploadJar`


**请求方式**:`POST`


**请求数据类型**:`multipart/form-data`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|file|file|formData|true|file||
|id|id|query|true|integer(int64)||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


暂无


**响应示例**:
```javascript

```


# 操作日志记录


## 清理操作日志记录


**接口地址**:`/monitor/operlog/clean`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


暂无


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 批量删除操作日志记录


**接口地址**:`/monitor/operlog/delete`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": [],
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|bo|bo|body|true|Request«List«long»»|Request«List«long»»|
|&emsp;&emsp;data|||false|array|integer|
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 导出操作日志记录列表


**接口地址**:`/monitor/operlog/export`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|businessType||query|false|integer(int32)||
|businessTypes||query|false|array|integer|
|costTime||query|false|integer(int64)||
|createBy||query|false|integer(int64)||
|createDept||query|false|integer(int64)||
|createTime||query|false|string(date-time)||
|deptName||query|false|string||
|errorMsg||query|false|string||
|id||query|false|integer(int64)||
|jsonResult||query|false|string||
|method||query|false|string||
|operIp||query|false|string||
|operLocation||query|false|string||
|operName||query|false|string||
|operParam||query|false|string||
|operTime||query|false|string(date-time)||
|operUrl||query|false|string||
|operatorType||query|false|integer(int32)||
|params||query|false|object||
|requestMethod||query|false|string||
|status||query|false|integer(int32)||
|tenantId||query|false|integer(int64)||
|title||query|false|string||
|updateBy||query|false|integer(int64)||
|updateTime||query|false|string(date-time)||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 获取操作日志记录列表


**接口地址**:`/monitor/operlog/list`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": {
    "businessType": 0,
    "businessTypes": [],
    "costTime": 0,
    "createBy": 0,
    "createDept": 0,
    "createTime": "",
    "deptName": "",
    "errorMsg": "",
    "id": 0,
    "jsonResult": "",
    "method": "",
    "operIp": "",
    "operLocation": "",
    "operName": "",
    "operParam": "",
    "operTime": "",
    "operUrl": "",
    "operatorType": 0,
    "params": {},
    "requestMethod": "",
    "status": 0,
    "tenantId": 0,
    "title": "",
    "updateBy": 0,
    "updateTime": ""
  },
  "pageNum": 0,
  "pageSize": 0,
  "requestId": "",
  "sortMap": {}
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|query|query|body|true|PageRequest«SysOperLogBo»|PageRequest«SysOperLogBo»|
|&emsp;&emsp;data|||false|SysOperLogBo|SysOperLogBo|
|&emsp;&emsp;&emsp;&emsp;businessType|||false|integer||
|&emsp;&emsp;&emsp;&emsp;businessTypes|||false|array|integer|
|&emsp;&emsp;&emsp;&emsp;costTime|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createDept|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createTime|||false|string||
|&emsp;&emsp;&emsp;&emsp;deptName|||false|string||
|&emsp;&emsp;&emsp;&emsp;errorMsg|||false|string||
|&emsp;&emsp;&emsp;&emsp;id|||false|integer||
|&emsp;&emsp;&emsp;&emsp;jsonResult|||false|string||
|&emsp;&emsp;&emsp;&emsp;method|||false|string||
|&emsp;&emsp;&emsp;&emsp;operIp|||false|string||
|&emsp;&emsp;&emsp;&emsp;operLocation|||false|string||
|&emsp;&emsp;&emsp;&emsp;operName|||false|string||
|&emsp;&emsp;&emsp;&emsp;operParam|||false|string||
|&emsp;&emsp;&emsp;&emsp;operTime|||false|string||
|&emsp;&emsp;&emsp;&emsp;operUrl|||false|string||
|&emsp;&emsp;&emsp;&emsp;operatorType|||false|integer||
|&emsp;&emsp;&emsp;&emsp;params|||false|object||
|&emsp;&emsp;&emsp;&emsp;requestMethod|||false|string||
|&emsp;&emsp;&emsp;&emsp;status|||false|integer||
|&emsp;&emsp;&emsp;&emsp;tenantId|||false|integer||
|&emsp;&emsp;&emsp;&emsp;title|||false|string||
|&emsp;&emsp;&emsp;&emsp;updateBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;updateTime|||false|string||
|&emsp;&emsp;pageNum|||false|integer(int32)||
|&emsp;&emsp;pageSize|||false|integer(int32)||
|&emsp;&emsp;requestId|||false|string||
|&emsp;&emsp;sortMap|||false|object||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|Paging«SysOperLogVo»|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|rows||array|SysOperLogVo|
|&emsp;&emsp;businessType||integer(int32)||
|&emsp;&emsp;businessTypes||array|integer|
|&emsp;&emsp;costTime||integer(int64)||
|&emsp;&emsp;createBy||integer(int64)||
|&emsp;&emsp;createDept||integer(int64)||
|&emsp;&emsp;createTime||string(date-time)||
|&emsp;&emsp;deptName||string||
|&emsp;&emsp;errorMsg||string||
|&emsp;&emsp;id||integer(int64)||
|&emsp;&emsp;jsonResult||string||
|&emsp;&emsp;method||string||
|&emsp;&emsp;operIp||string||
|&emsp;&emsp;operLocation||string||
|&emsp;&emsp;operName||string||
|&emsp;&emsp;operParam||string||
|&emsp;&emsp;operTime||string(date-time)||
|&emsp;&emsp;operUrl||string||
|&emsp;&emsp;operatorType||integer(int32)||
|&emsp;&emsp;requestMethod||string||
|&emsp;&emsp;status||integer(int32)||
|&emsp;&emsp;tenantId||integer(int64)||
|&emsp;&emsp;title||string||
|&emsp;&emsp;updateBy||integer(int64)||
|&emsp;&emsp;updateTime||string(date-time)||
|total||integer(int64)|integer(int64)|


**响应示例**:
```javascript
{
	"rows": [
		{
			"businessType": 0,
			"businessTypes": [],
			"costTime": 0,
			"createBy": 0,
			"createDept": 0,
			"createTime": "",
			"deptName": "",
			"errorMsg": "",
			"id": 0,
			"jsonResult": "",
			"method": "",
			"operIp": "",
			"operLocation": "",
			"operName": "",
			"operParam": "",
			"operTime": "",
			"operUrl": "",
			"operatorType": 0,
			"requestMethod": "",
			"status": 0,
			"tenantId": 0,
			"title": "",
			"updateBy": 0,
			"updateTime": ""
		}
	],
	"total": 0
}
```


# 消息通知


## 新增通道配置


**接口地址**:`/notify/channel/config/add`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": {
    "channelId": 0,
    "createAt": 0,
    "createBy": 0,
    "createDept": 0,
    "createTime": "",
    "id": 0,
    "param": "",
    "tenantId": 0,
    "title": "",
    "updateBy": 0,
    "updateTime": ""
  },
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|request|request|body|true|Request«ChannelConfig»|Request«ChannelConfig»|
|&emsp;&emsp;data|||false|ChannelConfig|ChannelConfig|
|&emsp;&emsp;&emsp;&emsp;channelId|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createAt|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createDept|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createTime|||false|string||
|&emsp;&emsp;&emsp;&emsp;id|||false|integer||
|&emsp;&emsp;&emsp;&emsp;param|||false|string||
|&emsp;&emsp;&emsp;&emsp;tenantId|||false|integer||
|&emsp;&emsp;&emsp;&emsp;title|||false|string||
|&emsp;&emsp;&emsp;&emsp;updateBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;updateTime|||false|string||
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|ChannelConfig|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|channelId||integer(int64)|integer(int64)|
|createAt||integer(int64)|integer(int64)|
|createBy||integer(int64)|integer(int64)|
|createDept||integer(int64)|integer(int64)|
|createTime||string(date-time)|string(date-time)|
|id||integer(int64)|integer(int64)|
|param||string||
|tenantId||integer(int64)|integer(int64)|
|title||string||
|updateBy||integer(int64)|integer(int64)|
|updateTime||string(date-time)|string(date-time)|


**响应示例**:
```javascript
{
	"channelId": 0,
	"createAt": 0,
	"createBy": 0,
	"createDept": 0,
	"createTime": "",
	"id": 0,
	"param": "",
	"tenantId": 0,
	"title": "",
	"updateBy": 0,
	"updateTime": ""
}
```


## 删除通道配置


**接口地址**:`/notify/channel/config/delById`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": 0,
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|request|request|body|true|Request«long»|Request«long»|
|&emsp;&emsp;data|||false|integer(int64)||
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 获取通道配置列表


**接口地址**:`/notify/channel/config/getAll`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


暂无


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|ChannelConfigVo|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|channelId|通道id|string||
|createAt|创建时间|integer(int64)|integer(int64)|
|id|通道配置id|integer(int64)|integer(int64)|
|param|通道配置参数|string||
|title|通道配置名称|string||


**响应示例**:
```javascript
[
	{
		"channelId": "",
		"createAt": 0,
		"id": 0,
		"param": "",
		"title": ""
	}
]
```


## 根据ID获取通道配置


**接口地址**:`/notify/channel/config/getById`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": 0,
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|request|request|body|true|Request«long»|Request«long»|
|&emsp;&emsp;data|||false|integer(int64)||
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|ChannelConfig|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|channelId||integer(int64)|integer(int64)|
|createAt||integer(int64)|integer(int64)|
|createBy||integer(int64)|integer(int64)|
|createDept||integer(int64)|integer(int64)|
|createTime||string(date-time)|string(date-time)|
|id||integer(int64)|integer(int64)|
|param||string||
|tenantId||integer(int64)|integer(int64)|
|title||string||
|updateBy||integer(int64)|integer(int64)|
|updateTime||string(date-time)|string(date-time)|


**响应示例**:
```javascript
{
	"channelId": 0,
	"createAt": 0,
	"createBy": 0,
	"createDept": 0,
	"createTime": "",
	"id": 0,
	"param": "",
	"tenantId": 0,
	"title": "",
	"updateBy": 0,
	"updateTime": ""
}
```


## 获取通道配置分页列表


**接口地址**:`/notify/channel/config/getList`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": {
    "channelId": 0,
    "createAt": 0,
    "createBy": 0,
    "createDept": 0,
    "createTime": "",
    "id": 0,
    "param": "",
    "title": "",
    "updateBy": 0,
    "updateTime": ""
  },
  "pageNum": 0,
  "pageSize": 0,
  "requestId": "",
  "sortMap": {}
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|request|request|body|true|PageRequest«ChannelConfigBo»|PageRequest«ChannelConfigBo»|
|&emsp;&emsp;data|||false|ChannelConfigBo|ChannelConfigBo|
|&emsp;&emsp;&emsp;&emsp;channelId|通道id||false|integer||
|&emsp;&emsp;&emsp;&emsp;createAt|创建时间||false|integer||
|&emsp;&emsp;&emsp;&emsp;createBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createDept|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createTime|||false|string||
|&emsp;&emsp;&emsp;&emsp;id|id||false|integer||
|&emsp;&emsp;&emsp;&emsp;param|通道配置参数||false|string||
|&emsp;&emsp;&emsp;&emsp;title|通道配置名称||false|string||
|&emsp;&emsp;&emsp;&emsp;updateBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;updateTime|||false|string||
|&emsp;&emsp;pageNum|||false|integer(int32)||
|&emsp;&emsp;pageSize|||false|integer(int32)||
|&emsp;&emsp;requestId|||false|string||
|&emsp;&emsp;sortMap|||false|object||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|Paging«ChannelConfigVo»|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|rows||array|ChannelConfigVo|
|&emsp;&emsp;channelId|通道id|string||
|&emsp;&emsp;createAt|创建时间|integer(int64)||
|&emsp;&emsp;id|通道配置id|integer(int64)||
|&emsp;&emsp;param|通道配置参数|string||
|&emsp;&emsp;title|通道配置名称|string||
|total||integer(int64)|integer(int64)|


**响应示例**:
```javascript
{
	"rows": [
		{
			"channelId": "",
			"createAt": 0,
			"id": 0,
			"param": "",
			"title": ""
		}
	],
	"total": 0
}
```


## 修改通道配置


**接口地址**:`/notify/channel/config/updateById`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": {
    "channelId": 0,
    "createAt": 0,
    "createBy": 0,
    "createDept": 0,
    "createTime": "",
    "id": 0,
    "param": "",
    "tenantId": 0,
    "title": "",
    "updateBy": 0,
    "updateTime": ""
  },
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|request|request|body|true|Request«ChannelConfig»|Request«ChannelConfig»|
|&emsp;&emsp;data|||false|ChannelConfig|ChannelConfig|
|&emsp;&emsp;&emsp;&emsp;channelId|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createAt|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createDept|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createTime|||false|string||
|&emsp;&emsp;&emsp;&emsp;id|||false|integer||
|&emsp;&emsp;&emsp;&emsp;param|||false|string||
|&emsp;&emsp;&emsp;&emsp;tenantId|||false|integer||
|&emsp;&emsp;&emsp;&emsp;title|||false|string||
|&emsp;&emsp;&emsp;&emsp;updateBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;updateTime|||false|string||
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|ChannelConfig|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|channelId||integer(int64)|integer(int64)|
|createAt||integer(int64)|integer(int64)|
|createBy||integer(int64)|integer(int64)|
|createDept||integer(int64)|integer(int64)|
|createTime||string(date-time)|string(date-time)|
|id||integer(int64)|integer(int64)|
|param||string||
|tenantId||integer(int64)|integer(int64)|
|title||string||
|updateBy||integer(int64)|integer(int64)|
|updateTime||string(date-time)|string(date-time)|


**响应示例**:
```javascript
{
	"channelId": 0,
	"createAt": 0,
	"createBy": 0,
	"createDept": 0,
	"createTime": "",
	"id": 0,
	"param": "",
	"tenantId": 0,
	"title": "",
	"updateBy": 0,
	"updateTime": ""
}
```


## 获取通道类型列表


**接口地址**:`/notify/channel/getList`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


暂无


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|Channel|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|code||string||
|createAt||integer(int64)|integer(int64)|
|createBy||integer(int64)|integer(int64)|
|createDept||integer(int64)|integer(int64)|
|createTime||string(date-time)|string(date-time)|
|icon||string||
|id||integer(int64)|integer(int64)|
|tenantId||integer(int64)|integer(int64)|
|title||string||
|updateBy||integer(int64)|integer(int64)|
|updateTime||string(date-time)|string(date-time)|


**响应示例**:
```javascript
[
	{
		"code": "",
		"createAt": 0,
		"createBy": 0,
		"createDept": 0,
		"createTime": "",
		"icon": "",
		"id": 0,
		"tenantId": 0,
		"title": "",
		"updateBy": 0,
		"updateTime": ""
	}
]
```


## 新增通道模板


**接口地址**:`/notify/channel/template/add`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": {
    "channelConfigId": 0,
    "content": "",
    "createAt": 0,
    "createBy": 0,
    "createDept": 0,
    "createTime": "",
    "id": 0,
    "title": "",
    "updateBy": 0,
    "updateTime": ""
  },
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|request|request|body|true|Request«ChannelTemplateVo»|Request«ChannelTemplateVo»|
|&emsp;&emsp;data|||false|ChannelTemplateVo_1|ChannelTemplateVo_1|
|&emsp;&emsp;&emsp;&emsp;channelConfigId|通道配置id||false|integer||
|&emsp;&emsp;&emsp;&emsp;content|通道模板内容||false|string||
|&emsp;&emsp;&emsp;&emsp;createAt|创建时间||false|integer||
|&emsp;&emsp;&emsp;&emsp;createBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createDept|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createTime|||false|string||
|&emsp;&emsp;&emsp;&emsp;id|通道模板id||false|integer||
|&emsp;&emsp;&emsp;&emsp;title|通道模板名称||false|string||
|&emsp;&emsp;&emsp;&emsp;updateBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;updateTime|||false|string||
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|ChannelTemplate|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|channelConfigId||integer(int64)|integer(int64)|
|content||string||
|createAt||integer(int64)|integer(int64)|
|createBy||integer(int64)|integer(int64)|
|createDept||integer(int64)|integer(int64)|
|createTime||string(date-time)|string(date-time)|
|id||integer(int64)|integer(int64)|
|tenantId||integer(int64)|integer(int64)|
|title||string||
|updateBy||integer(int64)|integer(int64)|
|updateTime||string(date-time)|string(date-time)|


**响应示例**:
```javascript
{
	"channelConfigId": 0,
	"content": "",
	"createAt": 0,
	"createBy": 0,
	"createDept": 0,
	"createTime": "",
	"id": 0,
	"tenantId": 0,
	"title": "",
	"updateBy": 0,
	"updateTime": ""
}
```


## 删除通道模板


**接口地址**:`/notify/channel/template/delById`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": 0,
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|request|request|body|true|Request«long»|Request«long»|
|&emsp;&emsp;data|||false|integer(int64)||
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 根据ID获取通道模板


**接口地址**:`/notify/channel/template/getById`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": 0,
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|request|request|body|true|Request«long»|Request«long»|
|&emsp;&emsp;data|||false|integer(int64)||
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|ChannelTemplate|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|channelConfigId||integer(int64)|integer(int64)|
|content||string||
|createAt||integer(int64)|integer(int64)|
|createBy||integer(int64)|integer(int64)|
|createDept||integer(int64)|integer(int64)|
|createTime||string(date-time)|string(date-time)|
|id||integer(int64)|integer(int64)|
|tenantId||integer(int64)|integer(int64)|
|title||string||
|updateBy||integer(int64)|integer(int64)|
|updateTime||string(date-time)|string(date-time)|


**响应示例**:
```javascript
{
	"channelConfigId": 0,
	"content": "",
	"createAt": 0,
	"createBy": 0,
	"createDept": 0,
	"createTime": "",
	"id": 0,
	"tenantId": 0,
	"title": "",
	"updateBy": 0,
	"updateTime": ""
}
```


## 获取通道模板列表


**接口地址**:`/notify/channel/template/getList`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": {
    "channelConfigId": 0,
    "content": "",
    "createAt": 0,
    "createBy": 0,
    "createDept": 0,
    "createTime": "",
    "id": 0,
    "title": "",
    "updateBy": 0,
    "updateTime": ""
  },
  "pageNum": 0,
  "pageSize": 0,
  "requestId": "",
  "sortMap": {}
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|request|request|body|true|PageRequest«ChannelTemplateVo»|PageRequest«ChannelTemplateVo»|
|&emsp;&emsp;data|||false|ChannelTemplateVo_1|ChannelTemplateVo_1|
|&emsp;&emsp;&emsp;&emsp;channelConfigId|通道配置id||false|integer||
|&emsp;&emsp;&emsp;&emsp;content|通道模板内容||false|string||
|&emsp;&emsp;&emsp;&emsp;createAt|创建时间||false|integer||
|&emsp;&emsp;&emsp;&emsp;createBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createDept|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createTime|||false|string||
|&emsp;&emsp;&emsp;&emsp;id|通道模板id||false|integer||
|&emsp;&emsp;&emsp;&emsp;title|通道模板名称||false|string||
|&emsp;&emsp;&emsp;&emsp;updateBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;updateTime|||false|string||
|&emsp;&emsp;pageNum|||false|integer(int32)||
|&emsp;&emsp;pageSize|||false|integer(int32)||
|&emsp;&emsp;requestId|||false|string||
|&emsp;&emsp;sortMap|||false|object||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|Paging«ChannelTemplateVo»|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|rows||array|ChannelTemplateVo|
|&emsp;&emsp;channelConfigId|通道配置id|integer(int64)||
|&emsp;&emsp;content|通道模板内容|string||
|&emsp;&emsp;createAt|创建时间|integer(int64)||
|&emsp;&emsp;id|通道模板id|integer(int64)||
|&emsp;&emsp;title|通道模板名称|string||
|total||integer(int64)|integer(int64)|


**响应示例**:
```javascript
{
	"rows": [
		{
			"channelConfigId": 0,
			"content": "",
			"createAt": 0,
			"id": 0,
			"title": ""
		}
	],
	"total": 0
}
```


## 修改通道模板


**接口地址**:`/notify/channel/template/updateById`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": {
    "channelConfigId": 0,
    "content": "",
    "createAt": 0,
    "createBy": 0,
    "createDept": 0,
    "createTime": "",
    "id": 0,
    "tenantId": 0,
    "title": "",
    "updateBy": 0,
    "updateTime": ""
  },
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|request|request|body|true|Request«ChannelTemplate»|Request«ChannelTemplate»|
|&emsp;&emsp;data|||false|ChannelTemplate|ChannelTemplate|
|&emsp;&emsp;&emsp;&emsp;channelConfigId|||false|integer||
|&emsp;&emsp;&emsp;&emsp;content|||false|string||
|&emsp;&emsp;&emsp;&emsp;createAt|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createDept|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createTime|||false|string||
|&emsp;&emsp;&emsp;&emsp;id|||false|integer||
|&emsp;&emsp;&emsp;&emsp;tenantId|||false|integer||
|&emsp;&emsp;&emsp;&emsp;title|||false|string||
|&emsp;&emsp;&emsp;&emsp;updateBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;updateTime|||false|string||
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|ChannelTemplate|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|channelConfigId||integer(int64)|integer(int64)|
|content||string||
|createAt||integer(int64)|integer(int64)|
|createBy||integer(int64)|integer(int64)|
|createDept||integer(int64)|integer(int64)|
|createTime||string(date-time)|string(date-time)|
|id||integer(int64)|integer(int64)|
|tenantId||integer(int64)|integer(int64)|
|title||string||
|updateBy||integer(int64)|integer(int64)|
|updateTime||string(date-time)|string(date-time)|


**响应示例**:
```javascript
{
	"channelConfigId": 0,
	"content": "",
	"createAt": 0,
	"createBy": 0,
	"createDept": 0,
	"createTime": "",
	"id": 0,
	"tenantId": 0,
	"title": "",
	"updateBy": 0,
	"updateTime": ""
}
```


## 消息列表


**接口地址**:`/notify/message/getList`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": {
    "content": "",
    "createAt": 0,
    "createBy": 0,
    "createDept": 0,
    "createTime": "",
    "id": 0,
    "messageType": "",
    "status": true,
    "tenantId": 0,
    "updateAt": 0,
    "updateBy": 0,
    "updateTime": ""
  },
  "pageNum": 0,
  "pageSize": 0,
  "requestId": "",
  "sortMap": {}
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|request|request|body|true|PageRequest«NotifyMessage»|PageRequest«NotifyMessage»|
|&emsp;&emsp;data|||false|NotifyMessage|NotifyMessage|
|&emsp;&emsp;&emsp;&emsp;content|||false|string||
|&emsp;&emsp;&emsp;&emsp;createAt|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createDept|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createTime|||false|string||
|&emsp;&emsp;&emsp;&emsp;id|||false|integer||
|&emsp;&emsp;&emsp;&emsp;messageType|||false|string||
|&emsp;&emsp;&emsp;&emsp;status|||false|boolean||
|&emsp;&emsp;&emsp;&emsp;tenantId|||false|integer||
|&emsp;&emsp;&emsp;&emsp;updateAt|||false|integer||
|&emsp;&emsp;&emsp;&emsp;updateBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;updateTime|||false|string||
|&emsp;&emsp;pageNum|||false|integer(int32)||
|&emsp;&emsp;pageSize|||false|integer(int32)||
|&emsp;&emsp;requestId|||false|string||
|&emsp;&emsp;sortMap|||false|object||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|Paging«NotifyMessage»|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|rows||array|NotifyMessage|
|&emsp;&emsp;content||string||
|&emsp;&emsp;createAt||integer(int64)||
|&emsp;&emsp;createBy||integer(int64)||
|&emsp;&emsp;createDept||integer(int64)||
|&emsp;&emsp;createTime||string(date-time)||
|&emsp;&emsp;id||integer(int64)||
|&emsp;&emsp;messageType||string||
|&emsp;&emsp;status||boolean||
|&emsp;&emsp;tenantId||integer(int64)||
|&emsp;&emsp;updateAt||integer(int64)||
|&emsp;&emsp;updateBy||integer(int64)||
|&emsp;&emsp;updateTime||string(date-time)||
|total||integer(int64)|integer(int64)|


**响应示例**:
```javascript
{
	"rows": [
		{
			"content": "",
			"createAt": 0,
			"createBy": 0,
			"createDept": 0,
			"createTime": "",
			"id": 0,
			"messageType": "",
			"status": true,
			"tenantId": 0,
			"updateAt": 0,
			"updateBy": 0,
			"updateTime": ""
		}
	],
	"total": 0
}
```


# 用户信息


## 新增用户


**接口地址**:`/system/user/add`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": {
    "createBy": 0,
    "createDept": 0,
    "createTime": "",
    "deptId": 0,
    "email": "",
    "id": 0,
    "nickName": "",
    "password": "",
    "phonenumber": "",
    "postIds": [],
    "remark": "",
    "roleId": 0,
    "roleIds": [],
    "sex": "",
    "status": "",
    "updateBy": 0,
    "updateTime": "",
    "userName": "",
    "userType": ""
  },
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|reqUser|reqUser|body|true|Request«SysUserBo»|Request«SysUserBo»|
|&emsp;&emsp;data|||false|SysUserBo|SysUserBo|
|&emsp;&emsp;&emsp;&emsp;createBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createDept|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createTime|||false|string||
|&emsp;&emsp;&emsp;&emsp;deptId|||false|integer||
|&emsp;&emsp;&emsp;&emsp;email|||false|string||
|&emsp;&emsp;&emsp;&emsp;id|||false|integer||
|&emsp;&emsp;&emsp;&emsp;nickName|||false|string||
|&emsp;&emsp;&emsp;&emsp;password|||false|string||
|&emsp;&emsp;&emsp;&emsp;phonenumber|||false|string||
|&emsp;&emsp;&emsp;&emsp;postIds|||false|array|integer|
|&emsp;&emsp;&emsp;&emsp;remark|||false|string||
|&emsp;&emsp;&emsp;&emsp;roleId|||false|integer||
|&emsp;&emsp;&emsp;&emsp;roleIds|||false|array|integer|
|&emsp;&emsp;&emsp;&emsp;sex|||false|string||
|&emsp;&emsp;&emsp;&emsp;status|||false|string||
|&emsp;&emsp;&emsp;&emsp;updateBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;updateTime|||false|string||
|&emsp;&emsp;&emsp;&emsp;userName|||false|string||
|&emsp;&emsp;&emsp;&emsp;userType|||false|string||
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 用户授权角色


**接口地址**:`/system/user/authRole`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": {
    "createBy": 0,
    "createDept": 0,
    "createTime": "",
    "roleIds": [],
    "updateBy": 0,
    "updateTime": "",
    "userId": 0
  },
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|userRole|userRole|body|true|Request«SysUserRolesBo»|Request«SysUserRolesBo»|
|&emsp;&emsp;data|||false|SysUserRolesBo|SysUserRolesBo|
|&emsp;&emsp;&emsp;&emsp;createBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createDept|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createTime|||false|string||
|&emsp;&emsp;&emsp;&emsp;roleIds|||false|array|integer|
|&emsp;&emsp;&emsp;&emsp;updateBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;updateTime|||false|string||
|&emsp;&emsp;&emsp;&emsp;userId|||false|integer||
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 根据用户编号获取授权角色


**接口地址**:`/system/user/authRoleByUserId`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": 0,
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|bo|bo|body|true|Request«long»|Request«long»|
|&emsp;&emsp;data|||false|integer(int64)||
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|SysUserInfoVo|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|postIds||array||
|posts||array|SysPostVo|
|&emsp;&emsp;createTime||string(date-time)||
|&emsp;&emsp;id||integer(int64)||
|&emsp;&emsp;postCode||string||
|&emsp;&emsp;postName||string||
|&emsp;&emsp;postSort||integer(int32)||
|&emsp;&emsp;remark||string||
|&emsp;&emsp;status||string||
|roleIds||array||
|roles||array|SysRoleVo|
|&emsp;&emsp;createTime||string(date-time)||
|&emsp;&emsp;dataScope||string||
|&emsp;&emsp;deptCheckStrictly||boolean||
|&emsp;&emsp;flag||boolean||
|&emsp;&emsp;id||integer(int64)||
|&emsp;&emsp;menuCheckStrictly||boolean||
|&emsp;&emsp;remark||string||
|&emsp;&emsp;roleKey||string||
|&emsp;&emsp;roleName||string||
|&emsp;&emsp;roleSort||integer(int32)||
|&emsp;&emsp;status||string||
|&emsp;&emsp;superAdmin||boolean||
|user||SysUserVo|SysUserVo|
|&emsp;&emsp;avatar||integer(int64)||
|&emsp;&emsp;createTime||string(date-time)||
|&emsp;&emsp;dept||SysDeptVo|SysDeptVo|
|&emsp;&emsp;&emsp;&emsp;ancestors||string||
|&emsp;&emsp;&emsp;&emsp;createTime||string||
|&emsp;&emsp;&emsp;&emsp;deptName||string||
|&emsp;&emsp;&emsp;&emsp;email||string||
|&emsp;&emsp;&emsp;&emsp;id||integer||
|&emsp;&emsp;&emsp;&emsp;leader||string||
|&emsp;&emsp;&emsp;&emsp;orderNum||integer||
|&emsp;&emsp;&emsp;&emsp;parentId||integer||
|&emsp;&emsp;&emsp;&emsp;parentName||string||
|&emsp;&emsp;&emsp;&emsp;phone||string||
|&emsp;&emsp;&emsp;&emsp;status||string||
|&emsp;&emsp;deptId||integer(int64)||
|&emsp;&emsp;email||string||
|&emsp;&emsp;id||integer(int64)||
|&emsp;&emsp;loginDate||string(date-time)||
|&emsp;&emsp;loginIp||string||
|&emsp;&emsp;nickName||string||
|&emsp;&emsp;password||string||
|&emsp;&emsp;phonenumber||string||
|&emsp;&emsp;postIds||array|integer|
|&emsp;&emsp;remark||string||
|&emsp;&emsp;roleId||integer(int64)||
|&emsp;&emsp;roleIds||array|integer|
|&emsp;&emsp;roles||array|SysRoleVo|
|&emsp;&emsp;&emsp;&emsp;createTime||string||
|&emsp;&emsp;&emsp;&emsp;dataScope||string||
|&emsp;&emsp;&emsp;&emsp;deptCheckStrictly||boolean||
|&emsp;&emsp;&emsp;&emsp;flag||boolean||
|&emsp;&emsp;&emsp;&emsp;id||integer||
|&emsp;&emsp;&emsp;&emsp;menuCheckStrictly||boolean||
|&emsp;&emsp;&emsp;&emsp;remark||string||
|&emsp;&emsp;&emsp;&emsp;roleKey||string||
|&emsp;&emsp;&emsp;&emsp;roleName||string||
|&emsp;&emsp;&emsp;&emsp;roleSort||integer||
|&emsp;&emsp;&emsp;&emsp;status||string||
|&emsp;&emsp;&emsp;&emsp;superAdmin||boolean||
|&emsp;&emsp;sex||string||
|&emsp;&emsp;status||string||
|&emsp;&emsp;tenantId||integer(int64)||
|&emsp;&emsp;userName||string||
|&emsp;&emsp;userType||string||


**响应示例**:
```javascript
{
	"postIds": [],
	"posts": [
		{
			"createTime": "",
			"id": 0,
			"postCode": "",
			"postName": "",
			"postSort": 0,
			"remark": "",
			"status": ""
		}
	],
	"roleIds": [],
	"roles": [
		{
			"createTime": "",
			"dataScope": "",
			"deptCheckStrictly": true,
			"flag": true,
			"id": 0,
			"menuCheckStrictly": true,
			"remark": "",
			"roleKey": "",
			"roleName": "",
			"roleSort": 0,
			"status": "",
			"superAdmin": true
		}
	],
	"user": {
		"avatar": 0,
		"createTime": "",
		"dept": {
			"ancestors": "",
			"createTime": "",
			"deptName": "",
			"email": "",
			"id": 0,
			"leader": "",
			"orderNum": 0,
			"parentId": 0,
			"parentName": "",
			"phone": "",
			"status": ""
		},
		"deptId": 0,
		"email": "",
		"id": 0,
		"loginDate": "",
		"loginIp": "",
		"nickName": "",
		"password": "",
		"phonenumber": "",
		"postIds": [],
		"remark": "",
		"roleId": 0,
		"roleIds": [],
		"roles": [
			{
				"createTime": "",
				"dataScope": "",
				"deptCheckStrictly": true,
				"flag": true,
				"id": 0,
				"menuCheckStrictly": true,
				"remark": "",
				"roleKey": "",
				"roleName": "",
				"roleSort": 0,
				"status": "",
				"superAdmin": true
			}
		],
		"sex": "",
		"status": "",
		"tenantId": 0,
		"userName": "",
		"userType": ""
	}
}
```


## 状态修改


**接口地址**:`/system/user/changeStatus`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": {
    "createBy": 0,
    "createDept": 0,
    "createTime": "",
    "deptId": 0,
    "email": "",
    "id": 0,
    "nickName": "",
    "password": "",
    "phonenumber": "",
    "postIds": [],
    "remark": "",
    "roleId": 0,
    "roleIds": [],
    "sex": "",
    "status": "",
    "updateBy": 0,
    "updateTime": "",
    "userName": "",
    "userType": ""
  },
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|reqUser|reqUser|body|true|Request«SysUserBo»|Request«SysUserBo»|
|&emsp;&emsp;data|||false|SysUserBo|SysUserBo|
|&emsp;&emsp;&emsp;&emsp;createBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createDept|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createTime|||false|string||
|&emsp;&emsp;&emsp;&emsp;deptId|||false|integer||
|&emsp;&emsp;&emsp;&emsp;email|||false|string||
|&emsp;&emsp;&emsp;&emsp;id|||false|integer||
|&emsp;&emsp;&emsp;&emsp;nickName|||false|string||
|&emsp;&emsp;&emsp;&emsp;password|||false|string||
|&emsp;&emsp;&emsp;&emsp;phonenumber|||false|string||
|&emsp;&emsp;&emsp;&emsp;postIds|||false|array|integer|
|&emsp;&emsp;&emsp;&emsp;remark|||false|string||
|&emsp;&emsp;&emsp;&emsp;roleId|||false|integer||
|&emsp;&emsp;&emsp;&emsp;roleIds|||false|array|integer|
|&emsp;&emsp;&emsp;&emsp;sex|||false|string||
|&emsp;&emsp;&emsp;&emsp;status|||false|string||
|&emsp;&emsp;&emsp;&emsp;updateBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;updateTime|||false|string||
|&emsp;&emsp;&emsp;&emsp;userName|||false|string||
|&emsp;&emsp;&emsp;&emsp;userType|||false|string||
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 删除用户


**接口地址**:`/system/user/delete`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": [],
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|bo|bo|body|true|Request«List«long»»|Request«List«long»»|
|&emsp;&emsp;data|||false|array|integer|
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 获取部门树列表


**接口地址**:`/system/user/deptTree`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": {
    "createBy": 0,
    "createDept": 0,
    "createTime": "",
    "deptName": "",
    "email": "",
    "id": 0,
    "leader": "",
    "orderNum": 0,
    "parentId": 0,
    "phone": "",
    "status": "",
    "updateBy": 0,
    "updateTime": ""
  },
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|reqDept|reqDept|body|true|Request«SysDeptBo»|Request«SysDeptBo»|
|&emsp;&emsp;data|||false|SysDeptBo|SysDeptBo|
|&emsp;&emsp;&emsp;&emsp;createBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createDept|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createTime|||false|string||
|&emsp;&emsp;&emsp;&emsp;deptName|||false|string||
|&emsp;&emsp;&emsp;&emsp;email|||false|string||
|&emsp;&emsp;&emsp;&emsp;id|||false|integer||
|&emsp;&emsp;&emsp;&emsp;leader|||false|string||
|&emsp;&emsp;&emsp;&emsp;orderNum|||false|integer||
|&emsp;&emsp;&emsp;&emsp;parentId|||false|integer||
|&emsp;&emsp;&emsp;&emsp;phone|||false|string||
|&emsp;&emsp;&emsp;&emsp;status|||false|string||
|&emsp;&emsp;&emsp;&emsp;updateBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;updateTime|||false|string||
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|Tree«long»|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


暂无


**响应示例**:
```javascript
[
	null
]
```


## 修改用户


**接口地址**:`/system/user/edit`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": {
    "createBy": 0,
    "createDept": 0,
    "createTime": "",
    "deptId": 0,
    "email": "",
    "id": 0,
    "nickName": "",
    "password": "",
    "phonenumber": "",
    "postIds": [],
    "remark": "",
    "roleId": 0,
    "roleIds": [],
    "sex": "",
    "status": "",
    "updateBy": 0,
    "updateTime": "",
    "userName": "",
    "userType": ""
  },
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|reqUser|reqUser|body|true|Request«SysUserBo»|Request«SysUserBo»|
|&emsp;&emsp;data|||false|SysUserBo|SysUserBo|
|&emsp;&emsp;&emsp;&emsp;createBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createDept|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createTime|||false|string||
|&emsp;&emsp;&emsp;&emsp;deptId|||false|integer||
|&emsp;&emsp;&emsp;&emsp;email|||false|string||
|&emsp;&emsp;&emsp;&emsp;id|||false|integer||
|&emsp;&emsp;&emsp;&emsp;nickName|||false|string||
|&emsp;&emsp;&emsp;&emsp;password|||false|string||
|&emsp;&emsp;&emsp;&emsp;phonenumber|||false|string||
|&emsp;&emsp;&emsp;&emsp;postIds|||false|array|integer|
|&emsp;&emsp;&emsp;&emsp;remark|||false|string||
|&emsp;&emsp;&emsp;&emsp;roleId|||false|integer||
|&emsp;&emsp;&emsp;&emsp;roleIds|||false|array|integer|
|&emsp;&emsp;&emsp;&emsp;sex|||false|string||
|&emsp;&emsp;&emsp;&emsp;status|||false|string||
|&emsp;&emsp;&emsp;&emsp;updateBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;updateTime|||false|string||
|&emsp;&emsp;&emsp;&emsp;userName|||false|string||
|&emsp;&emsp;&emsp;&emsp;userType|||false|string||
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 导出用户列表


**接口地址**:`/system/user/export`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|createBy||query|false|integer(int64)||
|createDept||query|false|integer(int64)||
|createTime||query|false|string(date-time)||
|deptId||query|false|integer(int64)||
|email||query|false|string||
|id||query|false|integer(int64)||
|nickName||query|false|string||
|password||query|false|string||
|phonenumber||query|false|string||
|postIds||query|false|array|integer|
|remark||query|false|string||
|roleId||query|false|integer(int64)||
|roleIds||query|false|array|integer|
|sex||query|false|string||
|status||query|false|string||
|superAdmin||query|false|boolean||
|updateBy||query|false|integer(int64)||
|updateTime||query|false|string(date-time)||
|userName||query|false|string||
|userType||query|false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 根据用户编号获取详细信息


**接口地址**:`/system/user/getDetail`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": 0,
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|req|req|body|true|Request«long»|Request«long»|
|&emsp;&emsp;data|||false|integer(int64)||
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|SysUserInfoVo|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|postIds||array||
|posts||array|SysPostVo|
|&emsp;&emsp;createTime||string(date-time)||
|&emsp;&emsp;id||integer(int64)||
|&emsp;&emsp;postCode||string||
|&emsp;&emsp;postName||string||
|&emsp;&emsp;postSort||integer(int32)||
|&emsp;&emsp;remark||string||
|&emsp;&emsp;status||string||
|roleIds||array||
|roles||array|SysRoleVo|
|&emsp;&emsp;createTime||string(date-time)||
|&emsp;&emsp;dataScope||string||
|&emsp;&emsp;deptCheckStrictly||boolean||
|&emsp;&emsp;flag||boolean||
|&emsp;&emsp;id||integer(int64)||
|&emsp;&emsp;menuCheckStrictly||boolean||
|&emsp;&emsp;remark||string||
|&emsp;&emsp;roleKey||string||
|&emsp;&emsp;roleName||string||
|&emsp;&emsp;roleSort||integer(int32)||
|&emsp;&emsp;status||string||
|&emsp;&emsp;superAdmin||boolean||
|user||SysUserVo|SysUserVo|
|&emsp;&emsp;avatar||integer(int64)||
|&emsp;&emsp;createTime||string(date-time)||
|&emsp;&emsp;dept||SysDeptVo|SysDeptVo|
|&emsp;&emsp;&emsp;&emsp;ancestors||string||
|&emsp;&emsp;&emsp;&emsp;createTime||string||
|&emsp;&emsp;&emsp;&emsp;deptName||string||
|&emsp;&emsp;&emsp;&emsp;email||string||
|&emsp;&emsp;&emsp;&emsp;id||integer||
|&emsp;&emsp;&emsp;&emsp;leader||string||
|&emsp;&emsp;&emsp;&emsp;orderNum||integer||
|&emsp;&emsp;&emsp;&emsp;parentId||integer||
|&emsp;&emsp;&emsp;&emsp;parentName||string||
|&emsp;&emsp;&emsp;&emsp;phone||string||
|&emsp;&emsp;&emsp;&emsp;status||string||
|&emsp;&emsp;deptId||integer(int64)||
|&emsp;&emsp;email||string||
|&emsp;&emsp;id||integer(int64)||
|&emsp;&emsp;loginDate||string(date-time)||
|&emsp;&emsp;loginIp||string||
|&emsp;&emsp;nickName||string||
|&emsp;&emsp;password||string||
|&emsp;&emsp;phonenumber||string||
|&emsp;&emsp;postIds||array|integer|
|&emsp;&emsp;remark||string||
|&emsp;&emsp;roleId||integer(int64)||
|&emsp;&emsp;roleIds||array|integer|
|&emsp;&emsp;roles||array|SysRoleVo|
|&emsp;&emsp;&emsp;&emsp;createTime||string||
|&emsp;&emsp;&emsp;&emsp;dataScope||string||
|&emsp;&emsp;&emsp;&emsp;deptCheckStrictly||boolean||
|&emsp;&emsp;&emsp;&emsp;flag||boolean||
|&emsp;&emsp;&emsp;&emsp;id||integer||
|&emsp;&emsp;&emsp;&emsp;menuCheckStrictly||boolean||
|&emsp;&emsp;&emsp;&emsp;remark||string||
|&emsp;&emsp;&emsp;&emsp;roleKey||string||
|&emsp;&emsp;&emsp;&emsp;roleName||string||
|&emsp;&emsp;&emsp;&emsp;roleSort||integer||
|&emsp;&emsp;&emsp;&emsp;status||string||
|&emsp;&emsp;&emsp;&emsp;superAdmin||boolean||
|&emsp;&emsp;sex||string||
|&emsp;&emsp;status||string||
|&emsp;&emsp;tenantId||integer(int64)||
|&emsp;&emsp;userName||string||
|&emsp;&emsp;userType||string||


**响应示例**:
```javascript
{
	"postIds": [],
	"posts": [
		{
			"createTime": "",
			"id": 0,
			"postCode": "",
			"postName": "",
			"postSort": 0,
			"remark": "",
			"status": ""
		}
	],
	"roleIds": [],
	"roles": [
		{
			"createTime": "",
			"dataScope": "",
			"deptCheckStrictly": true,
			"flag": true,
			"id": 0,
			"menuCheckStrictly": true,
			"remark": "",
			"roleKey": "",
			"roleName": "",
			"roleSort": 0,
			"status": "",
			"superAdmin": true
		}
	],
	"user": {
		"avatar": 0,
		"createTime": "",
		"dept": {
			"ancestors": "",
			"createTime": "",
			"deptName": "",
			"email": "",
			"id": 0,
			"leader": "",
			"orderNum": 0,
			"parentId": 0,
			"parentName": "",
			"phone": "",
			"status": ""
		},
		"deptId": 0,
		"email": "",
		"id": 0,
		"loginDate": "",
		"loginIp": "",
		"nickName": "",
		"password": "",
		"phonenumber": "",
		"postIds": [],
		"remark": "",
		"roleId": 0,
		"roleIds": [],
		"roles": [
			{
				"createTime": "",
				"dataScope": "",
				"deptCheckStrictly": true,
				"flag": true,
				"id": 0,
				"menuCheckStrictly": true,
				"remark": "",
				"roleKey": "",
				"roleName": "",
				"roleSort": 0,
				"status": "",
				"superAdmin": true
			}
		],
		"sex": "",
		"status": "",
		"tenantId": 0,
		"userName": "",
		"userType": ""
	}
}
```


## 获取用户信息


**接口地址**:`/system/user/getInfo`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


暂无


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|UserInfoVo|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|permissions||array||
|roles||array||
|user||SysUserVo|SysUserVo|
|&emsp;&emsp;avatar||integer(int64)||
|&emsp;&emsp;createTime||string(date-time)||
|&emsp;&emsp;dept||SysDeptVo|SysDeptVo|
|&emsp;&emsp;&emsp;&emsp;ancestors||string||
|&emsp;&emsp;&emsp;&emsp;createTime||string||
|&emsp;&emsp;&emsp;&emsp;deptName||string||
|&emsp;&emsp;&emsp;&emsp;email||string||
|&emsp;&emsp;&emsp;&emsp;id||integer||
|&emsp;&emsp;&emsp;&emsp;leader||string||
|&emsp;&emsp;&emsp;&emsp;orderNum||integer||
|&emsp;&emsp;&emsp;&emsp;parentId||integer||
|&emsp;&emsp;&emsp;&emsp;parentName||string||
|&emsp;&emsp;&emsp;&emsp;phone||string||
|&emsp;&emsp;&emsp;&emsp;status||string||
|&emsp;&emsp;deptId||integer(int64)||
|&emsp;&emsp;email||string||
|&emsp;&emsp;id||integer(int64)||
|&emsp;&emsp;loginDate||string(date-time)||
|&emsp;&emsp;loginIp||string||
|&emsp;&emsp;nickName||string||
|&emsp;&emsp;password||string||
|&emsp;&emsp;phonenumber||string||
|&emsp;&emsp;postIds||array|integer|
|&emsp;&emsp;remark||string||
|&emsp;&emsp;roleId||integer(int64)||
|&emsp;&emsp;roleIds||array|integer|
|&emsp;&emsp;roles||array|SysRoleVo|
|&emsp;&emsp;&emsp;&emsp;createTime||string||
|&emsp;&emsp;&emsp;&emsp;dataScope||string||
|&emsp;&emsp;&emsp;&emsp;deptCheckStrictly||boolean||
|&emsp;&emsp;&emsp;&emsp;flag||boolean||
|&emsp;&emsp;&emsp;&emsp;id||integer||
|&emsp;&emsp;&emsp;&emsp;menuCheckStrictly||boolean||
|&emsp;&emsp;&emsp;&emsp;remark||string||
|&emsp;&emsp;&emsp;&emsp;roleKey||string||
|&emsp;&emsp;&emsp;&emsp;roleName||string||
|&emsp;&emsp;&emsp;&emsp;roleSort||integer||
|&emsp;&emsp;&emsp;&emsp;status||string||
|&emsp;&emsp;&emsp;&emsp;superAdmin||boolean||
|&emsp;&emsp;sex||string||
|&emsp;&emsp;status||string||
|&emsp;&emsp;tenantId||integer(int64)||
|&emsp;&emsp;userName||string||
|&emsp;&emsp;userType||string||


**响应示例**:
```javascript
{
	"permissions": [],
	"roles": [],
	"user": {
		"avatar": 0,
		"createTime": "",
		"dept": {
			"ancestors": "",
			"createTime": "",
			"deptName": "",
			"email": "",
			"id": 0,
			"leader": "",
			"orderNum": 0,
			"parentId": 0,
			"parentName": "",
			"phone": "",
			"status": ""
		},
		"deptId": 0,
		"email": "",
		"id": 0,
		"loginDate": "",
		"loginIp": "",
		"nickName": "",
		"password": "",
		"phonenumber": "",
		"postIds": [],
		"remark": "",
		"roleId": 0,
		"roleIds": [],
		"roles": [
			{
				"createTime": "",
				"dataScope": "",
				"deptCheckStrictly": true,
				"flag": true,
				"id": 0,
				"menuCheckStrictly": true,
				"remark": "",
				"roleKey": "",
				"roleName": "",
				"roleSort": 0,
				"status": "",
				"superAdmin": true
			}
		],
		"sex": "",
		"status": "",
		"tenantId": 0,
		"userName": "",
		"userType": ""
	}
}
```


## 导入数据


**接口地址**:`/system/user/importData`


**请求方式**:`POST`


**请求数据类型**:`multipart/form-data`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|file|file|formData|true|file||
|updateSupport|updateSupport|formData|false|boolean||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 获取导入模板


**接口地址**:`/system/user/importTemplate`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


暂无


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 获取用户列表


**接口地址**:`/system/user/list`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": {
    "createBy": 0,
    "createDept": 0,
    "createTime": "",
    "deptId": 0,
    "email": "",
    "id": 0,
    "nickName": "",
    "password": "",
    "phonenumber": "",
    "postIds": [],
    "remark": "",
    "roleId": 0,
    "roleIds": [],
    "sex": "",
    "status": "",
    "updateBy": 0,
    "updateTime": "",
    "userName": "",
    "userType": ""
  },
  "pageNum": 0,
  "pageSize": 0,
  "requestId": "",
  "sortMap": {}
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|query|query|body|true|PageRequest«SysUserBo»|PageRequest«SysUserBo»|
|&emsp;&emsp;data|||false|SysUserBo|SysUserBo|
|&emsp;&emsp;&emsp;&emsp;createBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createDept|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createTime|||false|string||
|&emsp;&emsp;&emsp;&emsp;deptId|||false|integer||
|&emsp;&emsp;&emsp;&emsp;email|||false|string||
|&emsp;&emsp;&emsp;&emsp;id|||false|integer||
|&emsp;&emsp;&emsp;&emsp;nickName|||false|string||
|&emsp;&emsp;&emsp;&emsp;password|||false|string||
|&emsp;&emsp;&emsp;&emsp;phonenumber|||false|string||
|&emsp;&emsp;&emsp;&emsp;postIds|||false|array|integer|
|&emsp;&emsp;&emsp;&emsp;remark|||false|string||
|&emsp;&emsp;&emsp;&emsp;roleId|||false|integer||
|&emsp;&emsp;&emsp;&emsp;roleIds|||false|array|integer|
|&emsp;&emsp;&emsp;&emsp;sex|||false|string||
|&emsp;&emsp;&emsp;&emsp;status|||false|string||
|&emsp;&emsp;&emsp;&emsp;updateBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;updateTime|||false|string||
|&emsp;&emsp;&emsp;&emsp;userName|||false|string||
|&emsp;&emsp;&emsp;&emsp;userType|||false|string||
|&emsp;&emsp;pageNum|||false|integer(int32)||
|&emsp;&emsp;pageSize|||false|integer(int32)||
|&emsp;&emsp;requestId|||false|string||
|&emsp;&emsp;sortMap|||false|object||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|Paging«SysUserVo»|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|rows||array|SysUserVo|
|&emsp;&emsp;avatar||integer(int64)||
|&emsp;&emsp;createTime||string(date-time)||
|&emsp;&emsp;dept||SysDeptVo|SysDeptVo|
|&emsp;&emsp;&emsp;&emsp;ancestors||string||
|&emsp;&emsp;&emsp;&emsp;createTime||string||
|&emsp;&emsp;&emsp;&emsp;deptName||string||
|&emsp;&emsp;&emsp;&emsp;email||string||
|&emsp;&emsp;&emsp;&emsp;id||integer||
|&emsp;&emsp;&emsp;&emsp;leader||string||
|&emsp;&emsp;&emsp;&emsp;orderNum||integer||
|&emsp;&emsp;&emsp;&emsp;parentId||integer||
|&emsp;&emsp;&emsp;&emsp;parentName||string||
|&emsp;&emsp;&emsp;&emsp;phone||string||
|&emsp;&emsp;&emsp;&emsp;status||string||
|&emsp;&emsp;deptId||integer(int64)||
|&emsp;&emsp;email||string||
|&emsp;&emsp;id||integer(int64)||
|&emsp;&emsp;loginDate||string(date-time)||
|&emsp;&emsp;loginIp||string||
|&emsp;&emsp;nickName||string||
|&emsp;&emsp;password||string||
|&emsp;&emsp;phonenumber||string||
|&emsp;&emsp;postIds||array|integer|
|&emsp;&emsp;remark||string||
|&emsp;&emsp;roleId||integer(int64)||
|&emsp;&emsp;roleIds||array|integer|
|&emsp;&emsp;roles||array|SysRoleVo|
|&emsp;&emsp;&emsp;&emsp;createTime||string||
|&emsp;&emsp;&emsp;&emsp;dataScope||string||
|&emsp;&emsp;&emsp;&emsp;deptCheckStrictly||boolean||
|&emsp;&emsp;&emsp;&emsp;flag||boolean||
|&emsp;&emsp;&emsp;&emsp;id||integer||
|&emsp;&emsp;&emsp;&emsp;menuCheckStrictly||boolean||
|&emsp;&emsp;&emsp;&emsp;remark||string||
|&emsp;&emsp;&emsp;&emsp;roleKey||string||
|&emsp;&emsp;&emsp;&emsp;roleName||string||
|&emsp;&emsp;&emsp;&emsp;roleSort||integer||
|&emsp;&emsp;&emsp;&emsp;status||string||
|&emsp;&emsp;&emsp;&emsp;superAdmin||boolean||
|&emsp;&emsp;sex||string||
|&emsp;&emsp;status||string||
|&emsp;&emsp;tenantId||integer(int64)||
|&emsp;&emsp;userName||string||
|&emsp;&emsp;userType||string||
|total||integer(int64)|integer(int64)|


**响应示例**:
```javascript
{
	"rows": [
		{
			"avatar": 0,
			"createTime": "",
			"dept": {
				"ancestors": "",
				"createTime": "",
				"deptName": "",
				"email": "",
				"id": 0,
				"leader": "",
				"orderNum": 0,
				"parentId": 0,
				"parentName": "",
				"phone": "",
				"status": ""
			},
			"deptId": 0,
			"email": "",
			"id": 0,
			"loginDate": "",
			"loginIp": "",
			"nickName": "",
			"password": "",
			"phonenumber": "",
			"postIds": [],
			"remark": "",
			"roleId": 0,
			"roleIds": [],
			"roles": [
				{
					"createTime": "",
					"dataScope": "",
					"deptCheckStrictly": true,
					"flag": true,
					"id": 0,
					"menuCheckStrictly": true,
					"remark": "",
					"roleKey": "",
					"roleName": "",
					"roleSort": 0,
					"status": "",
					"superAdmin": true
				}
			],
			"sex": "",
			"status": "",
			"tenantId": 0,
			"userName": "",
			"userType": ""
		}
	],
	"total": 0
}
```


## 重置密码


**接口地址**:`/system/user/resetPwd`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": {
    "createBy": 0,
    "createDept": 0,
    "createTime": "",
    "deptId": 0,
    "email": "",
    "id": 0,
    "nickName": "",
    "password": "",
    "phonenumber": "",
    "postIds": [],
    "remark": "",
    "roleId": 0,
    "roleIds": [],
    "sex": "",
    "status": "",
    "updateBy": 0,
    "updateTime": "",
    "userName": "",
    "userType": ""
  },
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|reqUser|reqUser|body|true|Request«SysUserBo»|Request«SysUserBo»|
|&emsp;&emsp;data|||false|SysUserBo|SysUserBo|
|&emsp;&emsp;&emsp;&emsp;createBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createDept|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createTime|||false|string||
|&emsp;&emsp;&emsp;&emsp;deptId|||false|integer||
|&emsp;&emsp;&emsp;&emsp;email|||false|string||
|&emsp;&emsp;&emsp;&emsp;id|||false|integer||
|&emsp;&emsp;&emsp;&emsp;nickName|||false|string||
|&emsp;&emsp;&emsp;&emsp;password|||false|string||
|&emsp;&emsp;&emsp;&emsp;phonenumber|||false|string||
|&emsp;&emsp;&emsp;&emsp;postIds|||false|array|integer|
|&emsp;&emsp;&emsp;&emsp;remark|||false|string||
|&emsp;&emsp;&emsp;&emsp;roleId|||false|integer||
|&emsp;&emsp;&emsp;&emsp;roleIds|||false|array|integer|
|&emsp;&emsp;&emsp;&emsp;sex|||false|string||
|&emsp;&emsp;&emsp;&emsp;status|||false|string||
|&emsp;&emsp;&emsp;&emsp;updateBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;updateTime|||false|string||
|&emsp;&emsp;&emsp;&emsp;userName|||false|string||
|&emsp;&emsp;&emsp;&emsp;userType|||false|string||
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


暂无


**响应示例**:
```javascript

```


# 用户在线监控


## 强退用户


**接口地址**:`/monitor/online/kickoutByTokenValue`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": "",
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|bo|bo|body|true|Request«string»|Request«string»|
|&emsp;&emsp;data|||false|string||
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 获取在线用户监控列表


**接口地址**:`/monitor/online/list`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": {
    "browser": "",
    "deptName": "",
    "ipaddr": "",
    "loginLocation": "",
    "loginTime": 0,
    "os": "",
    "tokenId": "",
    "userName": ""
  },
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|request|request|body|true|Request«SysUserOnline»|Request«SysUserOnline»|
|&emsp;&emsp;data|||false|SysUserOnline|SysUserOnline|
|&emsp;&emsp;&emsp;&emsp;browser|||false|string||
|&emsp;&emsp;&emsp;&emsp;deptName|||false|string||
|&emsp;&emsp;&emsp;&emsp;ipaddr|||false|string||
|&emsp;&emsp;&emsp;&emsp;loginLocation|||false|string||
|&emsp;&emsp;&emsp;&emsp;loginTime|||false|integer||
|&emsp;&emsp;&emsp;&emsp;os|||false|string||
|&emsp;&emsp;&emsp;&emsp;tokenId|||false|string||
|&emsp;&emsp;&emsp;&emsp;userName|||false|string||
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|Paging«SysUserOnline»|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|rows||array|SysUserOnline|
|&emsp;&emsp;browser||string||
|&emsp;&emsp;deptName||string||
|&emsp;&emsp;ipaddr||string||
|&emsp;&emsp;loginLocation||string||
|&emsp;&emsp;loginTime||integer(int64)||
|&emsp;&emsp;os||string||
|&emsp;&emsp;tokenId||string||
|&emsp;&emsp;userName||string||
|total||integer(int64)|integer(int64)|


**响应示例**:
```javascript
{
	"rows": [
		{
			"browser": "",
			"deptName": "",
			"ipaddr": "",
			"loginLocation": "",
			"loginTime": 0,
			"os": "",
			"tokenId": "",
			"userName": ""
		}
	],
	"total": 0
}
```


# 租户管理


## 新增租户


**接口地址**:`/system/tenant/add`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": {
    "accountCount": 0,
    "address": "",
    "companyName": "",
    "contactPhone": "",
    "contactUserName": "",
    "createBy": 0,
    "createDept": 0,
    "createTime": "",
    "domain": "",
    "expireTime": "",
    "id": 0,
    "intro": "",
    "licenseNumber": "",
    "packageId": 0,
    "password": "",
    "remark": "",
    "status": "",
    "tenantId": 0,
    "updateBy": 0,
    "updateTime": "",
    "username": ""
  },
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|bo|bo|body|true|Request«SysTenantBo»|Request«SysTenantBo»|
|&emsp;&emsp;data|||false|SysTenantBo|SysTenantBo|
|&emsp;&emsp;&emsp;&emsp;accountCount|||false|integer||
|&emsp;&emsp;&emsp;&emsp;address|||false|string||
|&emsp;&emsp;&emsp;&emsp;companyName|||false|string||
|&emsp;&emsp;&emsp;&emsp;contactPhone|||false|string||
|&emsp;&emsp;&emsp;&emsp;contactUserName|||false|string||
|&emsp;&emsp;&emsp;&emsp;createBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createDept|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createTime|||false|string||
|&emsp;&emsp;&emsp;&emsp;domain|||false|string||
|&emsp;&emsp;&emsp;&emsp;expireTime|||false|string||
|&emsp;&emsp;&emsp;&emsp;id|||false|integer||
|&emsp;&emsp;&emsp;&emsp;intro|||false|string||
|&emsp;&emsp;&emsp;&emsp;licenseNumber|||false|string||
|&emsp;&emsp;&emsp;&emsp;packageId|||false|integer||
|&emsp;&emsp;&emsp;&emsp;password|||false|string||
|&emsp;&emsp;&emsp;&emsp;remark|||false|string||
|&emsp;&emsp;&emsp;&emsp;status|||false|string||
|&emsp;&emsp;&emsp;&emsp;tenantId|||false|integer||
|&emsp;&emsp;&emsp;&emsp;updateBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;updateTime|||false|string||
|&emsp;&emsp;&emsp;&emsp;username|||false|string||
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 删除租户


**接口地址**:`/system/tenant/delete`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": 0,
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|bo|bo|body|true|Request«long»|Request«long»|
|&emsp;&emsp;data|||false|integer(int64)||
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 动态切换租户


**接口地址**:`/system/tenant/dynamic`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": 0,
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|bo|bo|body|true|Request«long»|Request«long»|
|&emsp;&emsp;data|||false|integer(int64)||
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 清除动态租户


**接口地址**:`/system/tenant/dynamic/clear`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


暂无


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 修改租户


**接口地址**:`/system/tenant/edit`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": {
    "accountCount": 0,
    "address": "",
    "companyName": "",
    "contactPhone": "",
    "contactUserName": "",
    "createBy": 0,
    "createDept": 0,
    "createTime": "",
    "domain": "",
    "expireTime": "",
    "id": 0,
    "intro": "",
    "licenseNumber": "",
    "packageId": 0,
    "password": "",
    "remark": "",
    "status": "",
    "tenantId": 0,
    "updateBy": 0,
    "updateTime": "",
    "username": ""
  },
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|bo|bo|body|true|Request«SysTenantBo»|Request«SysTenantBo»|
|&emsp;&emsp;data|||false|SysTenantBo|SysTenantBo|
|&emsp;&emsp;&emsp;&emsp;accountCount|||false|integer||
|&emsp;&emsp;&emsp;&emsp;address|||false|string||
|&emsp;&emsp;&emsp;&emsp;companyName|||false|string||
|&emsp;&emsp;&emsp;&emsp;contactPhone|||false|string||
|&emsp;&emsp;&emsp;&emsp;contactUserName|||false|string||
|&emsp;&emsp;&emsp;&emsp;createBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createDept|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createTime|||false|string||
|&emsp;&emsp;&emsp;&emsp;domain|||false|string||
|&emsp;&emsp;&emsp;&emsp;expireTime|||false|string||
|&emsp;&emsp;&emsp;&emsp;id|||false|integer||
|&emsp;&emsp;&emsp;&emsp;intro|||false|string||
|&emsp;&emsp;&emsp;&emsp;licenseNumber|||false|string||
|&emsp;&emsp;&emsp;&emsp;packageId|||false|integer||
|&emsp;&emsp;&emsp;&emsp;password|||false|string||
|&emsp;&emsp;&emsp;&emsp;remark|||false|string||
|&emsp;&emsp;&emsp;&emsp;status|||false|string||
|&emsp;&emsp;&emsp;&emsp;tenantId|||false|integer||
|&emsp;&emsp;&emsp;&emsp;updateBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;updateTime|||false|string||
|&emsp;&emsp;&emsp;&emsp;username|||false|string||
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 导出租户列表


**接口地址**:`/system/tenant/export`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|accountCount||query|false|integer(int64)||
|address||query|false|string||
|companyName||query|false|string||
|contactPhone||query|false|string||
|contactUserName||query|false|string||
|createBy||query|false|integer(int64)||
|createDept||query|false|integer(int64)||
|createTime||query|false|string(date-time)||
|domain||query|false|string||
|expireTime||query|false|string(date-time)||
|id||query|false|integer(int64)||
|intro||query|false|string||
|licenseNumber||query|false|string||
|packageId||query|false|integer(int64)||
|password||query|false|string||
|remark||query|false|string||
|status||query|false|string||
|tenantId||query|false|integer(int64)||
|updateBy||query|false|integer(int64)||
|updateTime||query|false|string(date-time)||
|username||query|false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 获取租户详细信息


**接口地址**:`/system/tenant/getDetail`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": 0,
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|bo|bo|body|true|Request«long»|Request«long»|
|&emsp;&emsp;data|||false|integer(int64)||
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|SysTenantVo|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|accountCount||integer(int64)|integer(int64)|
|address||string||
|companyName||string||
|contactPhone||string||
|contactUserName||string||
|createBy||integer(int64)|integer(int64)|
|createDept||integer(int64)|integer(int64)|
|createTime||string(date-time)|string(date-time)|
|domain||string||
|expireTime||string(date-time)|string(date-time)|
|id||integer(int64)|integer(int64)|
|intro||string||
|licenseNumber||string||
|packageId||integer(int64)|integer(int64)|
|remark||string||
|status||string||
|tenantId||integer(int64)|integer(int64)|
|updateBy||integer(int64)|integer(int64)|
|updateTime||string(date-time)|string(date-time)|


**响应示例**:
```javascript
{
	"accountCount": 0,
	"address": "",
	"companyName": "",
	"contactPhone": "",
	"contactUserName": "",
	"createBy": 0,
	"createDept": 0,
	"createTime": "",
	"domain": "",
	"expireTime": "",
	"id": 0,
	"intro": "",
	"licenseNumber": "",
	"packageId": 0,
	"remark": "",
	"status": "",
	"tenantId": 0,
	"updateBy": 0,
	"updateTime": ""
}
```


## 查询租户列表


**接口地址**:`/system/tenant/list`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": {
    "accountCount": 0,
    "address": "",
    "companyName": "",
    "contactPhone": "",
    "contactUserName": "",
    "createBy": 0,
    "createDept": 0,
    "createTime": "",
    "domain": "",
    "expireTime": "",
    "id": 0,
    "intro": "",
    "licenseNumber": "",
    "packageId": 0,
    "password": "",
    "remark": "",
    "status": "",
    "tenantId": 0,
    "updateBy": 0,
    "updateTime": "",
    "username": ""
  },
  "pageNum": 0,
  "pageSize": 0,
  "requestId": "",
  "sortMap": {}
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|query|query|body|true|PageRequest«SysTenantBo»|PageRequest«SysTenantBo»|
|&emsp;&emsp;data|||false|SysTenantBo|SysTenantBo|
|&emsp;&emsp;&emsp;&emsp;accountCount|||false|integer||
|&emsp;&emsp;&emsp;&emsp;address|||false|string||
|&emsp;&emsp;&emsp;&emsp;companyName|||false|string||
|&emsp;&emsp;&emsp;&emsp;contactPhone|||false|string||
|&emsp;&emsp;&emsp;&emsp;contactUserName|||false|string||
|&emsp;&emsp;&emsp;&emsp;createBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createDept|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createTime|||false|string||
|&emsp;&emsp;&emsp;&emsp;domain|||false|string||
|&emsp;&emsp;&emsp;&emsp;expireTime|||false|string||
|&emsp;&emsp;&emsp;&emsp;id|||false|integer||
|&emsp;&emsp;&emsp;&emsp;intro|||false|string||
|&emsp;&emsp;&emsp;&emsp;licenseNumber|||false|string||
|&emsp;&emsp;&emsp;&emsp;packageId|||false|integer||
|&emsp;&emsp;&emsp;&emsp;password|||false|string||
|&emsp;&emsp;&emsp;&emsp;remark|||false|string||
|&emsp;&emsp;&emsp;&emsp;status|||false|string||
|&emsp;&emsp;&emsp;&emsp;tenantId|||false|integer||
|&emsp;&emsp;&emsp;&emsp;updateBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;updateTime|||false|string||
|&emsp;&emsp;&emsp;&emsp;username|||false|string||
|&emsp;&emsp;pageNum|||false|integer(int32)||
|&emsp;&emsp;pageSize|||false|integer(int32)||
|&emsp;&emsp;requestId|||false|string||
|&emsp;&emsp;sortMap|||false|object||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|Paging«SysTenantVo»|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|rows||array|SysTenantVo|
|&emsp;&emsp;accountCount||integer(int64)||
|&emsp;&emsp;address||string||
|&emsp;&emsp;companyName||string||
|&emsp;&emsp;contactPhone||string||
|&emsp;&emsp;contactUserName||string||
|&emsp;&emsp;createBy||integer(int64)||
|&emsp;&emsp;createDept||integer(int64)||
|&emsp;&emsp;createTime||string(date-time)||
|&emsp;&emsp;domain||string||
|&emsp;&emsp;expireTime||string(date-time)||
|&emsp;&emsp;id||integer(int64)||
|&emsp;&emsp;intro||string||
|&emsp;&emsp;licenseNumber||string||
|&emsp;&emsp;packageId||integer(int64)||
|&emsp;&emsp;remark||string||
|&emsp;&emsp;status||string||
|&emsp;&emsp;tenantId||integer(int64)||
|&emsp;&emsp;updateBy||integer(int64)||
|&emsp;&emsp;updateTime||string(date-time)||
|total||integer(int64)|integer(int64)|


**响应示例**:
```javascript
{
	"rows": [
		{
			"accountCount": 0,
			"address": "",
			"companyName": "",
			"contactPhone": "",
			"contactUserName": "",
			"createBy": 0,
			"createDept": 0,
			"createTime": "",
			"domain": "",
			"expireTime": "",
			"id": 0,
			"intro": "",
			"licenseNumber": "",
			"packageId": 0,
			"remark": "",
			"status": "",
			"tenantId": 0,
			"updateBy": 0,
			"updateTime": ""
		}
	],
	"total": 0
}
```


## 同步租户套餐


**接口地址**:`/system/tenant/syncTenantPackage`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|packageId|packageId|body|false|string||
|tenantId|tenantId|body|false|integer||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


暂无


**响应示例**:
```javascript

```


# 空间设备


## 设备日志


**接口地址**:`/space/deviceLogs`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": {
    "createBy": 0,
    "createDept": 0,
    "createTime": "",
    "deviceId": "",
    "identifier": "",
    "type": "",
    "updateBy": 0,
    "updateTime": ""
  },
  "pageNum": 0,
  "pageSize": 0,
  "requestId": "",
  "sortMap": {}
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|request|request|body|true|PageRequest«DeviceLogQueryBo»|PageRequest«DeviceLogQueryBo»|
|&emsp;&emsp;data|||false|DeviceLogQueryBo|DeviceLogQueryBo|
|&emsp;&emsp;&emsp;&emsp;createBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createDept|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createTime|||false|string||
|&emsp;&emsp;&emsp;&emsp;deviceId|设备id||false|string||
|&emsp;&emsp;&emsp;&emsp;identifier|属性名||false|string||
|&emsp;&emsp;&emsp;&emsp;type|类型||false|string||
|&emsp;&emsp;&emsp;&emsp;updateBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;updateTime|||false|string||
|&emsp;&emsp;pageNum|||false|integer(int32)||
|&emsp;&emsp;pageSize|||false|integer(int32)||
|&emsp;&emsp;requestId|||false|string||
|&emsp;&emsp;sortMap|||false|object||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|Paging«ThingModelMessage»|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|rows||array|ThingModelMessage|
|&emsp;&emsp;code||integer(int32)||
|&emsp;&emsp;data||object||
|&emsp;&emsp;deviceId||string||
|&emsp;&emsp;deviceName||string||
|&emsp;&emsp;id||string||
|&emsp;&emsp;identifier||string||
|&emsp;&emsp;mid||string||
|&emsp;&emsp;occurred||integer(int64)||
|&emsp;&emsp;productKey||string||
|&emsp;&emsp;time||integer(int64)||
|&emsp;&emsp;type||string||
|&emsp;&emsp;uid||string||
|total||integer(int64)|integer(int64)|


**响应示例**:
```javascript
{
	"rows": [
		{
			"code": 0,
			"data": {},
			"deviceId": "",
			"deviceName": "",
			"id": "",
			"identifier": "",
			"mid": "",
			"occurred": 0,
			"productKey": "",
			"time": 0,
			"type": "",
			"uid": ""
		}
	],
	"total": 0
}
```


# 系统访问记录


## 清理系统访问记录


**接口地址**:`/monitor/logininfor/clean`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


暂无


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 批量删除登录日志


**接口地址**:`/monitor/logininfor/delete`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": [],
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|bo|bo|body|true|Request«List«long»»|Request«List«long»»|
|&emsp;&emsp;data|||false|array|integer|
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 获取系统访问记录列表


**接口地址**:`/monitor/logininfor/export`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|browser||query|false|string||
|id||query|false|integer(int64)||
|ipaddr||query|false|string||
|loginLocation||query|false|string||
|loginTime||query|false|string(date-time)||
|msg||query|false|string||
|os||query|false|string||
|params||query|false|object||
|status||query|false|string||
|tenantId||query|false|integer(int64)||
|userName||query|false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 获取系统访问记录列表


**接口地址**:`/monitor/logininfor/list`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": {
    "browser": "",
    "id": 0,
    "ipaddr": "",
    "loginLocation": "",
    "loginTime": "",
    "msg": "",
    "os": "",
    "params": {},
    "status": "",
    "tenantId": 0,
    "userName": ""
  },
  "pageNum": 0,
  "pageSize": 0,
  "requestId": "",
  "sortMap": {}
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|query|query|body|true|PageRequest«SysLoginInfoBo»|PageRequest«SysLoginInfoBo»|
|&emsp;&emsp;data|||false|SysLoginInfoBo|SysLoginInfoBo|
|&emsp;&emsp;&emsp;&emsp;browser|||false|string||
|&emsp;&emsp;&emsp;&emsp;id|||false|integer||
|&emsp;&emsp;&emsp;&emsp;ipaddr|||false|string||
|&emsp;&emsp;&emsp;&emsp;loginLocation|||false|string||
|&emsp;&emsp;&emsp;&emsp;loginTime|||false|string||
|&emsp;&emsp;&emsp;&emsp;msg|||false|string||
|&emsp;&emsp;&emsp;&emsp;os|||false|string||
|&emsp;&emsp;&emsp;&emsp;params|||false|object||
|&emsp;&emsp;&emsp;&emsp;status|||false|string||
|&emsp;&emsp;&emsp;&emsp;tenantId|||false|integer||
|&emsp;&emsp;&emsp;&emsp;userName|||false|string||
|&emsp;&emsp;pageNum|||false|integer(int32)||
|&emsp;&emsp;pageSize|||false|integer(int32)||
|&emsp;&emsp;requestId|||false|string||
|&emsp;&emsp;sortMap|||false|object||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|Paging«SysLogininforVo»|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|rows||array|SysLogininforVo|
|&emsp;&emsp;browser||string||
|&emsp;&emsp;id||integer(int64)||
|&emsp;&emsp;ipaddr||string||
|&emsp;&emsp;loginLocation||string||
|&emsp;&emsp;loginTime||string(date-time)||
|&emsp;&emsp;msg||string||
|&emsp;&emsp;os||string||
|&emsp;&emsp;status||string||
|&emsp;&emsp;tenantId||integer(int64)||
|&emsp;&emsp;userName||string||
|total||integer(int64)|integer(int64)|


**响应示例**:
```javascript
{
	"rows": [
		{
			"browser": "",
			"id": 0,
			"ipaddr": "",
			"loginLocation": "",
			"loginTime": "",
			"msg": "",
			"os": "",
			"status": "",
			"tenantId": 0,
			"userName": ""
		}
	],
	"total": 0
}
```


## 账户解锁


**接口地址**:`/monitor/logininfor/unlockByUserName`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": "",
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|bo|bo|body|true|Request«string»|Request«string»|
|&emsp;&emsp;data|||false|string||
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


暂无


**响应示例**:
```javascript

```


# 虚拟设备


## 添加虚拟设备


**接口地址**:`/virtual_device/add`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": {
    "createAt": 0,
    "createBy": 0,
    "createDept": 0,
    "createTime": "",
    "devices": [],
    "id": "",
    "name": "",
    "productKey": "",
    "script": "",
    "state": "",
    "tenantId": 0,
    "trigger": "",
    "triggerExpression": "",
    "type": "",
    "uid": "",
    "updateBy": 0,
    "updateTime": ""
  },
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|bo|bo|body|true|Request«VirtualDevice»|Request«VirtualDevice»|
|&emsp;&emsp;data|||false|VirtualDevice|VirtualDevice|
|&emsp;&emsp;&emsp;&emsp;createAt|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createDept|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createTime|||false|string||
|&emsp;&emsp;&emsp;&emsp;devices|||false|array|string|
|&emsp;&emsp;&emsp;&emsp;id|||false|string||
|&emsp;&emsp;&emsp;&emsp;name|||false|string||
|&emsp;&emsp;&emsp;&emsp;productKey|||false|string||
|&emsp;&emsp;&emsp;&emsp;script|||false|string||
|&emsp;&emsp;&emsp;&emsp;state|||false|string||
|&emsp;&emsp;&emsp;&emsp;tenantId|||false|integer||
|&emsp;&emsp;&emsp;&emsp;trigger|||false|string||
|&emsp;&emsp;&emsp;&emsp;triggerExpression|||false|string||
|&emsp;&emsp;&emsp;&emsp;type|||false|string||
|&emsp;&emsp;&emsp;&emsp;uid|||false|string||
|&emsp;&emsp;&emsp;&emsp;updateBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;updateTime|||false|string||
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 批量删除虚拟设备


**接口地址**:`/virtual_device/batchDelete`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": [],
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|ids|ids|body|true|Request«List«string»»|Request«List«string»»|
|&emsp;&emsp;data|||false|array|string|
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 删除虚拟设备


**接口地址**:`/virtual_device/delete`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": "",
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|bo|bo|body|true|Request«string»|Request«string»|
|&emsp;&emsp;data|||false|string||
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 获取虚拟设备详情


**接口地址**:`/virtual_device/getDetail`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": "",
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|bo|bo|body|true|Request«string»|Request«string»|
|&emsp;&emsp;data|||false|string||
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|VirtualDevice|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|createAt||integer(int64)|integer(int64)|
|createBy||integer(int64)|integer(int64)|
|createDept||integer(int64)|integer(int64)|
|createTime||string(date-time)|string(date-time)|
|devices||array||
|id||string||
|name||string||
|productKey||string||
|script||string||
|state||string||
|tenantId||integer(int64)|integer(int64)|
|trigger||string||
|triggerExpression||string||
|type||string||
|uid||string||
|updateBy||integer(int64)|integer(int64)|
|updateTime||string(date-time)|string(date-time)|


**响应示例**:
```javascript
{
	"createAt": 0,
	"createBy": 0,
	"createDept": 0,
	"createTime": "",
	"devices": [],
	"id": "",
	"name": "",
	"productKey": "",
	"script": "",
	"state": "",
	"tenantId": 0,
	"trigger": "",
	"triggerExpression": "",
	"type": "",
	"uid": "",
	"updateBy": 0,
	"updateTime": ""
}
```


## 获取虚拟设备列表


**接口地址**:`/virtual_device/list`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": {
    "createAt": 0,
    "createBy": 0,
    "createDept": 0,
    "createTime": "",
    "devices": [],
    "id": "",
    "name": "",
    "productKey": "",
    "script": "",
    "state": "",
    "tenantId": 0,
    "trigger": "",
    "triggerExpression": "",
    "type": "",
    "uid": "",
    "updateBy": 0,
    "updateTime": ""
  },
  "pageNum": 0,
  "pageSize": 0,
  "requestId": "",
  "sortMap": {}
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|pageRequest|pageRequest|body|true|PageRequest«VirtualDevice»|PageRequest«VirtualDevice»|
|&emsp;&emsp;data|||false|VirtualDevice|VirtualDevice|
|&emsp;&emsp;&emsp;&emsp;createAt|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createDept|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createTime|||false|string||
|&emsp;&emsp;&emsp;&emsp;devices|||false|array|string|
|&emsp;&emsp;&emsp;&emsp;id|||false|string||
|&emsp;&emsp;&emsp;&emsp;name|||false|string||
|&emsp;&emsp;&emsp;&emsp;productKey|||false|string||
|&emsp;&emsp;&emsp;&emsp;script|||false|string||
|&emsp;&emsp;&emsp;&emsp;state|||false|string||
|&emsp;&emsp;&emsp;&emsp;tenantId|||false|integer||
|&emsp;&emsp;&emsp;&emsp;trigger|||false|string||
|&emsp;&emsp;&emsp;&emsp;triggerExpression|||false|string||
|&emsp;&emsp;&emsp;&emsp;type|||false|string||
|&emsp;&emsp;&emsp;&emsp;uid|||false|string||
|&emsp;&emsp;&emsp;&emsp;updateBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;updateTime|||false|string||
|&emsp;&emsp;pageNum|||false|integer(int32)||
|&emsp;&emsp;pageSize|||false|integer(int32)||
|&emsp;&emsp;requestId|||false|string||
|&emsp;&emsp;sortMap|||false|object||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|Paging«VirtualDevice»|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|rows||array|VirtualDevice|
|&emsp;&emsp;createAt||integer(int64)||
|&emsp;&emsp;createBy||integer(int64)||
|&emsp;&emsp;createDept||integer(int64)||
|&emsp;&emsp;createTime||string(date-time)||
|&emsp;&emsp;devices||array|string|
|&emsp;&emsp;id||string||
|&emsp;&emsp;name||string||
|&emsp;&emsp;productKey||string||
|&emsp;&emsp;script||string||
|&emsp;&emsp;state||string||
|&emsp;&emsp;tenantId||integer(int64)||
|&emsp;&emsp;trigger||string||
|&emsp;&emsp;triggerExpression||string||
|&emsp;&emsp;type||string||
|&emsp;&emsp;uid||string||
|&emsp;&emsp;updateBy||integer(int64)||
|&emsp;&emsp;updateTime||string(date-time)||
|total||integer(int64)|integer(int64)|


**响应示例**:
```javascript
{
	"rows": [
		{
			"createAt": 0,
			"createBy": 0,
			"createDept": 0,
			"createTime": "",
			"devices": [],
			"id": "",
			"name": "",
			"productKey": "",
			"script": "",
			"state": "",
			"tenantId": 0,
			"trigger": "",
			"triggerExpression": "",
			"type": "",
			"uid": "",
			"updateBy": 0,
			"updateTime": ""
		}
	],
	"total": 0
}
```


## 取虚拟设备执行日志


**接口地址**:`/virtual_device/logs/list`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": {
    "createBy": 0,
    "createDept": 0,
    "createTime": "",
    "deviceId": "",
    "identifier": "",
    "type": "",
    "updateBy": 0,
    "updateTime": ""
  },
  "pageNum": 0,
  "pageSize": 0,
  "requestId": "",
  "sortMap": {}
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|bo|bo|body|true|PageRequest«DeviceLogQueryBo»|PageRequest«DeviceLogQueryBo»|
|&emsp;&emsp;data|||false|DeviceLogQueryBo|DeviceLogQueryBo|
|&emsp;&emsp;&emsp;&emsp;createBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createDept|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createTime|||false|string||
|&emsp;&emsp;&emsp;&emsp;deviceId|设备id||false|string||
|&emsp;&emsp;&emsp;&emsp;identifier|属性名||false|string||
|&emsp;&emsp;&emsp;&emsp;type|类型||false|string||
|&emsp;&emsp;&emsp;&emsp;updateBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;updateTime|||false|string||
|&emsp;&emsp;pageNum|||false|integer(int32)||
|&emsp;&emsp;pageSize|||false|integer(int32)||
|&emsp;&emsp;requestId|||false|string||
|&emsp;&emsp;sortMap|||false|object||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|Paging«VirtualDeviceLog»|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|rows||array|VirtualDeviceLog|
|&emsp;&emsp;deviceTotal||integer(int32)||
|&emsp;&emsp;id||string||
|&emsp;&emsp;logAt||integer(int64)||
|&emsp;&emsp;result||string||
|&emsp;&emsp;virtualDeviceId||string||
|&emsp;&emsp;virtualDeviceName||string||
|total||integer(int64)|integer(int64)|


**响应示例**:
```javascript
{
	"rows": [
		{
			"deviceTotal": 0,
			"id": "",
			"logAt": 0,
			"result": "",
			"virtualDeviceId": "",
			"virtualDeviceName": ""
		}
	],
	"total": 0
}
```


## 修改虚拟设备


**接口地址**:`/virtual_device/modify`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": {
    "createAt": 0,
    "createBy": 0,
    "createDept": 0,
    "createTime": "",
    "devices": [],
    "id": "",
    "name": "",
    "productKey": "",
    "script": "",
    "state": "",
    "tenantId": 0,
    "trigger": "",
    "triggerExpression": "",
    "type": "",
    "uid": "",
    "updateBy": 0,
    "updateTime": ""
  },
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|bo|bo|body|true|Request«VirtualDevice»|Request«VirtualDevice»|
|&emsp;&emsp;data|||false|VirtualDevice|VirtualDevice|
|&emsp;&emsp;&emsp;&emsp;createAt|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createDept|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createTime|||false|string||
|&emsp;&emsp;&emsp;&emsp;devices|||false|array|string|
|&emsp;&emsp;&emsp;&emsp;id|||false|string||
|&emsp;&emsp;&emsp;&emsp;name|||false|string||
|&emsp;&emsp;&emsp;&emsp;productKey|||false|string||
|&emsp;&emsp;&emsp;&emsp;script|||false|string||
|&emsp;&emsp;&emsp;&emsp;state|||false|string||
|&emsp;&emsp;&emsp;&emsp;tenantId|||false|integer||
|&emsp;&emsp;&emsp;&emsp;trigger|||false|string||
|&emsp;&emsp;&emsp;&emsp;triggerExpression|||false|string||
|&emsp;&emsp;&emsp;&emsp;type|||false|string||
|&emsp;&emsp;&emsp;&emsp;uid|||false|string||
|&emsp;&emsp;&emsp;&emsp;updateBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;updateTime|||false|string||
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 手动执行虚拟设备


**接口地址**:`/virtual_device/run`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": "",
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|bo|bo|body|true|Request«string»|Request«string»|
|&emsp;&emsp;data|||false|string||
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 保存关联设备


**接口地址**:`/virtual_device/saveDevices`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": {
    "createBy": 0,
    "createDept": 0,
    "createTime": "",
    "devices": [],
    "id": "",
    "updateBy": 0,
    "updateTime": ""
  },
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|bo|bo|body|true|Request«VirtualSaveDevicesBo»|Request«VirtualSaveDevicesBo»|
|&emsp;&emsp;data|||false|VirtualSaveDevicesBo|VirtualSaveDevicesBo|
|&emsp;&emsp;&emsp;&emsp;createBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createDept|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createTime|||false|string||
|&emsp;&emsp;&emsp;&emsp;devices|设备id列表||false|array|string|
|&emsp;&emsp;&emsp;&emsp;id|id||false|string||
|&emsp;&emsp;&emsp;&emsp;updateBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;updateTime|||false|string||
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 保存脚本


**接口地址**:`/virtual_device/saveScript`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": {
    "createBy": 0,
    "createDept": 0,
    "createTime": "",
    "id": "",
    "script": "",
    "updateBy": 0,
    "updateTime": ""
  },
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|bo|bo|body|true|Request«DeviceSaveScriptBo»|Request«DeviceSaveScriptBo»|
|&emsp;&emsp;data|||false|DeviceSaveScriptBo|DeviceSaveScriptBo|
|&emsp;&emsp;&emsp;&emsp;createBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createDept|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createTime|||false|string||
|&emsp;&emsp;&emsp;&emsp;id|id||false|string||
|&emsp;&emsp;&emsp;&emsp;script|脚本||false|string||
|&emsp;&emsp;&emsp;&emsp;updateBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;updateTime|||false|string||
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 设置虚拟设备状态


**接口地址**:`/virtual_device/setState`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": {
    "createBy": 0,
    "createDept": 0,
    "createTime": "",
    "id": "",
    "state": "",
    "updateBy": 0,
    "updateTime": ""
  },
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|bo|bo|body|true|Request«ChangeStateBo»|Request«ChangeStateBo»|
|&emsp;&emsp;data|||false|ChangeStateBo|ChangeStateBo|
|&emsp;&emsp;&emsp;&emsp;createBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createDept|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createTime|||false|string||
|&emsp;&emsp;&emsp;&emsp;id|||false|string||
|&emsp;&emsp;&emsp;&emsp;state|运行状态||false|string||
|&emsp;&emsp;&emsp;&emsp;updateBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;updateTime|||false|string||
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


暂无


**响应示例**:
```javascript

```


# 规则引擎


## 删除规则


**接口地址**:`/rule_engine/delete`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": "",
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|request|request|body|true|Request«string»|Request«string»|
|&emsp;&emsp;data|||false|string||
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 保存规则


**接口地址**:`/rule_engine/edit`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": {
    "actions": [
      {
        "config": "",
        "type": ""
      }
    ],
    "createAt": 0,
    "createBy": 0,
    "createDept": 0,
    "createTime": "",
    "desc": "",
    "filters": [
      {
        "config": "",
        "type": ""
      }
    ],
    "id": "",
    "listeners": [
      {
        "config": "",
        "type": ""
      }
    ],
    "name": "",
    "state": "",
    "type": "",
    "uid": "",
    "updateBy": 0,
    "updateTime": ""
  },
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|ruleInfoBo|ruleInfoBo|body|true|Request«RuleInfoBo»|Request«RuleInfoBo»|
|&emsp;&emsp;data|||false|RuleInfoBo|RuleInfoBo|
|&emsp;&emsp;&emsp;&emsp;actions|动作||false|array|RuleAction|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;config|||false|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;type|||false|string||
|&emsp;&emsp;&emsp;&emsp;createAt|创建时间||false|integer||
|&emsp;&emsp;&emsp;&emsp;createBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createDept|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createTime|||false|string||
|&emsp;&emsp;&emsp;&emsp;desc|描述||false|string||
|&emsp;&emsp;&emsp;&emsp;filters|过滤器||false|array|FilterConfig|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;config|||false|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;type|||false|string||
|&emsp;&emsp;&emsp;&emsp;id|id||false|string||
|&emsp;&emsp;&emsp;&emsp;listeners|监听器||false|array|FilterConfig|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;config|||false|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;type|||false|string||
|&emsp;&emsp;&emsp;&emsp;name|规则名称||false|string||
|&emsp;&emsp;&emsp;&emsp;state|状态||false|string||
|&emsp;&emsp;&emsp;&emsp;type|规则类型||false|string||
|&emsp;&emsp;&emsp;&emsp;uid|用户id||false|string||
|&emsp;&emsp;&emsp;&emsp;updateBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;updateTime|||false|string||
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 规则列表


**接口地址**:`/rule_engine/list`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": {
    "actions": [
      {
        "config": "",
        "type": ""
      }
    ],
    "createAt": 0,
    "createBy": 0,
    "createDept": 0,
    "createTime": "",
    "desc": "",
    "filters": [
      {
        "config": "",
        "type": ""
      }
    ],
    "id": "",
    "listeners": [
      {
        "config": "",
        "type": ""
      }
    ],
    "name": "",
    "state": "",
    "type": "",
    "uid": "",
    "updateBy": 0,
    "updateTime": ""
  },
  "pageNum": 0,
  "pageSize": 0,
  "requestId": "",
  "sortMap": {}
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|request|request|body|true|PageRequest«RuleInfoBo»|PageRequest«RuleInfoBo»|
|&emsp;&emsp;data|||false|RuleInfoBo|RuleInfoBo|
|&emsp;&emsp;&emsp;&emsp;actions|动作||false|array|RuleAction|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;config|||false|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;type|||false|string||
|&emsp;&emsp;&emsp;&emsp;createAt|创建时间||false|integer||
|&emsp;&emsp;&emsp;&emsp;createBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createDept|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createTime|||false|string||
|&emsp;&emsp;&emsp;&emsp;desc|描述||false|string||
|&emsp;&emsp;&emsp;&emsp;filters|过滤器||false|array|FilterConfig|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;config|||false|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;type|||false|string||
|&emsp;&emsp;&emsp;&emsp;id|id||false|string||
|&emsp;&emsp;&emsp;&emsp;listeners|监听器||false|array|FilterConfig|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;config|||false|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;type|||false|string||
|&emsp;&emsp;&emsp;&emsp;name|规则名称||false|string||
|&emsp;&emsp;&emsp;&emsp;state|状态||false|string||
|&emsp;&emsp;&emsp;&emsp;type|规则类型||false|string||
|&emsp;&emsp;&emsp;&emsp;uid|用户id||false|string||
|&emsp;&emsp;&emsp;&emsp;updateBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;updateTime|||false|string||
|&emsp;&emsp;pageNum|||false|integer(int32)||
|&emsp;&emsp;pageSize|||false|integer(int32)||
|&emsp;&emsp;requestId|||false|string||
|&emsp;&emsp;sortMap|||false|object||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|Paging«RuleInfoVo»|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|rows||array|RuleInfoVo|
|&emsp;&emsp;actions|动作|array|RuleAction|
|&emsp;&emsp;&emsp;&emsp;config||string||
|&emsp;&emsp;&emsp;&emsp;type||string||
|&emsp;&emsp;createAt|创建时间|integer(int64)||
|&emsp;&emsp;desc|描述|string||
|&emsp;&emsp;filters|过滤器|array|FilterConfig|
|&emsp;&emsp;&emsp;&emsp;config||string||
|&emsp;&emsp;&emsp;&emsp;type||string||
|&emsp;&emsp;id|规则id|string||
|&emsp;&emsp;listeners|监听器|array|FilterConfig|
|&emsp;&emsp;&emsp;&emsp;config||string||
|&emsp;&emsp;&emsp;&emsp;type||string||
|&emsp;&emsp;name|规则名称|string||
|&emsp;&emsp;state|状态|string||
|&emsp;&emsp;type|规则类型|string||
|&emsp;&emsp;uid|用户id|string||
|total||integer(int64)|integer(int64)|


**响应示例**:
```javascript
{
	"rows": [
		{
			"actions": [
				{
					"config": "",
					"type": ""
				}
			],
			"createAt": 0,
			"desc": "",
			"filters": [
				{
					"config": "",
					"type": ""
				}
			],
			"id": "",
			"listeners": [
				{
					"config": "",
					"type": ""
				}
			],
			"name": "",
			"state": "",
			"type": "",
			"uid": ""
		}
	],
	"total": 0
}
```


## 暂停规则


**接口地址**:`/rule_engine/pause`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": "",
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|request|request|body|true|Request«string»|Request«string»|
|&emsp;&emsp;data|||false|string||
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 恢复规则


**接口地址**:`/rule_engine/resume`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": "",
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|request|request|body|true|Request«string»|Request«string»|
|&emsp;&emsp;data|||false|string||
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 清理日志


**接口地址**:`/rule_engine/ruleLog/clear`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": "",
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|request|request|body|true|Request«string»|Request«string»|
|&emsp;&emsp;data|||false|string||
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 规则日志


**接口地址**:`/rule_engine/ruleLog/list`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": {
    "content": "",
    "createBy": 0,
    "createDept": 0,
    "createTime": "",
    "ruleId": "",
    "state1": "",
    "success": true,
    "time": 0,
    "updateBy": 0,
    "updateTime": ""
  },
  "pageNum": 0,
  "pageSize": 0,
  "requestId": "",
  "sortMap": {}
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|request|request|body|true|PageRequest«RuleLogBo»|PageRequest«RuleLogBo»|
|&emsp;&emsp;data|||false|RuleLogBo|RuleLogBo|
|&emsp;&emsp;&emsp;&emsp;content|内容||false|string||
|&emsp;&emsp;&emsp;&emsp;createBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createDept|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createTime|||false|string||
|&emsp;&emsp;&emsp;&emsp;ruleId|规则id||false|string||
|&emsp;&emsp;&emsp;&emsp;state1|状态||false|string||
|&emsp;&emsp;&emsp;&emsp;success|是否成功||false|boolean||
|&emsp;&emsp;&emsp;&emsp;time|时间||false|integer||
|&emsp;&emsp;&emsp;&emsp;updateBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;updateTime|||false|string||
|&emsp;&emsp;pageNum|||false|integer(int32)||
|&emsp;&emsp;pageSize|||false|integer(int32)||
|&emsp;&emsp;requestId|||false|string||
|&emsp;&emsp;sortMap|||false|object||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|Paging«RuleLogVo»|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|rows||array|RuleLogVo|
|&emsp;&emsp;content|内容|string||
|&emsp;&emsp;logAt|时间|integer(int64)||
|&emsp;&emsp;ruleId|规则id|string||
|&emsp;&emsp;state|状态|string||
|&emsp;&emsp;success|是否成功|boolean||
|total||integer(int64)|integer(int64)|


**响应示例**:
```javascript
{
	"rows": [
		{
			"content": "",
			"logAt": 0,
			"ruleId": "",
			"state": "",
			"success": true
		}
	],
	"total": 0
}
```


## 删除定时任务


**接口地址**:`/rule_engine/task/delete`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": "",
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|request|request|body|true|Request«string»|Request«string»|
|&emsp;&emsp;data|||false|string||
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 停止定时任务


**接口地址**:`/rule_engine/task/pause`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": "",
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|request|request|body|true|Request«string»|Request«string»|
|&emsp;&emsp;data|||false|string||
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 更新定时任务


**接口地址**:`/rule_engine/task/renew`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": "",
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|request|request|body|true|Request«string»|Request«string»|
|&emsp;&emsp;data|||false|string||
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 恢复定时任务


**接口地址**:`/rule_engine/task/resume`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": "",
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|request|request|body|true|Request«string»|Request«string»|
|&emsp;&emsp;data|||false|string||
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 保存定时任务


**接口地址**:`/rule_engine/task/save`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": {
    "actions": [
      {
        "config": "",
        "type": ""
      }
    ],
    "createAt": 0,
    "createBy": 0,
    "createDept": 0,
    "createTime": "",
    "desc": "",
    "expression": "",
    "id": "",
    "name": "",
    "reason": "",
    "seconds": 0,
    "state": "",
    "type": "",
    "uid": "",
    "updateBy": 0,
    "updateTime": ""
  },
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|taskInfo|taskInfo|body|true|Request«TaskInfoBo»|Request«TaskInfoBo»|
|&emsp;&emsp;data|||false|TaskInfoBo|TaskInfoBo|
|&emsp;&emsp;&emsp;&emsp;actions|任务输出||false|array|RuleAction|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;config|||false|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;type|||false|string||
|&emsp;&emsp;&emsp;&emsp;createAt|创建时间||false|integer||
|&emsp;&emsp;&emsp;&emsp;createBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createDept|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createTime|||false|string||
|&emsp;&emsp;&emsp;&emsp;desc|描述||false|string||
|&emsp;&emsp;&emsp;&emsp;expression|表达式||false|string||
|&emsp;&emsp;&emsp;&emsp;id|id||false|string||
|&emsp;&emsp;&emsp;&emsp;name|任务名称||false|string||
|&emsp;&emsp;&emsp;&emsp;reason|操作备注||false|string||
|&emsp;&emsp;&emsp;&emsp;seconds|延时时长秒||false|integer||
|&emsp;&emsp;&emsp;&emsp;state|任务状态||false|string||
|&emsp;&emsp;&emsp;&emsp;type|任务类型||false|string||
|&emsp;&emsp;&emsp;&emsp;uid|创建者||false|string||
|&emsp;&emsp;&emsp;&emsp;updateBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;updateTime|||false|string||
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 清除定时任务日志


**接口地址**:`/rule_engine/taskLogs/clear`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": "",
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|request|request|body|true|Request«string»|Request«string»|
|&emsp;&emsp;data|||false|string||
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 定时任务日志list


**接口地址**:`/rule_engine/taskLogs/list`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": {
    "content": "",
    "createBy": 0,
    "createDept": 0,
    "createTime": "",
    "id": "",
    "logAt": 0,
    "success": true,
    "taskId": "",
    "updateBy": 0,
    "updateTime": ""
  },
  "pageNum": 0,
  "pageSize": 0,
  "requestId": "",
  "sortMap": {}
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|request|request|body|true|PageRequest«TaskLogBo»|PageRequest«TaskLogBo»|
|&emsp;&emsp;data|||false|TaskLogBo|TaskLogBo|
|&emsp;&emsp;&emsp;&emsp;content|||false|string||
|&emsp;&emsp;&emsp;&emsp;createBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createDept|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createTime|||false|string||
|&emsp;&emsp;&emsp;&emsp;id|||false|string||
|&emsp;&emsp;&emsp;&emsp;logAt|||false|integer||
|&emsp;&emsp;&emsp;&emsp;success|||false|boolean||
|&emsp;&emsp;&emsp;&emsp;taskId|||false|string||
|&emsp;&emsp;&emsp;&emsp;updateBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;updateTime|||false|string||
|&emsp;&emsp;pageNum|||false|integer(int32)||
|&emsp;&emsp;pageSize|||false|integer(int32)||
|&emsp;&emsp;requestId|||false|string||
|&emsp;&emsp;sortMap|||false|object||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|Paging«TaskLogVo»|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|rows||array|TaskLogVo|
|&emsp;&emsp;content||string||
|&emsp;&emsp;id||string||
|&emsp;&emsp;logAt||integer(int64)||
|&emsp;&emsp;success||boolean||
|&emsp;&emsp;taskId||string||
|total||integer(int64)|integer(int64)|


**响应示例**:
```javascript
{
	"rows": [
		{
			"content": "",
			"id": "",
			"logAt": 0,
			"success": true,
			"taskId": ""
		}
	],
	"total": 0
}
```


## 定时任务列表


**接口地址**:`/rule_engine/tasks/list`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": {
    "actions": [
      {
        "config": "",
        "type": ""
      }
    ],
    "createAt": 0,
    "createBy": 0,
    "createDept": 0,
    "createTime": "",
    "desc": "",
    "expression": "",
    "id": "",
    "name": "",
    "reason": "",
    "seconds": 0,
    "state": "",
    "type": "",
    "uid": "",
    "updateBy": 0,
    "updateTime": ""
  },
  "pageNum": 0,
  "pageSize": 0,
  "requestId": "",
  "sortMap": {}
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|request|request|body|true|PageRequest«TaskInfoBo»|PageRequest«TaskInfoBo»|
|&emsp;&emsp;data|||false|TaskInfoBo|TaskInfoBo|
|&emsp;&emsp;&emsp;&emsp;actions|任务输出||false|array|RuleAction|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;config|||false|string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;type|||false|string||
|&emsp;&emsp;&emsp;&emsp;createAt|创建时间||false|integer||
|&emsp;&emsp;&emsp;&emsp;createBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createDept|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createTime|||false|string||
|&emsp;&emsp;&emsp;&emsp;desc|描述||false|string||
|&emsp;&emsp;&emsp;&emsp;expression|表达式||false|string||
|&emsp;&emsp;&emsp;&emsp;id|id||false|string||
|&emsp;&emsp;&emsp;&emsp;name|任务名称||false|string||
|&emsp;&emsp;&emsp;&emsp;reason|操作备注||false|string||
|&emsp;&emsp;&emsp;&emsp;seconds|延时时长秒||false|integer||
|&emsp;&emsp;&emsp;&emsp;state|任务状态||false|string||
|&emsp;&emsp;&emsp;&emsp;type|任务类型||false|string||
|&emsp;&emsp;&emsp;&emsp;uid|创建者||false|string||
|&emsp;&emsp;&emsp;&emsp;updateBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;updateTime|||false|string||
|&emsp;&emsp;pageNum|||false|integer(int32)||
|&emsp;&emsp;pageSize|||false|integer(int32)||
|&emsp;&emsp;requestId|||false|string||
|&emsp;&emsp;sortMap|||false|object||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|Paging«TaskInfoVo»|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|rows||array|TaskInfoVo|
|&emsp;&emsp;actions|任务输出|array|RuleAction|
|&emsp;&emsp;&emsp;&emsp;config||string||
|&emsp;&emsp;&emsp;&emsp;type||string||
|&emsp;&emsp;createAt|创建时间|integer(int64)||
|&emsp;&emsp;desc|描述|string||
|&emsp;&emsp;expression|表达式|string||
|&emsp;&emsp;id|主键|string||
|&emsp;&emsp;name|任务名称|string||
|&emsp;&emsp;reason|操作备注|string||
|&emsp;&emsp;seconds||integer(int32)||
|&emsp;&emsp;state|任务状态|string||
|&emsp;&emsp;type|任务类型|string||
|&emsp;&emsp;uid|创建者|string||
|total||integer(int64)|integer(int64)|


**响应示例**:
```javascript
{
	"rows": [
		{
			"actions": [
				{
					"config": "",
					"type": ""
				}
			],
			"createAt": 0,
			"desc": "",
			"expression": "",
			"id": "",
			"name": "",
			"reason": "",
			"seconds": 0,
			"state": "",
			"type": "",
			"uid": ""
		}
	],
	"total": 0
}
```


# 认证


## 登录


**接口地址**:`/auth/login`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": {
    "code": "",
    "password": "",
    "tenantId": 0,
    "username": "",
    "uuid": ""
  },
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|body|body|body|true|Request«LoginBody»|Request«LoginBody»|
|&emsp;&emsp;data|||false|LoginBody|LoginBody|
|&emsp;&emsp;&emsp;&emsp;code|||false|string||
|&emsp;&emsp;&emsp;&emsp;password|||false|string||
|&emsp;&emsp;&emsp;&emsp;tenantId|||false|integer||
|&emsp;&emsp;&emsp;&emsp;username|||false|string||
|&emsp;&emsp;&emsp;&emsp;uuid|||false|string||
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|LoginVo|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|token||string||


**响应示例**:
```javascript
{
	"token": ""
}
```


## 退出登录


**接口地址**:`/auth/logout`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


暂无


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 用户注册


**接口地址**:`/auth/register`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "code": "",
  "password": "",
  "tenantId": 0,
  "userType": "",
  "username": "",
  "uuid": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|user|user|body|true|RegisterBody|RegisterBody|
|&emsp;&emsp;code|||false|string||
|&emsp;&emsp;password|||false|string||
|&emsp;&emsp;tenantId|||false|integer(int64)||
|&emsp;&emsp;userType|||false|string||
|&emsp;&emsp;username|||false|string||
|&emsp;&emsp;uuid|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 登录页面租户下拉框


**接口地址**:`/auth/tenant/list`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


暂无


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|LoginTenantVo|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|tenantEnabled||boolean||
|voList||array|TenantListVo|
|&emsp;&emsp;companyName||string||
|&emsp;&emsp;domain||string||
|&emsp;&emsp;tenantId||integer(int64)||


**响应示例**:
```javascript
{
	"tenantEnabled": true,
	"voList": [
		{
			"companyName": "",
			"domain": "",
			"tenantId": 0
		}
	]
}
```


## 小程序登录


**接口地址**:`/auth/xcxLogin`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": {
    "appId": "",
    "code": ""
  },
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|body|body|body|true|Request«XcxLoginBo»|Request«XcxLoginBo»|
|&emsp;&emsp;data|||false|XcxLoginBo|XcxLoginBo|
|&emsp;&emsp;&emsp;&emsp;appId|appId||false|string||
|&emsp;&emsp;&emsp;&emsp;code|授权码||false|string||
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|LoginVo|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|token||string||


**响应示例**:
```javascript
{
	"token": ""
}
```


# 设备


## 创建设备


**接口地址**:`/device/add`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": {
    "createAt": 0,
    "createBy": 0,
    "createDept": 0,
    "createTime": "",
    "deviceId": "",
    "deviceName": "",
    "id": "",
    "latitude": "",
    "longitude": "",
    "model": "",
    "offlineTime": 0,
    "onlineTime": 0,
    "parentId": "",
    "productKey": "",
    "secret": "",
    "uid": "",
    "updateBy": 0,
    "updateTime": ""
  },
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|bo|bo|body|true|Request«DeviceInfoBo»|Request«DeviceInfoBo»|
|&emsp;&emsp;data|||false|DeviceInfoBo|DeviceInfoBo|
|&emsp;&emsp;&emsp;&emsp;createAt|创建时间||false|integer||
|&emsp;&emsp;&emsp;&emsp;createBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createDept|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createTime|||false|string||
|&emsp;&emsp;&emsp;&emsp;deviceId|设备id||false|string||
|&emsp;&emsp;&emsp;&emsp;deviceName|设备名称||false|string||
|&emsp;&emsp;&emsp;&emsp;id|||false|string||
|&emsp;&emsp;&emsp;&emsp;latitude|纬度||false|string||
|&emsp;&emsp;&emsp;&emsp;longitude|经度||false|string||
|&emsp;&emsp;&emsp;&emsp;model|设备类型||false|string||
|&emsp;&emsp;&emsp;&emsp;offlineTime|设备离线时间||false|integer||
|&emsp;&emsp;&emsp;&emsp;onlineTime|设备在线时间||false|integer||
|&emsp;&emsp;&emsp;&emsp;parentId|父级id||false|string||
|&emsp;&emsp;&emsp;&emsp;productKey|产品key||false|string||
|&emsp;&emsp;&emsp;&emsp;secret|设备描述||false|string||
|&emsp;&emsp;&emsp;&emsp;uid|用户id||false|string||
|&emsp;&emsp;&emsp;&emsp;updateBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;updateTime|||false|string||
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 批量删除设备


**接口地址**:`/device/batchDelete`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": [],
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|request|request|body|true|Request«List«string»»|Request«List«string»»|
|&emsp;&emsp;data|||false|array|string|
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 获取子设备


**接口地址**:`/device/children/list`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:<p>获取子设备</p>



**请求示例**:


```javascript
{
  "data": "",
  "pageNum": 0,
  "pageSize": 0,
  "requestId": "",
  "sortMap": {}
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|request|request|body|true|PageRequest«string»|PageRequest«string»|
|&emsp;&emsp;data|||false|string||
|&emsp;&emsp;pageNum|||false|integer(int32)||
|&emsp;&emsp;pageSize|||false|integer(int32)||
|&emsp;&emsp;requestId|||false|string||
|&emsp;&emsp;sortMap|||false|object||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|DeviceInfoVo|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|createAt|创建时间|integer(int64)|integer(int64)|
|deviceId|设备id|string||
|deviceName|设备名称|string||
|group|所属分组|Group|Group|
|&emsp;&emsp;id||string||
|&emsp;&emsp;name||string||
|id||string||
|locate|位置信息|Locate|Locate|
|&emsp;&emsp;latitude||string||
|&emsp;&emsp;longitude||string||
|model|设备类型|string||
|offlineTime|设备离线时间|integer(int64)|integer(int64)|
|online|设备状态|boolean||
|onlineTime|设备在线时间|integer(int64)|integer(int64)|
|parentId|父级id|string||
|product|所属产品信息|Product|Product|
|&emsp;&emsp;category||string||
|&emsp;&emsp;createAt||integer(int64)||
|&emsp;&emsp;createBy||integer(int64)||
|&emsp;&emsp;createDept||integer(int64)||
|&emsp;&emsp;createTime||string(date-time)||
|&emsp;&emsp;iconId||integer(int64)||
|&emsp;&emsp;id||integer(int64)||
|&emsp;&emsp;img||string||
|&emsp;&emsp;isOpenLocate||boolean||
|&emsp;&emsp;keepAliveTime||integer(int64)||
|&emsp;&emsp;locateUpdateType||string||
|&emsp;&emsp;name||string||
|&emsp;&emsp;nodeType||integer(int32)||
|&emsp;&emsp;productKey||string||
|&emsp;&emsp;productSecret||string||
|&emsp;&emsp;tenantId||integer(int64)||
|&emsp;&emsp;transparent||boolean||
|&emsp;&emsp;uid||string||
|&emsp;&emsp;updateBy||integer(int64)||
|&emsp;&emsp;updateTime||string(date-time)||
|productKey|产品key|string||
|secret|设备描述|string||


**响应示例**:
```javascript
[
	{
		"createAt": 0,
		"deviceId": "",
		"deviceName": "",
		"group": {
			"additionalProperties1": {
				"id": "",
				"name": ""
			}
		},
		"id": "",
		"locate": {
			"latitude": "",
			"longitude": ""
		},
		"model": "",
		"offlineTime": 0,
		"online": true,
		"onlineTime": 0,
		"parentId": "",
		"product": {
			"category": "",
			"createAt": 0,
			"createBy": 0,
			"createDept": 0,
			"createTime": "",
			"iconId": 0,
			"id": 0,
			"img": "",
			"isOpenLocate": true,
			"keepAliveTime": 0,
			"locateUpdateType": "",
			"name": "",
			"nodeType": 0,
			"productKey": "",
			"productSecret": "",
			"tenantId": 0,
			"transparent": true,
			"uid": "",
			"updateBy": 0,
			"updateTime": ""
		},
		"productKey": "",
		"secret": ""
	}
]
```


## 获取设备配置


**接口地址**:`/device/config/get`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": "",
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|request|request|body|true|Request«string»|Request«string»|
|&emsp;&emsp;data|||false|string||
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|DeviceConfigVo|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|config|设备配置json内容|string||
|createAt|创建时间|integer(int64)|integer(int64)|
|deviceId|设备id|string||
|deviceName|设备名称|string||
|id|设备配置id|string||
|productKey|产品key|string||


**响应示例**:
```javascript
{
	"config": "",
	"createAt": 0,
	"deviceId": "",
	"deviceName": "",
	"id": "",
	"productKey": ""
}
```


## 保存设备配置


**接口地址**:`/device/config/save`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": {
    "config": "",
    "createBy": 0,
    "createDept": 0,
    "createTime": "",
    "deviceId": "",
    "updateBy": 0,
    "updateTime": ""
  },
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|request|request|body|true|Request«DeviceConfigAddBo»|Request«DeviceConfigAddBo»|
|&emsp;&emsp;data|||false|DeviceConfigAddBo|DeviceConfigAddBo|
|&emsp;&emsp;&emsp;&emsp;config|设备配置json内容||false|string||
|&emsp;&emsp;&emsp;&emsp;createBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createDept|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createTime|||false|string||
|&emsp;&emsp;&emsp;&emsp;deviceId|设备id||false|string||
|&emsp;&emsp;&emsp;&emsp;updateBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;updateTime|||false|string||
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 设备配置下发


**接口地址**:`/device/config/send`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": "",
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|bo|bo|body|true|Request«string»|Request«string»|
|&emsp;&emsp;data|||false|string||
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|InvokeResult|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|requestId||string||
|time||integer(int64)|integer(int64)|


**响应示例**:
```javascript
{
	"requestId": "",
	"time": 0
}
```


## 消费设备信息消息（实时推送设备信息）


**接口地址**:`/device/consumer`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": {
    "clientId": "",
    "createBy": 0,
    "createDept": 0,
    "createTime": "",
    "deviceId": "",
    "updateBy": 0,
    "updateTime": ""
  },
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|bo|bo|body|true|Request«DeviceConsumerBo»|Request«DeviceConsumerBo»|
|&emsp;&emsp;data|||false|DeviceConsumerBo|DeviceConsumerBo|
|&emsp;&emsp;&emsp;&emsp;clientId|clientId||false|string||
|&emsp;&emsp;&emsp;&emsp;createBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createDept|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createTime|||false|string||
|&emsp;&emsp;&emsp;&emsp;deviceId|设备id||false|string||
|&emsp;&emsp;&emsp;&emsp;updateBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;updateTime|||false|string||
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|DeferredResult«ThingModelMessage»|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|result||object||
|setOrExpired||boolean||


**响应示例**:
```javascript
{
	"result": {},
	"setOrExpired": true
}
```


## 删除设备


**接口地址**:`/device/delete`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": "",
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|request|request|body|true|Request«string»|Request«string»|
|&emsp;&emsp;data|||false|string||
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 获取设备详情


**接口地址**:`/device/detail`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": "",
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|request|request|body|true|Request«string»|Request«string»|
|&emsp;&emsp;data|||false|string||
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|DeviceInfo|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|createAt||integer(int64)|integer(int64)|
|createBy||integer(int64)|integer(int64)|
|createDept||integer(int64)|integer(int64)|
|createTime||string(date-time)|string(date-time)|
|deviceId||string||
|deviceName||string||
|group||Group|Group|
|&emsp;&emsp;id||string||
|&emsp;&emsp;name||string||
|id||string||
|locate||Locate|Locate|
|&emsp;&emsp;latitude||string||
|&emsp;&emsp;longitude||string||
|model||string||
|online||boolean||
|parentId||string||
|productKey||string||
|property||object||
|secret||string||
|state||State|State|
|&emsp;&emsp;offlineTime||integer(int64)||
|&emsp;&emsp;online||boolean||
|&emsp;&emsp;onlineTime||integer(int64)||
|subUid||array||
|tag||Tag|Tag|
|&emsp;&emsp;id||string||
|&emsp;&emsp;name||string||
|&emsp;&emsp;value||string||
|tenantId||integer(int64)|integer(int64)|
|uid||string||
|updateBy||integer(int64)|integer(int64)|
|updateTime||string(date-time)|string(date-time)|


**响应示例**:
```javascript
{
	"createAt": 0,
	"createBy": 0,
	"createDept": 0,
	"createTime": "",
	"deviceId": "",
	"deviceName": "",
	"group": {
		"additionalProperties1": {
			"id": "",
			"name": ""
		}
	},
	"id": "",
	"locate": {
		"latitude": "",
		"longitude": ""
	},
	"model": "",
	"online": true,
	"parentId": "",
	"productKey": "",
	"property": {},
	"secret": "",
	"state": {
		"offlineTime": 0,
		"online": true,
		"onlineTime": 0
	},
	"subUid": [],
	"tag": {
		"additionalProperties1": {
			"id": "",
			"name": "",
			"value": ""
		}
	},
	"tenantId": 0,
	"uid": "",
	"updateBy": 0,
	"updateTime": ""
}
```


## 设备物模型日志


**接口地址**:`/device/deviceLogs/list`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": {
    "createBy": 0,
    "createDept": 0,
    "createTime": "",
    "deviceId": "",
    "identifier": "",
    "type": "",
    "updateBy": 0,
    "updateTime": ""
  },
  "pageNum": 0,
  "pageSize": 0,
  "requestId": "",
  "sortMap": {}
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|request|request|body|true|PageRequest«DeviceLogQueryBo»|PageRequest«DeviceLogQueryBo»|
|&emsp;&emsp;data|||false|DeviceLogQueryBo|DeviceLogQueryBo|
|&emsp;&emsp;&emsp;&emsp;createBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createDept|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createTime|||false|string||
|&emsp;&emsp;&emsp;&emsp;deviceId|设备id||false|string||
|&emsp;&emsp;&emsp;&emsp;identifier|属性名||false|string||
|&emsp;&emsp;&emsp;&emsp;type|类型||false|string||
|&emsp;&emsp;&emsp;&emsp;updateBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;updateTime|||false|string||
|&emsp;&emsp;pageNum|||false|integer(int32)||
|&emsp;&emsp;pageSize|||false|integer(int32)||
|&emsp;&emsp;requestId|||false|string||
|&emsp;&emsp;sortMap|||false|object||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|Paging«ThingModelMessage»|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|rows||array|ThingModelMessage|
|&emsp;&emsp;code||integer(int32)||
|&emsp;&emsp;data||object||
|&emsp;&emsp;deviceId||string||
|&emsp;&emsp;deviceName||string||
|&emsp;&emsp;id||string||
|&emsp;&emsp;identifier||string||
|&emsp;&emsp;mid||string||
|&emsp;&emsp;occurred||integer(int64)||
|&emsp;&emsp;productKey||string||
|&emsp;&emsp;time||integer(int64)||
|&emsp;&emsp;type||string||
|&emsp;&emsp;uid||string||
|total||integer(int64)|integer(int64)|


**响应示例**:
```javascript
{
	"rows": [
		{
			"code": 0,
			"data": {},
			"deviceId": "",
			"deviceName": "",
			"id": "",
			"identifier": "",
			"mid": "",
			"occurred": 0,
			"productKey": "",
			"time": 0,
			"type": "",
			"uid": ""
		}
	],
	"total": 0
}
```


## 获取设备属性历史数据


**接口地址**:`/device/deviceProperty/log/list`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": {
    "createBy": 0,
    "createDept": 0,
    "createTime": "",
    "deviceId": "",
    "end": 0,
    "name": "",
    "start": 0,
    "updateBy": 0,
    "updateTime": ""
  },
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|query|query|body|true|Request«DevicePropertiesLogQueryBo»|Request«DevicePropertiesLogQueryBo»|
|&emsp;&emsp;data|||false|DevicePropertiesLogQueryBo|DevicePropertiesLogQueryBo|
|&emsp;&emsp;&emsp;&emsp;createBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createDept|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createTime|||false|string||
|&emsp;&emsp;&emsp;&emsp;deviceId|设备id||false|string||
|&emsp;&emsp;&emsp;&emsp;end|结束时间||false|integer||
|&emsp;&emsp;&emsp;&emsp;name|属性名称||false|string||
|&emsp;&emsp;&emsp;&emsp;start|开始时间||false|integer||
|&emsp;&emsp;&emsp;&emsp;updateBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;updateTime|||false|string||
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|DeviceProperty|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|deviceId||string||
|id||string||
|name||string||
|time||integer(int64)|integer(int64)|
|value||object||


**响应示例**:
```javascript
[
	{
		"deviceId": "",
		"id": "",
		"name": "",
		"time": 0,
		"value": {}
	}
]
```


## 下载设备模板


**接口地址**:`/device/exportData`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


暂无


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 获取设备详情


**接口地址**:`/device/getByPkDn`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": {
    "createBy": 0,
    "createDept": 0,
    "createTime": "",
    "dn": "",
    "pk": "",
    "updateBy": 0,
    "updateTime": ""
  },
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|query|query|body|true|Request«DeviceQueryByPkDnBo»|Request«DeviceQueryByPkDnBo»|
|&emsp;&emsp;data|||false|DeviceQueryByPkDnBo|DeviceQueryByPkDnBo|
|&emsp;&emsp;&emsp;&emsp;createBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createDept|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createTime|||false|string||
|&emsp;&emsp;&emsp;&emsp;dn|设备||false|string||
|&emsp;&emsp;&emsp;&emsp;pk|产品key||false|string||
|&emsp;&emsp;&emsp;&emsp;updateBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;updateTime|||false|string||
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|DeviceInfo|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|createAt||integer(int64)|integer(int64)|
|createBy||integer(int64)|integer(int64)|
|createDept||integer(int64)|integer(int64)|
|createTime||string(date-time)|string(date-time)|
|deviceId||string||
|deviceName||string||
|group||Group|Group|
|&emsp;&emsp;id||string||
|&emsp;&emsp;name||string||
|id||string||
|locate||Locate|Locate|
|&emsp;&emsp;latitude||string||
|&emsp;&emsp;longitude||string||
|model||string||
|online||boolean||
|parentId||string||
|productKey||string||
|property||object||
|secret||string||
|state||State|State|
|&emsp;&emsp;offlineTime||integer(int64)||
|&emsp;&emsp;online||boolean||
|&emsp;&emsp;onlineTime||integer(int64)||
|subUid||array||
|tag||Tag|Tag|
|&emsp;&emsp;id||string||
|&emsp;&emsp;name||string||
|&emsp;&emsp;value||string||
|tenantId||integer(int64)|integer(int64)|
|uid||string||
|updateBy||integer(int64)|integer(int64)|
|updateTime||string(date-time)|string(date-time)|


**响应示例**:
```javascript
{
	"createAt": 0,
	"createBy": 0,
	"createDept": 0,
	"createTime": "",
	"deviceId": "",
	"deviceName": "",
	"group": {
		"additionalProperties1": {
			"id": "",
			"name": ""
		}
	},
	"id": "",
	"locate": {
		"latitude": "",
		"longitude": ""
	},
	"model": "",
	"online": true,
	"parentId": "",
	"productKey": "",
	"property": {},
	"secret": "",
	"state": {
		"offlineTime": 0,
		"online": true,
		"onlineTime": 0
	},
	"subUid": [],
	"tag": {
		"additionalProperties1": {
			"id": "",
			"name": "",
			"value": ""
		}
	},
	"tenantId": 0,
	"uid": "",
	"updateBy": 0,
	"updateTime": ""
}
```


## 获取网关设备


**接口地址**:`/device/getParentDevices`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


暂无


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|ParentDeviceVo|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|deviceName||string||
|id||string||


**响应示例**:
```javascript
[
	{
		"deviceName": "",
		"id": ""
	}
]
```


## 获取设备物模型


**接口地址**:`/device/getThingModel`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": "",
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|request|request|body|true|Request«string»|Request«string»|
|&emsp;&emsp;data|||false|string||
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|ThingModelVo|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|id|主键|string||
|model|模型内容|Model|Model|
|&emsp;&emsp;events||array|Event|
|&emsp;&emsp;&emsp;&emsp;identifier||string||
|&emsp;&emsp;&emsp;&emsp;name||string||
|&emsp;&emsp;&emsp;&emsp;outputData||array|Parameter|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;dataType||DataType|DataType|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;specs||object||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;type||string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;description||string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;identifier||string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;name||string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;required||boolean||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;unit||string||
|&emsp;&emsp;properties||array|Property|
|&emsp;&emsp;&emsp;&emsp;accessMode||string||
|&emsp;&emsp;&emsp;&emsp;dataType||DataType|DataType|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;specs||object||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;type||string||
|&emsp;&emsp;&emsp;&emsp;description||string||
|&emsp;&emsp;&emsp;&emsp;icon||Icon|Icon|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;createBy||integer||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;createDept||integer||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;createTime||string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;iconContent||string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;iconName||string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;iconTypeId||integer||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;id||integer||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;tenantId||integer||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;updateBy||integer||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;updateTime||string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;version||string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;viewBox||string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;xmlns||string||
|&emsp;&emsp;&emsp;&emsp;iconId||integer||
|&emsp;&emsp;&emsp;&emsp;identifier||string||
|&emsp;&emsp;&emsp;&emsp;name||string||
|&emsp;&emsp;&emsp;&emsp;proData||string||
|&emsp;&emsp;&emsp;&emsp;unit||string||
|&emsp;&emsp;services||array|Service|
|&emsp;&emsp;&emsp;&emsp;identifier||string||
|&emsp;&emsp;&emsp;&emsp;inputData||array|Parameter|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;dataType||DataType|DataType|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;specs||object||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;type||string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;description||string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;identifier||string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;name||string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;required||boolean||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;unit||string||
|&emsp;&emsp;&emsp;&emsp;name||string||
|&emsp;&emsp;&emsp;&emsp;outputData||array|Parameter|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;dataType||DataType|DataType|
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;specs||object||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;type||string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;description||string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;identifier||string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;name||string||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;required||boolean||
|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;unit||string||
|productKey|产品key|string||


**响应示例**:
```javascript
{
	"id": "",
	"model": {
		"events": [
			{
				"identifier": "",
				"name": "",
				"outputData": [
					{
						"dataType": {
							"specs": {},
							"type": ""
						},
						"description": "",
						"identifier": "",
						"name": "",
						"required": true,
						"unit": ""
					}
				]
			}
		],
		"properties": [
			{
				"accessMode": "",
				"dataType": {
					"specs": {},
					"type": ""
				},
				"description": "",
				"icon": {
					"createBy": 0,
					"createDept": 0,
					"createTime": "",
					"iconContent": "",
					"iconName": "",
					"iconTypeId": 0,
					"id": 0,
					"tenantId": 0,
					"updateBy": 0,
					"updateTime": "",
					"version": "",
					"viewBox": "",
					"xmlns": ""
				},
				"iconId": 0,
				"identifier": "",
				"name": "",
				"proData": "",
				"unit": ""
			}
		],
		"services": [
			{
				"identifier": "",
				"inputData": [
					{}
				],
				"name": "",
				"outputData": [
					{}
				]
			}
		]
	},
	"productKey": ""
}
```


## 添加设备分组


**接口地址**:`/device/group/add`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": {
    "createAt": 0,
    "createBy": 0,
    "createDept": 0,
    "createTime": "",
    "deviceQty": 0,
    "id": "",
    "name": "",
    "remark": "",
    "uid": "",
    "updateBy": 0,
    "updateTime": ""
  },
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|group|group|body|true|Request«DeviceGroupBo»|Request«DeviceGroupBo»|
|&emsp;&emsp;data|||false|DeviceGroupBo|DeviceGroupBo|
|&emsp;&emsp;&emsp;&emsp;createAt|创建时间||false|integer||
|&emsp;&emsp;&emsp;&emsp;createBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createDept|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createTime|||false|string||
|&emsp;&emsp;&emsp;&emsp;deviceQty|设备数量||false|integer||
|&emsp;&emsp;&emsp;&emsp;id|分组id||false|string||
|&emsp;&emsp;&emsp;&emsp;name|设备组名称||false|string||
|&emsp;&emsp;&emsp;&emsp;remark|分组说明||false|string||
|&emsp;&emsp;&emsp;&emsp;uid|所属用户||false|string||
|&emsp;&emsp;&emsp;&emsp;updateBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;updateTime|||false|string||
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 添加设备到组


**接口地址**:`/device/group/addDevices`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": {
    "createBy": 0,
    "createDept": 0,
    "createTime": "",
    "devices": [],
    "group": "",
    "updateBy": 0,
    "updateTime": ""
  },
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|bo|bo|body|true|Request«DeviceAddGroupBo»|Request«DeviceAddGroupBo»|
|&emsp;&emsp;data|||false|DeviceAddGroupBo|DeviceAddGroupBo|
|&emsp;&emsp;&emsp;&emsp;createBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createDept|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createTime|||false|string||
|&emsp;&emsp;&emsp;&emsp;devices|设备列表||false|array|string|
|&emsp;&emsp;&emsp;&emsp;group|组id||false|string||
|&emsp;&emsp;&emsp;&emsp;updateBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;updateTime|||false|string||
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 清空组下所有设备


**接口地址**:`/device/group/clear`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": "",
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|request|request|body|true|Request«string»|Request«string»|
|&emsp;&emsp;data|||false|string||
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 删除分组


**接口地址**:`/device/group/delete`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": "",
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|request|request|body|true|Request«string»|Request«string»|
|&emsp;&emsp;data|||false|string||
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 修改设备分组


**接口地址**:`/device/group/edit`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": {
    "createAt": 0,
    "createBy": 0,
    "createDept": 0,
    "createTime": "",
    "deviceQty": 0,
    "id": "",
    "name": "",
    "remark": "",
    "uid": "",
    "updateBy": 0,
    "updateTime": ""
  },
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|bo|bo|body|true|Request«DeviceGroupBo»|Request«DeviceGroupBo»|
|&emsp;&emsp;data|||false|DeviceGroupBo|DeviceGroupBo|
|&emsp;&emsp;&emsp;&emsp;createAt|创建时间||false|integer||
|&emsp;&emsp;&emsp;&emsp;createBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createDept|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createTime|||false|string||
|&emsp;&emsp;&emsp;&emsp;deviceQty|设备数量||false|integer||
|&emsp;&emsp;&emsp;&emsp;id|分组id||false|string||
|&emsp;&emsp;&emsp;&emsp;name|设备组名称||false|string||
|&emsp;&emsp;&emsp;&emsp;remark|分组说明||false|string||
|&emsp;&emsp;&emsp;&emsp;uid|所属用户||false|string||
|&emsp;&emsp;&emsp;&emsp;updateBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;updateTime|||false|string||
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 下载设备分组模板


**接口地址**:`/device/group/exportData`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


暂无


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 导入设备分组


**接口地址**:`/device/group/importData`


**请求方式**:`POST`


**请求数据类型**:`multipart/form-data`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|file|file|formData|true|file||
|requestId|requestId|query|true|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|Response|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|code||integer(int32)|integer(int32)|
|data||object||
|message||string||
|requestId||string||


**响应示例**:
```javascript
{
	"code": 0,
	"data": {},
	"message": "",
	"requestId": ""
}
```


## 将设备从组中移除


**接口地址**:`/device/group/removeDevices`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": {
    "createBy": 0,
    "createDept": 0,
    "createTime": "",
    "devices": [],
    "group": "",
    "updateBy": 0,
    "updateTime": ""
  },
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|bo|bo|body|true|Request«DeviceAddGroupBo»|Request«DeviceAddGroupBo»|
|&emsp;&emsp;data|||false|DeviceAddGroupBo|DeviceAddGroupBo|
|&emsp;&emsp;&emsp;&emsp;createBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createDept|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createTime|||false|string||
|&emsp;&emsp;&emsp;&emsp;devices|设备列表||false|array|string|
|&emsp;&emsp;&emsp;&emsp;group|组id||false|string||
|&emsp;&emsp;&emsp;&emsp;updateBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;updateTime|||false|string||
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 获取分组列表


**接口地址**:`/device/groups/list`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": {
    "createAt": 0,
    "createBy": 0,
    "createDept": 0,
    "createTime": "",
    "deviceQty": 0,
    "id": "",
    "name": "",
    "remark": "",
    "uid": "",
    "updateBy": 0,
    "updateTime": ""
  },
  "pageNum": 0,
  "pageSize": 0,
  "requestId": "",
  "sortMap": {}
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|pageRequest|pageRequest|body|true|PageRequest«DeviceGroupBo»|PageRequest«DeviceGroupBo»|
|&emsp;&emsp;data|||false|DeviceGroupBo|DeviceGroupBo|
|&emsp;&emsp;&emsp;&emsp;createAt|创建时间||false|integer||
|&emsp;&emsp;&emsp;&emsp;createBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createDept|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createTime|||false|string||
|&emsp;&emsp;&emsp;&emsp;deviceQty|设备数量||false|integer||
|&emsp;&emsp;&emsp;&emsp;id|分组id||false|string||
|&emsp;&emsp;&emsp;&emsp;name|设备组名称||false|string||
|&emsp;&emsp;&emsp;&emsp;remark|分组说明||false|string||
|&emsp;&emsp;&emsp;&emsp;uid|所属用户||false|string||
|&emsp;&emsp;&emsp;&emsp;updateBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;updateTime|||false|string||
|&emsp;&emsp;pageNum|||false|integer(int32)||
|&emsp;&emsp;pageSize|||false|integer(int32)||
|&emsp;&emsp;requestId|||false|string||
|&emsp;&emsp;sortMap|||false|object||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|Paging«DeviceGroupVo»|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|rows||array|DeviceGroupVo|
|&emsp;&emsp;createAt|创建时间|integer(int64)||
|&emsp;&emsp;deviceQty|设备数量|integer(int32)||
|&emsp;&emsp;id|设备组id|string||
|&emsp;&emsp;name|设备组名称|string||
|&emsp;&emsp;remark|分组说明|string||
|&emsp;&emsp;uid|所属用户|string||
|total||integer(int64)|integer(int64)|


**响应示例**:
```javascript
{
	"rows": [
		{
			"createAt": 0,
			"deviceQty": 0,
			"id": "",
			"name": "",
			"remark": "",
			"uid": ""
		}
	],
	"total": 0
}
```


## 导入设备


**接口地址**:`/device/importData`


**请求方式**:`POST`


**请求数据类型**:`multipart/form-data`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|file|file|formData|true|file||
|requestId|requestId|query|true|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|Response|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|code||integer(int32)|integer(int32)|
|data||object||
|message||string||
|requestId||string||


**响应示例**:
```javascript
{
	"code": 0,
	"data": {},
	"message": "",
	"requestId": ""
}
```


## 设备列表


**接口地址**:`/device/list`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:<p>设备列表</p>



**请求示例**:


```javascript
{
  "data": {
    "createBy": 0,
    "createDept": 0,
    "createTime": "",
    "deviceId": "",
    "deviceName": "",
    "group": "",
    "keyword": "",
    "model": "",
    "online": true,
    "parentId": "",
    "productKey": "",
    "uid": "",
    "updateBy": 0,
    "updateTime": ""
  },
  "pageNum": 0,
  "pageSize": 0,
  "requestId": "",
  "sortMap": {}
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|pageRequest|pageRequest|body|true|PageRequest«DeviceQueryBo»|PageRequest«DeviceQueryBo»|
|&emsp;&emsp;data|||false|DeviceQueryBo|DeviceQueryBo|
|&emsp;&emsp;&emsp;&emsp;createBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createDept|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createTime|||false|string||
|&emsp;&emsp;&emsp;&emsp;deviceId|设备id||false|string||
|&emsp;&emsp;&emsp;&emsp;deviceName|设备名称||false|string||
|&emsp;&emsp;&emsp;&emsp;group|分组||false|string||
|&emsp;&emsp;&emsp;&emsp;keyword|关键字||false|string||
|&emsp;&emsp;&emsp;&emsp;model|设备类型||false|string||
|&emsp;&emsp;&emsp;&emsp;online|设备状态||false|boolean||
|&emsp;&emsp;&emsp;&emsp;parentId|父级id||false|string||
|&emsp;&emsp;&emsp;&emsp;productKey|产品key||false|string||
|&emsp;&emsp;&emsp;&emsp;uid|用户id||false|string||
|&emsp;&emsp;&emsp;&emsp;updateBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;updateTime|||false|string||
|&emsp;&emsp;pageNum|||false|integer(int32)||
|&emsp;&emsp;pageSize|||false|integer(int32)||
|&emsp;&emsp;requestId|||false|string||
|&emsp;&emsp;sortMap|||false|object||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|Paging«DeviceInfoVo»|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|rows||array|DeviceInfoVo|
|&emsp;&emsp;createAt|创建时间|integer(int64)||
|&emsp;&emsp;deviceId|设备id|string||
|&emsp;&emsp;deviceName|设备名称|string||
|&emsp;&emsp;group|所属分组|Group|Group|
|&emsp;&emsp;&emsp;&emsp;id||string||
|&emsp;&emsp;&emsp;&emsp;name||string||
|&emsp;&emsp;id||string||
|&emsp;&emsp;locate|位置信息|Locate|Locate|
|&emsp;&emsp;&emsp;&emsp;latitude||string||
|&emsp;&emsp;&emsp;&emsp;longitude||string||
|&emsp;&emsp;model|设备类型|string||
|&emsp;&emsp;offlineTime|设备离线时间|integer(int64)||
|&emsp;&emsp;online|设备状态|boolean||
|&emsp;&emsp;onlineTime|设备在线时间|integer(int64)||
|&emsp;&emsp;parentId|父级id|string||
|&emsp;&emsp;product|所属产品信息|Product|Product|
|&emsp;&emsp;&emsp;&emsp;category||string||
|&emsp;&emsp;&emsp;&emsp;createAt||integer||
|&emsp;&emsp;&emsp;&emsp;createBy||integer||
|&emsp;&emsp;&emsp;&emsp;createDept||integer||
|&emsp;&emsp;&emsp;&emsp;createTime||string||
|&emsp;&emsp;&emsp;&emsp;iconId||integer||
|&emsp;&emsp;&emsp;&emsp;id||integer||
|&emsp;&emsp;&emsp;&emsp;img||string||
|&emsp;&emsp;&emsp;&emsp;isOpenLocate||boolean||
|&emsp;&emsp;&emsp;&emsp;keepAliveTime||integer||
|&emsp;&emsp;&emsp;&emsp;locateUpdateType||string||
|&emsp;&emsp;&emsp;&emsp;name||string||
|&emsp;&emsp;&emsp;&emsp;nodeType||integer||
|&emsp;&emsp;&emsp;&emsp;productKey||string||
|&emsp;&emsp;&emsp;&emsp;productSecret||string||
|&emsp;&emsp;&emsp;&emsp;tenantId||integer||
|&emsp;&emsp;&emsp;&emsp;transparent||boolean||
|&emsp;&emsp;&emsp;&emsp;uid||string||
|&emsp;&emsp;&emsp;&emsp;updateBy||integer||
|&emsp;&emsp;&emsp;&emsp;updateTime||string||
|&emsp;&emsp;productKey|产品key|string||
|&emsp;&emsp;secret|设备描述|string||
|total||integer(int64)|integer(int64)|


**响应示例**:
```javascript
{
	"rows": [
		{
			"createAt": 0,
			"deviceId": "",
			"deviceName": "",
			"group": {
				"additionalProperties1": {
					"id": "",
					"name": ""
				}
			},
			"id": "",
			"locate": {
				"latitude": "",
				"longitude": ""
			},
			"model": "",
			"offlineTime": 0,
			"online": true,
			"onlineTime": 0,
			"parentId": "",
			"product": {
				"category": "",
				"createAt": 0,
				"createBy": 0,
				"createDept": 0,
				"createTime": "",
				"iconId": 0,
				"id": 0,
				"img": "",
				"isOpenLocate": true,
				"keepAliveTime": 0,
				"locateUpdateType": "",
				"name": "",
				"nodeType": 0,
				"productKey": "",
				"productSecret": "",
				"tenantId": 0,
				"transparent": true,
				"uid": "",
				"updateBy": 0,
				"updateTime": ""
			},
			"productKey": "",
			"secret": ""
		}
	],
	"total": 0
}
```


## 保存设备


**接口地址**:`/device/save`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": {
    "createAt": 0,
    "createBy": 0,
    "createDept": 0,
    "createTime": "",
    "deviceId": "",
    "deviceName": "",
    "id": "",
    "latitude": "",
    "longitude": "",
    "model": "",
    "offlineTime": 0,
    "onlineTime": 0,
    "parentId": "",
    "productKey": "",
    "secret": "",
    "uid": "",
    "updateBy": 0,
    "updateTime": ""
  },
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|bo|bo|body|true|Request«DeviceInfoBo»|Request«DeviceInfoBo»|
|&emsp;&emsp;data|||false|DeviceInfoBo|DeviceInfoBo|
|&emsp;&emsp;&emsp;&emsp;createAt|创建时间||false|integer||
|&emsp;&emsp;&emsp;&emsp;createBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createDept|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createTime|||false|string||
|&emsp;&emsp;&emsp;&emsp;deviceId|设备id||false|string||
|&emsp;&emsp;&emsp;&emsp;deviceName|设备名称||false|string||
|&emsp;&emsp;&emsp;&emsp;id|||false|string||
|&emsp;&emsp;&emsp;&emsp;latitude|纬度||false|string||
|&emsp;&emsp;&emsp;&emsp;longitude|经度||false|string||
|&emsp;&emsp;&emsp;&emsp;model|设备类型||false|string||
|&emsp;&emsp;&emsp;&emsp;offlineTime|设备离线时间||false|integer||
|&emsp;&emsp;&emsp;&emsp;onlineTime|设备在线时间||false|integer||
|&emsp;&emsp;&emsp;&emsp;parentId|父级id||false|string||
|&emsp;&emsp;&emsp;&emsp;productKey|产品key||false|string||
|&emsp;&emsp;&emsp;&emsp;secret|设备描述||false|string||
|&emsp;&emsp;&emsp;&emsp;uid|用户id||false|string||
|&emsp;&emsp;&emsp;&emsp;updateBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;updateTime|||false|string||
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 服务调用


**接口地址**:`/device/service/invoke`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:<p>服务调用</p>



**请求示例**:


```javascript
{
  "data": {
    "args": {},
    "deviceId": "",
    "service": ""
  },
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|request|request|body|true|Request«ServiceInvokeBo»|Request«ServiceInvokeBo»|
|&emsp;&emsp;data|||false|ServiceInvokeBo|ServiceInvokeBo|
|&emsp;&emsp;&emsp;&emsp;args|参数||false|object||
|&emsp;&emsp;&emsp;&emsp;deviceId|设备id||true|string||
|&emsp;&emsp;&emsp;&emsp;service|服务||true|string||
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|InvokeResult|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|requestId||string||
|time||integer(int64)|integer(int64)|


**响应示例**:
```javascript
{
	"requestId": "",
	"time": 0
}
```


## 属性获取


**接口地址**:`/device/service/property/get`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:<p>属性获取</p>



**请求示例**:


```javascript
{
  "data": {
    "deviceId": "",
    "propertyNames": []
  },
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|request|request|body|true|Request«GetDeviceServicePorpertyBo»|Request«GetDeviceServicePorpertyBo»|
|&emsp;&emsp;data|||false|GetDeviceServicePorpertyBo|GetDeviceServicePorpertyBo|
|&emsp;&emsp;&emsp;&emsp;deviceId|设备id||true|string||
|&emsp;&emsp;&emsp;&emsp;propertyNames|属性列表||false|array|string|
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|InvokeResult|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|requestId||string||
|time||integer(int64)|integer(int64)|


**响应示例**:
```javascript
{
	"requestId": "",
	"time": 0
}
```


## 属性设置


**接口地址**:`/device/service/property/set`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:<p>属性设置</p>



**请求示例**:


```javascript
{
  "data": {
    "args": {},
    "deviceId": ""
  },
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|request|request|body|true|Request«SetDeviceServicePorpertyBo»|Request«SetDeviceServicePorpertyBo»|
|&emsp;&emsp;data|||false|SetDeviceServicePorpertyBo|SetDeviceServicePorpertyBo|
|&emsp;&emsp;&emsp;&emsp;args|参数||false|object||
|&emsp;&emsp;&emsp;&emsp;deviceId|设备id||true|string||
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|InvokeResult|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|requestId||string||
|time||integer(int64)|integer(int64)|


**响应示例**:
```javascript
{
	"requestId": "",
	"time": 0
}
```


## 设备影子创建


**接口地址**:`/device/shadow/createShadow`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": {
    "code": 0,
    "createBy": 0,
    "createDept": 0,
    "createTime": "",
    "data": {},
    "deviceId": "",
    "deviceName": "",
    "from": "",
    "id": "",
    "identifier": "",
    "mid": "",
    "occurred": 0,
    "productKey": "",
    "time": 0,
    "type": "",
    "uid": "",
    "updateBy": 0,
    "updateTime": ""
  },
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|bo|bo|body|true|Request«ThingModelMessageBo»|Request«ThingModelMessageBo»|
|&emsp;&emsp;data|||false|ThingModelMessageBo|ThingModelMessageBo|
|&emsp;&emsp;&emsp;&emsp;code|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createDept|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createTime|||false|string||
|&emsp;&emsp;&emsp;&emsp;data|||false|object||
|&emsp;&emsp;&emsp;&emsp;deviceId|||false|string||
|&emsp;&emsp;&emsp;&emsp;deviceName|||false|string||
|&emsp;&emsp;&emsp;&emsp;from|||false|string||
|&emsp;&emsp;&emsp;&emsp;id|||false|string||
|&emsp;&emsp;&emsp;&emsp;identifier|||false|string||
|&emsp;&emsp;&emsp;&emsp;mid|||false|string||
|&emsp;&emsp;&emsp;&emsp;occurred|||false|integer||
|&emsp;&emsp;&emsp;&emsp;productKey|||false|string||
|&emsp;&emsp;&emsp;&emsp;time|||false|integer||
|&emsp;&emsp;&emsp;&emsp;type|||false|string||
|&emsp;&emsp;&emsp;&emsp;uid|||false|string||
|&emsp;&emsp;&emsp;&emsp;updateBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;updateTime|||false|string||
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 设备影子获取


**接口地址**:`/device/shadow/getShadow`


**请求方式**:`GET`


**请求数据类型**:`application/x-www-form-urlencoded`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|deviceId|deviceId|query|true|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|ThingModelMessage|
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|code||integer(int32)|integer(int32)|
|data||object||
|deviceId||string||
|deviceName||string||
|id||string||
|identifier||string||
|mid||string||
|occurred||integer(int64)|integer(int64)|
|productKey||string||
|time||integer(int64)|integer(int64)|
|type||string||
|uid||string||


**响应示例**:
```javascript
[
	{
		"code": 0,
		"data": {},
		"deviceId": "",
		"deviceName": "",
		"id": "",
		"identifier": "",
		"mid": "",
		"occurred": 0,
		"productKey": "",
		"time": 0,
		"type": "",
		"uid": ""
	}
]
```


## 模拟设备上报


**接口地址**:`/device/simulateSend`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": {
    "code": 0,
    "createBy": 0,
    "createDept": 0,
    "createTime": "",
    "data": {},
    "deviceId": "",
    "deviceName": "",
    "from": "",
    "id": "",
    "identifier": "",
    "mid": "",
    "occurred": 0,
    "productKey": "",
    "time": 0,
    "type": "",
    "uid": "",
    "updateBy": 0,
    "updateTime": ""
  },
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|bo|bo|body|true|Request«ThingModelMessageBo»|Request«ThingModelMessageBo»|
|&emsp;&emsp;data|||false|ThingModelMessageBo|ThingModelMessageBo|
|&emsp;&emsp;&emsp;&emsp;code|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createDept|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createTime|||false|string||
|&emsp;&emsp;&emsp;&emsp;data|||false|object||
|&emsp;&emsp;&emsp;&emsp;deviceId|||false|string||
|&emsp;&emsp;&emsp;&emsp;deviceName|||false|string||
|&emsp;&emsp;&emsp;&emsp;from|||false|string||
|&emsp;&emsp;&emsp;&emsp;id|||false|string||
|&emsp;&emsp;&emsp;&emsp;identifier|||false|string||
|&emsp;&emsp;&emsp;&emsp;mid|||false|string||
|&emsp;&emsp;&emsp;&emsp;occurred|||false|integer||
|&emsp;&emsp;&emsp;&emsp;productKey|||false|string||
|&emsp;&emsp;&emsp;&emsp;time|||false|integer||
|&emsp;&emsp;&emsp;&emsp;type|||false|string||
|&emsp;&emsp;&emsp;&emsp;uid|||false|string||
|&emsp;&emsp;&emsp;&emsp;updateBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;updateTime|||false|string||
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 添加标签


**接口地址**:`/device/tag/add`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": {
    "createBy": 0,
    "createDept": 0,
    "createTime": "",
    "deviceId": "",
    "id": "",
    "name": "",
    "updateBy": 0,
    "updateTime": "",
    "value": ""
  },
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|bo|bo|body|true|Request«DeviceTagAddBo»|Request«DeviceTagAddBo»|
|&emsp;&emsp;data|||false|DeviceTagAddBo|DeviceTagAddBo|
|&emsp;&emsp;&emsp;&emsp;createBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createDept|||false|integer||
|&emsp;&emsp;&emsp;&emsp;createTime|||false|string||
|&emsp;&emsp;&emsp;&emsp;deviceId|设备||false|string||
|&emsp;&emsp;&emsp;&emsp;id|tag id||false|string||
|&emsp;&emsp;&emsp;&emsp;name|tag名称||false|string||
|&emsp;&emsp;&emsp;&emsp;updateBy|||false|integer||
|&emsp;&emsp;&emsp;&emsp;updateTime|||false|string||
|&emsp;&emsp;&emsp;&emsp;value|tag值||false|string||
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


暂无


**响应示例**:
```javascript

```


## 设备解绑


**接口地址**:`/device/unbind`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求示例**:


```javascript
{
  "data": "",
  "requestId": ""
}
```


**请求参数**:


| 参数名称 | 参数说明 | 请求类型    | 是否必须 | 数据类型 | schema |
| -------- | -------- | ----- | -------- | -------- | ------ |
|request|request|body|true|Request«string»|Request«string»|
|&emsp;&emsp;data|||false|string||
|&emsp;&emsp;requestId|||false|string||


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK||
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


暂无


**响应示例**:
```javascript

```


# 验证码


## 生成验证码


**接口地址**:`/code`


**请求方式**:`POST`


**请求数据类型**:`application/json`


**响应数据类型**:`*/*`


**接口描述**:


**请求参数**:


暂无


**响应状态**:


| 状态码 | 说明 | schema |
| -------- | -------- | ----- | 
|200|OK|CaptchaVo|
|201|Created||
|401|Unauthorized||
|403|Forbidden||
|404|Not Found||


**响应参数**:


| 参数名称 | 参数说明 | 类型 | schema |
| -------- | -------- | ----- |----- | 
|captchaEnabled||boolean||
|img||string||
|uuid||string||


**响应示例**:
```javascript
{
	"captchaEnabled": true,
	"img": "",
	"uuid": ""
}
```