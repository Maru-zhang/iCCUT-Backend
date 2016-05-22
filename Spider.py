__author__ = 'maru'
#coding=gb2312
import urllib2
import re
from app import db
from app.models import Video,News
from BeautifulSoup import  BeautifulSoup



class ParserPage():

    def __init__(self):
        last_v = Video.query.last()
        last_n = News.query.last()

        if last_v == None:
            self.v_index = 0
        else:
            self.v_index = last_v.id
        if last_n == None:
            self.n_index = 0
        else:
            self.n_index = last_n.id
        self.video_url = 'http://v8.ccut.edu.cn/article.php?/'
        self.news_url = 'http://news.ccut.edu.cn/sort.php/'

    def parservideo(self,index):


        print self.video_url + str(index)
        try:
            html = urllib2.urlopen(self.video_url + str(index)).read().decode("gb2312")
        except UnicodeDecodeError,e:
            print("UnicodeDecodeError:"+e)
            return
        except urllib2.URLError,e:
            print("URLError"+e)
            return

        patName = re.compile(r'<font class=bigfont><b>(.*)</b>')
        patURL = re.compile(r'href="(.*\.rmvb|.*\.mp4)"')
        patList = re.compile(r'<a href="http://v8\.ccut\.edu\.cn/sort\.php\?/\d*">(.*?)</a>')

        try:
            resName = re.findall(patName,html)[0]
            resURL = re.findall(patURL,html)[0]
            resList = re.findall(patList,html)

        except IndexError,e:
            return

        video = Video(id=index,title=resName, url=resURL, leve1=resList[0], leve2=resList[1])
        db.session.add(video)
        db.session.commit()
        print("Success save to database --- %s" % resName)


    def parserNews(self,index):

        try:
            html = urllib2.urlopen(self.news_url + str(index)).read().decode("gb2312")
        except UnicodeDecodeError,e:
            print("UnicodeDecodeError:"+e)
            return
        except urllib2.URLError,e:
            print("URLError"+e)
            return

        try:
            soup = BeautifulSoup(html, fromEncoding="gb2312")
            for content in soup.findAll(colspan='2'):
                title = content.find(target='_blank').string
                newURL = content.a["href"]
                time = content.find(color='#666666').string
                new = News(id=index,title=title,url=newURL,datetime=time)
                db.session.add(new)
                db.session.commit()
                print('Success save to database. ---- %s' % title)
        except IndentationError,e:
            print(e)
        except AttributeError,e:
            print(e)


if __name__ == "__main__":

    index = 1
    parser = ParserPage()

    while index < 2000:
        try:
            result = parser.parserVideo(index=index)
        except TypeError,e:
            print("TypeError-----%s" % index)
            continue
        except Exception,e:
            print("resultError-----%s" % index)
            continue
        finally:
            index += 1


    # while index < 50:
    #     parser.parserNews(url='http://news.ccut.edu.cn/sort.php/%s' % index)
    #     index += 1




