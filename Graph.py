{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 405,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0    17\n",
      "1    17\n",
      "2    18\n",
      "3    18\n",
      "Name: day, dtype: int32\n",
      "0    yesterday\n",
      "1    yesterday\n",
      "2        today\n",
      "3        today\n",
      "Name: day, dtype: object\n"
     ]
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 447.35x360 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "import json\n",
    "import numpy as np\n",
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt\n",
    "import matplotlib.ticker as ticker\n",
    "import seaborn as sns\n",
    "import datetime\n",
    "\n",
    "\n",
    "def yesterday_today(jsonFV): ## 파일은 어제 오늘 json 파일 합친 내용으로\n",
    "    yesterday = datetime.date.today() - timedelta(1)\n",
    "\n",
    "    #filename = yesterday.strftime('%Y%m%d') + '.json'\n",
    "    #jsonFV = json.loads(open(filename, 'r', encoding='utf-8').read())\n",
    "    \n",
    "    df = pd.DataFrame(jsonFV, columns=('date', 'human', 'ihunch'))\n",
    "    df.date = pd.to_datetime(df['date'])\n",
    "    \n",
    "    df['day'] = df.date.dt.day.astype(int)\n",
    "    df['day'] = np.where(df['day'] == yesterday.day, 'yesterday', 'today')\n",
    "    df['hour'] = df.date.dt.hour.astype(int)\n",
    "    df['ihunch'] = df['ihunch'].astype(float)\n",
    "    \n",
    "    df = df.set_index(['day','hour'])['ihunch']\n",
    "    df = df.groupby(['day','hour']).mean().to_frame().reset_index()\n",
    "\n",
    "    figure = sns.relplot(x=\"hour\", y=\"ihunch\", kind=\"line\", hue=\"day\", legend=\"full\", data=df)\n",
    "    figure.set(xlim=(-1,24), ylim=(0,1))\n",
    "    \n",
    "def week_to_day(jsonFV): ##오늘을 기준으로 일주일간 json 파일 \n",
    "    '''\n",
    "    week = datetime.date.today() - timedelta(weeks=1)\n",
    "    week_list = []\n",
    "    \n",
    "    for i in range(7):\n",
    "        week += timedelta(1)\n",
    "        week_list.extend(json.load(open(week.strftime('%Y%m%d') + '.json', 'r', encoding ='utf-8')))\n",
    "    '''\n",
    "    \n",
    "    df = pd.DataFrame(jsonFV, columns=('date', 'human', 'ihunch'))\n",
    "    df.date = pd.to_datetime(df['date'])\n",
    "    df['day'] = df.date.dt.day.astype(int)\n",
    "    df['ihunch'] = df['ihunch'].astype(float)\n",
    "    \n",
    "    df = df.groupby(['day'])['ihunch'].mean().to_frame().reset_index()\n",
    "\n",
    "    figure = sns.relplot(x=\"day\", y=\"ihunch\", kind=\"line\", legend=\"full\", data=df)\n",
    "\n",
    "def week_to_hour(jsonFV): ##오늘을 기준으로 일주일간 json 파일\n",
    "    '''\n",
    "    week = datetime.date.today() - timedelta(weeks=1)\n",
    "    week_list = []\n",
    "    \n",
    "    for i in range(7):\n",
    "        week += timedelta(1)\n",
    "        week_list.extend(json.load(open(week.strftime('%Y%m%d') + '.json', 'r', encoding ='utf-8')))\n",
    "    '''\n",
    "    \n",
    "    df = pd.DataFrame(week_list, columns=('date', 'human', 'ihunch'))\n",
    "    df.date = pd.to_datetime(df['date'])\n",
    "    df['hour'] = df.date.dt.hour.astype(int)\n",
    "    df['day'] = df.date.dt.day.astype(int)\n",
    "    df['ihunch'] = df['ihunch'].astype(float)\n",
    "    \n",
    "\n",
    "    df = df.set_index(['day','hour'])['ihunch']\n",
    "    df = df.groupby(['day','hour']).mean().to_frame().reset_index()\n",
    "    \n",
    "    figure = sns.relplot(x=\"hour\", y=\"ihunch\", kind=\"line\", hue=\"day\", legend=\"full\", data=df)\n",
    "    figure.set(xlim=(-1,24), ylim=(0,1))\n",
    "\n",
    "def today(jsonFV): ##오늘꺼 시간-분단위로 그래프 그림\n",
    "    '''\n",
    "    today = datetime.date.today()\n",
    "\n",
    "    filename = today.strftime('%Y%m%d') + '.json'\n",
    "    jsonFV = json.loads(open(filename, 'r', encoding='utf-8').read())\n",
    "    '''\n",
    "    \n",
    "    df = pd.DataFrame(jsonFV, columns=('date', 'human', 'ihunch'))\n",
    "    df.date = pd.to_datetime(df['date'])\n",
    "    \n",
    "    df['hour'] = df.date.dt.hour.astype(int)\n",
    "    df['minute'] = df.date.dt.minute.astype(int)\n",
    "    df['ihunch'] = df['ihunch'].astype(float)\n",
    "    \n",
    "    df = df.set_index(['hour','minute'])['ihunch']\n",
    "    print(df)\n",
    "    df = df.groupby(['hour','minute']).mean().to_frame().reset_index()\n",
    "    figure = sns.relplot(x=\"minute\", y=\"ihunch\", kind=\"line\", hue=\"hour\", legend=\"full\", data=df)\n",
    "    figure.set(xlim=(-1,61), ylim=(0,1))\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
