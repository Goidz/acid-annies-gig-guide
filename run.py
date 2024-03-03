from datetime import date

import re
"""
Learned about validating URL input via this thread on Stackoverflow: 
https://stackoverflow.com/questions/7160737/how-to-validate-a-url-in-python-malformed-or-not
"""
url_regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' #localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

"""
Date of the event from user input.
Found assistance with date validation via this thread on Stackoverflow:
https://stackoverflow.com/questions/16870663/how-do-i-validate-a-date-string-format-in-python
"""
def get_event_date():
    date_is_valid = False
    while date_is_valid is False:
        date_input = input("Please enter the date of the event (yyyy-mm-dd)")
        if date_input: #Validate is not empty
            if len(date_input) == 10: #Validate length
                if "-" in date_input: #Validate separator
                    try:
                        valid_date = date.fromisoformat(date_input)
                        date_is_valid = True
                        return valid_date
                    except ValueError:
                        print("Date format invalid, please follow yyyy-mm-dd")
                else:
                    print("Date separator invalid, please follow yyyy-mm-dd")
            else:
                print("Date format invalid, please follow yyyy-mm-dd")
        else:
            print("Date cant be empty, please follow yyyy-mm-dd")

"""
#List of genres for select_genre function.
"""
genres = ["black metal", "blues", "death metal", "stoner", "rock", "doom", "thrash metal", 
"prog", "heavy metal", "power metal", "jazz", "speed metal", "core", "punk", ]

"""
Selecting a genre from the genres list.
Is required. Loops through until user selected correct option from genres list.
"""
def select_genre():
    user_input = input("Please choose a genre (in lower case): \n")
    if user_input in genres:
            return user_input
    else:
        while user_input not in genres:
            print(f"Incorrect input. Please select a genre (In lowercase) from the list: {genres}.")
            user_input = input("")
            if user_input in genres:
                break

"""
Function to validate text-input from user for event_title_info function.
Text fields can not be empty so at least some characters required.
"""
def get_text_input(input_title, min_len=1):
    input_is_valid = False
    while input_is_valid is False:
        user_input = input(input_title)
        if user_input:
            if len(user_input) >= min_len:
                input_is_valid = True
                return user_input
            else:
                print(f"Input should be at least {min_len} chars")
        else:
            print("Can't be empty")  

"""
Learned about "django url validation regex" via this thread on Stackoverflow:
https://stackoverflow.com/questions/7160737/how-to-validate-a-url-in-python-malformed-or-not
"""
def get_band_url():
    input_is_valid = False
    while input_is_valid is False:
        user_input = input("Enter artist music link (enter 'skip' to skip this step)")
        input_is_valid = re.match(url_regex, user_input) is not None
        if input_is_valid:
            return user_input
        else:
            if user_input == "skip":
                return ""
            else:
                print("Invalid url") 

"""
Event title/artists and location input.
"""
def event_title_info():
    event_day = get_event_date()
    print(f"{genres}.")
    event_genre = select_genre()
    event_title = get_text_input("\nEnter artist(s)/event:\n", 1)
    event_venue = get_text_input("Enter location/venue:\n", 1)
    event_location = get_text_input("Enter city\n", 3)
    artist_url = get_band_url()
    print(f"On the menu today! A delicious serving of {event_genre}!")
    print(f"The Mayhem will occur on: {event_day}, {event_title} live at {event_venue}, {event_location}. You can listen to them at {artist_url}")

event_title_info()

