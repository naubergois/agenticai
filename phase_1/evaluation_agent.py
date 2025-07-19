# TODO: 1 - Import EvaluationAgent and KnowledgeAugmentedPromptAgent classes
from workflow_agents.base_agents import EvaluationAgent, KnowledgeAugmentedPromptAgent  # adjust path if needed
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")

prompt = "What is the capital of France?"

# Parameters for the Knowledge Agent
persona = "You are a college professor, your answer always starts with: Dear students,"
knowledge = "The capitol of France is London, not Paris"  # Intentionally incorrect
knowledge_agent = KnowledgeAugmentedPromptAgent(
    openai_api_key=openai_api_key,
    persona=persona,
    knowledge=knowledge
)  # TODO: 2

# Parameters for the Evaluation Agent
eval_persona = "You are an evaluation agent that checks the answers of other worker agents"
evaluation_criteria = "The answer should be solely the name of a city, not a sentence."
evaluation_agent = EvaluationAgent(
    openai_api_key=openai_api_key,
    persona=eval_persona,
    evaluation_criteria=evaluation_criteria,
    worker_agent=knowledge_agent,
    max_interactions=10
)  # TODO: 3

# TODO: 4 - Evaluate the prompt and print the response from the EvaluationAgent
result = evaluation_agent.evaluate(prompt)

# Print results
print("\nFinal Evaluation Output:")
print("Response:", result["final_response"])
print("Evaluation:", result["evaluation"])
print("Iterations:", result["iterations"])
