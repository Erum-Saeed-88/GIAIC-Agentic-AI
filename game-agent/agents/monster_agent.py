from openai import AssistantAgent
from tools.game_tools import roll_dice

class MonsterAgent:
    def __init__(self):
        self.agent = AssistantAgent(name="MonsterAgent", instructions="Handles monster combat using dice rolls.")

    async def run(self, context: str):
        player_roll = roll_dice()
        monster_roll = roll_dice()
        result = f"🎲 You rolled {player_roll}. Monster rolled {monster_roll}."

        if player_roll >= monster_roll:
            outcome = "✅ You defeated the monster!"
            next_agent = "ItemAgent"
        else:
            outcome = "❌ The monster overpowered you... You flee!"
            next_agent = "NarratorAgent"

        return {
            "reply": f"{result}\n{outcome}",
            "handoff_to": next_agent,
            "context": context
        }
