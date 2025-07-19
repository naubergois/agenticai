🧠 Agentic Workflows – OpenAI-Based AI Agents
This project showcases the implementation of various agent-based workflows using the OpenAI API. It demonstrates how to build modular, composable agents capable of interacting via natural language, retrieving external knowledge, evaluating responses, routing tasks, and planning actions.

The system is structured to be easily extensible and serves as a practical introduction to RAG (Retrieval-Augmented Generation), persona-driven prompting, automated evaluation loops, and routing based on semantic similarity.

📁 Project Structure
bash
Copiar
Editar
starter/
│
├── phase_1/
│   ├── workflow_agents/
│   │   └── base_agents.py               # Contains all agent class definitions
│   ├── test_direct_prompt_agent.py      # Test script for DirectPromptAgent
│   ├── test_augmented_prompt_agent.py   # Test script for AugmentedPromptAgent
│   ├── test_knowledge_augmented_agent.py# Test for KnowledgeAugmentedPromptAgent
│   ├── test_rag_knowledge_agent.py      # Test for RAGKnowledgePromptAgent
│   ├── test_evaluation_agent.py         # Test for EvaluationAgent
│   ├── test_routing_agent.py            # Test for RoutingAgent
│   ├── test_action_planning_agent.py    # Test for ActionPlanningAgent
│   └── run_all_tests.py                 # Script to execute all tests and log output
⚙️ Installation
Clone the repository:

bash
Copiar
Editar
git clone https://github.com/your-username/agentic-workflows.git
cd agentic-workflows/starter/phase_1
Create a virtual environment:

bash
Copiar
Editar
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
Install dependencies:

bash
Copiar
Editar
pip install -r requirements.txt
Set up environment variables:

Create a .env file in the phase_1 directory:

env
Copiar
Editar
OPENAI_API_KEY=your_openai_api_key
🧪 Running the Tests
To run all the test scripts and save output logs:

bash
Copiar
Editar
python run_all_tests.py
You’ll see outputs like:

bash
Copiar
Editar
▶️ Executing test_direct_prompt_agent.py...
✅ Output saved to test_output_direct_prompt.txt
🧠 Agents Overview
Agent	Description
DirectPromptAgent	Simple LLM call with a user-provided prompt
AugmentedPromptAgent	Adds a fixed persona to influence response
KnowledgeAugmentedPromptAgent	Embeds external knowledge into system prompt
RAGKnowledgePromptAgent	Splits and embeds large texts, uses similarity search
EvaluationAgent	Iteratively evaluates responses against criteria
RoutingAgent	Selects the best agent using semantic similarity
ActionPlanningAgent	Extracts step-by-step instructions from user prompts

📦 Output Files
chunks-*.csv: stores text chunks for RAG agent

embeddings-*.csv: stores embeddings of chunks

test_output_*.txt: logs from each agent's test

✅ Final Notes
All agents use the GPT-3.5-Turbo model.

Embeddings are generated using text-embedding-3-large.

The project uses Vocareum’s OpenAI proxy endpoint (can be adjusted in code).

📜 License
MIT License. Feel free to use and adapt.

