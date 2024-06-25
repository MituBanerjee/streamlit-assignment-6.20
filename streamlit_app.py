import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import math

# Title and input data
st.title("Data App Assignment, on June 20th")
st.write("### Input Data and Examples")

# Load data from CSV
df = pd.read_csv("Superstore_Sales_utf8.csv", parse_dates=['Order_Date'])

# Display the dataframe
st.dataframe(df)

# (1) Dropdown for selecting Category
selected_category = st.selectbox("Select a Category", df['Category'].unique())

# (2) Multi-select for selecting Sub_Categories in the selected Category
sub_categories = st.multiselect("Select Sub-Categories", df[df['Category'] == selected_category]['Sub_Category'].unique())

# Filter data based on selected sub-categories
filtered_df = df[df['Sub_Category'].isin(sub_categories)]

# 3. Show a line chart of sales for the selected items
sales_by_month_filtered = filtered_df.filter(items=['Sales']).groupby(pd.Grouper(freq='M')).sum()
st.line_chart(sales_by_month_filtered, y="Sales")

# 4. Show three metrics for the selected items
total_sales = filtered_df['Sales'].sum()
total_profit = filtered_df['Profit'].sum()
overall_profit_margin = (total_profit / total_sales) * 100 if total_sales != 0 else 0

st.metric("Total Sales", f"${total_sales:,.2f}")
st.metric("Total Profit", f"${total_profit:,.2f}")

# Calculate overall average profit margin for all products across all categories

total_sales_overall = df['Sales'].sum()
total_profit_overall = df['Profit'].sum()
overall_avg_profit_margin = (total_profit_overall / total_sales_overall) * 100 if total_sales_overall != 0 else 0
profit_margin_delta = overall_profit_margin - overall_avg_profit_margin

st.metric("Overall Profit Margin", f"{overall_profit_margin:.2f}%", delta=f"{profit_margin_delta:.2f}%")

st.write("## Your additions")
st.write("### (1) add a drop down for Category (https://docs.streamlit.io/library/api-reference/widgets/st.selectbox)")
st.write("### (2) add a multi-select for Sub_Category *in the selected Category (1)* (https://docs.streamlit.io/library/api-reference/widgets/st.multiselect)")
st.write("### (3) show a line chart of sales for the selected items in (2)")
st.write("### (4) show three metrics (https://docs.streamlit.io/library/api-reference/data/st.metric) for the selected items in (2): total sales, total profit, and overall profit margin (%)")
st.write("### (5) use the delta option in the overall profit margin metric to show the difference between the overall average profit margin (all products across all categories)")






