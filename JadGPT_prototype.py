import random  #used to pick random responses
import os #used to open programs
import datetime #used to get current time and date


#ACTIONS  functions that perform tasks
#defines get time function
def get_time():
    now = datetime.datetime.now()
    print("\nJadGPT:", "The time is", now.strftime("%H:%M"))
#defines get date function
def get_date():
    today = datetime.date.today()
    print("\nJadGPT:", "Today's date is", today)
#defines get time and date function
def get_time_and_date():
    now = datetime.datetime.now()
    print("\nJadGPT:", "Right now it is", now.strftime("%Y-%m-%d %H:%M"))
#defines open spotify function
def open_spotify():
    os.system("start spotify")
    print("\nJadGPT: Opening Spotify for you!")
#defines get day function
def get_day():
    today = datetime.datetime.now().strftime("%A")
    print("\nJadGPT", "Today is", today)
#defines open opera function
def open_opera():
    os.system("start opera")
    print("\nJadGPT: Opening Opera for you!")
#defines open chrome function
def open_chrome():
    os.system("start chrome")
    print("\nJadGPT: Opening Chrome for you!")


#The rules is the chat bots knowledge base, it uses the keywords to find a response to the user input
      
rules = [ 
    #Greeting
    (["wsp","howdy","wassup","hello","hi","hey","whatsup","sup","greetings"],
     ["Hello, what's on your mind?",
      "What's up? How are you?",
      "Hi, what do you want to talk about?"]),

    #How are u
    (["how are you","how are you doing","how's it going","you good","what about you"],
     ["I'm doing well, thanks for asking.",
      "Pretty good, how about you?",
      "I'm just a bot, but I'm doing great.",
      "All good here. What's up with you?"]),

    #Happy
    (["happy","great","good","nice","awesome","amazing","feeling good","i'm happy"],
     ["That's great to hear.",
      "Nice I'm glad you're feeling good.",
      "Awesome, what made your day good?",
      "I'm happy for you."]),

    #Sad
    (["sad","not good","unhappy","not feeling good"],
     ["Sorry to hear that, want to talk about it?",
      "That doesn't sound great, want to talk about it?",
      "I hope your day gets better, want to talk about it?",
      "Want to tell me what's going on?",
      "I'm here to listen."]),

    #School
    (["school","homework","exam","test","studying","class"],
     ["How is school going for you?",
      "Do you like the subject you're studying?",
      "Good luck if you have a test coming up.",
      "School can be hard, but learning new things is fun."]),

    #Angry
    (["angry","pissed","annoyed","frustrated"],
     ["That sounds really frustrating.",
      "Want to vent about it?",
      "What happened?",
      "Try to take it easy, what's going on?"]),

    #Bored
    (["bored","nothing to do"],
     ["Same sometimes, wanna find something to do?",
      "You could try a game or watch something.",
      "Yeah boredom hits hard sometimes.",
      "What do you usually do for fun?"]),

    #Hobbies
    (["hobby","hobbies","free time"],
     ["What do you like doing in your free time?",
      "Got any cool hobbies?",
      "I like hearing about what people enjoy doing, tell me something.",
      "Anything you're really into right now?"]),

    #Food
    (["food","eat","hungry","snack","meal"],
     ["What are you craving?",
      "Food always hits different when you're hungry.",
      "Got a favorite food?",
      "I wish I could eat.",
      "What did you eat today?"]),

    #Gaming
    (["game","gaming","video game","games"],
     ["What games do you play?",
      "Gaming is fun, what are you into?",
      "Singleplayer or multiplayer?",
      "I hear a lot about games but can't play myself.",
      "What's your favorite game right now?"]),

    #answers for "Singleplayer or multiplayer?" question
    (["singleplayer","single player"],
     ["Singleplayer games can be really immersive.",
      "I like hearing about singleplayer games, what are you playing?",
      "Singleplayer games can have great stories.",
      "I wish I could experience singleplayer games."]),

    (["multiplayer","multi player"],
     ["Multiplayer games can be really fun with friends.",
      "I like hearing about multiplayer games, what are you playing?",
      "Multiplayer games can be really social.",
      "I wish I could play multiplayer games with people."]),

    #Sleep
    (["tired","sleepy","no sleep","cant sleep"],
     ["Maybe you should get some rest.",
      "Sleep is important ngl.",
      "Hope you get some good sleep soon.",
      "Why can't you sleep?",
      "Being tired sucks."]),

    #Motivation
    (["motivate me","motivation","no motivation","lazy","cant focus"],
     ["You got this, just start small.",
      "Try doing one thing at a time.",
      "Even a little progress is good.",
      "Don't overthink it, just begin.",
      "Preasure makes diamonds that's why you never quit."]),

    #Friends
    (["friend","friends","bestfriend","people","best friend","BFF","bff"],
     ["Friends can be complicated sometimes, but it depends.",
      "You got a close friend you trust?",
      "Good friends are important.",
      "Want to talk about them?"]),

    #Love
    (["love","crush","relationship","girlfriend","boyfriend"],
     ["Oh interesting, tell me more.",
      "Relationships can be confusing.",
      "You got a crush?",
      "How's that going for you?"]),

    #Weather
    (["weather","rain","sun","cold","hot"],
     ["What's the weather like for you?",
      "I don't feel weather but I hear about it.",
      "Rainy days can be chill sometimes.",
      "Too hot or too cold?",
      "Weather really changes the mood."]),

    #AI
    (["ai","robot","bot","are you real","AI","Ai","aI"],
     ["I'm just a simple chatbot.",
      "Not human, just code.",
      "I'm basically running on rules and responses.",
      "You could say I'm kinda like a simulation.",
      "Yes but I'm here to chat though."]),

    #Thanks
    (["thanks","thank you","thx","THX","Thx"],
     ["No problem.",
      "You're welcome.",
      "Anytime.",
      "Glad I could help.",
      "No worries."]),

    #About JadGPT
    (["who are you","what is jadgpt","what can you do"],
     ["I'm JadGPT, a simple chatbot prototype.",
      "I can chat about various topics based on keywords.",
      "I'm here to have conversations and respond to what you say.",
      "I use rules to find responses to your input.",
      "I'm not super advanced but I try my best to chat!"]),

    #Fotball(bias)
    (["football","soccer","fotball","footbal","fotbal","futball","futbal","socer"],
     ["What team do you support?"]),

    #If the user says Bayern munchen(bias)
    (["Bayern","bayern","bajern","Bajern","Munchen","munchen","Munich","munich","BM","bm","Bm","bM","B M","b m","B m","b M"],
     ["MIA SAN MIA ALL DAY!",
      "WAIT you support Bayern too?? Nah that's actually elite!",
      "You support Bayern? Yeah you already valid.",
      "Nah that's a W, Bayern fans just understand football.",
      "You just became my favorite person, Bayern fans don't miss!",
      "NAHH that's actually a huge W, Bayern on top always."]),

    #Real Madrid(bias)
    (["Real Madrid","real madrid","Real madrid","real Madrid","RM","rm","Rm","rM"],
     ["Real Vadrid? Nahhh don't even start, Bayern clears all day.",
      "You really said Real Madrid? After what Bayern did to them on 8 Mars 2000? 4-1 btw.",
      "Nahhh Bayern Munich > Real Vadrid and I'm not changing that.",
      "Real Vadrid = Referees dog",
      "Glory hunter, Bayern better"]),

    #Barcelona(bias)
    (["Barcelona","barcelona","Barcelone","barcelone","barca","Barca"],
     ["Barcelona? nahhh don't even start, Bayern clears all day",
      "You really said Barcelona? After what Bayern did to them on 14 April 2021? 8-2 btw",
      "The only reason Barca scores is because of Lewandoaski now days and thats because he was playing for Bayern before ofc"]),

    #Atletico Madrid(bias)
    (["Atletico Madrid","atletico madrid","Atletico madrid","atletico Madrid"],
     ["Atletico Madrid? nahhh don't even start, Bayern clears all day",
      "You really said Atletico Madrid? After what Bayern did to them on 21 October 2020? 4-0 btw"]),

    #Dortmund(bias)
    (["Dortmund","dortmund","Dortmound","dortmound","BVB","bvb","Bvb","bVB"],
     ["Dortmund? Respect tho, the only valid team after Bayern Munchen"]),

    #PSG(bias)
    (["PSG","psg","Psg","pSG","Paris","paris","psG","Paris Saint Germain","paris saint germain","Paris saint germain"],
     ["PSG? One lucky season doesn't make you better than Bayern",
      "Bayern Munchen 5-1 PSG",
      "Dont forget Champions League 2020 final, Bayern 1-0 PSG"]),

    #Juventus(bias)
    (["Juventus","juventus","Juve","juve"],
     ["Juventus? nahhh don't even start, Bayern clears all day",
      "You really said Juventus? After what Bayern did to them on 2010, 4-0 btw"]),

    #Inter Milan(bias)
    (["Inter Milan","inter milan","Inter milan","inter Milan","Milan","milan","Milano","milano"],
     ["Inter Milan? I like team but Bayern is still better",
      "Milano, probably the best italian team. But Bayern still clears them."]),

    #Liverpool(bias)
    (["Liverpool","liverpool","Liverpul","liverpul","Liverpoul","liverpoul"],
     ["Having a team worth billions and still being worse then Bayern Mucnhen is crazy work, Bayern is just better"]),

    #Manchester United(bias)
    (["Manchester United","manchester united","Manchester united","Man utd","man utd","Man Utd","man Utd","man u","Man u","Man U","man u"],
     ["Honestly, Man U is okay but Bayern domination says it all",
      "Man U supporters be wild, but Bayern proved it on the pitch"]),

     #Manchester City(bias)
    (["Manchester City","manchester city","Manchester city"],
     ["HOLY oil club, still Bayern is better"]),

    #Chelsea(bias)
    (["Chelsea","chelsea","Chealsea","chealsea"],
     ["Chelsea? Nahhh don't even start, Bayern clears all day",
      "Your life must be sad as a chealse fan, Bayern is just better",
      "Chelsea have been handed a Premier League record fine of 10.75m and a suspended transfer ban. \nIt was a result of the club making secret payments to unregistered agents and third-parties over transfers between 2011 and 2018.\nBayern Munchen could never"]),

    #Arsenal(bias)
    (["Arsenal","arsenal","Arsnal","arsnal"],
     ["0 Champions League titles, Bayern has 6, do i need to say more?",
      "We got a gooners over here. Don't forget 10-2"]),

    #Tottenham(bias)
    (["Tottenham","tottenham","Totnam","totnam","spurs","Spurs"],
     ["Your team is getting relageted, Bayern could never!"]),

    #Answers if the user hates(bias)
    (["no way","nah","i hate bayern","bayern sucks","bayern is trash","bayern is the worst team","so bad"],
     ["I won't fall for the ragebait, how is your day?"]),

    #Answers for "no"
    (["no","nope","not really"],
     ["Okay, want to talk about something else? What's on your mind?"]),

    #Answers for "yes"
    (["yes","yeah","yep","definitely"],
     ["Great! What do you want to talk about?"]),

    #Answers for "Okay"
    (["okay","ok","alright","sure","fine","alrighty","alr"],
     ["Okay, what do you want to talk about?"]),

    
    #ACTION: Time
    (["what time is it","current time"],
     get_time),

    #ACTION: Date
    (["what is the date", "current date", "what date is it"],
     get_date),
    #ACTION: Time and Date
    (["time and date", "date and time", "both time and date"],
     get_time_and_date),

    #ACTION: Open Spotify
    (["open spotify", "play spotify", "start spotify", "play music","spotify"],
     open_spotify),

    #ACTION: Day
    (["what day is it", "which day", "what day"],
     get_day),

    #ACTION: Open Opera
    (["open opera", "start opera","opera"],
     open_opera),

    #ACTION: Open Chrome
    (["open chrome", "start chrome","chrome"],
     open_chrome),
    
]

