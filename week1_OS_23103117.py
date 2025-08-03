
numbers = input("Enter numbers separated by spaces: ")


numbers_list = numbers.split()


total = 0
count = 0
for num in numbers_list:
    total = total + int(num)
    count = count + 1


if count == 0:
    print("No numbers entered.")
else:
    average = total / count
    print("Average of the entered numbers is:", average)
