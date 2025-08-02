from openai import AssistantAgent
from tools.skill_tools import get_career_roadmap

class SkillAgent:
    def __init__(self):
        self.agent = AssistantAgent(name="SkillAgent", instructions="Show skill-building roadmap for a chosen field.")

    async def run(self, field: str):
        roadmap = get_career_roadmap(field)
        return {
            "reply": f"To become skilled in **{field}**, here's your roadmap:\n{roadmap}",
            "handoff_to": "JobAgent",
            "field": field
        }
