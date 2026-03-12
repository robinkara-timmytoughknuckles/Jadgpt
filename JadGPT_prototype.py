import random

rules = [ 
    #Greeting
    (["wsp","howdy","wassup","hello","hi","hey","whatsup","sup","greetings"],
     ["Hello, what's on your mind?",
      "What's up? How are you?",
      "Hi, what do you want to talk about?"]),
    #How are u
    (["how are you","how are you doing","how's it going","you good"],
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