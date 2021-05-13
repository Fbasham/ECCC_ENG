import pandas as pd

###########################################################
## Used as a helper file for cleaning and parsing csv files
###########################################################


# df = pd.read_csv('data/realtime/flows.csv',converters={'Date':pd.to_datetime})
# df = df.groupby(['ID',df['Date'].dt.year,df['Date'].dt.month,df['Date'].dt.day]).agg('mean')
# df.to_csv('average_realtime_flows.csv')


# df = pd.read_csv('data/realtime/levels.csv',converters={'Date':pd.to_datetime})
# df = df.groupby(['ID',df['Date'].dt.year,df['Date'].dt.month,df['Date'].dt.day]).agg('mean')
# df.to_csv('average_realtime_levels.csv')


# df = pd.read_csv('./data/flow/historical_flows.csv',converters={'Date':pd.to_datetime})
# df = df.groupby(['ID',df['Date'].dt.month,df['Date'].dt.day]).agg(['min','max']).stack()
# df.to_csv('average_historical_flows.csv')


# df = pd.read_csv('./data/level/historical_levels.csv',converters={'Date':pd.to_datetime})
# df = df.groupby(['ID',df['Date'].dt.month,df['Date'].dt.day]).agg(['min','max']).stack()
# df.to_csv('average_historical_levels.csv')