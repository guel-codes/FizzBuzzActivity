# FizzBuzzActivity
 Python Learning Club Activity for Github

## Files created
- helpers.py
- fizzbuzz.py

### helpers.py
```python
def fizzbuzz(list_):
    for number in list_:
        if number % 3 == 0 and number % 5 == 0:
            print(f"FizzBuzz")
        elif number % 3 == 0:
            print(f"Fizz")
        elif number % 5 == 0:
            print(f"Buzz")
        else:
            print(number)
            
``` 
### fizzbuzz.py
```python
from helpers import fizzbuzz
my_list = [1,2,3,5,7,9,15,45]

def test_fizzbuzz():
    fizzbuzz(my_list)

test_fizzbuzz()
```
# Requirements/Tests:
- Prints "Fizz" for numbers in list divisible by 3
- Prints "Buzz" for numbers in list divisible by 5
- Prints "FizzBuzz" for numbers in list divisible by 3 & 5
- Prints out numbers if it is not divisible by 3,5 or 3 & 5

