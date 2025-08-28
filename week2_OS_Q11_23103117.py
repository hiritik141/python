#week2_OS_Q11_23103117
# Custom implementation of map using list comprehension
def my_map(func, iterable):
    return [func(x) for x in iterable]


nums = [1, 2, 3, 4, 5]

squares = my_map(lambda x: x ** 2, nums)
print("Squares:", squares)

as_str = my_map(str, nums)
print("As strings:", as_str)

doubles = my_map(lambda x: x * 2, nums)
print("Doubles:", doubles)
