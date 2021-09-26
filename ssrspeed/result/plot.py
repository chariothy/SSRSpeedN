# 要添加一个新单元，输入 '# %%'
# 要添加一个新的标记单元，输入 '# %% [markdown]'
# %%


# %%
import json
import re

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
def exportAsMPlot(result=None, pic_path=None):
    """Matplotlib生成可视化，后被plotly代替
        此处留做技术文档备忘

    Args:
        result (tuple, optional): [description]. Defaults to None.
        pic_path (str, optional): [description]. Defaults to None.
    """
    import pandas as pd
    import matplotlib.pyplot as plt
    import seaborn as sns

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
    
    import plotly.graph_objects as go
    fig = go.Figure()
    fig.add_trace(go.Bar(x=remarks, y=gpings, marker_color=colors, name='Google ping'))
    fig.add_trace(go.Bar(x=remarks, y=pings, name='Ping'))
    fig.update_traces(opacity=0.8)
    fig.update_layout(barmode='overlay', legend=dict(x=0.01, y=0.99))
    
    if pic_path:
        fig.write_html(pic_path)
    fig.show()
        
        
if __name__ == '__main__':
    exportAsPlot()