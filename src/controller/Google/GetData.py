import requests
from bs4 import BeautifulSoup
import codecs
import html
from src.controller.Main import Methods as methods


# from

def google_search(search_term):

    # response = urllib2.urlopen('http://74.125.228.100', timeout=20)

    res = get_google_page(search_term)
    if res is not None:
        text = html.unescape(res.text)
        soup = BeautifulSoup(text, "html.parser")
        prettytext = soup.prettify()

        frawpage = codecs.open('../../rawpage.txt', 'w', 'utf-8')
        frawpage.write(prettytext)
        frawpage.close()
        movie_name = soup.find('div', {'class': 'FSP1Dd'})
        return movie_name.getText()


def get_google_page(search_term):
    url = 'https://www.google.com/search?q=' + search_term + ' movie'
    try:
        res = requests.get(url)
        res.raise_for_status()
        return res
    except Exception as exc:
        print('error while loading page occured: ' + str(exc))
        user_decision = input('do you want to try again?[y/n]')
        if methods.y_n_switch_case(user_decision):
            get_google_page(search_term)
        else:
            print('Really? ok then! try again when you are ready :D ')
