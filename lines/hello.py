def count_lines(file_path):
    """Count the number of non-empty lines in a Python file."""
    try:
        with open(file_path, 'r') as file:
            lines = [line.strip() for line in file.readlines() if line.strip() and not line.strip().startswith("#")]
            return len(lines)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return -1


#

    #


    #


    except Exception as e:
        print(f"An error occurred: {e}")
        return -1
# Example usage
file_path = input("Enter the path to the Python file: ")
line_count = count_lines(file_path)

if line_count != -1:
    print(f"The number of non-empty lines in '{file_path}' is: {line_count}")