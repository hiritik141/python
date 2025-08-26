import sys
import textwrap

def wrap_file(filename, width):
    try:
        with open(filename, 'r') as f:
            for line in f:
                # Remove trailing newline before wrapping
                wrapped_lines = textwrap.wrap(line.strip(), width=width)
                for wrapped_line in wrapped_lines:
                    print(wrapped_line)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python wrap.py <filename> <width>")
    else:
        filename = sys.argv[1]
        try:
            width = int(sys.argv[2])
            wrap_file(filename, width)
        except ValueError:
            print("Width must be an integer.")
