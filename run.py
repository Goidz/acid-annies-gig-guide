from datetime import date
import re
import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("aunty_acids_guide_to_mayhem")


"""
#List of genres for select_genre function.
"""
genres = ["Black Metal", "Blues", "Death Metal", "Stoner", "Rock",
"Doom", "Thrash Metal", "Prog", "Heavy Metal", "Power Metal",
"Jazz", "Funk", "Speed Metal", "Core", "Punk", "Soul", "Psychedelic"]


"""
Learned about validating URL input via this thread on Stackoverflow:
https://stackoverflow.com/questions/7160737/how-to-validate-a-url-in-python-malformed-or-not
"""
url_regex = re.compile(
        r'^(?:http|ftp)s?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\
          .?|[A-Z0-9-]{2,}\.?)|'  # domain...
        r'localhost|'   # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)


def get_event_date():
    """
    Date of the event from user input.
    Found assistance with date validation via this thread on Stackoverflow:
    https://stackoverflow.com/questions/16870663/how-do-i-validate-a-date-string-format-in-python
    """
    date_is_valid = False
    while date_is_valid is False:
        date_input = input("Please enter the date of the event (yyyy-mm-dd) \n")
        if date_input:  # Validate is not empty
            if len(date_input) == 10:  # Validate length
                if "-" in date_input:  # Validate separator
                    try:
                        valid_date = date.fromisoformat(date_input)
                        date_is_valid = True
                        return valid_date
                    except ValueError:
                        print("Date format invalid, please follow (yyyy-mm-dd)")
                else:
                    print("Date separator invalid, please follow (yyyy-mm-dd)")
            else:
                print("Date format invalid, please follow (yyyy-mm-dd)")
        else:
            print("Date cant be empty, please follow yyyy-mm-dd")


def display_genres_options(genres):
    """
    Displaying the list of genres to select as index.
    Makes selection process easier for user as not displayed in list form.
    Simplifies user input for later display functionality.
    """    
    index = 1
    print("\nPlease select the event genres from below.")
    print("---- Available genres ----\n")
    for genre in genres:
        print(f"{index} - {genre}")  # Creates an indexed list from genres[]
        index = index + 1
    print("--------------------------")


def check_if_valid_genre_option(genres, selected_genre):
    """
    Checks if the number entered falls within the index length.
    Learned about .join in this article:
    https://stackoverflow.com/questions/8270092/remove-all-whitespace-in-a-string
    """
    try:
        selected_genre = ''.join(selected_genre.split())
        selected_genre_index = int(selected_genre)
        if (selected_genre_index < len(genres)) and (selected_genre_index > 0):
            return True
        return False
    except:
        return False


def validate_genre_input(genres):
    """
    Validates user input from given genres_list options
    Creates input as list
    splits at ,s 
    Calls previous function check_if_valid_genre_option()
    Return error msg if incorrect
    """
    input_is_valid = False
    while input_is_valid is False:
        user_input = input("Select the event genres (comma separated): ")  # Asks for user input
        errors_found = False
        selected_genre_list = []  # Creates empty list to add correct input
        user_input_list = user_input.split(",")  # creates new variable to split user input at ","
        for user_input_element in user_input_list:  # Stores user input in new variable
            if check_if_valid_genre_option(genres, user_input_element):  # Calls earlier created function to check input
                selected_genre_list.append(int(user_input_element))  # if correct adds input as int to selected_genres_list
            else:
                print(f"This option is not valid: {user_input_element}")  # error msg if incorrect
                errors_found = True
        input_is_valid = not errors_found
    return selected_genre_list


"""
def select_genre(genres):
    
    # Selecting a genre from the genres list.
    # Is required. Loops through until user selected correct option from genres list.
    
    user_input = input("\nPlease choose a genre. Please Capitalize! Seperate multiple entries with commas.\
(ex. write. Black Metal, Blues): \n")
    select_artist = user_input.split(",")
    for select in select_artist:
        while select not in genres:
            print(f"Incorrect input. Please select a genre \
    from the list (Please Capitalize! ex. write. Black Metal, Blues): {genres}.")
            user_input = input("\n")
            select_artist = user_input.split(",")
        return select_artist

    for select in select_artist:
        if select in genres:
            return select_artist
        else:
            while select_artist not in genres:
                print(f"Incorrect input. Please select a genre \
from the list (Please Capitalize! ex. write. Black Metal, Blues): {genres}.")
                user_input = input("\n")
                if user_input in genres:
                    break              
                return user_input
"""

def get_text_input(input_title, min_len=1):
    """
    Function to validate text-input from user for event_title_info function.
    Text fields can not be empty so at least some characters required.
    """
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


def get_url():
    """
    Learned about "django url validation regex" via this thread on Stackoverflow:
    https://stackoverflow.com/questions/7160737/how-to-validate-a-url-in-python-malformed-or-not
    Function for URL input from user. In this case a preview track of artists performing.
    """
    input_is_valid = False
    while input_is_valid is False:
        user_input = input("Enter artist music link \
(enter 'skip' to skip this step) \n")
        input_is_valid = re.match(url_regex, user_input) is not None
        if input_is_valid:
            return user_input
        else:
            if user_input == "skip":  # enables user to skip step.
                return "Link not provided."
            else:
                print("Invalid url. Type skip to skip this option.")


def get_url_map():  #Event location via map
    """
    Function for URL input from user. In this case, a location map.
    """
    input_is_valid = False
    while input_is_valid is False:
        user_input = input("Enter venue/event location map link (Google Maps) \
(enter 'skip map' to skip this step) \n")
        input_is_valid = re.match(url_regex, user_input) is not None
        if input_is_valid:
            return user_input
        else:
            if user_input == "skip":  # enables user to skip step.
                return "Link not provided."
            else:
                print("Invalid url. Type skip to skip this option")

"""
def add_data():
    SHEET.append_row([get_event_date()], table_range = "A2")
"""

def main():
    """
    Run all functions.
    """
    event_day = get_event_date()
    # print(f"{genres}.")
    event_genre = display_genres_options(genres)
    event_title = get_text_input("\nEnter artist(s) or event name:\n", 1)
    event_venue = get_text_input("Enter event location or venue:\n", 1)
    venue_map = get_url_map()
    event_location = get_text_input("Enter city\n", 3)
    artist_url = get_url()
    print("\nResult!\n")
    print(f"On the menu today! A delicious serving of {event_genre}!")
    print("\n")
    print(f"The Mayhem will occur on: {event_day}, \
{event_title} live at {event_venue}, {event_location}.")
    print("\nMap")
    print(f"{venue_map}")
    print("\nHere's a sneak peak!")
    print(f"{artist_url}")


print("Welcome to Aunty Acid's Guide to Mayhem, a Gig guide!")
print("This app intends to function as a simplistic way \
to create and upload events.")
print("\nLet's get started! \n")
main()
