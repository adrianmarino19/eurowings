import pandas as pd
from math import radians, sin, cos, sqrt, atan2
from datetime import datetime

gdp_per_capita_eur_dict = {
    'ES': 37316.7, 'GB': 41833.8, 'RO': 12710.7, 'FR': 43853.4, 'DE': 47938.5,
    'OM': 14340.6, 'IT': 36311.4, 'IL': 38530.8, 'AT': 47834.1, 'GR': 18680.4, 'NO': 67981.5,
    'AU': 51021, 'PT': 22955.4, 'NL': 57180.6, 'TR': 8624.7, 'CZ': 21448.8,
    'BG': 8805.6, 'PL': 15628.5, 'BE': 50067, 'SK': 18413.1, 'BR': 6618.6, 'CY': 28025.1,
    'KZ': 9670.5, 'IN': 2291.4, 'DK': 61821.9, 'SE': 54426.6, 'LU': 109163.7, 'KR': 31353.3,
    'KW': 28124.1, 'CH': 79108.2, 'LB': 4510.7, 'IE': 93051, 'EE': 21527.1, 'TN': 3393.9,
    'SA': 21005.1, 'CA': 46984.5, 'CN': 11544.3, 'JP': 38382.3, 'FI': 46281.6, 'AE': 39402,
    'AL': 5841.9, 'UA': 3187.8, 'MA': 3087, 'RU': 10373.4, 'HU': 17092.8, 'RS': 8669.7,
    'GE': 4879.8, 'HR': 15659.1, 'XK': 4190.4, 'SI': 25478.1, 'IQ': 4168.8, 'AR': 8118.9,
    'NZ': 41063.4, 'DZ': 3327.3, 'BY': 5855.4, 'LV': 19066.5, 'TW': 31140.9, 'JO': 3834,
    'ID': 3870, 'EG': 3231.9, 'ME': 7632, 'AF': 464.4, 'MX': 9477, 'BO': 3213,
    'NG': 1844.1, 'US': 63032.4, 'PH': 3195.9, 'LT': 21366.9, 'PK': 1309.5,
    'UZ': 1758.6, 'SG': 63666.9, 'CO': 6180.3, 'UY': 15967.8, 'MC': 155700, 'MT': 29303.1,
    'AM': 4219.2, 'IS': 69146.1, 'BA': 6165, 'BH': 22943.7, 'TH': 7074,
    'MY': 10073.7, 'AD': 44900.4, 'VN': 3766.5, 'CR': 11781, 'AZ': 4782.6, 'LI': 162204.3,
    'IR': 2486.7, 'LY': 3606.3, 'YE': 741.6, 'MD': 4141.8, 'GH': 2201.4, 'PS': 3465.9,
    'SC': 13797, 'JE': 51840, 'ZA': 5625.9, 'GM': 684.9, 'SY': 1141.2, 'CV': 3182.4,
    'QA': 55208.7, 'BD': 1834.2, 'CL': 14157.9, 'PA': 11999.8, 'IM': 80055, 'MK': 6141.6,
    'KH': 1405.8, 'PE': 6546.6, 'EC': 5617.8, 'GT': 4835.7, 'SN': 1489.5, 'RE': 22314.6,
    'GG': 60300, 'MU': 10635.3, 'ML': 809.1, 'GI': 83034.9, 'KG': 1112.4, 'ET': 857.7,
    'KE': 1859.4, 'NI': 2064.6, 'KY': 76725, 'UG': 742.5, 'LK': 3467.7, 'MV': 9471.3,
    'SO': 394.2, 'CD': 505.8, 'SL': 470.7, 'SM': 55187.1, 'LA': 2372.4, 'CG': 2143.8, 'SR': 4352.4,
    'WS': 3930.3, 'PY': 4956.3, 'GF': 21075.3, 'DO': 7893, 'GP': 21758.4, 'MR': 1461.6, 'CI': 2475.9,
    'BJ': 1227.6, 'CU': 8883, 'BT': 3118.5, 'PF': 16650, 'GW': 720.9, 'VE': 288.9,
    'SV': 4023, 'ST': 1955.7, 'FK': 72000, 'HN': 2397.6, 'FJ': 5961.6,
    'ZW': 1342.8, 'RW': 843.3, 'NC': 32220, 'BM': 96957, 'GU': 31761, 'MN': 4115.7,
    'NP': 1209.6, 'TJ': 773.1, 'ZM': 1013.4, 'BF': 825.3, 'TZ': 1047.6, 'LC': 9219.6,
    'SD': 1470.6, 'VC': 6655.5, 'DJ': 2761.2, 'NE': 522.9, 'GN': 850.5,
    'GA': 7128.9, 'MM': 1404.9, 'FO': 53675.1, 'AG': 15437.7, 'MZ': 438.3,
    'BQ': 21150, 'GL': 48600, 'AW': 23397.3, 'VA': 76500, 'MQ': 21775.8, 'BB': 16882.2,
    'BS': 29871, 'JM': 4527.9, 'LR': 550.8, 'TT': 14395.5, 'CM': 1515.6, 'CE': 451.8,
    'KN': 17208, 'AO': 2998.8, 'TD': 598.5, 'SX': 21330, 'PG': 2426.4,
    'MG': 470.7, 'BW': 6738.3, 'BN': 27978.3, 'BZ': 4443.3, 'TC': 26550,
    'CW': 20070, 'GD': 9037.8, 'TL': 1677.6, 'TG': 810, 'GQ': 8034.3, 'YT': 8444.7,
    'PR': 29406.6, 'SS': 202.5, 'MW': 562.5, 'CK': 14809.5, 'MF': 21775.8,
    'TM': 6252.3, 'VI': 34528.5, 'VG': 38070, 'KM': 1296, 'HT': 1342.8, 'PW': 14356.8,
    'MS': 11070, 'AI': 18270, 'BI': 215.1, 'GY': 12591
}



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

