import random
target_number = random.randint(1, 100)

guesses = None
attempts = 0

print("***Welcome to the Guess the Number game!***")
print("I have picked a number between 1 and 100.")

while (guesses != target_number):
    try:
    
        guesses = int(input("Guess the number: "))
        if(guesses > target_number):
            print("Lower number please!")
            attempts += 1
        elif(guesses < target_number):    
            print("Higher number please!")
            attempts += 1

    except ValueError:
        print("Invalid input! Please enter a valid integer.")

print(f"you have guessed the number {target_number} correctly in {attempts} attempt")