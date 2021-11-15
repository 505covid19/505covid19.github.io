import time
import json
import requests
from datetime import datetime
import pandas as pd
import numpy as np

#在顶部声明 Notebook 类型，必须在引入 pyecharts.charts 等模块前声明
# from pyecharts.globals import CurrentConfig, NotebookType
# CurrentConfig.NOTEBOOK_TYPE = NotebookType.JUPYTER_NOTEBOOK

from pyecharts.charts import Map
import pyecharts.options as opts
# 定义抓取数据函数
def catch_data():
    url = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5'
    reponse = requests.get(url=url).json()
    # 返回数据字典
    data = json.loads(reponse['data'])
    return data
def catch_other_data():
    url = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_foreign'
    reponse = requests.get(url=url).json()
    # 返回数据字典
    data = json.loads(reponse['data'])
    return data
print(1)

# 抓取数据并将数据存入data中
data = catch_data()
print(2)

other_data = catch_other_data()
print(3)
# 查看数据的关键词（以列表返回一个字典所有的键）
print(data.keys())
print(other_data.keys())
print("成功")



# 提取各地区数据明细
areaTree = data['areaTree']
# 查看并分析具体数据
# areaTree



# 提取国外地区数据明细
foreignList = other_data['foreignList']
# 查看并分析具体数据
# foreignList



# 国内数据提取
china_data = areaTree[0]['children']  # 提取国内各省数据
china_list = []  # 创建新列表用于储存数据

# 计算china_data中的数据数量（省的数量），逐步提取对应省的数据
for a in range(len(china_data)):
    # 提取数据
    province = china_data[a]['name']  # 提取对应省名称
    confirm = china_data[a]['total']['confirm'] # 提取对应省的累计确诊数据
    heal = china_data[a]['total']['heal'] # 提取对应省的累计治愈数据
    dead = china_data[a]['total']['dead'] # 提取对应省的累计死亡数据
    nowConfirm = confirm - heal - dead # 计算对应省的现有确诊数量
    # 存放数据
    china_dict = {} # 创建新字典用于储存数据
    china_dict['province'] = province # 创建province键存放各省名称
    china_dict['nowConfirm'] = nowConfirm # 创建nowconfirm键存放各省现有确诊数量
    china_list.append(china_dict) # 在china_list列表末尾添加china_dict字典

china_data = pd.DataFrame(china_list) # 将列表转换成panda表格型数据结构
china_data.head() # 读取前五行数据



# 国际数据提取
world_data = foreignList # 提取各国数据
world_list = [] # 创建新列表用于储存数据

# 计算world_data中的数据数量（国家的数量），逐步提取对应国家的数据
for a in range(len(world_data)):
    # 提取数据
    country = world_data[a]['name']  # 提取对应国家的名称
    nowConfirm = world_data[a]['nowConfirm'] # 提取对应国家的现有确诊数据
    confirm = world_data[a]['confirm'] # 提取对应国家的累计确诊数据
    dead = world_data[a]['dead'] # 提取对应国家的累计确诊数据
    heal = world_data[a]['heal'] # 提取对应国家的累计确诊数据
    # 存放数据
    world_dict = {}
    world_dict['country'] = country
    world_dict['nowConfirm'] = nowConfirm
    world_dict['confirm'] = confirm
    world_dict['dead'] = dead
    world_dict['heal'] = heal
    world_list.append(world_dict)

world_data = pd.DataFrame(world_list)
world_data.head()


world_data.loc[world_data['country']=="中国"]



confirm = areaTree[0]['total']['confirm'] # 提取中国累计确诊数据
heal = areaTree[0]['total']['heal'] # 提取中国累计治愈数据
dead = areaTree[0]['total']['dead'] # 提取中国累计死亡数据
nowConfirm = confirm - heal - dead # 计算中国现有确诊数量

world_data = world_data.append({'country': "中国", 'nowConfirm': nowConfirm, 'confirm': confirm, 'heal': heal, 'dead': dead},
                               ignore_index=True)




world_data.loc[world_data['country']=="中国"]
print(4)


