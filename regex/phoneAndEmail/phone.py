import re 

phone_regex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?              # area code 
    (\s|-|\.)?                      # separator
    (\d{3})                         # first 3 digits
    (\s|-|\.)                       # Separator
    (\d{4})                         # Last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?  # extension
    )''', re.VERBOSE)

def get_phone_numbers(text):
    phone_number_matches = []

    for groups in phone_regex.findall(text):
        phoneNum = '-'.join([groups[1], groups[3], groups[5]])
        if groups[8] != '':
            phoneNum += ' x' + groups[8]
        phone_number_matches.append(phoneNum)

    return phone_number_matches 