from openai import AssistantAgent

class ExploreAgent:
    def __init__(self):
        self.agent = AssistantAgent(name="ExploreAgent", instructions="Suggest attractions and local food for a destination.")

    async def run(self, destination: str):
        suggestions = {
            "bali": {
                "attractions": ["Ubud Monkey Forest", "Tanah Lot Temple", "Kuta Beach"],
                "food": ["Nasi Goreng", "Satay", "Babi Guling"]
            },
            "tokyo": {
                "attractions": ["Shibuya Crossing", "Tokyo Skytree", "Akihabara"],
                "food": ["Sushi", "Ramen", "Takoyaki"]
            },
            "paris": {
                "attractions": ["Eiffel Tower", "Louvre Museum", "Seine River Cruise"],
                "food": ["Croissants", "Crêpes", "Ratatouille"]
            }
        }
        info = suggestions.get(destination.lower(), {"attractions": [], "food": []})
        return {
            "reply": f"🗺️ **Attractions in {destination}**:\n- " + "\n- ".join(info["attractions"]) +
                     f"\n\n🍽️ **Try These Foods**:\n- " + "\n- ".join(info["food"]),
            "handoff_to": None
        }
