import re

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    # Match four groups of 1–3 digits
    pattern = r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$"
    match = re.match(pattern, ip)
    if not match:
        return False

    # Check each number
    for num in match.groups():
        # No leading zeros unless the number is exactly '0'
        if len(num) > 1 and num[0] == "0":
            return False
        # Check range 0–255
        if not 0 <= int(num) <= 255:
            return False

    return True

if __name__ == "__main__":
    main()
