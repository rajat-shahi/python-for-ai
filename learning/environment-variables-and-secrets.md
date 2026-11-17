# ENVIRONMENT VARIABLES AND SECRETS :

- environment variables are string settings available to a running process
- use them for configuration that changes between machines or environments
- examples: database name, API key, timeout and debug setting
- a secret grants access; keep its value out of source code and logs

## Read values in Python

```python
import os

database = os.getenv("DATABASE_NAME", "practice_db")
api_key = os.environ.get("API_KEY")

if not api_key:
    raise ValueError("Set API_KEY before running the application")

print(f"Using database: {database}")
print("API key configured:", bool(api_key))
```

- `os.getenv("NAME")` and `os.environ.get("NAME")` return `None` when missing, unless a default is supplied
- `os.environ["NAME"]` raises `KeyError` when missing
- an empty string is different from a missing variable; `if not api_key` rejects both
- a default is useful for a non-secret setting; don't provide a real fallback secret
- convert types explicitly: `timeout = int(os.getenv("TIMEOUT_SECONDS", "10"))`
- `bool("false")` is True because it is non-empty; parse boolean text explicitly
- example: `debug = os.getenv("DEBUG", "false").lower() == "true"`

See Python's [`os.environ` and `os.getenv` documentation](https://docs.python.org/3/library/os.html#os.environ).

## Set variables in the terminal

macOS/Linux shell examples; these use placeholder values:

```bash
export DATABASE_NAME="practice_db"
export API_KEY="placeholder-only"
python code/environment-variables/main.py
unset API_KEY
```

- exported variables are inherited by programs started from that shell
- another already-running terminal or Interactive Window may have a different environment
- setting `os.environ["NAME"]` changes the current process and future child processes; it doesn't change the parent shell
- changing configuration files doesn't automatically update a running process

## Load a local .env file

- Python doesn't automatically load `.env` files
- install `python-dotenv` in the environment that runs your script
- pip workflow: `python -m pip install python-dotenv`
- uv project workflow: `uv add python-dotenv`
- package name is `python-dotenv`; import name is `dotenv`

Example `.env` content, using placeholders:

```dotenv
API_KEY=replace-with-your-local-key
DATABASE_NAME=practice_db
TIMEOUT_SECONDS=10
DEBUG=false
```

```python
import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv(Path(__file__).resolve().parent / ".env")
api_key = os.getenv("API_KEY")
```

- this explicit path loads `.env` beside the script, independent of the working directory
- `__file__` is available in scripts; interactive input may not define it
- `load_dotenv()` without a path searches for a file; an explicit path makes the intended file clear
- existing environment values win by default; `override=True` changes that behavior deliberately
- call the loader before reading values

See the [python-dotenv guide](https://bbc2.github.io/python-dotenv/) for loading and precedence.

## Your current examples

- [main.py](../code/environment-variables/main.py) reads `API_KEY` and `DATABASE_NAME` from the process environment
- [env-file.py](../code/environment-variables/env-file.py) loads `.env` and reads `API_KEY` and `DATABASE`
- `DATABASE` and `DATABASE_NAME` are different keys; use consistent names in the code and configuration
- `env-file.py` reports whether the API key is configured without printing its value
- changing a `.env` entry means loading it again in a fresh process, or deliberately choosing an override policy

## Keep secrets out of Git

- ignore `.env` and local variants; share an `.env.example` containing names and placeholders only
- an ignored file remains plain text on disk; environment variables aren't encryption either
- avoid printing secrets, dumping `os.environ`, or including credentials in screenshots and exceptions
- deployment environments can inject credentials through their secret storage facilities
- if a real secret is committed, revoke or rotate it first; deleting the file in a later commit doesn't remove history
- coordinate any history cleanup with collaborators

GitHub documents the [response to a committed secret](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository).

## Practice check

- run with a placeholder API key, then run with it missing and with it empty
- predict which cases pass validation
- set one placeholder in the shell and another in `.env`; explain which wins with default loading
