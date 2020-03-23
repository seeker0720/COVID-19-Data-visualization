## COVID-19 Data visualization

### 项目简介

通过现有的新型冠状病毒的数据，生成数据可视化展示图。

### 环境依赖

确保使用的Python版本为3.6+，在项目根目录下执行以下还命令

1. 创建名为 env 的虚拟环境

```bash
virtualenv env
```

2. 激活虚拟环境

```bash
source env/bin/activate
```

3. 安装依赖的包

```bash
pip install -r requirements.txt
```

> 注：步骤2， 在windows系统下命令为， `./env/Scripts/activate`。当然可以直接执行步骤3，但不建议这样做

### 目录结构

- COVID19/(项目根目录)
    - core/
        - get_df.py
        - get_figure.py
        - run.py
    - data/（原始数据目录）
        - csv/
            - city_day_data_byDXY.csv
        - json/
    - output/（输出的可视化文件目录）
        - *.html
    - README.md
    - requirements.txt



### 注意事项

因为主要使用pyecharts库，默认的静态资源需要连接远程服务器， 如果需要在不能联网的环境上使用 pyecharts，需要离线安装 pyecharts 以及提供本地静态资源 HOST 服务。 具体方法请到该网址查看[ https://assets.pyecharts.org/ ]( https://assets.pyecharts.org/ )

---

项目所用的数据来源于丁香园网站发布的数据，如果需要，请查看该项目[DXY-COVID-19-Data]( https://github.com/BlankerL/DXY-COVID-19-Data )

