import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import math

st.title("Data App Assignment, on June 20th")

st.write("### Input Data and Examples")
df = pd.read_csv("Superstore_Sales_utf8.csv", parse_dates=True)
st.dataframe(df)

# This bar chart will not have solid bars--but lines--because the detail data is being graphed independently
st.bar_chart(df, x="Category", y="Sales")

# Now let's do the same graph where we do the aggregation first in Pandas... (this results in a chart with solid bars)

# (1) add a drop down for Category 
category = st.selectbox("Select a Category", df['Category'].unique())

# Using as_index=False here preserves the Category as a column.  If we exclude that, Category would become the datafram index and we would need to use x=None to tell bar_chart to use the index
st.bar_chart(df.groupby("Category", as_index=False).sum(), x="Category", y="Sales", color="#04f")

# (2) add a multi-select for Sub_Category in the selected Category 
sub_categories = st.multiselect("Select Sub_Categories", df[df['Category'] == category]['Sub_Category'].unique())
# Filtered data based on selected category and sub-categories
filtered_df = df[(df['Category'] == selected_category) & (df['Sub_Category'].isin(sub_categories))]


# (3) show a line chart of sales for the selected items in (2)
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
# Aggregating by time

# Here we ensure Order_Date is in datetime format, then set is as an index to our dataframe
df["Order_Date"] = pd.to_datetime(df["Order_Date"])
df.set_index('Order_Date', inplace=True)

# Here the Grouper is using our newly set index to group by Month ('M')
sales_by_month = df.filter(items=['Sales']).groupby(pd.Grouper(freq='M')).sum()

st.dataframe(sales_by_month)

# Here the grouped months are the index and automatically used for the x axis
st.line_chart(sales_by_month, y="Sales")

st.write("## Your additions")
st.write("### (1) add a drop down for Category (https://docs.streamlit.io/library/api-reference/widgets/st.selectbox)")
st.dataframe(df.groupby("Category").sum())
###1category = st.selectbox("Select a Category", df['Category'].unique())

st.write("### (2) add a multi-select for Sub_Category *in the selected Category (1)* (https://docs.streamlit.io/library/api-reference/widgets/st.multiselect)")
###2 sub_categories = st.multiselect("Select Sub_Categories", df[df['Category'] == category]['Sub_Category'].unique())

st.write("### (3) show a line chart of sales for the selected items in (2)")


st.write("### (4) show three metrics (https://docs.streamlit.io/library/api-reference/data/st.metric) for the selected items in (2): total sales, total profit, and overall profit margin (%)")

st.write("### (5) use the delta option in the overall profit margin metric to show the difference between the overall average profit margin (all products across all categories)")






