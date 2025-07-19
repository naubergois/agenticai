from workflow_agents.base_agents import RoutingAgent, KnowledgeAugmentedPromptAgent
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Create dummy agents
agent_texas = KnowledgeAugmentedPromptAgent(api_key, "You are a historian of Texas.", "Texas history is rich.")
agent_europe = KnowledgeAugmentedPromptAgent(api_key, "You are a historian of Europe.", "Europe has many cultures.")

# Routing agent setup
router = RoutingAgent(api_key, {})
router.agents = [
    {
        "name": "TexasAgent",
        "description": "Answer questions about Texas.",
        "func": lambda x: agent_texas.respond(x)
    },
    {
        "name": "EuropeAgent",
        "description": "Answer questions about Europe.",
        "func": lambda x: agent_europe.respond(x)
    }
]

prompt = "Tell me about Rome in Italy."
response = router.route(prompt)

print("Prompt:", prompt)
print("Response:", response)