import requests, random
from bs4 import BeautifulSoup
for i in range(1, 51):
    links = []
    url = 'https://books.toscrape.com/catalogue/page-{}.html'.format(i)
    pagina = requests.get(url, verify=False)


    #raspagem dos links das imagens
    soup = BeautifulSoup(pagina.text, 'html.parser') 
    for item in soup.find_all('img'):
        links.append('https://books.toscrape.com/' + item['src']) 
    links = list(set(links))

    #download das imagens
    for item in links:
            try:
                img_data = requests.get(item, verify=False).content
                with open('{}.jpg'.format(random.randint(1,100000)), 'wb') as handler:
                    handler.write(img_data)
            except:
                pass