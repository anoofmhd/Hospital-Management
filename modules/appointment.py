from db_config import get_connection

def book_appointment():
    doctor_id = int(input("Doctor ID : "))
    patient_id = int(input("Patient ID : "))
    date = input("Date (YYYY-MM-DD) : ")
    description = input("Description : ")

    conn = get_connection()
    cursor = conn.cursor()
    try:
        conn.start_transaction()
        cursor.execute("INSERT INTO appointment  (doctor_id, patient_id, appointment_date, description) VALUES (%s, %s, %s, %s)",
                       (doctor_id, patient_id, date, description))
        conn.commit()
        print('Appointment booked.')
    except Exception as e:
        print("Error : ", e)
        conn.rollback()
    conn.close()