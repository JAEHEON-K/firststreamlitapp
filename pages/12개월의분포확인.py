import streamlit as st
import pandas as pd
import plotly.express as px

# Load the dataset
data_path = 'daily_temp.csv'
data = pd.read_csv(data_path)

# Preprocess the data
data['날짜'] = pd.to_datetime(data['날짜'])
data['월'] = data['날짜'].dt.month

# Handle missing values (drop rows with missing temperature data)
data = data.dropna(subset=['평균기온(℃)', '최저기온(℃)', '최고기온(℃)'])

# Streamlit app
def main():
    st.title("12달의 기온 분포 시각화")
    
    # Melt the data for easier plotting
    melted_data = data.melt(
        id_vars=['월'], 
        value_vars=['평균기온(℃)', '최저기온(℃)', '최고기온(℃)'], 
        var_name='기온 유형', 
        value_name='온도 (℃)'
    )

    # Create an interactive boxplot using Plotly
    fig = px.box(
        melted_data, 
        x='월', 
        y='온도 (℃)', 
        color='기온 유형', 
        title='월별 기온 분포',
        labels={"월": "월", "온도 (℃)": "온도 (℃)"},
        category_orders={"월": list(range(1, 13))}
    )

    # Display the plot
    st.plotly_chart(fig)

if __name__ == "__main__":
    main()

