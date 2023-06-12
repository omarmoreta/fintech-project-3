import streamlit as st
import streamlit.components.v1 as components

# page configurations
st.set_page_config(
    page_title="Recess Black Jack",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="auto"
)

# embed blackjack game in iframe
components.iframe(
    "https://thirsty-bhaskara-2f67ea.netlify.app/", 
    height=1200, 
    scrolling=True
)