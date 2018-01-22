import os
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("download.default_directory=C:/riss_crawl")
driver = webdriver.Chrome('./chromedriver.exe', chrome_options=options)
driver.implicitly_wait(3)

keyword = '인성교육'

def load_degree(driver, page):

    url = 'http://www.riss.kr/search/Search.do?detailSearch=false&viewYn=OP&queryText=&iGroupView=5&icate=all&colName=bib_t&pageScale=1000&strSort=RANK&order=%2FDESC&query='
    url2 = '&iStartCount='

    driver.get(url+keyword+url2+str(page * 1000))

    window_before = driver.window_handles[0]

    driver.find_element_by_xpath('//*[@id="allchk2"]').click()
    driver.find_element_by_xpath('/html/body/div[1]/div[4]/div[2]/div[3]/form/div[3]/div[3]/div/div[1]/p[1]/span/a[1]/img').click()
   
    window_after = driver.window_handles[1]
    driver.switch_to_window(window_after)
    driver.implicitly_wait(120)
    driver.find_element_by_xpath('//*[@id="radio-8"]').click()
    driver.find_element_by_xpath('//*[@id="radio-3"]').click()
    driver.find_element_by_xpath('/html/body/form/div/div[2]/div[5]/a[1]/img').click()

    driver.close()
    driver.switch_to_window(window_before)
load_degree(driver, 0)

cnt = 0

for i in range(8):
    load_degree(driver, i)
    cnt += 1

download = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Downloads')
desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')

filename = [f for f in os.listdir(download)]
filename.sort(key=lambda x: os.stat(os.path.join(download, x)).st_mtime)
filename = list(reversed(filename))[:cnt]

os.mkdir('degree')
for i in filename:
    os.rename(download + '/' + i, './degree/' + i)