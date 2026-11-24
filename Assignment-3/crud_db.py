
import sqlite3

class Employee:
    def __init__(self):
        self.con = sqlite3.connect("employee.db")
        self.cur = self.con.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS employee(id INTEGER PRIMARY KEY, name TEXT, salary INTEGER)")

    def add(self):
        i = int(input("ID: "))
        n = input("Name: ")
        s = int(input("Salary: "))
        self.cur.execute("INSERT INTO employee VALUES(?,?,?)", (i, n, s))
        self.con.commit()
        print("Added.")

    def display(self):
        self.cur.execute("SELECT * FROM employee")
        for r in self.cur.fetchall():
            print(r)

    def update(self):
        i = int(input("ID: "))
        s = int(input("New salary: "))
        self.cur.execute("UPDATE employee SET salary=? WHERE id=?", (s, i))
        self.con.commit()
        print("Updated.")

    def delete(self):
        i = int(input("ID: "))
        self.cur.execute("DELETE FROM employee WHERE id=?", (i,))
        self.con.commit()
        print("Deleted.")

e = Employee()

while True:
    print("\n1. Add")
    print("2. Display")
    print("3. Update")
    print("4. Delete")
    print("5. Exit")

    ch = int(input("Choice: "))

    if ch == 1:
        e.add()
    elif ch == 2:
        e.display()
    elif ch == 3:
        e.update()
    elif ch == 4:
        e.delete()
    elif ch == 5:
        break
    else:
        print("Wrong choice")
