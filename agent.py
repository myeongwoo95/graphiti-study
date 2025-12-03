import os
import asyncio
from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from tools import add_numbers, multiply_numbers, get_string_length, save_to_memory, search_memory
from tools.graphiti_tools import set_graphiti_instance
from prompts.memory_agent_prompt import MEMORY_AGENT_PROMPT
from graphiti_core import Graphiti
from graphiti_core.llm_client.openai_client import OpenAIClient
from graphiti_core.llm_client.config import LLMConfig

load_dotenv()

# Graphiti 인스턴스 생성
custom_llm = OpenAIClient(
    config=LLMConfig(
        api_key=os.getenv("OPENAI_API_KEY"),
        model="gpt-5-nano",
        small_model="gpt-5-nano"
    )
)

# Neo4jGraph 인스턴스 생성
graphiti = Graphiti(
    uri=os.getenv("NEO4J_URI"),
    user=os.getenv("NEO4J_USERNAME"),
    password=os.getenv("NEO4J_PASSWORD"),
    llm_client=custom_llm
)

# Graphiti 인스턴스 등록
set_graphiti_instance(graphiti)

# LLM 설정
llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0,
)

# Agent 생성
agent = create_agent(
    model=llm,
    tools=[save_to_memory, search_memory],
    system_prompt=MEMORY_AGENT_PROMPT
)

# 비동기 함수 실행
async def main():
    result = await agent.ainvoke({
        "messages": [
            {"role": "user", "content": "전에 내가 이름 개명햇다고햇는데 멀로햇는지 기억나??"}
        ]
    })
    
    # 결과 출력
    if "messages" in result:
        print("\n✅ Agent 응답:")
        print(result['messages'][-1].content)
    else:
        print(result)

if __name__ == "__main__":
    asyncio.run(main())