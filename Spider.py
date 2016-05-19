__author__ = 'maru'
#coding=gb2312
import urllib2
import re
from app import db
from app.models import Video,User


class ParserPage():

    def parserPage(self,url):

        try:
            html = urllib2.urlopen(url).read().decode("gb2312")
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

        return {
            "name": resName,
            "url": resURL,
            "leve1": resList[0],
            "leve2": resList[1]
        }


if __name__ == "__main__":

    index = 0
    parser = ParserPage()

    while index < 0:
        try:
            result = parser.parserPage(url="http://v8.ccut.edu.cn/article.php?/%s" % index)
            name = result['name']
            url = result['url']
            leve1 = result['leve1']
            leve2 = result['leve2']
            video = Video(title=name, url=url, leve1=leve1, leve2=leve2)
            db.session.add(video)
            db.session.commit()
            print("Success save to database --- %s" % name)
        except TypeError,e:
            print("TypeError-----%s" % index)
            continue
        except Exception,e:
            print("resultError-----%s" % index)
            continue
        finally:
            index += 1

    u1 = User(username='maru',email='sdad',password='sasa')
    db.session.add(u1)
    db.session.commit()

    print User.query.all()

