

import streamlit as st
import streamlit.components.v1 as components
import pandas as pd

st.title("Current Confirmed Targets")

    # Fixed URL for the CSV file on GitHub
csv_url_scotland = "https://raw.githubusercontent.com/thePrimeProject/surveyTargetCalculation/main/updatedTargets%20scotland_W6326%20-%20Prime%20Raw%20Data%20-%20V4%2B5%2B6.csv?token=GHSAT0AAAAAACEWCQWE7JFMAEJ6IK3ZRXPMZFRJTVA"
csv_url_england = "https://raw.githubusercontent.com/thePrimeProject/surveyTargetCalculation/main/updatedTargets%20england_W6326%20-%20Prime%20Raw%20Data%20-%20V4%2B5%2B6.csv?token=GHSAT0AAAAAACEWCQWFGGEXEXCC5TX3Z63OZFRJO3A"
try:
    df_scot = pd.read_csv(csv_url_scotland)
    df_eng = pd.read_csv(csv_url_england)
    st.header("Scotland:")
    st.dataframe(df_scot)
    st.header("England:")
    st.dataframe(df_eng)
except pd.errors.ParserError:
    st.error("Failed to parse CSV file. Please make sure the URL is correct.")
