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
    now_confirm_map = get_figure.province_map(label_name='现有确诊', column_name='now_confirm')
    now_confirm_map.render(f'{BASE_DIR}{os.sep}output{os.sep}COVID-19疫情动态图(cn当日现有确诊病例数).html')
    total_confirm_map = get_figure.province_map(label_name='累计确诊', column_name='confirm')
    total_confirm_map.render(f'{BASE_DIR}{os.sep}output{os.sep}COVID-19疫情动态图(cn当日累计确诊病例数).html')
    
    
if __name__ == '__main__':
    main()
    