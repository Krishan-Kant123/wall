import requests
from bs4 import BeautifulSoup

def tags(pgno:int=1 , tag:str="black"):
    url = f'https://wallpaper.mob.org/gallery/tag={tag}/{pgno}'
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Mobile Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.8",
        "Referer": "https://wallpaper.mob.org/",
        "Upgrade-Insecure-Requests": "1"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:

        soup = BeautifulSoup(response.content, "html.parser")

        image_tags = soup.select(".page-gallery-list__item img")
        list=[]
        for img in image_tags:
                    img_src = (img.get("src") or img.get("data-src"))
                    if img_src:
                        # print(img_src)
                        list.append(img_src+"?h=600&r=0.5")
                
        return list
