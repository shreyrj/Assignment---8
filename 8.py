def __init__(self):
self.string = ""
def get_string(self):
"""
Takes a string input from the user and stores it in the class instance variable `string`.
"""
self.string = input("Enter a string: ")
def print_string(self):
"""
Prints the stored string in reverse order.
"""
reversed_string = self.string[::-1]
print("Reversed string:", reversed_string)