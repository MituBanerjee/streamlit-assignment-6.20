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

# (3) show a line chart of sales for the selected items in (2)

# Filter data based on selected category and sub-categories
    filtered_data = df[(df['Category'] == category) & (df['Sub_Category'].isin(sub_categories))]

    # Line chart using Altair
    line_chart = alt.Chart(filtered_data).mark_line().encode(
        x='Date:T',  # 'T' indicates temporal data (dates)
        y='Sales:Q',  # 'Q' indicates quantitative data (sales)
        color='Sub_Category:N',  # 'N' indicates nominal data (sub-categories)
        tooltip=['Date', 'Sales', 'Sub_Category']
    ).properties(
        width=800,
        height=400
    ).interactive()

    # Display line chart
    st.altair_chart(line_chart, use_container_width=True)

if __name__ == "__main__":
    main()






    
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






