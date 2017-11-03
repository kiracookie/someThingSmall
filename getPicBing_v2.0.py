import os,urllib.request,sys,json,cgi;


#获取bing背景图片


type = sys.getfilesystemencoding() #

baseUrl="http://cn.bing.com";

picApiUrl = baseUrl+"/HPImageArchive.aspx?format=js&n=100" #网页地址

response = urllib.request.urlopen(picApiUrl) #打开链接

baseFilePath="D:\\445915\\resource\\BingPics\\";#硬盘路径

print("当前文件路径："+baseFilePath);

webContent=bytes.decode(response.read());#读取数据

json_to_python = json.loads(webContent)#json转对象

imageslist=json_to_python['images']; #获取图片列表

for image in imageslist:
    picUrl=baseUrl+ image['url'] ; #获取图片url
    picUrlHsh=baseUrl+ '/hpwp/'+image['hsh'] ;
    
    print(picUrl);
    print(picUrlHsh);


    #文件相关逻辑


# 背景图片
    picResponse=urllib.request.urlopen(picUrl);

    fileNames=picUrl.split("/");

    fileName=fileNames[len(fileNames)-1]

    exts=fileName.split('.')

    ext=exts[len(exts)-1]

    file = open(baseFilePath+fileName,"wb") #打开一个文本文件

    file.write(picResponse.read()) #写入数据

    file.flush();

    file.close() #关闭文件

    try:
         # 根据文件哈希值获取图片
        picHshResponse=urllib.request.urlopen(picUrlHsh);

        params = cgi.parse_header(picHshResponse.headers.get('Content-Disposition', ''))[-1];

        hshFileName=params['filename'];

        # hshExt=hshFileName.split('.')[-1];

        # print(hshExt);


        # hshExt=hshFileExts[len(hshFileExts)-1];

        hshFile = open(baseFilePath+hshFileName,"wb") #打开一个文本文件

        hshFile.write(picHshResponse.read()) #写入数据

        hshFile.flush();

        hshFile.close();
    except Exception as e:
        continue




