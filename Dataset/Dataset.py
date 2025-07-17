#Here in this I am writing this to generate a sample dataset which will act like real dataset of dmrc 
#I couldnt get the real dataset anywhere on the internet similar to this i am simulating one here
import pandas as pd 
import numpy as np
import random



#Setting seed
random.seed(42)
np.random.seed(42)


#Categories
stations = [
    "Rajiv Chowk", "Hauz Khas", "Kashmere Gate", "Central Secretariat", 
    "Chandni Chowk", "Dwarka Sector 21", "Noida City Centre", "Vaishali", 
    "Saket", "Karol Bagh", "MG Road", "New Delhi", "Lajpat Nagar", 
    "Botanical Garden", "Inderlok", "Shivaji Stadium", "Yamuna Bank", 
    "Vishwavidyalaya", "Mayur Vihar", "Rohini West"
]


days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday","Sunday"]
time_slots = ["Morning(7PM - 10 AM)", "Afternoon(11AM - 2PM)", "Evening(4PM - 8PM)", "Night(9PM - 11PM)"]
weather = ["Clear", "Rainy", "Foggy", "Cloudy"]
event_nearby = ["Yes", "No"]
holiday = ["Yes", "No"]


#Defining number of rows 
num_rows = 10000


#Generating Base Dagta

data = {
    "Station_name": np.random.choice(stations, num_rows),
    "Day_of_week": np.random.choice(days, num_rows),
    "Time_slot": np.random.choice(time_slots, num_rows),
    "Weather_condition": np.random.choice(weather, num_rows),
    "Event_nearby": np.random.choice(event_nearby, num_rows, p=[0.9,0.1]),
    "Is_holiday": np.random.choice(holiday, num_rows, p=[0.85,0.15]),
}


df = pd.DataFrame(data)


#Genrating crowd count with my observation 

def simulate_Passenger_count(row):
    base = 200
    if row["Station_name"] in ["Rajiv Chowk", "Kashmere Gate","New Delhi"]:
        base+=500
    if row["Time_slot"] in ["Morning(7PM - 10AM)","Evening(4PM - 8Pm)"]:
        base+=400
    if row["Day_of_week"] in ['Monday',"Tuesday","Wednesday","Thursday","Friday"]:
        base+=300
    if row["Weather_condition"] in ["Rainy","Foggy"]:
        base+=100
    if row["Event_nearby"] == "NO":
        base+=250
    if row["Is_holiday"] == "No":
        base-=200
    return max(50,int(np.random.normal(loc=base,scale=50)))

#Applying fucntion to generetate        
df['Avg_passenger_count'] = df.apply(simulate_Passenger_count,axis=1)


df.to_csv("delhi_metro_data.csv",index=False)

     