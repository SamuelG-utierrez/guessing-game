import random  #the module needed

random_number = random.randint(1, 10) #random number needed to be guessed
previous_guesses = [] #saving all prev guesses
correct_answer_picked = False #if true, they win
tries_remaining = 5 #tries they get

while not correct_answer_picked and tries_remaining > 0:  #while they have turns and havent guessed correctly
    print(f"You have {tries_remaining} tries remaining.\n") #tries they got
    user_guess = int(input("Enter a number between 1 - 10: ")) #their current guess

    while user_guess < 1 or user_guess > 10 or user_guess in previous_guesses:  #checking for invalid inputs
        if user_guess < 1 or user_guess > 10: #if outside of the range
            print("\nInvalid input!") #print invalid
            print(f"You still have {tries_remaining} tries remaining.") #they dont lose a try
            user_guess = int(input("Please enter a number between 1 and 10: ")) #retry the guess
        else: #holy this is a lot of comments
            print(f"\nYou already guessed {user_guess}!") #if they guessed same thing again
            print("Choose a different number.") #they choose a new one
            print(f"\nPrevious guesses: {previous_guesses}") #their old guesses (if forgot)
            print(f"\nYou still have {tries_remaining} tries remaining.") #current tries
            user_guess = int(input("\nEnter a number between 1 - 10: ")) #retry the guess

    previous_guesses.append(user_guess) #adds the new guess to the end of the list

    if user_guess == random_number: #if they get it right!
        print(f"\nYou guessed correctly! The number was {random_number}.") #they get a conrats
        print(f"\nYour guesses: {previous_guesses}") #they get shown all their old guesses
        correct_answer_picked = True #end the game
    else: #if they dont get it right
        tries_remaining = tries_remaining - 1 #lose a try
        if user_guess > random_number: #check if lwoer or higher
            print("Try again! The random number is lower!") #let htem know if lower
        else: #what am i supposed to put here? its just an else
            print("Try again! The random number is higher!")#let know if higher
        print(f"\nPrevious guesses: {previous_guesses}\n")# get their prev guesses

if not correct_answer_picked: #if they run out of tries
    print("You ran out of tries!") #they get made fun of!
    print(f"\nYour guesses were: {previous_guesses}") #all of their (wrong) guesses
    print(f"\nThe correct number was {random_number}.") #what the guess should have bee
    print("\nGame over!") #they lose. LOSER
    #too many comments