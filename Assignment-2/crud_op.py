
import csv
import os

class Employee:
    def __init__(self):
        self.f = "employee.csv"

    def create(self):
        with open(self.f, "w", newline="") as f:
            w = csv.writer(f)
            w.writerow(["ID", "Name", "Salary"])
            print("File created.")

    def add(self):
        if not os.path.exists(self.f):
            print("Create file first.")
            return

        with open(self.f, "a", newline="") as f:
            w = csv.writer(f)
            i = input("ID: ")
            n = input("Name: ")
            s = input("Salary: ")
            w.writerow([i, n, s])
            print("Added.")

    def display(self):
        if not os.path.exists(self.f):
            print("File not found.")
            return

        with open(self.f, "r") as f:
            for r in csv.reader(f):
                print(r)

    def update(self):
        if not os.path.exists(self.f):
            print("File not found.")
            return

        with open(self.f, "r") as f:
            rows = list(csv.reader(f))

        i = input("ID: ")
        found = False

        for r in rows[1:]:
            if r[0] == i:
                r[1] = input("New name: ")
                r[2] = input("New salary: ")
                found = True
                break

        if found:
            with open(self.f, "w", newline="") as f:
                csv.writer(f).writerows(rows)
            print("Updated.")
        else:
            print("ID not found.")

    def delete(self):
        if not os.path.exists(self.f):
            print("File not found.")
            return

        with open(self.f, "r") as f:
            rows = list(csv.reader(f))

        i = input("ID: ")
        new = [rows[0]]

        for r in rows[1:]:
            if r[0] != i:
                new.append(r)

        if len(new) == len(rows):
            print("ID not found.")
        else:
            with open(self.f, "w", newline="") as f:
                csv.writer(f).writerows(new)
            print("Deleted.")

e = Employee()

while True:
    print("\n1. Create  2. Add  3. Display")
    print("4. Update  5. Delete  6. Exit")

    try:
        ch = int(input("Choice: "))

        if ch == 1:
            e.create()
        elif ch == 2:
            e.add()
        elif ch == 3:
            e.display()
        elif ch == 4:
            e.update()
        elif ch == 5:
            e.delete()
        elif ch == 6:
            break
        else:
            print("Wrong choice")

    except ValueError:
        print("Enter a number.")
