from strands import Agent
from strands.models import BedrockModel
from prompt_utils import apply_prompt_template
import asyncio
import os
from strands_tools import calculator

os.environ["BYPASS_TOOL_CONSENT"] = "true"

agent_name = "basic_agent"

# 프롬프트 템플릿을 사용하여 시스템 프롬프트 생성
system_prompt = apply_prompt_template(
    prompt_name=agent_name, 
    prompt_context={"AGENT_NAME": agent_name}
)


print("=== 시스템 프롬프트 ===")
print(system_prompt)
print("=====================")
# 처음부터 streaming=True로 설정
model = BedrockModel(
    model_id="us.anthropic.claude-3-7-sonnet-20250219-v1:0",
    streaming=True  #
)
agent = Agent(
    system_prompt=system_prompt,
    model=model,
    tools=[calculator]  # 👈 Calculator tool - API 키 불필요, 수학/과학 계산
)

async def run_streaming():
    print("=== 스트리밍 응답 ===")
    
    user_input = "지난 분기 판매 데이터가 Q1: 100만원, Q2: 150만원, Q3: 180만원이야. 성장률을 분석하고 다음 분기 예측해줘"
    
    result = await asyncio.to_thread(agent, user_input)
    
    # message 속성 사용
    print(result.message)

if __name__ == "__main__":
    asyncio.run(run_streaming()) # 스트리밍 모드 활성화