import streamlit as st

st.set_page_config(page_title="Hello", page_icon="👋")

st.title("Welcome to Streamlit! 👋")
st.sidebar.success("Select a demo above.")

st.markdown("""
Streamlit is an open-source app framework built for data science and machine learning.

**Choose a demo from the sidebar** to explore plotting, mapping, and dataframes.

### Learn more
- [Streamlit](https://streamlit.io)
- [Documentation](https://docs.streamlit.io)
- [Community forum](https://discuss.streamlit.io)
""")
