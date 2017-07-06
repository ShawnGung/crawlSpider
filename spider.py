import re
import requests
        

class QSBK :
    def __init__(self):
         self.url ='http://www.qiushibaike.com'
         self.content = []
        # print("content:"+str(self.content))
     #获取网页源码  
    def getSource(self,url):  
        user_agent = 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'  
        headers = {'User_agent': user_agent}  
        r=requests.get(url,headers=headers)  
        result=r.text  
        return result
    
    def getDetail(self,url):
        number = 1
        pattern = re.compile('<div.*?author.*?">.*?<h2>(.*?)</h2>.*?'+
                     '<div class="articleGender.*?">(.*?)</div>.*?'+
                     '<div class="content.*?<span>(.*?)</span>.*?'+
                     '<div class="stats.*?class="number">(.*?)</i>.*?'+
                     'class="number">(.*?)</i>'
                     ,re.S)
        items = re.findall(pattern,self.getSource(url))
        for item in items:
            self.content.append(u'')
            print (u'')
            self.content.append(str(number)+u'楼'+u'\n楼主：'+item[0]+u''+item[1]+u'岁'+u'\n发言:'
                   +item[2]+u'\n好笑：'
                   +item[3]+u'\n评论：'+item[4]+'\n'+'\n')
            print (number,u'楼',u'\n楼主：',item[0],u'',item[1],u'岁',u'\n发言:'
                   ,item[2],u'\n好笑：'
                   ,item[3],u'\n评论：',item[4])  
            number+=1
        return items
    
    
    def getAllPage(self,start,end):
        for page in range(start,end+1):
            self.content = []
            self.content.append(u'正在获取第'+str(page)+u'页的数据...'+'\n')
            print (u'正在获取第', str(page), u'页的数据...')
            url = self.url+'/8hr/page/'+str(page)
            data = self.getDetail(url)
            self.save(str(data),str(page))
        print (u'',u'\n加载结束！')
        self.content.append(u''+u'\n加载结束！\n')

            
    def save(self,data,name):
        fileName = 'page'+name+'.'+'txt'
        f = open(fileName,'w',encoding='utf-8')
        f.write("".join(self.content))
        print (u'',u'成功保存数据',fileName)
        self.content.append(u''+u'成功保存数据'+fileName)
        f.close()

            
    

qsbk = QSBK()
start = input("please input the start page: ")
end = input("please input the end page: ")
qsbk.getAllPage(int(start),int(end))
