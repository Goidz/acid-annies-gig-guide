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
            #choice += 1
            if choice in genres:
                print(f"You chose {choice}.")
                break
   
select_genre()    

"""
Event title and location input.
"""
def event_title_info():
    event_title = input("\nEnter artist(s)/event:\n")
    event_venue = input("Enter location/venue:\n")
    event_location = input("Enter city\n")

event_title_info()


def print_all_functions():    
    event_day = get_event_date()
    event_genre = select_genre()
    event_title_info()
    print(f"Looking for some {event_genre}!? On {event_day}, {event_title} live at {event_venue}, {event_location}")
    
print_all_functions()




