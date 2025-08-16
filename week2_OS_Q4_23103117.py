#week2_OS_Q4_23103117
#Question 4: Write a function group (list, size) that takes a list and splits into smaller lists of given size.


def group(lst, size):
    result = []
    for i in range(0, len(lst), size):
        result.append(lst[i:i+size])
    return result


n = int(input("Enter how many elements you want in the list: "))
lst = []
for i in range(n):
    element = int(input(f"Enter element {i+1}: "))
    lst.append(element)

size = int(input("Enter group size: "))

print("Original List:", lst)
print("Grouped List:", group(lst, size))
