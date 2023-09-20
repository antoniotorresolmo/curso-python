for contador in range(100):
    if contador % 3 == 0 and contador % 5 == 0:
        print("FizzBuzz")
    elif contador % 3 == 0:
        print("Fizz")
    elif contador % 5 == 0:
        print("Buzz")
    else:
        print(contador)