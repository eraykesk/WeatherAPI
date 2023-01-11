import requests
def main():
    # defining base url
    BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
    # getting the api key
    API_KEY = open('api_key', 'r').read()
    # defining city
    CITY = "Ödemiş"




    url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY

    # getting the response
    response = requests.get(url).json()

    # extracting the response
    temp_kelvin = response['main']['temp']
    temp_cels = kelvin_to_celsius(temp_kelvin)
    feels_like_kelv = response['main']['feels_like']
    feels_like_cels=kelvin_to_celsius(feels_like_kelv)
    humidity = response['main']['humidity']
    description = response['weather'][0]['description']

    # printing the results
    print(f"Temperature in {CITY}: {temp_cels:.2f}")
    print(f"Temperature in {CITY} feels like: {feels_like_cels:.2f}")
    print(f"Humidity in {CITY} : {humidity}")
    print(f"Weather in {CITY} is {description} ")

# function to convert kelvin temperature to celsius
def kelvin_to_celsius(kelvin):
    celsius = kelvin - 273.15
    return celsius

if __name__ == "__main__":
    main()
