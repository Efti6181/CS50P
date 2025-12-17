import sys
from pyfiglet import Figlet
import random

figlet = Figlet()
fonts = figlet.getFonts()

# No command-line arguments → random font
if len(sys.argv) == 1:
    font = random.choice(fonts)

# Proper usage: python figlet.py -f fontname
elif len(sys.argv) == 3 and sys.argv[1] in ["-f", "--font"]:
    if sys.argv[2] in fonts:
        font = sys.argv[2]
    else:
        sys.exit("Invalid usage")

# Anything else → error
else:
    sys.exit("Invalid usage")

# Ask the user for input
text = input("Input: ")

# Render output
figlet.setFont(font=font)
print("Output:")
print(figlet.renderText(text))