# 在顶部声明 Notebook 类型，必须在引入 pyecharts.charts 等模块前声明
# from pyecharts.globals import CurrentConfig, NotebookType
# CurrentConfig.NOTEBOOK_TYPE = NotebookType.JUPYTER_NOTEBOOK

from pyecharts.charts import Map
import pyecharts.options as opts

# 创建图表
m = Map()
# 导入图表数据
m.add("", [list(z) for z in zip(list(china_data["province"]), list(china_data["nowConfirm"]))],
      maptype="china", is_map_symbol_show=False)
# 设置图表参数
m.set_global_opts(title_opts=opts.TitleOpts(title="COVID-19中国现有地区现有确诊人数地图"),
                     visualmap_opts=opts.VisualMapOpts(is_piecewise=True,
                     pieces = [
                        {"min": 5000 , "label": '>5000',"color": "#893448"}, #不指定 max，表示 max 为无限大
                        {"min": 1000, "max": 4999, "label": '1000-4999',"color" : "#ff585e" },
                        {"min": 500, "max": 999, "label": '500-1000',"color": "#fb8146"},
                        {"min": 101, "max": 499, "label": '101-499',"color": "#ffA500"},
                        {"min": 10, "max": 100, "label": '10-100',"color": "#ffb248"},
                        {"min": 1, "max": 9, "label": '1-9',"color" : "#fff2d1" },
                        {"max": 1, "label": '0',"color" : "#ffffff" }]))
# 加载JavaScript
# 在第一次渲染的时候调用 load_javascript() 会预先加载基本 JavaScript 文件到 Notebook 中。
# 如若后面其他图形渲染不出来，则请开发者尝试再次调用，因为 load_javascript 只会预先加载最基本的 js 引用。
# 而主题、地图等 js 文件需要再次按需加载。
# m.load_javascript()

print(5)

# 显示图表
# load_javascript() 和 render_notebook() 方法需要在不同的 cell 中调用，
# 这是 Notebook 的内联机制，其实本质上我们是返回了带有 _html_, _javascript_ 对象的 class。notebook 会自动去调用这些方法。
m.render_notebook()


print(6)


# # 导入国家中英文对照表
# world_name = pd.read_excel("国家中英文对照表.xlsx")
#
# # 比对world_data的"country"列与world_name的"中文"列内容相同的位置，在相应位置插入对应国家的英文名
# world_data_t = pd.merge(world_data, world_name, left_on="country",right_on="中文", how="inner")
#
# world_data_t





m2 = Map()
# m2.add("", [list(z) for z in zip(list(world_data_t["英文"]), list(world_data_t["nowConfirm"]))],
#         maptype="world", is_map_symbol_show=False)
m2.set_global_opts(title_opts=opts.TitleOpts(title="COVID-19世界各国现有确诊人数地图"),
                     visualmap_opts=opts.VisualMapOpts(is_piecewise=True,
                pieces = [
                        {"min": 5000 , "label": '>5000',"color": "#893448"},
                        {"min": 1000, "max": 4999, "label": '1000-4999',"color" : "#ff585e" },
                        {"min": 500, "max": 999, "label": '500-1000',"color": "#fb8146"},
                        {"min": 101, "max": 499, "label": '101-499',"color": "#ffA500"},
                        {"min": 10, "max": 100, "label": '10-100',"color": "#ffb248"},
                        {"min": 0, "max": 9, "label": '0-9',"color" : "#fff2d1" }]))
m2.set_series_opts(label_opts=opts.LabelOpts(is_show=False))
# 加载JavaScript
# 在第一次渲染的时候调用 load_javascript() 会预先加载基本 JavaScript 文件到 Notebook 中。
# 如若后面其他图形渲染不出来，则请开发者尝试再次调用，因为 load_javascript 只会预先加载最基本的 js 引用。
# 而主题、地图等 js 文件需要再次按需加载。
m2.load_javascript()

print(7)




# load_javascript() 和 render_notebook() 方法需要在不同的 cell 中调用，
# 这是 Notebook 的内联机制，其实本质上我们是返回了带有 _html_, _javascript_ 对象的 class。notebook 会自动去调用这些方法。
m2.render_notebook()
print(8)



