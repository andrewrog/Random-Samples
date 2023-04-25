import random
import math
import statistics

# Andrew Rogers, Chris Nickel
# Sampling Method for Food Assistance (Gunnison)

# Seperating food assistance from non-food assistance

food_assistance = 2277
total_pop = 16918 #2020 data, 2020 to 2021 not much change
no_food_assistance = total_pop - food_assistance

food_per = food_assistance / total_pop #food assistance weight
no_food_per = no_food_assistance / total_pop #non food assistance weight

# 0 (no food assistance), 1 (food assistance)
person_list = [0, 1]

#Use the weights to for a sample of k=100 folks
values = random.choices(person_list, weights=(no_food_per, food_per), k=100)

# Finding the two parameters in the random sample list
number_food = values.count(0) 
number_non_food = values.count(1)

# Calculating the percentages in the random sample list
number_food_per = number_food / 100
number_non_food_per = number_non_food / 100

print(f"In the random sample of 100 folks, {number_food_per} had food assistance and {number_non_food_per} had no food assistance")
#In the random sample of 100 folks, 0.15 had food assistance and 0.85 had no food assistance.
