rawIn = input("Please just enter a sentence:")
import re
wordCount = len(re.findall(r'\w+', rawIn))
print("Total word cout:", wordCount)
charCount = len(re.findall(r'[a-zA-Z]', rawIn))
print("Total character cout:", charCount)
