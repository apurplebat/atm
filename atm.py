"""
Assignment 2 - ATM script.
"""

def main():
    """
    My main function.
    """
    #global vars. attempts is set at 0 but can increase.
    attempts = 0
    pin_num = 1234
    while True:
        #after 3 attempts, the account locks.
        if attempts>=3:
            print('Account locked. Stop hacking!')
            break

        #catches non-integer inputs, which counts as an attempt.
        try:
            user_input = int(input('Please enter your PIN number: '))
        except ValueError:
            attempts = attempts + 1
            print(f"Invalid input; numbers only. Attempt {attempts} of 3.")
            continue

        #if it doesn't match, count the attempt and keep looping.
        if user_input != pin_num:
            attempts = attempts + 1
            print(f"Incorrect PIN. Attempt {attempts} of 3.")

        #if PIN matches, print balance and end the looping program.
        else:
            print('Your account balance is: $7.25. Need a loan?')
            break


# for command line.
if __name__ == '__main__':
    main()
