def fizzbuzz(list_):
    for number in list_:
        if number % 3 == 0 and number % 5 == 0:
            print(f"FizzBuzz")
        elif number % 3 == 0:
            print(f"Fizz")
        elif number % 5 == 0:
            print(f"Buzz")
        else:
            pass
    
    