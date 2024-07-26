# 프론트엔드: 사용자에게 보여지는 화면 개발
#  - 웹 디자이너: 목업, 와이어프레임, 웹디자인
#  - 웹 퍼블리셔: HTML, CSS, JS 화면단 개발

# www → 사용자 화면단은 HTML, CSS, JS 웹 표준!
#  → 프론트엔드 프레임워크: React.js, Vue.js
#  →                      Next.js, Nuxt.js
#  → Python의 Streamlit

import os
import streamlit as st
import requests

st.title("Speech Recognition")
st.write("음성 파일을 업로드해주세요.")
st.write("(mp3, aac, ac3, ogg, flac, wav)")

# 음성파일 업로드
file = st.file_uploader("Choose a Speech file", accept_multiple_files=False)

if file is not None:
    # 사용자가 업로드한 파일을 저장하는 디렉토리 생성!
    dir = "voice_data"
    if not os.path.exists(dir):
        os.mkdir(dir)

    # 파일 저장
    with open(os.path.join(dir, file.name), "wb") as f:
        f.write(file.getbuffer())

        # 업로드한 음성파일 확인!
        st.write("업로드한 파일을 확인하세요")

        # 음성파일 확인
        st.audio(os.path.join(dir, file.name), format="audio/wav", autoplay=False)

        # stt
        # * API를 사용하기 위한 필수 정보
        # 1. URL(IP+PORT) → http://127.0.0.1:8000/stt/clova
        # 2. HTTP Method → POST
        # 3. DATA → Data or File
        respose = requests.post("http://127.0.0.1:8000/stt/clova", files={"file":file})

        if respose.status_code == 200:
            print("STT RUN")
            st.subheader("STT 결과입니다.")
            stt = respose.text
            print(stt)
            print(type(stt))
            st.write(stt)
            st.download_button(label="STT 파일 다운로드", data=stt, file_name="stt.txt")
        else:
            print("현재 STT 서비스를 사용할 수 없습니다.")