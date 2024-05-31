import streamlit as st
import pandas as pd

st.title("hello. world")
st.write("hehe")

chart_data = pd.DataFrame([[1,2,3], [4,5,6]], columns=['a','b','c'])
st.line_chart(chart_data)