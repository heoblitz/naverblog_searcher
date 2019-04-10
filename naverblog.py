#!/usr/local/bin/pypy3
# coding: utf-8
import urllib.request
import sys
import os
import re

# 지정한 날짜에 맞는 블로그만 리스트로 리턴
def date_search(start_date, end_date, link_data, post_data):
	link_match = []
	for i in range(0, len(link_data)):
		if(int(post_data[i])>=start_date and int(post_data[i])<=end_date):
			if([]!=re.findall('blog.naver.com',link_data[i])): # daum 블로그 링크 제거
				link_match.append(link_data[i])
	return link_match

# 네이버 api 사용, json 파일에서 링크, 날짜 데이터만 리스트로 가져옴
def blog_searcher(keyword, select):
	client_id = "클라이언트 id" 
	client_secret = "클라이언트 키 값" # naver 개발자 홈페이지에서 어플리케이션 등록 후 입력할것!
	
	encText = urllib.parse.quote(keyword)
	url = "https://openapi.naver.com/v1/search/blog?query=" + encText # json 결과
	url = url + "&display=100&start=1&sort=" + select #sim date 

	request = urllib.request.Request(url)
	request.add_header("X-Naver-Client-Id",client_id)
	request.add_header("X-Naver-Client-Secret",client_secret)
	response = urllib.request.urlopen(request)
	rescode = response.getcode()

	if(rescode==200):
		response_body = response.read()
		search_data = response_body.decode('utf-8')
		link_data = re.findall('\"link\":[ ]\".+', search_data)
		post_data = re.findall('\"postdate\":[ ]\".+', search_data)
		
		for i in range(0, len(link_data)):
			link_data[i] = link_data[i][8:].replace(';', '&').replace('\"', '').replace(',', '')
			post_data[i] = post_data[i][13:21]
		return (link_data, post_data)
	else:
		print("Error Code:" + rescode)


		




