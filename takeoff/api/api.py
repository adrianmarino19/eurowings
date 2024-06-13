from fastapi import FastAPI
from takeoff.predict import predict_api
from takeoff.utils import airport_to_countrycode
#need to fix pages import but Nils has the big C


app = FastAPI()

@app.get('/')
def index():
    return {'ok': True}

@app.get('/predict')
def predict(origin_air, dest_air, cab_class, trip_type, is_connected, trip_len, search_date, flight_date, airline):
    #FROM USERINPUT STREAMLIT -- Origin aipoirt(0), destination airport(1), cabin class(9), mainCarrier(4)
    #FROM HARDCODED FOR NOW -- OriginAirport(0)	DestinationAirport(1)	OriginCountry(2)	DestinationCountry(3)	mainCarrier(4)	isConnectingFlight(5)	isEWRoute(6)	Market(7)	UserCountryCode(8)	cabinClass(9)	kind(10)	TripLengthNights(11)	TravelHorizonDays(12)	RedirectsCount(13)	Segments(14)	ODPax(15)	TripPax(16)
    #data = ['origin_air', 'dest_air', 'airline', 'cab_class', 'flight_date', 'pred_date', 'trip_type']
    #0, 0, 'DE', 'DE', 'ECONOMY', 'RETURN', 3.0, 109.0, 2.0, 4.0, 4.0, 2.0]
    #data = [origin_air, dest_air, airline, cab_class, flight_date, pred_date, trip_type]

    #print(data)
    #convert the origin aiport to countycode so can be used for origin country
    #data[2] = airport_to_countrycode(OriAirp_input)

    #convert the destination airport to coutrycode so can be used for dest country
    #data[3] = airport_to_countrycode(DestAirp_input)
    data = [origin_air, dest_air, cab_class, trip_type, is_connected, trip_len, search_date, flight_date, airline]

    #test
    # data = ['MAD', 'BCN', 'ECONOMY', 'RETURN', 1, 30, "2026-05-10", "2026-06-10", "FR"]
    print(data)
    print("test data")
    price = predict_api(data)
    print(price)
    return {'price': str(price[0])}
