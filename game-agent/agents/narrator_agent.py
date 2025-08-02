from openai import AssistantAgent
from tools.game_tools import generate_event

class NarratorAgent:
    def __init__(self):
        self.agent = AssistantAgent(name="NarratorAgent", instructions="Narrates the story and offers choices.")

    async def run(self, input_text: str):
        if "forest" in input_text.lower() or "mountain" in input_text.lower():
            location = "forest" if "forest" in input_text.lower() else "mountain"
            event = generate_event(location)
            handoff = "MonsterAgent" if "ambushes" in event or "dragon" in event else "ItemAgent"
            return {
                "reply": f"📜 {event}",
                "handoff_to": handoff,
                "context": location
            }
        return {
            "reply": "Where would you like to go: forest or mountain?",
            "handoff_to": None
        }
