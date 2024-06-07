import pandas as pd


def separate_columns(df):
    categorical_columns = df.dtypes[(df.dtypes == "object")].index
    categorical_columns = categorical_columns.drop(["cabinClass", "kind"])

    for ohe_var in list(categorical_columns):
        OHE_filtering(df, ohe_var)

    numeric_columns = df.dtypes[(df.dtypes == "int64") | (df.dtypes == "float64")].index
    numeric_columns = numeric_columns.drop("Average_FlightFare")

    ordinal_columns = df.dtypes[(df.dtypes == "object")].index
    ordinal_columns = ordinal_columns.drop(["OriginAirport",
                                    "DestinationAirport",
                                    "OriginCountry",
                                    "DestinationCountry",
                                    "mainCarrier",
                                    "Market",
                                    "UserCountryCode"])
    return categorical_columns, numeric_columns, ordinal_columns

def OHE_filtering(df, col):
    """ This function renames unpopular destinations to Other such that less columns will be generated during
    the one hot encoding"""
    """BE CAREFUL!!! Only run once as otherwise the destinations will be split into smaller and smaller chunks"""
    avg_of_val = (df[col].value_counts().mean())

    #filtering for the less important ones (less common), will bundle them up in a Rest column in OHE
    filtered_airports_rest = (df[col].value_counts() <= avg_of_val)
    rest_encoding = filtered_airports_rest.index[filtered_airports_rest].tolist()
    rest_encoding.sort()

    #What I want to do now is based on these values, I want to call all rest_ECONDING to be renamed to "Other"
    #and keep unique as they are

    df.loc[df[col].isin(rest_encoding), [col]] = ["Other"]
    return df

def preprocess(df):
    #data=[destaiport, ]
    #convert data lsit to df
    categorical_columns, _, _ = separate_columns(df)
    for col in categorical_columns:
        OHE_filtering(df, col)
    return df

