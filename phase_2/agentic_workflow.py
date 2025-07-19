import os
import sys

# ✅ Corrigido: adiciona diretamente o caminho onde está base_agents.py
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'phase_1', 'workflow_agents')))

# ✅ Agora importa direto do arquivo
from base_agents import (
    ActionPlanningAgent,
    KnowledgeAugmentedPromptAgent,
    EvaluationAgent,
    RoutingAgent
)
import os
from dotenv import load_dotenv

# TODO: 2 - Load the OpenAI key
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

# TODO: 3 - Load the product spec
with open("Product-Spec-Email-Router.txt", "r", encoding="utf-8") as file:
    product_spec = file.read()

# ------------------- Instantiate Agents -------------------

# Action Planning Agent
knowledge_action_planning = (
    "Stories are defined from a product spec by identifying a "
    "persona, an action, and a desired outcome for each story. "
    "Each story represents a specific functionality of the product "
    "described in the specification. \n"
    "Features are defined by grouping related user stories. \n"
    "Tasks are defined for each story and represent the engineering "
    "work required to develop the product. \n"
    "A development Plan for a product contains all these components"
)

# TODO: 4 - Instantiate action_planning_agent
action_planning_agent = ActionPlanningAgent(
    openai_api_key=openai_api_key,
    knowledge=knowledge_action_planning
)

# Product Manager Agent
persona_product_manager = "You are a Product Manager, you are responsible for defining the user stories for a product."
knowledge_product_manager = (
    "Stories are defined by writing sentences with a persona, an action, and a desired outcome. "
    "The sentences always start with: As a "
    "Write several stories for the product spec below, where the personas are the different users of the product. "
    + product_spec  # TODO: 5
)

# TODO: 6 - Instantiate product_manager_knowledge_agent
product_manager_knowledge_agent = KnowledgeAugmentedPromptAgent(
    openai_api_key=openai_api_key,
    persona=persona_product_manager,
    knowledge=knowledge_product_manager
)

# TODO: 7 - Instantiate product_manager_evaluation_agent
product_manager_evaluation_agent = EvaluationAgent(
    openai_api_key=openai_api_key,
    persona="You are an evaluation agent that checks the answers of other worker agents.",
    evaluation_criteria="The answer should follow this format: As a [type of user], I want [an action or feature] so that [benefit/value].",
    worker_agent=product_manager_knowledge_agent,
    max_interactions=5
)

# Program Manager Agent
persona_program_manager = "You are a Program Manager, you are responsible for defining the features for a product."
knowledge_program_manager = "Features of a product are defined by organizing similar user stories into cohesive groups."
program_manager_knowledge_agent = KnowledgeAugmentedPromptAgent(
    openai_api_key=openai_api_key,
    persona=persona_program_manager,
    knowledge=knowledge_program_manager
)

# TODO: 8 - Instantiate program_manager_evaluation_agent
program_manager_evaluation_agent = EvaluationAgent(
    openai_api_key=openai_api_key,
    persona="You are an evaluation agent that checks the answers of other worker agents.",
    evaluation_criteria="The answer should be product features that follow the following structure: "
                        "Feature Name: A clear, concise title that identifies the capability\n"
                        "Description: A brief explanation of what the feature does and its purpose\n"
                        "Key Functionality: The specific capabilities or actions the feature provides\n"
                        "User Benefit: How this feature creates value for the user",
    worker_agent=program_manager_knowledge_agent,
    max_interactions=5
)

# Development Engineer Agent
persona_dev_engineer = "You are a Development Engineer, you are responsible for defining the development tasks for a product."
knowledge_dev_engineer = "Development tasks are defined by identifying what needs to be built to implement each user story."
development_engineer_knowledge_agent = KnowledgeAugmentedPromptAgent(
    openai_api_key=openai_api_key,
    persona=persona_dev_engineer,
    knowledge=knowledge_dev_engineer
)

# TODO: 9 - Instantiate development_engineer_evaluation_agent
development_engineer_evaluation_agent = EvaluationAgent(
    openai_api_key=openai_api_key,
    persona="You are an evaluation agent that checks the answers of other worker agents.",
    evaluation_criteria="The answer should be tasks following this exact structure: "
                        "Task ID: A unique identifier for tracking purposes\n"
                        "Task Title: Brief description of the specific development work\n"
                        "Related User Story: Reference to the parent user story\n"
                        "Description: Detailed explanation of the technical work required\n"
                        "Acceptance Criteria: Specific requirements that must be met for completion\n"
                        "Estimated Effort: Time or complexity estimation\n"
                        "Dependencies: Any tasks that must be completed first",
    worker_agent=development_engineer_knowledge_agent,
    max_interactions=5
)

# ------------------- Routing Agent -------------------

# TODO: 11 - Define support functions
def product_manager_support_function(input_query):
    result = product_manager_evaluation_agent.evaluate(input_query)
    return result["final_response"]

def program_manager_support_function(input_query):
    result = program_manager_evaluation_agent.evaluate(input_query)
    return result["final_response"]

def development_engineer_support_function(input_query):
    result = development_engineer_evaluation_agent.evaluate(input_query)
    return result["final_response"]

# TODO: 10 - Instantiate routing_agent with routes
routing_agent = RoutingAgent(
    openai_api_key=openai_api_key,
    agents=[
        {
            "name": "Product Manager",
            "description": "Generate user stories from a product spec",
            "func": product_manager_support_function
        },
        {
            "name": "Program Manager",
            "description": "Organize user stories into product features",
            "func": program_manager_support_function
        },
        {
            "name": "Development Engineer",
            "description": "Generate development tasks from user stories",
            "func": development_engineer_support_function
        }
    ]
)

# ------------------- Workflow Execution -------------------

print("\n*** Workflow execution started ***\n")
workflow_prompt = "What would the development tasks for this product be?"
print(f"Task to complete in this workflow, workflow prompt = {workflow_prompt}")

print("\nDefining workflow steps from the workflow prompt")
# TODO: 12 - Implement the workflow
workflow_steps = action_planning_agent.extract_steps_from_prompt(workflow_prompt)
completed_steps = []

for idx, step in enumerate(workflow_steps):
    print(f"\n🔄 Executing Step {idx + 1}: {step}")
    result = routing_agent.route(step)
    print(f"✅ Result: {result}")
    completed_steps.append(result)

print("\n🟩 Final Output of Workflow:")
for step in completed_steps:
    print(step)
