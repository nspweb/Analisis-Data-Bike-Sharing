import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Title of the dashboard
st.title("Bike Sharing Dashboard")

# Load the dataset
data_path = 'data/all_data.csv'  # Replace with the actual path
df = pd.read_csv(data_path)

# Define the season and weather labels for better readability
season_labels = {
    1: 'Winter',
    2: 'Spring',
    3: 'Summer',
    4: 'Fall'
}

weather_labels = {
    1: 'Clear/Few Clouds',
    2: 'Mist/Cloudy',
    3: 'Light Snow/Rain',
    4: 'Heavy Rain/Thunderstorm'
}

# Map the seasons and weather situations to their labels
df['season_label'] = df['season_day'].map(season_labels)
df['weather_label'] = df['weathersit_day'].map(weather_labels)

# Add user input for selecting season
st.sidebar.subheader("Filter by Season")
selected_season = st.sidebar.multiselect(
    'Choose season(s):', options=df['season_label'].unique(), default=df['season_label'].unique())

# Add user input for selecting weather condition
st.sidebar.subheader("Filter by Weather Condition")
selected_weather = st.sidebar.multiselect(
    'Choose weather condition(s):', options=df['weather_label'].unique(), default=df['weather_label'].unique())

# Filter the dataframe based on user input
filtered_df = df[df['season_label'].isin(selected_season) & df['weather_label'].isin(selected_weather)]

# Display key summary statistics for filtered data
st.subheader("Summary of Filtered Data")

# Handle case where the filtered data is empty
if filtered_df.empty:
    st.write("No data available for the selected filters.")
else:
    # Calculate total and average usage for the filtered data
    total_usage = filtered_df['cnt_hour'].sum()
    average_usage = filtered_df['cnt_hour'].mean()

    # Display the summary text
    st.write(f"Total number of bike uses in the selected filters: **{total_usage:,.0f}**")
    st.write(f"Average hourly bike usage: **{average_usage:,.2f}** users per hour.")

    # If the user selected only one weather condition, display a specific message about it
    if len(selected_weather) == 1:
        st.write(f"Under the weather condition '**{selected_weather[0]}**', the average number of users per hour is **{average_usage:,.2f}**.")

# #1 Impact of Season on Bike Usage
st.subheader("Impact of Season on Bike Usage")

# Group by season and calculate average usage
usage_by_season = filtered_df.groupby('season_label')['cnt_hour'].mean().reset_index()

# Barplot for bike usage by season
plt.figure(figsize=(10, 6))
sns.barplot(data=usage_by_season, x='season_label', y='cnt_hour', palette='viridis')
plt.title('Bike Usage by Season', fontsize=16)
plt.xlabel('Season', fontsize=14)
plt.ylabel('Average Bike Usage (Hourly)', fontsize=14)
plt.xticks(rotation=45)
plt.grid(axis='y')

# Show the plot
st.pyplot(plt)

# #2 Impact of Weather Conditions on Bike Usage
st.subheader("Impact of Weather Conditions on Bike Usage")

# Group by weather condition and calculate average usage
usage_by_weather = filtered_df.groupby('weather_label')['cnt_hour'].mean().reset_index()

# Barplot for weather condition's impact on bike usage
plt.figure(figsize=(12, 7))

# Define colors for the bars, highlighting the highest value
max_value = usage_by_weather['cnt_hour'].max()
colors = ['darkblue' if val == max_value else 'lightblue' for val in usage_by_weather['cnt_hour']]

# Barplot with custom colors
sns.barplot(x='weather_label', y='cnt_hour', data=usage_by_weather, palette=colors)
plt.title('Impact of Weather Conditions on Bike Usage', fontsize=18, weight='bold')
plt.xlabel('Weather Condition', fontsize=14)
plt.ylabel('Average Bike Usage (Hourly)', fontsize=14)
plt.xticks(rotation=45, ha='right', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Adjust layout and show the plot
plt.tight_layout()
st.pyplot(plt)

# Show filtered data (optional)
st.subheader("Filtered Data Preview")
st.write(filtered_df.head())