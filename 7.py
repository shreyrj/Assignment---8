class StringReverser:
def reverse_words(self, s: str) -> str:
"""
Reverses the words in a string.
:param s: a string to be reversed
:return: a string with the words reversed
"""
# Split the string into words
words = s.split()
# Reverse the order of the words
reversed_words = words[::-1]
# Join the words back together into a single string
reversed_string = ' '.join(reversed_words)
return reversed_string