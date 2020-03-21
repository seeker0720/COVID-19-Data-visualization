#!/usr/bin/env python
# coding=utf-8

"""
@File：get_df.py
@Author：MicroKing
@Date：2020/3/21 11:15
@Desc:
"""
import os
import pandas as pd

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data_file = f'{BASE_DIR}{os.sep}data{os.sep}csv{os.sep}city_day_data_byDXY.csv'


def get_df_city():
    """
    
    :return: pandas` Dataframe object
    """
    return pd.read_csv(data_file)


def get_df_day_province(target_date):
    """
    
    :param target_date: string
    :return: pandas` Dataframe object
    """
    df_city = get_df_city()
    df_day_city = df_city[df_city['date'] == target_date]
    df_day_province = df_day_city.groupby('province')[['confirm', 'suspect', 'heal', 'dead']].sum()
    df_day_province['now_confirm'] = df_day_province['confirm'] - df_day_province['heal'] - df_day_province['dead']
    df_day_province['date'] = target_date
    return df_day_province


def get_df_province():
    """
    
    :return: pandas` Dataframe object
    """
    df_city = get_df_city()
    date_ls = df_city['date'].unique().tolist()
    df_day_province_ls = [get_df_day_province(target_date=d) for d in date_ls]
    return pd.concat(df_day_province_ls).reset_index()
    

if __name__ == '__main__':
    print(get_df_province())
