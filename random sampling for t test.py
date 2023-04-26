import math
import statistics
import random

#All the rates that were gathered from the interweb
population_list = [.045, .044, .042, .048, .047, .044, .033, .031, .027, .028, .028, .023, .026, .027, .024, .023, .024, .023, .023, .021, .02, .03, .022]
sample_list = [] #Keeping track of the indexes that have been used

#Looping through ten times to pull ten values
for x in range(0, 10):
    index = random.randint(0, 23)
    sample_list.append(population_list[index])
      
average = statistics.mean(sample_list) #Finding the average rate in the sample list
print(f"The average unemployment rate in the sample list is: {average}")



    
    

