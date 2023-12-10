import streamlit as st
import pandas as pd
def data():
    data=pd.read_csv(r'Data.csv')
    data.drop('Unnamed: 0', axis=1, inplace=True)
    st.write(data)

    File = data.to_csv()
    st.download_button(
        label="Download data as CSV",
        data=File,
        file_name='Spotify Data.csv',
        mime='text/csv', )
