# Weather Forecast Application - User Guide

## Introduction
Welcome to the Weather Forecast Application! This application provides real-time weather updates and future weather forecasts for any city worldwide. It is designed to be user-friendly, displaying temperature data in multiple formats (Celsius, Fahrenheit, and Kelvin), along with detailed weather conditions and icons.

## Features
- **Real-time Weather Updates**: Get the current weather conditions for your selected city.
- **Multi-day Forecast**: Choose how many days ahead you want to see the forecast.
- **Temperature Units**: View temperatures in Celsius, Fahrenheit, or Kelvin.
- **Visual Representation**: Icons and background images change based on weather conditions.

## How to Use
### Step 1: Enter a City
1. Open the application.
2. Enter the name of the city you want to check the weather for.
3. Click the **Submit** button.

### Step 2: Choose Forecast Preferences
1. Select the number of days you want the forecast for.
2. Choose your preferred temperature unit (Celsius, Fahrenheit, or Kelvin).
3. Submit your selection to view the forecast.

### Step 3: View Weather Data
- The current temperature, weather condition, and an associated icon will be displayed.
- If a multi-day forecast was selected, a list of upcoming days with their weather details will be shown.

## Troubleshooting
- **No City Provided**: If you do not enter a city, an error message will be displayed.
- **Invalid City**: If the city does not exist, you will be prompted to enter a valid city.
- **API Issues**: Ensure that the API key is correctly placed in the `API_Key.txt` file.

## Technical Details
```plaintext
- Framework: Django
- Weather Data Source: OpenWeather API
- Frontend: HTML (city_weather.html)
- Backend: Python (views.py)
```

Thank you for using the Weather Forecast Application!

