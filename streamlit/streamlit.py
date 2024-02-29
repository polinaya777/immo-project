import pandas as pd
import requests
import streamlit as st


# Define the sidebar navigation
page = st.sidebar.selectbox("Choose a page", ["Home", "Price prediction", "Contacts"])

# Define the content of the Home page
if page == "Home":
    # Display a logo (logo.png should be in the same directory as your script)
    # 'st.image("logo.png")

    # Display some colored text
    st.markdown("""
        <style>
        .red-text {
            color: red;
        }
        .blue-text {
            color: blue;
        }
        </style>

        Welcome to our Immo Prediction <span class="red-text">API</span> 
        Are your going to buy or sell <span class="blue-text">a house or apartment?</span>
        """, unsafe_allow_html=True)

    
# Define the content of the Price prediction page
elif page == "Price prediction":
    
    # The URL of FastAPI endpoint
    url = "https://projects-immo-latest.onrender.com/predict"
    
    st.title("How much is your home worth?")
    st.text("House price predictor by MerMade")
    st.markdown("""
    This is the price prediction page. Here you can predict prices.
    """)

    # Streamlit app title
    st.title("Real Estate Price Prediction")
    st.text("by MerMade")

    dataLocality = pd.read_csv("data/locality_zip_codes.csv")


    #sylvan Order:

    col1, col2 = st.columns(2)

    with col1:
        subproperty_type = st.selectbox("Subproperty Type", ("APARTMENT","APARTMENT_BLOCK","BUNGALOW","CASTLE","CHALET","COUNTRY_COTTAGE","EXEPTIONAL_PROPERTY", "DUPLEX","FARMHOUSE", "FLAT_STUDIO","GROUND_FLOOR","LOFT","KOT","MANOR_HOUSE","MANSION","MIXED_USE_BUILDING","PENTHOUSE","SERVICE_FLAT","TOWN_HOUSE","TRIPLEX","VILLA", "HOUSE","OTHER_PROPERTY"))
        state_building = st.selectbox("Building State", ("MISSING","AS_NEW","GOOD","JUST_RENOVATED","TO_RESTORE","TO_RENOVATE","TO_BE_DONE_UP"))
    
        locality = st.selectbox("Locality", ("Aalst","Antwerp","Arlon","Ath","Bastogne","Brugge","Brussels","Charleroi","Dendermonde","Diksmuide","Dinant","Eeklo","Gent","Halle-Vilvoorde","Hasselt","Huy","Ieper","Kortrijk","Leuven","Liège","Maaseik","Marche-en-Famenne","Mechelen","Mons","Mouscron","Namur","Neufchâteau","Nivelles","Oostend","Oudenaarde","Philippeville","Roeselare","Sint-Niklaas","Soignies","Thuin","Tielt","Tongeren","Tournai","Turnhout","Verviers","Veurne","Virton","Waremme"))
        if locality:
            data = dataLocality[dataLocality['locality'] == f"{locality}"]
            zip_code = st.selectbox("ZIP Code",data['zip_code'].to_list())
        
        construction_year = st.number_input("Construction Year", value=2000, min_value=1800, max_value=2024)
        total_area_sqm = st.number_input("Total Area in sqm", value=10,min_value=10,max_value=15000)
        nbr_bedrooms = st.number_input("Number of Bedrooms", value=2, min_value=1, max_value=100)

    with col2:

        equipped_kitchen = st.selectbox("Equipped Kitchen", ("MISSING", "INSTALLED", "HYPER_EQUIPPED","SEMI_EQUIPPED","NOT_INSTALLED","USA_UNINSTALLED","USA_HYPER_EQUIPPED","USA_SEMI_EQUIPPED",))
        surface_land_sqm = st.number_input("Land Area in sqm", value=150, min_value=10, max_value=1000000)
        nbr_frontages = st.number_input("Number of Frontages", value=0, min_value=0, max_value=10)
        epc = st.selectbox("Energy Performance Certificate", ("MISSING", "A","B","C","D","E","F"))
        fl_double_glazing = st.checkbox("Double Glazing", value=True)  
        fl_open_fire = st.checkbox("Open Fire")  
        fl_terrace = st.checkbox("Terrace")
        if fl_terrace:
            terrace_sqm = st.number_input("Terrace Area in sqm", value=10, min_value=10, max_value=500)
        else :
            terrace_sqm = 0
        fl_garden = st.checkbox("Garden")
        if fl_garden:
            garden_sqm = st.number_input("Garden Area in sqm", value=10, min_value=10, max_value=1000000)
        else:
            garden_sqm = 0

        fl_swimming_pool = st.checkbox("Swimming Pool")
        

    # Input manualy this
    latitude = 0
    longitude = 0
    primary_energy_consumption_sqm = 0
    cadastral_income = 0

    payload = {
            "num_features": {
                "construction_year": construction_year,
                "latitude": latitude,
                "longitude": longitude,
                "total_area_sqm": total_area_sqm,
                "surface_land_sqm": surface_land_sqm,
                "nbr_frontages": nbr_frontages,
                "nbr_bedrooms": nbr_bedrooms,
                "terrace_sqm": terrace_sqm,
                "primary_energy_consumption_sqm": primary_energy_consumption_sqm,
                "cadastral_income": cadastral_income,
                "garden_sqm": garden_sqm,
                "zip_code": zip_code
            },
            "fl_features": {
                "fl_terrace": int(fl_terrace),
                "fl_open_fire": int(fl_open_fire),
                "fl_swimming_pool": int(fl_swimming_pool),
                "fl_garden": int(fl_garden),
                "fl_double_glazing": int(fl_double_glazing)
            },
            "cat_features": {
                "subproperty_type": subproperty_type,
                "locality": locality,
                "equipped_kitchen": equipped_kitchen,
                "state_building": state_building,
                "epc": epc
            }
        }


    # Button to send the request
    if st.button("Predict Price"):
        
        response = requests.post(url, json=payload)
        
        if response.status_code == 200:
            # Convert the response content to a Python dictionary
            response_data = response.json()
            # Extract values from response and display the prediction result
            predicted_price = response_data.get("Prediction of price", "No prediction")
            price_range = response_data.get("Price range based on model accuracy", "No range provided")
            st.markdown(f"### Predicted Price: {predicted_price}")
            st.markdown(f"### Price Range Based on Model Accuracy: {price_range}")
            
        else:
            # Handle errors
            st.error(f"Failed to get response: {response.status_code}")
            print(response.text)



# Define the content of the Contacts page
elif page == "Contacts":
    st.title("Contacts")
    st.markdown("""
    This is the contacts page. Here you can find our contact information.
    """)
    st.subheader("Contact Information")
    st.markdown("""
    **Email:**
    **Phone:**
    """)

    