# WORKING WITH DATA :

- request weather data
- convert it into a DataFrame
- convert dates, plot the values and save the results

## Working with dates

- `from datetime import datetime, timedelta`
- `datetime.now()` (current local date and time)
- `timedelta(days=7)` (duration of seven days)
- `time_now - timedelta(days=7)` (date and time one week earlier)
- `date_value.strftime("%Y-%m-%d")` (format as a YYYY-MM-DD string)
- `%Y` (four-digit year), `%m` (month), `%d` (day)

## Processing the weather response

- `data = response.json()` (parse the response body)
- `daily_data = data["daily"]` (daily weather values)
- `time`, `temperature_2m_max` and `temperature_2m_min` are parallel lists in this example
- build columns named `date`, `max_temp` and `min_temp` using `pd.DataFrame(...)`
- `df["date"] = pd.to_datetime(df["date"])` converts date strings to pandas datetime values
- datetime values support chronological plotting and later date operations
- see [API notes](working-with-api.md) for requests and response handling

## Date range and indexes

- a range from seven days ago through today has eight calendar dates when both endpoints are included
- `range(1, 8)` visits positions `1` through `7`, skipping the first response entry
- the printed loop and the DataFrame may therefore cover different numbers of days
- decide whether the chart should cover today plus six days or the previous seven complete days
- use the returned dates and list lengths when checking what was actually received
- don't assume the response always contains eight entries

## Matplotlib basics

- `import matplotlib.pyplot as plt`
- `plt.figure(figsize=(10, 6))` (new figure, width and height in inches)
- `plt.plot(x, y)` (plot y against x)
- `plt.title(...)`, `plt.xlabel(...)`, `plt.ylabel(...)` (add labels)
- `plt.grid()` (add a grid)
- `plt.show()` (display the figure)
- the linear example uses `y = 2 * x`
- `[i * i for i in range(-10, 11)]` creates y values for the quadratic example

## Plotting weather

- plot `df["date"]` against `df["max_temp"]` and `df["min_temp"]`
- `marker="o"` (circular markers at data points)
- `markersize`, `markerfacecolor`, `markeredgecolor`, `markeredgewidth` (marker appearance)
- `label="Max Temperature"` gives a line a legend label
- `plt.legend()` displays the labels
- `plt.xticks(rotation=45)` rotates date labels
- `plt.tight_layout()` adjusts spacing to reduce clipping

## Saving results

- `plt.savefig("weather_chart.png")` (save the current figure)
- save before `plt.show()` in these examples
- `df.to_csv("data/delhi_weather.csv", index=False)` (save the table)
- output paths are relative to the working directory
- create missing output folders before saving
