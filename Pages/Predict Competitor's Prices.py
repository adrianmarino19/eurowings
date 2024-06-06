import streamlit as st
import pandas as pd
import random


# URL of the logo image
logo_url = "https://upload.wikimedia.org/wikipedia/commons/b/b4/Eurowings_Logo.svg"
# Display the logo
st.image(logo_url, width=400)

st.write("## Competitor Flight Fare Predictions")

st.write("Provide flight details to get price predictions of Eurowings' competitors.")

st.write("---")

# Create four columns
col1, col2, col3, col4 = st.columns(4)

# Place text fields in the columns
with col1:
    text_input_1 = st.text_input("Origin")

with col2:
    text_input_2 = st.text_input("Destination")

with col3:
    text_input_2 = st.date_input("Date")

with col4:
    text_input_2 = st.time_input("Time")

# Button
st.button("Let him cook!")

import streamlit as st

st.write("---")

st.write("Predicted Flight Fares:")


# Define the competitors and dummy fares
competitors = [
    "Ryanair",
    "EasyJet",
    "Norwegian Air Shuttle",
    "Wizz Air",
    "Vueling Airlines",
    "Transavia",
    "Air Europa",
    "Germanwings",
    "TUI Airways",
    "Condor"
]

# Generate random realistic prices in the range of $100 to $170 for each competitor
dummy_fares = [round(random.uniform(100, 170)) for _ in range(len(competitors))]

# Create a DataFrame
data = {'Competitor': competitors, 'Flight Price': dummy_fares}
df = pd.DataFrame(data)

# Display the table in Streamlit
st.table(df)
