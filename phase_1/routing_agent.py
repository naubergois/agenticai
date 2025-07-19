# TODO: 1 - Import the KnowledgeAugmentedPromptAgent and RoutingAgent
from workflow_agents.base_agents import KnowledgeAugmentedPromptAgent, RoutingAgent  # Adjust the import path if needed
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

# Define the Texas agent
persona_texas = "You are a college professor"
knowledge_texas = "You know everything about Texas"
# TODO: 2
texas_agent = KnowledgeAugmentedPromptAgent(
    openai_api_key=openai_api_key,
    persona=persona_texas,
    knowledge=knowledge_texas
)

# Define the Europe agent
persona_europe = "You are a college professor"
knowledge_europe = "You know everything about Europe"
# TODO: 3
europe_agent = KnowledgeAugmentedPromptAgent(
    openai_api_key=openai_api_key,
    persona=persona_europe,
    knowledge=knowledge_europe
)

# Define the Math agent
persona_math = "You are a college math professor"
knowledge_math = "You know everything about math, you take prompts with numbers, extract math formulas, and show the answer without explanation"
# TODO: 4
math_agent = KnowledgeAugmentedPromptAgent(
    openai_api_key=openai_api_key,
    persona=persona_math,
    knowledge=knowledge_math
)

# Create the routing agent
routing_agent = RoutingAgent(openai_api_key, {})  # Initialized with empty agent list for now

# Define the routing rules
agents = [
    {
        "name": "texas agent",
        "description": "Answer a question about Texas",
        "func": lambda x: texas_agent.respond(x)  # TODO: 5
    },
    {
        "name": "europe agent",
        "description": "Answer a question about Europe",
        "func": lambda x: europe_agent.respond(x)  # TODO: 6
    },
    {
        "name": "math agent",
        "description": "When a prompt contains numbers, respond with a math formula",
        "func": lambda x: math_agent.respond(x)  # TODO: 7
    }
]

# Assign agents to the routing agent
routing_agent.agents = agents

# TODO: 8 - Test with multiple prompts
prompts = [
    "Tell me about the history of Rome, Texas",
    "Tell me about the history of Rome, Italy",
    "One story takes 2 days, and there are 20 stories"
]

for prompt in prompts:
    print("\nPrompt:", prompt)
    response = routing_agent.route(prompt)
    print("Routed Response:", response)
