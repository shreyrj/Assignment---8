dict_list = [
{'make': 'Nokia', 'model': 216, 'color': 'Black'},
{'make': 'Mi Max', 'model': '2', 'color': 'Gold'},
{'make': 'Samsung', 'model': 7, 'color': 'Blue'}
]
# Sort the list of dictionaries using a lambda function
sorted_dict_list = sorted(dict_list, key=lambda x: x['make'])
# Print the sorted list of dictionaries
print("Sorting the List of dictionaries:", sorted_dict_list)