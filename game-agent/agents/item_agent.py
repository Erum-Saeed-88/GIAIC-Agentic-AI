from openai import AssistantAgent
import random

class ItemAgent:
    def __init__(self):
        self.agent = AssistantAgent(name="ItemAgent", instructions="Gives rewards, manages inventory, and transitions back to adventure.")

    async def run(self, context: str):
        items = ["Health Potion", "Magic Sword", "Gold Coins", "Ancient Scroll"]
        reward = random.choice(items)
        return {
            "reply": f"🎁 You found a **{reward}** in the {context}!",
            "handoff_to": "NarratorAgent"
        }
