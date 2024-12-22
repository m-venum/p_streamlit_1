"""
# My first app
Here's our first attempt at using data to create a table:
"""

import streamlit as st
import numpy as np
import pandas as pd

st.title("_Streamlit_ is :blue[cool] :sunglasses:")

if st.checkbox('Show dataframe 1'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    chart_data
