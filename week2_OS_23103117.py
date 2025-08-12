#week2_OS_23103117
#1: Create a Python program that initializes a list of five different fruits. Use indexing to print
#the first and last fruit from the list. Then, use slicing to print the middle three fruits.


fruits = []


print("Enter the names of 5 different fruits:")
for i in range(5):
    fruit = input(f"Fruit {i+1}: ")
    fruits.append(fruit)


print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])


print("Middle fruits:", fruits[1:4])

