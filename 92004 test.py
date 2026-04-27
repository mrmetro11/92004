'''I am writing a code to create a quiz for the basketball star Steven Adams.
20/4/26. Jack Pick.'''

questions =("Where in New Zealand is Steven Adams from?: ",
            "How tall is Steven Adams?: ",
            "What team in the NBA is Steven Adams currently in?: ",
            "What team was Steven Adams previously in before his current team?: ",
            "How many siblings does Steven Adams have?: ",
            "Where is Steven Adams dad from?: ",
            "Where is Steven Adams mum from?: ",
            "Where did Steven Adams go to college for basketball in the US?: ",
            "What was Steven Adams first team in the NBA?: "
            "What year was Steven Adams drafted to his first team in the NBA?: ")

options =(("A. Auckland", "B. Rotorua", "C. Christchurch",),
          ("A. 6'3", "B. 6'5", "C. 6'11",),
          ("A. Rockets", "B. Lakers", "C. Bulls",),
          ("A. Grizzlies", "B. Celtics", "C. Kings",),
          ("A. 10", "B. 5", "C. 17",),
          ("A. England", "B. New Zealand", "C. United States",),
          ("A. New Zealand", "B. Tonga", "C. Samoa",),
          ("A. Pittsburgh", "B. Kansas", "C. Kentucky",),
          ("A. Heat", "B. Warriors", "C. City",),
          ("A. 2015", "B. 2013", "C. 2012",))
awnsers = ("B", "C", "A", "A", "C", "A", "B", "A", "C", "B")
guesses = []
score = 0
question_num = 0
for question in questions:
    print("----------------------")
    print(question)
    for option in options [question_num]:
        print(option)
        guess = input("Enter (A, B, C,): ").upper()
        guesses.append(guess)
        if guess == awnsers[question_num]:
            score += 1
            print("CORRECT!")
        else:
            print("INCORRECT!")
            print(f"{awnsers[question_num]} is the correct awnser")
        question_num += 1