# Integers are whole numbers in Python, meaning they do not have any decimal places.
# They are used to represent exact quantities, such as counts or durations.

# Create integer data type from Day 3 timer in seconds
day_3_timer = 1263
print("Day 3 Timer (Sec):", day_3_timer, "Seconds")
print("Data Type:", type(day_3_timer))

# Uncomment the code in Line 11, analyse it, tell what is wrong with the code and correct if there is error
# Please, leave your corrected code in the comment section
# print("\nDay 3 Timer: " + day_3_timer + "Seconds")

# Create another integer data type from Steps column
day_3_steps = 3748
print("\nDay 3 Steps:", day_3_steps, "steps")
print("Data Type:", type(day_3_steps))

# Integer Arithmetic Operations
day_1_heart_points, day_2_heart_points, day_3_heart_points = 42, 42, 41  # Multiple variable assignment
total_heart_points = day_1_heart_points + day_2_heart_points + day_3_heart_points
print("\nTotal Heart Points from Day 1 to Day 3:", total_heart_points)
print("Data Type:", type(total_heart_points))
