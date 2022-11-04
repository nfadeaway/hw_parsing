import bs4
import requests
from bs4 import BeautifulSoup


def main():
    HEADERS = {
        # ВАШ HEADERS
    }

    keywords = ['дизайн', 'фото', 'web', 'python', 'QR', 'графического', 'Rust']
    filtered_news = []

    url = 'https://habr.com/ru/all/'
    pagetext = requests.get(url, headers=HEADERS).text
    soup = bs4.BeautifulSoup(pagetext, 'html.parser')
    all_news = soup.find_all('article')
    for article in all_news:
        for keyword in keywords:
            if keyword in article.find(class_='article-formatted-body').text:
                filtered_news.append(article.find("time")["title"] + ' - ' + article.find("h2").text +
                                     ' - https://habr.com' + article.find(class_="tm-article-snippet__title-link")["href"])
    print(*set(filtered_news), sep='\n')


if __name__ == '__main__':
    main()
