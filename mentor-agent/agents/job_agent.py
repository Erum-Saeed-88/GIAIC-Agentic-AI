from openai import AssistantAgent

class JobAgent:
    def __init__(self):
        self.agent = AssistantAgent(name="JobAgent", instructions="Share real-world job roles based on skill domain.")

    async def run(self, field: str):
        job_map = {
            "data science": ["Data Analyst", "Machine Learning Engineer", "AI Researcher"],
            "web development": ["Frontend Developer", "Full-Stack Developer", "UI Engineer"],
            "cybersecurity": ["Security Analyst", "Penetration Tester", "SOC Analyst"]
        }
        jobs = job_map.get(field.lower(), ["No jobs found"])
        jobs_list = "\n- " + "\n- ".join(jobs)
        return {
            "reply": f"Here are real-world jobs for **{field}**:\n{jobs_list}",
            "handoff_to": None
        }
