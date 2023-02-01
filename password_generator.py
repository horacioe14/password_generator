"""Program that generates passwords"""

import string
import random


def password_generator():
    while True:
        print('''-- Password generator --
        Choose option:
        1: generate password
        2: exit the program''')
        data = input()
        if data == '1':
            print('Your choice: ' + data)
            letters = string.ascii_lowercase
            digits = '0123456789'
            special = '!@#$%&*^|()_+'
            password = ''
            while True:
                print('''Provide password length:''')
                length_choice = input()
                if not length_choice.isnumeric():
                    print('Please enter number\n')
                    continue
                break
            while True:
                print('Use uppercase letter? (y/n)): ')
                upper_choice = input().lower()
                if upper_choice == 'y':
                    break
                if upper_choice == 'n':
                    break
                print('Please enter y or n\n')
                continue
            while True:
                print('Use digits? (y/n)): ')
                digits_choice = input().lower()
                if digits_choice == 'y':
                    break
                if digits_choice == 'n':
                    break
                print('Please enter y or n\n')
                continue
            while True:
                print('Use special characters? (y/n)): ')
                special_choice = input().lower()
                if special_choice == 'y':
                    break
                if special_choice == 'n':
                    break
                print('Please enter y or n\n')
                continue

            if upper_choice == 'y' and digits_choice == 'y' and special_choice == 'y':
                for value in range(int(length_choice)):
                    password += random.choice(letters +
                                              letters.upper()+digits+special)
            elif upper_choice == 'y' and digits_choice == 'y' and special_choice == 'n':
                for value in range(int(length_choice)):
                    password += random.choice(letters+letters.upper()+digits)
            elif upper_choice == 'y' and digits_choice == 'n' and special_choice == 'y':
                for value in range(int(length_choice)):
                    password += random.choice(letters+letters.upper()+special)
            elif upper_choice == 'y' and digits_choice == 'n' and special_choice == 'n':
                for value in range(int(length_choice)):
                    password += random.choice(letters+letters.upper())
            elif upper_choice == 'n' and digits_choice == 'n' and special_choice == 'n':
                for value in range(int(length_choice)):
                    password += random.choice(letters)
            elif upper_choice == 'n' and digits_choice == 'y' and special_choice == 'y':
                for value in range(int(length_choice)):
                    password += random.choice(letters+digits+special)
            elif upper_choice == 'n' and digits_choice == 'n' and special_choice == 'y':
                for value in range(int(length_choice)):
                    password += random.choice(letters+special)
            elif upper_choice == 'n' and digits_choice == 'y' and special_choice == 'n':
                for value in range(int(length_choice)):
                    password += random.choice(letters+digits)

            print(f'Generated password: {password}\n')

            continue
        if data == '2':
            print('\nBye!\n')
            break
        print('\nPlease enter the correct value\n')
        continue


if __name__ == '__main__':
    password_generator()
