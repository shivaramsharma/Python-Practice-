#Count the frequency of each character in a string using a dictionary

def count_char_frequency(text_string):
    frequency_dict = {}
    for char in text_string:
        if char in frequency_dict:
            frequency_dict[char] += 1
        else:
            frequency_dict[char] = 1
    return frequency_dict

input_string = "this is python progrraming language"

char_counts = count_char_frequency(input_string)

print(f"given string is {input_string}")
print(f"output char counts is {char_counts}")

