# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import csv

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os
from collections import Counter

datapath = os.path.normpath("archive/Lottery_Mega_Millions_Winning_Numbers__Beginning_2002.csv")

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

    vc6 = df['Mega Ball'].value_counts().sort_values(ascending=False)

    agg_freq = vc1.add(vc2.add(vc3.add(vc4.add(vc5))))

    #plot_frequency(agg_freq.drop(np.arange(32,71,1)))

    return(agg_freq, vc6)

def plot_frequency(freq,type):
    fig,ax = plt.subplots()
    ax = freq.plot.bar(x='num', y='freq')
    plt.title(type)
    plt.show()

def top_frequency(freq):
    #freq = freq.drop(np.arange(1,32,1))
    freq = freq.sort_values(ascending=False)
    #print(freq)
    return freq

def pick_tickets(entries, fnum, fmega):
    tickets = []
    entry_i = 1
    fnum_i = 0
    #print(fnum.index[fnum_i])
    #print(fnum.index[fnum_i+1])
    #print(fnum.index[fnum_i+2])
    #print(fnum.index[fnum_i+3])
    #print(fnum.index[fnum_i+4])
    fmnum_i = 0
    while entry_i <= entries:
        try:
            #print("Loop " + str(entry_i))
            entry_dict = {}
            entry_dict.update({"B1": fnum.index[fnum_i]})
            entry_dict.update({"B2": fnum.index[fnum_i+1]})
            entry_dict.update({"B3": fnum.index[fnum_i+2]})
            entry_dict.update({"B4": fnum.index[fnum_i+3]})
            entry_dict.update({"B5": fnum.index[fnum_i+4]})
            entry_dict.update({"M1": fmega.index[fmnum_i]})
            tickets.append(entry_dict)
            fnum_i += 5
            fmnum_i += 1
            entry_i += 1
        except:
            entry_dict = {}
            flag = 0
            unique = False
            while unique == False:
                random = np.random.randint(0,32,5)
                print(random)
                flag = len(set(random)) == len(random)
                if(flag):
                    unique = True
                else:
                    unique = False
            random_mega = np.random.randint(0,25,1)
            entry_dict.update({"B1": fnum.index[random[0]]})
            entry_dict.update({"B2": fnum.index[random[1]]})
            entry_dict.update({"B3": fnum.index[random[2]]})
            entry_dict.update({"B4": fnum.index[random[3]]})
            entry_dict.update({"B5": fnum.index[random[4]]})
            entry_dict.update({"M1": fmega.index[random_mega[0]]})
            tickets.append(entry_dict)
            entry_i += 1

    return tickets

def dict_2_csv(dicts):
    keys = dicts[0].keys()
    #print(keys)
    with open('test.csv', 'w') as output_file:
        dict_writer = csv.DictWriter(output_file,keys)
        dict_writer.writeheader()
        dict_writer.writerows(dicts)



if __name__ == '__main__':
    entries = int(input("Enter number of entries to generate: "))
    df = import_data(datapath)
    cols = ['B1','B2','B3','B4','B5']
    df[cols] = df['Winning Numbers'].str.split(' ', expand=True).astype(int)
    #print(df.head())
    valid = 0
    while valid == 0:
        valid, df = data_check(df)

    frequency_num, frequency_mega = aggregate_frequency(df,cols)

    frequency_num = top_frequency(frequency_num)

    plot_frequency(frequency_num, 'Number Frequency')
    plot_frequency(frequency_mega, 'Megaball Frequency')

    tickets = pick_tickets(entries, frequency_num, frequency_mega)
    print(tickets)

    dict_2_csv(tickets)
