import csv
import time
import os

# Source for csv reading
# https://stackoverflow.com/questions/56342198/python-code-to-read-csv-file-based-on-user-input
def readCSV():
    movies_list = []

    while True:
        try:
            file = str(input("\nEnter file you want to use: "))

            # Add file extension '.csv' if not included
            if not ".csv" in file:
                file += ".csv"
            
            # Bool to check if file exists
            exists = os.path.isfile(file)

            if(exists == True):
                #print(exists)
                break
            else:
                print("Error! File not found, please try again\n")
        except IOError:
            print("File not found")

    #Open file, and parse data
    with open(file, newline='') as csv_file:
        movies_file = csv.reader(csv_file)
        for row in movies_file:
            movies_list.append(Films(row[0], row[1], row[2], row[3]))
        
    return movies_list


# Display menu options
def menu():
    print("Please choose from the below options:")
    print("1 - Show movies released in a specific year")
    print("2 - Show highest rated movie for each year")
    print("3 - Show movies and their release year for a specific language")
    print("4 - Exit\n")

# Display data requested by user
def display_data(user_input, movies):
    num_movies = 0
    
    #Display movies released in user specified year
    if(user_input == 1):
        user_year = input("\nSee movies released in what year? ")
        print("")

        # Iterate thru movies, display films released in user specified year
        for film in movies:
            if film.year == user_year:
                print(film.title)
                num_movies += 1 # counter to track # of movies
            else:
                continue
        
        print("")
        if(num_movies < 1):
            print("There were no movies released in ", user_year)
            print("")

    # Display highest rated movie(s) in user specified year
    elif(user_input == 2):
        #print("\nShow highest rated movie in specific year")

        high_rated = []

        year = input("Please enter which year you would like to see the 3 highest rated 3 movies: ")

        # Append all movies released in user specified year to list 'high_rated'
        for film in movies:
            if(film.year == year):
                high_rated.append(film)
            else:
                continue
        
        highest_rated = sorted(high_rated, key=lambda films: films.rating)

        print(highest_rated)

    elif(user_input == 3):
        print("\nShow movie+year for specific langauges")
        return 0

    elif(user_input == 4):
        print("\nExiting program....")
        exit()

# Get user input for menu option, loop for validation
# Source: https://medium.com/better-programming/how-to-indefinitely-request-user-input-until-valid-in-python-388a7c85aa6e
def getInput():
    while True:
        try:
            userChoice = int(input("Enter number of option selected: ")) 
            if userChoice > 0 and userChoice < 5:
                return userChoice
            print("Error! Invalid option, please try again\n")
        except Exception as e:
            print(e)

# Create class to store films
class Films():
    title = ""
    year = 0
    languages = []
    rating = 0

    def __init__(self, var1, var2, var3, var4):
        self.title = var1
        self.year = var2
        self.languages = var3
        self.rating = var4






# Read in csv file



# Parse csv file into objects to handle data

# Source for parsing csv file into objects
# https://stackoverflow.com/questions/31933257/python-3-how-to-read-a-csv-file-and-store-specific-values-as-variables

movies = readCSV()

time.sleep(1)

print("\nGreat, I've read your file and parsed the data!\n")

time.sleep(1)

while True:
    # Print menu (use function)
    menu()

    # Get user input for menu option, loop for validation
    userInput = getInput()

    # Display data requested by user
    display_data(userInput, movies)


