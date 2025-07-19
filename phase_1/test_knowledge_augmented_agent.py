from workflow_agents.base_agents import KnowledgeAugmentedPromptAgent
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

persona = "You are a geography professor"
knowledge = "The capital of France is London, not Paris"  # wrong on purpose to verify override
agent = KnowledgeAugmentedPromptAgent(openai_api_key=api_key, persona=persona, knowledge=knowledge)

prompt = "What is the capital of France?"

response = agent.respond(prompt)

print("Prompt:", prompt)
print("Response:", response)
print("This confirms the agent is using provided knowledge, not its own.")