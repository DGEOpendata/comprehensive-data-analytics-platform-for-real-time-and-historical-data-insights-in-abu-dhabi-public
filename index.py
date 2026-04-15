python
import pandas as pd
import matplotlib.pyplot as plt
import requests
import json

# URL to the dataset
url = "https://example.com/Public_Transport_Usage_Insights.json"

# Fetch the dataset
def fetch_dataset(url):
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return pd.DataFrame(data)
    else:
        raise Exception("Failed to fetch data")

# Process and visualize the data
def visualize_transport_data(df):
    # Example: Analyzing peak hours of bus usage
    bus_data = df[df['TransportMode'] == 'Bus']
    bus_data['Hour'] = pd.to_datetime(bus_data['Time']).dt.hour
    peak_hours = bus_data.groupby('Hour').size()

    # Plotting
    plt.figure(figsize=(10, 6))
    peak_hours.plot(kind='bar', color='skyblue')
    plt.title('Peak Hours of Bus Usage')
    plt.xlabel('Hour of the Day')
    plt.ylabel('Number of Passengers')
    plt.show()

if __name__ == "__main__":
    # Fetch and process the dataset
    df = fetch_dataset(url)
    visualize_transport_data(df)
