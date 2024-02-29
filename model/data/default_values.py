import pandas as pd


def default_values (data_set):
    data = pd.read_csv(data_set)
    print(data.head(3))
    
    cat_features = [
        #"property_type"
        "subproperty_type",
        "locality",
        "equipped_kitchen",
        "state_building",
        "epc"
    ]

    num_features = [
        "construction_year",
        "latitude",
        "longitude",
        "total_area_sqm",
        "surface_land_sqm",
        "nbr_frontages",
        "nbr_bedrooms",
        "terrace_sqm",
        "primary_energy_consumption_sqm",
        "cadastral_income",
        "garden_sqm",
        "zip_code"
    ]

    fl_features = [
        "fl_terrace",
        "fl_open_fire",
        "fl_swimming_pool",
        "fl_garden",
        "fl_double_glazing",
        #"fl_floodzone", 
        #"fl_furnished"
    ]

    # Create default values dictionary
    default_values = {}
    
    # Assign default values for categorical features
    for cat_feature in cat_features:
        default_values[cat_feature] = 'MISSING'

    # Assign default values for boolean features
    for fl_feature in fl_features:
        default_values[fl_feature] = 0

    # Assign default values for numerical features (using mean)
    for num_feature in num_features:
        default_values[num_feature] = data[num_feature].mean()

    # Create DataFrame with default values
    default_values_df = pd.DataFrame(default_values, index=[0])
    print (default_values_df.head())

    default_values_df.to_csv("default_values.csv", index=False)

    

    

default_values("data/properties_small.csv")