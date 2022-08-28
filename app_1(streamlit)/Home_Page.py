import streamlit as st
import pandas as pd
import numpy as np

st.title('Welcome to  Open pub')

st.text('Data Set :')
cols=['fsa_id','name','address','postcode','easting','northing','latitude','longitude','local_authority']
df=pd.read_csv('data\open_pubs.csv',names=cols)
st.dataframe(df.head())
st.write('No of rows & columns :',df.shape)
df=df.replace('\\N',np.NaN)
df=df.dropna()
df.isnull().sum()
df[['latitude','longitude']]=df[['latitude','longitude']].apply(pd.to_numeric)
st.write('* Summary Statistics of Nummerical Columns :')

st.write(df.describe())





