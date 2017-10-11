import requests
from bs4 import BeautifulSoup
import  os
import  time


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

def save(path, info):
    mkdir(path) #设置好路径
    f = open(str(hash(info)) + '.jpg', 'ab')# 避免文件重名
    f.write(info.content)
    f.close()


headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
all_url = ['http://www.imooc.com/course/list?page={}'.format(str(i)) for i in range(1, 32)]
mkpath  = r'E:\python\-learn-python\imooc\images'
for page_url in all_url:
    start_html = requests.post(page_url, headers = headers) #在列表中循环请求分页地址
    soup = BeautifulSoup(start_html.text, 'html.parser') #获取网页解析内容
    all_img = soup.find('div', class_='moco-course-list').find_all('img')#找到全部的img地址
    for img in all_img:
        img_src = img['src'] #取出里面的src内容
        print(img_src)
        imgInfo = requests.get(img_src, headers = headers)
        save(mkpath, imgInfo)
