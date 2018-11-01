# 模块名 repair
##1、 维保人员查看可接单
#### 请求地址
'''
GET  /repairs
'''
#### 请求参数

name              |type  |NN|comments
-------        -  |------|--|----------------------
weibao_acount     |string|  |维保人员账号

#### 响应  
##### 200 

name              |type  |NN|comments
-------        -  |------|--|----------------------
title             |string|  |所有维修表单标题

## 2、维保人员查看已接单  
#### 请求地址
'''
GET  /receipts/weibao_account
'''
#### 请求参数

name              |type  |NN|comments
--------          |------|--|------------------------
weibao_account    |string|  |维修人员账号

#### 响应
##### 200

name              |type  |NN|comments
-------        -  |------|--|----------------------
title             |string|  |所有已接维修表单标题
 
## 3、抢单
#### 请求地址
'''
UPDATA  /repair
'''
#### 请求参数
name      |type   |NN|comments
-----     |----   |--|----------------------
number_id |string |  |维修表单id

#### 响应
##### 200

name          |type  |comments
------------ -|--- --|----------------------
status        |string| 维修表单接单标识改为‘1’
weibao_account|string|添加维保人员账号
receive_time  |DATE  |添加接单时间

如果查看维修单详情的时候，维修单被其他人接取，则无法完成接单操作

##4、完成单
#### 请求地址
'''
UPDATA  /repairing
'''

####请求参数
name          |type   |NN|comments
-----         |----   |--|----------------------
number_id     |string |  |维保单id

#### 响应
#### 200

name         |type  |comments
-------------|--- --|----------------------
finish_status|string| 维修表单接单标识改为‘1’
reason       |string|添加问题原因
solve_way    |string|添加解决办法

