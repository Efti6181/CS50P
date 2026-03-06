import re
def main():
    print(validate(input("IPv4 Address: ")))
def validate(ip):
    pattern = r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$"
    match = re.match(pattern, ip)
    if not match:
        return False
    for num in match.groups():
        if len(num) > 1 and num[0] == "0":
            return False
        if not 0 <= int(num) <= 255:
            return False
    return True
if __name__ == "__main__":
    main()

