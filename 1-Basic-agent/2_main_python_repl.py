from strands import Agent
from strands.models import BedrockModel
from prompt_utils import apply_prompt_template
import asyncio
import os
from strands_tools import python_repl

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
    tools=[python_repl]  # 👈 tools 연동 (한 줄 추가)  #https://github.com/strands-agents/tools
)

async def run_streaming():
    print("=== 스트리밍 응답 ===")
    user_input = "Python에서 subprocess를 사용해서 'ls -la' 명령을 실행해줘"#"Hello world 를 프린팅하는 파이썬 코드를 작성하고 실행시켜 줄래?"
    
    result = await asyncio.to_thread(agent, user_input)
    
    # message 속성 사용
    print(result.message)

if __name__ == "__main__":
    asyncio.run(run_streaming()) # 스트리밍 모드 활성화