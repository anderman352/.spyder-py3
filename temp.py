#!/usr/bin/python
import time

def main(): 
    flag = ''
    with open('./flag.txt', 'r') as f:
        flag = f.readline().strip()

    print("=========== Welcome to the USHKUYNIK smart rifle system! ===========", end="", flush=True)
    time.sleep(1)

    admin = False
    admin_pw_encrypted = '6d6e71775b7174727b7d6f6f536460506479774c677877656c4668727a717b40494f46565751545e'

    while True:
        print("\nWhat would you like to do?\n", flush=True)
        print("1. Activate FRIEND-OR-FOE system")
        print("2. Enter administrator password")
        print("3. Exit")
        user_in = input('> ')

        if user_in == '1':
            if admin:
                print('\nFRIEND-OR-FOE system activated.', flush=True)
                time.sleep(0.5)
                print(f'\nCongratulations! Here is the flag: {flag}')
                exit()
            else:
                print('\nERROR: Administrator privileges required.', flush=True)
                time.sleep(1)
        elif user_in == '2':
            print('\nPlease enter the administrator password: ', end="", flush=True)
            pw = input("")
            admin_pw = ''.join(chr(ord(c) ^ i) for i, c in enumerate(bytes.fromhex(admin_pw_encrypted).decode("utf-8")))
            if pw == admin_pw:
                admin = True 
                print('\nAdministrator password verified. Privileges updated.', flush=True)
                time.sleep(1)
            else:
                print('\nERROR: Incorrect administrator password', flush=True)
                time.sleep(1)
        elif user_in == '3':
            exit()
        else:
            print('\nInvalid option. Please try again', flush=True)
            time.sleep(1)


if __name__ == "__main__":
    main()