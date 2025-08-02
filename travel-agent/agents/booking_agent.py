from openai import AssistantAgent
from tools.travel_tools import get_flights, suggest_hotels

class BookingAgent:
    def __init__(self):
        self.agent = AssistantAgent(name="BookingAgent", instructions="Simulate booking flights and suggest hotels for a chosen destination.")

    async def run(self, destination: str):
        flight_info = get_flights(destination)
        hotel_info = suggest_hotels(destination)
        return {
            "reply": f"✈️ **Flight Info**:\n{flight_info}\n\n🏨 **Hotel Suggestions**:\n{hotel_info}",
            "handoff_to": "ExploreAgent",
            "destination": destination
        }
