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
    
    :return: pandas` DataFrame object
    """
    return pd.read_csv(data_file)


def get_df_day_province(target_date, df):
    """
    
    :param target_date: string
    :param df: DataFrame object
    :return: pandas` DataFrame object
    """
    df_city = df
    df_day_city = df_city[df_city['date'] == target_date]
    df_day_province = df_day_city.groupby('province')[['confirm', 'suspect', 'heal', 'dead']].sum()
    df_day_province['date'] = target_date
    return df_day_province


def get_df_province():
    """
    
    :return: pandas` DataFrame object
    """
    df_city = get_df_city()
    date_ls = df_city['date'].unique().tolist()
    df_day_province_ls = [get_df_day_province(target_date=d, df=df_city) for d in date_ls]
    df_province = pd.concat(df_day_province_ls).reset_index()
    df_province['now_confirm'] = df_province['confirm'] - df_province['heal'] - df_province['dead']
    return df_province


def get_df_cn_area():
    """
    
    :return: DataFrame Object
    """
    df_province = get_df_province()
    df_cn_area = pd.pivot(data=df_province,
                          index='date',
                          columns='province',
                          values=['confirm', 'now_confirm', 'suspect', 'heal', 'dead'])
    # df_cn_area.index = df_cn_area['date'].apply(lambda x: x[5:])
    
    return df_cn_area.fillna(0).astype(int).sort_values(by=df_cn_area.index[-1],
                                                        axis=1,
                                                        ascending=False)


# def get_df_cn_area_all(column_name):
#     """
#
#     :param column_name: string
#     :return: DataFrame Object
#     """
#     df_province = get_df_province()
#     area_ls = df_province['province'].unique().tolist()
#     df_cn_area_ls = [get_df_cn_area(area=area, column_name=column_name, df=df_province) for area in area_ls]
#     df_cn_area_all = pd.concat(df_cn_area_ls, axis=1)
#     return df_cn_area_all.fillna(0).astype(int).sort_values(by=df_cn_area_all.index[-1],
#                                                             axis=1,
#                                                             ascending=False)


def get_figure_all():
    pass


if __name__ == '__main__':
    # print(get_df_cn_area_all(column_name='confirm'))
    print(get_df_province())
    print(get_df_cn_area())
    
