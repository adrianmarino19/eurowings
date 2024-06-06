import streamlit as st

# URL of the logo image
logo_url = "https://upload.wikimedia.org/wikipedia/commons/b/b4/Eurowings_Logo.svg"
# Display the logo
st.image(logo_url, width=400)

st.write("## Competitor Flight Fare Predictions")

st.write("Provide flight details to get price predictions of Eurowings' competitors.")

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
