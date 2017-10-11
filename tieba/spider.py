import requests
from  bs4 import  BeautifulSoup
import time

#首先我们写好抓取网页的函数
def get_html(url):
    try:
        r = requests.get(url, timeout = 30)
        r.raise_for_status() #它就可以有效的判断网络连接的状态
        #手动设置编码格式
        r.encoding = 'utf-8'
        return r.text
    except:
        return  'ERROR:打开网页出错'

#接下来开始分析网页然后获取数据
def get_content(url):

    #初始化一个列表保存所有的帖子信息
    comments = []
    html = get_html(url) #拿到网页的数据
    soup = BeautifulSoup(html, 'lxml') #做一锅汤
    liTags = soup.find_all('li', attrs = {'class':'j_thread_list'})#找到这个帖子
    for li in liTags:
        comment = {}
        #进行数据的组装，核心点是找到title，link, name, time, replyNum等元素在哪
        try:
            comment['title'] = li.find('a', attrs = {'class':'j_th_tit'}).text.strip()
            comment['link'] = "http://tieba.baidu.com/"+li.find('a', attrs = {'class':'j_th_tit'})['href']
            comment['name'] = li.find('span', attrs={'class': 'tb_icon_author'}).text.strip()
            comment['time'] = li.find('span', attrs={'class': 'pull-right is_show_create_time'}).text.strip()
            comment['replyNum'] = li.find('span', attrs={'class': 'threadlist_rep_num center_text'}).text.strip()
            comments.append(comment)
        except:
            print('出了点小问题，请检查一下')

    return  comments #返回爬取的数据dict

#接下来就是保存文件到本地
def savefile(dict):

    '''
    将爬取到的文件写入到本地
    保存到当前目录的 tieba.txt文件中。

    '''
    #设置写入的编码，不然遇到了gbk可能会出问题
    with open('tieba.txt', 'a+', encoding = 'utf-8') as f:
        for comment in dict:
            f.write('标题: {} \t 链接:{} \t 发帖人:{} \t 发帖时间:{} \t 回复数量: {} \n'.format(comment['title'],
            comment['link'], comment['name'], comment['time'], comment['replyNum'])) #format，字符串的格式化操作，使用{}占位符
    print('当前页面爬取完成')

#主函数
def main(base_url, deep):
    url_list = []
    for i in range(0, deep):
        url_list.append(base_url + '$pn' + str(50 * i)) #组装其他页码的内容
    print('所有的页面内容都组装好了')

    #循环写入数据
    for url in url_list:
        content = get_content(url) #在循环中每次保存一次
        savefile(content) #保存文件到本地
    print('所有的信息都保存完毕')

base_url = 'http://tieba.baidu.com/f?ie=utf-8&kw=%E6%B1%9F%E8%A5%BF%E5%86%9C%E4%B8%9A%E5%A4%A7%E5%AD%A6'
deep = 3
#设置要爬取的页码

if __name__ == '__main__':
    main(base_url,deep)

