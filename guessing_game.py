import random
secret_number = random.randint(1,20)
guess = 0
attempts = 0
print("I'm thinking of a number between 1 and 20")
while guess != secret_number:
    guess = int(input("take a guess"))
    attempts = attempts + 1
    if guess <secret_number:
        print("Too Low")
    elif guess > secret_number:
        print("Too High")
    else:
        print(f"You got it! The number was {secret_number}.")

print(f"it took you {attempts} tries.")