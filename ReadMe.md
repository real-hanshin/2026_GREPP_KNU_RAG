# KBO 야구 규정 RAG 챗봇 실습

이 프로젝트는 LangChain과 RAG(Retrieval-Augmented Generation) 파이프라인을 활용하여, KBO 야구 규정에 대한 복잡한 조건부 질문이나 날짜 계산 등을 수행하는 AI 챗봇입니다.

## 프로젝트 구조

- `app.py`: 메인 실행 파일 (테스트 케이스 및 질의응답 실행)
- `chain.py`: 프롬프트 엔지니어링(CoT 적용) 및 RAG 체인(LCEL) 구성
- `vectorstore.py`: `dataset.csv` 로드, 문서 임베딩 및 FAISS 벡터 DB 관리
- `embeddings.py`: Ollama 기반 로컬 임베딩 모델 연동
- `dataset.csv`: KBO 야구 규정 원본 데이터
- `.env`: API 키 등 환경 변수 관리

## 사전 준비 사항

이 프로젝트는 로컬 임베딩(Ollama)과 클라우드 LLM(Groq)을 혼합하여 사용합니다.

1. **Ollama 설치 및 임베딩 모델 준비**
   로컬 환경에 [Ollama](https://ollama.com/)를 설치한 후, 터미널에서 아래 명령어를 실행해 임베딩 모델을 다운로드합니다.
   ```bash
   ollama pull nomic-embed-text-v2-moe




### 실행 방법
```bash
# 가상환경 실행 후
pip install -r requirements.txt

# 의존성 설치 이후
python app.py
```

### 실행 결과
1. 작성 가이드 예시 실행
2. 사용자 직접 입력
3. 종료
선택 (1/2/3): 1

입력: 나는 인공지능학과 3학년 조한신이야. 학번은 202203214이고. 홍길동 교수님께 LLM기초 과목(01분반) 기말고사 범위 중 langchain 부분에 대해 질문하는 면담 요청 메일을 정중하게 작성해줘. 교수님 메일은 hongGD@kongju.ac.kr이고, DB에 저장해줘.

[실행 결과]
이메일 초안이 저장되었습니다.
제목: **[LLM기초/01분반] 면담 요청 - 인공지능학과 3학년 조한신**

본문:
```
홍길동 교수님께

인공지능학과 3학년 조한신(학번: 202203214)입니다.

LLM기초 과목(01분반) 기말고사 범위 중 langchain 부분에 대해 질문하고자 면담을 요청드립니다.

바쁘신 와중에 시간을 내어 주시면 감사하겠습니다.

감사합니다.
조한신 드림
```"# 2026_GREPP_KNU_AGENT" 
