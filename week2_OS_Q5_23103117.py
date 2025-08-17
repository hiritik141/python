def lensort(lst):
    return sorted(lst, key=len)

def extsort(files):
    return sorted(files, key=lambda x: x.split(".")[-1])

print("Choose an option:")
print("1. Sort strings by length (lensort)")
print("2. Sort files by extension (extsort)")

choice = int(input("Enter your choice (1 or 2): "))

if choice == 1:
    n = int(input("Enter number of strings: "))
    lst = []
    for i in range(n):
        word = input(f"Enter string {i+1}: ")
        lst.append(word)
    print("Original List:", lst)
    print("Sorted by Length:", lensort(lst))

elif choice == 2:
    m = int(input("Enter number of files: "))
    files = []
    for i in range(m):
        fname = input(f"Enter file name {i+1} (with extension): ")
        files.append(fname)
    print("Original Files:", files)
    print("Sorted by Extension:", extsort(files))

else:
    print("Invalid choice!")
