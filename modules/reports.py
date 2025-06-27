from db_config import get_connection

def view_today_appointments():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM today_appointments')
    for row in cursor.fetchall():
        print(row)
    conn.close()