import json
import re
import csv
import xlrd
import xlwt

x = {
    "errcode": 0,
    "errmsg": "操作成功",
    "list_data": [
        {
            "user_id": "-1",
            "card_num": "10000208",
            "card_value": "100000000",
            "stakeholder_name": "测试014",
            "deadline": "2018-12-25",
            "eq_integral_value": "0",
            "received": "0",
            "wait_release": "0",
            "bindtime": "0000-00-00 00:00:00",
            "card_pass": "03b9JyRyXhxzJqpRrk1r3HaAA7XPVS69o3N3ZBDGhhDvS9g",
            "bind": "未绑定",
            "valid": "2018\/12\/25",
            "binddate": "-",
            "op_btn": "<button class=\"td-btn primary\" onclick=\"copy('10000208')\">复制卡密<\/button>\n                            <input type=\"hidden\" value='权益卡卡号：10000208 密码：BGodxM，使用方法：登录APP-我的-我的权益卡内进行绑定即可' name='copy_10000208'>\n                            <button class=\"td-btn primary\" data-target=\"#changeTime\" data-toggle=\"modal\" onclick=\"getid('10000208')\">变更期限<\/button>\n                            <button class=\"td-btn primary\" onclick=\"window.location.href = '.\/index.php?m=equity&a=detail&card_num=10000208'\">详情<\/button>"
        },
        {
            "user_id": "-1",
            "card_num": "10000207",
            "card_value": "100000000",
            "stakeholder_name": "测试013",
            "deadline": "2018-12-24",
            "eq_integral_value": "0",
            "received": "0",
            "wait_release": "0",
            "bindtime": "0000-00-00 00:00:00",
            "card_pass": "da8bMnvmQohBp4uqwOrZSQWu2v65tC187\/1MpkUE1\/5aoEY",
            "bind": "未绑定",
            "valid": "2018\/12\/24",
            "binddate": "-",
            "op_btn": "<button class=\"td-btn primary\" onclick=\"copy('10000207')\">复制卡密<\/button>\n                            <input type=\"hidden\" value='权益卡卡号：10000207 密码：QoZfC9，使用方法：登录APP-我的-我的权益卡内进行绑定即可' name='copy_10000207'>\n                            <button class=\"td-btn primary\" data-target=\"#changeTime\" data-toggle=\"modal\" onclick=\"getid('10000207')\">变更期限<\/button>\n                            <button class=\"td-btn primary\" onclick=\"window.location.href = '.\/index.php?m=equity&a=detail&card_num=10000207'\">详情<\/button>"
        }
        ]
        }

s = x['list_data'][0]['op_btn']
print(s)
result1 = re.findall('权益卡卡号：(\d+)', s)
result2 = re.findall('密码：(\w+)', s)
print(result1)
print(result2)
mapz = (result1 + result2)
print(mapz)


#测试xlwt
#创建新的excel文件
newfile = xlwt.Workbook()
#创建新的表单
#addsheet的格式add_sheet(sheetname, cell_overwrite_ok=False)
newsheet = newfile.add_sheet('test1',cell_overwrite_ok=True)
#索引从0，0开始
newsheet.write(0,0,mapz[0])
newsheet.write(0,1,mapz[1])
newfile.save('firsttest.xls')
 
#打开相应的excel文件
workbook = xlrd.open_workbook(r'firsttest.xls')
#找到相应的sheet
#可以通过index，index从0开始计算
#也可以通过sheet的名字 
rdsheet = workbook.sheet_by_index(0) 
rdsheet = workbook.sheet_by_name('test1')
print(rdsheet.cell(0,0))
#cell函数返回的是Cell 对象）包含ctype value xf_index
#输出number:10.0
print(rdsheet.cell(0,0).ctype)
#输出2？使用type查询结果为:<type 'member_descriptor'>具体含义？
print(rdsheet.cell(0,0).value)
#输出10.0
print(rdsheet.cell(0,0).xf_index)
#输出None
 
# rdbook = xlrd.open_workbook(r'firsttest.xls')
# wtbook = copy.copy(rdbook)
# wtsheet = wtbook.get_sheet(0)
# type(wtsheet)
# wtsheet.write(0,0,'aaaaa')
# wtbook.save('bb.xls')
 
# newrdbook = xlrd.open_workbook(r'bb.xls')
# print(newrdbook.sheet_by_name('test1').cell(0,0))
# #输出text:'aaaaa'
# print(rdbook.sheet_by_index(0).cell(0,0))
# #输出number:10.0
