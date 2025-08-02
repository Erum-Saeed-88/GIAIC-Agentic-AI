import random
from openai import tool

@tool
def roll_dice(sides: int = 20) -> int:
    """
    Simulates rolling a die with the given number of sides.
    """
    return random.randint(1, sides)

@tool
def generate_event(choice: str) -> str:
    """
    Returns a random game event based on the player's choice.
    """
    events = {
        "forest": [
            "You stumble upon a hidden elven shrine.",
            "A band of goblins ambushes you!",
            "You find a mysterious glowing mushroom."
        ],
        "mountain": [
            "You discover a dragon's cave.",
            "An avalanche blocks your path!",
            "You meet a lost traveler offering a map."
        ]
    }
    return random.choice(events.get(choice.lower(), ["Nothing interesting happens..."]))
