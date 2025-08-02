import asyncio
from agents.narrator_agent import NarratorAgent
from agents.monster_agent import MonsterAgent
from agents.item_agent import ItemAgent

async def main():
    print("🧙 Welcome to the Fantasy Adventure Game!\n")

    narrator = NarratorAgent()
    monster = MonsterAgent()
    item = ItemAgent()

    current_agent = "NarratorAgent"
    context = None

    while True:
        if current_agent == "NarratorAgent":
            user_input = input("\nWhere will you go (forest or mountain)? ")
            result = await narrator.run(user_input)
        elif current_agent == "MonsterAgent":
            result = await monster.run(context)
        elif current_agent == "ItemAgent":
            result = await item.run(context)
        else:
            print("⚠️ Unknown agent. Ending game.")
            break

        print(f"\n🤖 {current_agent}: {result['reply']}")
        current_agent = result.get("handoff_to")
        context = result.get("context")

        if current_agent is None:
            break

if __name__ == "__main__":
    asyncio.run(main())

