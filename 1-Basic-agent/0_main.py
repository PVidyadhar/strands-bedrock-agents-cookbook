from strands import Agent
from strands.models import BedrockModel
from prompt_utils import apply_prompt_template
import os

os.environ["BYPASS_TOOL_CONSENT"] = "true"

agent_name = "basic_agent"

# 프롬프트 템플릿을 사용하여 시스템 프롬프트 생성
system_prompt = apply_prompt_template(
    prompt_name=agent_name, 
    prompt_context={"AGENT_NAME": agent_name}
)

# BedrockModel 객체 생성
model = BedrockModel(
    model_id="us.anthropic.claude-3-7-sonnet-20250219-v1:0",
     streaming=False 
)

# Agent 생성
agent = Agent(
    system_prompt=system_prompt,
    model=model
)

if __name__ == "__main__":
    user_input = "Hi, nice to meet you. I'm currently implementing the Strands Agents SDK. Can you provide me with a response?"
    
    # 동기 방식 실행
    response = agent(user_input)
    print(response)