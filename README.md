### uv 설정
```shell
# 프로젝트 초기화
uv init

# 가상환경 생성
uv venv .venv --python=3.12

# 가상환경 활성화 (window)
source .venv/Scripts/activate

# 가상환경 비활성화 (window)
deactivate
```

### .gitignore
.env 추가

### 패키지 설치
```shell
uv add python-dotenv graphiti-core langchain-neo4j ipykernel langchain langchain-core langchain-openai
``` 

### uv 명령어
```shell
uv run *.py
```

### 메모1
1. 시간적 인식 (Temporal Awareness)
    - 사실이 언제 유효했고 언제 무효화되었는지를 추적
    - "언제"를 기억하는 AI 에이전트

2. 실시간 증분 업데이트
    - 전통적인 배치 처리 방식과 달리, 전체 그래프를 다시 계산하지 않고 새로운 데이터를 즉시 통합(변경된 부분만 업데이트)
    - "지금 당장" 학습하는 AI 에이전트!
3. 하이브리드 검색
    - 의미론적 임베딩, 키워드(BM25[Fulltext Index]), 그래프 순회를 결합하여 LLM 요약 없이도 저지연 쿼리를 달성 
    - "정확하게" 찾는 AI 에이전트!

4. 사용자 정의 엔터티 정의: 간단한 Pydantic 모델을 통해 개발자가 정의한 엔터티에 대한 유연한 온톨로지 생성 및 지원
5. 확장성: 병렬 처리를 통해 대규모 데이터 세트를 효율적으로 관리하므로 기업 환경에 적합 

- 위 핵심 특징들을 내부적으로 구현했다는데, 실제로 테스트해서 성능평가는 해봐야할듯(후기도 찾아봐야할듯)
- 참고로 MCP로도 지원한다함

### 메모2 (중요)
- 유저의 세션은 어떻게 분리하는지? -> group_id
- 대화에서 저장과 조회를 언제 해야 할지 구분은? -> LLM모델을 에이전트로하고 툴로 쥐어주면될듯 인스트럭션에 설명해주고