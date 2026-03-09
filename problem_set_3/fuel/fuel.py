while True:
    try:
        x, y = input("Fraction: ").split("/")
        x = int(x)
        y = int(y)
        if x < 0 or y < 0:
            raise ValueError
        if x > y:
            raise ValueError
        if y == 0:
            raise ZeroDivisionError
        break
    except (ValueError, ZeroDivisionError):
        pass
percentage = round(x / y * 100)
if percentage <= 1:
    print("E")
elif percentage >= 99:
    print("F")
else:
    print(f"{percentage}%")

