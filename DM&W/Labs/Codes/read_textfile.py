# Program to read and display the contents of 'transactions.txt'

try:
    # Open the file in read mode
    with open("transactions.txt", "r") as file:
        # Read and display the contents of the file
        content = file.read()
        print("Contents of 'transactions.txt':")
        print(content)
except FileNotFoundError:
    print("Error: The file 'transactions.txt' does not exist.")
