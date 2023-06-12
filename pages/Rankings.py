import streamlit as st
import requests

# page configurations
st.set_page_config(
    page_title="Crypto Ranking",
    page_icon="💰",
    initial_sidebar_state="auto"
)

# function to fetch coincap api and return the crypto data
def get_crypto():
    url = "https://api.coincap.io/v2/assets"
    params = {"limit": 10, "sort": "marketCap"}
    response = requests.get(url, params=params)
    data = response.json()
    return data["data"]

# creating four functions to format the data being used from each column
# price format function
def format_price(price):
    return f"${float(price):,.2f}"

# market cap format function
def format_market_cap(market_cap):
    market_cap = float(market_cap) / 1_000_000_000
    return f"${market_cap:.2f}B"

# max supply or volume function
def format_max_supply_or_volume(sup_or_vol):
    if float(sup_or_vol) > 1_000_000_000:
        sup_or_vol = float(sup_or_vol) / 1_000_000_000
        return f"{sup_or_vol:.2f}B"
    else:
        sup_or_vol = float(sup_or_vol) / 1_000_000
        return f"{sup_or_vol:.2f}M"

# daily change format function
def format_daily_change(daily_change):
    return f"{float(daily_change):,.2f}%"

# calling the fetch API function to return the data
data = get_crypto()

# page title and subheader
st.title("Crypto Market Data")
st.markdown("Top 10 Cryptocurrencies by Market Cap")

# looping over the data, calling formatting functions, and creating a table to display the data
for currency in data:
    rank = currency["rank"]
    name = currency["name"]
    symbol = currency["symbol"]
    supply = format_max_supply_or_volume(currency["supply"])
    price = format_price(currency["priceUsd"])
    market_cap = format_market_cap(currency["marketCapUsd"])
    daily_change = format_daily_change(currency["changePercent24Hr"])
    daily_volume = format_max_supply_or_volume(currency["volumeUsd24Hr"])
    
    # creating a subheader for each row
    st.subheader(f"#{rank} - {symbol}: {name}")
    
    # creating four columns
    col1, col2, col3, col4 = st.columns(4)
    
    # adding the different data points in each column
    with col1:
        st.metric("Price", price, daily_change)
    with col2:
        st.metric("Market Cap", market_cap)
    with col3:
        st.metric("Supply", supply)
    with col4:
        st.metric("Daily Volume", daily_volume)
    
    # separator line
    st.write("---")