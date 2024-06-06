import streamlit as st

# URL of the logo image
logo_url = "https://upload.wikimedia.org/wikipedia/commons/b/b4/Eurowings_Logo.svg"
# Display the logo
st.image(logo_url, width=400)

st.write("### Test different pricing options for Eurowings flights and get an analysis of their respective impacts on market share and revenue.")

# Add a slider to the app
slider_value = st.slider(
    label="Select a price",
    min_value=0,
    max_value=500,
    value=50,  # Default value
    step=1
)

# Display the value of the slider
st.write(f"Selected price: {slider_value}")


# Create two columns
col1, col2 = st.columns(2)

# Add metrics to the first column
with col1:
    st.metric(label="Market Share", value="70%", delta="+15%")

    st. write("What percentage of the potential customers redirected from specific flights that Eurowings competes for will they manage to capture from their competitors?")

# Add metrics to the second column
with col2:
    st.metric(label="Revenue", value="100 Million", delta="+2%")

    st. write("How will the selected price impact the revenue?")
