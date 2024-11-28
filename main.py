import random
secret_num = random.randint(1,100)
count = 0
while True:
  try:
    user_guess = int(input("Guess a number between 1 and 100: "))
  except ValueError:
    print("Please enter a number")
    continue
  if user_guess == secret_num:
    print("You guessed the number!")
    break
  elif user_guess > secret_num:
    print("Too high")
  elif user_guess < secret_num:
    print("Too low")
  count +=1

print("You win! It took you", count, "guesses.")
