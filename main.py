import requests

api_key="74e165b25acb49b3abc6f15769de2bc4"
url="https://newsapi.org/v2/everything?q=tesla&" \
     "from=2024-01-05&sortBy=publishedAt&" \
     "apiKey=74e165b25acb49b3abc6f15769de2bc4"

# make request
request=requests.get(url)

# get the dictionary with data
content=request.json()

# Access the particular title and the description
for article in content["articles"]:
   print(article["title"])
   print(article["description"])