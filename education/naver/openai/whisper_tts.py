from openai import OpenAI
from dotenv import load_dotenv, find_dotenv

_= load_dotenv(find_dotenv())

# Whisper TTS 소개
#   - model: tts-1, tts-1-hd
#   - input:입력 파일의 최대 길이는 4096자
#   - voice: 오디오 생성시 사용할 음성
#     (alloy, echo, fable, onyx, nova, shimmer)
#    - respinse_format: 오디오 형식(mp3, opus, aac, flac)

client = OpenAI(api_key="")

# 음성파일 저장경로
speech_file_path = "data/tts_audio.mp3"
response = client.audio.speech.create(
    model="tts-1",
    input="su, su, su, super nova!! nova Can't stop hypersetellar",
    voice="nova",
    response_format="mp3",
    speed=1,
)
response.stream_to_file(speech_file_path)