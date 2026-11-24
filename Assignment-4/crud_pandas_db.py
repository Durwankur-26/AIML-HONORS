
import pandas as pd
import os

class Employee:
    def __init__(self):
        if os.path.exists("employee.csv"):
            self.df = pd.read_csv("employee.csv")
        else:
            self.df = pd.DataFrame(columns=["id", "name", "salary"])

    def add(self):
        i = int(input("ID: "))
        n = input("Name: ")
        s = int(input("Salary: "))

        r = pd.DataFrame({
            "id": [i],
            "name": [n],
            "salary": [s]
        })

        self.df = pd.concat([self.df, r], ignore_index=True)
        self.df.to_csv("employee.csv", index=False)
        print("Added.")

    def display(self):
        print(self.df)

    def update(self):
        i = int(input("ID: "))
        s = int(input("New salary: "))

        if i in self.df["id"].values:
            self.df.loc[self.df["id"] == i, "salary"] = s
            self.df.to_csv("employee.csv", index=False)
            print("Updated.")
        else:
            print("Not found.")

    def delete(self):
        i = int(input("ID: "))

        if i in self.df["id"].values:
            self.df = self.df[self.df["id"] != i]
            self.df.to_csv("employee.csv", index=False)
            print("Deleted.")
        else:
            print("Not found.")

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
