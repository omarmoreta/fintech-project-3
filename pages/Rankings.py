import streamlit as st
import requests
import plotly.graph_objects as go

st.set_page_config(
    page_title="Crypto Ranking",
    page_icon="💰",
    # layout="wide",
    initial_sidebar_state="auto"
)

st.title("Crypto Market Data")
st.markdown("Top 10 Cryptocurrencies by Market Cap")

def get_crypto():
    url = "https://api.coincap.io/v2/assets"
    params = {"limit": 10, "sort": "marketCap"}
    response = requests.get(url, params=params)
    data = response.json()
    return data["data"]

def format_price(price):
    return f"${float(price):,.2f}"

def format_market_cap(market_cap):
    market_cap = float(market_cap) / 1_000_000_000
    return f"${market_cap:.2f}B"

def format_max_supply_or_volume(sup_or_vol):
    if float(sup_or_vol) > 1_000_000_000:
        sup_or_vol = float(sup_or_vol) / 1_000_000_000
        return f"{sup_or_vol:.2f}B"
    else:
        sup_or_vol = float(sup_or_vol) / 1_000_000
        return f"{sup_or_vol:.2f}M"

def format_daily_change(daily_change):
    return f"{float(daily_change):,.2f}%"

data = get_crypto()

for currency in data:
    rank = currency["rank"]
    name = currency["name"]
    symbol = currency["symbol"]
    supply = format_max_supply_or_volume(currency["supply"])
    price = format_price(currency["priceUsd"])
    market_cap = format_market_cap(currency["marketCapUsd"])
    daily_change = format_daily_change(currency["changePercent24Hr"])
    daily_volume = format_max_supply_or_volume(currency["volumeUsd24Hr"])
    
    st.subheader(f"#{rank} - {symbol}: {name}")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Price", price, daily_change)
    with col2:
        st.metric("Market Cap", market_cap)
    with col3:
        st.metric("Supply", supply)
    with col4:
        st.metric("Daily Volume", daily_volume)
    
    st.write("---")

