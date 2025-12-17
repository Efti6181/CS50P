while True:
    try:
        x, y = input("Fraction: ").split("/")
        x = int(x)
        y = int(y)

        # Reject negatives
        if x < 0 or y < 0:
            raise ValueError

        # Reject x > y
        if x > y:
            raise ValueError

        # Reject division by zero
        if y == 0:
            raise ZeroDivisionError

        break

    except (ValueError, ZeroDivisionError):
        # Simply reprompt
        pass

percentage = round(x / y * 100)

if percentage <= 1:
    print("E")
elif percentage >= 99:
    print("F")
else:
    print(f"{percentage}%")
