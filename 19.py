original_list = ['red', 'black', 'white', 'green', 'orange']
substring1 = 'ack'
substring2 = 'abc'
contains_substring = lambda s, sub: sub in s
result1 = list(filter(lambda x: contains_substring(x, substring1), original_list))
result2 = list(filter(lambda x: contains_substring(x, substring2), original_list))
print("Original list:", original_list)
print(f"Elements of the list that contain '{substring1}':", result1)
print(f"Elements of the list that contain '{substring2}':", result2)