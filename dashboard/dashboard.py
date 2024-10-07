import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv('data/all_data.csv')

# --- Judul Dashboard ---
st.title("Bike Sharing Dashboard")

# Sidebar untuk filter interaktif
st.sidebar.header("Filter")

# 1. Penggunaan Sepeda Berdasarkan Musim
st.sidebar.subheader("Penggunaan Sepeda Berdasarkan Musim")
season_options = ['All', 'springer', 'summer', 'fall', 'winter']  # Sesuaikan nama musim di sini
selected_season = st.sidebar.selectbox("Pilih Musim", season_options)

# 2. Dampak Kondisi Cuaca terhadap Jumlah Pengguna Sepeda
st.sidebar.subheader("Dampak Kondisi Cuaca")
weather_options = ['All', 'Clear', 'Mist + Cloudy', 'Light Snow, Light Rain + Thunderstorm']
selected_weather = st.sidebar.selectbox("Pilih Kondisi Cuaca", weather_options)

# 3. Puncak Penggunaan Sepeda Berdasarkan Jam dan Status Hari
st.sidebar.subheader("Puncak Penggunaan Sepeda Berdasarkan Jam")
selected_hours = st.sidebar.slider("Pilih Rentang Jam", 0, 23, (0, 23))

# Mengelompokkan data berdasarkan musim dan menghitung rata-rata
usage_by_season = data.groupby('season_day').agg({
    'cnt_day': 'mean',
    'casual_day': 'mean',
    'registered_day': 'mean'
}).reset_index()

# Mengganti kode musim dengan nama musim
season_map = {1: 'springer', 2: 'summer', 3: 'fall', 4: 'winter'}
usage_by_season['season_day'] = usage_by_season['season_day'].map(season_map)

# Menyaring data berdasarkan pilihan musim
if selected_season != 'All':
    usage_by_season = usage_by_season[usage_by_season['season_day'] == selected_season]

# Mengecek apakah ada data yang tersaring
st.subheader("Penggunaan Sepeda Berdasarkan Musim")
if not usage_by_season.empty:
    # Membuat plot visualisasi
    plt.figure(figsize=(10, 6))
    sns.barplot(data=usage_by_season, x='season_day', y='cnt_day', palette='coolwarm')
    plt.title('Penggunaan Sepeda Berdasarkan Musim', fontsize=16)
    plt.xlabel('Musim', fontsize=14)
    plt.ylabel('Jumlah Penggunaan Sepeda', fontsize=14)
    plt.grid(axis='y', linestyle='--')
    st.pyplot(plt)
else:
    st.write(f"Tidak ada data untuk musim {selected_season}.")

# 2. Dampak Kondisi Cuaca terhadap Jumlah Pengguna Sepeda
st.subheader("Dampak Kondisi Cuaca terhadap Jumlah Pengguna Sepeda")
usage_by_weather = data.groupby('weathersit_day').agg({
    'cnt_day': 'mean',
    'casual_day': 'mean',
    'registered_day': 'mean'
}).reset_index()

# Mengganti kode cuaca dengan deskripsi
weather_map = {
    1: 'Clear',
    2: 'Mist + Cloudy',
    3: 'Light Snow, Light Rain + Thunderstorm',
}
usage_by_weather['weathersit_day'] = usage_by_weather['weathersit_day'].map(weather_map)

# Menyaring data berdasarkan pilihan cuaca
if selected_weather != 'All':
    usage_by_weather = usage_by_weather[usage_by_weather['weathersit_day'] == selected_weather]

# Membuat plot untuk penggunaan sepeda berdasarkan cuaca
if not usage_by_weather.empty:
    plt.figure(figsize=(12, 7))
    sns.barplot(x='weathersit_day', y='cnt_day', data=usage_by_weather, palette='Blues_r')
    plt.title('Dampak Kondisi Cuaca terhadap Jumlah Pengguna Sepeda', fontsize=18)
    plt.xlabel('Kondisi Cuaca', fontsize=14)
    plt.ylabel('Rata-rata Jumlah Pengguna', fontsize=14)
    plt.grid(axis='y', linestyle='--')
    st.pyplot(plt)
else:
    st.write(f"Tidak ada data untuk kondisi cuaca {selected_weather}.")

# 3. Puncak Penggunaan Sepeda Berdasarkan Jam dan Status Hari
st.subheader("Puncak Penggunaan Sepeda Berdasarkan Jam dan Status Hari")
data['is_holiday'] = data['holiday_hour'].apply(lambda x: 'Holiday' if x == 1 else 'Working')

peak_usage = data.groupby(['hr', 'is_holiday']).agg({
    'cnt_hour': 'sum'
}).reset_index()

# Filter data berdasarkan jam yang dipilih
peak_usage_filtered = peak_usage[(peak_usage['hr'] >= selected_hours[0]) & (peak_usage['hr'] <= selected_hours[1])]

# Membuat plot untuk penggunaan sepeda pada jam puncak
plt.figure(figsize=(10, 6))
sns.lineplot(data=peak_usage_filtered, x='hr', y='cnt_hour', hue='is_holiday', palette='Set2')
plt.title('Penggunaan Sepeda pada Jam Puncak', fontsize=16)
plt.xlabel('Jam', fontsize=14)
plt.ylabel('Jumlah Pengguna Sepeda', fontsize=14)
plt.legend(title='Hari Kerja vs Hari Libur')
plt.grid(True, linestyle='--')
st.pyplot(plt)