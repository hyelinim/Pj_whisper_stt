from fastapi import FastAPI, UploadFile
from openai import OpenAI
from dotenv import load_dotenv, find_dotenv
import os
import requests
import uvicorn

app = FastAPI()

# OPENAI_API_KEY 가져오기
_ = load_dotenv(find_dotenv())

client = OpenAI(api_key="")

@app.get("/")
async def root():
    return {"message" : "Hello"}

# 웹 브라우저(클라이언트) -> 음성파일 업로드 -> 분석 클릭 -> API -> Whisper -> 결과 -> 웹 브라우저(클라이언트)
# POST, https://127.0.0.1/stt/whisper, input(음성파일)
@app.post("/stt/whisper")
async def stt_whisper(file: UploadFile):    # 음성 파일
    # 사용자가 업로드 한 음성파일 저장
    save_dir = "save"
    
    # save 폴더 없는 경우 생성
    if not os.path.isdir("save"):
        os.mkdir("save")

    voice = await file.read()
    with open(os.path.join(save_dir, file.filename), "wb") as fp:
        fp.write(voice)
    print(f"음성파일 {file.filename}을 저장하였습니다.")

    # 음성 파일 불러오기
    file = open(f"save/{file.filename}", "rb")

    # STT 실행
    transcript = client.audio.transcriptions.create(
        model="whisper-1",
        file=file
    )
    print(f"STT 결과 : {transcript.text}")

    # STT 결과 전송
    return {"status_code":200,
            "STT" : transcript.text}


@app.post("/stt/clova")
async def stt_clova(file:UploadFile):
    # 사용자가 업로드 한 음성파일 저장
    save_dir = "save"
    
    # save 폴더 없는 경우 생성
    if not os.path.isdir("save"):
        os.mkdir("save")

    # 파일 이름이 중복일 경우 -> 파일 이름을 유니크하게 만드는 작업이 필요함 -> UUID << 직접 공부하기 많이 사용됨!!!
    voice = await file.read()
    with open(os.path.join(save_dir, file.filename), "wb") as fp:
        fp.write(voice)
    print(f"음성파일 {file.filename}을 저장하였습니다.")

    # 음성 파일 불러오기
    file = open(f"save/{file.filename}", "rb")

    # NAVER CLOVA API KEY 설정
    client_id = ""
    client_secret = ""

    # TEXT 변환 언어 설정
    lang = "Kor" # 언어 코드 ( Kor, Jpn, Eng, Chn )

    # API URL 설정
    url = "https://naveropenapi.apigw.ntruss.com/recog/v1/stt?lang=" + lang
    
    # API에 전달한 HTTP message Header 설정
    headers = {
        "X-NCP-APIGW-API-KEY-ID": client_id,
        "X-NCP-APIGW-API-KEY": client_secret,
        "Content-Type": "application/octet-stream"
    }

    # NAVER CLOVA STT API 요청 
    response = requests.post(url,  data=file, headers=headers)
    rescode = response.status_code
    if(rescode == 200):
        print (response.text)
    else:
        print("Error : " + response.text)

    return {"status_code" : 200,
            "STT" : response.text}

if __name__=="__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)