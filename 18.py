input_string = "PaceWisd0m"
check_valid = lambda s: any(c.isupper() for c in s) and \
any(c.islower() for c in s) and \
any(c.isdigit() for c in s) and \
len(s) >= 10
if check_valid(input_string):
print("Valid string")
else:
print("Invalid string")