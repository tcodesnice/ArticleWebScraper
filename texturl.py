import requests
from bs4 import BeautifulSoup

def get_article_text(url):
    try:
        # Fetch the HTML content of the URL
        response = requests.get(url)
        response.raise_for_status()

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'lxml')

        # Find the main article text (you may need to inspect the HTML structure of the website)
        # This is just a generic example; you'll need to customize it for specific websites
        article_text = ""
        if soup.find('article'):
            article = soup.find('article')
            paragraphs = article.find_all('p')
            for p in paragraphs:
                article_text += p.get_text() + '\n'

        return article_text

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

def main():
    url = input("Enter the URL of the news article: ")
    article_text = get_article_text(url)

    if article_text:
        print("Text content of the article:")
        print(article_text)
    else:
        print("Failed to retrieve the text content of the article.")

if __name__ == "__main__":
    main()
