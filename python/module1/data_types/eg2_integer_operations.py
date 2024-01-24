#!/usr/bin/env python3

# Performing integer operations
timer_day_1 = 1251
timer_day_2 = 1248

# Calculating total time duration for Day 1 & 2
total_time = timer_day_1 + timer_day_2
print("Total Time Duration for Day 1 & 2 (Sec):", total_time)
print("Data Type:", type(total_time))

# Finding the average time duration for Day 1 & 2
average_time = total_time / 2
print("\nAverage Time Duration for Day 1 & 2 (Sec):", average_time)
print("Data Type:", type(average_time))

# Finding the minimum time duration for Day 1 & 2
min_time = min(timer_day_1, timer_day_2)
print("\nMinimum Time Duration between Day 1 & 2 (Sec):", min_time)
print("Data Type:", type(min_time))

# Finding the maximum time duration for Day 1 & 2
max_time = max(timer_day_1, timer_day_2)
print("\nMaximum Time Duration between Day 1 & 2 (Sec):", max_time)
print("Data Type:", type(max_time))
