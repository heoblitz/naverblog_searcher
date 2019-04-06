#!/usr/local/bin/pypy3
# coding: utf-8
from multiprocessing import Pool
import webcrawling
import naverblog
import time
import sys
import os

'''
명령어 전달 형식
arguments passing

pypy3 main.py "keyword" "2019-01-01" "2019-01-03" "sim or date" 
	      argv[1]     argv[2]      argv[3]      argv[4]

'''

start_time = time.time() 
data = sys.argv[1] # 검색 할 keyword
(blog_list, blog_date) = naverblog.blog_searcher(sys.argv[1], sys.argv[4]) # 네이버 api 파싱 후 블로그 링크, 날짜 데이터 리스트로 리턴

start_date = sys.argv[2].replace("-","") # 2019-01-01 -> 20190101
end_date = sys.argv[3].replace("-","") # 2019-01-03 -> 20190103
	
link_date = naverblog.date_search(int(start_date), int(end_date), blog_list, blog_date) # 지정한 날짜에 맞는 블로그 리스트만 리턴

link_list = webcrawling.compile_link(link_date) # webcrawling using selenium
pool = Pool(processes=8) # multiprocessing core 8 	
pool.map(webcrawling.gets_link, link_list) # use multiprocessing Pool

pool.terminate()
print("<h4>--- %s seconds ---</h4>" %(time.time() - start_time))




