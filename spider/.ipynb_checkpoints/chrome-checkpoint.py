from selenium import webdriver
import scrapy
from IPython.display import Image
from scrapy import Selector
import string
from pyvirtualdisplay import Display
display = Display(visible=0, size=(1280, 100))
display.start()
#_____________________基本设定___________________________
CHROME_DRIVER_PATH = r'/usr/bin/chromedriver' 
#PROXY = "http://127.0.0.1:8080"
#PROXY = "http://35.189.179.23:8080" 
#_____________________启动参数___________________________
options = webdriver.ChromeOptions()
options.add_argument('lang=zh_CN.UTF-8')
options.add_argument('user-agent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36"')

options.add_argument("--no-sandbox")
options.add_argument("--disable-remote-fonts")
#options.add_argument("--ignoreHTTPSErrors=true")
#options.add_argument("--allow-insecure-localhost")
prefs = {"profile.managed_default_content_settings.images":2,
         "profile.managed_default_content_settings.javascript":2
        }
#options.add_argument('--proxy-server=http://127.0.0.1:8080')  
options.add_experimental_option("prefs",prefs)
#_____________________代理参数__________________________

#_____________________启动浏览器___________________________
driver = webdriver.Chrome(
    chrome_options=options, 
    executable_path=CHROME_DRIVER_PATH,
    #desired_capabilities = desired_capabilities,
                         )
for i in range(1):
    
    platform='wise'
    ms='1'
    lsAble='1'
    rset='rcmd'
    word='免费代理2'
    qid='8396144568311373391'
    rq='免费代理'
    fom = '0'
    baiduid='126A4F890DC00E899F6FB3874F7818C5:FG=1'
    tn=''
    clientWidth='400'
    t='1532509517831'
    r='9203'
    url ='https://m.baidu.com/rec?&platform='+platform+'&ms='+ms+'&lsAble='+lsAble+'&rset='+rset+'&word='+word+'&qid='+qid+'&rq='+rq+'&from='+fom+'&baiduid='+baiduid+'&tn='+tn+'&clientWidth='+clientWidth+'&t='+t+'&r='+r
    #print(url)
    #url = 'https://www.owler.com'
    driver.get(url)
    #driver.get('http://mitm.it/')
    
    #driver.find_element_by_id(“xxx”).click()
    
    #driver.get('https://www.iplocation.net')
    contant = driver.page_source
    driver.save_screenshot('sxcsdn.png')
    #pages = Selector(text=contant).xpath("//html")
    #ip = pages.xpath("//span[@style='font-weight: bold; color:green;']/text()").extract()
    #driver.delete_all_cookies()#删除当前会话的所有cookie
    #driver.delete_cookie('my_cookie')#删除一个指定的cookie
    #refresh() - 刷新当前页面
    
    driver.close()
    driver.quit()