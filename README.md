# Agentic Workflows

This repository demonstrates how to build modular AI agents with the OpenAI API and how to compose them into more complex workflows. The project is divided into two phases:

- **Phase&nbsp;1:** implementation of individual agents and accompanying test scripts.
- **Phase&nbsp;2:** composition of those agents into a small product management workflow.

The goal is to provide a practical introduction to retrieval‑augmented generation (RAG), persona-driven prompting, automated evaluation, routing, and action planning.

## Repository Structure

```
.
├── phase_1/               # agent library and tests
│   ├── workflow_agents/
│   │   └── base_agents.py
│   ├── direct_prompt_agent.py
│   ├── augmented_prompt_agent.py
│   ├── knowledge_augmented_prompt_agent.py
│   ├── rag_knowledge_prompt_agent.py
│   ├── evaluation_agent.py
│   ├── routing_agent.py
│   ├── action_planning_agent.py
│   ├── run_all_tests.py
│   └── test_*              # test scripts and sample outputs
└── phase_2/
    ├── agentic_workflow.py # uses agents from phase_1
    ├── Product-Spec-Email-Router.txt
    └── workflow_agents/
```

## Phase 1 – Agent Library

The first phase introduces seven agent classes located in `phase_1/workflow_agents/base_agents.py`. Each class illustrates a different pattern for interacting with an LLM:

- **DirectPromptAgent** – sends a user prompt directly to the model.
- **AugmentedPromptAgent** – prepends a fixed persona to influence the response.
- **KnowledgeAugmentedPromptAgent** – adds domain knowledge to the system prompt.
- **RAGKnowledgePromptAgent** – performs embedding-based search over large text to answer queries.
- **EvaluationAgent** – iteratively scores and improves another agent’s answer.
- **RoutingAgent** – selects an appropriate agent based on semantic similarity of the prompt.
- **ActionPlanningAgent** – extracts step‑by‑step actions from a request.

Each agent has a simple test script in the `phase_1` folder. Running `run_all_tests.py` executes them sequentially and stores their outputs in `test_output_*.txt` files.

## Phase 2 – Product Management Workflow

The second phase shows how to combine the library into a practical workflow. The script `phase_2/agentic_workflow.py` routes the steps of a high‑level prompt through specialized agents representing a Product Manager, Program Manager and Development Engineer. It demonstrates how action planning, routing and automated evaluation can be chained to generate user stories, product features and development tasks from a single specification.

## Installation

1. Clone the repository and navigate to the project directory.
   ```bash
   git clone https://github.com/your-username/agentic-workflows.git
   cd agentic-workflows
   ```
2. Create a virtual environment and activate it (optional but recommended).
   ```bash
   python -m venv venv
   source venv/bin/activate  # on Windows use venv\Scripts\activate
   ```
3. Install dependencies. The core libraries are `openai`, `python-dotenv`, `numpy` and `pandas`.
   ```bash
   pip install openai python-dotenv numpy pandas
   ```
4. Create a `.env` file in the repository root with your OpenAI API key:
   ```
   OPENAI_API_KEY=your_openai_api_key
   ```

## Running the Phase 1 Tests

From the `phase_1` directory run:
```bash
python run_all_tests.py
```
Each test stores its result in a `test_output_*.txt` file.

## Running the Phase 2 Workflow

With your API key configured, execute:
```bash
python phase_2/agentic_workflow.py
```
The script prints the steps derived from the action plan and the final output produced by the routed agents.

## Output Files

- `chunks-*.csv` – text chunks used by the RAG agent
- `embeddings-*.csv` – embeddings of those chunks
- `test_output_*.txt` – logs from each test script

## License

MIT License. Feel free to use and adapt this project.
