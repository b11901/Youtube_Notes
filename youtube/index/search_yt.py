import requests
from bs4 import BeautifulSoup

def search_youtube(user_input):
    base_url = "https://www.youtube.com/results?search_query="
    url = base_url + user_input.replace(" ", "+")
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'lxml')

    i = 1
    title_list = []
    links_list = []
    thumb_list = []
    for div in soup.find_all('div', class_='yt-lockup-content'):
        title_list.append(div.a['title'])
        b_link = div.a['href']
        link = 'https://youtube.com' + b_link
        #Grabbing necessary links
        links_list.append(link)
        thumb_list.append(b_link)

        i += 1

    description_list = []
    for div in soup.find_all('div', class_="yt-lockup-description yt-ui-ellipsis yt-ui-ellipsis-2"):
        print(div.text)
        description_list.append(div.text)


    return links_list,description_list,title_list,thumb_list
