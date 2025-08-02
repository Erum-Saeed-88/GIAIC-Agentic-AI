import asyncio
from agents.destination_agent import DestinationAgent
from agents.booking_agent import BookingAgent
from agents.explore_agent import ExploreAgent

async def main():
    print("🌍 Welcome to AI Travel Designer Agent!\n")
    user_input = input("What kind of travel are you interested in (relaxation, adventure, romantic)? ")

    # DestinationAgent
    dest_agent = DestinationAgent()
    dest_result = await dest_agent.run(user_input)
    print("\n🤖 DestinationAgent:", dest_result["reply"])

    # BookingAgent
    if dest_result["handoff_to"] == "BookingAgent":
        booking_agent = BookingAgent()
        booking_result = await booking_agent.run(dest_result["destination"])
        print("\n🤖 BookingAgent:", booking_result["reply"])

        # ExploreAgent
        if booking_result["handoff_to"] == "ExploreAgent":
            explore_agent = ExploreAgent()
            explore_result = await explore_agent.run(booking_result["destination"])
            print("\n🤖 ExploreAgent:", explore_result["reply"])

if __name__ == "__main__":
    asyncio.run(main())

