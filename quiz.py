'''I am writing a code to create a quiz for the basketball star Steven Adams.
20/4/26. Jack Pick.'''
#list of the questions
questions = ("Where in New Zealand is Steven Adams from?:",
                       "How tall is Steven Adams?:",
                       "What team in the NBA is Steven Adams currently in?:",
                       "What team was Steven Adams previously in before his current team?:",
                       "How many siblings does Steven Adams have?:",
                       "Where is Steven Adams dad from?:",
                       "Where is Steven Adams mum from?:",
                       "Where did Steven Adams go to college for basketball in the US?:",
                       "What was Steven Adams first team in the NBA?:",
                       "What year was Steven Adams drafted to his first team in the NBA?:")

#list of all the options to chose for the questions
options =(("A. Auckland", "B. Rotorua", "C. Christchurch"),
                   ("A. 6'3", "B. 6'5", "C. 6'11"),
                   ("A. Rockets", "B. Lakers", "C. Bulls"),
                   ("A. Grizzlies", "B. Celtics", "C. Kings"),
                   ("A. 10", "B. 5", "C. 17"),
                   ("A. England", "B. New Zealand", "C. United States"),
                   ("A. New Zealand", "B. Tonga", "C. Samoa"),
                   ("A. Pittsburgh", "B. Kansas", "C. Kentucky"),
                   ("A. Heat", "B. Warriors", "C. City"),
                   ("A. 2015", "B. 2013", "C. 2012"))
#list of the correst answers
answers = ["B", "C", "A", "A", "C", "A", "B", "A", "C", "B"]
guesses = []
valid = ["A", "B", "C"]
score = 0
question_num = 0

for question in questions:
    print("----------------------")
    print(question)
    for option in options[question_num]:
        print(option)
    guess = input("Enter (A, B, C): ").upper()
    while guess is not valid:
        print("Invalid input please enter only A, B or C!!")       
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1

print("----------------------")
print("       RESULTS       ")
print("----------------------") 

print("correct answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()
#turning the score into a percentage
score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")   