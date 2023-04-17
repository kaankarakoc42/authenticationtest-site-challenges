import requests
from fake_useragent import UserAgent
from scrapy.selector import Selector
ua = UserAgent()

ses= requests.session()
ses.headers.update({'user-agent': ua.chrome})

#simple form auth
"""
res = ses.get("https://authenticationtest.com/simpleFormAuth/")
cookie = ses.cookies.get_dict()
print(cookie)
res = ses.post("https://authenticationtest.com//login/?mode=simpleFormAuth",data={"email":"simpleForm@authenticationtest.com","password":"pa$$w0rd"},cookies=cookie)
html = Selector(res)
state = html.xpath("/html/body/div/h1").get()
print(state)
"""

#bootstrap auth
"""
res = ses.get("https://authenticationtest.com/bootstrapAuth/")
cookie = ses.cookies.get_dict()
html = Selector(res)
code = html.xpath("/html/body/div/div/div[2]/form/div[3]/label/code/text()").get()
print(code)
res = ses.post("https://authenticationtest.com//login/?mode=bootstrapAuth",data={"email":"bootstrap@authenticationtest.com","password":"pa$$w0rd","captcha":code},cookies=cookie)
html = Selector(res)
state = html.xpath("/html/body/div/h1").get()
print(state)
"""

#complex auth
"""
res = ses.get("https://authenticationtest.com/complexAuth/")
cookie = ses.cookies.get_dict()

res = ses.post("https://authenticationtest.com//login/?mode=complexAuth",
               data={"loveForm":"on","selectLogin":"yes","email":"complex@authenticationtest.com","password":"pa$$w0rd"},
               cookies=cookie)

html = Selector(res)
state = html.xpath("/html/body/div/h1").get()
print(state)
"""

#ocrChallenge captcha (*burda tek attım)
"""
from reader import image_to_string

res = ses.get("https://authenticationtest.com/ocrChallenge/")
cookie = ses.cookies.get_dict()
print(cookie)
captcha = image_to_string(ses.get("https://authenticationtest.com/ocrChallenge/captcha.php",cookies=cookie))
res = ses.post("https://authenticationtest.com//login/?mode=ocrChallenge",data={"captcha":captcha,"email":"ocr@authenticationtest.com","password":"pa$$w0rd"},cookies=cookie)
html = Selector(res)
state = html.xpath("/html/body/div/h1").get()
print(state)
"""

#delayed login
"""
cookie = ses.get("https://authenticationtest.com/delayChallenge/").cookies.get_dict()
res = ses.post("https://authenticationtest.com//login/?mode=delayChallenge",data={"email":"delay@authenticationtest.com","password":"pa$$w0rd"},cookies=cookie)
html = Selector(res)
state = html.xpath("/html/body/div/h1").get()
print(state)
"""

#multi page login
"""
cookie = ses.get("https://authenticationtest.com/multiChallenge").cookies.get_dict()
res = ses.post("https://authenticationtest.com//login/?mode=multiChallenge",data={"email":"multi@authenticationtest.com","password":"pa$$w0rd"},cookies=cookie)
html = Selector(res)
state = html.xpath("/html/body/div/h1").get()
print(state)
"""

#popup form login
"""
cookie = ses.get("https://authenticationtest.com/newWindowChallenge/").cookies.get_dict()
res = ses.post("https://authenticationtest.com/login/?mode=newWindowChallenge",data={"email":"newwindow@authenticationtest.com","password":"pa$$w0rd"},cookies=cookie)
print(res.content)
"""

#with iframe login
"""
cookie = ses.get("https://authenticationtest.com/iframeChallenge/login.html").cookies.get_dict()
res = ses.post("https://authenticationtest.com/login/?mode=iframeChallenge",data={"email":"iframe@authenticationtest.com","password":"pa$$w0rd"},cookies=cookie)
print(res.content)
"""
# login with xsrf token
"""
res = ses.get("https://authenticationtest.com/xsrfChallenge/")
cookie = res.cookies.get_dict()
html = Selector(res)
xss_code = html.xpath("/html/body/div/div/div[2]/form/div[3]/input/@value").get()
print(xss_code)
res = ses.post("https://authenticationtest.com//login/?mode=xsrfChallenge",data={"xsrfToken":xss_code,"email":" xsrf@authenticationtest.com","password":"pa$$w0rd"},cookies=cookie)
html = Selector(res)
state = html.xpath("/html/body/div/h1").get()
print(state)
"""

#dynamic login field challenge (*buna da tek attım)
"""
res = ses.get("https://authenticationtest.com/dynamicChallenge/")
cookie = res.cookies.get_dict()
html = Selector(res)
email_field_name = html.xpath("/html/body/div/div/div[2]/form/div[1]/input").attrib["name"] 
password_field_name = html.xpath("/html/body/div/div/div[2]/form/div[2]/input").attrib["name"]
res = ses.post("https://authenticationtest.com//login/?mode=dynamicChallenge",data={email_field_name:" dynamic@authenticationtest.com",password_field_name:"pa$$w0rd"},cookies=cookie)
html = Selector(res)
state = html.xpath("/html/body/div/h1").get()
print(state)
"""

# TOTP MFA Authentication Challenge (tek atıldı)
"""
from reader import read_qr_code
res = ses.get("https://authenticationtest.com/totpChallenge/")
cookie = res.cookies.get_dict()
html = Selector(res)
qr_code = html.xpath("/html/body/div/div/div[1]/div/img").attrib["src"]
secret = read_qr_code(ses.get(qr_code)).split("?")[1].split("=")[1]
code = ses.get("https://authenticationtest.com/totp/?secret="+secret).json()["code"]
res = ses.post("https://authenticationtest.com/login/?mode=totpChallenge",data={"totpmfa":code,"email":"totp@authenticationtest.com","password":"pa$$w0rd"},cookies=cookie)
html = Selector(res)
state = html.xpath("/html/body/div/h1").get()
print(state)
"""
#hijacking
"""
res = ses.get("https://authenticationtest.com/",cookies={'PHPSESSID': 'odc12fpnod270ac477utmlgpdg'})
html = Selector(res)
state = html.xpath("/html/body/nav/span").get()
print(state)
"""
