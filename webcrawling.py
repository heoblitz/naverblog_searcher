from selenium.webdriver.chrome.options import Options 
from selenium import webdriver
from bs4 import BeautifulSoup
import sys
import re

link_start = "<a href=\""
link_end = "\" target=\"_blank\">블로그 링크</a>"

visitor_start = "<a href=\"http://blog.naver.com/NVisitorgp4Ajax.nhn?blogId="
visitor_end = "&amp;logNo=221492203765\" target=\"_blank\">방문자 수</a>"

#headless chrome 사용하는 옵션
chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--headless')

#link를 리스트로 받고 크롤링 후, stdout에 출력해주는 함수
def gets_link(compiled_link):
	
	try:
		driver = webdriver.Chrome(chrome_options=chrome_options)
		driver.get(compiled_link)
	except:
		driver.quit()
		return

	html_data = driver.page_source
	soup = BeautifulSoup(html_data, 'html.parser')
	
	driver.close()

	like_data = soup.find_all('em', class_='u_cnt _count')
	like = re.findall('[0-9]+', str(like_data))

	if(like!=[]): 
		like_value = int(like[0])	
	else:
		like_value = 0

	comment_data = soup.find_all('div', class_= 'area_comment pcol2')
	comment = re.findall('[ ][0-9]+', str(comment_data))

	'''
	title_data = soup.find_all('span', class_= 'se-fs- se-ff-')
	try:
		title_data = title_data[0]
	except:
		title_data = "제목을 읽지 못했습니다."
	'''
	
	if(comment!=[]):	
		comment_value = int(comment[0][1:])
	else:
		comment_value = 0

	if(like_value+comment_value):
		blog_id = re.findall('Id=[a-z0-9_]+', compiled_link)
		visitor_link = "&nbsp;"*2 + visitor_start + blog_id[0][3:] + visitor_end + "</h4>" + "<br>"
		compiled_link = "&nbsp;"*2 + link_start + compiled_link + link_end  
		print("<h4>공감 수: %d  댓글 수: %d"%(like_value, comment_value))
		print(compiled_link)
		print(visitor_link)
		print("")
		sys.stdout.flush()

	driver.quit()

	return 0

#크롤링을 위해 ajax.nhn 호출 링크로 변환
def compile_link(link):
	compiled_link = [] 
	for i in range(0, len(link)):
		blog_id_data = re.findall('[/][0-9a-z-_]+[?]', link[i])
		blog_id = blog_id_data[0].replace('/', '').replace('?', '')
		
		log_no_data = re.findall('[logNo=][0-9]{10,}', link[i])
		log_no = log_no_data[0][1:]
		
		data = "http://blog.naver.com/PostView.nhn?blogId=" + blog_id + "&logNo=" + log_no
		compiled_link.append(data)

	return compiled_link

	 




