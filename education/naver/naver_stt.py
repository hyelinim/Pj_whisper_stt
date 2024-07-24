# Naver STT 소개
#  - 사용 가능 음성 포맷: mp3, aac, ac3, ogg, flac, wav
#  - RESTAPI -> HTTP METHOD: POST,
#               URL: https://naveropenapi.apigw.ntruss.com/recog/v1/stt
#               KEY(2): client id, client secret
#               DATA: 필수(y), 제한(최대60초), 포맷(음성 파일)
import sys
import requests
from dotenv import load_dotenv, find_dotenv
import os

_=load_dotenv(find_dotenv())  # .env 불러오기


client_id = ""
client_secret = ""
lang = "Kor" # 언어 코드 ( Kor, Jpn, Eng, Chn )
# 
url = "https://naveropenapi.apigw.ntruss.com/recog/v1/stt?lang=" + lang
data = open('data/tts_audio.mp3', 'rb')
headers = {
    "X-NCP-APIGW-API-KEY-ID": client_id,
    "X-NCP-APIGW-API-KEY": client_secret,
    "Content-Type": "application/octet-stream"
}

# API 요청
response = requests.post(url,  data=data, headers=headers)
rescode = response.status_code
if(rescode == 200):
    print (response.text)
else:
    print("Error : " + response.text)