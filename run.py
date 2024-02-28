from datetime import datetime

the_date = datetime.now().date()
print(the_date)


genres = ["black metal", "blues", "death metal", "stoner", "rock", "doom", "thrash metal", 
"prog", "heavy metal", "power metal", "jazz", "speed metal", "core\n"]
print(f"These are your genres to pick from: {genres}.\n")

"""
Selecting a genre from the genres list.
"""
def select_genre():
    choice = input("Please choose a genre (in lower case): \n")
    if choice in genres:
        print(f"You chose {choice}.")
    else:
        print("Incorrect. Please select a genre from the list")

        
        


select_genre()    
