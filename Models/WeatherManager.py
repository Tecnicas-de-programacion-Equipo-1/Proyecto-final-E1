import urllib.request
import json
from Models.Weather import Weather
from Models.JsonManager import JsonManager


class WeatherManager:
    class Constants:
        base_url = "http://api.openweathermap.org/data/2.5/weather?q=Mexico,MX&appid="
        env_file = "Env-example/env_example"


    @classmethod
    def get_weather_data(cls):
        try:
            env_variables = JsonManager.open_json_file(cls.Constants.env_file)
            if env_variables is None:
                return
            key = env_variables.get("key", None)

            with urllib.request.urlopen(cls.Constants.base_url + key) as response:
                data = response.read().decode()
                json_data = json.loads(data)
                return Weather(json_data)
        except Exception as error:
            return None