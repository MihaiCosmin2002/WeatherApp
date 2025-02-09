import datetime
import os

import requests
from django.shortcuts import render


def index(request):
    api_key = open(os.path.dirname(os.path.dirname(__file__)) + "\\API_Key.txt", "r").read()
    current_weather_url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}"
    forecast_url = "https://api.openweathermap.org/data/2.5/onecall?lat={}&lon={}&exclude=current,minutely,hourly,alerts&appid={}"
    context = {
        "what": 'static/image.jpg'
    }
    if request.method == "POST":
        city = ""
        if request.POST['City'] == "":
            context = {
                "ERROR": "You didn't provide a city.",
                "what": 'static/image.jpg'
            }
            return render(request, "weather_app/index.html", context)
        for name in request.POST['City'].split(" "):
            city += name[0].upper() + name[1:] + " "
        degrees = request.POST.get('Degrees')
        forecast_days = request.POST.get('Forecast Days')
        try:
            weather_data, daily_forecast, what = fetch_weather_and_forcast(city, api_key, current_weather_url, forecast_url, forecast_days)
            if daily_forecast is None:
                try:
                    context = {
                        "weather_data": weather_data,
                        "daily_forecast": "no",
                        "degrees": degrees,
                        "forecast_days": forecast_days.split(" ")[0],
                        "what": what
                    }
                except:
                    context = {
                        "weather_data": weather_data,
                        "daily_forecast": 'no',
                        "degrees": degrees,
                        "forecast_days": 'no',
                        "what": what
                    }
            else:
                try:
                    context = {
                        "weather_data": weather_data,
                        "daily_forecast": daily_forecast,
                        "degrees": degrees,
                        "forecast_days": forecast_days.split(" ")[0],
                        'what': what
                    }
                except:
                    context = {
                        "weather_data": weather_data,
                        "daily_forecast": daily_forecast,
                        "degrees": degrees,
                        "forecast_days": 'no',
                        'what': what
                    }
            return render(request, "weather_app/index.html", context)
        except Exception as e:
            context = {
                "ERROR": "Provide an existing city!",
                "what": 'static/image.jpg'
            }
            return render(request, "weather_app/index.html", context)
    else:
        return render(request, "weather_app/index.html",context)


def fetch_weather_and_forcast(city, api_key, current_weather_url, forecast_url, forecast_days):
    response = requests.get(current_weather_url.format(city, api_key)).json()
    lat, lon = response['coord']['lat'], response['coord']['lon']
    forecast_response = requests.get(forecast_url.format(lat, lon, api_key)).json()
    if response['weather'][0]['main'] == "Clear":
        weather_data = {
            "city": city,
            "temperature_c": round(response['main']['temp'] - 273.15),
            "temperature_f": round((response['main']['temp'] - 273.15) * 1.8 + 32),
            "temperature_k": round(response['main']['temp']),
            "description": response['weather'][0]['description'],
            "icon": response['weather'][0]['icon'],
            "what": 'static/why-sky-blue-2db86ae.jpg'
        }
    elif response['weather'][0]['main'] == "Clouds":
        weather_data = {
            "city": city,
            "temperature_c": round(response['main']['temp'] - 273.15),
            "temperature_f": round((response['main']['temp'] - 273.15) * 1.8 + 32),
            "temperature_k": round(response['main']['temp']),
            "description": response['weather'][0]['description'],
            "icon": response['weather'][0]['icon'],
            "what": 'static/pexels-pixabay-209831.jpg'
        }
    elif response['weather'][0]['main'] == "Rain":
        weather_data = {
            "city": city,
            "temperature_c": round(response['main']['temp'] - 273.15),
            "temperature_f": round((response['main']['temp'] - 273.15) * 1.8 + 32),
            "temperature_k": round(response['main']['temp']),
            "description": response['weather'][0]['description'],
            "icon": response['weather'][0]['icon'],
            "what": 'static/istockphoto-1461681027-612x612.jpg'
        }

    try:
        daily_forecast = []
        i = 0
        for daily_data in forecast_response['daily']:
            if int(forecast_days.split(" ")[0]) == i:
                break
            elif daily_data['weather'][0]['main'] == "Clear":
                daily_forecast.append({
                    "day": datetime.datetime.fromtimestamp(daily_data['dt']).strftime("%A"),
                    "min_temp_c": round(daily_data['temp']['min'] - 273.15),
                    "max_temp_c": round(daily_data['temp']['max'] - 273.15),
                    "min_temp_f": round((daily_data['temp']['min'] - 273.15) * 1.8 + 32),
                    "max_temp_f": round((daily_data['temp']['max'] - 273.15) * 1.8 + 32),
                    "min_temp_k": round(daily_data['temp']['min']),
                    "max_temp_k": round(daily_data['temp']['max']),
                    "description": daily_data['weather'][0]['description'],
                    "icon": daily_data['weather'][0]['icon'],
                    "image": 'static/Lx0q.gif',
                })
                i += 1
            elif daily_data['weather'][0]['main'] == "Clouds":
                daily_forecast.append({
                    "day": datetime.datetime.fromtimestamp(daily_data['dt']).strftime("%A"),
                    "min_temp_c": round(daily_data['temp']['min'] - 273.15),
                    "max_temp_c": round(daily_data['temp']['max'] - 273.15),
                    "min_temp_f": round((daily_data['temp']['min'] - 273.15) * 1.8 + 32),
                    "max_temp_f": round((daily_data['temp']['max'] - 273.15) * 1.8 + 32),
                    "min_temp_k": round(daily_data['temp']['min']),
                    "max_temp_k": round(daily_data['temp']['max']),
                    "description": daily_data['weather'][0]['description'],
                    "icon": daily_data['weather'][0]['icon'],
                    "image": 'static/srG.gif'
                })
                i += 1
            elif daily_data['weather'][0]['main'] == "Rain":
                daily_forecast.append({
                    "day": datetime.datetime.fromtimestamp(daily_data['dt']).strftime("%A"),
                    "min_temp_c": round(daily_data['temp']['min'] - 273.15),
                    "max_temp_c": round(daily_data['temp']['max'] - 273.15),
                    "min_temp_f": round((daily_data['temp']['min'] - 273.15) * 1.8 + 32),
                    "max_temp_f": round((daily_data['temp']['max'] - 273.15) * 1.8 + 32),
                    "min_temp_k": round(daily_data['temp']['min']),
                    "max_temp_k": round(daily_data['temp']['max']),
                    "description": daily_data['weather'][0]['description'],
                    "icon": daily_data['weather'][0]['icon'],
                    "image": 'static/7scx.gif'
                })
                i += 1
        return weather_data, daily_forecast, weather_data["what"]
    except:
        return weather_data, None, weather_data["what"]
