import random
import string

# Function to generate a random transaction ID
def generate_transaction_id():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

# Function to generate random items
def generate_items():
    items = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    return random.sample(items, k=random.randint(3, len(items)))

# Function to create the transactions file
def create_large_transaction_file():
    with open("transactions3.txt", "w") as file:
        for _ in range(10000):
            transaction_id = generate_transaction_id()
            items = generate_items()
            file.write(f"{transaction_id}-" + " ".join(items) + "\n")

    print("File 'transactions3.txt' with 10,000 transactions created successfully.")

if __name__ == "__main__":
    create_large_transaction_file()
