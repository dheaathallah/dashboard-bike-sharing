import streamlit as st
import pandas as pd
# Load dataset
df = pd.read_csv("day.csv")
st.set_page_config(page_title="Dashboard Analisis Sepeda", page_icon="🚴")

# Judul dashboard
st.title("📊 Dashboard Analisis Data Sepeda")

# Menampilkan data (opsional)
st.subheader("Data Awal")
st.write(df.head())  # Menampilkan 5 data pertama

# Menampilkan ringkasan statistik
st.subheader("Ringkasan Statistik")
st.write(df.describe())
# Menampilkan grafik jumlah penyewaan sepeda per hari
st.subheader("Grafik Penyewaan Sepeda")
st.line_chart(df["cnt"])  # cnt = jumlah penyewaan sepeda

# Menambahkan interaktivitas untuk filter memilih range tanggal
import datetime

# Konversi kolom tanggal ke format datetime
df["dteday"] = pd.to_datetime(df["dteday"])

# Pilih rentang tanggal
st.subheader("📆 Pilih Rentang Tanggal")
start_date = st.date_input("Tanggal Mulai", df["dteday"].min())
end_date = st.date_input("Tanggal Akhir", df["dteday"].max())

# Filter data berdasarkan rentang tanggal
df_filtered = df[(df["dteday"] >= pd.to_datetime(start_date)) & (df["dteday"] <= pd.to_datetime(end_date))]

# Tampilkan data yang sudah difilter
st.write(df_filtered.head())

# Update grafik dengan data yang sudah difilter
st.subheader("📈 Grafik Penyewaan Sepeda (Filtered)")
st.line_chart(df_filtered.set_index("dteday")["cnt"])

# Menambahkan grafik interaktif dengan plotly
import plotly.express as px

st.subheader("📊 Penyewaan Sepeda Berdasarkan Musim")
fig = px.bar(df, x="season", y="cnt", color="season", labels={"season": "Musim", "cnt": "Jumlah Penyewaan"})
st.plotly_chart(fig)

# Menambahkan filter berdasarkan cuaca
# Pilih kondisi cuaca
weather_filter = st.selectbox("Pilih Kondisi Cuaca", df["weathersit"].unique())

# Filter data berdasarkan cuaca
df_weather = df[df["weathersit"] == weather_filter]
st.write(df_weather.head())

import plotly.express as px

st.subheader("🔍 Clustering Penyewaan Sepeda Berdasarkan Musim")
season_mapping = {1: "Spring", 2: "Summer", 3: "Fall", 4: "Winter"}
df["season_label"] = df["season"].map(season_mapping)

# Visualisasi jumlah penyewaan berdasarkan musim
fig = px.box(df, x="season_label", y="cnt", color="season_label", title="Distribusi Penyewaan Sepeda per Musim")
st.plotly_chart(fig)

# Update grafik
st.subheader("📊 Grafik Penyewaan Sepeda Berdasarkan Cuaca")
st.line_chart(df_weather.set_index("dteday")["cnt"])

# Jalankan dengan perintah: streamlit run app.py