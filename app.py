import streamlit as st
import random
import time
import pytz
from datetime import datetime

# Set timezone to UTC+3
local_tz = pytz.timezone('Africa/Nairobi')
now = datetime.now(local_tz)

# Page settings
st.set_page_config(page_title="BILOW Binary AI", layout="centered")
st.markdown("<h2 style='text-align:center;'>📲 BILOW Signal Bot</h2>", unsafe_allow_html=True)
st.markdown(f"**Time (UTC+3):** {now.strftime('%Y-%m-%d %H:%M:%S')}")

# Pairs and signals
pairs = ["EUR/USD", "GBP/USD", "AUD/USD", "USD/JPY"]
signals = ["📈 BUY (UP)", "📉 SELL (DOWN)", "⏳ WAIT"]
expiry = st.selectbox("Select Expiry", ["5s", "10s", "15s", "30s", "1m"])

for pair in pairs:
    if st.button(f"Get Signal for {pair}"):
        with st.spinner(f"Analyzing {pair}..."):
            time.sleep(random.uniform(1, 2))
        signal = random.choice(signals)
        st.success(f"{pair} | Signal: {signal} | Expiry: {expiry}")
