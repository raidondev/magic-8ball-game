import random

# User asks a question
user_ask_question = input("Ask me a question: ")

# Magic 8-Ball answers
magic8ball_magic8ball_answer = ""

# Pick a random number between 1-10
random_number = random.randint(1, 10)

# Repeat the question back to the user sarcastically
repeat_question_as_question = user_ask_question + "Really? That's what you ask me?"

# Check if user asked question
# TODO: Add checks for vaild questions and no input from user.

# Defines a random output based on random_number 1-10
if random_number == 1:
    magic8ball_answer = "Yes - definitely"
elif random_number == 2:
    magic8ball_answer = "It is decidedly so"
elif random_number == 3:
    magic8ball_answer = "Without a doubt"
elif random_number == 4:
    magic8ball_answer = "Reply hazy, try again"
elif random_number == 5:
    magic8ball_answer = "Ask again later"
elif random_number == 6:
    magic8ball_answer = "Better not tell you now"
elif random_number == 7:
    magic8ball_answer = "My sources say no"
elif random_number == 8:
    magic8ball_answer = "Outcome looks grim!"
elif random_number == 9:
    magic8ball_answer = "Very doubtful"
elif random_number == 10:
    magic8ball_answer = repeat_question_as_question
else:
    magic8ball_answer = "Error"

print("Magic 8-Ball: " + magic8ball_answer)