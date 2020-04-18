import re,urllib.request,urllib.response,urllib.error,time,xlwt,xlrd

year='17'
fileBaseUrl='http://www.chemspider.com/FilesHandler.ashx?type=str&striph=yes&id='
f=open(year+'.html','r', encoding='utf-8')
content=f.read()
f.close()

pattern = re.compile(r'http://www.chemspider.com/chemical-structure.*?>\d+<',re.S)
results = pattern.findall(content)

wbk = xlwt.Workbook()
sheet = wbk.add_sheet("20"+year)
column=0
raw=0

for result in results:
    column=0
    patternF = re.compile(r'>\d+<',re.S)
    resutlF = patternF.search(result)
    _no=resutlF.group(0).replace('<','').replace('>','');
    patternHref = re.compile(r'www.chemspider.com/chemical-structure.*?.html',re.S)
    resutlHref = patternHref.search(result)
    fileId=re.compile(r'\d+',re.S).search(resutlHref.group(0)).group(0)
    print(_no+"    "+fileBaseUrl+fileId)

    print(_no+":"+resutlHref.group(0)+":"+fileBaseUrl+fileId)
    urllib.request.urlretrieve(fileBaseUrl+fileId, _no+".mol")
    if(raw%5==0):
        print('休眠')
        time.sleep(1)
    
    #sheet.write(raw,column,_no)
    #column+=1
    #sheet.write(raw,column,fileId)
    #column+=1
    #sheet.write(raw,column,fileBaseUrl+fileId)
    raw+=1


#wbk.save(year+'url.xls')
