from workflow_agents.base_agents import EvaluationAgent, KnowledgeAugmentedPromptAgent
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Knowledge agent
persona_worker = "You are a bot that always says the capital of France is London"
knowledge = "The capital of France is London"
worker_agent = KnowledgeAugmentedPromptAgent(api_key, persona_worker, knowledge)

# Evaluation agent
persona_eval = "You are an evaluation agent that checks if the answer is just the correct capital city"
criteria = "The answer should be 'Paris' and only that."

evaluator = EvaluationAgent(api_key, persona_eval, criteria, worker_agent, max_interactions=3)

prompt = "What is the capital of France?"
result = evaluator.evaluate(prompt)

print("Prompt:", prompt)
print("Final Response:", result['final_response'])
print("Evaluation:", result['evaluation'])
print("Iterations:", result['iterations'])