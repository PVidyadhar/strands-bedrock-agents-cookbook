from strands import Agent
from strands.models import BedrockModel
from prompt_utils import apply_prompt_template
import asyncio
import os
from strands_tools import python_repl, calculator

os.environ["BYPASS_TOOL_CONSENT"] = "true"

agent_name = "basic_agent"

# 프롬프트 템플릿을 사용하여 시스템 프롬프트 생성
system_prompt = apply_prompt_template(
    prompt_name=agent_name, 
    prompt_context={"AGENT_NAME": agent_name}
)

# 처음부터 streaming=True로 설정
model = BedrockModel(
    model_id="us.anthropic.claude-3-7-sonnet-20250219-v1:0",
    streaming=True
)

agent = Agent(
    system_prompt=system_prompt,
    model=model,
    tools=[python_repl, calculator]  # 👈 두 가지 tool 모두 사용 - 복합적인 데이터 분석
)

async def run_streaming():
    print("=== 스트리밍 응답 ===")
    
    # 복합적인 데이터 분석 시나리오:
    # 1. Calculator로 기본 ROI 계산
    # 2. Python REPL로 여러 프로젝트의 통계 분석
    user_input = """
    우리 회사는 3개 프로젝트에 투자했어:
    - 프로젝트 A: 투자 50만원, 수익 75만원
    - 프로젝트 B: 투자 80만원, 수익 100만원  
    - 프로젝트 C: 투자 120만원, 수익 180만원
    
    각 프로젝트의 ROI를 계산하고, Python으로 평균 ROI와 표준편차를 구해서
    어떤 프로젝트가 가장 효율적이고 안정적인지 분석해줘.
    """
    
    result = await asyncio.to_thread(agent, user_input)
    
    # message 속성 사용
    print(result.message)

if __name__ == "__main__":
    asyncio.run(run_streaming())  # 스트리밍 모드 활성화
