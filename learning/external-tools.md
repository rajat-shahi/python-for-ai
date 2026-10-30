# EXTERNAL TOOLS :

- import modules to reuse existing code
- standard library modules come with Python
- external packages need to be installed separately

## Import patterns

- `import math` then `math.sqrt(25)` (import the module)
- `from math import sqrt, pi, pow` (import specific names)
- `import pandas as pd` (import with an alias)
- `import random as rm` (use `rm` as the module name)
- avoid `from module import *`; it makes names harder to track and can cause conflicts

## Standard library examples

- `math.sqrt(25)` (square root; returns `5.0`)
- `math.pow(2, 5)` (power; returns `32.0`)
- `datetime.date.today()` (current local date)
- `os.getcwd()` (current working directory)
- `json.dumps(data)` (convert a Python object, such as a dictionary, to a JSON string)

## Random choices

- `rm.randint(1, 10)` (random integer; both endpoints included)
- `rm.choice(["heart", "diamond", "spade"])` (choose one item)
- `num == 1 and choice == "diamond"` (both conditions must match to win)

## Installing external packages

- `python -m pip install pandas numpy matplotlib` (install packages for that Python interpreter)
- `python -m pip install package_name==version` (install a specific version)
- install before importing; a missing package can cause `ModuleNotFoundError`
- see [requirements notes](requirements.md) for saving and installing project dependencies

## Pandas

- `import pandas as pd`
- use a dictionary with column names as keys and lists of values as columns
- `df = pd.DataFrame(data)` (create a table)
- column lists in this example must have the same number of items
- `print(df)` (display the table with row indexes)

## Requests

- `import requests`
- `response = requests.get("https://api.github.com")` (send an HTTP GET request)
- `response.status_code` (HTTP status code; `200` means OK)
- `response.content` (response body as bytes)
- the example uses `response._content`; prefer the public `response.content` attribute
- this example needs an internet connection and the `requests` package

## Naming conflicts

- avoid overwriting imported module names
- after `import datetime`, assigning `datetime = "2026-01-01"` hides the module name
- use `date_text` or `today` for your own values instead
- avoid script names like `random.py` or `pandas.py` when importing those modules
