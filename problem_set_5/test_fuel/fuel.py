def main():
    while True:
        try:
            fraction = input("Fraction: ")
            percent = convert(fraction)
            print(gauge(percent))
            break
        except (ValueError, ZeroDivisionError):
            pass


def convert(fraction):
    """
    Convert a string fraction like '3/4' into an integer percentage.
    Raises ValueError for invalid fractions, negative numbers, or numerator > denominator.
    Raises ZeroDivisionError for denominator 0.
    """
    try:
        x_str, y_str = fraction.split("/")
        x = int(x_str)
        y = int(y_str)
    except:
        raise ValueError("Invalid fraction format")

    if y == 0:
        raise ZeroDivisionError("Denominator cannot be zero")
    if x < 0 or y < 0:
        raise ValueError("Negative values not allowed")
    if x > y:
        raise ValueError("Numerator cannot be greater than denominator")

    return round(x / y * 100)


def gauge(percentage):
    """
    Return 'E' if <= 1%, 'F' if >= 99%, otherwise return percentage string.
    """
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
