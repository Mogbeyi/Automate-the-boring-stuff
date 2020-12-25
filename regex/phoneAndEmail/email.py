import re

# Create email regex.
email_regex = re.compile(
    r"""(
[a-zA-Z0-9._%+-]+           # username
@                           # symbol
[a-zA-Z0-9.-]+              # domain name
(\.[a-zA-Z]{2,4})           # dot-something
)""",
    re.VERBOSE,
)


def get_email_adresses(text):
    email_matches = []

    for groups in email_regex.findall(text):
        email_matches.append(groups[0])

    return email_matches
