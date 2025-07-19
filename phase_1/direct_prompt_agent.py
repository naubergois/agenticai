# Test script for DirectPromptAgent class

# TODO: 1 - Import the DirectPromptAgent class from BaseAgents
from workflow_agents.base_agents import DirectPromptAgent  # adjust path if needed

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# TODO: 2 - Load the OpenAI API key from the environment variables
openai_api_key = os.getenv("OPENAI_API_KEY")

prompt = "What is the capital of France?"

# TODO: 3 - Instantiate the DirectPromptAgent as direct_agent
direct_agent = DirectPromptAgent(openai_api_key=openai_api_key)

# TODO: 4 - Use direct_agent to send the prompt defined above and store the response
direct_agent_response = direct_agent.respond(prompt)

# Print the response from the agent
print(direct_agent_response)

# TODO: 5 - Print an explanatory message describing the knowledge source used by the agent to generate the response
print("\nExplanation:")
print("The agent used general world knowledge from the OpenAI model's training data,")
print("which includes well-known facts such as 'Paris is the capital of France.'")
