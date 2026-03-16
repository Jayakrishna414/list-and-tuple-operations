# LIST AND TUPLE - ALL IN ONE EXAMPLE

print("----- LIST OPERATIONS -----")

# Creating a list
numbers = [10, 20, 30, 40, 50]
print("Original List:", numbers)

# Access element
print("First element:", numbers[0])

# Add element
numbers.append(60)
print("After append:", numbers)

# Insert element
numbers.insert(2, 25)
print("After insert:", numbers)

# Remove element
numbers.remove(40)
print("After remove:", numbers)

# Length of list
print("Length of list:", len(numbers))

# Loop through list
print("List elements:")
for num in numbers:
    print(num)

print("\n----- TUPLE OPERATIONS -----")

# Creating a tuple
fruits = ("apple", "banana", "mango", "orange")
print("Tuple:", fruits)

# Access element
print("First fruit:", fruits[0])

# Length of tuple
print("Length of tuple:", len(fruits))

# Loop through tuple
print("Tuple elements:")
for fruit in fruits:
    print(fruit)

print("\n----- LIST OF TUPLES -----")

# List of tuples
students = [("Krishna", 85), ("Ravi", 78), ("Anu", 92)]

for name, marks in students:
    print(name, "scored", marks)

print("\n----- TUPLE TO LIST CONVERSION -----")

# Convert tuple to list
t = (1, 2, 3, 4)
l = list(t)

# Add element
l.append(5)

print("Converted list:", l)
