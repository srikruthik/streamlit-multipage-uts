import numpy as np
import pandas as pd
import streamlit as st

st.set_page_config(page_title="Mapping Demo", page_icon="🌍")
st.title("Mapping Demo")

st.write("Explore randomly generated locations around San Francisco.")
map_data = pd.DataFrame({
    "lat": 37.76 + np.random.randn(100) / 100,
    "lon": -122.4 + np.random.randn(100) / 100,
})
st.map(map_data)
