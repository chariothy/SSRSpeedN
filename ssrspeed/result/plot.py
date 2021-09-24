# 要添加一个新单元，输入 '# %%'
# 要添加一个新的标记单元，输入 '# %% [markdown]'
# %%


# %%
import json
import re

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

REG_RATE = re.compile(r'\|?(\d\.?\d?)x\|?')

def get_color(remark:str)->str:
    rate = '1'
    match = REG_RATE.search(remark)
    if match:
        rate = match.groups()[0]

    if rate == '3':
        return 'grey'
    elif rate == '1.5':
        return 'blue'
    elif rate == '1':
        return 'green'
    elif rate == '0.1':
        return 'yellow'
    elif rate == '0.8':
        return 'cyan'
    else:
        return 'black'
    
    
def load_result():
    with open('./results/2021-09-24-15-01-50.json', mode='r') as fp:
        return json.load(fp)
        
# %%
def exportAsPlot(result=None, pic_path=None):
    if result is None:
        result = load_result()
    remarks = ['|'.join(x['remarks'].split('|')[1:]) for x in result]
    pings = [x['ping'] for x in result]
    gpings = [x['gPing'] for x in result]
    dspeeds = [x['dspeed'] for x in result]
    maxspeeds = [x['maxDSpeed'] for x in result]
    colors = [get_color(x['remarks']) for x in result]
    
    df = pd.DataFrame({'ping': pings, 'gping': gpings, 'remark': remarks})
    plt.figure(figsize=(20,10))
    sb1 = sns.barplot(x = 'remark', y = 'gping', data = df, color = 'blue', palette=colors)
    sb2 = sns.barplot(x = 'remark', y = 'ping', data = df, color = 'red')

    for item in sb2.get_xticklabels():
        item.set_rotation(90)
    plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
    plt.tight_layout()
    if pic_path:
        plt.savefig(pic_path)
    else:
        plt.show()
