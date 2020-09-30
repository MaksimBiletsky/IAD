import pandas as pd
import make_plot
import preprocessing

pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)
database_df =pd.read_csv('DATABASE.csv', sep=';')

preprocessing.parse(database_df)

database_df.set_index('day/month', inplace=True)

make_plot.make_graphics(database_df,  ['Wind Speed', 'Wind', 'Temperature'])