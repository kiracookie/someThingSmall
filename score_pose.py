import os,urllib.request,sys,json,cgi,xlwt,xlrd,re,shutil;


#获取当前路径

rootdir=os.getcwd()

# print(rootdir)

maxScore=-3#设定对比值

list = os.listdir(rootdir) #列出文件夹下所有的目录与文件

#excel初始坐标
column=0
row=0

wbk = xlwt.Workbook()
sheet = wbk.add_sheet('sheet1')
sheet.write(row,column,'文件名')
column+=1
sheet.write(row,column,'pose')
column+=1
sheet.write(row,column,'score')

for file in  list :
	# 判断不为目录且dok 
 if os.path.isfile(file) and ".dok" in file:
    file_path=file.replace('.dok','')
    # print(file)
    current_file=open(rootdir+"\\"+file, mode='r')
    file_content=current_file.read()
    # print(file_content)
    pattern = re.compile(r'^REMARK Cluster+.+mol$',re.M)
    results = pattern.findall(file_content)
    # print(results)
    if_move_file=False
    for result in results:
        pose_score=result.replace('REMARK Cluster  ','').replace(' of Poses:  ',',').replace(' Score: ',',').replace(' kcal/mol','').split(',')
        if float(pose_score[2])<maxScore:
            #写入excel部分
            column=0
            row+=1
            sheet.write(row,column,file)
            column+=1
            sheet.write(row,column,int(pose_score[0]))
            column+=1
            sheet.write(row,column,float(pose_score[2]))
            if_move_file=True
            
    #移动文件部分
            #TODO 关联另外一个文件
    if if_move_file:
      if not os.path.exists(file_path):
          os.mkdir(file_path)
    print(file+"=="+file_path+'/'+file)
    shutil.copyfile(file,file_path+'/'+file)
wbk.save('resutl.xls')        
print("写入结束")
