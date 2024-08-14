import streamlit as st
import pandas as pd

import preprocessor, helper

st.sidebar.title('Olympics Analysis')

user_menu = st.sidebar.radio(
    'Select an option',
    ('Medal Tally', 'Overall Analysis', 'Country-wise Analysis', 'Athelete Wise Analysis')
)

df = preprocessor.preprocess()

if user_menu == 'Medal Tally':
    st.sidebar.header('Medla Tally')
    medal_tally = helper.medal_tally(df)
    year, country = helper.country_year_list(df)

    selected_year = st.sidebar.selectbox('Select Year', year)
    selected_country = st.sidebar.selectbox('Select Country', country)

    x = helper.fetch_medal_tally(df , selected_year , selected_country)

    st.table(x)

