# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import requests

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


def get_current_weather():

    # Collect the input (city name) from the user.
    city = input("What city do you want to do know the weather for?\n")
    state = input("If you're in the US, what is the state abbreviation? If not, click Enter.\n")
    country = input("What is the country name?\n")

    weather_url = f"https://api.openweathermap.org/data/2.5/weather?q={location},{state_code},{country_code}&units=imperial&appid=e89c759b0eeedfb883f2c032ba235e16"
    print(weather_url)

    data = requests.get(weather_url)
    results = data.json()

    print(f"Location Name: {results['name']}, Country Name: {results['sys']['country']}\n Temperature: {results['main']['temp']}, Description: {results['weather'][0]['description']}")

def get_forcast():

    # Collect the input (city name) from the user.
    city = input("What city do you want to do know the weather for?\n")
    state = input("If you're in the US, what is the state abbreviation? If not, click Enter.\n")
    country = input("What is the country name?\n")

    forcast_url = f"https://pro.openweathermap.org/data/2.5/forecast/hourly?q={city},{state},{country}&appid=e89c759b0eeedfb883f2c032ba235e16"
    data = requests.get(forcast_url)
    print(data.json())


def main():
    # This is the welcome message.
    print("Hello! Welcome to City Weather Finder.")  # Welcome message in ASCII -- extra

    # What is the user's choice?
    user_choice = input("Do you want to find the current weather(A) or get the 4 day forcast(B)? Enter 'A' or 'B'")

    if user_choice == 'A':
        get_current_weather()
    elif user_choice == 'B':
        get_forcast()





# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

