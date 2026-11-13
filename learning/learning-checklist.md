# PYTHON LEARNING CHECKLIST :

- scope: Python foundations through a reproducible, version-controlled data/API project
- use this as a start-to-finish checklist for the topics in this repository and the four new tooling topics
- existing code means a topic has been practiced; it doesn't automatically mean every task is mastered
- all boxes start unchecked so you can record what you can do independently
- complete a section when you can explain the behavior, run an example, change it and diagnose a simple failure
- command examples assume macOS/Linux; check the working directory before running them

## 1. Set up Python and the editor

- [ ] Check the interpreter version with `python3 --version` and identify the Python used by the editor.
- [ ] Run a `.py` file from the terminal and run a small expression in the Interactive Window.
- [ ] Print `os.getcwd()` in both places and explain any difference.
- [ ] Find the repository root, the `code/` examples and the `learning/` notes.
- [ ] Explain the difference between a file, directory, relative path and absolute path.
- [ ] Read an error traceback and locate the failing source line.

Practice: run a hello-world file, change its message and run it again from another directory.

## 2. Variables, datatypes and printing

Notes: [basics](basics.md).

- [ ] Assign names, ages, prices and boolean values to variables.
- [ ] Distinguish `int`, `float`, `str`, `bool` and `None`; inspect values using `type()`.
- [ ] Explain why indentation and colons matter for Python blocks.
- [ ] Write useful `#` comments and distinguish comments from multiline strings/docstrings.
- [ ] Use `+`, `-`, `*`, `/`, `//`, `%` and `**`; predict each result.
- [ ] Control precedence using parentheses and update values with `+=`.
- [ ] Join, repeat and format strings with f-strings.
- [ ] Use `upper`, `lower`, `title`, `strip`, `replace`, `find` and `count`.
- [ ] Explain why a string method's returned value may need assigning back.
- [ ] Control `print()` with `sep` and `end`; unpack a list into separate arguments with `*`.

Practice: print a formatted student summary and clean a user-supplied name without changing its original variable accidentally.

## 3. Conditions and loops

Notes: [control flow](basics.md).

- [ ] Compare values using `==`, `!=`, `<`, `<=`, `>` and `>=`.
- [ ] Combine conditions using `and`, `or` and `not`.
- [ ] Distinguish equality, identity and membership checks.
- [ ] Choose behavior using `if`, `elif` and `else`.
- [ ] Use a conditional expression to choose a value.
- [ ] Loop over values and use `range(start, stop, step)`.
- [ ] Predict which values are included when the stop argument is excluded.
- [ ] Explain why printing a duration doesn't make a loop wait.

Practice: classify temperatures and print a sequence using a non-default step.

## 4. Data structures

Notes: [data structures](data-structures.md).

- [ ] Choose a list, tuple, dictionary or set for a concrete problem.
- [ ] Create empty and populated collections and inspect their lengths.
- [ ] Index and slice lists/tuples using positive and negative indexes.
- [ ] Add, update, insert, pop and delete list items.
- [ ] Sort/reverse a list and explain how those operations differ.
- [ ] Use membership, counts and first-match indexes; handle a missing match.
- [ ] Create a list comprehension with a condition.
- [ ] Demonstrate aliasing with assignment and shared nested values in a shallow copy.
- [ ] Create a single-item tuple, unpack tuples and swap two values.
- [ ] Look up dictionary values using brackets and `.get()`; explain missing-key behavior.
- [ ] Update/delete dictionary entries and inspect keys, values and pairs.
- [ ] Access a value in a nested dictionary.
- [ ] Remove duplicates with a set and explain why the original order isn't guaranteed.
- [ ] Compare set `remove()` with `discard()` when an item is missing.
- [ ] Avoid variable names that hide built-ins such as `list`, `dict` or `sum`.

Practice: store student scores, update them and select unique names without assuming set order.

## 5. Functions and scope

Notes: [building programs](building-programs.md).

- [ ] Define and call a reusable function.
- [ ] Explain parameters versus arguments and positional versus keyword arguments.
- [ ] Provide defaults and override individual values at call time.
- [ ] Distinguish displaying a result with `print()` from returning it.
- [ ] Return multiple values and unpack the resulting tuple.
- [ ] Return a dictionary when results need names.
- [ ] Predict what a function without an explicit return value produces.
- [ ] Explain local and module-level variables using the scope example.
- [ ] Calculate a final price using tax and a fixed discount.

