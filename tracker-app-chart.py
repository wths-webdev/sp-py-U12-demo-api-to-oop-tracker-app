'''
This version uses matplotlib to add a bar chart 
of the fruits and calories
'''
import requests
import json
import random
import matplotlib.pyplot as plt

# Define the Fruit class
class Fruit:
    def __init__(self, name, family, genus, calories, sugar):
        self.__name = name
        self.__family = family
        self.__genus = genus
        self.__calories = calories
        self.__sugar = sugar

    def __str__(self):
        return (
            f"Name: {self.__name}\n"
            f"Family: {self.__family}\n"
            f"Calories: {self.__calories}\n"
            f"Sugar: {self.__sugar}"
        )
    
    def get_name(self):
        return self.__name
    
    def get_calories(self):
        return self.__calories
    
    def get_sugar(self):
        return self.__sugar

# Function to fetch data and return it
def fetch_fruit_data(fruit_name):
    url = f"http://www.fruityvice.com/api/fruit/{fruit_name}"
    response = requests.get(url)

    if response.status_code == 200:
        fruit_data = response.json()
        return fruit_data
    else:
        print(f"Error fetching data for {fruit_name}.")
        return None
    
# Create a Fruit object using the data
def create_fruit(fruit_json):
    fruit = Fruit(
                    fruit_json["name"],
                    fruit_json["family"],
                    fruit_json["genus"],
                    fruit_json["nutritions"]["calories"],
                    fruit_json["nutritions"]["sugar"]
                )
    return fruit

print()
print("Welcome to the Fruit Tracker!")
print("Track the nutritional values you've consumed in fruits today!")
print()
# store all the fruit objects
fruits = []
calories = 0
sugar = 0

# Main program logic
while True:
    user_input = input("Enter a fruit: ").lower().strip()
    print()
    print(random.choice(["Yummmm", "Tasty :P", "I'll take a bite of that!", "Great choice!"]))
    print("Loading...")

    # fetch fruit data using the API
    fruit_data = fetch_fruit_data(user_input)

    # error handling: if fruit isn't found, continue in loop
    if not fruit_data:
        continue
    
    # create an fruit object
    fruit_obj = create_fruit(fruit_data)
    print(fruit_obj)
    # append the fruit to our list
    fruits.append(fruit_obj)

    print()
    keep_going = input("Track another fruit (y/n): ").lower().strip()
    if keep_going == "n":
        break

# display summary to user
print()
print("Here's your fruity breakdown for today:")
for fruit in fruits:
    calories += fruit.get_calories()
    sugar += fruit.get_sugar()
print(f"Calories: {calories}")
print(f"Sugar: {sugar}")

# --- bar chart -----------------------------------
# https://www.w3schools.com/PYTHON/matplotlib_bars.asp
# two lists needed for the x (names) and y (calories) axis
fruit_names = []
fruit_calories = []

# extract info for the chart
for fruit in fruits:
    fruit_names.append(fruit.get_name())
    fruit_calories.append(fruit.get_calories())

# bar(x,y)
plt.bar(fruit_names, fruit_calories)

# https://www.w3schools.com/Python/matplotlib_labels.asp
plt.title("Fruit breakdown")

# make the bars horizontal instead. (check the w3schools link...)

# try the pie chart on your own!
# https://www.w3schools.com/PYTHON/matplotlib_pie_charts.asp
# you have to specify the parameter because there are multiple constructors (overloading).
plt.pie(fruit_calories, labels=fruit_names)
# talk about what to google after we see the plots on top of each other (need subplot)
plt.show()
