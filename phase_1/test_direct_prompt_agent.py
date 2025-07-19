from workflow_agents.base_agents import DirectPromptAgent
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

agent = DirectPromptAgent(api_key)
prompt = "What is the capital of France?"
response = agent.respond(prompt)

print("Prompt:", prompt)
print("Response:", response)