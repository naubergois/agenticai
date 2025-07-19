import os
import sys
from dotenv import load_dotenv

# Adiciona 'phase_1' ao sys.path para permitir importações corretas
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'phase_1')))

# Importa o agente correto
from workflow_agents.base_agents import RAGKnowledgePromptAgent

# Carrega variáveis do ambiente
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Define o conhecimento e o prompt
knowledge = "Clara hosts a podcast called Crosscurrents about science and culture. It covers ethics, AI, and biology."
prompt = "What is Clara's podcast about?"

# Cria o agente com chunking e overlap apropriado
agent = RAGKnowledgePromptAgent(api_key, persona="A science journalist", chunk_size=200, chunk_overlap=50)

# Gera os chunks e garante que o arquivo CSV será salvo com nome único
chunks = agent.chunk_text(knowledge)
print(f"Chunks gerados: {len(chunks)}")

# Calcula embeddings e salva no CSV
df_embeddings = agent.calculate_embeddings()
print(f"Embeddings calculados: {len(df_embeddings)}")

# Executa busca baseada em similaridade e gera resposta
response = agent.find_prompt_in_knowledge(prompt)

# Mostra resultado final
print("Prompt:", prompt)
print("RAG-Based Response:", response)