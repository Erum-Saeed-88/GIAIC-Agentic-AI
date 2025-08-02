from openai import AssistantAgent
from openai.types.beta.assistant import Message
from openai import tool_call

class CareerAgent:
    def __init__(self):
        self.agent = AssistantAgent(name="CareerAgent", instructions="Help students explore career paths based on their interests.")

    async def run(self, messages: list[Message]):
        interest_map = {
            "technology": "data science",
            "design": "web development",
            "security": "cybersecurity"
        }
        for message in messages:
            for key in interest_map:
                if key in message.content.lower():
                    field = interest_map[key]
                    return {
                        "reply": f"You seem interested in {key}. I recommend looking into **{field}**.",
                        "handoff_to": "SkillAgent",
                        "field": field
                    }
        return {"reply": "Can you share more about your interests?"}
