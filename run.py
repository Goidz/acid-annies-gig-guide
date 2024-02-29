from datetime import datetime

#the_date = datetime.now().date()
#print(the_date)

"""
Event title and location input.
"""
def enter_event_title():
    event_title = input("Enter artist(s)/event.(Seperate with commas) \n")
    event_location = input("Enter location/venue \n")
    print(f"Tonight {event_title} live at {event_location}")
    print("Next step. Pick a genre from below:\n")

enter_event_title()

"""
List of genres for select_genre function.
"""
genres = ["black metal", "blues", "death metal", "stoner", "rock", "doom", "thrash metal", 
"prog", "heavy metal", "power metal", "jazz", "speed metal", "core"]
print(f"These are your genres to pick from: {genres}.\n")

"""
Selecting a genre from the genres list.
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
