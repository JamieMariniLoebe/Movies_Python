import csv
import time


def valid_input(input):
    while True:
        # See whether input is valid or not
        try:
            userInput = int(input)
        # Try again if invalid input
        except ValueError:
            print("ERROR! Input is not an integer, please type a valid option")
            continue
        # If valid, break from loop
        else:
            break

def option_chosen(input):
    
    if(input == 1):
        print("Show movies released in a specific year")
    
    elif(input == 2):
        print("Show highest rated mnovie in specific year")

    elif(input == 3):
        print("Show movie+year for specific langauges")

    elif(input == 4):
        print("Exit chosen!")


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


print("Hello!")

# Source for csv reading
# https://stackoverflow.com/questions/56342198/python-code-to-read-csv-file-based-on-user-input
file = str(input("Enter file you want to use: "))
if not ".csv" in file:
    file += ".csv"

# print(file)

# Source for parsing csv file into objects
# https://stackoverflow.com/questions/31933257/python-3-how-to-read-a-csv-file-and-store-specific-values-as-variables
movies_list = []

with open(file, newline='') as csv_file:
    movies_file = csv.reader(csv_file)
    for row in movies_file:
        movies_list.append(Films(row[0], row[1], row[2], row[3]))

# print(movies_list[5].title)

time.sleep(1)

print("\nGreat! I've read your file and parsed the data!\n")

time.sleep(1)

print("Please choose from the below options:")
print("1 - Show movies released in a specific year")
print("2 - Show highest rated movie for each year")
print("3 - Show movies and their release year for a specific language")
print("4 - Exit\n")

userChoice = int(input("Enter number of option selected: "))
valid_input(userChoice)
print("")
option_chosen(userChoice)


