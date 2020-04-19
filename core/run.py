#!/usr/bin/env python
# coding=utf-8

"""
@File：run.py
@Author：MicroKing
@Date：2020/3/21 10:44
@Desc:
"""
import os
import sys
import time

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from core import get_figure


def timer(func):
    def wrapper(*args, **kwargs):
        print('程序开始运行，请稍候...')
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        total_time = end_time - start_time
        print(f'程序执行完毕，用时 {total_time:.2f} s')
    return wrapper


@timer
def main():
    # now_confirm_map = get_figure.province_map(label_name='现有确诊', column_name='now_confirm')
    # now_confirm_map.render(f'{BASE_DIR}{os.sep}output{os.sep}COVID-19疫情动态图(cn当日现有确诊病例数).html')
    #
    # total_confirm_map = get_figure.province_map(label_name='累计确诊', column_name='confirm')
    # total_confirm_map.render(f'{BASE_DIR}{os.sep}output{os.sep}COVID-19疫情动态图(cn当日累计确诊病例数).html')
    #
    # cn_area_total_confirm_line = get_figure.area_line(label_name='累计确诊', column_name='confirm')
    # cn_area_total_confirm_line.render(f'{BASE_DIR}{os.sep}output{os.sep}COVID-19各地区病例趋势图(cn当日累计确诊病例).html')
    #
    # cn_area_now_confirm_line = get_figure.area_line(label_name='现有确诊', column_name='now_confirm')
    # cn_area_now_confirm_line.render(f'{BASE_DIR}{os.sep}output{os.sep}COVID-19各地区病例趋势图(cn当日现有确诊病例).html')
    #
    # cn_area_heal_line = get_figure.area_line(label_name='累计治愈', column_name='heal')
    # cn_area_heal_line.render(f'{BASE_DIR}{os.sep}output{os.sep}COVID-19各地区病例趋势图(cn当日累计治愈病例).html')
    #
    # cn_area_dead_line = get_figure.area_line(label_name='累计死亡', column_name='dead')
    # cn_area_dead_line.render(f'{BASE_DIR}{os.sep}output{os.sep}COVID-19各地区病例趋势图(cn当日累计死亡病例).html')
    map_all = get_figure.get_figure_map_all()
    map_all.render(f'{BASE_DIR}{os.sep}output{os.sep}疫情动态地图.html')
    
    line_all = get_figure.get_figure_area_all()
    line_all.render(f'{BASE_DIR}{os.sep}output{os.sep}疫情动态趋势图.html')
    
    timeline_confirm = get_figure.get_grid_timeline_confirm()
    timeline_confirm.render(f'{BASE_DIR}{os.sep}output{os.sep}新型冠状病毒数据可视化-confirm（China）.html')

    timeline_now_confirm = get_figure.get_grid_timeline_now_confirm()
    timeline_now_confirm.render(f'{BASE_DIR}{os.sep}output{os.sep}新型冠状病毒数据可视化-2now_confirm（China）.html')

    timeline_heal = get_figure.get_grid_timeline_heal()
    timeline_heal.render(f'{BASE_DIR}{os.sep}output{os.sep}新型冠状病毒数据可视化3-heal（China）.html')
    
    
if __name__ == '__main__':
    main()
