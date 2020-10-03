for a in range(100):
    if a % 15 == 0:
        print("FizzBuzz")
        continue
    elif a % 3 == 0:
        print("Fizz")
        continue
    elif a % 5 == 0:
        print("Buzz")
        continue
    print(a)

