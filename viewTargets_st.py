

import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
st.set_page_config(page_title="PRIME",page_icon=None,layout="wide")

st.title("Current Confirmed Survey Targets")

    # Fixed URL for the CSV file on GitHub
csv_url_scotland = "https://raw.githubusercontent.com/thePrimeProject/survey-target-viewer/main/updatedTargets%20scotland_W6326%20-%20Prime%20Raw%20Data%20-%20V4%2B5%2B6.csv"
csv_url_england = "https://raw.githubusercontent.com/thePrimeProject/survey-target-viewer/main/updatedTargets%20england_W6326%20-%20Prime%20Raw%20Data%20-%20V4%2B5%2B6.csv"
try:
    df_scot = pd.read_csv(csv_url_scotland)
    df_eng = pd.read_csv(csv_url_england)
    st.header("Scotland:")
    st.table(df_scot)
    st.header("England:")
    st.table(df_eng)
except pd.errors.ParserError:
    st.error("Failed to parse CSV file. Please make sure the URL is correct.")
