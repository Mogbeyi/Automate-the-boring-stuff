import re

text = 'Robocop eats baby food. BABY FOOD.'
vowels = 'aeiouAEIOU'

def vowel_regex_finder():
    vowelRegex = re.compile(r'[aeiouAEIOU]')
    return vowelRegex.findall(text)

def consonant_regex_finder():
    consonant_regex = re.compile(r'[^aeiouAEIOU]')
    return consonant_regex.findall(text)

def vowel_normal_finder():
    result = []

    for char in text:
        if char in vowels:
            result.append(char)

    return result

print(vowel_regex_finder())
print(vowel_normal_finder())
print(consonant_regex_finder())

