import pickle
from takeoff.utils import cleaning
import pandas as pd

model_filename = "takeoff/pipeline1.pkl"
model = pickle.load(open(model_filename,"rb"))
accepted_dest_airport = 1
# Do a list of all the OHT filtering to hard code every single airport
# and shit so that even if in the predict you have access to the list to check if it's other or if
#it exists. HARD CODE ALL



def predict_api(data):
    """DATA IS A LIST, that we then turn to a df here for the predict"""
#what should is the expected input give an example for myself so i know what ot work with
    #find way to seperate input
    """

OriginAirport	DestinationAirport	OriginCountry	DestinationCountry	mainCarrier	isConnectingFlight	isEWRoute	Market	UserCountryCode	cabinClass	kind	TripLengthNights	TravelHorizonDays	RedirectsCount	Segments	ODPax	TripPax
BLQ	            LOS	                IT	            Other	            AF	        1	                0	        IT	    IT	            ECONOMY	    RETURN	31.0	            91.0	            2.0	            4.0	        4.0	    2.0
    """
    clean_data = cleaning(data)
    print("clean data")
    predictions = model.predict(clean_data)
    return predictions

"""
1. USING OHE_filtering make the accepted_best for all the ones that aren't turned to rest
2. Based on these airports, we will compare what predict needs
"""

prediction = predict_api(['HAM', 'STN', 'DE', 'GB', 'FR', 0, 0, 'DE', 'DE', 'ECONOMY', 'RETURN', 3.0, 109.0, 2.0, 4.0, 4.0, 2.0])
#prediction = predict_api(['BLQ', 'LOS', 'IT', 'Other', 'AF', 1, 0, 'IT', 'IT', 'ECONOMY',
#    'RETURN', 31.0, 91.0, 2.0, 4.0, 4.0, 2.0])

print(prediction)
