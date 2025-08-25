def example_list_function():
  example_list = ['element1', 'element2', 'element3']
  for element in example_list:
      print(element)

# Call the function and print each element
example_list_function()


students = ["Yousif", "Zaid", "Abdullah", "Hassan"]
def manage_students():
    # your code here
    first_student = students[1]
    last_student = students[-1]
    return f"first student: {first_student}, last student:{last_student}"

# Call the function and print the result
print('Exercise 1:', manage_students())



# Exercise 2: Loop and String Concatenation
#
# Create a tuple named foods containing the same number of foods (strings) as there are names in the students list.
# Create a variable named meal and assign an empty string to it.
# Use a for loop to iterate over the strings in foods and append each string to meal.
foods = ("Burger", "Apple", "Banana", "Pizza")

def combine_foods():
    # your code here
    meal = ""
    for food in foods:
        meal += f"{food} "
    return meal

# Call the function and print the result
print('Exercise 2:', combine_foods())

def slice_foods():
    # your code here
    last_two_foods = foods[-1: 1: -1]

    # last_two_foods = (foods[-1], foods[-2]) other solution
    return last_two_foods

# Call the function and print the result
print('Exercise 3:', slice_foods())


home_town = {
    "city":"Manama",
    "state": "Zinj",
    "population": 10000
}
def hometown_info():
    # your code here
    home_town_message = f"I was born in {home_town['city']}, {home_town['state']} - population of {home_town['population']}"
    return home_town_message

# Call the function and print the result
print('Exercise 4:', hometown_info())

def list_home_town_items():
    # your code here
    text = ""
    for key, value in home_town.items():
        text += f"{key} = {value}\n"

    return text

# Call the function and print the result
print('Exercise 5:', list_home_town_items())


def create_awesome_students():
    # your code here
    awesome_students = []

    for student in students:
        awesome_students.append(f"{student} is Awesome!")
    return awesome_students

# Call the function and print the result
print('Exercise 6:', create_awesome_students())

def filter_foods_with_a():
    # your code here
    foods_with_an_a = []
    for food in foods:
        if "a" in food:
            foods_with_an_a.append(food)
    return foods_with_an_a

# Call the function and print the result
print('Exercise 7:', filter_foods_with_a())