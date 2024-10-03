import pandas as pd
import plotly.express as px
import streamlit as st

# Load the dataset directly using pd.read_csv
data = pd.read_csv("data/all_data.csv")

# Helper function 1: Create a DataFrame for daily bike usage
def create_daily_usage_df(df):
    """Create a DataFrame for daily bike usage."""
    daily_usage_df = df[['dteday', 'cnt_day']].drop_duplicates().set_index('dteday')
    return daily_usage_df

# Helper function 2: Create a DataFrame for hourly bike usage
def create_hourly_usage_df(df):
    """Create a DataFrame for hourly bike usage."""
    hourly_usage_df = df[['dteday', 'hr', 'cnt_hour']].copy()
    return hourly_usage_df

# Create DataFrames for daily and hourly usage
daily_usage_df = create_daily_usage_df(data)
hourly_usage_df = create_hourly_usage_df(data)

# Dashboard layout
st.header('Dashboard Penggunaan Sepeda :sparkles:')

# Date filter for selecting a specific day
selected_date = st.selectbox('Pilih Tanggal:', daily_usage_df.index.unique())

# Filter daily data based on the selected date
daily_data = daily_usage_df.loc[[selected_date]]

# Visualization 1: Daily bike usage
st.subheader(f'Penggunaan Sepeda pada {selected_date}')
st.write(daily_data)

# Create a bar plot with plotly
fig1 = px.bar(daily_data, x=daily_data.index, y='cnt_day', title='Jumlah Penggunaan Sepeda Harian')
st.plotly_chart(fig1)

# Visualization 2: Hourly bike usage
st.subheader(f'Penggunaan Sepeda per Jam pada {selected_date}')
hourly_data = hourly_usage_df[hourly_usage_df['dteday'] == selected_date]

# Create a line plot with plotly
fig2 = px.line(hourly_data, x='hr', y='cnt_hour', title='Jumlah Penggunaan Sepeda per Jam')
st.plotly_chart(fig2)
