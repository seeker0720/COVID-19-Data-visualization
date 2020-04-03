#!/usr/bin/env python
# coding=utf-8

"""
@File：get_figure.py
@Author：MicroKing
@Date：2020/3/21 13:36
@Desc:
"""
import os
from pyecharts.charts import Map, Timeline, Line, Tab
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
    df_province = get_df.get_df_province()
    # 初始化图像大小
    tl = Timeline(init_opts=opts.InitOpts(width='1500px', height='700px'))
    # 设置播放速度
    tl.add_schema(play_interval=1000)
    for target_date in df_province['date'].unique():
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


def area_line(label_name, column_name):
    df_cn_area_all = get_df.get_df_cn_area()[column_name]
    dates = df_cn_area_all.index.map(lambda x:x[5:]).tolist()
    global_setting = dict(datazoom_opts=[opts.DataZoomOpts(type_='inside'), opts.DataZoomOpts()],
                          legend_opts=opts.LegendOpts(pos_top='3%'),
                          yaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(formatter="{value} 人"),
                                                   splitline_opts=opts.SplitLineOpts(is_show=True)),
                          xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=60)),
                          tooltip_opts=opts.TooltipOpts(axis_pointer_type='cross'))

    line = Line(init_opts=opts.InitOpts(width='1500px', height='700px'))
    line.add_xaxis(dates)
    for p in df_cn_area_all.columns:
        line.add_yaxis(p, df_cn_area_all[p], label_opts=opts.LabelOpts(is_show=False), is_selected=False)
    line.set_global_opts(title_opts=opts.TitleOpts(title=f"Line-全国{label_name}病例趋势by_province"),
                         **global_setting)
    return line


def get_figure_area_all():
    tab_area = Tab(page_title='Line-Area')
    tab_area.add(area_line(label_name='累计确诊', column_name='confirm'), 'COVID-19各地区病例趋势图(cn当日累计确诊病例)')
    tab_area.add(area_line(label_name='现有确诊', column_name='now_confirm'), 'COVID-19各地区病例趋势图(cn当日现有确诊病例)')
    tab_area.add(area_line(label_name='累计治愈', column_name='heal'), 'COVID-19各地区病例趋势图(cn当日累计病例)')
    tab_area.add(area_line(label_name='累计死亡', column_name='dead'), 'COVID-19各地区病例趋势图(cn当日累计死亡病例)')
    return tab_area


def get_figure_map_all():
    tab_map = Tab(page_title='Map-Area')
    tab_map.add(province_map(label_name='现有确诊', column_name='now_confirm'), 'COVID-19疫情动态图(cn当日现有确诊病例数)')
    tab_map.add(province_map(label_name='累计确诊', column_name='confirm'), 'COVID-19疫情动态图(cn当日累计确诊病例数)')
    return tab_map


if __name__ == '__main__':
    pass