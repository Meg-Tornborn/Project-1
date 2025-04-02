import sys
import scipy
import scipy.stats as ss
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import random

part_rate = pd.read_csv('SAT_CT_District_Participation_2012.csv', 
                        encoding='utf-8',  
                        names=['District', 'Participation Rate'], skiprows=1)                                                                                

part_rate.head(129)

mean_rates = part_rate['Participation Rate'].mean()
stdev_rates = part_rate['Participation Rate'].std(ddof=0)
print('Mean rates are {:.2f}'.format(mean_rates))
print('Standard deviation is {:.2f}'.format(stdev_rates))

zscore_rates = ss.zscore(part_rate['Participation Rate'], ddof=0)
part_rate = part_rate.assign(zscore=zscore_rates)
part_rate.head(129)