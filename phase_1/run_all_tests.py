import subprocess
import os

BASE_DIR = os.path.dirname(__file__)

# Lista de scripts de teste e arquivos de saída
tests = [
    ("test_direct_prompt_agent.py", "test_output_direct_prompt.txt"),
    ("test_augmented_prompt_agent.py", "test_output_augmented_prompt.txt"),
    ("test_knowledge_augmented_agent.py", "test_output_knowledge_agent.txt"),
    ("test_evaluation_agent.py", "test_output_evaluation.txt"),
    ("test_routing_agent.py", "test_output_routing.txt"),
    ("test_action_planning_agent.py", "test_output_action_planning.txt"),
    ("test_rag_knowledge_agent.py", "test_output_rag_agent.txt")
]

print("Running agent test scripts...\n")

def abs_path(name: str) -> str:
    """Return path relative to this file's directory."""
    return os.path.join(BASE_DIR, name)

for script, output_file in tests:
    print(f"Executing {script}...")
    try:
        script_path = abs_path(script)
        output_path = abs_path(output_file)
        with open(output_path, "w", encoding="utf-8") as out:
            subprocess.run(["python", script_path], stdout=out, stderr=subprocess.STDOUT, check=False)
        print(f"Output saved to {output_file}\n")
    except subprocess.CalledProcessError as e:
        print(f"Error running {script}: {e}\n")

print("All tests completed.")
