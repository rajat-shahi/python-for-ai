# PANDAS BASICS :

- `import pandas as pd`
- a DataFrame is a table with rows, columns and an index
- `df = pd.DataFrame(data)` (create a table from a dictionary of column lists)
- column lists must have the same length
- examples are in `code/pandas-basics-playground/`

## Reading files

- `pd.read_csv("files/server-metrics.csv")` (comma-separated data)
- `pd.read_csv("files/server-metrics.tsv", sep="\t")` (tab-separated data)
- `pd.read_json("files/server-metrics.json")` (JSON array of records)
- `pd.read_json("files/server-metrics.jsonl", lines=True)` (one JSON object per line)
- paths above assume the working directory is `code/pandas-basics-playground/`
- `parse_dates=["date"]` in `read_csv()` converts the date column while loading
- blank CSV fields are normally read as missing values
- a missing measurement is different from a valid measurement of zero

## Exploring data

- `df.head()` (first five rows), `df.tail()` (last five rows)
- `df.sample(5)` (five randomly selected rows)
- `df.shape` (tuple containing row count and column count)
- `rows, columns = df.shape` (unpack the counts)
- `df.columns` (column labels), `df.dtypes` (column datatypes)
- `df.info()` (prints columns, non-null counts and datatypes; returns `None`)
- `df.describe()` (summary statistics; numeric columns by default when present)
- `df.isna().sum()` (count missing values per column)
- scripts need `print(df.head())` to display the returned table; an Interactive Window can display an expression directly

## Selecting columns

- `df["instance"]` (one column as a Series)
- `df[["instance", "cpu", "memory"]]` (multiple columns as a DataFrame)
- the inner list holds column names; the outer brackets select them

## Selecting rows and cells

- `.iloc` selects by integer position
- `df.iloc[0]` (first row)
- `df.iloc[1:3]` (positions `1` and `2`; stop excluded)
- `df.iloc[2, 3]` (third row, fourth column)
- `.loc` selects by row and column labels
- `df.loc[0]` (row labeled `0`; not always the first row)
- `df.loc[0:2, ["instance", "cpu", "memory"]]` (labels `0` through `2`, inclusive, on this default index)
- numeric index labels and row positions can look identical until the index changes

## Filtering rows

- `df["cpu"] > 80` creates a boolean mask (one True/False result per row)
- `df[df["cpu"] > 80]` selects rows where the condition is True
- `df[df["instance"].isin(["ins-3", "ins-5"])]` selects matching server IDs
- `.isin()` uses exact matches; `isn-5` doesn't match `ins-5`
- missing CPU measurements don't pass the `> 80` filter in this example

## Saving files

- `df.to_csv("output/server-metrics.csv", index=False)` (save CSV without an extra index column)
- create the output directory first with `os.makedirs("output", exist_ok=True)`
- `to_csv()` writes CSV even if the filename ends with `.xlsx`
- use `df.to_excel("output/server-metrics.xlsx", index=False)` for a real Excel workbook
- Excel export needs an appropriate writer engine installed, such as `openpyxl`
- the existing `.xlsx` output made with `to_csv()` contains CSV text

## Calculations used in the sales example

- `df.iterrows()` yields an index label and row Series for each row
- calculate `quantity * price` per row and collect the results in a list
- `df["total"] = totals` (add the calculated column)
- `df["total"].sum()` (grand total)
- see [modules](organising-code-into-modules.md) for the helper functions
