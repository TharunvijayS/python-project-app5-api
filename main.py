import requests
from send_email import send_email

api_key="74e165b25acb49b3abc6f15769de2bc4"
url="https://newsapi.org/v2/everything?q=tesla&" \
     "from=2024-01-05&sortBy=publishedAt&" \
     "apiKey=74e165b25acb49b3abc6f15769de2bc4&"\
    "language=en"

# make request
request=requests.get(url)

# get the dictionary with data
content=request.json()

# Access the particular title and the description
body=""
for article in content["articles"][:20]:
     if article["author"] is not None:
       body=("Subject: Today's News" + "\n"
             +body + article["title"] + "\n"
             + article["description"]
             + "\n" + article["url"] + 2*"\n")

body=body.encode("utf-8")
send_email(message=body)


