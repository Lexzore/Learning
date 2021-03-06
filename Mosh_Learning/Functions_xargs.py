# To use more then 2 arguments
def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


print(multiply(2, 3, 4, 5))


# Dictionary
def save_user(**user):
    print(user["name"])


save_user(id=1, name="Oliver", age=37)
