import sys
import os

sys.path.insert(0, os.path.dirname(__file__))

# Load .env
env_path = os.path.join(os.path.dirname(__file__), "../.env")
if os.path.exists(env_path):
    with open(env_path) as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                key, value = line.split("=", 1)
                os.environ.setdefault(key.strip(), value.strip())

from application.agent_executor import agent_executor


def main():
    print("Productivity Engine — type 'exit' to quit\n")
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() == "exit":
            break
        if not user_input:
            continue
        result = agent_executor(user_input)
        print(f"Agent: {result}\n")


if __name__ == "__main__":
    main()
