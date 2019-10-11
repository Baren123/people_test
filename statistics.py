#coding: utf-8

import os
import re
import numpy as np 
import matplotlib.pyplot as plt

# import numpy as np 
# from matplotlib import pyplot as plt 

DATA_PATH = 'D:\Work_Project\python_test\人口年度数据.txt'

txtDict = {}
list_year_x = []
list_population_size_y = []
list_women_pre_y = []
list_city_pre_y = []
list_female_pie = []
list_country_pie = []
male_all = 0
female_all = 0
city_all = 0
country_all = 0

with open(DATA_PATH,'r') as f:
    lines = f.readlines() # 读取所有行  
    for line in lines:
        if line.startswith('#'):
            pass
        else :
            rang_data = line.split(',')
            key = rang_data[0].split('年')[0]  
            value = rang_data[1:]
            txtDict[key] = value
    y_length = len(txtDict)
    print(y_length)
    total_population_x = sorted(txtDict.keys())
    for i in range(y_length):
        fig_total_population_x = int(total_population_x[i])
        fig_total_population_y = int(txtDict[total_population_x[i]][0])
        print("x:%d,%d,y:%d" %(i,fig_total_population_x,fig_total_population_y))
        list_year_x.append(fig_total_population_x)
        list_population_size_y.append(fig_total_population_y)
        list_women_pre_y.append(float(txtDict[total_population_x[i]][2])/float(txtDict[total_population_x[i]][0]))
        list_city_pre_y.append(float(txtDict[total_population_x[i]][3])/float(txtDict[total_population_x[i]][0]))
        if (fig_total_population_x==2016):
            male_all = int(txtDict[total_population_x[i]][1])
            female_all = int(txtDict[total_population_x[i]][2]) 
            city_all = int(txtDict[total_population_x[i]][3])
            country_all = int(txtDict[total_population_x[i]][4])
            print("test")
            print(i)
            print("%d,%d" %(male_all,female_all))
            
        # list_female_pie.append()


    plt.subplot(2, 2, 1)
    plt.title("total population") 
    plt.xlabel("year") 
    plt.ylabel("population size(ten thousand)") 
    plt.plot(list_year_x,list_population_size_y,marker='o') 
 


    plt.subplot(2, 2, 2)       
    plt.title("women and percent of the country's population") 
    plt.xlabel("year") 
    plt.ylabel("precent(%)") 
    plt.plot(list_year_x,list_women_pre_y,'r', marker='o') 
    plt.plot(list_year_x,list_city_pre_y,'b',marker='o', label="city's population") 
    plt.legend(["women", "city's population"], loc='upper center',facecolor='green')

    plt.subplot(2, 2, 3)  
    m_perc = male_all / (male_all+female_all)
    f_perc = female_all / (male_all+female_all)
    labels = ['female','male']
    plt.title("2016")
    # colors = ['blue','yellowgreen']
    # autopct 表示的是使用百分号表示, explode=[0, 0.05]表示两个饼的间隔
    plt.pie([m_perc, f_perc], labels=labels, autopct='%1.1f%%', startangle=90)
    # plt.pie([m_perc, f_perc], colors=colors, labels=labels, autopct='%1.1f%%')

    plt.subplot(2, 2, 4)  
    city_perc = city_all / (city_all+country_all)
    country_perc= country_all / (city_all+country_all)
    labels = ['city','country']
    plt.title("2016")
    # colors = ['blue','yellowgreen']
    # autopct 表示的是使用百分号表示, explode=[0, 0.05]表示两个饼的间隔
    # plt.pie([city_perc, country_perc], colors=colors, labels=labels, autopct='%1.1f%%')
    plt.pie([city_perc, country_perc], labels=labels, autopct='%1.1f%%', startangle=90)
    plt.show() 
    
    
    
 
