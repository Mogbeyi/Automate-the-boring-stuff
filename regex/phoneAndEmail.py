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

text = clipboard.paste()
matches = []

for groups in phoneRegex.findall(text):
    print(groups)
    phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)
