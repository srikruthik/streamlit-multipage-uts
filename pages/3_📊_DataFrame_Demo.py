import numpy as np
import pandas as pd
import streamlit as st

st.set_page_config(page_title="DataFrame Demo", page_icon="📊")
st.title("DataFrame Demo")

rows = st.slider("Number of rows", min_value=5, max_value=100, value=20)
data = pd.DataFrame({
    "A": np.random.randint(0, 100, rows),
    "B": np.random.randn(rows).round(2),
    "C": np.random.choice(["North", "South", "East", "West"], rows),
})
st.dataframe(data, use_container_width=True)
st.write("Summary statistics")
st.dataframe(data.describe(include="all"), use_container_width=True)
