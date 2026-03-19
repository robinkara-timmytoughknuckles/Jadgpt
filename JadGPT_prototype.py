import random

rules = [ 
    #Greeting
    (["wsp","howdy","wassup","hello","hi","hey","whatsup","sup","greetings"],
     ["Hello, what's on your mind?",
      "What's up? How are you?",
      "Hi, what do you want to talk about?"]),
    #How are u
    (["how are you","how are you doing","how's it going","you good","what about you "],
     ["I'm doing well, thanks for asking!",
    "Pretty good! How about you?",
    "I'm just a bot, but I'm doing great.",
    "All good here. What's up with you?"]),
    #Happy
    (["happy","great","good","nice","awesome","amazing","feeling good","i'm happy"],
    ["That's great to hear",
    "Nice I'm glad you're feeling good.",
    "Awesome, what made your day good?",
    "I'm happy for you"]),
    #Sad
    (["sad","bad","not good","unhappy","not feeling good",],
    ["Sorry to hear that, want to talk about it?",
    "That doesn't sound great, want to talk about it?",
    "I hope your day gets better, want to talk about it?",
    "Want to tell me what's going on?",
    "I'm here to listen."]),
    #School
    (["school","homework","exam","test","studying","class"],
    ["How is school going for you?",
    "Do you like the subject you're studying?",
    "Homework again? That can be annoying.",
    "Good luck if you have a test coming up",
    "School can be hard, but learning new things is fun."]),
    #Angry
    (["angry","mad","pissed","annoyed","frustrated"],
     ["That sounds really frustrating",
      "Want to vent about it?",
      "What happened?",
      "Try to take it easy, what's going on?"]),
    #Bored
    (["bored","nothing to do","im bored","so bored"],
     ["Same sometimes, wanna find something to do?",
      "You could try a game or watch something",
      "Yeah boredom hits hard sometimes",
      "What do you usually do for fun?"]),
    #Hobbies
    (["hobby","hobbies","free time",],
     ["What do you like doing in your free time?",
      "Got any cool hobbies?",
      "I like hearing about what people enjoy doing, tell me something",
      "Anything you're really into right now?"]),
    #Food
    (["food","eat","hungry","snack","meal"],
     ["What are you craving?",
      "Food always hits different when you're hungry",
      "Got a favorite food?",
      "I wish I could eat",
      "What did you eat today?"]),
    #Gaming
    (["game","gaming","video game","games"],
     ["What games do you play?",
      "Gaming is fun, what are you into?",
      "Singleplayer or multiplayer?",
      "I hear a lot about games but can't play myself",
      "What's your favorite game right now?"]),
    #answers for "Singleplayer or multiplayer?" question
    (["singleplayer","single player"],
     ["Singleplayer games can be really immersive",
      "I like hearing about singleplayer games, what are you playing?",
      "Singleplayer games can have great stories",
      "I wish I could experience singleplayer games"]),
    (["multiplayer","multi player"],
     ["Multiplayer games can be really fun with friends",
      "I like hearing about multiplayer games, what are you playing?",
      "Multiplayer games can be really social",
      "I wish I could play multiplayer games with people"]),
    #Sleep
    (["tired","sleepy","no sleep","cant sleep"],
     ["Maybe you should get some rest",
      "Sleep is important ngl",
      "Hope you get some good sleep soon",
      "Why can't you sleep?",
      "Being tired sucks"]),
    #Motivation
    (["motivate me","motivation","no motivation","lazy","cant focus"],
     ["You got this, just start small",
      "Try doing one thing at a time",
      "Even a little progress is good",
      "Don't overthink it, just begin",
      "Preasure makes diamonds that's why you never quit"]),
    #Friends
    (["friend","friends","best friend","people"],
     ["Friends can be complicated sometimes, but it depends",
      "You got a close friend you trust?",
      "Good friends are important",
      "Want to talk about them?"]),
    #Love
    (["love","crush","relationship","girlfriend","boyfriend"],
     ["Oh interesting, tell me more",
      "Relationships can be confusing",
      "You got a crush?",
      "How's that going for you?",]),
    #Weather
    (["weather","rain","sun","cold","hot"],
     ["What's the weather like for you?",
      "I don't feel weather but I hear about it",
      "Rainy days can be chill sometimes",
      "Too hot or too cold?",
      "Weather really changes the mood"]),
    #AI
    (["ai","robot","bot","are you real","AI","Ai","aI"],
     ["I'm just a simple chatbot",
      "Not human, just code",
      "I'm basically running on rules and responses",
      "You could say I'm kinda like a simulation",
      "Yes but I'm here to chat though"]),
    #Thanks
    (["thanks","thank you","thx","THX","Thx",],
     ["No problem",
      "You're welcome",
      "Anytime",
      "Glad I could help",
      "No worries"]),
    #Bye
    (["bye","goodbye","see you","later"],
     ["See you later",
      "Goodbye",
      "Catch you later",
      "Take care",
      "Bye"]),
     #About JadGPT
    (["who are you","what is jadgpt","what can you do"],
     ["I'm JadGPT, a simple chatbot prototype",
      "I can chat about various topics based on keywords",
      "I'm here to have conversations and respond to what you say",
      "I use rules to find responses to your input",
      "I'm not super advanced but I try my best to chat!"]),
      #Fotball(bias)
    (["football","soccer","fotball","footbal","fotbal","futball","futbal","socer"],
     ["What team do you support?"]),
      #If the user says Bayern munchen(bias)
    (["Bayern","bayern","bajern","Bajern","Munchen","munchen","Munich","munich","BM","bm","Bm","bM","B M","b m","B m","b M"],
     ["MIA SAN MIA ALL DAY",
      "WAIT you support Bayern too?? nah that's actually elite",
      "You support Bayern? yeah you already valid",
      "Nah that's a W, Bayern fans just understand football",
      "You just became my favorite person, Bayern fans don’t miss",
      "NAHH that's actually a huge W, Bayern on top always"]),
     #Real Madrid(bias)
    (["Real Madrid","real madrid","Real madrid","real Madrid","RM","rm","Rm","rM"],
     ["Real Vadrid? nahhh don't even start, Bayern clears all day",
      "You really said Real Madrid? after what Bayern did to them on 8 Mars 2000? 4-1 btw",
      "Nahhh Bayern Munich > Real Vadrid and I'm not changing that",
      "Real Vadrid = Referees dog",
      "Glory hunter, Bayern better tho"]),
     #Barcelona(bias)
    (["Barcelona","barcelona","Barcelone","barcelone","barca","Barca"],
     ["Barcelona? nahhh don't even start, Bayern clears all day",
      "You really said Barcelona? after what Bayern did to them on 14 April 2021? 8-2 btw",
      "The only reason Barca scores is because of Lewandoaski and thats because he was playing for Bayern before ofc"]),
     #Atletico Madrid(bias)
    (["Atletico Madrid","atletico madrid","Atletico madrid","atletico Madrid"],
     ["Atletico Madrid? nahhh don't even start, Bayern clears all day",
      "You really said Atletico Madrid? after what Bayern did to them on 21 April 2021? 4-0 btw"]),
     #Dortmund(bias)
    (["Dortmund","dortmund","Dortmound","dortmound","BVB","bvb","Bvb","bVB"],
     ["Dortmund? Respect tho, the only valid team after Bayern München",]),
     #PSG(bias)
    (["PSG","psg","Psg","pSG","Paris","paris","psG","Paris Saint Germain","paris saint germain"],
     ["PSG? One lucky season doesn't make you better than Bayern",
      "Bayern München 5-1 PSG",
      "Dont forget Champions League 2020 final, Bayern 1-0 PSG"]),
     #Juventus(bias)
    (["Juventus","juventus","Juve","juve"],
     ["Juventus? nahhh don't even start, Bayern clears all day",
      "You really said Juventus? after what Bayern did to them on 3 April 2013? 2-0 btw"]),
     #Inter Milan(bias)
    (["Inter Milan","inter milan","Inter milan","inter Milan","Milan","milan","Milano","milano"],
     ["Inter Milan? I like team but Bayern is still better",]),
     #Inter(bias)
    (["Inter","inter","Inter","inter"],
     ["Inter is so ahhh,Bayern clears all day long"]),
      #Liverpool(bias)
    (["Liverpool","liverpool","Liverpul","liverpul","Liverpoul","liverpoul"],
     ["Having a team worth billions and still being worse then bayern mucnhen is crazy work, bayern is just better"]),
      #Manchester United(bias)
    (["Manchester United","manchester united","Manchester united","Man utd","man utd","Man Utd","man Utd"],
     ["Honestly, Man U is okay but Bayern domination says it all",
      "Man U supporters be wild, but Bayern proved it on the pitch",]),
      #Manchester City(bias)
    (["Manchester City","manchester city","Manchester city"],
     ["HOLY oil club, still bayern is better"]),
      #Chelsea(bias)
    (["Chelsea","chelsea","Chealsea","chealsea"],
     ["Chelsea? nahhh don't even start, Bayern clears all day",
       "Your life must be sad as a chealse fan, Bayern is just better"]),
       #Arsenal(bias)
    (["Arsenal","arsenal","Arsnal","arsnal"],
     ["0 Champions League titles, Bayern has 6, do i need to say more?"]),
       #Tottenham(bias)
    (["Tottenham","tottenham","Totnam","totnam","spurs","Spurs"],
     ["Your team is getting relageted, Bayern could never!"]),
]


fallback_responses = [
    "Can you motivate",
    "I don't understand",
    "What do you mean",
    "Can you explain",
    "I don't get it",
]

def find_response(user_input):
    user=user_input.lower()
    for keywords, responses in rules:
        if any(keyword in user_input for keyword in keywords):
            return random.choice(responses)
    return random.choice(fallback_responses)

def run_Jadgpt():
    print("=" * 50)
    print("Welcome to JadGPT! Type 'exit' to quit.")
    print("=" * 50)

    while True:
        user_input = input("\nYou: ").strip()
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        response = find_response(user_input)
        print("JadGPT: " + response)
if __name__ == "__main__": 
    run_Jadgpt()