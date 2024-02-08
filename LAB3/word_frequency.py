from collections import Counter
import re

def word_frequency(input_string):
    words = re.findall(r'\b\w+\b', input_string.lower())
    return dict(Counter(words))

text = "This is aaaa sample text 1. Sample text is here 1."
frequency_dict = word_frequency(text)
print(frequency_dict)
