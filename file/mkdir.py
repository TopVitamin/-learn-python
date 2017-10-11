import  os

def mkdir(path):
    #去除首尾空格
    path = path.strip()
    #去除右边的 \ 符号
    path = path.rstrip('\\')

    #判断路径是否存在
    isExists = os.path.exists(path)

    #判断结果
    if not isExists:
        #如果不存在这个目录，则创建这个
        os.mkdir(path)
        os.chdir(path)
        print(path + '路径创建成功')
        return True
    else:
        #如果目录存在，就不创建，提示目录已经存在
        print(path + '路径已经存在，不需要创建了')
        os.chdir(path)
        return False
mkpath  = r'E:\python\-learn-python\file\images'
mkdir(mkpath)
open('1.txt','w')
