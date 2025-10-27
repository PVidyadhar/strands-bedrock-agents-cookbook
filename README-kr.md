# Strands Agent

![Strands](strands.png)

Amazon Bedrock과 Strands Agents SDK를 활용한 AI 에이전트 구축 프로젝트입니다.

## 프로젝트 개요

이 프로젝트는 Strands Agents SDK를 사용하여 다양한 AI 에이전트를 구축하는 방법을 보여줍니다. 모델, 도구, 프롬프트라는 세 가지 핵심 구성 요소를 중심으로 간단하면서도 강력한 에이전트를 만들 수 있습니다.

## 주요 기능

### 포함된 유틸리티

- **advanced_rag_utils.py**: AWS Bedrock을 사용한 고급 RAG(Retrieval-Augmented Generation) 기능
  - Knowledge Base 검색 및 생성
  - 메타데이터 필터링
  - Bedrock 클라이언트 설정

- **llm_cost_utils.py**: LLM 사용량 모니터링 및 비용 계산
  - Bedrock 토큰 카운트 추적
  - CloudWatch 메트릭 통합
  - 비용 분석

### 주요 사용 사례

Strands.ipynb 노트북에는 다음과 같은 10가지 실용적인 사용 사례가 포함되어 있습니다:

1. **웹 스크래핑**: Hacker News에서 기사 제목과 링크 추출
2. **주식 가격 분석**: 이동평균, 변동성, 수익률 분석 및 시각화
3. **보험 청구 검사**: 기상 데이터 검증 및 DynamoDB 저장
4. **Knowledge Base + 인터넷 검색**: 10K 문서 검색 및 뉴스 수집
5. **커스텀 Python 도구**: LLM 사용량 계산기
6. **DataFrame 조작**: pandas를 활용한 데이터 처리
7. **PySpark 데이터 처리**: 대용량 데이터 변환 및 저장
8. **머신러닝 파이프라인**: 고객 이탈 예측 모델 구축
9. **멀티 에이전트 시스템**: 금융 자문 에이전트 오케스트레이션
10. **MCP 통합**: AWS 문서 쿼리 및 아키텍처 다이어그램 생성

## 설치 방법

### 필수 요구사항

```bash
pip install strands-agents strands-agents-tools strands-agents-builder nest_asyncio uv
```

### 선택적 라이브러리

```bash
# 금융 분석용
pip install yfinance matplotlib

# 웹 스크래핑용
pip install beautifulsoup4 pandas requests

# 머신러닝용
pip install scikit-learn joblib seaborn
```

## 사용 방법

### 기본 에이전트 생성

```python
from strands import Agent

agent = Agent()
agent("Explain Amazon Bedrock Agents?")
```

### 도구를 사용한 에이전트

```python
from strands_tools import python_repl, file_write
from strands import Agent
import os

os.environ["BYPASS_TOOL_CONSENT"] = "true"

agent = Agent(tools=[python_repl, file_write])
response = agent("웹 페이지에서 데이터를 스크래핑하고 CSV로 저장해줘")
```

### 커스텀 도구 정의

```python
from strands import tool, Agent

@tool
def my_custom_tool(query: str) -> str:
    """커스텀 도구 설명"""
    # 도구 로직
    return result

agent = Agent(tools=[my_custom_tool])
```

## 설정

프로젝트 루트에 `variables.json` 파일을 생성하여 AWS 설정을 구성하세요:

```json
{
  "kbSemanticChunk": "your-knowledge-base-id",
  "region": "us-west-2",
  "account_number": "your-aws-account-number"
}
```

## 지원 모델

- Amazon Bedrock 모델 (Nova, Claude, Titan 등)
- Anthropic Claude 모델 패밀리
- Ollama (로컬 개발용)
- LiteLLM을 통한 기타 제공자

## 파일 구조

```
.
├── Strands.ipynb                      # 메인 데모 노트북
├── research_agent_kb_internet.ipynb   # 연구 에이전트 예제
├── advanced_rag_utils.py              # RAG 유틸리티 함수
├── llm_cost_utils.py                  # 비용 계산 도구
├── kb_id.txt                          # Knowledge Base ID
├── strands.png                        # 프로젝트 이미지
└── README.md                          # 이 파일
```

## 주요 특징

- **모델 중심 접근**: 다양한 LLM 모델을 쉽게 통합
- **풍부한 도구 생태계**: 20개 이상의 사전 구축된 도구 및 MCP 서버 지원
- **간단한 API**: 몇 줄의 코드로 강력한 에이전트 구축
- **확장 가능**: 로컬 개발부터 프로덕션 배포까지
- **AWS 통합**: Bedrock, DynamoDB, CloudWatch 등과 네이티브 통합

## 참고 자료

- [Strands Agents 공식 문서](https://docs.strands.ai)
- [Amazon Bedrock 문서](https://docs.aws.amazon.com/bedrock/)
- [Strands Agents 발표 블로그](https://aws.amazon.com/blogs/)

## 라이선스

이 프로젝트의 라이선스는 프로젝트 소유자에게 문의하세요.

## 기여

이슈와 풀 리퀘스트를 환영합니다!
