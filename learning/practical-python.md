# PRACTICAL PYTHON :

- working directories and file paths
- check whether files and folders exist
- create folders before saving output

## Current working directory

- `import os`
- `os.getcwd()` (directory Python is currently working from)
- relative paths are resolved from this directory, not automatically from the script's folder
- running a script from the terminal and running it in the Interactive Window can use different working directories

## File paths

- `data/sample.txt` (file in a child folder of the working directory)
- `..` (go up one directory)
- `../../sample-data1.txt` (go up two directories, then look for the file)
- an absolute path starts from the filesystem root
- `os.path.join("data", "sample.txt")` (combine path parts)
- the examples using `files/...` or `data/...` expect the relevant example folder as the working directory

## Checking paths

- `os.path.exists(path)` (a file or directory exists)
- `os.path.isdir(path)` (path exists and is a directory)
- `os.path.isfile(path)` (path exists and is a file)
- `exists()` alone doesn't tell us whether a path is a folder
- `sales-analysis/analyser.py` currently checks the CSV path; it doesn't yet calculate sales totals

## Creating output directories

- `os.makedirs("output", exist_ok=True)` (create the folder and missing parents)
- `exist_ok=True` allows an existing directory; a file at that path still causes an error
- no separate existence check is needed before this call
- creating a directory doesn't create the output file

```python
import os

os.makedirs("output", exist_ok=True)
output_path = os.path.join("output", "server-metrics.csv")
df.to_csv(output_path, index=False)
```

- `df` above is an existing DataFrame
- see [pandas basics](pandas-basics.md) for reading and saving data
