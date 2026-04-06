import sys
import os

sys.path.insert(0, os.path.dirname(__file__))

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
