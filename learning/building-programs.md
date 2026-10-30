# BUILDING PROGRAMS :

- functions (reusable blocks of code)
- DRY (Don't Repeat Yourself)
- parameters, arguments, return values and scope

## Creating and calling functions

- `def` defines a function; use a colon and indent its body
- `def say_hello():` (function without parameters)
- `say_hello()` (call the function)
- `pass` is a placeholder that does nothing; it does not stop the function

## Parameters and arguments

- parameters are names in the function definition: `def add(x, y):`
- arguments are values passed when calling it: `add(10, 15)`
- positional arguments match the order of parameters
- keyword arguments use parameter names: `greet(last_name="shahi", first_name="rajat")`
- keyword arguments can be written in a different order

## Default values

- `def total(b, c, a=10):` (use `10` when `a` is omitted)
- `total(5, 10)` uses the default; `total(5, 10, 15)` overrides it
- required parameters come before parameters with defaults in these examples
- avoid naming a function `sum`; it hides Python's built-in `sum()`

## Return values

- `return` sends a result back and exits the function
- `print()` displays a value; it does not return that value to the caller
- a function without an explicit return value returns `None`
- `return result, x, y` (return a tuple of three values)
- `res, num1, num2 = add(10, 15)` (unpack the returned tuple)
- `return dict(add=add, diff=diff, mul=mul, div=div)` (return named results in a dictionary)
- conditions can return different results, like `Hot`, `Moderate` or `Cold`

## Calculation examples

- `calculate(x, y)` returns addition, subtraction, multiplication and division results
- `y` must not be zero when calculating `x / y`
- `tax = price * tax_rate`
- `final_price = price + tax - discount`
- `calculate_total(100, 0.08, 10)` prints a total of `98.0`
- `0.08` means 8% tax; the discount in this example is a fixed amount
- `calculate_total(price=200, tax_rate=0.08, discount=10)` (keyword arguments)
- this example prints the total; add a `return` if another part of the program needs the value

## Variable scope

- a variable defined at module level is global to that module
- a variable assigned inside a function is local to that function by default
- a local variable can have the same name as a global variable
- in the example, `value = 20` inside `scope()` does not change the outer `value = 10`
- the function prints `20`; printing the global value afterwards gives `10`
