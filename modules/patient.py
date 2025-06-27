from db_config import get_connection

def add_patient():
    name = input(" Name : ")
    age = int(input(' Age : '))
    gender = input(' Gender : ')
    contact = input(' Contact : ')

    conn = get_connection()
    cursor = conn.cursor()
    cursor.callproc("AddPatient", (name, age, gender, contact))
    conn.commit()
    print('Patient added successfully.')
    conn.close()