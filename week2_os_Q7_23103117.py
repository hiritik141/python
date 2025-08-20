#week2_os_Q7_23103117
#Question 7: Write a function to compute the number of characters, words and lines in a file.
def file_stats(filename):
    with open(filename, "r") as f:
        text = f.read()

    num_chars = len(text)                  
    num_words = len(text.split())         
    num_lines = text.count("\n") + 1 if text else 0   

    return num_chars, num_words, num_lines


filename = input("Enter file name: ")

try:
    chars, words, lines = file_stats(filename)
    print("Characters:", chars)
    print("Words:", words)
    print("Lines:", lines)
except FileNotFoundError:
    print("Error: File not found! Please check the file name or path.")
