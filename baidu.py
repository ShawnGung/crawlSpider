#百度贴吧爬虫
import requests
from bs4 import BeautifulSoup

#url:
#http://tieba.baidu.com/f?kw=%E7%94%9F%E6%B4
#%BB%E5%A4%A7%E7%88%86%E7%82%B8&ie=utf-8&pn=0

class BDTB:
    def __init__(self):
        self.url = r'http://tieba.baidu.com/f?kw=%E7%' +\
        r'94%9F%E6%B4%BB%E5%A4%A7%E7%88%86%E7%82%B8&ie=utf-8'
       
    def get_html(self,url):
        r = requests.get(url)
        return r.text

        
    def getDetail(self,url):
        #利用beautifulSoup来完成匹配
        text = self.get_html(url)
        #bs
        soup = BeautifulSoup(text,'html.parser')
        liTags = soup.find_all('li',class_=" j_thread_list clearfix")

        #这里返回的是list列表，保存着每个li以及li下所有子标签
        #通过循环找到信息

        #初始化一个字典来存储信息
        comments=[]
        for li in liTags:
            comment={}
            #这里返回的都是tag子节点对象,有对应的方法
            comment['title'] = li.find('a',class_="j_th_tit").text.strip()
            comment['comment'] = li.find('span',attrs={"title":"回复"}).text.strip()
            #这里的span还有一个子标签，不用string看下情况
            comment['author'] =li.find('span',attrs={"class":"frs-author-name-wrap"}).text.strip()+"\n"
            comments.append(comment)
        print(comments)
        return comments


    def save(self,data,page):
        fileName = 'page'+str(page)+'.txt'
        f  = open(fileName,'w',encoding='utf-8')
        for comment in data:
            f.write("标题："+comment['title']+"\t评论数量:"+comment['comment']+"\t作者:"+comment['author'])
        print("finished")

    def start(self,number):
        #构造url
        for page in range(0,number):
            url = self.url+'&&'+str(page*50)
            data = self.getDetail(url)
            self.save(data,page)

b = BDTB()
b.start(3)
