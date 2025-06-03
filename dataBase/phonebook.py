import sqlite3

# اتصال به دیتابیس
conn = sqlite3.connect('phonebook.db')
cursor = conn.cursor()

# ساخت جدول (در صورت نیاز)
cursor.execute('''
CREATE TABLE IF NOT EXISTS contacts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    phone TEXT NOT NULL,
    email TEXT
)
''')

# توابع کاربردی
def add_contact(name, phone, email):
    cursor.execute("INSERT INTO contacts (name, phone, email) VALUES (?, ?, ?)", (name, phone, email))
    conn.commit()
    print("contact has been added succesfully.")

def show_contacts():
    cursor.execute("SELECT * FROM contacts")
    results = cursor.fetchall()
    if results:
        for row in results:
            print(row)
    else:
        print("There is no contact to show.")

def search_contact(number):
    cursor.execute("SELECT * FROM contacts WHERE phone LIKE ?", ('%' + number + '%',))
    results = cursor.fetchall()
    if results:
        for row in results:
            print(row)
    else:
        print("No such contact was founded.")

def delete_contact(contact_id):
    cursor.execute("DELETE FROM contacts WHERE id = ?", (contact_id,))
    conn.commit()
    print(f"contact with id:{contact_id} was deleted.")

# منوی اصلی
def menu():
    while True:
        print("\n--- phonebook  ---")
        print("1. add contact")
        print("2. show all  contacts")
        print("3. search contact")
        print("4. delete contact")
        print("5. exit")

        choice = input("choose an option: ")

        if choice == '1':
            name = input("name: ")
            phone = input("phone number : ")
            email = input("email (optional): ")
            add_contact(name, phone, email)

        elif choice == '2':
            show_contacts()

        elif choice == '3':
            number = input("number for search: ")
            search_contact(number)

        elif choice == '4':
            contact_id = input("contact id to remove: ")
            delete_contact(contact_id)

        elif choice == '5':
            print("exit from the app...")
            break

        else:
            print("invalid input!")

    conn.close()

# اجرای برنامه
menu()