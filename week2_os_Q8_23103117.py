#week2_os_Q8_23103117
#Question 8: Write a program named ‘reverse.py’ to print lines of a file in reverse order.
# reverse.py

def reverse_file(filename):
    with open(filename, "r") as f:
        lines = f.readlines()  

    # Print lines in reverse order
    for line in reversed(lines):
        print(line.strip())    


filename = input("Enter file name: ")

try:
    reverse_file(filename)
except FileNotFoundError:
    print("Error: File not found! Please check the file name or path.")
