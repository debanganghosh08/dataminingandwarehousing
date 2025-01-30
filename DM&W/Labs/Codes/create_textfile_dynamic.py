# Program to dynamically create a text file and display its contents

# Function to create the file dynamically
def create_transaction_file():
    with open("transactions2.txt", "w") as file:
        while True:
            transaction_id = input("Enter transaction id (or 'stop' to finish): ")
            if transaction_id.lower() == 'stop':
                break

            num_items = int(input("Enter number of items purchased in transaction: "))
            items = []
            for _ in range(num_items):
                item = input("Enter the item: ")
                items.append(item)

            # Write transaction to file
            file.write(f"{transaction_id}-" + " ".join(items) + "\n")

# Function to read and display the file contents
def display_transaction_file():
    try:
        with open("transactions2.txt", "r") as file:
            content = file.read()
            print("Contents of 'transactions2.txt':")
            print(content)
    except FileNotFoundError:
        print("Error: The file 'transactions2.txt' does not exist.")

# Main logic
if __name__ == "__main__":
    create_transaction_file()
    display_transaction_file()
