- when we share our projects with others, we can have all the requirements in the requirements.txt file

- then, `python -m pip install -r requirements.txt`
- it will install all the packages mentioned in 'requirements.txt' along with the versions you have mentioned

- `python -m pip freeze > requirements.txt` (save installed package versions from the current environment; this doesn't detect which packages the code actually uses)
