# -*- coding:utf-8 -*-
import  requests
from bs4 import BeautifulSoup

def main():
    headerResult = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
        'Host':'www.lagou.com',
        'Referer':'https://www.lagou.com/'
    }

    result =  requests.get("https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=", headers = headerResult)
    print(str(result.content, 'utf-8'))


if __name__ == "__main__":
    main()