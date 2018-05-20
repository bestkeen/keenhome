#coding:utf-8
import tushare as ts
import pandas as pd
import sys
import time
import csv
import os
#with open('/root/sql/qz_day_block/data/2018-05-15-day.csv','r') as f:

with open('/home/keen/sql/day_k_stock/data/2018-05-18-day.csv','r') as f:
    reader = csv.reader(f)
    my_list = list(reader)

for stock in my_list:
	df = ts.get_sina_dd(stock[0],date = '2018-05-17' ,vol=200)
	if str(df)!= 'None':
		df['pv'] = df.price*df.volume
		df['pp'] = df.price - df.preprice
		s_data = df[(df['pv']> int(stock[5])) & (((df['pp']<3) & (df['pp']>0.005)) | (df['pp']< -0.005))]
		b_data = df[(df['pv']> int(stock[4])) & (df['pv']< int(stock[5])) & (((df['pp']<3) & (df['pp']>0.01)) | (df['pp']< -0.01))]
#		s_data = df[(df['time']> '13:30:00') &(df['pv']> int(stock[5])) & (((df['pp']<3) & (df['pp']>0.005)) | (df['pp']< -0.005))]
#		b_data = df[(df['time']> '13:30:00') &(df['pv']> int(stock[4])) & (df['pv']< int(stock[5])) & (((df['pp']<3) & (df['pp']>0.01)) | (df['pp']< -0.01))]
#		s_data = df[(df['time']> '11:00:00') &(df['time']< '13:30:00') &(df['pv']> int(stock[5])) & (((df['pp']<3) & (df['pp']>0.005)) | (df['pp']< -0.005))]
#		b_data = df[(df['time']> '11:00:00') &(df['time']< '13:30:00') &(df['pv']> int(stock[4])) & (df['pv']<stock[5]) & (((df['pp']<3) & (df['pp']>0.01)) | (df['pp']< -0.01))]
		if len(b_data) != 0:
			print ('**************Big volumes***************')
			print (b_data.reset_index(drop=True))
		if len(s_data) != 0:
			print ('************Super volumes***************')
			print (s_data.reset_index(drop=True))
