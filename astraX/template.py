import os

# Define the root directory for the project
root_dir = "astraX"

# Folder structure as a list of paths
folder_structure = [
    os.path.join(root_dir, 'astraX', 'core'),
    os.path.join(root_dir, 'astraX', 'embeddings'),
    os.path.join(root_dir, 'astraX', 'utils'),
    os.path.join(root_dir, 'astraX', 'agents'),
    os.path.join(root_dir, 'astraX', 'models'),
    os.path.join(root_dir, 'astraX', 'api_keys'),
    os.path.join(root_dir, 'examples'),
    os.path.join(root_dir, 'tests')
]

# Files to create inside the folders
files = {
    'astraX/core': [
        '__init__.py',
        'llm_loader.py',
        'agent_executor.py',
        'memory_manager.py',
        'tool_registry.py',
        'prompt_parser.py'
    ],
    'astraX/embeddings': [
        '__init__.py',
        'embedder.py',
        'rag_pipeline.py',
        'prompt_embeddings.py'
    ],
    'astraX/utils': [
        '__init__.py',
        'prompt_template.py',
        'parser.py',
        'rag_helpers.py'
    ],
    'astraX/agents': [
        '__init__.py',
        'astraX_agent.py',
        'action_tools.py'
    ],
    'astraX/models': [
        '__init__.py',
        'openai_model.py',  # Requires API key
        'anthropic_model.py',  # Requires API key
        'mistral_model.py',  # No API key needed, local model
        'grok_model.py',  # No API key needed, local model
        'gemma_model.py',  # No API key needed, local model
        'llama_model.py',  # No API key needed, local model
        'model_utils.py'
    ],
    'astraX/api_keys': [
        'openai_key.py',
        'anthropic_key.py'
    ],
    'examples': [
        'example1.py',
        'example2.py'
    ],
    'tests': [
        '__init__.py',
        'test_llm_loader.py',
        'test_agent_executor.py',
        'test_memory_manager.py',
        'test_tool_registry.py',
        'test_embedder.py',
        'test_rag.py'
    ],
    '': ['requirements.txt', 'setup.py']
}

# Function to create directories and files
def create_structure():
    try:
        # Create the folders
        for folder in folder_structure:
            os.makedirs(folder, exist_ok=True)  # exist_ok=True to avoid error if folder already exists

        # Create the files inside the folders
        for folder, filenames in files.items():
            for filename in filenames:
                filepath = os.path.join(folder, filename)
                # Create the file if it does not exist
                if not os.path.exists(filepath):
                    with open(filepath, 'w') as f:
                        pass  # Just create an empty file
                else:
                    pass  # Skip if the file already exists

        print("Folder structure for AstraX has been created successfully.")

    except Exception as e:
        print(f"Error occurred: {e}")

# Call the function
if __name__ == "__main__":
    create_structure()