Practice: implement a calculator function, then change its inputs and explain each returned result.

## 6. Imports and initial dependency management

Notes: [external tools](external-tools.md) and [requirements](requirements.md).

- [ ] Import a whole module, selected names and an alias.
- [ ] Distinguish standard-library modules from installed third-party packages.
- [ ] Use `math`, `random`, `datetime`, `os` and `json` in small examples.
- [ ] Explain why a local file named `random.py` can cause import confusion.
- [ ] Understand what a virtual environment isolates.
- [ ] Create a practice environment with `python3 -m venv .venv` and activate it with `source .venv/bin/activate`.
- [ ] Install a package with `python -m pip install PACKAGE` in that environment.
- [ ] Install requirements with `python -m pip install -r requirements.txt`.
- [ ] Explain that `pip freeze` reports installed packages, rather than discovering imports used by the code.
- [ ] Diagnose a missing package by checking the selected interpreter before reinstalling it.

Practice: import pandas successfully in the same interpreter used by the editor.

## 7. Working directories and output folders

Notes: [practical Python](practical-python.md).

- [ ] Resolve paths containing child folders and `..` relative to the working directory.
- [ ] Compare `os.path.exists`, `isfile` and `isdir`.
- [ ] Join path components with `os.path.join()`.
- [ ] Create missing parent folders with `os.makedirs(..., exist_ok=True)`.
- [ ] Explain what happens if the intended directory path already refers to a file.
- [ ] Read a small text file and write a separate output using `with open(...)`, choosing an encoding and mode.
- [ ] Explain that writing with mode `"w"` replaces existing file contents.

Practice: save output after starting the script from a different directory and correct the path deliberately.

## 8. HTTP requests and JSON

Notes: [working with APIs](working-with-api.md).

- [ ] Identify a URL's domain, endpoint and query parameters.
- [ ] Send a GET request with `requests`, including query parameters and headers.
- [ ] Set a request timeout.
- [ ] Inspect status, headers, text and bytes without assuming that `print(response)` prints the body.
- [ ] Parse JSON into Python data and access a nested value.
- [ ] Explain why `.json()` doesn't make another network request.
- [ ] Check HTTP failure with `raise_for_status()` before relying on the body.
- [ ] Handle a response with invalid JSON or a missing expected key.
- [ ] Explain reverse geocoding and trace the place lookup in the weather app.
- [ ] Use the returned temperature together with its units rather than assuming a unit.

Practice: request weather for two locations and explain the data path from response to printed summary.

## 9. Pandas fundamentals

Notes: [pandas basics](pandas-basics.md).

- [ ] Construct a DataFrame from equally sized column lists.
- [ ] Load CSV, TSV, JSON and JSON Lines practice files using the right reader/options.
- [ ] Inspect `head`, `tail`, `sample`, `shape`, `columns`, `dtypes`, `info` and `describe`.
- [ ] Select one column as a Series and several columns as a DataFrame.
- [ ] Select rows/cells with `.iloc` and `.loc`; explain position versus label.
- [ ] Predict slicing endpoints for `.iloc` and label-based `.loc`.
- [ ] Filter using a boolean mask and use `.isin()` for exact matches.
- [ ] Count missing values and distinguish missing data from zero.
- [ ] Practice `fillna()` and `dropna()` on a copy; explain the information each choice changes or removes.
- [ ] Convert a date column using `pd.to_datetime()`.
- [ ] Save CSV with `index=False` and load it again to check the result.
- [ ] Explain why changing a CSV filename to `.xlsx` doesn't create an Excel workbook.
- [ ] Save real Excel output with `to_excel()` and an installed writer engine if needed.
- [ ] Calculate a row total and a grand total.

Practice: select high-CPU observations, count missing measurements and save a filtered CSV without overwriting the original.

## 10. Dates, data processing and charts

Notes: [working with data](working-with-data.md).

