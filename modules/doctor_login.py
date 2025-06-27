from db_config import get_connection
from modules import doctor

def doctor_login():
    conn = get_connection()
    cursor = conn.cursor()
    username = input('Enter username : ')
    password = input('Enter password : ')

    query = "SELECT * FROM hospital.doctorusers WHERE username = %s AND password = %s"
    cursor.execute(query, (username, password))
    result = cursor.fetchone()

    cursor.close()
    conn.close()

    if result:
        print('Login success as Doctor')
        while True:
            print('-- DOCTOR MENU ---')
            print("1. View Doctors.")
            print("2. Exit.")

            choice = input("Enter your choice : ")

            if choice == '1':
                doctor.list_doctors()
            elif choice == '2':
                print('Exiting from Doctor...')
                break
            else:
                print('Invalid input. Please enter a valid input.')

    else:
        print('Login failed as Doctor.\n Please verify the username and password.')