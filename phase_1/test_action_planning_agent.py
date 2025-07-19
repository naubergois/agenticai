from workflow_agents.base_agents import ActionPlanningAgent
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

knowledge = "You break a prompt into a list of steps needed to complete it."
agent = ActionPlanningAgent(api_key, knowledge)

prompt = "Create a user story, define the feature, and list tasks"
steps = agent.extract_steps_from_prompt(prompt)

print("Prompt:", prompt)
print("Extracted Steps:")
for i, step in enumerate(steps, 1):
    print(f"{i}. {step}")