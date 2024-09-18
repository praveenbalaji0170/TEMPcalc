import pandas as pd
import random
from datetime import datetime

# Generate sample temperature data
def generate_temperature_data(days=7, readings_per_day=5):
    data = []
    
    # Loop through each day
    for day in range(1, days + 1):
        day_name = f"Day {day}"
        
        # Generate random temperature readings for the day
        for reading in range(readings_per_day):
            time = datetime.now().strftime("%H:%M:%S")  # Current time
            temperature = round(random.uniform(15, 40), 1)  # Random temperature between 15°C and 40°C
            data.append([day_name, time, temperature])
    
    return data

# Function to create a DataFrame and rank temperatures
def create_temperature_csv(data):
    # Create a DataFrame
    df = pd.DataFrame(data, columns=['Day', 'Time', 'Temperature (°C)'])
    
    # Rank the temperatures in descending order
    df['Rank'] = df['Temperature (°C)'].rank(ascending=False)
    
    # Save to CSV
    df.to_csv('temperature_data.csv', index=False)
    print("Temperature data saved to 'temperature_data.csv'.")

# Generate temperature data for 7 days with 5 readings per day
temperature_data = generate_temperature_data(days=7, readings_per_day=5)

# Create CSV and rank the temperatures
create_temperature_csv(temperature_data)
