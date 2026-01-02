import json
import os
import matplotlib.pyplot as plt

FILE_NAME = "students.json"

def load_data():
    if not os.path.exists(FILE_NAME):
        return []

    with open(FILE_NAME, "r") as file:
        return json.load(file)


def save_data(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)
        

def calculate_average(marks):
    if not marks:
        return 0
    return sum(marks) / len(marks)


def assign_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 60:
        return "C"
    else:
        return "Fail"


def validate_marks(marks):
    for m in marks:
        if m < 0 or m > 100:
            return False
    return True


def plot_individual_trend():
    data = load_data()

    name = input("Enter student name for trend analysis: ")
    found=False
    for student in data:
        if student["name"].lower() == name.lower():
            marks = student["marks"]
            tests = [f"Test {i+1}" for i in range(len(marks))]

            plt.figure()
            plt.plot(tests, marks, marker='o')
            plt.xlabel("Tests")
            plt.ylabel("Marks")
            plt.title(f"Performance Trend - {student['name']}")
            plt.ylim(0, 100)
            plt.grid()

            plt.show()
            found=True
            break
        
    if not found:
        print("Student not found.")
    

def add_student():
    name = input("Enter student name: ")

    marks = list(map(int, input("Enter marks separated by space: ").split()))

    if not validate_marks(marks):
        print("Invalid marks entered!")
        return

    avg = calculate_average(marks)
    grade = assign_grade(avg)

    student = {
        "name": name,
        "marks": marks,
        "average": round(avg, 2),
        "grade": grade
    }

    data = load_data()
    data.append(student)
    save_data(data)

    print("Student record added successfully!")


def view_students():
    data = load_data()
    if not data:
        print("No records found.")
        return

    for s in data:
        print(s)

def report_students():
    data=load_data()
    name=input("Enter the name of student: ")
    found=False
    for student in data:
        if student['name'].lower()==name.lower():
            if 0<=student['average']<35:
                print(f"{student['name']} needs to improve a lot!")
            elif 35<=student['average']<65:
                print(f"{student['name']} should practice more")
            elif 65<=student['average']<85:
                print(f"{student['name']} is doing well...do more hardwork ")
            else :
                print(f"You are awesome!Keep going!!")


def main():
    while True:
        print("\n1. Add Student")
        print("2. View Records")
        print("3. Visualize Performance")
        print("4. Provide Report")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            plot_individual_trend()
        elif choice=="4":
            report_students()
        elif choice =="5":
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
