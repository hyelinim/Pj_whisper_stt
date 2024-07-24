from openai import OpenAI
from dotenv import load_dotenv, find_dotenv

# .env 파일 불러오기(.env -> 환경변수 : OPENAI_API_KEY)
_ = load_dotenv(find_dotenv())

# Whisper STT 소개
#   - 파일 업로드는 25MB 제한 -> 25MB 이상 파일이오면 청크로 나누는 작업 필요!
#   - 입력 파일 형식 mpo3, mp4, mpeg, mpga, m4a, awav, webm

client = OpenAI(api_key="")

# 음성 파일 불러오기
#   - rb: read byte
file = open("data/voice.wav", "rb") 

print(file)

# Whisper STT -> Text 파일 변경
# transcript = client.audio.transcriptions.create(
#     model="whisper-1", #현재 ahisper-1만 오픈
#     file=file,

# )

# print(transcript.text)

# Whisper STT -> SRT(자막) 파일 변경
#   - 자막 인덱스(1부터 시작)
#   - 시간 시:분:초, 밀리초
# transcript = client.audio.transcriptions.create(
#     model="whisper-1",
#     file=file,
#     response_format="srt"
# )
# print(transcript)

# # 영어 번역
# transcript = client.audio.transcriptions.create(
#     model="whisper-1",
#     file=file,
# )
# print(transcript.text)

# 
# 
# 
# 
# 
# 