- [ ] Use `datetime`, `timedelta` and `strftime` to build a date range.
- [ ] Count calendar dates when both endpoints are included.
- [ ] Build a DataFrame from the weather response's parallel arrays.
- [ ] Confirm that the displayed dates, selected rows and chart period agree.
- [ ] Plot a line and label its title, axes and units.
- [ ] Plot minimum and maximum temperatures with a legend.
- [ ] Adjust markers, date-label rotation and layout for readability.
- [ ] Save the chart before displaying it and export the underlying table.

Practice: make a chart whose date range matches its title exactly, then verify it against the saved CSV.

## 11. Organise code into modules

Notes: [modules](organising-code-into-modules.md).

- [ ] Move reusable functions into `helpers.py` and import them into a main script.
- [ ] Explain module lookup separately from relative data-file paths.
- [ ] Write a short docstring that describes a helper's purpose.
- [ ] Keep numeric totals numeric and apply currency formatting only for display.
- [ ] Trace the sales workflow from input row through helper to grand total.
- [ ] Use `if __name__ == "__main__":` so importing a module doesn't automatically run its main workflow.

Practice: import a calculation helper into a second script without duplicating its implementation.

## 12. Error handling and debugging

Notes: [error handling](error-handling.md).

- [ ] Trigger and identify `ValueError`, `TypeError`, `ZeroDivisionError`, `KeyError` and `FileNotFoundError` in practice examples.
- [ ] Explain why `input()` returns text and convert it explicitly.
- [ ] Put input conversion inside the `try` block that is meant to handle its failure.
- [ ] Catch specific exceptions and display useful messages.
- [ ] Predict which statements are skipped after an exception.
- [ ] Explain when an exception propagates to the caller.
- [ ] Distinguish a calculated result from a failure path that returns `None`.
- [ ] Reproduce a failure with the smallest useful input before changing code.

Practice: accept two numbers, handle invalid input and zero division, then show a successful result.

## 13. Classes, state and inheritance

Notes: [classes](classes.md).

- [ ] Explain class, instance, attribute and method using the animal examples.
- [ ] Initialize attributes with `__init__` and explain what `self` refers to.
- [ ] Create two objects and confirm they hold independent instance state.
- [ ] Use default and keyword constructor arguments for configuration.
- [ ] Explain why the practice client classes don't yet make real API calls.
- [ ] Accumulate validation errors and return boolean results.
- [ ] Explain how returning an internal list allows callers to change that list.
- [ ] Print validation errors using argument unpacking, `sep` and `end`.
- [ ] Demonstrate name mangling and explain why double underscores don't secure an API key.
- [ ] Inherit parent methods and an initializer in a child class.
- [ ] Override a method and predict which implementation runs for each object.
- [ ] Print a returned string explicitly when running a script.

Practice: build two validators, cause an error in only one, then explain why their error lists differ.

## 14. Git and GitHub

Notes: [Git and GitHub](git-and-github.md).

- [ ] Explain local Git history versus a repository hosted on GitHub.
- [ ] Configure author identity and understand that authentication is separate.
- [ ] Choose `git init` for a new practice repository or clone an existing one.
- [ ] Identify working-tree, staged and committed changes using status and diffs.
- [ ] Stage selected files, inspect the staged diff and make a focused commit.
- [ ] Inspect history and explain why a commit isn't automatically uploaded.
- [ ] Add Python ignore rules and verify a rule with `git check-ignore -v`.
- [ ] Explain why adding an already tracked file to `.gitignore` doesn't untrack it.
- [ ] Create a feature branch, make a small change and push it.
- [ ] Open a pull request, inspect its diff/checks and merge it when ready.
- [ ] Update the local default branch after the merge.
- [ ] Explain fetch, fast-forward pull, push, upstream, branch and fork.
- [ ] Unstage an edit without deleting it and distinguish that from discarding the edit.
- [ ] Resolve a simple conflict in a disposable practice repository.

Practice: use the branch-to-pull-request workflow for a small documentation change. See the linked note's official references for command details.

## 15. Environment variables and secrets

Notes: [environment variables and secrets](environment-variables-and-secrets.md).

