import random

print(random.random())
print("------------------------")

print(random.randint(2,17))
print("------------------------")

print(random.uniform(1,4.5))
print("------------------------")

fruits = ["apple", "banana", "cherry"]
print(random.choice(fruits))  
print("------------------------")

fruits2 = ["apple", "banana", "cherry","mango"]
print(random.choices(fruits2, weights=[1, 10, 1,1], k=3))
print("------------------------")

cards = ["Ace", "King", "Queen", "Jack"]
random.shuffle(cards)
print(cards)
print("------------------------")

numbers = [1, 2, 3, 4, 5]
print(random.sample(numbers, 3))
print("------------------------")

random.seed(42)  # Set seed to 42
print(random.random())  # Always outputs the same number, e.g., 0.6394267984578837
print("------------------------")


