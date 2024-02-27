import requests
import pandas as pd
import streamlit as st
import json
import requests


st.title("How much is your home worth?")
st.text("House price predictor by MerMade")

subproperty = st.selectbox(
    'What type of subproperty?',
    ("Apartment", "House"))

bedrooms = st.selectbox(
    'How many bedrooms?',
    (1, 2, 3, 4, 5, 6))


# The URL of your FastAPI endpoint
url = "https://immo-eliza-deployment-20bn.onrender.com/predict"

# The structured request payload
payload = {
    "num_features": {
        "zip_code": 1000,
        "nbr_bedrooms": bedrooms
        },   
    "fl_features": {
        "fl_terrace": 0
        },   
    "cat_features": {
        #"subproperty_type": subproperty, gives an error
        "epc": "A"
        } 
    }

# payload = {
#     "num_features": {
#         "construction_year": 2000,
#         "latitude": 50.8503,
#         "longitude": 4.3517,
#         "total_area_sqm": 100.0,
#         "surface_land_sqm": 500.0,
#         "nbr_frontages": 2.0,
#         "nbr_bedrooms": bedrooms,
#         "terrace_sqm": 10.0,
#         "primary_energy_consumption_sqm": 250.0,
#         "cadastral_income": 1000.0,
#         "garden_sqm": 50.0,
#         "zip_code": 1000
#     },
#     "fl_features": {
#         "fl_terrace": 0,
#         "fl_open_fire": 0,
#         "fl_swimming_pool": 0,
#         "fl_garden": 0,
#         "fl_double_glazing": 1
#     },
#     "cat_features": {
#         "subproperty_type": subproperty,
#         "locality": "Brussels",
#         "equipped_kitchen": "NOT_INSTALLED",
#         "state_building": "TO_RENOVATE",
#         "epc": "MISSING"
#     }
# }

# Sending the POST request to your FastAPI endpoint
response = requests.post(url, json=payload)

# Print out the response to see the prediction
#print(response.json())

# Check if the response is successful
if response.status_code == 200:
    # Print out the CSV response directly
    print(response.text)  # Prints the CSV formatted text directly to the console
else:
    # Handle errors
    print(f"Failed to get response: {response.status_code}")
    print(response.text)

st.text("Response from API:")
price = st.button("Get Price", type="primary")

if price:
    st.text(response.text)


# ## Testing other visualization method
# data_df = pd.DataFrame(
#     {
#         "Price Range": [20, 950, 250, 500],
#     }
# )

# st.data_editor(
#     data_df,
#     column_config={
#         "Price Range": st.column_config.NumberColumn(
#             "Price (in Euros)",
#             help="The price of your future home",
#             min_value=0,
#             max_value=1000,
#             step=1,
#             format="€%d",
#         )
#     },
#     hide_index=True,
# )


##----- Pseudo code app request---

# dict_api = {
#     param1: subproperty
# }

# r = request.get(dict_api, URL API)

# json.load(r)
