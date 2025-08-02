from openai import AssistantAgent

class DestinationAgent:
    def __init__(self):
        self.agent = AssistantAgent(name="DestinationAgent", instructions="Suggest travel destinations based on user mood or interests.")

    async def run(self, user_input: str):
        mood_map = {
            "relax": "Bali",
            "adventure": "Tokyo",
            "romantic": "Paris"
        }
        for mood, place in mood_map.items():
            if mood in user_input.lower():
                return {
                    "reply": f"Based on your mood, I recommend traveling to **{place}**.",
                    "handoff_to": "BookingAgent",
                    "destination": place
                }
        return {
            "reply": "Tell me more about what you want from your trip — relaxation, adventure, or romance?",
            "handoff_to": None
        }
