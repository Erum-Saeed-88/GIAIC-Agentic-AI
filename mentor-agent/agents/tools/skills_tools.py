from openai import tool

@tool
def get_career_roadmap(field: str) -> str:
    """
    Returns a list of skills and a roadmap for the selected career field.
    """
    roadmaps = {
        "data science": "1. Python\n2. Statistics\n3. Machine Learning\n4. SQL\n5. Projects",
        "web development": "1. HTML/CSS\n2. JavaScript\n3. React/Node.js\n4. Backend (Django/Express)\n5. Deploy Projects",
        "cybersecurity": "1. Networking Basics\n2. Linux\n3. Security Tools\n4. Threat Analysis\n5. Certs like CEH",
    }
    return roadmaps.get(field.lower(), "No roadmap available for this field.")
