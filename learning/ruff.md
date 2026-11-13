# FORMATTING AND LINTING WITH RUFF :

- formatting makes code layout consistent (spacing, quotes and line wrapping)
- linting detects selected code problems (unused imports, undefined names and more)
- Ruff provides separate commands for those jobs
- passing Ruff checks doesn't prove the program produces correct results

## Install in a project

Inside a uv project:

```bash
uv add --dev ruff
uv run ruff --version
```

- `--dev` records a development dependency
- without uv, install into an active virtual environment with `python -m pip install ruff`
- use one project's environment consistently; editor and terminal should use the intended tool version

The [Ruff tutorial](https://docs.astral.sh/ruff/tutorial/) covers installation, linting and automatic fixes.

## Check before changing code

```bash
uv run ruff check .
uv run ruff format --check .
```

- `.` means the current directory, subject to discovery and exclusions
- pass `main.py` instead to focus on one file
- `check` reports lint violations
- `format --check` reports formatting differences without rewriting files
- in an existing uv project, `uv run` can still synchronize its environment and lockfile

## Fix and format

```bash
uv run ruff check --fix .
uv run ruff format .
uv run ruff check .
git diff
```

- `--fix` applies available fixes allowed by the safety policy; some violations require manual edits
- unsafe fixes are opt-in; don't enable them without understanding the suggested change
- lint fixes first, then format, then inspect the diff and run the relevant program/tests
- formatting doesn't sort imports; enable the import rules for that

See the [linter](https://docs.astral.sh/ruff/linter/) and [formatter](https://docs.astral.sh/ruff/formatter/) references for the different behaviors.

## Configuration

Add this example to a practice project's `pyproject.toml`:

```toml
[tool.ruff]
line-length = 88

[tool.ruff.lint]
extend-select = ["I"]

[tool.ruff.format]
quote-style = "double"
```

- `extend-select` adds import rules (`I`) to the defaults
- `ruff check --fix` can organize imports with those rules enabled
- Ruff also supports `ruff.toml` or `.ruff.toml`; the section names differ outside `pyproject.toml`
- don't copy `[tool.ruff]` headings unchanged into a standalone `ruff.toml`
- line length is a formatting target; not every long string or comment can be automatically wrapped
- lint enforcement of line length is a separate rule (`E501`)

See [Ruff configuration](https://docs.astral.sh/ruff/configuration/) for rule selection and file discovery.

## Understand a diagnostic

```python
import os

print("Hello")
```

- if `os` is unused, the `F401` rule reports the unused import
- `F821` reports an undefined name
- use `uv run ruff rule F401` to read a rule explanation
- `# noqa: F401` suppresses that rule on a line when there is an intentional reason
- fix the cause first; avoid broad suppression just to make the output quiet

## Editor and automation

- install Astral's Ruff extension in VS Code and select it as the Python formatter
- enable format on save if desired; import organization and lint fixes are separate editor actions
- a continuous integration check can run `uv sync --locked`, `uv run ruff check .` and `uv run ruff format --check .`
- commit configuration and `uv.lock`; ignore `.ruff_cache/`
- start with one practice file before checking all older learning examples

## Practice check

- create an unused import and uneven spacing in a practice file
- predict what linting reports and what formatting changes
- run both checks, fix the file and confirm they pass
- add a wrong calculation that is valid Python; explain why Ruff alone may not catch it
