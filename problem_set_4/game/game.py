import random

# Prompt user for level
while True:
    try:
        level = int(input("Level: "))
        if level > 0:
            break
    except ValueError:
        pass

# Generate target number
target = random.randint(1, level)

# Guess loop
while True:
    try:
        guess = int(input("Guess: "))
        if guess <= 0:
            continue
    except ValueError:
        continue

    if guess < target:
        print("Too small!")   
    elif guess > target:
        print("Too large!")
    else:
        print("Just right!")
        break
