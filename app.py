import pandas as pd
import streamlit as st
import plotly.express as px

st.title(":chart:, Pandas Data Dashboard")
st.write('Upload CSV file and visualize data with charts')

file_uploaded = st.file_uploader('Upload Your CSV file', type=['csv'])

if file_uploaded is not None:
    try:
        df = pd.read_csv(file_uploaded)
        st.dataframe(df.head())
        st.success('CSV file Uploaded Successfully')

    except Exception as e:
        st.error('Error While reading File')
        st.write(e)

else:
    st.info('Please Upload a .csv file')

if file_uploaded is not None:
    columns_name = df.columns.tolist()

    chart = st.selectbox('Select Chart Type', ["Bar Chart", "Line Chart", "Pie Chart"])

    if chart in ["Bar Chart", "Line Chart"]:
        x_column = st.selectbox('Select X-axis', columns_name)
        y_column = st.selectbox('Select Y-axis', columns_name)
        st.write('You Selected: ', x_column, 'and', y_column)

        if chart == "Bar Chart":

            chart_data = df[[x_column, y_column]].set_index(x_column)
            st.bar_chart(chart_data)

        elif chart == "Line Chart":

            chart_data = df[[x_column, y_column]].set_index(x_column)
            st.line_chart(chart_data)

    elif chart in ["Pie Chart"]:
        pie_chart = st.selectbox('Select Category Column', columns_name)
        value_column = st.selectbox('Select Value Column', columns_name)

        fig = px.pie(
            df,
            names=pie_chart,      # categories
            values=value_column,   # values
            title="Pie Chart Distribution"
        )

        st.plotly_chart(fig)