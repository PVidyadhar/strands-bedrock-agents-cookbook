from strands import Agent
from strands.models import BedrockModel
from prompt_utils import apply_prompt_template
import asyncio
import os

os.environ["BYPASS_TOOL_CONSENT"] = "true"

agent_name = "basic_agent" #https://github.com/strands-agents/tools

# 프롬프트 템플릿을 사용하여 시스템 프롬프트 생성
system_prompt = apply_prompt_template(
    prompt_name=agent_name, 
    prompt_context={"AGENT_NAME": agent_name}
)

# 처음부터 streaming=True로 설정
model = BedrockModel(
    model_id="us.anthropic.claude-3-7-sonnet-20250219-v1:0",
    streaming=True  #
)
agent = Agent(
    system_prompt=system_prompt,
    model=model
)

async def run_streaming():
    print("=== 스트리밍 응답 ===")
    user_input = "Hi, nice to meet you. I'm currently implementing the Strands Agents SDK. Can you provide me with a response 10 categories of animals?"
    
    result = await asyncio.to_thread(agent, user_input)
    
    # message 속성 사용
    print(result.message)

if __name__ == "__main__":
    asyncio.run(run_streaming()) # 스트리밍 모드 활성화