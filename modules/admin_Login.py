import db_config
from modules import patient
from modules import doctor
from modules import appointment
from modules import billing
from modules import reports

def ad_login():
    conn = db_config.get_connection()
    cursor = conn.cursor()
    username = input("Enter the username of the admin : ")
    password = input("Enter the password : ")

    query = "SELECT * FROM hospital.adminusers WHERE username = %s AND password = %s"
    cursor.execute(query, (username, password))
    result = cursor.fetchone()

    cursor.close()
    conn.close()

    if result:
        while True:
            print("---- Login success as ADMIN ----")
            print('--- Admin Menu ---')
            print('1. Add patient')
            print('2. Add Doctor')
            print('3. View Doctors')
            print('4. Book appointment')
            print('5. Generate bill')
            print('6. View appointment')
            print('7. Exit')

            choice = input("Enter your choice : ")

            if choice == '1':
                patient.add_patient()
            elif choice == '2':
                doctor.add_doctor()
            elif choice == '3':
                doctor.list_doctors()
            elif choice == '4':
                appointment.book_appointment()
            elif choice == '5':
                billing.generate_bill()
            elif choice == '6':
                reports.view_today_appointments()
            elif choice == '7':
                print('Exiting.....')
                break

            else:
                print('Enter valid input please.')

    else:
        print('Login failed...')
