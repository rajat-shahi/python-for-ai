import requests

print("Hello world!")
print("I am learning AI")
print("My name is Rajat")


response = requests.get("https://api.github.com")
print(response.status_code)
body = response._content
print(body)
