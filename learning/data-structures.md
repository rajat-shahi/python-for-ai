# DATA STRUCTURES :

- LIST (ordered, changeable items)
- TUPLE (ordered, fixed items)
- DICTIONARY (key-value pairs)
- SET (unique items, unordered)

## Common things to learn

- create
- access
- modify/change (add, remove, update)
- common methods
- common uses
- common mistakes

## Lists

- use when order matters and items might change
- `fruits = ["apple", "banana", "orange"]`
- `my_list = []` (empty list)
- can contain mixed datatypes and duplicate values

## Accessing lists

- indexing starts at `0`
- `fruits[0]` (first item), `fruits[-1]` (last item)
- `fruits[0:2]` (items at index `0` and `1`; stop index excluded)
- `fruits[1:]` (from index `1` to the end)

## Changing lists

- `fruits[0] = "mango"` (update an item)
- `fruits.append("kiwi")` (add at the end)
- `fruits.insert(0, "kiwi")` (add at a specific index)
- `last_item = fruits.pop()` (remove and return the last item)
- `del fruits[2:5]` (delete a slice)

## List methods and checks

- `len(numbers)` (number of items)
- `numbers.count(1)` (count occurrences)
- `numbers.index(5)` (first matching index; raises `ValueError` if missing)
- `numbers.sort()` (sort the list in place)
- `numbers.reverse()` (reverse the list in place)
- `numbers.copy()` (create a shallow copy)
- `"apple" in fruits` (check membership)
- `if fruits:` (check whether the list has items)
- `[num for num in nums if num != 2 and num % 2 == 0]` (new list of even numbers except `2`)

## Copying lists and common mistakes

- `other = nums` (same list; changes through either name affect it)
- `other = nums.copy()` (new outer list; nested objects are still shared)
- `.copy()` is a shallow copy, not a deep copy
- a deep copy also copies nested mutable objects; use `copy.deepcopy()` when needed
- accessing a missing index raises `IndexError`
- avoid adding or removing items from a list while looping over that same list
- avoid names like `list`, `tuple`, `dict` and `set`; they hide Python's built-in names

## Tuples

- use for ordered values whose items should not be replaced
- `colors = ("green", "red", "blue")`
- `empty_tuple = ()`
- `single_tuple = (12,)` (comma is required; `(12)` is an integer)
- `coordinates = 2.14, 17.23` (parentheses are optional here)
- indexing and slicing work like lists: `colors[0]`, `colors[1:3]`

## Tuple unpacking and changes

- `x, y = (3, 14)` (assign each item to a variable)
- `y, x = x, y` (swap values)
- `first, second, *rest = colors` (collect remaining items into a list)
- ordinary unpacking needs the same number of variables and items
- cannot replace an item directly: `point[0] = 2` raises `TypeError`
- `point = (2, point[1])` (assign a new tuple)
- convert to a list, edit, then convert back with `tuple(values)` if needed

## Dictionaries

- use for looking up values by a specific key
- `person = {"name": "rajat", "age": 26}`
- `my_dict = {}` (empty dictionary)
- `scores = dict(math=22, physics=91)` (another way to create one)
- keys are unique; assigning an existing key replaces its value
- keys must be hashable (strings, numbers, or tuples of hashable items)

## Accessing dictionaries

- `scores["math"]` (get a value; missing key raises `KeyError`)
- `scores.get("hindi")` (returns `None` if missing)
- `scores.get("hindi", "not available")` (custom default if missing)
- `"city" in person` (check keys, not values)
- `students["rajat"]["class"]` (access a nested dictionary)

## Changing dictionaries and methods

- `person["age"] = 27` (update a value)
- `person["email"] = "name@example.com"` (add a key-value pair)
- `del person["age"]` (delete a key-value pair)
- `country = person.pop("country")` (remove a key and return its value)
- `person.clear()` (remove all entries)
- `person.update({"age": 22, "city": "delhi"})` (add or update multiple entries)
- `person.keys()`, `person.values()`, `person.items()` (views of keys, values, or pairs)
- `person.copy()` (shallow copy)

## Sets

- use to remove duplicates or check membership quickly
- `numbers = {1, 2, 3, 3}` (stores only `1, 2, 3`)
- `empty_set = set()` (`{}` creates an empty dictionary)
- `set([2, 2, 4, 6])` (create from a list)
- sets are unordered; they do not sort items or support indexing
- items must be hashable

## Changing sets and common uses

- `colors.add("green")` (add an item)
- `colors.remove("red")` (remove an item; raises `KeyError` if missing)
- `colors.discard("red")` (remove an item safely if present)
- `"aman" in allowed_users` (check membership)
- `list(set(names))` (remove duplicates; original order is not preserved)
- use a list when order matters
