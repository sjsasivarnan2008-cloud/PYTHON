"""
CSA08 CO5 - Task B5: Rule-Based Air Quality Query Assistant Chatbot
Parses user queries and interfaces with database to return telemetry summaries.
"""

def mock_station_lookup(station: str):
    data = {
        "Adyar": (51.1, "Satisfactory"),
        "Guindy": (108.6, "Poor / Unhealthy"),
        "Velachery": (42.4, "Good"),
        "T Nagar": (76.5, "Moderate")
    }
    return data.get(station)

def chatbot_respond(query: str) -> str:
    q = query.lower()
    stations = ["adyar", "guindy", "velachery", "t nagar"]
    matched_st = None
    for s in stations:
        if s in q:
            matched_st = s.title()
            break

    if any(k in q for k in ["pm2.5", "pm25", "air", "pollution"]):
        if matched_st:
            res = mock_station_lookup(matched_st)
            if res:
                return f"Current PM2.5 in {matched_st} is {res[0]} µg/m³ ({res[1]})."
            return f"No live telemetry available for {matched_st}."
        return "Please specify a monitoring station (e.g., Adyar, Guindy, Velachery, T Nagar)."
    elif "hello" in q or "hi" in q:
        return "Hello! I am the City Air Quality Bot. Ask me about PM2.5 levels at any station."
    return "I assist with city environmental telemetry and station air quality inquiries."

def main():
    print("=" * 68)
    print("  CSA08 CO5 TASK B5: AIR QUALITY QUERY ASSISTANT CHATBOT")
    print("=" * 68)

    sample_dialogue = [
        "Hi bot!",
        "What is the PM2.5 in Adyar today?",
        "Tell me about air pollution in Guindy",
        "How is the traffic near the station?"
    ]

    for user_input in sample_dialogue:
        reply = chatbot_respond(user_input)
        print(f"  User : {user_input}")
        print(f"  Bot  : {reply}")
        print("  " + "─" * 60)

    print("=" * 68)

if __name__ == "__main__":
    main()
