import random

def startgame():
    level_is_chosen = False
    difficulty = ""
    random_num = random.randint(1, 100)
    has_guessed_answer = False
    user_guess = ""
    guess_attempts = 1
    play_again_answer = False
    print(random_num)
    print("Welcome to the Number Guessing Game! \nI'm thinking of a number between 1 and 100.\n")

    print("Please select the difficulty level: \n1. Easy (10 chances) \n2. Medium (5 chances) \n3. Hard (3 chances)\n")

    while level_is_chosen == False:
        level_choice = input("Enter your choice: ")
        
        if level_choice == "1":
            guesses = 10
            difficulty = "Easy"
            level_is_chosen = True

        elif level_choice == "2":
            guesses = 5
            difficulty = "Medium"
            level_is_chosen = True

        elif level_choice == "3":
            guesses = 3
            difficulty = "Hard"
            level_is_chosen = True

        else:
            print("Please choose a number 1-3.")
        
    print(f"\nGreat! You have selected the {difficulty} difficulty level. \nLet's start the game!\n")

    while has_guessed_answer == False:
        if guesses != 0:
            try:
                user_guess = int(input(f"Guess {guess_attempts} \nEnter your guess: "))
            except ValueError as Error:
                print("Oops! You didn't enter a number!\n")
                continue

            if user_guess != random_num:
                if user_guess >= random_num:
                    print(f"Incorrect! The number is less than {user_guess}.\n")
                    guesses -= 1
                    guess_attempts += 1
                elif user_guess <= random_num:
                    print(f"Incorrect! The number is greater than {user_guess}.\n")
                    guesses -= 1
                    guess_attempts += 1
                else: 
                    print("Please choose a number 1-100.")
            else:
                print(f"Congratulations! You guessed the correct number in {guess_attempts} attempt/s.")
                break
        else:
            print("You have run out of guessess!")
            break

    while play_again_answer == False:
        continue_playing = input("Would you like to play again (Y/N): ")
        if continue_playing.upper() == "N":
            print("Okay Goodbye!")
            return
        elif continue_playing.upper() == "Y":
            print("Okay lets go again!")
            startgame()
        else:
            print("Try again!")

startgame()
