# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import pandas as pd
import numpy as np
import matplotlib as mp
import os

datapath = os.path.normpath("/home/andy/PycharmProjects/lottostats/archive/Lottery_Mega_Millions_Winning_Numbers__Beginning_2002.csv")

def import_data(datapath):
    data = pd.read_csv(datapath)
    return data

if __name__ == '__main__':
    df = import_data(datapath)
    cols = ['B1','B2','B3','B4','B5']
    df[cols] = df['Winning Numbers'].str.split(' ', expand=True)

    vc1 = df['B1'].value_counts()
    vc2 = df['B2'].value_counts()
    vc3 = df['B3'].value_counts()
    vc4 = df['B4'].value_counts()
    vc5 = df['B5'].value_counts()
