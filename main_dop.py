import bs4
import requests
from bs4 import BeautifulSoup


def main():
    HEADERS = {
        # ВАШ HEADERS
    }

    keywords = ['дизайн', 'фото', 'web', 'python', 'QR', 'графического', 'Rust']
    filtered_news = []

    habr_main_url = 'https://habr.com/ru/all/'
    pagetext = requests.get(habr_main_url, headers=HEADERS).text
    soup = bs4.BeautifulSoup(pagetext, 'html.parser')
    all_news = soup.find_all('article')
    article_urls = ['https://habr.com' + article.find(class_="tm-article-snippet__title-link")["href"]
                    for article in all_news]
    for article_url in article_urls:
        pagetext = requests.get(article_url, headers=HEADERS).text
        soup = bs4.BeautifulSoup(pagetext, 'html.parser')
        article = soup.find('article')
        text_content = article.find(id='post-content-body')
        for keyword in keywords:
            if keyword in text_content.text:
                filtered_news.append(
                    article.find("time")["title"] + ' - ' + article.find("h1").text + ' - ' + article_url)
    print(*set(filtered_news), sep='\n')


if __name__ == '__main__':
    main()
