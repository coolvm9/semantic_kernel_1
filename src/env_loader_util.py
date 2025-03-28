import os
from dotenv import load_dotenv


def load_env(project_name, env_stage="dev"):
    home = os.path.expanduser("~")
    env_file = f"{env_stage}.env"
    env_path = os.path.join(home, ".env_configs", project_name, env_file)

    # Ensure the project directory exists
    os.makedirs(os.path.dirname(env_path), exist_ok=True)

    # If the environment file doesn't exist, create it (with default content if desired)
    if not os.path.exists(env_path):
        with open(env_path, 'w') as f:
            f.write("# Environment variables\n")
        print(f"Created new env file at: {env_path}")

    # Load shared env if exists
    shared_path = os.path.join(home, ".env_configs", "shared.env")
    if os.path.exists(shared_path):
        load_dotenv(dotenv_path=shared_path)

    # Load the project's env file
    load_dotenv(dotenv_path=env_path, override=True)

def get_env_variable(key):
    print(key + '----------')
    return os.getenv(key)

if __name__ == '__main__':
    import sys
    # Allow project_name to be set as a command-line argument
    if len(sys.argv) > 1:
        project_name = sys.argv[1]
    else:
        project_name = input("Enter the project name: ")

    load_env(project_name, "dev")
    print(get_env_variable('OPENAI_API_KEY'))