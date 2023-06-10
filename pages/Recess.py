import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Recess Black Jack",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="auto"
)

# embed streamlit docs in a streamlit app
components.iframe(
    "https://thirsty-bhaskara-2f67ea.netlify.app/", 
    # width=, 
    height=1200, 
    scrolling=True
)