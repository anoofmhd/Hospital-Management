from db_config import get_connection

def generate_bill():
    appointment_id = int(input('Appointment ID : '))
    fee = float(input('Consultation Fee : '))

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO bill (appointment_id, consultation_fee, total_amount) VALUES (%s, %s, %s)',
                   (appointment_id, fee, fee))
    conn.commit()
    print('Bill generated.')
    conn.close()