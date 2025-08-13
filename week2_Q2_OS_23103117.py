#week2_Q2_OS_23103117
#Question 2: Write a Python program that creates a dictionary with five key-value pairs, where the keys
#are the names of students and the values are their ages. Access and print the age of a specific student using
#their name as the key. Also, add a new student to the dictionary and print the updated dictionary.
#• Example
#o Age of the specific student: 20 (or the age of the student you accessed)
#o Updated dictionary: {'Alice': 21, 'Bob': 22, 'Charlie': 20, 'David': 23, 'Eve': 19, 'Frank': 24}
#(or your updated dictionary with the new student added)


students = {
    "Alice": 21,
    "Bob": 22,
    "Charlie": 20,
    "David": 23,
    "Eve": 19
}

print("Available students:", ", ".join(students.keys()))

student_name = input("Enter the student name to find age: ").capitalize()

if student_name in students:
    print("Age of the specific student:", students[student_name])
else:
    print(f"{student_name} not found in the dictionary.")

new_name = input("Enter new student name: ").capitalize()
new_age = int(input(f"Enter age of {new_name}: "))

students[new_name] = new_age

print("Updated dictionary:", students)
