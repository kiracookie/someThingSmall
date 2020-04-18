import os,hashlib

file_path="//10.221.224.40/scan/BingPics"


def get_file_md5(file_path):
    """
    获取文件md5值
    :param file_path: 文件路径名
    :return: 文件md5值
    """
    with open(file_path, 'rb') as f:
        md5obj = hashlib.md5()
        md5obj.update(f.read())
        _hash = md5obj.hexdigest()
    return str(_hash).upper()

file_names=os.listdir(file_path)
#print(file_names)
# 文件名拼接路径
file_list = [os.path.join(file_path,file) for file in file_names]

for file_name in file_list:

    print(get_file_md5(file_name))
    
#print(file_list)

