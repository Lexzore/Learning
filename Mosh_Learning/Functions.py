# 1- Perform a task
def greet(first_name, last_name):
    print(f"Hi {first_name} {last_name}")
    print("Welcome on board. \n ")


# 2- Return a value to save in a variable
def get_greeting(name):
    return f"Hi {name}"


# Arguments
greet("Oliver", "Tepper")
greet("Johanna", "Meyer-Oerthling")


message = get_greeting("Oliver")
print(message)

# Write to a file
file = open("content.txt", "w")
file.write(message)


# Set default Arguments(number, by=1)
def increment(number, by):
    return number + by


# Keyword Arguments
print(increment(number=1, by=7))  # Python makes a hiden save variable
