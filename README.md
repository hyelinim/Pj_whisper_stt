# PJ_whisper_stt
음성인식(stt) Whisper 모델을 사용한 API 구현하기
-FastAPI → API 생성 → Whisper(stt) 사용
-터미널: uvicorn main:app --reload (Fast API 실행)
-FastAPI 적극 추천(쉽게 빠르고, 코드가 간결, swagger API 명세서, 테스트)

서버 → API: 음성파일 → whisperAPI → 결과(텍스트)


### 1. 가상 환경 구축
- Terminal은 command prompt 사용할 것!
- python -m venv ./ venv
- .\venv\Scripts\activate (가상환경 접속)
- 가상환경 생성 후 Ctrl+Shift+P -> Python select interpreter -> venv
- 터미널 새로 키면 venv 가상환경 접속됨.

- venv와 anaconda 차이점
 + venv: 프로젝트 1개 한정
 + anaconda: 모든 프로젝트에 사용 가능

### 2. 라이브러리 설치
- requirements.txt 파일 생성
- 설치해야할 라이브러리 추가
-터미널에서 pip install -r requirements.txt -> 목록에 라이브러리 모두 설치

### 3.
https://platform.openai.com


### 4. 음성인식 소개
#### 4-1. Whisper AI 사용해보기
- STT(Speech to Text)
   +  회의자료 정리, 청각장애인을 위한 기기, 자막
- TSS(Text to Speech)
   +  텔레마케터(ARS)

- STT + ChatGPT →  활용시 성능은?
- TTS + ChatGPT →  활용시 성능은?

- STT & TSS 모델
   + 네이버, 카카오, 구글, OpenAI(Whisper)
   + 한국어 성능을 고려해야함 → Whisper 한국어 성능 매우 높음
   + WER(Word Error Rate) 성능지표, 낮을수록 좋음
     OpenAI(Whisper)의 한국어 WER이 3.1
                       영어 English 4.1
   + STT & TTS 모델이 ChatGPT와 연계해서 서비스하는 횟수가 많음

#### 4-2. 음성인식 프로세스
1. 음성 획득
   - 마이크와 같은 장치에서 음성을 획득하고 아날로그 음성 신호를 디지털 데이터로 변환
2. 특징 추출
   - 변환된 디지털 데이터는 음성의 특징을 추출하기 위해 처리, 음성의 음향, 특성(음량, 음높이, 음색 등)을 이래하기 위해 수행
3. 음소 식별
   - 음성을 음소(음성의 최소 단위)로 분해 / "나무" → n, a, m, u
4. 단어 인식
   - AI는 이 음소들을 조합해 단어를 생성, 어떤 언어의 어떤 단어에 해당하는지 판단
5. 문맥 이해와 변환
   - 마지막으로 AI는 문맥을 이해하고 적절한 문접과 어휘를 사용하여 음성을 텍스트로 변환
 요약: 전처리 → 패턴인식 → 후처리

#### 4-3. 음성인식 평가방향
1. 화자 독립(YES) or 화자 종속(NO) → 화자 독립
2. 연속 단어 처리 유무             → 연속 단어 처리
3. 단어 처리 수(양)                → 많으면 많을수록 좋음

#### 4-4. 음성인식 평가지표
1. CER(Character Error Rate) : 문자 평가
   - 음성(cat), AI(hat) → CER(0.33) = 1/3
2. WER(Word Error Rate)      : 단어 평가
   - 음성(The cat is black), AI(a cat is black) → WER(0.25) = 1/4
 * 음성인식 모델 성능 비교!

#### 4-5. 음성인식 분야 어려움!
1. 음성과 음향
   - 음성: 사람의 소리
   - 음향: 배경에 존재하는 다양한 소리
2. 사람마다 발성기관 모두 다름, 읽는 속도

#### 5. API에 데이터(값) 전달 방법
1. METHOD(GET) → 쿼리스트링 ex) url?변수=값&변수=값
2. METHOD(POST) → http message BODY에 담아서 보내기, HTML Form으로 전달

# 클라이언트 - HTTP 프로토콜 - 서버'
# → 클라이언트(API 요청) - HTTP message 형식 - 서버(API)
# → HTTP message(header, body)
# → HTTP message → requests 라이브러리 사용해서 생성 가능!
# http://127.0.0.1:8000

#### 6. Docker Container
- Docker Engine(Docker Desktop) 동작
- Docker Image → Docker Engine → Docker Container 생성(사용)
- Dockerfile → build → Docker Image 생성!
- docker compose 사용 전체를 관장

- 객체지향언어: class(설계도면) → 객체생성 → 인스턴스(실체) →사용!
- 컨테이너: image(컨테이너 도면) → 도커엔진: 컨테이너 생성 → 컨테이너 → 사용!

- API(Whisper, Clova) → Docker Container 서비스

#### 7. API 서비스 배포
1. 프로그래밍 개발
2. Dockerfile 작성
3. Build를 통한 Docker image 생성
   - docker images (현재 사용할 수 있는 도커이미지 목록 출력)
   - docker build -t "이미지 이름", (Dockerfile을 사용한 도커 이미지 생성)
   - docker ps (현재 실행중인 도커컨테이너 목록 출력)
   - docker run ~~~ (도커 컨테이너 실행 + 도커 이미지 필요!) 
4. docker-compose.yaml 작성
5. docker compose 실행(서비스 동작)
   - docker compose up -d
   - docker-compose or docker compose 명령어(docker compose 최신 버전)
   - up(실행), stop(멈춤), down(종료)
   - "-d" : daemon으로 실행하세요. (daemon: 백그라운드에서 동작하세요.)
6. 사용
   - docker ps
   - docker logs "컨테이너 이름" (도커 컨테이너의 로그 확인)
   - docker exec -it "컨테이너 이름" /bin/bash
   - docker compose down (컨테이너 종료)
   - docker compose up
   - docker rmi -f "컨테이너 이름" (도커 이미지 단건 삭제)
   - docker rmi -f $(docker images -q) (도커 이미지 모두 삭제)

docker compose?
   - 특정 어플리케이션을 개발하는데 필요한 프로그램들이 다수
   - pyhton(uvicorn), mariadb, nginx, CertBot , ...
   - 위의 내용들을 각각 컨테이너로 구동
   - 도커 컨테이너는 독립된 환경에서 동작하기 때문에
     일반적으로 다른 컨테이너와 통신이 불가
   - 도커 네트워크 설정을 통해서 컨테이너간 통신이 가능하게 할 수 있음
   - 도커만 사용하면 하나의 어플리케이션을 동작하기 위해 필요한 프로그램이
     5개 있다고 가정했을 떄 docker run 명령어를 5번해서 각각 설명해야 함(비효율적, 관리 어려움)
   - 일반적인 도커는 docker run을 통해서 컨테이너를 동작한 후에
     도커 네트워크 설정을 할 수 있음.
   - docker compose를 사용하면 하나의 파일로 어플리케이션에 필요한모든 프로그램을 관리할 수 있고, 
     파일 자체에서 볼륨과 네트워크 등의 설정을 가능함
   