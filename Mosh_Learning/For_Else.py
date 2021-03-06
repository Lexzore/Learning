successfull = False

for number in range(1, 4):
    print("Attempt", number, number * ".")
    if successfull:
        print("Successfull")
        break
else:
    # execute if for loop dont break
    print(f"Attempted {number} times and failed.")
