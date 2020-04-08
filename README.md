# naverblog_searcher  
[![license](https://img.shields.io/github/license/DAVFoundation/captain-n3m0.svg?style=flat-square)](https://github.com/wone2287/naverblog_searcher/blob/master/LICENSE)
   
Search <a href="https://section.blog.naver.com/BlogHome.nhn" target="_blank">naver blog</a> posts using web service crawler.

![Alt Text](image.gif)

* backend: PHP, Python3(PyPy3)
  * pypy3 crawler based on selenium  
  
* frontend: bootstrapk

## INSTALL 
* Built any web server support PHP (ex nginx-php, apache-php)  

* Install pypy3  
https://pypy.org/download.html
* Make sure you have installed these libs already.  
```bash
pypy3 -m pip install selenium
pypy3 -m pip install BeautifulSoup4
```
* Download the headless chrome compatible on your server.   
https://chromedriver.chromium.org/
