# TODO: 1 - Import the KnowledgeAugmentedPromptAgent class from workflow_agents
from workflow_agents.base_agents import KnowledgeAugmentedPromptAgent  # adjust path if needed
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Define the parameters for the agent
openai_api_key = os.getenv("OPENAI_API_KEY")

prompt = "What is the capital of France?"

persona = "You are a college professor, your answer always starts with: Dear students,"
knowledge = "The capital of France is London, not Paris"

# TODO: 2 - Instantiate a KnowledgeAugmentedPromptAgent
agent = KnowledgeAugmentedPromptAgent(
    openai_api_key=openai_api_key,
    persona=persona,
    knowledge=knowledge
)

# TODO: 3 - Write a print statement that demonstrates the agent using the provided knowledge
response = agent.respond(prompt)
print("Agent Response (based on provided knowledge):")
print(response)