main_OriginAirport = ['AAL', 'AAR', 'ABJ', 'ABV', 'ABZ', 'ACC', 'ACE', 'ACH', 'ADA', 'ADD', 'AES', 'AEY', 'AGA', 'AHB', 'AHO', 'AHU', 'AJA', 'ALA', 'ALF', 'ALG', 'ANR', 'AOE', 'AOI', 'AQJ', 'ASR', 'AUH', 'BAH', 'BAL', 'BAY', 'BCM', 'BDS', 'BEM', 'BES', 'BFS', 'BGG', 'BGO', 'BGW', 'BHD', 'BIA', 'BIQ', 'BJA', 'BJL', 'BJV', 'BKO', 'BLL', 'BMA', 'BNX', 'BOH', 'BOJ', 'BOO', 'BRE', 'BRN', 'BRQ', 'BSR', 'BTS', 'BUS', 'BVE', 'BZG', 'BZO', 'BZR', 'CAG', 'CCF', 'CDT', 'CFE', 'CFR', 'CFU', 'CHQ', 'CIT', 'CIY', 'CKY', 'CLJ', 'CND', 'COO', 'CRA', 'CWL', 'CZL', 'DBV', 'DEB', 'DIY', 'DJE', 'DLE', 'DLM', 'DMM', 'DND', 'DNZ', 'DOH', 'DOL', 'DRS', 'DSS', 'DTM', 'DWC', 'DYU', 'EAM', 'EAS', 'EBL', 'ECN', 'EDO', 'EFL', 'EGC', 'ELQ', 'ENU', 'ERC', 'ERF', 'ERH', 'ESU', 'ETZ', 'EUN', 'EVE', 'EVN', 'EXT', 'EZS', 'FAE', 'FDH', 'FEZ', 'FKB', 'FLR', 'FMO', 'FNA', 'FNC', 'FNI', 'FRU', 'FUE', 'GCI', 'GHV', 'GIB', 'GIZ', 'GLN', 'GOA', 'GRO', 'GRQ', 'GRX', 'GRZ', 'GUW', 'GWT', 'GYD', 'GZP', 'GZT', 'HAS', 'HAU', 'HBE', 'HER', 'HOR', 'HOV', 'HRG', 'HSA', 'HTY', 'HUY', 'IAS', 'IFN', 'IGD', 'IKA', 'INI', 'INN', 'INV', 'IOM', 'ISE', 'ISU', 'IVL', 'JER', 'JIK', 'JMK', 'JNX', 'JSH', 'JSI', 'JSY', 'JTR', 'KAN', 'KCM', 'KEF', 'KGS', 'KIK', 'KIR', 'KKN', 'KLU', 'KLV', 'KLX', 'KRN', 'KRS', 'KSC', 'KSF', 'KSU', 'KTT', 'KUN', 'KUO', 'KUT', 'KVA', 'KWI', 'KYA', 'KZR', 'LBC', 'LCG', 'LCJ', 'LDE', 'LDY', 'LEI', 'LEJ', 'LFW', 'LGG', 'LIG', 'LIL', 'LJU', 'LLA', 'LNZ', 'LOS', 'LPA', 'LPI', 'LPP', 'LRH', 'LRS', 'LUZ', 'LXR', 'MAH', 'MCT', 'MED', 'MHD', 'MIR', 'MJI', 'MJT', 'MLH', 'MLN', 'MLX', 'MME', 'MMX', 'MOL', 'MPL', 'MQM', 'MSQ', 'MSR', 'MST', 'MZH', 'NAV', 'NBE', 'NDR', 'NJF', 'NKC', 'NOC', 'NQY', 'NQZ', 'NRK', 'NUM', 'NWI', 'NYO', 'OGU', 'OHD', 'OLB', 'OMH', 'OMO', 'OMR', 'ONQ', 'ORK', 'ORN', 'OSR', 'OSS', 'OST', 'OUA', 'OUD', 'OUL', 'OVD', 'OXB', 'OZZ', 'PAD', 'PAS', 'PDL', 'PDV', 'PED', 'PEG', 'PFO', 'PGF', 'PHC', 'PIK', 'PIS', 'PIX', 'PLQ', 'PMO', 'PNA', 'PRN', 'PSR', 'PUF', 'PUY', 'PVK', 'PXO', 'PZU', 'QSF', 'QSR', 'RAE', 'RAI', 'RBA', 'RDO', 'RDZ', 'REG', 'REU', 'RHO', 'RJK', 'RLG', 'RMF', 'RMI', 'RMO', 'RMU', 'RNS', 'ROB', 'RTM', 'RVN', 'RZE', 'RZV', 'SBZ', 'SCN', 'SCO', 'SCQ', 'SCV', 'SDR', 'SEN', 'SFA', 'SFT', 'SHJ', 'SID', 'SJJ', 'SKD', 'SKP', 'SNN', 'SOU', 'SPC', 'SPU', 'SPX', 'SSH', 'SSJ', 'SUF', 'SVG', 'SXB', 'SYZ', 'SZF', 'SZG', 'SZY', 'SZZ', 'TAS', 'TBS', 'TBZ', 'TER', 'TFN', 'TGD', 'TGM', 'TIF', 'TIV', 'TJK', 'TKU', 'TLM', 'TLN', 'TMP', 'TNG', 'TOS', 'TPS', 'TRD', 'TRF', 'TRN', 'TRS', 'TSR', 'TTU', 'TUF', 'TUN', 'TUU', 'TZX', 'UGC', 'ULH', 'UME', 'VAA', 'VAR', 'VAS', 'VGO', 'VIL', 'VIT', 'VLL', 'VRN', 'VST', 'XNB', 'XRY', 'YNB', 'ZAD', 'ZAZ', 'ZTH']
main_DestinationAirport = ['AAE', 'AAL', 'AAR', 'ABJ', 'ABV', 'ABZ', 'ACC', 'ADA', 'ADD', 'ADF', 'AES', 'AEY', 'AHO', 'AHU', 'AJA', 'ALA', 'ALF', 'ANR', 'ANX', 'AOE', 'AOI', 'AOK', 'AQJ', 'ASB', 'ASR', 'AXD', 'BAH', 'BAL', 'BAY', 'BCM', 'BDS', 'BDU', 'BEM', 'BES', 'BFS', 'BGG', 'BGO', 'BGW', 'BHD', 'BHK', 'BIA', 'BIQ', 'BJA', 'BJL', 'BJV', 'BKO', 'BLL', 'BNX', 'BOH', 'BOJ', 'BOO', 'BRE', 'BRN', 'BRQ', 'BSK', 'BSR', 'BTS', 'BUS', 'BVC', 'BVE', 'BZG', 'BZO', 'BZR', 'CCF', 'CDT', 'CFE', 'CFK', 'CFR', 'CIT', 'CKY', 'CLJ', 'CLY', 'CMF', 'COO', 'CRA', 'CWL', 'CZL', 'DCM', 'DEB', 'DIY', 'DJE', 'DLE', 'DMM', 'DNZ', 'DOH', 'DRS', 'DSS', 'DTM', 'DWC', 'DYU', 'EAS', 'EBA', 'ECN', 'EDO', 'EFL', 'EGC', 'ELU', 'EMA', 'ERC', 'ERF', 'ERH', 'ESU', 'ETZ', 'EUN', 'EVE', 'EVN', 'EXT', 'EZS', 'FAE', 'FDH', 'FEG', 'FEZ', 'FKB', 'FLW', 'FMM', 'FMO', 'FNA', 'FNI', 'FRO', 'FRU', 'FSC', 'GCI', 'GHV', 'GIB', 'GIZ', 'GJL', 'GLA', 'GNB', 'GNJ', 'GNY', 'GOA', 'GOT', 'GPA', 'GRQ', 'GRX', 'GRZ', 'GUW', 'GWT', 'GYD', 'GZP', 'GZT', 'HAJ', 'HAU', 'HBE', 'HHN', 'HOR', 'HTY', 'HUY', 'HVG', 'IAS', 'IFJ', 'IFN', 'IGD', 'INI', 'INN', 'INV', 'IOA', 'IOM', 'ISU', 'IVL', 'JER', 'JIJ', 'JKH', 'JNX', 'JSH', 'JSI', 'JSY', 'JTY', 'JYV', 'KAO', 'KCM', 'KGS', 'KIK', 'KIR', 'KIT', 'KLR', 'KLU', 'KLX', 'KOI', 'KOK', 'KRN', 'KRS', 'KSC', 'KTT', 'KTW', 'KUN', 'KUO', 'KUT', 'KVA', 'KWI', 'KYA', 'KZR', 'LBA', 'LCG', 'LCJ', 'LCY', 'LDE', 'LDY', 'LEI', 'LEJ', 'LEU', 'LFW', 'LGG', 'LIG', 'LIL', 'LJU', 'LKN', 'LLA', 'LMP', 'LNZ', 'LPI', 'LPL', 'LPP', 'LRH', 'LRS', 'LUX', 'LUZ', 'LXR', 'LXS', 'LYR', 'MCT', 'MED', 'MHD', 'MHQ', 'MIR', 'MJI', 'MJT', 'MLH', 'MLN', 'MLO', 'MLX', 'MME', 'MMX', 'MOL', 'MPL', 'MQM', 'MQX', 'MSQ', 'MST', 'MZH', 'NAJ', 'NAV', 'NBE', 'NCL', 'NDR', 'NIM', 'NJF', 'NKC', 'NOC', 'NOP', 'NQY', 'NQZ', 'NRK', 'NRN', 'NTE', 'NUE', 'NUM', 'NWI', 'NYO', 'OGU', 'OHD', 'OLB', 'OMO', 'OMR', 'ONQ', 'ORK', 'ORN', 'OSD', 'OSI', 'OSS', 'OST', 'OSY', 'OUA', 'OUD', 'OUL', 'OVD', 'OXB', 'OZZ', 'PAD', 'PAS', 'PDL', 'PDV', 'PEG', 'PGF', 'PHC', 'PIK', 'PIS', 'PLQ', 'PNA', 'POZ', 'PRN', 'PSR', 'PUF', 'PUY', 'PVK', 'PZU', 'QRW', 'QSF', 'QSR', 'RAI', 'RBA', 'REG', 'REU', 'RJK', 'RJL', 'RLG', 'RMF', 'RMI', 'RMO', 'RMU', 'RNS', 'RTM', 'RUH', 'RVN', 'RZE', 'RZV', 'SBZ', 'SCN', 'SCO', 'SCQ', 'SCV', 'SDL', 'SDR', 'SEN', 'SFA', 'SFT', 'SHJ', 'SID', 'SJJ', 'SKD', 'SKP', 'SLL', 'SMI', 'SNN', 'SOU', 'SPC', 'SPX', 'SUF', 'SUJ', 'SVG', 'SVJ', 'SVL', 'SXB', 'SYZ', 'SZF', 'SZG', 'SZY', 'SZZ', 'TAS', 'TAT', 'TAY', 'TBS', 'TBZ', 'TER', 'TFN', 'TGM', 'TIV', 'TJK', 'TKU', 'TLM', 'TLN', 'TLS', 'TMP', 'TMR', 'TOE', 'TOS', 'TPS', 'TRD', 'TRF', 'TRN', 'TRS', 'TSR', 'TTU', 'TUF', 'TZL', 'TZX', 'UGC', 'ULH', 'UME', 'VAA', 'VAN', 'VAR', 'VAS', 'VBY', 'VDS', 'VGO', 'VHM', 'VIL', 'VIT', 'VOL', 'VRN', 'VST', 'VXE', 'VXO', 'WMI', 'WRO', 'XRY', 'ZAZ']
main_OriginCountry = ['AE', 'AL', 'AM', 'AZ', 'BA', 'BF', 'BG', 'BH', 'BJ', 'BY', 'CI', 'CV', 'CY', 'CZ', 'DK', 'DZ', 'EE', 'EG', 'EH', 'ET', 'FI', 'FO', 'GE', 'GG', 'GH', 'GI', 'GM', 'GN', 'GW', 'HR', 'HU', 'IM', 'IQ', 'IR', 'IS', 'JE', 'JO', 'KG', 'KW', 'KZ', 'LB', 'LR', 'LT', 'LU', 'LV', 'LY', 'MD', 'ME', 'MK', 'ML', 'MR', 'MT', 'NG', 'NO', 'OM', 'QA', 'RO', 'RS', 'SA', 'SD', 'SI', 'SK', 'SL', 'SN', 'TG', 'TJ', 'TN', 'UZ', 'XK']
main_DestinationCountry = ['AL', 'AM', 'AZ', 'BA', 'BE', 'BF', 'BG', 'BH', 'BJ', 'BY', 'CI', 'CV', 'CZ', 'DK', 'DZ', 'EE', 'EH', 'ET', 'FI', 'FO', 'GE', 'GG', 'GH', 'GI', 'GM', 'GN', 'GW', 'IL', 'IM', 'IQ', 'IR', 'IS', 'JE', 'JO', 'KG', 'KW', 'KZ', 'LB', 'LT', 'LU', 'LV', 'LY', 'MD', 'ME', 'MK', 'ML', 'MR', 'MT', 'NE', 'NG', 'NO', 'OM', 'QA', 'RO', 'RS', 'SA', 'SD', 'SE', 'SI', 'SK', 'SL', 'SN', 'TG', 'TJ', 'TM', 'TN', 'UZ', 'XK']
main_mainCarrier = ['1B', '1L', '2L', '3F', '3L', '3Z', '4M', '4O', '4R', '4X', '4Y', '5F', '5K', '5M*', '5O', '5W', '6B', '6H', '6K', '6Y', '8H', '8R', 'A0', 'A2', 'A5', 'A9', 'AA', 'AH', 'AI', 'AP', 'AY', 'B2', 'B9', 'BI', 'BJ', 'BN', 'BQ', 'BZ', 'C3', 'CD', 'CJ', 'CL', 'CY', 'D4', 'DI', 'DN*', 'DV', 'DX', 'DY', 'E4*', 'E5', 'E6', 'EA', 'EC', 'EE', 'EN', 'EP', 'ET', 'EY', 'F3', 'FB', 'FH', 'FI', 'FL', 'FT', 'FZ', 'G6', 'G9', 'GF', 'GM', 'GQ', 'GR', 'GW*', 'H1', 'H3', 'H4', 'H6*', 'H7', 'HC', 'HF', 'HH', 'HN*', 'HP', 'HY', 'I2', 'IA', 'IR', 'IV', 'IZ', 'J2', 'J9', 'JU', 'KC', 'KC*', 'KK', 'KM', 'KQ', 'KU', 'LG', 'LM', 'M2', 'ME', 'MI', 'N7', 'NE', 'NI', 'NL', 'NO', 'NP', 'NT', 'OA', 'OG', 'OK', 'OR', 'OU', 'OV', 'P4', 'P6', 'PE', 'Q4', 'QB', 'QS', 'RC', 'RE', 'RJ', 'RO', 'S4', 'SE', 'SF', 'SI', 'SM', 'SQ', 'SR', 'SS', 'SV', 'SZ', 'T3', 'T5', 'TB', 'TF', 'TI*', 'TR', 'TU', 'U5', 'U8', 'UA', 'UD', 'UG', 'UX', 'V3', 'VL', 'VR', 'VS', 'WB', 'WF', 'WG', 'WI', 'WK', 'WX', 'WY', 'X3', 'X5', 'X9', 'XK', 'XR', 'XY', 'XZ', 'YW', 'ZB', 'ZQ']
main_Market = ['AD', 'AF', 'AL', 'AM', 'AO', 'AR', 'AS', 'AW', 'AZ', 'BA', 'BD', 'BF', 'BG', 'BH', 'BJ', 'BM', 'BO', 'BR', 'BS', 'BY', 'CA', 'CI', 'CL', 'CM', 'CN', 'CO', 'CR', 'CU', 'CV', 'CY', 'DJ', 'DK', 'DO', 'DZ', 'EC', 'EE', 'EG', 'ET', 'FJ', 'FK', 'FO', 'GD', 'GE', 'GF', 'GG', 'GH', 'GI', 'GM', 'GN', 'GP', 'GT', 'HK', 'HN', 'HR', 'HU', 'ID', 'IN', 'IQ', 'IR', 'IS', 'JO', 'JP', 'KE', 'KG', 'KH', 'KP', 'KR', 'KW', 'KY', 'KZ', 'LB', 'LC', 'LI', 'LK', 'LR', 'LT', 'LU', 'LV', 'LY', 'MC', 'MD', 'ME', 'MG', 'MK', 'ML', 'MM', 'MN', 'MO', 'MQ', 'MR', 'MT', 'MU', 'MV', 'MX', 'MY', 'MZ', 'NC', 'NG', 'NO', 'NP', 'NZ', 'OM', 'PA', 'PE', 'PF', 'PH', 'PK', 'PR', 'PS', 'PY', 'QA', 'RE', 'RO', 'RS', 'RU', 'RW', 'SC', 'SD', 'SG', 'SH', 'SI', 'SK', 'SL', 'SN', 'SO', 'SV', 'SY', 'TC', 'TG', 'TH', 'TJ', 'TM', 'TN', 'TW', 'TZ', 'UG', 'UY', 'UZ', 'VA', 'VE', 'VG', 'VN', 'XK', 'YE', 'YT', 'ZA', 'ZM', 'ZW']
main_UserCountryCode = ['AD', 'AF', 'AG', 'AL', 'AM', 'AR', 'AZ', 'BA', 'BD', 'BF', 'BG', 'BH', 'BJ', 'BM', 'BO', 'BR', 'BT', 'BY', 'CA', 'CD', 'CG', 'CI', 'CL', 'CN', 'CO', 'CR', 'CU', 'CV', 'CY', 'DJ', 'DK', 'DO', 'DZ', 'EC', 'EE', 'EG', 'ET', 'FJ', 'FK', 'FO', 'GA', 'GE', 'GF', 'GG', 'GH', 'GI', 'GM', 'GN', 'GP', 'GT', 'GU', 'GW', 'HN', 'HR', 'HU', 'ID', 'IM', 'IN', 'IQ', 'IR', 'IS', 'JE', 'JO', 'JP', 'KE', 'KG', 'KH', 'KR', 'KW', 'KY', 'KZ', 'LA', 'LB', 'LC', 'LI', 'LK', 'LT', 'LU', 'LV', 'LY', 'MC', 'MD', 'ME', 'MK', 'ML', 'MM', 'MN', 'MR', 'MT', 'MU', 'MV', 'MX', 'MY', 'NC', 'NE', 'NG', 'NI', 'NO', 'NP', 'NZ', 'OM', 'PA', 'PE', 'PF', 'PH', 'PK', 'PS', 'PY', 'QA', 'RE', 'RS', 'RU', 'RW', 'SC', 'SD', 'SG', 'SI', 'SK', 'SL', 'SM', 'SN', 'SO', 'SR', 'ST', 'SV', 'SY', 'TH', 'TJ', 'TN', 'TW', 'TZ', 'UA', 'UG', 'UY', 'UZ', 'VC', 'VE', 'VN', 'WS', 'XK', 'YE', 'ZA', 'ZM', 'ZW']

