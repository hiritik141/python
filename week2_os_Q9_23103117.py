#week2_os_Q9_23103117
# Program to print each line of a file in reverse order

filename = input("Enter the file name: ")

try:
    with open(filename, "r") as f:
        lines = f.readlines()

    print("\nReversed lines:\n")
    for line in lines:
        print(line.strip()[::-1])  

except FileNotFoundError:
    print("File not found! Please check the file name.")
