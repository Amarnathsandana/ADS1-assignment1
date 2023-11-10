# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 18:00:16 2023

@author: Amarnath Sandana Sevanan
"""

import pandas as pd
import matplotlib.pyplot as plt


def lineplot():
    """
    This function plots the acccessibility of clean fuels 
    and technologies in four countires
    """
    data1 = pd.read_excel("DF.xlsx")
    print(data1)
    plt.figure()
    plt.xlim(2012, 2020)
    #plotting Graph
    plt.plot(data1['Year'], data1['Afghanistan'], label='Afghanistan')
    plt.plot(data1['Year'], data1['Bangladesh'], label='Bangladesh')
    plt.plot(data1['Year'], data1['India'], label='India')
    plt.plot(data1['Year'], data1['China'], label='China')
    
    plt.title("Access to clean fuels and technologies")
    plt.legend()
    plt.xlabel('Year')
    plt.ylabel('Ease of cooking')
    
    plt.savefig('linefig.png')
    plt.show()
    


def piechart():
    """
    This function plots the accessibility of electricity(in %)
    """
    data2 = pd.read_excel("PieGraphData.xlsx")
    print(data2)
    #plotting chart 
    plt.figure(figsize=(8, 7))
    plt.subplot(1, 2, 1)
    paint = ["indianred", "cadetblue", "mediumpurple","plum"]
    plt.pie(
        data2[2010],
        labels=data2['Countries'],
        autopct='%1.1f%%',
        colors=paint
    )
    plt.title('2010')
    plt.subplot(1, 2, 2)
    paint = ["indianred", "cadetblue", "mediumpurple", "plum"]
    plt.pie(
        data2[2020],
        labels=data2['Countries'],
        autopct='%1.1f%%',
        colors=paint
    )
    plt.title('2020')
    
    plt.savefig('piefig2.png')
    plt.show()
    

  
def barchart():
     """
     This function plots the renewable energy consumption of four countires
     """
     data3 = pd.read_excel("BarGraphData.xlsx")
     print(data3)
     #Plotting barchart
     data3.plot( 
         x="Countries",
         y=[2012, 2015],
         kind="bar",
         color=['#81D4FA', 'darkblue']
     )

     plt.title("Renewable Energy Consumption(TJ)")
     plt.xlabel('Countries', fontsize=15)
     plt.ylabel('Energy(TJ)', fontsize=15)
     plt.savefig('barfig.png')
     plt.show()
     
     
lineplot()
piechart()
barchart()












