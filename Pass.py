inpu = int(input("How many numbers?:  "))

for i in range(inpu + 1):
    if i % 20 == 0:
        print("Twist -- Is divisible by 20 -- ", i)
    if i == 0:
        pass
    if i % 5 == 0:
        print("Fizz -- Is divisible by 5 -- ", i)
    if i % 3 == 0:
        print("Buzz -- Is divisible by 3 -- ", i)
    else:
        print(i)