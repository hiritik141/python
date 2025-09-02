#Question 12: Python provides a built-in function filter (f, a) that returns items of the list a for which
#f(item) returns true. Provide an implementation for filter using list comprehensions
# Custom implementation of filter using list comprehension
def my_filter(f, a):
    return [item for item in a if f(item)]

if __name__ == "__main__":
  
    data = list(map(int, input("Enter numbers separated by space: ").split()))
    
 
    choice = input("Filter condition (even/odd/greater): ").strip().lower()
    
    if choice == "even":
        result = my_filter(lambda x: x % 2 == 0, data)
    elif choice == "odd":
        result = my_filter(lambda x: x % 2 != 0, data)
    elif choice == "greater":
        limit = int(input("Enter the limit: "))
        result = my_filter(lambda x: x > limit, data)
    else:
        result = data  
    
    print("Filtered result:", result)
