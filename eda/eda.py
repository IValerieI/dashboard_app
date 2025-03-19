import streamlit as st
import numpy as np
import pandas as pd
import altair as alt

st.title("Анализ данных")
st.write("Датасет содержит информацию о количестве проданного товара за 5 лет. Необходимо предсказать продажи на 3 месяца вперед.")

# Load data - Read CSV into a Pandas DataFrame
df = pd.read_csv('data/product_sales.csv')
df["year"] = df["year"].astype('int')
df["date"] = pd.to_datetime(df["date"], format="%Y-%m-%d")
df.rename(columns={"day": "dayOfYear"})
df["day"] = df["date"].dt.day

# Year selection - Create slider for year range selection
year_list = df["year"].unique()
year_selection = st.slider('Выберите период', 2013, 2017, (2015, 2016))
year_selection_list = list(np.arange(year_selection[0], year_selection[1]+1))

# Sales selection - Create slider for sales range selection
sales_list = df["sales"].unique()
sales_selection = st.slider('Выберите количество', df["sales"].min(), df["sales"].max(), (df["sales"].min(), df["sales"].median()))
sales_selection_list = list(np.arange(sales_selection[0], sales_selection[1]+1))

# Subset data - Filter DataFrame based on selections
df_selection = df[df['year'].isin(year_selection_list) & df['sales'].isin(sales_selection_list)]

# Editable DataFrame - Allow users to made live edits to the DataFrame
df_editor = st.data_editor(df_selection, height=300, use_container_width=True)

st.write("Количество записей после фильтрации:")
st.write(df_editor.shape[0])
st.write("Общий размер датасета:")
st.write(df.shape)
st.write("Описание колонки sales")
st.dataframe(df["sales"].describe(), width=150)

# Display line chart
st.write("Продажи")
chart = alt.Chart(df).mark_line().encode(
            x=alt.X('date:T', title='Дата'),
            y=alt.Y('sales:Q', title='Количество проданного товара')
            ).properties(height=320).interactive()
st.altair_chart(chart, use_container_width=True)

st.write("Графики продаж в зависимости от периода:")

st.write("Различные годы")
df_yearly = pd.pivot_table(df, values='sales', columns='year', index='month')
df_yearly_chart = pd.melt(df_yearly.reset_index(), id_vars='month', var_name='year', value_name='sales')
chart_yearly = alt.Chart(df_yearly_chart).mark_line().encode(
            x=alt.X('month:O', title='Месяц'),
            y=alt.Y('sales:Q', title='Количество проданного товара'),
            color='year:N'
            ).properties(height=320).interactive()
st.altair_chart(chart_yearly, use_container_width=True)

st.write("Различные месяцы")
df_monthly = pd.pivot_table(df, values='sales', columns='month', index='day')
df_monthly_chart = pd.melt(df_monthly.reset_index(), id_vars='day', var_name='month', value_name='sales')
chart_monthly = alt.Chart(df_monthly_chart).mark_line().encode(
            x=alt.X('day:O', title='День'),
            y=alt.Y('sales:Q', title='Количество проданного товара'),
            color='month:N'
            ).properties(height=320).interactive()
st.altair_chart(chart_monthly, use_container_width=True)

st.write("Различные дни недели (по годам)")
df_weekday_years = pd.pivot_table(df, values='sales', columns='year', index='weekday')
df_weekday_years_chart = pd.melt(df_weekday_years.reset_index(), id_vars='weekday', var_name='year', value_name='sales')
chart_weekday_years = alt.Chart(df_weekday_years_chart).mark_line().encode(
            x=alt.X('weekday:O', title='День недели'),
            y=alt.Y('sales:Q', title='Количество проданного товара'),
            color='year:N'
            ).properties(height=320).interactive()
st.altair_chart(chart_weekday_years, use_container_width=True)

st.write("Различные дни недели (по месяцам)")
df_weekday_months = pd.pivot_table(df, values='sales', columns='month', index='weekday')
df_weekday_months_chart = pd.melt(df_weekday_months.reset_index(), id_vars='weekday', var_name='month', value_name='sales')
chart_weekday_months = alt.Chart(df_weekday_months_chart).mark_line().encode(
            x=alt.X('weekday:O', title='День недели'),
            y=alt.Y('sales:Q', title='Количество проданного товара'),
            color='month:N'
            ).properties(height=320).interactive()
st.altair_chart(chart_weekday_months, use_container_width=True)