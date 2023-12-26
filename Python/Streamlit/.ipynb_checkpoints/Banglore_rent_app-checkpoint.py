import streamlit as st
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt



df = pd.read_csv("bengaluru_house_prices.csv")
df = df.dropna()


st.write("""
# Banglore Rent
"""
)

st.write(df.head(5))

st.scatter_chart(df, x="balcony",y="price")

X = df[["bath","balcony"]]
Y = df[["price"]]

from sklearn.linear_model import LinearRegression
regressor= LinearRegression()

regressor.fit(X,Y)


bth = st.slider('Number of baths',1,9,2)
blc = st.slider('Number of balcony',0,3,1)


# bth =2
# blc =1

lst = [[bth,blc]]
   
df_input = pd.DataFrame(lst, columns =['bath', 'balcony'])
    
X_pred = pd.DataFrame(df_input)

Y_pred=regressor.predict(X_pred)

st.write("Predicted price of your property is:" )
st.write(Y_pred)
