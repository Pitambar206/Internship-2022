import streamlit as st
import pandas as pd
import numpy as np
import Home_Page
st.set_page_config(page_title='Pub location')
st.header('Display a map Based on the Local Authority')

Option=st.selectbox('The local Authority',set(Home_Page.df['local_authority']))
submit_button=st.button('Find')
if submit_button:
    df1=Home_Page.df.loc[(Home_Page.df['local_authority']== Option)]
    st.map(df1)