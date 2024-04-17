import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

st.header('Air Quality Dashboard')
st.subheader('Untuk pemenuhan proyek Analysis data dengan python Dicoding')


st.write(
    """Penjelasan atribut data:

- No:(integer) Jumlah baris dalam kumpulan data, dianggap sebagai kuantitatif
- Year: (integer) tahun data, dianggap sebagai kategorikal
- Month: (integer) bulan dari data, dianggap sebagai kategorikal
- Day: (integer) hari dari data, dianggap sebagai kategorikal
- Hour: (integer) jam dari data, dianggap sebagai kategorikal
- PM2.5: (integer) Konsentrasi PM2.5 per jam di area tersebut. Diukur dalam (ug/m³), dianggap sebagai - kontinu
- PM10: (integer) HKonsentrasi PM2.5 per jam di area tersebut. Diukur dalam (ug/m³), dianggap sebagai kontinu
- SO2: (integer) Konsentrasi PM2.5 per jam di area tersebut. Diukur dalam (ug/m³), dianggap sebagai kontinu
- NO2: (integer) Konsentrasi PM2.5 per jam di area tersebut. Diukur dalam (ug/m³), dianggap sebagai kontinu
- CO-:(integer) Konsentrasi PM2.5 per jam di area tersebut. Diukur dalam (ug/m³), dianggap sebagai kontinu
- O3:(integer) HKonsentrasi PM2.5 per jam di area tersebut. Diukur dalam (ug/m³), dianggap sebagai kontinu
- PRES:(integer) Tekanan udara di area tersebut. Diukur dalam Pascal, dianggap sebagai kontinu
- DEWP:(integer) suhu titik derajat yang dianggap kontinu
- RAIN: (integer) Curah hujan di area yang dianggap kontinu
- WD: (string) Arah angin di area tersebut, dianggap sebagai kategorikal.
- WSPM () Kecepatan angin. Diukur dalam (m/s), dianggap sebagai kontinu
- Station(string): Nama lokasi pemantauan kualitas udara. Data terdiri dari 12 lokasi pemantauan di Beijing, dianggap sebagai kategorikal
"""
)

#Load data yang telah diolah
air_quality = pd.read_csv('C:/Users/Muchtar/Documents/Dzaky/DS/Dicoding/Submission_Data Analysis Python/air_quality.csv')
st.table(air_quality.describe(include= 'all'))