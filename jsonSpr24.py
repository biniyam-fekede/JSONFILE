# Import the json module to enable JSON class library.
import json

# Define a dictionary `data` that holds personal information about an individual, including their name, age, city of residence, and others...
data = {
    'name': 'John Doe',
    'age' : 30,
    'city' : 'New York, NY', 
    'interest' : ['Reading', 'Soccer', 'History', 'Politics', 'Gym'],
    'is_Teacher' : False
}
# Use the json.dump() function to write the dictionary into this file in JSON format.
# Write the dictionary to a JSON file with indentation for better readability
with open('data1.json', 'w') as json_file:
    json.dump(data, json_file, indent=4)

print("Data has been written to data1.json")

# Read the json file back into a Python dictionary
with open('data1.json', 'r') as json_file:
    # create an object called load_data. Load the json file into the parameter.
    load_data = json.load(json_file)

print("Successful able to read data1.json")
# Output the data that was read from the file to the console. 
print(load_data)