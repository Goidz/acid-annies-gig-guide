from datetime import datetime

the_date = datetime.now().date()
print(the_date)

genre = ""
genres = {"black metal", "blues", "death metal", "stoner", "rock", "doom", "thrash metal", 
"prog", "heavy metal", "power metal", "jazz", "speed_metal", "core"}
print(f"These are your genres to pick from: {genres}.")

"""
Selecting a genre from the genres list.
"""
def select_genre():
    choice = input("Please choose a genre: \n")
    while choice == genres:
        print(select_genre)

        
        


select_genre()    
