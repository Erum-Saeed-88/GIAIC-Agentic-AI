# agent/smart_agent.py
import os
from typing import List, Dict
from time import sleep

# official google genai import (per docs)
from google import genai
from google.genai import types

# simple helper to read env
def get_api_key():
    key = os.getenv("GEMINI_API_KEY")
    if not key:
        raise EnvironmentError(
            "GEMINI_API_KEY missing. Set it as environment variable before running."
        )
    return key

class SmartStudentAgent:
    """
    Simple Smart Student Assistant using Gemini (google-genai SDK).
    Methods:
      - answer_question
      - make_quiz
      - make_flashcards
      - plan_study
    """

    def __init__(self, model: str = "gemini-2.5-flash"):
        # client will pick up GEMINI_API_KEY from env automatically (per docs).
        # we still call get_api_key() to show clearer error if missing.
        get_api_key()
        self.client = genai.Client()
        self.model = model

    def _call_model(self, prompt: str, max_wait: int = 30) -> str:
        """
        Core call to Gemini using generate_content per official quickstart.
        """
        response = self.client.models.generate_content(
            model=self.model,
            contents=prompt
        )
        # The SDK returns an object with .text property per docs.
        return response.text

    def answer_question(self, question: str) -> str:
        prompt = f"Student question (short, clear answer):\n{question}\n\nPlease answer simply, with examples if helpful."
        return self._call_model(prompt)

    def make_quiz(self, topic: str, num_questions: int = 5) -> List[Dict]:
        prompt = (
            f"Create {num_questions} multiple choice questions (4 options each) "
            f"on this topic: {topic}. For each question, give 'question', "
            f"'options' (list) and 'answer' (the correct option letter). "
            f"Return as plain text, numbered."
        )
        text = self._call_model(prompt)
        # naive parser: return raw text as single item if parsing fails
        # you can improve this later with structured output or JSON instruction.
        return [{"raw_text": text}]

    def make_flashcards(self, topic: str, num_cards: int = 6) -> List[Dict]:
        prompt = (
            f"Make {num_cards} simple flashcards for: {topic}. "
            f"Format as Q: ... \\n A: ... (one per line)."
        )
        text = self._call_model(prompt)
        return [{"raw_text": text}]

    def plan_study(self, topic: str, days: int = 7) -> str:
        prompt = (
            f"Create a {days}-day study plan for learning {topic}. "
            f"Each day 30-45 minutes, list goals and short activities."
        )
        return self._call_model(prompt)
