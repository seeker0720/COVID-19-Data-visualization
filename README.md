## COVID-19 Data visualization

![Python Version](https://img.shields.io/badge/Python-3.6%2B-blue?style=plastic)  ![GitHub tag (latest by date)](https://img.shields.io/github/v/tag/seeker0720/COVID-19-Data-visualization?style=plastic)  ![GitHub last commit (branch)](https://img.shields.io/github/last-commit/seeker0720/COVID-19-Data-visualization/master?style=plastic)  ![GitHub stars](https://img.shields.io/github/stars/seeker0720/COVID-19-Data-visualization?style=plastic)  ![GitHub repo size](https://img.shields.io/github/repo-size/seeker0720/COVID-19-Data-visualization?style=plastic)  ![GitHub](https://img.shields.io/github/license/seeker0720/COVID-19-Data-visualization?style=plastic)

- 全国疫情组合图

![COVID-19-Grid.gif](https://i.loli.net/2020/04/12/9ZuxspvHbQC72e5.gif)

- 全国疫情地图

![GIF-map-demo.gif](https://i.loli.net/2020/03/24/sKlU51hgfe3vHcP.gif)

- 全国分地区疫情趋势图

![GIF-line-demo.gif](https://i.loli.net/2020/03/24/AZt31oXKn6Dk8WE.gif)

- 世界疫情地图

![world_map.gif](https://i.loli.net/2020/04/23/DjkcsBtwCEzZXKu.gif)

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
    - JupyterNoteboolFile/(用于生成世界疫情地图)
    - output/（输出的可视化文件目录）
        - *.html
    - README.md
    - requirements.txt



### 注意事项

因为主要使用pyecharts库，默认的静态资源需要连接远程服务器， 如果需要在不能联网的环境上使用 pyecharts，需要离线安装 pyecharts 以及提供本地静态资源 HOST 服务。 具体方法请到该网址查看[ https://assets.pyecharts.org/ ]( https://assets.pyecharts.org/ )

---

项目所用的数据来源于丁香园网站发布的数据，如果需要，请查看该项目[DXY-COVID-19-Data]( https://github.com/BlankerL/DXY-COVID-19-Data )

### 生成图表

#### 生成中国疫情相关图表

激活项目的虚拟环境后，切换目录至**`COVID19/core/`**，执行以下命令

```bash
python run.py
```

生成图表，在**`COVID19/output`**目录下可查看有关国内疫情的图表。

#### 生成世界疫情相关图表

因为生成世界疫情图表所使用的[数据来源]( https://github.com/BlankerL/DXY-COVID-19-Data )有些不同，需要进行较多的数据清洗，故使用Jupyter文档的方式生成，在生成世界疫情图表时，确保已安装可以运行Jupyter文档的环境（建议直接安装Anaconda），直接执行 **JupyterNotebookFile** 目录下的**LTS_DXYArea.ipynb** 文件即可。

