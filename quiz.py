def quiz():
    questions = ["What is the chemical symbol for the element Gold?",
                 "Which composer wrote 'The Four Seasons'?",
                 "In which year did World War I begin?",
                 "Who painted the famous artwork 'The Starry Night'?"]
    options = [["A. Au", "B. Ag", "C. Fe", "D. Cu"],
               ["A. Ludwig van Beethoven", "B. Wolfgang Amadeus Mozart", "C. Johann Sebastian Bach", "D. Antonio Vivaldi"],
               ["A. 1914", "B. 1915", "C. 1916", "D. 1917"],
               ["A. Vincent van Gogh", "B. Pablo Picasso", "C. Leonardo da Vinci", "D. Claude Monet"]]
    answers = ["A", "D", "A", "A"]
    score = 0
    
    print("Welcome to the Challenging Quiz Game!\n")
    for i in range(len(questions)):
        print("Question", i+1, ":", questions[i])
        for option in options[i]:
            print(option)
        user_answer = input("Your answer: ").upper()
        if user_answer == answers[i]:
            print("Correct!")
            score += 1
        else:
            print("Incorrect!")
    
    print("\nQuiz Complete!")
    print("Your score is:", score, "/", len(questions))

quiz()
