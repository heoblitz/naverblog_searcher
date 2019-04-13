#!/usr/local/bin/pypy3
# coding: utf-8

'''

명령어 전달 형식
argv list value

pypy3 main.py "keyword" "2019-01-01" "2019-01-03" "sim or date" 
	       argv[1]    argv[2]      argv[3]      argv[4]

'''

from multiprocessing import Pool
import webcrawling
import naverblog
import time
import sys
import os

# 프로그램 실행시간 측정
start_time = time.time()

# 검색 키워드
keyword = sys.argv[1]
start_date = sys.argv[2].replace("-","") 
end_date = sys.argv[3].replace("-","")
search_option = sys.argv[4]

# 네이버 api 파싱 후 블로그 링크, 날짜 데이터 리스트로 리턴
(blog_list, blog_date) = naverblog.blog_searcher(keyword, search_option) 

# 지정한 날짜에 맞는 블로그 리스트만 리턴
link_date = naverblog.date_search(int(start_date), int(end_date), blog_list, blog_date)

# 링크 데이터 크롤링 가능하게 ajax 링크로 변환
link_list = webcrawling.compile_link(link_date) 

# 멀티프로세싱으로 크롤링 함수 실행 (process=8)
pool = Pool(processes=8)
pool.map(webcrawling.gets_link, link_list) 

pool.terminate()
print("<h4>--- %s seconds ---</h4>" %(time.time() - start_time))




