import requests

import graphs

import pandas as pd

from os.path import exists

# Function to save data to an Excel sheet
def save_data(json_data):

    # if there are previous data points, then concatenate the new data with the old data
    if exists('locationOfISS.xlsx'):

        object_one = pd.read_excel('locationOfISS.xlsx')

        df = pd.json_normalize(json_data)

        updated_file = pd.concat([object_one, df])

        updated_file.to_excel('locationOfISS.xlsx')

    # else create the excel sheet
    else:

        df = pd.json_normalize(json_data)
        df.to_excel('locationOfISS.xlsx')



def get_current_weather():
    # Collect the input (city name) from the user.
    city = input("What city do you want to do know the weather for?\n")

    # Collect the input (state name) from the user (if in the US).
    state = input("If you're in the US, what is the state abbreviation? If not, click Enter.\n")

    # Collect the input (country name) from the user.
    country = input("What is the country name?\n")

    # API link
    weather_url = f"https://api.openweathermap.org/data/2.5/weather?q={city},{state},{country}&units=imperial&appid=e89c759b0eeedfb883f2c032ba235e16"

    # API REQUEST
    data = requests.get(weather_url)

    # Store response received from the API request as JSON data
    results = data.json()

    # Invalid location conditional
    if results['cod'] == '404':
        print("You entered an invalid location.")
        continue_or_quit_program()

    # How do we use .get for more chaining keys?
    print(results)
    print(results.get('name'))

    # Print the location name, country name, temperature, and weather description
    print(
        f"Location Name: {results.get('name')}, Country Name: {results['sys']['country']}\n Temperature: {results['main']['temp']}, Description: {results['weather'][0]['description']}")

    save_data(results)

    continue_or_quit_program()


# Function that gets a 5-day forecast at 3-hour intervals
def get_forcast():
    # Collect the input (city name) from the user.
    city = input("What city do you want to do know the weather for?\n")

    # Collect the input (state name) from the user (if in the US).
    state = input("If you're in the US, what is the state abbreviation? If not, click Enter.\n")

    # Collect the input (country name) from the user.
    country = input("What is the country name?\n")

    # API link
    forcast_url = f"https://api.openweathermap.org/data/2.5/forecast?q={city},{state},{country}&units=imperial&appid=e89c759b0eeedfb883f2c032ba235e16"

    # API REQUEST
    data = requests.get(forcast_url)

    # Store response received from the API request as JSON data
    results = data.json()

    # Invalid location conditional
    if results['cod'] == '404':
        print("You entered an invalid location.")
        continue_or_quit_program()

    # Array to store dates
    date_forecast = []

    # Array to store temperatures
    temp_forecast = []

    # Loop to get the dates, temperature, and weather description for the 5-day weather forecast at 3-hour intervals
    for forcast in results['list']:
        date_forecast.append(forcast['dt_txt'])
        temp_forecast.append(forcast['main'].get('temp'))
        print(
            f"Date: {forcast['dt_txt']} Temperature: {forcast['main'].get('temp')}, Description: {forcast['weather'][0].get('description')}")

    print(date_forecast)
    print(temp_forecast)
    temp_date_dict = {'date': date_forecast, 'temp': temp_forecast}

    graphs.basic_plot(temp_date_dict)

    continue_or_quit_program()


def continue_or_quit_program():
    # Continue or quit
    continue_or_quit = input("Enter 'A' to return to the menu or Enter 'B' to quit.")

    continue_or_quit = continue_or_quit.lower()

    if continue_or_quit == "a":
        get_menu()
    elif continue_or_quit == "b":
        exit()


def get_menu():
    run_menu = True

    # while run_menu :
    # What is the user's choice: current weather or 5-day forecast?
    user_choice = input(
        "Do you want to find the current weather(A) or get the 5 day forecast(B)? Enter 'A' or 'B' or 'Q' to quit")

    user_choice = user_choice.lower()

    if user_choice == 'a':
        get_current_weather()
    elif user_choice == 'b':
        get_forcast()
    elif user_choice == 'q':
        exit()


def main():
    # This is the welcome message.
    print("Hello! Welcome to City Weather Finder.")  # Welcome message in ASCII -- extra

    get_menu()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
