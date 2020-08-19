import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import seaborn as sns
import datetime


def yesterday_today(jsonFV): ## 파일은 어제 오늘 json 파일 합친 내용으로
    yesterday = datetime.date.today() - timedelta(1)

    #filename = yesterday.strftime('%Y%m%d') + '.json'
    #jsonFV = json.loads(open(filename, 'r', encoding='utf-8').read())
    
    df = pd.DataFrame(jsonFV, columns=('date', 'human', 'ihunch'))
    df.date = pd.to_datetime(df['date'])
    
    df['day'] = df.date.dt.day.astype(int)
    df['day'] = np.where(df['day'] == yesterday.day, 'yesterday', 'today')
    df['hour'] = df.date.dt.hour.astype(int)
    df['ihunch'] = df['ihunch'].astype(float)
    
    df = df.set_index(['day','hour'])['ihunch']
    df = df.groupby(['day','hour']).mean().to_frame().reset_index()
    
    plt.figure(figsize = (8,6), dpi = 80)
    figure = sns.relplot(x="hour", y="ihunch", kind="line", style="day", hue="day", legend ='full', marker='.', linewidth=2, data=df)
    plt.axhline(y=0.5, ls=":", c=".5")
    figure.set(xlim=(0,24), ylim=(0,1))
    
def week_to_day(jsonFV): ##오늘을 기준으로 일주일간 json 파일 
    '''
    week = datetime.date.today() - timedelta(weeks=1)
    week_list = []
    
    for i in range(7):
        week += timedelta(1)
        week_list.extend(json.load(open(week.strftime('%Y%m%d') + '.json', 'r', encoding ='utf-8')))
    '''
    
    df = pd.DataFrame(week_list, columns=('date', 'human', 'ihunch'))
    df.date = pd.to_datetime(df['date'])
    df['day'] = df.date.dt.day.astype(int)
    df['ihunch'] = df['ihunch'].astype(float)
    
    df = df.groupby(['day'])['ihunch'].mean().to_frame().reset_index()
    print(df)
    plt.figure(figsize = (8,6), dpi = 80)
    figure = sns.relplot(x="day", y="ihunch", kind="line", ci=None, marker='o', color='r', dashes=False, linewidth=2, data=df)
    plt.axhline(y=0.5, ls=":", c=".5")
    figure.set(xlim=(week.day, week.day + 7), ylim=(0,1))
    
def week_to_percent(jsonFV): ##오늘을 기준으로 일주일간 json 파일
    '''
    week = datetime.date.today() - timedelta(weeks=1)
    week_list = []
    
    for i in range(7):
        week += timedelta(1)
        week_list.extend(json.load(open(week.strftime('%Y%m%d') + '.json', 'r', encoding ='utf-8')))
    '''
    
    df = pd.DataFrame(week_list, columns=('date', 'human', 'ihunch'))
    df.date = pd.to_datetime(df['date'])
    df['day'] = df.date.dt.day.astype(int)
    df['ihunch'] = df['ihunch'].astype(float) >= 0.50
    
    df = df.set_index(['day'])['ihunch']
    df = df.groupby(['day']).apply(lambda x: sum(x >= 0.50) * 100.0/len(x)).to_frame().reset_index()
    
    plt.figure(figsize = (8,6), dpi = 80)
    figure = sns.barplot(x='day', y='ihunch', data=df, palette='Set3')
    figure.set(ylim=(0,100), ylabel='percentage')
    
    for index, row in df.iterrows():
        figure.text(row.name, row.ihunch, round(row.ihunch,2), color='black', ha="center")

def today(jsonFV): ##오늘꺼 시간-분단위로 그래프 그림
    '''
    today = datetime.date.today()

    filename = today.strftime('%Y%m%d') + '.json'
    jsonFV = json.loads(open(filename, 'r', encoding='utf-8').read())
    '''
    
    df = pd.DataFrame(jsonFV, columns=('date', 'human', 'ihunch'))
    df.date = pd.to_datetime(df['date'])
    
    df['hour'] = df.date.dt.hour.astype(int)
    df['minute'] = df.date.dt.minute.astype(int)
    df['ihunch'] = df['ihunch'].astype(float)
    
    df = df.set_index(['hour','minute'])['ihunch']
    df = df.groupby(['hour','minute']).mean().to_frame().reset_index()
    
    plt.figure(figsize = (8,6), dpi = 80)
    figure = sns.relplot(x="minute", y="ihunch", kind="line", hue="hour", legend="full", data=df)
    figure.set(xlim=(-1,61), ylim=(0,1))

