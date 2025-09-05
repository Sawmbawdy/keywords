inpu = str(input("Enter your word: "))
for i in inpu:
    if i == "A" or i == "a":
        print("Found an", i)
    else:
        print("Found an", i, "instead")