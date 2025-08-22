# agent/runner.py
import argparse
import textwrap
from agent.smart_agent import SmartStudentAgent

class Runner:
    """
    Runner provides a simple CLI for the SmartStudentAgent.
    """

    def __init__(self):
        self.agent = SmartStudentAgent()

    def run(self):
        parser = argparse.ArgumentParser(
            description="Smart Student Assistant - CLI",
            formatter_class=argparse.RawTextHelpFormatter
        )
        parser.add_argument("--mode", choices=["qa","quiz","flash","plan"], required=True,
                            help=textwrap.dedent("""\
                                qa    : ask a question
                                quiz  : generate quiz
                                flash : generate flashcards
                                plan  : create a study plan
                            """))
        parser.add_argument("--topic", type=str, help="Topic or question text")
        parser.add_argument("--n", type=int, default=5, help="number of items (for quiz/flash)")

        args = parser.parse_args()

        if not args.topic:
            print("Error: --topic required for selected mode.")
            return

        if args.mode == "qa":
            print("Question:", args.topic)
            out = self.agent.answer_question(args.topic)
            print("\nAnswer:\n", out)
        elif args.mode == "quiz":
            res = self.agent.make_quiz(args.topic, args.n)
            print("\nQuiz result (raw):\n", res[0]["raw_text"])
        elif args.mode == "flash":
            res = self.agent.make_flashcards(args.topic, args.n)
            print("\nFlashcards (raw):\n", res[0]["raw_text"])
        elif args.mode == "plan":
            out = self.agent.plan_study(args.topic, args.n)
            print("\nStudy Plan:\n", out)

if __name__ == "__main__":
    Runner().run()
