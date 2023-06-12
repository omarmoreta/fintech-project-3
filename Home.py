import streamlit as st
import requests
import pandas as pd
import plotly.express as px

# page configurations
st.set_page_config(
    page_title="Crypto Home",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="auto"
)

# page title and banner image
st.title("Crypto Currency Playground")
st.image("./assets/images/banner.jpg")

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

# fetching the crypto data from coincap API and coverting into json/dataframe
url = f"https://api.coincap.io/v2/assets/{selection}/history?interval=d1"
response = requests.get(url)
data = response.json()
df = pd.DataFrame(data["data"])

# formatting date and price column data
df["date"] = pd.to_datetime(df["date"])
df["priceUsd"] = pd.to_numeric(df["priceUsd"])

# creating crypto price line_chart
fig_line = px.line(df, x="date", y="priceUsd")

# creating crypto price scatter plot
fig_scatter = px.scatter(
    df,
    x="date",
    y="priceUsd",
    color="priceUsd",
    color_continuous_scale="reds",
)

# creating crypto price bar chart
fig_bar = px.bar(
    df, 
    x='date', 
    y='priceUsd',
    hover_data=['priceUsd', 'priceUsd'],
    color='priceUsd',
    height=400
)

# plotting the crypto price line chart
st.header(f"{selection} price line chart")
st.plotly_chart(fig_line, theme="streamlit", use_container_width=True)

# creating page columns & bar charts
col1, col2 = st.columns(2)

# plotting crypto price scatter plot
with col1:
    st.header(f"{selection} price scatter plot")
    st.plotly_chart(fig_scatter, theme="streamlit")

# plotting crypto price bar chart
with col2:
    st.header(f"{selection} price bar chart")
    st.plotly_chart(fig_bar, theme="streamlit")

# with open("assets/css/style.css") as file:
#     st.markdown(f"<style>{file.read()}</style>", unsafe_allow_html = True)