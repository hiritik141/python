#week2_OS_Q6_23103117

f = open("example.txt", "w")

f.write("Hello, this is the first line.\n")

lines = ["This is the second line.\n",
         "This is the third line.\n",
         "This is the fourth line.\n"]
f.writelines(lines)

f.close()   


f = open("example.txt", "r")

print("Reading entire file with read():")
print(f.read())   

f.close()



f = open("example.txt", "r")

print("\nReading line by line using readline():")
print(f.readline(), end="")   
print(f.readline(), end="")  
print(f.readline(), end="")   

f.close()
