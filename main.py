import requests
import urllib3

from send_mail import send_email

urllib3.disable_warnings()
api_key = '008c016a654a470090cae7c1532abc80'
url = 'https://newsapi.org/v2/everything'
params = {
    'q': 'tesla',
    'from': '2024-07-07',
    'sortBy': 'publishedAt',
    'language': 'en',
    'pageSize': 20,
    'apiKey': '008c016a654a470090cae7c1532abc80',
}
response = requests.get(url=url, params=params, verify=False).json()
body = 'Subject: Today\'s News\n\n'
for article in response['articles']:
    if article['title'] != '[Removed]' or article['title'] is not None:
        body += f'{article['title']}\n{article['description']}\n{article['url']}\n\n'
send_email(msg=body.encode('utf-8'))
