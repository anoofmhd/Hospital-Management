from db_config import get_connection

def list_doctors():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT d.name, s.name FROM doctor d JOIN department s ON d.dept_id = s.dept_id")
    for row in cursor.fetchall():
        print(row)
    conn.close()

def add_doctor():
    name = input('Name : ')
    specialization = input('Specialization : ')
    dept_id = int(input('Department ID : '))

    conn = get_connection()
    cursor = conn.cursor()
    cursor.callproc("AddDoctor", (name, specialization, dept_id))
    print("Doctor added successfully.")
    conn.close()



