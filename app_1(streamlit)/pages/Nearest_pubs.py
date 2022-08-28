import streamlit as st
import pandas as pd
import numpy as np
import Home_Page
st.set_page_config(page_title='Find the Nearest Pub ')
st.header('Display the nearest pubs on the map')

location=Home_Page.df[['latitude','longitude']]
lat=st.number_input('Enter your longitude')
lon=st.number_input('Enter your latitude')
button=st.button('Show pubs')
new_location=np.array([lat,lon])
dist=np.sqrt(np.sum((new_location-location)**2,axis=1))
n=5
min_indices=np.argpartition(dist,n-1)[:n]
if button:
    st.map(Home_Page.df.iloc[min_indices])