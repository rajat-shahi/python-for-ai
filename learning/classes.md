# CLASSES AND OBJECTS :

- OOP (object-oriented programming) groups related data and functions
- class (definition used to create objects)
- object or instance (one value created from a class)
- attributes (data stored on an object)
- methods (functions defined on a class)

## Creating a class

```python
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def info(self):
        print(f"Name: {self.name}, Breed: {self.breed}")

jerry = Dog(name="Jerry", breed="Labrador")
jerry.info()
```

- `__init__()` initializes an instance when it is created
- `self` refers to the instance whose method is running
- pass `name` and `breed`; Python supplies `self` for `jerry.info()`
- `self.name = name` stores the argument as an instance attribute
- `jerry.breed` accesses an attribute
- separate instances can hold different values
- `None` can represent an unspecified value, as in the second dog's breed

## Configuration and client examples

- `APIConfig` groups an API key, model name, token limit and base URL
- default parameter values are used when arguments are omitted
- keyword arguments can override individual defaults: `APIConfig("example-key", max_tokens=50)`
- `OpenAIClient` groups provider/model information with related methods
- `AnthropicClient.connect()` currently prints a message; it doesn't authenticate or make a network request
- the client names, model strings and keys in these examples are practice values
- storing an API configuration doesn't by itself send an API request

## Keeping validation state

- `self.errors = []` creates a separate error list for each new validator
- `validate_age()` accepts values from `0` through `150`; outside that range it records an error and returns `False`
- `validate_email()` only checks for `@`; this is a practice check, not complete email validation
- successful validation returns `True`
- errors accumulate across calls on the same instance
- `get_errors()` returns the existing list, so callers can modify that same list
- return `self.errors.copy()` if callers should receive a separate outer list

## Printing and unpacking errors

- `*errors` unpacks list items as separate function arguments
- `print("ERROR", *errors, sep="\n", end="...")` prints a heading, each error on a new line, then ends with `...`
- `sep` separates arguments; `end` is added once after the final argument
- `print(errors)` displays the list representation, including brackets
- `*errors` here is argument unpacking, not multiplication

## Double underscores and name mangling

- inside `MLModel`, `self.__api_key` is transformed into `self._MLModel__api_key`
- this helps avoid accidental naming conflicts; it doesn't enforce secrecy
- `model.__api_key = "changed"` outside the class creates a different attribute in this example
- the original `model._MLModel__api_key` remains `"secret"`
- `vars(model)` shows the instance's stored attributes
- someone can still access or change the mangled attribute
- don't rely on underscores to protect real API keys; avoid hardcoding secrets in source code

## Inheritance

- `class Dog(Animal):` makes `Dog` a child class of `Animal`
- the child inherits parent behavior such as `eat()` and `sleep()`
- it can add its own behavior, such as `bark()`
- because `Dog` doesn't define `__init__()` in this example, it uses the inherited initializer
- `Dog("Buddy")` therefore sets `self.name` through `Animal.__init__()`

## Overriding methods

- a child overrides a parent method by defining the same method name
- `Dog.makes_sound()` returns a barking message
- `Cat.makes_sound()` returns a meowing message
- `dog.makes_sound()` runs the version found for the dog's class
- different classes can respond differently to the same method call (polymorphism)
- these methods return strings; use `print(dog.makes_sound())` to display them in a script
