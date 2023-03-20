class BracketValidator:
def __init__(self, input_string):
self.input_string = input_string
def is_valid(self):
stack = []
for char in self.input_string:
if char in ["(", "{", "["]:
stack.append(char)
else:
if not stack:
return False
current_char = stack.pop()
if current_char == "(":
if char != ")":
return False
if current_char == "{":
if char != "}":
return False
if current_char == "[":
if char != "]":
return False
if stack:
return False
return True