def haversine(lat1, lon1, lat2, lon2):
    # Convert latitude and longitude from degrees to radians
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])

    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    r = 6371  # Radius of Earth in km
    return c * r

def get_dist(src, des):
    print(src)
    print(des)
    df = pd.read_csv('data/airport_coordinates.csv', delimiter=';')
    print('data loaded')
    src_cord = df[df['Airport Code'] == src]
    dest_cord = df[df['Airport Code'] == des]
    src_lat = src_cord['Latitude']
    src_lon = src_cord['Longitude']
    print(src_lat)

    des_lat = dest_cord['Latitude']
    des_lon = dest_cord['Longitude']

    return haversine(src_lat, src_lon, des_lat, des_lon)


def get_gdp(des):
    df = pd.read_csv('data/airport_coordinates.csv', delimiter=';')
    dest_cord = df[df['Airport Code'] == des]
    country_code = str(dest_cord['Country Code'].values[0])
    print(country_code)
    return gdp_per_capita_eur_dict[country_code]

def days_between(d1, d2):
    print(d1)
    print(d2)

    d1 = datetime.strptime(d1, "%Y-%m-%d")
    #d1 = d1.strftime("%Y-%m-%d")

    d2 = datetime.strptime(d2, "%Y-%m-%d")
    #d2 = d2.strftime("%Y-%m-%d")

    print(d1)
    print(d2)
    return abs((d1 - d2).days)


def cleaning(data):

    # [origin_air, dest_air, cab_class, trip_type, is_connected, trip_len, search_date, flight_date, airline]
    print("start clean")
    dist = get_dist(data[0], data[1])
    print("dist done")
    print(dist)
    gdp = get_gdp(data[1])
    print("gdb done")
    horizon = days_between(data[6], data[7])
    print("horizon")
    print(horizon)
    final_data = [dist, gdp, data[2], data[3], data[4], data[5], horizon, data[-1]]
    test_cols = ["Distance",
                "GDP_per_capita_EUR",
                "cabinClass",
                "kind",
                "isConnectingFlight",
                "TripLengthNights",
                "TravelHorizonDays",
                "mainCarrier"]

    # [
    #     'OriginAirport', 'DestinationAirport', 'OriginCountry', 'DestinationCountry',
    #     'mainCarrier', 'isConnectingFlight', 'isEWRoute', 'Market', 'UserCountryCode',
    #     'cabinClass', 'kind', 'TripLengthNights', 'TravelHorizonDays', 'RedirectsCount',
    #     'Segments', 'ODPax', 'TripPax'
    # ]


    # Create a DataFrame
    data = pd.DataFrame([final_data], columns=test_cols)
    print("Checking dataiscorrectfor predict")
    for index, row in data.iterrows():
        print(row[0])
        print(row[1])
        print(row[2])
        print(row[3])
        print(row[4])
        print(row[5])
        print(row[6])
        print(row[7])
    return data

def airport_to_countrycode(airport):
    file = "data/airport_coordinates.csv"
    airport_df = pd.read_csv(file, delimiter=";")
    conversion_dict = airport_df.set_index('Airport Code')['Country Code'].to_dict()
    return conversion_dict[airport]

def distance(origin, destination):
    return origin - destination

def time_horizon(price_date, flight_date):
    return price_date - flight_date
