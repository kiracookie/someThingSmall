import os,urllib.request,sys,json;


#获取bing背景图片


type = sys.getfilesystemencoding() #

baseUrl="http://cn.bing.com";

picApiUrl = baseUrl+"/HPImageArchive.aspx?format=js&n=100" #网页地址

response = urllib.request.urlopen(picApiUrl) #打开链接

baseFilePath="C:\\Users\\kai.zang\\Pictures\\";#硬盘路径

print("当前文件路径："+baseFilePath);

webContent=bytes.decode(response.read());#读取数据

json_to_python = json.loads(webContent)#json转对象

imageslist=json_to_python['images']; #获取图片列表

for image in imageslist:
    picUrl=baseUrl+ image['url'] ; #获取图片url
    
    print(picUrl);

    #文件相关逻辑
    
    fileNames=picUrl.split("/");
    
    fileName=fileNames[len(fileNames)-1]

    exts=fileName.split('.')

    ext=exts[len(exts)-1]

    picResponse=urllib.request.urlopen(picUrl);

    file = open(baseFilePath+fileName,"wb") #打开一个文本文件

    file.write( picResponse.read()  ) #写入数据

    file.flush();

    file.close() #关闭文件

