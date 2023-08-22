import os
import pandas as pd
import plotly.express as px
from dash import dcc
import numpy as np

location = 'currencies_data'


def load_data(location):

    path, dirs, files = next(os.walk(f'./{location}/'))
    df_list = []

    for i in range(len(files)):
        tmp_df = pd.read_csv(f'./{location}/{files[i]}')
        df_list.append(tmp_df)
    df = pd.concat(df_list, ignore_index=True)
    return df

def data_cleansing():

    df_cl = load_data(location)
    df_date = pd.to_datetime(df_cl['<DATE>'], format="%Y%m%d")
    df_year = df_date.dt.year
    df_open = np.log10(df_cl['<OPEN>'])
    df_cl['Date'] = df_date
    df_cl['Year'] = df_year
    df_cl['Open'] = df_open

    print(df_open, df_cl['<OPEN>'])
    return df_cl

def create_plot():

    df_plot = data_cleansing()
    fig = px.line(df_plot, y='Open', x='Date', color='<TICKER>')
    fig.show()


def create_checkbox():

    df_check_list = load_data(location)
    df_cl = df_check_list['<TICKER>'].unique()
    dcc.Checklist(df_cl)
    return df_cl

if __name__ == '__main__':

    # print(f'LOADED_DATA: {load_data(location)} \n')
    print(f'PLOT: {create_plot()} \n')
    print(f'Cleansed data: {data_cleansing()} \n')
    print(f'CHECK_BOX: {create_checkbox()} \n\n')