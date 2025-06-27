from db_config import get_connection
from modules import patient
from modules import doctor
from modules import billing
from modules import reports
from modules import appointment

def recep_login():
    conn = get_connection()
    cursor = conn.cursor()
    username = input('Enter the username of Receptionist : ')
    password = input('Enter the password : ')

    query = "SELECT * FROM hospital.receptionist_users WHERE username = %s AND password = %s"
    cursor.execute(query, (username, password))
    result = cursor.fetchone()

    cursor.close()
    conn.close()

    if result:
        while True:
            print("---- Login success as RECEPTIONIST ----")
            print('--- Receptionist Menu ---')
            print('1. Add patient')
            print('2. View Doctors')
            print('3. Book appointment')
            print('4. Generate bill')
            print('5. View appointment')
            print('6. Exit')

            choice = input("Enter your choice : ")

            if choice == '1':
                patient.add_patient()
            elif choice == '2':
                doctor.list_doctors()
            elif choice == '3':
                appointment.book_appointment()
            elif choice == '4':
                billing.generate_bill()
            elif choice == '5':
                reports.view_today_appointments()
            elif choice == '6':
                print('Exiting.....')
                break
            else:
                print('Enter valid input please.')

    else:
        print('Login failed...')

