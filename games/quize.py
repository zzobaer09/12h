# ----------------------------------------------------------------
def game():
    
    question_num = 0 
    correct_point = 0
    guesses = []
    for key in questions:
        print(key)
        for i in options[question_num]:
            print(i)
        question_num += 1
        guess = input("enter (a, b, c, d): ").upper()
        guesses.append(guess)
        correct_point += chack_answers(questions.get(key) , guess)
    display_score(correct_point , guesses)
    # play_again()
        
        
        
        
         

# ----------------------------------------------------------------

def chack_answers(ans , user_guess):
    if ans == user_guess:
        return 1
    else:
        return 0

# ----------------------------------------------------------------
def display_score(correct_points , guesses):
    print("********************************")
    print("RESULT HERE!!")
    print("********************************")
    
    # here i have printed correct answers
    print("answers are: " , end=' ')
    for i in questions:
        print(questions.get(i) , end=' ')
    print()    
    # here i have printed user guesses
    print("your guesses are: " , end=' ')
    for i in guesses:
        print(i , end=' ')
    print()
    
    scores = int((correct_points/len(questions))*100)
    print("CONGRATULATIONS!!")
    print(f"your score is: {scores}%")
# ----------------------------------------------------------------
def play_again():
    play_again = input("do you wanna play again? [y/n]: ").lower()
    if play_again == "y":
      return True
    else:
      return False






questions = {
 "Who created Python?: ": "A",
 "What year was Python created?: ": "B",
 "Python is tributed to which comedy group?: ": "C",
 "Is the Earth round?: ": "A"
}

options = [["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerburg"],
          ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
          ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],
          ["A. True","B. False", "C. sometimes", "D. What's Earth?"]]

    
 
game()


while play_again():
    game()
    
print("Byeeeee!!")
