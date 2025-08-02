import asyncio
from agents.career_agent import CareerAgent
from agents.skill_agent import SkillAgent
from agents.job_agent import JobAgent

async def main():
    print("👩‍🏫 Welcome to Career Mentor Agent!\n")
    user_input = input("Tell me about your interests: ")

    # Career Agent
    career_agent = CareerAgent()
    messages = [{"role": "user", "content": user_input}]
    career_result = await career_agent.run(messages)
    print("🤖 CareerAgent:", career_result["reply"])

    # Skill Agent
    if career_result["handoff_to"] == "SkillAgent":
        skill_agent = SkillAgent()
        skill_result = await skill_agent.run(career_result["field"])
        print("🤖 SkillAgent:", skill_result["reply"])

        # Job Agent
        if skill_result["handoff_to"] == "JobAgent":
            job_agent = JobAgent()
            job_result = await job_agent.run(skill_result["field"])
            print("🤖 JobAgent:", job_result["reply"])

if __name__ == "__main__":
    asyncio.run(main())

