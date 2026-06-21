import random
import time
from datetime import datetime

BOT_NAME = "FriendlyAI"

greetings = [
    "Hello! It's so wonderful to see you.",
    "Hey there! What can I help you with today?",
    "Hi! I hope your day is going fantastic so far."
]

jokes = [
    "Why do programmers prefer dark mode? Because light attracts bugs!",
    "Why was the computer cold? It left its Windows open.",
    "Why did Python go to school? To improve its class!"
]

motivational_quotes = [
    "Believe you can and you're halfway there. ✨",
    "The only way to do great work is to love what you do. 🚀",
    "Don't count the days, make the days count!",
    "Progress over perfection. You've got this! 💪"
]


def chatbot():
    sentiment_score = 0
    message_count = 0
    chat_log = []
    
    print("=" * 50)
    print(f"🤖 {BOT_NAME}: Welcome! Type 'help' at any time to see my features.")
    print("=" * 50)
    
    user_name = input(f"\n🤖 {BOT_NAME}: Before we start, what's your name?\nYou: ").strip()
    if not user_name:
        user_name = "Friend"
        
    print(f"🤖 {BOT_NAME}: Nice to meet you, {user_name}!")
    print("-" * 50)
    
    while True:
       
        user_input = input(f"\n{user_name}: ").strip()
        user_clean = user_input.lower()
        
        if not user_input:
            continue
            
        message_count += 1
        chat_log.append(f"{user_name}: {user_input}")
        
        bot_reply = ""
        
        if user_clean in ["exit", "quit", "bye", "goodbye"]:
            bot_reply = f"Goodbye, {user_name}! Have a wonderful day."
            print(f"🤖 {BOT_NAME}: {bot_reply}")
            chat_log.append(f"{BOT_NAME}: {bot_reply}")
            break
            
        elif any(word in user_clean for word in ["hello", "hi", "hey"]):
            bot_reply = random.choice(greetings)
            
        elif "how are you" in user_clean or "how are u" in user_clean or "whats up" in user_clean or "what's up" in user_clean:
            bot_reply = f"I'm doing great, {user_name}! Thanks for checking in. How are you?"
            
        elif "what is my name" in user_clean:
            bot_reply = f"Your name is {user_name}! I have a great memory."
            
        elif "your name" in user_clean or "who are you" in user_clean:
            bot_reply = f"My name is {BOT_NAME}. I am a friendly, rule-based chatbot built using Python!"
            
        elif "i am happy" in user_clean or "i'm happy" in user_clean:
            sentiment_score += 1
            bot_reply = "That makes me so happy to hear! Keep that awesome energy going!"
            
        elif "i am sad" in user_clean or "i'm sad" in user_clean:
            sentiment_score -= 1
            bot_reply = "I'm really sorry you're feeling down. Lean on me! You can ask me for a 'joke' or to 'motivate me'."
            
        elif "mood report" in user_clean:
            if sentiment_score > 0:
                vibe = "Positive 🎉"
            elif sentiment_score < 0:
                vibe = "Negative 🩹"
            else:
                vibe = "Neutral ⚖️"
            bot_reply = f"Here is your Mood Report -> Vibe: {vibe} (Current Score: {sentiment_score})"
            
        elif "time" in user_clean:
            bot_reply = datetime.now().strftime("The current time is %I:%M %p")
            
        elif "date" in user_clean:
            bot_reply = datetime.now().strftime("Today's date is %d-%m-%Y")
            
        elif "messages" in user_clean:
            bot_reply = f"We have exchanged {message_count} messages so far in this conversation!"
            
        elif user_clean.startswith("calculate "):
            expression = user_input[10:].strip()

            clean_math = expression.replace(" ", "")
            allowed_chars = set("0123456789+-*/().")
            
            if set(clean_math).issubset(allowed_chars):
                try:
                    result = eval(clean_math, {"__builtins__": None}, {})
                    bot_reply = f"Answer: {result}"
                except:
                    bot_reply = "Oops, that expression looks a bit broken. Check your numbers!"
            else:
                bot_reply = "I can only calculate basic math expressions (numbers, +, -, *, /)."
                
    
        elif "joke" in user_clean:
            bot_reply = random.choice(jokes)
            
        elif "motivate me" in user_clean or "motivation" in user_clean:
            bot_reply = random.choice(motivational_quotes)
            
    
        elif "what is ai" in user_clean:
            bot_reply = "AI stands for Artificial Intelligence! It's when computers are programmed to think, learn, and solve problems like humans."
            
        elif "what is python" in user_clean:
            bot_reply = "Python is a powerful, beginner-friendly programming language. It's exactly what I am written in!"
            
        elif "who created you" in user_clean:
            bot_reply = "I was created by Rakshit Passi as an AI internship project using Python and rule-based logic."
            
    
        elif "help" in user_clean:
            bot_reply = (
                "\n✨ Here is what I can do! Just type any of these options:\n\n"
                "😊 Mood Tracking:\n"
                "  • 'I am happy' / 'I am sad' / 'Mood Report'\n\n"
                "⏰ Utilities:\n"
                "  • 'Time' / 'Date' / 'Messages'\n\n"
                "🔢 Calculator:\n"
                "  • 'Calculate 25+10' / 'Calculate 100/5'\n\n"
                "🎭 Fun Features:\n"
                "  • 'Joke' / 'Motivate me'\n\n"
                "📚 Knowledge:\n"
                "  • 'What is AI' / 'What is Python' / 'Who created you'\n\n"
                "❌ Close Chat:\n"
                "  • 'Exit' / 'Quit' / 'Bye'"
            )
            
    
        else:
            bot_reply = "I didn't quite catch that. Try typing 'help' to see my valid commands!"
            
    
        print(f"🤖 {BOT_NAME}: {bot_reply}")
        chat_log.append(f"{BOT_NAME}: {bot_reply}")
        print("-" * 30)
        time.sleep(0.4)

    
    print("\n" + "=" * 50)
    
    if sentiment_score > 0:
        print("📊 Overall Session Vibe: Positive Mood")
    elif sentiment_score < 0:
        print("📊 Overall Session Vibe: Negative Mood")
    else:
        print("📊 Overall Session Vibe: Neutral Mood")

    try:
        with open("chat_history.txt", "a", encoding="utf-8") as file:
            file.write(f"\n--- Session Log: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ---\n")
            file.write(f"User Name: {user_name} | Total Interactions: {message_count}\n")
            for line in chat_log:
                file.write(line + "\n")
        print("💾 Your conversation has been successfully saved to 'chat_history.txt'!")
    except Exception as e:
        print("Could not save the conversation logs:", e)

    print("=" * 50)

if __name__ == "__main__":
    chatbot()