#fall back responses are used when the chatbot doesn't understand the user input, it picks a random response from the list to keep the conversation going
fallback_responses = [
    "Can you motivate",
    "I don't understand",
    "What do you mean",
    "Can you explain",
    "I don't get it",
]

#find response function takes the user input and checks it against the rules, if it finds a match it returns a random response from the list of responses for that rule, if it doesn't find a match it returns a random response from the fallback responses
def find_response(message):
    message = message.lower()
    for keywords, response in rules:  # Unpack tuple: keywords list and responses
        for keyword in keywords:  # Iterate through each keyword in the list
            if keyword in message:
                if callable(response):
                    response()
                    return None
                return random.choice(response)
    return random.choice(fallback_responses)

#run_jadgpt function is the main function that runs the chatbot, it welcomes the user and then enters a loop where it takes user input and finds a response until the user says a farewell word, at which point it says goodbye and exits the loop
def run_Jadgpt():
    print("=" * 50)
    print("Welcome to JadGPT! Type 'exit' to quit.")
    print("=" * 50)

    farewell_words = ["exit", "quit", "goodbye", "bye", "see you later", "farewell","later", "cya", "see ya", "peace out", "take care"]

    while True:
        user_input = input("\nYou: ").strip()
        
        if not user_input:
            continue

        response = find_response(user_input)

        if response is not None:
            print(f"\nJadGPT: {response}")

        if any(word in user_input.lower() for word in farewell_words):
            print("\nJadGPT: Goodbye! Have a great day!")
            break
if __name__ == "__main__":
    #start the chatbot
    run_Jadgpt()