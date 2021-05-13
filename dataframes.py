import pandas as pd
import os
import csv

# get a list of all flow files
HISTORICAL_FLOW_FILES = os.listdir('data/flow')
HISTORICAL_LEVEL_FILES = os.listdir('data/level')
REALTIME_FLOW_FILES = os.listdir('data/realtime/flow')
REALTIME_LEVEL_FILES = os.listdir('data/realtime/level')

# dataframe of all stations
df_stations = pd.read_csv(r'./data/stations/Stations.csv').set_index('StationId')

# # dataframe of all known historical flows
df_historical_flows = pd.read_csv('./data/historical/average_historical_flows.csv')
dfc = df_historical_flows.copy()
df_historical_flows['Year'] = 2020
dfc['Year'] = 2021
df_historical_flows = pd.concat([df_historical_flows,dfc])
df_historical_flows['Date'] = pd.to_datetime(df_historical_flows[['Year','Month','Day']],errors='coerce')

# # dataframe of all known historical levels
df_historical_levels = pd.read_csv('./data/historical/average_historical_levels.csv')
dfc = df_historical_levels.copy()
df_historical_levels['Year'] = 2020
dfc['Year'] = 2021
df_historical_levels = pd.concat([df_historical_levels,dfc])
df_historical_levels['Date'] = pd.to_datetime(df_historical_levels[['Year','Month','Day']],errors='coerce')

# dataframe of realtime average flows
df_flows = pd.read_csv('./data/realtime/average_realtime_flows.csv')
df_flows['Date'] = pd.to_datetime(df_flows[['Year','Month','Day']])

# dataframe of realtime average levels
df_levels = pd.read_csv('./data/realtime/average_realtime_levels.csv')
df_levels['Date'] = pd.to_datetime(df_levels[['Year','Month','Day']])


#################################
## Old content used to clean csv
#################################

# def clean_df(file):
#     with open(file) as f:
#         reader = csv.reader(f)
#         _id = next(reader)[0][-7:]
#     df = pd.read_csv(file,skiprows=4,converters={'Date':pd.to_datetime})
#     df['ID'] = _id
#     return df
# dataframe of all stations
# df_flows = pd.concat([clean_df(fr'./data/realtime/flow/{file_name}') for file_name in REALTIME_FLOW_FILES])
# df_flows.to_csv('flows.csv',index=False)

# dataframe of all stations
# df_levels = pd.concat([clean_df(fr'./data/realtime/level/{file_name}') for file_name in REALTIME_LEVEL_FILES])
# df_levels.to_csv('levels.csv',index=False)

# df_historical_flows = pd.concat([pd.read_csv(fr'./data/flow/{file_name}',encoding='ISO-8859-1',converters={'Date':pd.to_datetime}) for file_name in HISTORICAL_FLOW_FILES])

# df_historical_levels = pd.concat([pd.read_csv(fr'./data/level/{file_name}',encoding='ISO-8859-1',converters={'Date':pd.to_datetime}) for file_name in HISTORICAL_LEVEL_FILES])
