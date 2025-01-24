import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

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
    st.title("월별 기온 분포 시각화")
    
    # Sidebar for month selection
    selected_month = st.sidebar.selectbox("월을 선택하세요:", range(1, 13))
    
    # Filter data for the selected month
    filtered_data = data[data['월'] == selected_month]
    
    if filtered_data.empty:
        st.warning(f"선택한 {selected_month}월에 해당하는 데이터가 없습니다.")
    else:
        st.subheader(f"{selected_month}월 기온 분포")
        
        # Create a boxplot
        fig, ax = plt.subplots(figsize=(8, 6))
        filtered_data[['평균기온(℃)', '최저기온(℃)', '최고기온(℃)']].boxplot(ax=ax)
        ax.set_title(f"{selected_month}월 기온 분포")
        ax.set_ylabel("온도 (℃)")
        plt.xticks([1, 2, 3], ['평균기온', '최저기온', '최고기온'])
        
        # Display the plot
        st.pyplot(fig)

if __name__ == "__main__":
    main()
