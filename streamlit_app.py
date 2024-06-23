import streamlit as st
import pandas as pd
import altair as alt

# Title and input data
st.title("Data App Assignment, on June 20th")
st.write("### Input Data and Examples")

# Load data from CSV
df = pd.read_csv("Superstore_Sales_utf8.csv", parse_dates=['Order_Date'])

# Display the dataframe
st.dataframe(df)

# Dropdown for selecting Category
selected_category = st.selectbox("Select a Category", df['Category'].unique())

# Multi-select for selecting Sub_Categories in the selected Category
sub_categories = st.multiselect("Select Sub-Categories", df[df['Category'] == selected_category]['Sub_Category'].unique())

# Filtered data based on selected category and sub-categories
filtered_df = df[(df['Category'] == selected_category) & (df['Sub_Category'].isin(sub_categories))]

# Bar chart without aggregation
st.subheader(f"Bar Chart for Category: {selected_category}")
st.bar_chart(filtered_df, x="Sub_Category", y="Sales")

# Bar chart with aggregation (solid bars)
st.subheader(f"Aggregated Bar Chart for Category: {selected_category}")
sales_by_category = filtered_df.groupby("Sub_Category", as_index=False).sum()
st.bar_chart(sales_by_category, x="Sub_Category", y="Sales", color="#04f")

# Line chart for sales of selected sub-categories
if len(sub_categories) > 0:
    st.subheader(f"Line Chart of Sales for Selected Sub-Categories")
    sales_by_sub_category = filtered_df.groupby(['Sub_Category', pd.Grouper(key='Order_Date', freq='M')]).sum().reset_index()

    line_chart = alt.Chart(sales_by_sub_category).mark_line().encode(
        x='Order_Date:T',
        y='Sales:Q',
        color='Sub_Category:N',
        tooltip=['Order_Date', 'Sales', 'Sub_Category']
    ).properties(
        width=800,
        height=400
    ).interactive()

    # Display the line chart using Altair
    st.altair_chart(line_chart)
else:
    st.write("Please select at least one sub-category to see the line chart.")

st.write("## Your additions")
st.write("### (1) add a drop down for Category (https://docs.streamlit.io/library/api-reference/widgets/st.selectbox)")
st.dataframe(df.groupby("Category").sum())
###1category = st.selectbox("Select a Category", df['Category'].unique())

st.write("### (2) add a multi-select for Sub_Category *in the selected Category (1)* (https://docs.streamlit.io/library/api-reference/widgets/st.multiselect)")
###2 sub_categories = st.multiselect("Select Sub_Categories", df[df['Category'] == category]['Sub_Category'].unique())

st.write("### (3) show a line chart of sales for the selected items in (2)")


st.write("### (4) show three metrics (https://docs.streamlit.io/library/api-reference/data/st.metric) for the selected items in (2): total sales, total profit, and overall profit margin (%)")

st.write("### (5) use the delta option in the overall profit margin metric to show the difference between the overall average profit margin (all products across all categories)")






