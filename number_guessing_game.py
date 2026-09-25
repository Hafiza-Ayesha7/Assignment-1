# Step 1: Define target variable
secret_number = 7

# Step 2: User guess input
guess = int(input("Guess the secret number: "))

# Step 3: Match verification
if guess == secret_number:
    print("Correct guess!")
else:
    print("Wrong guess, try again next time.")