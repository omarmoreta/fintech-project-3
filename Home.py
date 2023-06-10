import streamlit as st
import requests
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(
    page_title="Crypto Home",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="auto"
)

st.title("Crypto Currency Playground")
st.image("./assets/images/banner.jpg")

crypto_list = ['bitcoin', 
               'ethereum', 
               'tether',
               'usd-coin', 
               'xrp', 
               'dogecoin', 
               'solana', 
               'polygon'
               ]

with st.sidebar:
    selection = st.selectbox('Select Crypto', crypto_list)

url = f"https://api.coincap.io/v2/assets/{selection}/history?interval=d1"
response = requests.get(url)
data = response.json()
df = pd.DataFrame(data["data"])

df["date"] = pd.to_datetime(df["date"])
df["priceUsd"] = pd.to_numeric(df["priceUsd"])

fig = px.line(df, x="date", y="priceUsd")

st.header(f"{selection} price line chart")
st.plotly_chart(fig, theme="streamlit", use_container_width=True)

fig_scatter = px.scatter(
    df,
    x="date",
    y="priceUsd",
    color="priceUsd",
    color_continuous_scale="reds",
)

fig_bar = px.bar(
    df, 
    x='date', 
    y='priceUsd',
    hover_data=['priceUsd', 'priceUsd'],
    color='priceUsd',
    height=400
)

col1, col2 = st.columns(2)

with col1:
    st.header(f"{selection} price scatter plot")
    st.plotly_chart(fig_scatter, theme="streamlit")

with col2:
    st.header(f"{selection} price bar chart")
    st.plotly_chart(fig_bar, theme="streamlit")

# with open("assets/css/style.css") as file:
#     st.markdown(f"<style>{file.read()}</style>", unsafe_allow_html = True)