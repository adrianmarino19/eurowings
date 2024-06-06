import streamlit as st

# URL of the logo image
logo_url = "https://upload.wikimedia.org/wikipedia/commons/b/b4/Eurowings_Logo.svg"
# Display the logo
st.image(logo_url, width=400)

st.write("### Test different pricing options for Eurowings flights and get an analysis of their respective impacts on market share and revenue.")

# Custom CSS to change the slider color
st.markdown(
    """
    <style>
    /* Change the color of the slider track */
    .stSlider > div > div > div:nth-child(2) > div {
        background: #AF1F65;  /* Change this to your desired color */
    }

    /* Change the color of the slider thumb */
    .stSlider > div > div > div:nth-child(3) > div {
        background-color: #AF1F65;  /* Change this to your desired color */
        border: 2px solid #AF1F65;  /* Change the border color if needed */
    }

    /* Adjust the track fill color to match the track */
    .stSlider > div > div > div:nth-child(2) > div > div {
        background: #AF1F65;  /* Change this to match the track color */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Add a slider to the app
slider_value = st.slider(
    label="Select a value",
    min_value=0,
    max_value=100,
    value=50,  # Default value
    step=1
)


# Create two columns
col1, col2 = st.columns(2)

# Add metrics to the first column
with col1:
    st.metric(label="Market Share", value="70%", delta="+15")

    st. write("What percentage of the redirects (potential customers) for the specific flights EW is competing for will they capture from competitors?")

# Add metrics to the second column
with col2:
    st.metric(label="Revenue", value="100 Million", delta="+2%")

    st. write("How will these pricing changes impact the revenue?")
