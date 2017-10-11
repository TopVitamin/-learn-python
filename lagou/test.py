# -*- coding:utf-8 -*-
import  requests
from bs4 import BeautifulSoup
import json
def main():
    headerResult = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
        'Host':'www.lagou.com',
        'Referer':'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',
		'X-Anit-Forge-Code':'0',
		'X-Anit-Forge-Token':None,
		'X-Requested-With':'XMLHttpRequest'
    }

    formData = {
		'first':'true',
		'pn':'1',
		'kd':'python'
	}

    result =  requests.post("https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false&isSchoolJob=0", headers = headerResult, data = formData )
    #print(str(result.content, 'utf-8'))
    jsonResult = result.json()
    positions = jsonResult['content']['positionResult']['result']
    line = json_dumps(positions, ensure_ascii = False)
    with open('lagou.json', 'w') as fp:
        fp.write(line.encode('utf-8'))

if __name__ == "__main__":
    main()
