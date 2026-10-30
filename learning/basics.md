# Basic Programming language operations :

- store information (variables)
- make decisions (if-else)
- repeat actions (loops)
- calculate things (operators)

## Important rules in Python :

- syntax (rules for writing valid Python code)
- indentation (groups code into blocks; Python doesn't use curly braces like C++)
- use a colon before the indented block of a condition, loop or function

## Variables

- used to store information
- `name = "rajat"`
- `age = 26`
- `type(value)` (find the datatype of a value)

## Comments

- use `#` for comments
- triple quotes create multiline strings; they can be used as docstrings, but are not comments
- good comments explain WHY, not just WHAT

## Datatypes

- integers (whole numbers without decimals)
- floats (numbers with decimal points)
- strings (text)
- booleans (`True` or `False`)
- `can_vote = age >= 18` (store the result of a comparison)

## Numbers

- `+` (addition), `-` (subtraction), `*` (multiplication)
- `/` (division), `//` (floor division), `%` (remainder), `**` (power)
- `10 / 7` gives a float; `10 // 7` gives `1`
- Python follows operator precedence; use parentheses to control calculation order

## Strings

- text inside single or double quotes
- triple quotes for multiline strings
- `first_name + " " + last_name` (join strings)
- `"-" * 30` (repeat a string)
- `len(text)` (number of characters)
- `f"Hello, {first_name}"` (insert values into text)
- raw strings keep backslashes literal: prefix the opening quote with `r`

## String methods

- `text.upper()`, `text.lower()`, `text.title()` (change case)
- `text.strip()` (remove whitespace from both ends)
- `price.strip("$")` (remove dollar signs from both ends only)
- `price.replace("$", "")` (remove dollar signs throughout the string)
- `text.startswith("I")`, `text.endswith("Python")` (return a boolean)
- `text.find("Python")` (first matching index; `-1` if not found)
- `text.count("Python")` (count matches)
- matching is case-sensitive (`python` and `Python` are different)
- strings are immutable; save the result: `text = text.replace("Python", "JavaScript")`

## Operators

- arithmetic (basic math operations)
- assignment (assign or update variable values)
  - `score += 5` (same as `score = score + 5` for numbers)
- comparison (compare values and return a boolean)
  - `==`, `!=`, `>`, `>=`, `<`, `<=`
- logical (combine and evaluate conditions)
  - `and` (both conditions), `or` (either condition), `not` (reverse truth value)
- bitwise (perform bit-by-bit operations on integers)
- identity: `is`, `is not` (check whether variables refer to the same object)
  - `x is y`
- membership: `in`, `not in` (check whether a value exists in a collection or string)
  - `'a' in 'apple'`

## Control flow

- `if`, `else` (choose between two paths)
- `if`, `elif`, `else` (check multiple conditions in order)
- `"Adult" if can_vote else "Minor"` (choose a value using a condition)
- `for i in range(5):` (repeat for `0, 1, 2, 3, 4`)
- `for i in range(1, 6):` (repeat from `1` to `5`)
- `for i in range(0, 11, 2):` (repeat from `0` to `10`, step of `2`)
- `range(start, stop, step)` excludes the stop value
- printing `1sec`, `2sec`, etc. does not actually pause the loop

## Printing

- `print(value)` (display a value)
- `print(first_name, last_name, sep="|")` (separator between arguments)
- `print("Hello", end=" ")` (change the ending; default is a newline)
