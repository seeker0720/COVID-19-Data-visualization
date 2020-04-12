#!/usr/bin/env python
# coding=utf-8

"""
@File：get_figure.py
@Author：MicroKing
@Date：2020/3/21 13:36
@Desc:
"""
import os
from pyecharts.globals import ThemeType
from pyecharts.charts import Map, Timeline, Line, Bar, Pie, Tab, Grid
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
        confirm_map.add(label_name, map_data_ls, "china",
                        is_map_symbol_show=False, label_opts=opts.LabelOpts(is_show=True))
        # 设置要显示的标题，这里为每当日的病例数及日期
        title = f"{df_day_province[column_name].sum():,.0f}\n\n{target_date[-5:]}"
        # 设置区间分组
        pieces = [
            {'min': 10000, 'color': '#4F070D'},
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
    dates = df_cn_area_all.index.map(lambda x: x[5:]).tolist()
    global_setting = dict(datazoom_opts=[opts.DataZoomOpts(type_='inside'), opts.DataZoomOpts()],
                          legend_opts=opts.LegendOpts(pos_top='3%'),
                          yaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(formatter="{value} 人"),
                                                   splitline_opts=opts.SplitLineOpts(is_show=True)),
                          xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=60)),
                          tooltip_opts=opts.TooltipOpts(axis_pointer_type='cross'))

    line = Line(init_opts=opts.InitOpts(width='1500px', height='700px'))
    line.add_xaxis(dates)
    for p in df_cn_area_all.columns:
        line.add_yaxis(p,
                       df_cn_area_all[p],
                       label_opts=opts.LabelOpts(is_show=False), is_selected=False)
    line.set_global_opts(title_opts=opts.TitleOpts(title=f"Line-全国{label_name}病例趋势by_province"),
                         **global_setting)
    return line


def gird_chart(column, label,target_date, df_city, df_province, df_cn, min_num, max_num):
    chart_df = df_province[df_province['date'] == target_date].sort_values(by=column, ascending=False)
    map_data = [list(z) for z in zip(chart_df['province'], chart_df[column])]
    time_list = df_cn['date'].tolist()
    total_num = df_cn[column].tolist()
    
    min_data, max_data = (min_num, max_num)
    data_mark = []
    i = 0
    for x in time_list:
        if x == target_date:
            data_mark.append(total_num[i])
        else:
            data_mark.append("")
        i = i + 1
    
    map_chart = (
        Map()
            .add(
            series_name="",
            data_pair=map_data,
            #             zoom=1,
            center=[119.5, 34.5],
            is_map_symbol_show=False,
            itemstyle_opts={
                "normal": {"areaColor": "#323c48", "borderColor": "#404a59"},
                "emphasis": {
                    "label": {"show": Timeline},
                    "areaColor": "rgba(255,255,255, 0.5)",
                },
            },
        )
            .set_global_opts(
            legend_opts=opts.LegendOpts(pos_left="27%", pos_top='10%'),
            title_opts=opts.TitleOpts(
                title=f"{target_date[:2]}月{target_date[-2:]}日 全国分地区{label}病例情况（单位：人） 数据来源：丁香园",
                subtitle="",
                pos_left="center",
                pos_top="top",
                title_textstyle_opts=opts.TextStyleOpts(
                    font_size=25, color="rgba(255,255,255, 0.9)"
                ),
            ),
            tooltip_opts=opts.TooltipOpts(
                is_show=True,
                # formatter=JsCode(
                #     """function(params) {
                #     if ('value' in params.data) {
                #         return params.data.value[2] + ': ' + params.data.value[0];
                #     }
                # }"""
                # ),
            ),
            visualmap_opts=opts.VisualMapOpts(
                is_calculable=True,
                dimension=0,
                pos_left="10",
                pos_top="top",
                range_text=["High", "Low"],
                #                 range_color=["white", "yellow","red"],
                range_color=['#FFFFFF', '#FDEBCF', '#F59E83', '#E55A4E', '#CB2A2F', '#811C24', '#4F070D'],
                textstyle_opts=opts.TextStyleOpts(color="#ddd"),
                min_=min_data,
                max_=max_data,
            ),
        
        )
    )
    
    line_chart = (
        Line()
            .add_xaxis(time_list)
            .add_yaxis("", total_num)
            .add_yaxis(
            "",
            data_mark,
            markpoint_opts=opts.MarkPointOpts(data=[opts.MarkPointItem(type_='max', )]),
        )
            .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
            .set_global_opts(
            title_opts=opts.TitleOpts(
                title=f"全国{label}病例总量（单位：人）", pos_left="72%", pos_top="5%"
            ),
            yaxis_opts=opts.AxisOpts(
                splitline_opts=opts.SplitLineOpts(is_show=False)),
            tooltip_opts=opts.TooltipOpts(axis_pointer_type='cross')
        )
    )
    chart_dff = chart_df[chart_df['province'] != '湖北']
    bar_x_data = chart_dff['province'].tolist()
    bar_y_data = [{"name": x[0], "value": x[1]} for x in map_data if x[0] != '湖北']
    bar = (
        Bar()
            .add_xaxis(xaxis_data=bar_x_data)
            .add_yaxis(
            series_name="",
            yaxis_data=bar_y_data,
            label_opts=opts.LabelOpts(
                is_show=True, position="right", formatter="{b} : {c}"
            ),
        )
            .reversal_axis()
            .set_global_opts(
            legend_opts=opts.LegendOpts(pos_left="27%", pos_top='15%'),
            xaxis_opts=opts.AxisOpts(
                axislabel_opts=opts.LabelOpts(is_show=False)
            ),
            yaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(is_show=False)),
            tooltip_opts=opts.TooltipOpts(is_show=False),
            visualmap_opts=opts.VisualMapOpts(
                is_calculable=True,
                dimension=0,
                pos_left="10",
                pos_top="top",
                range_text=["High", "Low"],
                #                 range_color=["white", "yellow","red"],
                range_color=['#FDEBCF', '#F59E83', '#E55A4E', '#CB2A2F', '#811C24', '#4F070D'],
                textstyle_opts=opts.TextStyleOpts(color="#ddd"),
                min_=min_data,
                max_=max_data,
            ),
        )
    )
    
    #     pie_data = [[x[0], x[1]] for x in map_data if x[0] != '湖北']
    pie_data = [
        ['武汉', sum(df_city[(df_city['date'] == target_date) & (df_city['city'] == '武汉')][column])],
        ['HB非武汉', (sum(chart_df[chart_df['province'] == '湖北'][column]) - sum(
            df_city[(df_city['date'] == target_date) & (df_city['city'] == '武汉')][column]))],
        ['非湖北', sum(chart_df[chart_df['province'] != '湖北'][column])]
    ]
    pie = (
        Pie()
            .add(
            series_name="",
            data_pair=pie_data,
            radius=["15%", "35%"],
            center=["80%", "82%"],
            rosetype='radius',
            itemstyle_opts=opts.ItemStyleOpts(
                border_width=1, border_color="rgba(0,0,0,0.3)"
            ),
        )
            .set_global_opts(
            tooltip_opts=opts.TooltipOpts(is_show=True, formatter="{b} {d}%"),
            legend_opts=opts.LegendOpts(is_show=False),
        )
            .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    )
    
    grid_chart = (
        Grid()
            .add(
            bar,
            grid_opts=opts.GridOpts(
                pos_left="10", pos_right="45%", pos_top="50%", pos_bottom="5"
            ),
        )
            .add(
            line_chart,
            grid_opts=opts.GridOpts(
                pos_left="65%", pos_right="80", pos_top="10%", pos_bottom="50%"
            ),
        )
            .add(pie, grid_opts=opts.GridOpts(pos_left="45%", pos_top="60%"))
            .add(map_chart, grid_opts=opts.GridOpts())
    )
    
    return grid_chart


