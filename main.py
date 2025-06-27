import mysql.connector
from modules import admin_Login
from modules import receptionist_Login
from modules import doctor_login

def main():
    while True:
        print('---LOGIN AS---')
        print('1. Admin')
        print('2. Receptionist')
        print('3. Doctor')
        print('4. Exit')
        choice = input('Enter your choice  :  ')

        if choice == '1':
            admin_Login.ad_login()
        elif choice == '2':
            receptionist_Login.recep_login()
        elif choice == '3':
            doctor_login.doctor_login()
        elif choice == '4':
            print('Exiting.....')
            break
        else:
            print("Input is wrong. Please enter valid input")

if __name__ == '__main__':
        main()