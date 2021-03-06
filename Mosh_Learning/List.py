letters = ["a", "b", "c"]
matrix = [[1, 2], [3, 4]]
zeros = [0] * 5
combined = zeros + letters
numbers = list(range(10))
chars = list("Hello")

print(combined)
print(numbers)
print(chars)

# Accessing Items
print(letters[0])
print(letters[0:3])
print(numbers[::2])  # every second letter

# List Unpacking
first, second, *other = numbers
print(first)
print(second)
print(other)

# Add
letters.append("d")
letters.insert(0, "-")  # remove on position 0
print(letters)

# Remove
letters.pop(0)
letters.remove("b")
print(letters)
