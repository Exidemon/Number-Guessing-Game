import random

level_is_chosen = False
difficulty = ""
random_num = str(random.randint(1, 100))
has_guessed_answer = False
user_guess = ""
guess_attempts = 0
continue_playing = True
print(random_num)

print("Welcome to the Number Guessing Game! \nI'm thinking of a number between 1 and 100.\n")

while continue_playing == True:
    print("Please select the difficulty level: \n1. Easy (10 chances) \n2. Medium (5 chances) \n3. Hard (3 chances)\n")

    while level_is_chosen == False:
        level_choice = int(input("Enter your choice: "))
        
        if level_choice == 1:
            guesses = 10
            difficulty = "Easy"
            level_is_chosen = True

        elif level_choice == 2:
            guesses = 5
            difficulty = "Medium"
            level_is_chosen = True

        elif level_choice == 3:
            guesses = 3
            difficulty = "Hard"
            level_is_chosen = True

        else:
            print("Please choose a number 1-3.")
        
    print(f"\nGreat! You have selected the {difficulty} difficulty level. \nLet's start the game!\n")

    while has_guessed_answer == False:
        if guesses != 0:
            user_guess = input("Enter your guess: ")
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
                print(f"Congratulations! You guessed the correct number in {guess_attempts} attempts.")
                has_guessed_answer = True
        else:
            print("You have run out of guessess!")
            break
