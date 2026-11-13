# ORGANISING CODE INTO MODULES :

- a module is a Python file containing reusable definitions and code
- move shared helpers into a separate file
- keep the main workflow in `main.py`

## Importing local functions

- `helpers.py` defines `calculate_total()` and `format_currency()`
- `from helpers import calculate_total, format_currency` imports those functions
- call the imported functions directly by name
- Python must be able to find `helpers.py` on its module search path
- avoid filenames that clash with the libraries you import

## Helper functions

- `calculate_total(quantity, price)` returns `quantity * price`
- `format_currency(amount)` returns `f"${amount:,.2f}"`
- `,` adds thousands separators; `.2f` displays two decimal places
- `format_currency(1234.5)` returns `"$1,234.50"`
- the formatted result is a string; use the original numbers for calculations
- a string at the start of a function body is its docstring (documents the function)

## Sales workflow

- read `data/sales.csv` with pandas
- loop through `df.iterrows()` to get each row's quantity and price
- pass those values to `calculate_total()` and append the result to `totals`
- assign `df["total"] = totals` to add the column
- use `format_currency()` when displaying each product's total
- use `df["total"].sum()` to calculate the grand total

## Paths and output

- `data/sales.csv` is relative to the working directory
- the example expects to run from `code/organising-code-into-modules/`
- importing helpers and resolving data paths are separate operations
- `"-" * len("Sales Data:")` makes an underline matching the heading length
- `\n` starts a new line in printed text
