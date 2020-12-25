from phone import *
from email import *
import pyperclip


def main():
    text = str(pyperclip.paste())
    phone_numbers = get_phone_numbers(text)
    emails = get_email_adresses(text)
    numbers_and_emails = phone_numbers + emails

    if len(numbers_and_emails) > 0:
        finalMatch = "\n".join(numbers_and_emails)
        pyperclip.copy(finalMatch)
        print("Copied to clipboard:")
        print(finalMatch)
    else:
        print("No phone numbers or email adresses found.")


if __name__ == "__main__":
    main()