- [ ] Read a setting with `os.getenv()` and supply a non-secret default.
- [ ] Explain missing, empty and present values; validate a required key without printing it.
- [ ] Convert numeric and boolean settings from strings.
- [ ] Set a placeholder variable in the shell and explain inheritance by a child process.
- [ ] Install `python-dotenv` and load a specific `.env` file before reading values.
- [ ] Predict precedence when the same name exists in the shell and `.env`.
- [ ] Use consistent keys; fix the conceptual mismatch between `DATABASE` and `DATABASE_NAME`.
- [ ] Use presence checks instead of printing credential values.
- [ ] Share placeholder settings through `.env.example` and ignore real local `.env` files.
- [ ] Explain why plaintext files, environment variables and double underscores aren't encryption.
- [ ] Describe rotation/revocation as the first response to an exposed credential.

Practice: use placeholder credentials to test present, missing, empty and conflicting settings; observe only presence or validation messages.

## 16. Modern project management with uv

Notes: [uv](uv.md).

- [ ] Check `uv --version` and learn where to find installation instructions.
- [ ] Create a separate simple application using `uv init --no-package`.
- [ ] Distinguish project metadata, lockfile, interpreter preference and installed environment.
- [ ] Add an application dependency and a development dependency.
- [ ] Inspect the changes to `pyproject.toml` and `uv.lock`.
- [ ] Remove a dependency using uv rather than deleting installed files manually.
- [ ] Use `uv tree` to distinguish direct and transitive dependencies.
- [ ] Explain resolution with `uv lock` versus installation with `uv sync`.
- [ ] Run a script with `uv run python main.py` without manually activating the environment.
- [ ] Inspect the selected interpreter and ensure it satisfies the project and dependency requirements.
- [ ] Explain `--locked` versus `--frozen` and the default exact behavior of `uv sync`.
- [ ] Recreate the environment using the committed metadata and lockfile in a separate checkout.
- [ ] Practice a dependency upgrade and review the lockfile diff.
- [ ] Explain importing requirements into a project versus installing them with `uv pip`.

Practice: use `code/uv-starter/` as the reference, then reproduce its setup in a separate practice project.

## 17. Ruff formatting and linting

Notes: [Ruff](ruff.md).

- [ ] Add Ruff as a development dependency in the practice project.
- [ ] Explain linting separately from formatting.
- [ ] Run `uv run ruff check .` and interpret an unused-import diagnostic.
- [ ] Run `uv run ruff format --check .` to inspect layout without rewriting source files.
- [ ] Apply fixes, format the file and inspect the resulting Git diff.
- [ ] Add configuration to `pyproject.toml` and enable import organization.
- [ ] Explain why `ruff format` alone doesn't sort imports or check runtime correctness.
- [ ] Use a rule-specific explanation or suppression when appropriate.
- [ ] Configure the editor formatter and understand separate save actions.
- [ ] Run lint/format checks before committing; optionally add the same checks to CI.

Practice: introduce an unused import, bad spacing and a wrong calculation; explain which problems Ruff detects and which require behavioral checks.

## 18. Final project: weather summary from a fresh checkout

- [ ] Write a short project description: inputs, expected output, units and date range.
- [ ] Start a separate uv application and a Git feature branch.
- [ ] Declare only the packages the application needs; add Ruff as a development dependency.
- [ ] Put non-secret defaults in configuration and validate required credentials only if the chosen API needs them.
- [ ] Keep local secrets ignored and provide placeholder settings in `.env.example`.
- [ ] Separate request, validation, transformation and output functions into sensible modules.
- [ ] Request weather with query parameters, a timeout and HTTP error handling.
- [ ] Validate required response fields before building the DataFrame.
- [ ] Convert dates, select the intended period and handle missing values deliberately.
- [ ] Create output directories and save a CSV and labeled chart.
- [ ] Check an ordinary response, missing configuration, invalid coordinates, unavailable service and missing response fields.
- [ ] Check boundary dates and confirm zero measurements aren't treated as missing values.
- [ ] Compare a few transformed rows and chart points with the source response.
- [ ] Run the program and Ruff checks, then review the Git diff.
- [ ] Document exact setup and run commands, including the working directory and selected interpreter.
- [ ] Commit source, notes, configuration and lockfile; inspect the staged contents for secrets and generated clutter.
- [ ] Push the branch, review the pull request and merge when satisfied.
- [ ] In a fresh checkout, use `uv sync --locked`, configure local settings and reproduce the result.

Completion check: another person can follow the README from a fresh checkout, produce the expected output and identify a deliberate configuration failure without seeing a secret value.
