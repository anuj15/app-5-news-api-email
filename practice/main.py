import requests
import urllib3
import streamlit as st

urllib3.disable_warnings()
url = 'https://api.nasa.gov/planetary/apod'
api_key = 'lUc3yMH5p2hSnIBOtMVScRslTyfAGa9v6XTUkRGM'
params = {
    'api_key': api_key,
}
response = requests.get(url=url, params=params, verify=False).json()
pic_url = response['url']
pic = requests.get(url=pic_url, verify=False).content
with open(file='pic.jpg', mode='wb')as f:
    f.write(pic)
st.title(body=response['title'])
st.image(image='pic.jpg')
st.write(response['explanation'])
