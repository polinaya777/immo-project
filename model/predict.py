import joblib
import pandas as pd
from sklearn.metrics import mean_absolute_error


def predict(input_dataset, output_dataset):
    """Predicts house prices from 'input_dataset', stores it to 'output_dataset'."""
    # Load the data
    data = pd.read_csv(input_dataset)

    
    # Load the model artifacts using joblib
    artifacts = joblib.load("model/Gradient_boost_artifacts.joblib")


    # Unpack the artifacts
    num_features = artifacts["features"]["num_features"]
    fl_features = artifacts["features"]["fl_features"]
    cat_features = artifacts["features"]["cat_features"]
    imputer = artifacts["imputer"]
    enc = artifacts["enc"]
    model = artifacts["model"]


    # Extract the used data
    data_extr = data[num_features + fl_features + cat_features]


    # Apply imputer and encoder on data
    data_extr[num_features] = imputer.transform(data_extr[num_features])
    data_cat = enc.transform(data_extr[cat_features]).toarray()
    

    # Combine the numerical and one-hot encoded categorical columns
    data_processed = pd.concat(
        [
            data_extr[num_features + fl_features].reset_index(drop=True),
            pd.DataFrame(data_cat, columns=enc.get_feature_names_out()),
        ],
        axis=1,
    )


    # Make predictions
    predictions = model.predict(data_processed)
    #predictions = predictions[:10]  # just picking 10 to display sample output :-)  

    ### -------- DO NOT TOUCH THE FOLLOWING LINES -------- ###
    # Save the predictions to a CSV file (in order of data input!)
    pd.DataFrame({"predictions": predictions}).to_csv(output_dataset, index=False)

    mae_test = mean_absolute_error(data["price"], predictions)
    print(f"test_set MAE: {mae_test}")




