# Pandas file practice

All data is fictional. Each file has 12 server observations and the same seven columns.

- `instance` (server ID; repeats across dates)
- `region` (server location)
- `date` (observation date, YYYY-MM-DD)
- `cpu`, `memory` (usage percentages, 0 to 100)
- `requests` (request count for that observation)
- `active` (whether the server is running)

## Reading files

Run this from the project root, including in the VS Code Interactive Window:

```python
from pathlib import Path
import pandas as pd

files = Path("code/pandas-playground/files")

csv_df = pd.read_csv(files / "server-metrics.csv", parse_dates=["date"])
tsv_df = pd.read_csv(files / "server-metrics.tsv", sep="\t", parse_dates=["date"])
json_df = pd.read_json(files / "server-metrics.json", orient="records")
jsonl_df = pd.read_json(files / "server-metrics.jsonl", lines=True)
missing_df = pd.read_csv(files / "server-metrics-missing.csv")

print(csv_df.head())
print(csv_df.shape)
print(csv_df.dtypes)
print(missing_df.isna().sum())
```

Relative paths start from your current working directory. If the files are not found, check `Path.cwd()` and adjust `files`.

## Practice

- Compare the clean CSV, TSV, JSON and JSON Lines datasets: their values match.
- Read only `instance`, `cpu` and `memory` with `usecols` in `read_csv()`.
- Read the first five CSV rows with `nrows=5`.
- Filter observations where CPU usage is above 80.
- Find average memory usage by region.
- Find the four missing cells in the missing-values CSV; try `fillna()` or `dropna()`.
- Compare a missing measurement with the valid zero measurements for the inactive server.

JSON is one array of records. JSON Lines stores one JSON object per line and needs `lines=True`.
