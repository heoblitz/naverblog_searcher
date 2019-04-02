# coding: utf-8
from multiprocessing import Pool
import webcrawling
import naverblog
import time
import sys
import os

os.system('pkill chromium')
start_time = time.time()
data = sys.argv[1]
(blog_list, blog_date) = naverblog.blog_searcher(sys.argv[1], sys.argv[4])

start_date = sys.argv[2].replace("-","")
end_date = sys.argv[3].replace("-","")
	
link_date = naverblog.date_search(int(start_date), int(end_date), blog_list, blog_date)

link_list = webcrawling.compile_link(link_date)
pool = Pool(processes=8)	
pool.map(webcrawling.gets_link, link_list)  

pool.terminate()
print("<h4>--- %s seconds ---</h4>" %(time.time() - start_time))

os.system('pkill chromium')



