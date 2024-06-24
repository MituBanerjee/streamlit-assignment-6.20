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

# Filtered data based on selected category and sub-categories
filtered_df = df[(df['Category'] == selected_category) & (df['Sub_Category'].isin(sub_categories))]

# (3) Line chart for sales of selected sub-categories
if len(sub_categories) > 0:
    st.subheader(f"Line Chart of Sales for Selected Sub-Categories")
    sales_by_sub_category = filtered_df.groupby(['Sub_Category', pd.Grouper(key='Order_Date', freq='M')]).sum().reset_index()

    line_chart = st.line_chart(data=sales_by_sub_category, x='Order_Date', y='Sales', group='Sub_Category')

    # (4) Metrics for selected items in multi-select
    st.subheader(f"Metrics for Selected Items")
    total_sales = filtered_df['Sales'].sum()
    total_profit = filtered_df['Profit'].sum()
    overall_profit_margin = (total_profit / total_sales) * 100 if total_sales != 0 else 0

    st.write(f"Total Sales: ${total_sales:.2f}")
    st.write(f"Total Profit: ${total_profit:.2f}")
    st.write(f"Overall Profit Margin: {overall_profit_margin:.2f}%")

    # (5) Delta in overall profit margin compared to overall average profit margin
    overall_avg_profit_margin = (df['Profit'].sum() / df['Sales'].sum()) * 100 if df['Sales'].sum() != 0 else 0
    profit_margin_delta = overall_profit_margin - overall_avg_profit_margin

    st.write(f"Delta from Overall Average Profit Margin: {profit_margin_delta:.2f}%")

else:
    st.write("Please select at least one sub-category to see the line chart and metrics.")

st.write("## Your additions")
st.write("### (1) add a drop down for Category (https://docs.streamlit.io/library/api-reference/widgets/st.selectbox)")
st.write("### (2) add a multi-select for Sub_Category *in the selected Category (1)* (https://docs.streamlit.io/library/api-reference/widgets/st.multiselect)")
st.write("### (3) show a line chart of sales for the selected items in (2)")
st.write("### (4) show three metrics (https://docs.streamlit.io/library/api-reference/data/st.metric) for the selected items in (2): total sales, total profit, and overall profit margin (%)")
st.write("### (5) use the delta option in the overall profit margin metric to show the difference between the overall average profit margin (all products across all categories)")






