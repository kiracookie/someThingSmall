import os,urllib.request,sys,json,cgi,re,shutil;


#获取当前路径

rootdir=os.getcwd()

result_file_path='diresult'          #结果文件夹

result_excel_name='result.txt'             #结果excel名称

pdb_path='I:\TDDOWNLOAD\someThingSmall'#pdb文件夹路径

dok_path='I:\TDDOWNLOAD\someThingSmall'#dok文件夹路径


maxScore=-7#设定对比值

list = os.listdir(dok_path) #列出文件夹下所有的目录与文件

# print(list)

#excel初始坐标
column=0
row=0

# wbk = xlwt.Workbook()
# sheet = wbk.add_sheet('sheet1')
# sheet.write(row,column,'文件名')
# column+=1
# sheet.write(row,column,'pose')
# column+=1
# sheet.write(row,column,'score')

               #创建result文件夹
if not os.path.exists(result_file_path):
    os.mkdir(result_file_path)
    #清空文件内容
with open(result_file_path+os.path.sep+result_excel_name,'w') as f:
    f.write('')
for file in  list :
	# 判断不为目录且dok 
 if not os.path.isfile(file) and ".dok" in file:
    file_path=file.replace('.dok','')
    # print(file)
    current_file=open(dok_path+os.path.sep+file, mode='r')
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
            # column=0
            # row+=1
            # sheet.write(row,column,file)
            # column+=1
            # sheet.write(row,column,int(pose_score[0]))
            # column+=1
            # sheet.write(row,column,float(pose_score[2]))
            if_move_file=True
            break


    #移动文件部分
    if if_move_file:
        with open(result_file_path+os.path.sep+result_excel_name,'a+') as f:
            f.write(file+':\n')
        for result in results:
            with open(result_file_path+os.path.sep+result_excel_name,'a+') as f:
                f.write(result+'\n')
        if not os.path.exists(result_file_path+os.path.sep+file_path):
            os.mkdir(result_file_path+os.path.sep+file_path)
            #复制dok文件到结果目录
        shutil.copyfile(dok_path+os.path.sep+file,result_file_path+os.path.sep+file_path+os.path.sep+file)
             #复制pdb文件到结果目录
        shutil.copyfile(pdb_path+os.path.sep+file.replace('dok','pdb'),result_file_path+os.path.sep+file_path+os.path.sep+file.replace('dok','pdb'))
# wbk.save(result_file_path+os.path.sep+result_excel_name)
print("写入结束")
