import streamlit as st
from pages.Rankings import get_crypto
import pandas as pd

# page configurations
st.set_page_config(
    page_title="Crypto Filtering",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="auto"
)

# page header
st.header("CoinCap API DataFrame")

# fetching the API with imported function
data = get_crypto()
df = pd.DataFrame(data)
df = df.drop(columns=["maxSupply", "explorer", "rank", "id"])
df