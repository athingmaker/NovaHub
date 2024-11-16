import random as rand

jokes = [
    "Why did the chicken cross the road? To get to the other side.",
    "Why don't scientists trust atoms? Because they make up everything.",
    "Why did the scarecrow win an award? Because he was outstanding in his field.",
    "Why did the bicycle fall over? Because it was two-tired.",
    "Why did the coffee file a police report? It got mugged.",
    "Why did the hipster burn his tongue? He drank his coffee before it was cool.",
    "Why did the tomato turn red? Because it saw the salad dressing.",
    "Why did the chicken go to the seance? To talk to the other side.",
    "Why don't skeletons fight each other? They don't have the guts.",
    "Why did the table go to therapy? It had trouble standing on its own four legs.",
    "Why did the computer go to the doctor? It had a virus.",
    "Why did the ditch get into trouble? Because it was always digging.",
    "Why did the bicycle fall in love? Because it was two-tired of being single.",
    "Why did the scarecrow win an academy award? Because he was outstanding in his field.",
    "Why did the hipster buy a map? He wanted to know where all the vintage stores were.",
    "Why did the tomato turn blue? Because it was in a jazz band.",
    "Why did the chicken join a band? Because it had the drumsticks.",
    "Why don't skeletons fight each other? They don't have the guts.",
    "Why did the table go to art school? It wanted to draw attention to itself.",
    "Why did the computer go to therapy? It had a memory leak.",
    "Why did the ditch get a promotion? Because it was always digging deeper.",
    "Why did the bicycle join the circus? Because it was a wheelie good performer.",
    "Why did the scarecrow win the lottery? Because he was always betting on the fields.",
    "Why did the hipster get a pet rock? Because it was authentic and unique.",
    "Why did the tomato turn green? Because it saw the salad dressing.",
    "Why did the chicken get a scholarship? Because it was eggs-traordinary.",
    "Why don't skeletons fight each other? They don't have the guts.",
    "Why did the table go to the gym? It wanted to work on its six-pack.",
    "Why did the computer go to jail? It was caught hacking.",
    "Why did the ditch get a ticket? Because it was caught digging without a permit.",
    "Why did the bicycle join the army? Because it wanted to serve its country.",
    "Why did the scarecrow win an Oscar? Because it was outstanding in its field.",
    "Why did the hipster get a new phone? Because it was vintage and no one else had it.",
    "Why did the tomato turn purple? Because it was in a grape mood.",
    "Why did the chicken get a job? Because it wanted to egg-spress itself.",
    "Why don't skeletons fight each other? They don't have the guts.",
    "Why did the table go to a museum? It wanted to see some bone structure.",
    "Why did the computer go to a party? It wanted to socialize with other devices.",
    "Why did the ditch get a medal? Because it dug deep when it was needed.",
    "Why did the bicycle join a cult? Because it was looking for a wheely good time.",
    "Why did the scarecrow win a Nobel Prize? Because it was outstanding in its field.",
    "Why did the hipster get a tattoo? Because it was a statement piece.",
    "Why did the tomato turn yellow? Because it saw the salad dressing.",
    "Why did the scarecrow win a Nobel Prize? Because it was outstanding in its field.",
    "Why did the hipster get a tattoo? Because it was a statement piece.",
    "Why did the tomato turn yellow? Because it saw the salad dressing.",
    "Why did the chicken get a degree? Because it wanted to be eggs-traordinary.",
    "Why don't skeletons fight each other? They don't have the guts.",
    "Why did the table go to a spa? It needed a good woodworking.",
    "Why did the computer go to a therapist? It had a hard drive.",
    "Why did the ditch get a job? Because it was good at digging.",
    "Why did the bicycle join a book club? It wanted to read between the wheels.",
    "Why did the scarecrow win a Pulitzer Prize? Because it was outstanding in its field.",
    "Why did the hipster get a plant? Because it was into organic living.",
    "Why did the tomato turn orange? Because it was in a pumpkin patch.",
    "Why did the chicken get a job as a chef? Because it knew how to crack under pressure.",
    "Why don't skeletons fight each other? They don't have the guts.",
    "Why did the table go to a bar? It heard there were a lot of happy hours.",
    "Why did the computer go to a concert? It wanted to hear some byte music.",
    "Why did the ditch get a promotion? Because it always dug deep.",
    "Why did the bicycle join a gym? Because it wanted to pump up its tires.",
    "Why did the scarecrow win a Grammy? Because it was outstanding in its field.",
    "Why did the hipster get a record player? Because it was into vinyl.",
    "Why did the tomato turn pink? Because it saw the salad dressing.",
    "Why did the chicken get a job as a baker? Because it knew how to rise to the occasion.",
    "Why don't skeletons fight each other? They don't have the guts."
]

def get_weather(city):
    weather_data = {
        "New York": "15°C, Clear sky, Humidity: 60%",
        "London": "10°C, Light rain, Humidity: 80%",
        "Paris": "18°C, Cloudy, Humidity: 70%"
    }
    return weather_data.get(city, "Weather data unavailable")

while True:
    userresponse = input("You: ").lower()
    
    if "what is the " in userresponse:
        if "weather" in userresponse:
            print("Bot: I am unable to find the weather because I am too stupid and lazy. Please try again later.")
        if "time" in userresponse:
            print("Bot: I am unable to find the time because I am too lazy.")
    
    if "tell me " in userresponse:
        if "a joke" in userresponse:
            print(f"Bot: {jokes[rand.randint(0, len(jokes)-1)]}")
        
        if "the weather" in userresponse:
            city = "New York"  # You can change this if needed
            weather = get_weather(city)
            print(f"Bot: The current weather in {city} is: {weather}")
        
        if "the time" in userresponse:
            print("Bot: I am unable to find the time because I am too lazy.")
        
        if any(phrase in userresponse for phrase in ["your name", "yourname", "you're name", "ur name", "u name", "yur name"]):
            print("Bot: My name is NovaAI V0.1.")