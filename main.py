import streamlit as st 
import pandas as pd
import numpy as np
import altair as alt
import plotly.express as pt
st.header("Hii There, What's UP!!")
st.write('Hello, *World!* :sunglasses:')

df2 = pd.DataFrame(
     np.random.randn(200, 3),
     columns=['a', 'b', 'c'])
c = alt.Chart(df2).mark_square().encode(
    x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
fig=pt.scatter_3d(df2,x="a",y="b",z="c",color="c")
st.write(fig)