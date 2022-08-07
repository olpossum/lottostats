# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib as mp
import os

datapath = os.path.normpath("/home/andy/PycharmProjects/lottostats/archive/Lottery_Mega_Millions_Winning_Numbers__Beginning_2002.csv")

def import_data(datapath):
    data = pd.read_csv(datapath, parse_dates=['Draw Date'])
    return data

def data_check(df):
    valid = 0
    start_date = np.datetime64('2017-10-31')
    df = df[(df['Draw Date'] > start_date)]
    if df['B1'].max() > 70:
        valid = 0
        print("Ball 1 Data Out of Range 1 to 70")
        print("Max Value = " + df['B1'].max().astype(str))
        df = df[(df['B1'] < df['B1'].max())]
        return(valid, df)
    elif df['B2'].max() > 70:
        valid = 0
        print("Ball 2 Data Out of Range 1 to 70")
        print("Max Value = " + df['B2'].max().astype(str))
        df = df[(df['B2'] < df['B2'].max())]
        return(valid, df)
    elif df['B3'].max() > 70:
        valid = 0
        print("Ball 3 Data Out of Range 1 to 70")
        print("Max Value = " + df['B3'].max().astype(str))
        df = df[(df['B3'] < df['B3'].max())]
        return(valid, df)
    elif df['B4'].max() > 70:
        valid = 0
        print("Ball 4 Data Out of Range 1 to 70")
        print("Max Value = " + df['B4'].max().astype(str))
        df = df[(df['B4'] < df['B4'].max())]
        return(valid, df)
    elif df['B5'].max() > 70:
        valid = 0
        print("Ball 5 Data Out of Range 1 to 70")
        print("Max Value = " + df['B5'].max().astype(str))
        df = df[(df['B5'] < df['B5'].max())]
        return(valid, df)
    else:
        valid = 1
        return(valid, df)

def aggregate_frequency(df, cols):
    template = pd.Series(int(0),index=np.arange(1,71,1))

    vc1 = df['B1'].value_counts().sort_index().add(template,fill_value=0).astype(int)
    vc2 = df['B2'].value_counts().sort_index().add(template,fill_value=0).astype(int)
    vc3 = df['B3'].value_counts().sort_index().add(template,fill_value=0).astype(int)
    vc4 = df['B4'].value_counts().sort_index().add(template,fill_value=0).astype(int)
    vc5 = df['B5'].value_counts().sort_index().add(template,fill_value=0).astype(int)

    vc6 = df['Mega Ball'].value_counts().sort_index()

    agg_freq = vc1.add(vc2.add(vc3.add(vc4.add(vc5))))

    return(agg_freq, vc6)

def plot_frequency(freq):
    fig,ax = plt.subplots()
    ax = freq.plot.bar(x='num', y='freq')
    plt.show()

def top_frequency(freq):
    freq = freq.drop(np.arange(1,32,1))
    freq = freq.sort_values(ascending=False)
    print(freq)
    return freq

def pick_ticket(entries, fnum, fmega):
    ticket = {}

if __name__ == '__main__':
    entries = 5
    df = import_data(datapath)
    cols = ['B1','B2','B3','B4','B5']
    df[cols] = df['Winning Numbers'].str.split(' ', expand=True).astype(int)
    print(df.head())
    valid = 0
    while valid == 0:
        valid, df = data_check(df)

    frequency_num, frequency_mega = aggregate_frequency(df,cols)

    frequency_num = top_frequency(frequency_num)

    #plot_frequency(frequency_num)
    #plot_frequency(frequency_mega)


