import random

# Program to generate 100 random integers in the range 1 to 50

def generate_random_numbers():
    random_numbers = [random.randint(1, 50) for _ in range(100)]
    print("100 Random Numbers between 1 and 50:")
    print(random_numbers)

if __name__ == "__main__":
    generate_random_numbers()
