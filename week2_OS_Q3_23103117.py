#week2_OS_Q3_23103117
def duplicate(numbers):
    duplicates = []
    seen = set()

    for num in numbers:
        if num in seen and num not in duplicates:
            duplicates.append(num)
        else:
            seen.add(num)
    return duplicates


# Example usage:
nums = []
print("Enter 10 integers:")
for _ in range(10):
    nums.append(int(input()))

result = duplicate(nums)
print("Duplicates:", result if result else "No duplicates found")
