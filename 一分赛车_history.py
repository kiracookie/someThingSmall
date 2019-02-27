import os,urllib.request,sys,json,cgi,xlwt,xlrd;

#获取一分钟赛车历史

type = sys.getfilesystemencoding() #

baseUrl="https://luck96.com/kaijiangweb/"

histroyMethod="getHistoryList.do"

excelPath="D:\\445915\\resource\\一分钟赛车\\"#硬盘路径

searchTime = input("输入查询日期格式为yyyy-MM-dd: ");

lotCode="JSSC60"

requestUrl=baseUrl+histroyMethod+"?date="+searchTime+"&lotCode="+lotCode
print("当前文件路径："+excelPath+searchTime)

print("请求url:"+requestUrl)

response = urllib.request.urlopen(requestUrl) #打开链接

webContent=bytes.decode(response.read());#读取数据

json_to_python = json.loads(webContent)#json转对象

results=json_to_python['result']; #获取图片列表

column=0
raw=0

wbk = xlwt.Workbook()
sheet = wbk.add_sheet(searchTime)
sheet.write(raw,column,'期数')
column+=1
sheet.write(raw,column,'号码')
    
for result in results:
    column=0
    raw+=1
    sheet.write(raw,column,result['preDrawIssue'])
    column+=1
    sheet.write(raw,column,",".join('%s' %id for id in result['preDrawCode']))
    
wbk.save(excelPath+searchTime+'.xls')

print("写入结束")