def get_grid_timeline(column, label, df_city, df_province, df_cn, min_num, max_num):
    pass
    timeline = Timeline(
        init_opts=opts.InitOpts(width="1500px", height="850px", theme=ThemeType.DARK)
    )
    time_list = get_df.get_dff_city()['date'].unique().tolist()
    for y in time_list:
        g = gird_chart(column=column,
                       label=label,
                       target_date=y,
                       df_city=df_city,
                       df_province=df_province,
                       df_cn=df_cn,
                       min_num=min_num,
                       max_num=max_num)
        timeline.add(g, time_point=str(y))

    timeline.add_schema(
        orient="vertical",
#         is_auto_play=True,
        is_inverse=True,
        play_interval=5000,
        pos_left="null",
        pos_right="5",
        pos_top="20",
        pos_bottom="20",
        width="60",
        label_opts=opts.LabelOpts(is_show=True, color="#fff"),
    )
    return timeline


def get_figure_area_all():
    tab_area = Tab(page_title='Line-Area')
    tab_area.add(area_line(label_name='累计确诊', column_name='confirm'),
                 'COVID-19各地区病例趋势图(cn当日累计确诊病例)')
    tab_area.add(area_line(label_name='现有确诊', column_name='now_confirm'),
                 'COVID-19各地区病例趋势图(cn当日现有确诊病例)')
    tab_area.add(area_line(label_name='累计治愈', column_name='heal'),
                 'COVID-19各地区病例趋势图(cn当日累计治愈病例)')
    tab_area.add(area_line(label_name='累计死亡', column_name='dead'),
                 'COVID-19各地区病例趋势图(cn当日累计死亡病例)')
    return tab_area


def get_figure_map_all():
    tab_map = Tab(page_title='Map-Area')
    tab_map.add(province_map(label_name='现有确诊', column_name='now_confirm'),
                'COVID-19疫情动态图(cn当日现有确诊病例数)')
    tab_map.add(province_map(label_name='累计确诊', column_name='confirm'),
                'COVID-19疫情动态图(cn当日累计确诊病例数)')
    return tab_map


def get_grid_timeline_confirm():
    timeline = get_grid_timeline(column='confirm',
                                 label='累计确诊',
                                 df_city=get_df.get_dff_city(),
                                 df_province=get_df.get_df_province(dff=get_df.get_dff_city()),
                                 df_cn=get_df.get_df_cn(df=get_df.get_dff_city()),
                                 min_num=1,
                                 max_num=1600)
    return timeline


def get_grid_timeline_now_confirm():
    timeline = get_grid_timeline(column='now_confirm',
                                 label='现有确诊',
                                 df_city=get_df.get_dff_city(),
                                 df_province=get_df.get_df_province(dff=get_df.get_dff_city()),
                                 df_cn=get_df.get_df_cn(df=get_df.get_dff_city()),
                                 min_num=-30,
                                 max_num=1000)
    return timeline


if __name__ == '__main__':
    pass

    # timeline = get_grid_timeline(column='confirm',
    #                              label='累计确诊',
    #                              df_city=get_df.get_dff_city(),
    #                              df_province=get_df.get_df_province(dff=get_df.get_dff_city()),
    #                              df_cn=get_df.get_df_cn(df=get_df.get_dff_city()),
    #                              min_num=1,
    #                              max_num=1600)
    # timeline.render(f"{BASE_DIR}\\output\\新型冠状病毒数据可视化（China）.html")
    # print('ok')