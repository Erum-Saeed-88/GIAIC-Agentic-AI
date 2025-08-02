from openai import tool

@tool
def get_flights(destination: str) -> str:
    """
    Returns mock flight info to a destination.
    """
    return f"Flight booked to {destination}: PKR 70,000 - Economy class - Direct flight"

@tool
def suggest_hotels(destination: str) -> str:
    """
    Returns mock hotel suggestions for a destination.
    """
    hotels = {
        "bali": ["Ocean View Resort", "Bali Bliss Villas", "Sunset Paradise"],
        "tokyo": ["Shinjuku Inn", "Tokyo Capsule Stay", "Asakusa Hotel"],
        "paris": ["Eiffel View Hotel", "Parisian Luxe", "Montmartre Stay"]
    }
    return "\n- " + "\n- ".join(hotels.get(destination.lower(), ["No hotels found"]))
