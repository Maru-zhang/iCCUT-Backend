__author__ = 'maru'
#coding=gb2312
import urllib2
import re
from app import db
from app.models import Video,News
from BeautifulSoup import  BeautifulSoup



class ParserPage():

    video_url = 'http://v8.ccut.edu.cn/article.php?/'
    news_url = 'http://news.ccut.edu.cn/sort.php/'

    def __init__(self):
        last_v = Video.query.order_by(Video.id.desc()).first()
        last_n = News.query.order_by(News.id.desc()).first()

        if last_v == None:
            self.v_index = 0
        else:
            self.v_index = int(last_v.id)

        if last_n == None:
            self.n_index = 0
        else:
            self.n_index = int(last_n.id)



    def parserVideo(self):

        url = 'http://v8.ccut.edu.cn/article.php?/%s' % self.v_index
        print url

        try:
            html = urllib2.urlopen(url).read().decode("gb2312")

            patName = re.compile(r'<font class=bigfont><b>(.*)</b>')
            patURL = re.compile(r'href="(.*\.rmvb|.*\.mp4)"')
            patList = re.compile(r'<a href="http://v8\.ccut\.edu\.cn/sort\.php\?/\d*">(.*?)</a>')

            resName = re.findall(patName,html)[0]
            resURL = re.findall(patURL,html)[0]
            resList = re.findall(patList,html)

            video = Video(id=self.v_index,title=resName, url=resURL, leve1=resList[0], leve2=resList[1])
            db.session.add(video)
            db.session.commit()

            print("Success save to database --- %s" % resName)
        except Exception,e:
            print("Error:%s" % e)
            db.session.rollback()
            self.v_index += 1

            return


    def parserNews(self):

        try:
            html = urllib2.urlopen(self.news_url + str(self.n_index)).read().decode("gb2312")
            soup = BeautifulSoup(html, fromEncoding="gb2312")
            for content in soup.findAll(colspan='2'):
                title = content.find(target='_blank').string
                newURL = content.a["href"]
                time = content.find(color='#666666').string
                new = News(id=self.n_index,title=title,url=newURL,datetime=time)
                db.session.add(new)
                db.session.commit()
                self.n_index += 1
                print('Success save to database. ---- %s' % title)
        except Exception,e:
            print("Error:"+e)
            self.n_index += 1
            db.session.rollback()
            return


if __name__ == "__main__":

    parser = ParserPage()

    count = 1

    while count < 21457:
        parser.parserVideo()
        count+=1
        # try:
        #     parser.parserVideo()
        # except TypeError,e:
        #     print("TypeError-----%s",e)
        #     continue
        # except Exception,e:
        #     print("resultError-----%s",e)
        #     continue
        # finally:
        #     count+=1




    # while index < 50:
    #     parser.parserNews(url='http://news.ccut.edu.cn/sort.php/%s' % index)
    #     index += 1




