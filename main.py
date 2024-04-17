import requests

api_key = "2b105c672a454e82b91956f246748806"
url ="https://newsapi.org/v2/everything?q=tesla&from=2024-03-17&sortBy\
    =publishedAt&apiKey=2b105c672a454e82b91956f246748806"

#Make request
request = requests.get(url)
# Get a dictionary with data
content = request.json()
#Access the article titles and description
for article in content["articles"][:20]:
    if article["title"] is not None:
        body ="Subject: Today's news" + "\n" + body + article["title"] + "\n" + article["description"] + "\n"
                + article["url"] + 2* "\n"

body = body.encode("utf-8")
    print(article["title"])
    print(article["description"])
