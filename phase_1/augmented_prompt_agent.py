# TODO: 1 - Import the AugmentedPromptAgent class
from workflow_agents.base_agents import AugmentedPromptAgent  # adjust the path if needed
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve OpenAI API key from environment variables
openai_api_key = os.getenv("OPENAI_API_KEY")
prompt = "What is the capital of France?"
persona = "You are a college professor; your answers always start with: 'Dear students,'"

# TODO: 2 - Instantiate an object of AugmentedPromptAgent with the required parameters
agent = AugmentedPromptAgent(openai_api_key=openai_api_key, persona=persona)

# TODO: 3 - Send the 'prompt' to the agent and store the response in a variable named 'augmented_agent_response'
augmented_agent_response = agent.respond(prompt)

# Print the agent's response
print(augmented_agent_response)

# TODO: 4 - Add a comment explaining:
# - What knowledge the agent likely used to answer the prompt.
# - How the system prompt specifying the persona affected the agent's response.

# The agent likely used general factual knowledge from the OpenAI model's internal training data,
# which includes common geography facts like "Paris is the capital of France."
# The system prompt specified the persona of a college professor and instructed the agent to start all responses with "Dear students,"
# which directly influenced the tone and structure of the output, making it more formal, educational, and aligned with a professor's voice.
