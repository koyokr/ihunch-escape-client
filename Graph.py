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

    figure = sns.relplot(x="hour", y="ihunch", kind="line", hue="day", legend="full", data=df)
    figure.set(xlim=(-1,24), ylim=(0,1))
    
def week_to_day(jsonFV): ##오늘을 기준으로 일주일간 json 파일 
    '''
    week = datetime.date.today() - timedelta(weeks=1)
    week_list = []
    
    for i in range(7):
        week += timedelta(1)
        week_list.extend(json.load(open(week.strftime('%Y%m%d') + '.json', 'r', encoding ='utf-8')))
    '''
    
    df = pd.DataFrame(jsonFV, columns=('date', 'human', 'ihunch'))
    df.date = pd.to_datetime(df['date'])
    df['day'] = df.date.dt.day.astype(int)
    df['ihunch'] = df['ihunch'].astype(float)
    
    df = df.groupby(['day'])['ihunch'].mean().to_frame().reset_index()

    figure = sns.relplot(x="day", y="ihunch", kind="line", legend="full", data=df)

def week_to_hour(jsonFV): ##오늘을 기준으로 일주일간 json 파일
    '''
    week = datetime.date.today() - timedelta(weeks=1)
    week_list = []
    
    for i in range(7):
        week += timedelta(1)
        week_list.extend(json.load(open(week.strftime('%Y%m%d') + '.json', 'r', encoding ='utf-8')))
    '''
    
    df = pd.DataFrame(week_list, columns=('date', 'human', 'ihunch'))
    df.date = pd.to_datetime(df['date'])
    df['hour'] = df.date.dt.hour.astype(int)
    df['day'] = df.date.dt.day.astype(int)
    df['ihunch'] = df['ihunch'].astype(float)
    

    df = df.set_index(['day','hour'])['ihunch']
    df = df.groupby(['day','hour']).mean().to_frame().reset_index()
    
    figure = sns.relplot(x="hour", y="ihunch", kind="line", hue="day", legend="full", data=df)
    figure.set(xlim=(-1,24), ylim=(0,1))

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
    print(df)
    df = df.groupby(['hour','minute']).mean().to_frame().reset_index()
    figure = sns.relplot(x="minute", y="ihunch", kind="line", hue="hour", legend="full", data=df)
    figure.set(xlim=(-1,61), ylim=(0,1))

