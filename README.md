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
uv add python-dotenv graphiti-core langchain-neo4j ipykernel
```

### uv 명령어
```shell
uv run *.py
```