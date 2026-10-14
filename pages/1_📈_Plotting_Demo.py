import numpy as np
import pandas as pd
import streamlit as st

st.set_page_config(page_title="Plotting Demo", page_icon="📈")
st.title("Plotting Demo")

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["Series A", "Series B", "Series C"],
)
st.line_chart(chart_data)
st.bar_chart(chart_data)
