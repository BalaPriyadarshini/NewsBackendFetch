from config import API_KEY
from flask import Flask, render_template
import requests

app = Flask(__name__)


def fetch_technical_news():
    url = f'https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey={API_KEY}'
    response = requests.get(url)
    data = response.json()
    articles = data.get('articles', [])
    news = []
    for article in articles:
        title = article.get('title')
        content = article.get('description')
        date = article.get('publishedAt')
        news.append({'title': title, 'content': content, 'date': date})
    return news


@app.route('/')
def index():
    news = fetch_technical_news()
    return render_template('index.html', news=news)


if __name__ == '__main__':
    app.run(debug=True)
