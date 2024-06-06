from takeoff.utils import separate_columns, preprocess
import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder, OrdinalEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.compose import make_column_selector, make_column_transformer
from sklearn.pipeline import make_pipeline
from sklearn.impute import SimpleImputer
import pickle
from sklearn.metrics import r2_score

def load_data(filename):
    df = pd.read_csv(filename)
    df.drop(columns=["flightWeek", "weekOfYear", "Revenue"], inplace=True)
    df.dropna(inplace=True)
    return df




def prepare_pipeline(df):
    categorical_columns, numeric_columns, ordinal_columns = separate_columns(df)
    num_transformer = StandardScaler()
    ordinal_transformer = OrdinalEncoder()
    cat_transformer = OneHotEncoder(sparse_output=False)

    preproc_basic = make_column_transformer(
        (num_transformer, numeric_columns),
        (ordinal_transformer, ordinal_columns),
        (cat_transformer, categorical_columns),
        #DONT FORGET TO DO TRANSFORMER FOR THE SIN COS OF THE TIME ONES I DORPPED fo final
        remainder='passthrough'
    )

    pipe = make_pipeline(preproc_basic, RandomForestRegressor())
    return pipe

def train_model(df):
    pipe = prepare_pipeline(df)

    X = df.drop(columns=["Average_FlightFare"])
    y = df["Average_FlightFare"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.7)

    pipe.fit(X_train, y_train)

    print("Evaluate model")
    evaluate(pipe, X_test, y_test)
    return pipe

def evaluate(model, X_test, y_test):
    y_pred = model.predict(X_test)
    r2_score(y_test, y_pred)

def save_model(model):
    with open("pipeline.pkl", "wb") as file:
        pickle.dump(model, file)

if __name__ == "__main__":
    file = "SkyScannerRedirrect_DataScienceBootCamp.csv"
    print("Load data")
    df = load_data(file)
    df = preprocess(df)
    print("Train model")
    model = train_model(df)
    print("Save model")
    save_model(model)
