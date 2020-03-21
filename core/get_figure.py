#!/usr/bin/env python
# coding=utf-8

"""
@File：get_figure.py
@Author：MicroKing
@Date：2020/3/21 13:36
@Desc:
"""
import os
from pyecharts.charts import Map, Timeline
from pyecharts import options as opts
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
from core import get_df


def province_map(label_name, column_name):
    """
    column_name in ['confirm', 'now_confirm', 'heal', 'dead']
    :param label_name: string
    :param column_name: string
    :return:
    """
    city_data = get_df.get_df_city()
    df_province = get_df.get_df_province()
    # 初始化图像大小
    tl = Timeline(init_opts=opts.InitOpts(width='1500px', height='700px'))
    # 设置播放速度
    tl.add_schema(play_interval=1000)
    for target_date in city_data['date'].unique():
        confirm_map = Map()
        df_day_province = df_province[df_province['date'] == target_date]
        map_data_ls = [list(z) for z in zip(df_day_province['province'], df_day_province[column_name])]
        # label_opts 参数 is_show 用于设置显示地区的名称，当 is_show 为 False 时，不显示，默认为 True
        confirm_map.add(label_name, map_data_ls, "china", label_opts=opts.LabelOpts(is_show=False))
        # 设置要显示的标题，这里为每当日的病例数及日期
        title = f"{df_day_province[column_name].sum():,.0f}\n\n{target_date[-5:]}"
        # 设置区间分组
        pieces =[{'min': 10000, 'color': '#4F070D'},
                 {'min': 1000, "max": 9999, 'color': '#811C24'},
                 {'min': 500, "max": 999, 'color': '#CB2A2F'},
                 {'min': 100, "max": 499, 'color': '#E55A4E'},
                 {'min': 10, "max": 99, 'color': '#F59E83'},
                 {'min': 1, "max": 9, 'color': '#FDEBCF'},
                 {'max': 0, 'color': '#FFFFFF', 'label': '0'}]
        # map图的全局设置，包括标题、图例、可视化图等选项的位置参数
        confirm_map.set_global_opts(title_opts=opts.TitleOpts(title=title, pos_left='46%', pos_top='15%'),
                                    legend_opts=opts.LegendOpts(pos_top='15%', pos_left='40%'),
                                    visualmap_opts=opts.VisualMapOpts(max_=70000,
                                                                      is_piecewise=True,
                                                                      pos_left='20%',
                                                                      pos_bottom='8%',
                                                                      pieces=pieces))
    
        tl.add(confirm_map, target_date)
    return tl


if __name__ == '__main__':
    pass