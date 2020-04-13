import matplotlib.pyplot as plt
from covid_panda import *
import pandas as pd



def plot_global_regions(df, dtype, regions,start):
    ''' plot global df and label for legend. '''
    
    df = df.set_index('Country/Region').T[regions]
    l = df.count()
    
    for region in regions:
        plt.plot(df[f'{region}'][start:], label = f'{region}')
    
    return 
    


def plot_all_subregion_sums(df,regions,start):
    ''' adds sum column to df then plots those sums  given a df and a list of regions.'''
    
    df = add_sum_column_for_subregion(df,regions)

    for region in regions:
    
        plt.plot(df[f'{region} total'][start:], label = f'{region} sum',marker = "o")

    return 

def plot_all_region_sums(df,regions,start):
    ''' adds sum column to df then plots those sums  given a df and a list of regions.'''
    
    df = add_sum_column_for_region(df,regions)

    for region in regions:
    
        plt.plot(df[f'{region} total'][start:], label = f'{region} sum',marker = "o")

    return 


