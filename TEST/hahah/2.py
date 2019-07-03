from bs4 import BeautifulSoup
import requests
rl = requests.get("http://699pic.com/zhuanti/shijiedushuri1.html",verify=False)
soup = BeautifulSoup(rl.content,"html.parser")
all = soup.find_all(class_="lazy")
for i in all:
    try:
        jpg_url=i["data-original"]
        print(jpg_url)
        jpg_title=i["title"]
        print(jpg_title )
        r2 = requests.get("http://img95.699pic.com/photo/50121/2335.jpg_wh300.jpg")
        with open(jpg_title+".jpg","wb")as fp:
            fp.write(r2.content)
    except:
        pass