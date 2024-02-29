from datetime import date

"""
Date of the event from user input.
"""
"""
Event title and location input.
"""
def enter_event_title():
    date_info = input("Please enter the date of the event (yyyy-mm-dd)").split("-")
    print(date_info)
    year, month, day = [int(item) for item in date_info]
    event_day = date(year, month, day)
    print(f"The Mayhem will occur on: {event_day}")
    event_title = input("\nEnter artist(s)/event:\n")
    event_venue = input("Enter location/venue:\n")
    event_location = input("Enter city\n")
    print(f"On {event_day}, {event_title} live at {event_venue}, {event_location}")
    

enter_event_title()

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