"""

OriginAirport	DestinationAirport	OriginCountry	DestinationCountry	mainCarrier	isConnectingFlight	isEWRoute	Market	UserCountryCode	cabinClass	kind	TripLengthNights	TravelHorizonDays	RedirectsCount	Segments	ODPax	TripPax
BLQ	            LOS	                IT	            Other	            AF	        1	                0	        IT	    IT	            ECONOMY	    RETURN	31.0	            91.0	            2.0	            4.0	        4.0	    2.0
"""

def cleaning(data):
    if data[0] not in main_OriginAirport:
        data[0] = "Other"
    if data[1] not in main_DestinationAirport:
        data[1] = "Other"
    if data[2] not in main_OriginCountry:
        data[2] = "Other"
    if data[3] not in main_DestinationCountry:
        data[3] = "Other"
    if data[4] not in main_mainCarrier:
        data[4] = "Other"
    if data[7] not in main_Market:
        data[7] = "Other"
    if data[8] not in main_UserCountryCode:
        data[8] = "Other"

    test_cols = [
        'OriginAirport', 'DestinationAirport', 'OriginCountry', 'DestinationCountry',
        'mainCarrier', 'isConnectingFlight', 'isEWRoute', 'Market', 'UserCountryCode',
        'cabinClass', 'kind', 'TripLengthNights', 'TravelHorizonDays', 'RedirectsCount',
        'Segments', 'ODPax', 'TripPax'
    ]


    # Create a DataFrame
    data = pd.DataFrame([data], columns=test_cols)

    return data

def airport_to_countrycode(airport):
    file = "data/airport_coordinates.csv"
    airport_df = pd.read_csv(file, delimiter=";")
    conversion_dict = airport_df.set_index('Airport Code')['Country Code'].to_dict()
    return conversion_dict[airport]
