import re

def identify_bullet_or_numbering(text):
    bullet_patterns = [r'^\s*[•◦▪▫●○■□►→∙‣⦿]']
    numbering_patterns = [r'^\s*(\d+|\([a-zA-Z]\)|[ivxlcdmIVXLCDM]+)\.?']

    for pattern in bullet_patterns:
        if re.match(pattern, text):
            return "Bullet Point"

    for pattern in numbering_patterns:
        if re.match(pattern, text):
            return "Numbering"

    return None

text = "1.1 דגשדג"
result = identify_bullet_or_numbering(text)
if result:
    print(f"The text represents {result}.")
else:
    print("The text does not represent any recognized bullet or numbering style.")
