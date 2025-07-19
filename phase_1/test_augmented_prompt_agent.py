from workflow_agents.base_agents import AugmentedPromptAgent
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

persona = "You are a friendly travel guide."
agent = AugmentedPromptAgent(api_key, persona)
prompt = "Tell me something about Paris."
response = agent.respond(prompt)

print("Prompt:", prompt)
print("Response:", response)