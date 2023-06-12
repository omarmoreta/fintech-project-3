import streamlit as st
from pages.Rankings import *
import pandas as pd
import plotly.express as px

# page configurations
st.set_page_config(
    page_title="Crypto Filtering",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="auto"
)

# list of crypto to select from dropdown
crypto_list = ['bitcoin', 
               'ethereum', 
               'tether',
               'usd-coin', 
               'xrp', 
               'dogecoin', 
               'solana', 
               'polygon'
               ]

# dropdown in the sidebar for crypto selection
with st.sidebar:
    selection = st.selectbox('Select Crypto', crypto_list)

data = get_crypto()
df = pd.DataFrame(data)
df = df.drop(columns=["maxSupply", "explorer", "rank", "id"])
df