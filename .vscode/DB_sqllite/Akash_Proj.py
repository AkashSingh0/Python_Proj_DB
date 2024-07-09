import sqlite3
conn = sqlite3.connect('Techi_Project.db')

cursor = conn.cursor()

cursor.execute(''' 
    CREATE TABLE IF NOT EXISTS AKashProj (
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               time TEXT NOT NULL
    )
''')

def list_AkashProj():
    cursor.execute("SELECT * FROM AkashProj")
    for row in cursor.fetchall():
        print(row)

def add_AkashProj(name, time):
    cursor.execute("INSERT INTO AkashProj(name, time) VALUES (?,?)", (name, time))
    conn.commit()

def update_AkashProj(ProjID, new_name, new_time):
    cursor.execute("UPDATE AkashProj SET name = ?, time= ? WHERE id= ?", (new_name, new_time, ProjID))
    conn.commit()

def Delete_AkashProj(ProjID):
    cursor.execute("DELETE FROM AkashProj WHERE id=?", (ProjID,))
    conn.commit()

def main():
    while True:
        print("\n AkashProject with DB")
        print("1. List AkashProj")
        print("2. Add AkashProj")
        print("3. Update AkashProj")
        print("4. Delete AkashProj")
        print("5. Exit App")

        choice = input("Enter Your choice: ")

        if choice == '1':
            list_AkashProj()

        elif choice == '2':
            name=input("Enter the AkashProj name: ")
            time=input("Enter the AkashProj time: ")
            add_AkashProj(name, time)

        elif choice == '3':
            ProjID=input("Enter AkashProj ID to update")
            name=input("Enter the AkashProj name: ")
            time=input("Enter the AkashProj time: ")
            update_AkashProj(ProjID,name, time)

        elif choice == '4':
            ProjID=input("Enter AkashProj ID to Delete")
            Delete_AkashProj(ProjID)

        elif choice == '5':
           break

        else:
            print("Invalid Choice")

    conn.close()

if  __name__ == "__main__":
    main()