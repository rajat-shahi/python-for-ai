# GIT AND GITHUB FUNDAMENTALS :

- Git records versions of a project locally
- GitHub hosts Git repositories and provides pull requests, issues and collaboration
- repository (project files plus Git history)
- commit (recorded snapshot), branch (a movable reference to a commit)
- remote (named connection to another repository, commonly `origin`)

## The three places changes live

- working tree (files you edit)
- staging area or index (content prepared for the next commit)
- commit history (snapshots already recorded)
- editing a file doesn't stage it; staging a file doesn't commit it
- `git add` stages its content at that moment; later edits need staging again

## Start or clone a repository

```bash
git --version
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

- these settings identify commit authors; they don't sign you into GitHub
- `git init -b main` starts a new repository in the current folder
- `git clone https://github.com/OWNER/REPO.git` copies an existing repository and its history
- replace `OWNER` and `REPO` with your actual values
- choose init for a new project or clone for an existing one
- this workspace already has Git; don't initialize it again for this exercise

## Everyday local workflow

```bash
git status
git diff
git add learning/git-and-github.md
git diff --staged
git commit -m "Add Git learning notes"
git log --oneline -5
```

- `status` shows staged, unstaged and untracked files
- `diff` shows unstaged edits; `diff --staged` shows what the next commit would contain
- stage specific paths so unrelated edits stay separate
- commits are local until pushed

The [Git tutorial](https://git-scm.com/docs/gittutorial) explains staging, commits, branches and collaboration.

## Branches and GitHub flow

```bash
git switch -c add-weather-summary
# edit, check and commit your changes
git push -u origin add-weather-summary
```

- a new branch starts from your current commit
- `-u` records the upstream branch for future push/pull operations
- open a pull request on GitHub from the feature branch into the default branch
- a pull request proposes a merge and provides a place for review
- after review and successful checks, merge it and update your local default branch
- `git switch main` then `git pull --ff-only` updates it when no divergent local history exists
- replace `main` if the repository uses another default branch
- a fork is a separate repository; a branch is a line of work inside a repository
- an issue tracks a bug or task; it doesn't change the code

Use [GitHub flow](https://docs.github.com/en/get-started/using-github/github-flow) for the branch, review and merge cycle.

## Remotes, fetch and pull

- `git remote -v` lists configured remote URLs
- for a newly initialized local repository, `git remote add origin https://github.com/OWNER/REPO.git` connects an existing GitHub repository
- `git fetch origin` downloads remote history without merging it into your current branch
- `git pull --ff-only` fetches and updates only when a fast-forward is possible; it stops on divergence
- `git push` uploads local commits to the configured remote branch
- GitHub authentication is separate from commit identity; configure SSH or a supported HTTPS credential method

## Gitignore for Python projects

Suggested patterns to understand and adapt:

```gitignore
.venv/
__pycache__/
*.py[cod]
.ruff_cache/
.env
.env.*
!.env.example
.DS_Store
```

- `.gitignore` affects untracked files; it doesn't remove files already tracked
- `!` makes an exception so a placeholder-only `.env.example` can be shared
- commit source code, notes, project configuration and an application's `uv.lock`
- `git check-ignore -v code/environment-variables/.env` explains an ignore match
- `git ls-files -- path/to/file` checks whether a file is tracked
- if needed, `git rm --cached path/to/file` stages its removal from tracking while keeping the local copy
- untracking doesn't erase earlier commits or make an exposed secret safe

See GitHub's [ignore guide](https://docs.github.com/en/get-started/git-basics/ignoring-files) and [secret removal guidance](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository).

## Undo and conflicts

- `git restore --staged path/to/file` unstages changes and keeps working files
- `git restore path/to/file` discards unstaged edits to that file; inspect the diff first
- `git revert COMMIT` records a new commit reversing an earlier commit; useful for shared history
- a conflict means Git needs help combining changes
- inspect `git status`, edit the conflicted sections, remove conflict markers, then stage and complete the operation
- during a merge, `git merge --abort` cancels that merge when you decide to start again

The [restore reference](https://git-scm.com/docs/git-restore) distinguishes restoring working files from restoring the index.

## Practice check

- in a practice repository, edit a file, stage it, then edit it again
- predict what `git diff` and `git diff --staged` will each show
- commit the staged version and explain why the second edit remains uncommitted
