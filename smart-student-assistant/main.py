# main.py
"""
Entry point for Smart Student Assistant.
Instead of typing `python -m agent.runner ...`,
you can just do `python main.py ...`
"""

from agent.runner import Runner

if __name__ == "__main__":
    Runner().run()

