import streamlit as st
import warnings
warnings.filterwarnings('ignore')
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt  
import seaborn as sns
import statsmodels.api as sm
from statsmodels.tsa.seasonal import seasonal_decompose

color = sns.color_palette()
sns.set_style('darkgrid')

st.title("ARIMA")

df = pd.read_csv('data/product_sales.csv')
df["year"] = df["year"].astype('int')
df["date"] = pd.to_datetime(df["date"], format="%Y-%m-%d")
df.rename(columns={"day": "dayOfYear"})
df["day"] = df["date"].dt.day

result = seasonal_decompose(df['sales'], model='additive', period=365)

fig = plt.figure()
fig = result.plot()
fig.set_size_inches(15, 12)
st.pyplot(fig)