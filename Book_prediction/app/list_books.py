import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def get_list():
    browser = webdriver.Chrome("app/chromedriver.exe")
    browser.get("https://www.goodreads.com/review/list/134820979-aditirao-kalanji?utf8=%E2%9C%93&utf8=%E2%9C%93&ref=nav_mybooks&shelf=owned&title=aditirao-kalanji&per_page=infinite")
    time.sleep(1)
    
    elem = browser.find_element_by_tag_name("body")
	#elem = find_element(by=By.TAG_NAME, value="body"
    no_of_pagedowns = 10
    
    while no_of_pagedowns:
        elem.send_keys(Keys.PAGE_DOWN)
        time.sleep(0.2)
        no_of_pagedowns-=1
        
    aTags = browser.find_elements_by_css_selector('a')
    
    count=0
    books=[]
    
    for a in aTags:
        title = a.get_attribute('title')
        href = a.get_attribute('href')
		#print(title,"\t",href)
        
        if title!='' and '/book/show' in href:
            books.append(title)
            count+=1
	#print("Total: ", count)
    return books, count