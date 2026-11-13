# ERROR HANDLING :

- an exception interrupts normal execution when an operation fails
- `try` runs code that may fail
- `except` handles a matching exception

## Try and except

```python
try:
    result = 10 / 0
    print(result)
except ZeroDivisionError:
    print("You can't divide a number by zero")
```

- when an exception occurs, the remaining statements in that `try` block are skipped
- Python looks for a matching handler
- after a handled exception, execution continues after the `try`/`except` statement
- an unhandled exception propagates to the caller and can stop the program
- prefer specific exceptions over a bare `except:` so unrelated failures remain visible

## Errors in the examples

- `ZeroDivisionError` (divide a number by zero)
- `ValueError` (for example, `int("hello")`)
- `TypeError` (for example, adding a string to an integer)
- `input()` returns a string, even when the user types digits
- use `int(input(...))` when an integer is required

## Where the try block belongs

- `catching-error.py` passes the raw age string to `age_increment()`
- `age + 10` therefore raises `TypeError`; its `except ValueError` doesn't catch that error
- `int(input(...))` for `num` currently runs before the function call
- conversion errors there are outside the function's `try` block
- put both conversion and the risky arithmetic inside the block that should handle them

```python
try:
    age = int(input("Enter your age: "))
    num = int(input("Enter a number: "))
    print(f"In 10 years you'll be {age + 10}")
    print(age / num)
except ValueError:
    print("Please enter whole numbers")
except ZeroDivisionError:
    print("You can't divide a number by zero")
```

## Functions and errors

- `divide(a, b)` can return a result or raise an exception
- a caller can handle exceptions raised inside another function
- in `main.py`, successful division returns a number; its failure handler only prints a message
- that failure path implicitly returns `None`
- catch errors where you can decide what should happen next
