# WORKING WITH APIs :

- send a request to a service and use its response
- the examples use `requests` for HTTP GET requests
- JSON is a text format used to exchange structured data

## Building the URL

- URL contains a domain, endpoint path and optional query parameters
- `?` starts the query; `&` separates parameters
- `latitude`, `longitude` and `current` are parameters in the weather request
- f-strings insert our coordinate values into the URL
- `requests.get(url, params={"latitude": latitude, "longitude": longitude})` can build query parameters for us
- use the exact domain, endpoint and parameter names required by the service
- `GET` is the HTTP method; don't put the word `GET` inside the URL string

## Making the request

- `response = requests.get(url)` (returns a Response object)
- `headers={"User-Agent": "weather-app-rajat"}` identifies the application in the place lookup example
- pass headers using `requests.get(url, headers=headers)`
- `timeout=10` sets a timeout for network operations so the request doesn't wait indefinitely

## Understanding the response

- `print(response)` (short representation such as `<Response [200]>`)
- `response.status_code` (HTTP status; `200` means OK)
- `response.headers` (response metadata)
- `response.text` (body decoded as a string)
- `response.content` (body as bytes; prefer this over the internal `_content` attribute)
- `response.json()` (parse the JSON body into Python values)
- a JSON object becomes a dictionary; a JSON array becomes a list
- `.json()` doesn't make another request or modify the original response
- `.json()` can fail if the body isn't valid JSON, even when the status is `200`

## Weather app

- `get_place(latitude, longitude)` looks up a place using coordinates (reverse geocoding)
- the example uses `https://nominatim.openstreetmap.org/reverse` with `lat`, `lon` and `format=json`
- `data["address"]["city"]` accesses a city in a nested dictionary
- some addresses may not contain `city`; check the available keys or use `.get()` with a fallback
- `get_weather()` gets the place name, then requests current temperature from Open-Meteo
- `data["current"]["temperature_2m"]` accesses the temperature
- returning a value lets another function use it; printing only displays it

## Handling failures

- `response.raise_for_status()` raises an HTTP error for unsuccessful 4xx/5xx responses
- successfully parsing JSON doesn't prove the HTTP request succeeded
- network failures, HTTP errors, invalid JSON and missing dictionary keys are separate problems

```python
response = requests.get(url, timeout=10)
response.raise_for_status()
data = response.json()
```

- see [error handling](error-handling.md) for `try` and `except`
