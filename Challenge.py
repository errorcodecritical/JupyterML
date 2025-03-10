## NEW CODE SEGMENT

import pandas as pd
from ucimlrepo import fetch_ucirepo

#Converts hours, minutes, seconds to seconds for easier handling

def hms_to_seconds(t):
    h, m, s = [int(i) for i in t.split(':')]
    return 3600*h + 60*m + s
  
# fetch dataset 
room_occupancy_estimation = fetch_ucirepo(id=864) 
  
# data (as pandas dataframes) 
X = room_occupancy_estimation.data.features
y = room_occupancy_estimation.data.targets

# Get dataset information

# Get number of target elements of the same category
target_distribution = y.pivot_table(index=["Room_Occupancy_Count"], aggfunc="size")

# We can see the dataset is unbalanced. Ruh-roh!
X.iloc[:,1]

time = X.iloc[:, 1]
time[0]
#room_occupancy_estimation(room_occupancy_estimation.loc["Date"])

## NEW CODE SEGMENT

import seaborn as sns
import matplotlib.pyplot as plt

# Set a theme for Seaborn plots
sns.set_theme()

# Histogram of "Room_Occupancy_Count"
plt.figure(figsize=(10, 6))
sns.barplot(x=["0", "1", "2", "3"], y=target_distribution.values)
plt.title("Room Occupancy Distribution")
plt.xlabel("Number of Occupants")
plt.ylabel("Occurences")
plt.show()

# We can see the dataset is unbalanced. Ruh-roh!
