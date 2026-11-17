# VIRTUAL ENVIRONMENTS :

- keep each project's packages separate
- `venv` creates the environment; pip installs packages
- uv can manage both environments and projects

## Using venv and pip

Run inside your project folder (macOS/Linux):

```bash
python3 -m venv .venv             # create
source .venv/bin/activate         # activate
python -m pip install requests   # install a package
python -m pip list               # list installed packages
```

## Requirements files

```bash
python -m pip freeze > requirements.txt       # save installed versions
python -m pip install -r requirements.txt     # install from the file
```

- `freeze` saves packages from the current environment, including their dependencies
- `>` replaces the existing requirements file
- on another machine, create and activate a fresh environment before installing
- `deactivate` (leave the environment)

## Using uv

Choose a project type (run one):

```bash
uv init --app my-app             # application you run (default type)
uv init --lib my-library         # reusable package other projects import
uv init --no-package my-project  # simple scripts without a package build setup
```

- use `--no-package` for basic script practice; `--lib` sets up a packaged library
- see [uv project types](https://docs.astral.sh/uv/concepts/projects/init/) for details

For the simple script project above:

```bash
cd my-project
uv add requests                 # add a dependency
uv add --dev ruff               # add a development tool
uv run python main.py           # run using the project environment
```

- no manual activation needed with `uv run`
- `uv remove requests` (remove a dependency)
- `uv sync --locked` (recreate/sync the environment from an up-to-date lockfile)

## Moving from pip to uv

Keep the requirements-file workflow with `uv pip` (macOS/Linux):

```bash
uv venv .venv                          # create only if you need a new environment
source .venv/bin/activate
uv pip install requests                # install a package
uv pip install -r requirements.txt     # install requirements
uv pip list                            # list installed packages
uv pip freeze > requirements.txt       # save installed versions; overwrites the file
uv pip uninstall requests              # remove a package
uv pip check                           # check dependency compatibility
```

- an existing virtual environment can be reused; skip creation and activate it
- `uv pip sync requirements.txt` matches the environment to the file, removing extras
- `uv pip` changes installed packages; it doesn't update `pyproject.toml` or create `uv.lock`

Or migrate to a uv project, from your existing project folder:

```bash
uv init --no-package             # skip if already initialized
uv add -r requirements.txt       # import dependencies into the project
uv run python main.py           # replace main.py with your script
```

- after migrating, manage dependencies with `uv add` / `uv remove` and share `pyproject.toml` + `uv.lock`
- importing a frozen requirements file declares its indirect dependencies too; review the resulting list
- see the [uv migration guide](https://docs.astral.sh/uv/guides/migration/pip-to-project/)

## Important files

- `.venv/` (installed environment; ignore in Git)
- `requirements.txt` (package requirements for the pip workflow)
- `pyproject.toml` (uv project settings and declared dependencies)
- `uv.lock` (resolved versions; commit it with the application)
- `.env` stores configuration; it is different from `.venv/`

More: [uv notes](uv.md) and [requirements notes](requirements.md).
