import streamlit as st
import pandas as pd
import random
import requests



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
    text_input_1 = st.text_input("Origin Airport")

with col2:
    text_input_2 = st.text_input("Destination Airport")

with col3:
    # Dropdown with options
    text_input_3 = st.selectbox(
        "Cabin class:",
        ["ECONOMY", "BUSINESS", "PREMIUMECONOMY", "FIRST"]
    )

with col4:
    # Dropdown with options
    text_input_4 = st.selectbox(
        "Carrier:",
        ["FR", "U2", "VY", "PC", "W4", "EW", "LH", "W6", "RR", "TK", "A3", "XQ", "TO", "VF", "BA", "LS", "LW", "OS", "W9", "HV"]
    )

# Button
bt = st.button("Let him cook!")

st.write("---")

# Title
st.write("Predicted flight fare:")

# Define the table data
logo_url = "https://1000logos.net/wp-content/uploads/2020/03/Ryanair-Logo.png"  # Updated link
airline_name = "Ryanair"
price = "127 Euro"

# Create a table row using HTML without the second column
html_content = f"""
<div style='display: flex; align-items: center; padding: 10px; border-bottom: 1px solid #ddd;'>
    <div style='flex: 1; text-align: center;'>
        <img src='{logo_url}' alt='Ryanair Logo' style='height: 100px; max-width: 100%; object-fit: contain;' />
    </div>
    <div style='flex: 1; text-align: center; font-size: 20px; color: green;'>
        {price}
    </div>
</div>
"""

# Display the table row
st.markdown(html_content, unsafe_allow_html=True)


if text_input_4 and text_input_1 and text_input_2 and text_input_3 and bt:

    base_url = "https://takeoff-image-jy4h6ma67q-ew.a.run.app/"
    endpoint = "predict"

    params = {
        "OriAirp_input": text_input_1,
        "DestAirp_input": text_input_2,
        "CabClass_input": text_input_3,
        "MainCarr_input": text_input_4
    }

    # Make the GET request
    response = requests.get(f"{base_url}{endpoint}", params=params)

    if response.status_code == 200:

        # Print the response
        st.write(response.json()["price"])
