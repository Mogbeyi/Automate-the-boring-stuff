import clipboard, re

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?              # area code 
    (\s|-|\.)?                      # separator
    (\d{3})                         # first 3 digits
    (\s|-|\.)                       # Separator
    (\d{4})                         # Last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?  # extension
    )''', re.VERBOSE)

# Create email regex. 
emailRegex = re.compile(r'''(
[a-zA-Z0-9._%+-]+           # username
@                           # symbol
[a-zA-Z0-9.-]+              # domain name
(\.[a-zA-Z]{2,4})           # dot-something
)''', re.VERBOSE)

def get_phone_numbers(text):
    phone_number_matches = []

    for groups in phoneRegex.findall(text):
        phoneNum = '-'.join([groups[1], groups[3], groups[5]])
        if groups[8] != '':
            phoneNum += ' x' + groups[8]
        phone_number_matches.append(phoneNum)

    return phone_number_matches 

def get_email_adresses(text):
    email_matches = []

    for groups in emailRegex.findall(text):
        email_matches.append(groups[0])

    return email_matches

def main():
    text = clipboard.paste()
    phone_numbers = get_phone_numbers(text)
    emails = get_email_adresses(text)
    numbers_and_emails = phone_numbers + emails

    if len(numbers_and_emails) > 0:
        finalMatch = '\n'.join(numbers_and_emails)
        clipboard.copy(finalMatch)
        print('Copied to clipboard:')
        print(finalMatch)
    else:
        print("No phone numbers or email adresses found.")

main()