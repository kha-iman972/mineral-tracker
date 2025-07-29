
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from datetime import datetime

CSV_FILE = 'mineral_data.csv'
minerals = ['Nitrogen', 'Phosphorus', 'Potassium', 'Magnesium', 'Calcium', 'Iron']
target_ranges = {
    'Nitrogen': (50, 80), 'Phosphorus': (25, 40), 'Potassium': (90, 130),
    'Magnesium': (30, 50), 'Calcium': (120, 180), 'Iron': (3.5, 5.5)
}

def load_data():
    try:
        df = pd.read_csv(CSV_FILE)
        df['Date'] = pd.to_datetime(df['Date'])
        return df
    except:
        return pd.DataFrame(columns=['Date'] + minerals)

def save_entry(entry):
    df = load_data()
    df = pd.concat([df, pd.DataFrame([entry])], ignore_index=True)
    df.to_csv(CSV_FILE, index=False)

st.title("🌿 Mineral Tracker Dashboard")
with st.form("entry_form"):
    st.subheader("Add New Mineral Entry")
    values = {m: st.number_input(f"{m} (ppm)", 0.0, 500.0, 0.0) for m in minerals}
    if st.form_submit_button("Submit Entry"):
        save_entry({"Date": datetime.now(), **values})
        st.success("✅ Entry added!")

df = load_data()
if not df.empty:
    st.subheader("📋 Recent Data")
    st.dataframe(df.tail(10))
    st.subheader("📊 Mineral Charts")
    for m, (low, high) in target_ranges.items():
        fig, ax = plt.subplots()
        ax.plot(df['Date'], df[m], marker='o', label=m)
        ax.axhspan(0, low, color='red', alpha=0.1)
        ax.axhspan(low, high, color='green', alpha=0.1)
        ax.axhspan(high, df[m].max()+10, color='orange', alpha=0.1)
        ax.set_title(f"{m} Over Time")
        ax.legend()
        st.pyplot(fig)
