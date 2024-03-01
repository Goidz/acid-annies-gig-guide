from datetime import date

"""
Date of the event from user input.
Found help with date validation via this thread on Stackoverflow:
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

event_day = get_event_date()
print(f"The date is: {event_day}")

          

print("\nNext step. Pick a genre from below:\n")

"""
List of genres for select_genre function.
"""
genres = ["black metal", "blues", "death metal", "stoner", "rock", "doom", "thrash metal", 
"prog", "heavy metal", "power metal", "jazz", "speed metal", "core"]
print("These are your genres to pick from:\n")
print(f"{genres}.")

"""
Selecting a genre from the genres list.
Loops through until user selected correct option from genres list.
"""
def select_genre():
    choice = input("Please choose a genre (in lower case): \n")
    if choice in genres:
            print(f"You chose {choice}.")
    else:
        while choice not in genres:
            print(f"Incorrect input. Please select a genre (In lowercase) from the list: {genres}.")
            choice = input("")
            if choice in genres:
                print(f"You chose {choice}.")
                break
   
select_genre()

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
Event title/artists and location input.
"""
def event_title_info():
    event_day = get_event_date()
    event_title = get_text_input("\nEnter artist(s)/event:\n", 1)
    event_venue = get_text_input("Enter location/venue:\n", 1)
    event_location = get_text_input("Enter city\n", 2)
    print(f"The Mayhem will occur on: {event_day}, {event_title} live at {event_venue}, {event_location}!")

event_title_info()

