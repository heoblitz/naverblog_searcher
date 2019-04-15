#!/usr/local/bin/pypy3
# coding: utf-8
from selenium.webdriver.chrome.options import Options 
from selenium import webdriver
from bs4 import BeautifulSoup
import sys
import re

# html <a> 태그로 묶기 위한 문자열 
link_start = "<a href=\""
link_end = "\" target=\"_blank\">블로그 링크</a>"
visitor_start = "<a href=\"http://blog.naver.com/NVisitorgp4Ajax.nhn?blogId="
visitor_end = "&amp;logNo=221492203765\" target=\"_blank\">방문자 수</a>"

# headless chrome 사용하는 옵션
chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--headless')

# link를 리스트로 받고 크롤링 후, stdout에 출력해주는 함수
def gets_link(compiled_link):
        try:
                driver = webdriver.Chrome(chrome_options=chrome_options)
                driver.set_page_load_timeout(10) # 웹페이지 로딩에 10초 이상 걸리면 중단
                driver.get(compiled_link)
		
		# 특정 자바스크립트 로딩이 안되는 문제로, 스크롤을 가장 아래로 내리고 해당 태크에 클릭 값 보내줌.
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") # 문서 제일 아래로 스크롤 다운
                driver.find_element_by_xpath("//*[starts-with(@id, 'area_sympathy')]/div/a").send_keys(Keys.SPACE) # .click() 동작 error로 space key 보냄
		
        except:
                driver.close()
                driver.quit()
                return

	html_data = driver.page_source
	soup = BeautifulSoup(html_data, 'html.parser')

	driver.close()
	driver.quit()

	# html data 에서 공감 수 파싱
	like_data = soup.find_all('em', class_='u_cnt _count')
	like = re.findall('[0-9]+', str(like_data))

	if(like!=[]): 
		like_value = int(like[0])	
	else:
		like_value = 0

	# html data 에서 댓글 수 파싱
	comment_data = soup.find_all('div', class_= 'area_comment pcol2')
	comment = re.findall('[ ][0-9]+', str(comment_data))
	
	if(comment!=[]):	
		comment_value = int(comment[0][1:])
	else:
		comment_value = 0

	'''
	# 제목 파싱하는 구문 주석 처리
	title_data = soup.find_all('span', class_= 'se-fs- se-ff-')
	try:
		title_data = title_data[0]
	except:
		title_data = "제목을 읽지 못했습니다."
	'''

	# 최소 조건으로 공감과 댓글 수 의 합이 1 이상만 출력함
	if(like_value+comment_value):
		blog_id = re.findall('Id=[a-z0-9_]+', compiled_link) # 블로거 id 값 regex로 파싱
		visitor_link = "&nbsp;"*2 + visitor_start + blog_id[0][3:] + visitor_end + "</h4>" + "<br>"
		compiled_link = "&nbsp;"*2 + link_start + compiled_link + link_end  
		print("<h4>공감 수: %d  댓글 수: %d"%(like_value, comment_value))
		print(compiled_link)
		print(visitor_link)
		print("")
		sys.stdout.flush() # php가 interactive 하게 stdout 값을 받기 위해 스트림을 비워줌

	return 0

# 크롤링을 위해 ajax.nhn 호출 링크로 변환
def compile_link(link):
	compiled_link = [] 
	for i in range(0, len(link)):
		blog_id_data = re.findall('[/][0-9a-z-_]+[?]', link[i]) # blog_id 값 regex로 파싱
		blog_id = blog_id_data[0].replace('/', '').replace('?', '') # '/', '?' 특수문자 제거
		
		log_no_data = re.findall('[logNo=][0-9]{10,}', link[i]) # 게시글 번호 값 regex로 파싱
		log_no = log_no_data[0][1:] # '=' 값 제거
		
		data = "http://blog.naver.com/PostView.nhn?blogId=" + blog_id + "&logNo=" + log_no
		compiled_link.append(data)

	return compiled_link

	 




