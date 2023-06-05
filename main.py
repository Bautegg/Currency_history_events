import os
import pandas as pd
import plotly.express as px


def load_data(location):

    path, dirs, files = next(os.walk(f'./{location}/'))
    df_list = []

    for i in range(len(files)):
        tmp_df = pd.read_csv(f'./{location}/{files[i]}')
        df_list.append(tmp_df)
    df = pd.concat(df_list, ignore_index=True)
    return df


def create_plot():

    df_plot = load_data(location)
    fig = px.line(df_plot, y='<OPEN>', x='<DATE>', color='<TICKER>')
    fig.show()


if __name__ == '__main__':
    location = 'currencies_data'
    print(f'1 USD is X PLN: {load_data(location)} \n')
    print(f'PLOT: {create_plot()} \n')