import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()

browser.get("https://www.goodreads.com/review/list/134820979-aditirao-kalanji?utf8=%E2%9C%93&utf8=%E2%9C%93&ref=nav_mybooks&shelf=owned&title=aditirao-kalanji&per_page=infinite")
time.sleep(1)

elem = browser.find_element_by_tag_name("body")
#elem = find_element(by=By.TAG_NAME, value="body")
print("1")
#print(elem)

no_of_pagedowns = 10

while no_of_pagedowns:
    elem.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.2)
    no_of_pagedowns-=1

print("2")

aTags = browser.find_elements_by_css_selector('a')
'''
ele=aTags[0].get_attribute('title')
print(ele, "\tType: ",type(ele) )
if ele==None:
    print("None")
elif ele=='':
    print("Blank")
else:
    print("Else")
'''
count=0

for a in aTags:
    title = a.get_attribute('title')
    href = a.get_attribute('href')
    #print(title,"\t",href)
    #book=a.string
    if title!='' and '/book/show' in href:
        print(title)
        count+=1


print("Total: ", count)
    
'''
post_elems = browser.find_element_by_tag_name("a")
print(post_elems.title)
#print("*******************\n",len(post_elems))
print("3")

for post in post_elems:
    print(post.tag_name)
print("4")
'''


'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pyvirtualdisplay import Display

def correct_url(url): 
    if not url.startswith("http://") and not url.startswith("https://"):
        url = "http://" + url
    return url

def scrollDown(browser, numberOfScrollDowns):
    body = browser.find_element_by_tag_name("body")
    while numberOfScrollDowns >=0:
        body.send_keys(Keys.PAGE_DOWN)
        numberOfScrollDowns -= 1
    return browser

def crawl_url(url, run_headless=True):
    if run_headless:
        display = Display(visible=0, size=(1024, 768))
        display.start()

    url = correct_url(url)
    browser = webdriver.Firefox()
    browser.get(url)
    browser = scrollDown(browser, 10)

    all_hover_elements = browser.find_elements_by_class_name("hover-box")
    count=0
    for hover_element in all_hover_elements:
        a_element = hover_element.find_element_by_tag_name("a")
        book_title = a_element.get_attribute("title")
        book_link = a_element.get_attribute("href")
        print(book_title)
        #print(product_link)
        count+=1

    browser.quit()

if __name__=='__main__':
    url = "https://www.goodreads.com/review/list/134820979-aditirao-kalanji?utf8=%E2%9C%93&utf8=%E2%9C%93&ref=nav_mybooks&shelf=owned&title=aditirao-kalanji&per_page=infinite"
    crawl_url(url)
'''
