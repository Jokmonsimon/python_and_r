# Strings are not just text; they are versatile and essential for working with any textual data.
# Strings in Python are sequences of characters, and they play a crucial role in handling textual data.
# Whether it is words, sentences, or dates, strings empower us to work with text in meaningful ways.

# Day 2 Date
day_2_date = "20-Nov-2023"
print("Day 2 Date:", day_2_date)
print("Data Type", type(day_2_date))

# Day 2 Activity
day_2_activity = "Running"
print("\nDay 2 Activity:", day_2_activity)
print("Data Type: ", type(day_2_activity))

# String Concatenation (+) - Combining two or more strings together
concat_date_and_activity = day_2_date + " " + day_2_activity
print("\nDay 2 Date + Day 2 Activity: " + concat_date_and_activity)
print("Data Type: ", type(concat_date_and_activity))

# Concatenate strings to make a sentence
sentence = "On " + day_2_date + ", the activity of Day 2 was " + day_2_activity
print("\nThe complete sentence reads: " + sentence + ".")
