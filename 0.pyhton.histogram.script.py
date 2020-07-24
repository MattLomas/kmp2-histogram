#!
# -*- coding: utf-8 -*-

"""Module: KMP-2 Historgram Pre-Exercise
	Create a histogram as per the pre-class exercise sheet.
"""

__author__ = "Matt Lomas"
__copyright__ = "Copyright 2020, The Kanban Project"
__credits__ = ["Kanbanise", "Sandra Wong", "Travis Davidson",
                    "Matt Lomas"]
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Matt Lomas"
__email__ = "mattlomas@promail.com"
__status__ = "Production"

# url for PDF creation > https://stackoverflow.com/questions/35484458/how-to-export-to-pdf-a-graph-based-on-a-pandas-dataframe

# url for histogram in MacOS Numbers > https://discussions.apple.com/thread/3437599


#
# import modules
#

import sys
import math
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from collections import Counter
from statistics import mode
# create the dataframe from simple array

rawdata = np.array([10,8,8,25,22,2,39,6,10,22,9,15,18,2,22,49,10,24,3,8,1,10,22,7,6,19,4,9,17])

print("\n------------\n")
print("Raw Data List:")
print(rawdata)
print("")
print("Data MAX   : ",rawdata.max())
print("Data MIN   :  ",rawdata.min())
print("Classes Bin:   7\n(provided)\n")

# caclulate the class-width CW as (max-min)\7
cw = math.ceil((rawdata.max()-rawdata.min()) / 7)
print("Class-Width:  ",cw,"\n")


# Generate data on commute times.
##histdata = pd.Series(rawdata)


#histdata.plot.hist(grid=True, bins=10, rwidth=0.9,
#                   color='#607c8e')

#histdata.plot.hist(grid=True, bins=10,
#                   color='#607c8e')

##histdata.plot.hist(grid=True, bins=7, rwidth=0.99,
##                   color='#607c8e')


##plt.title("KMP-2 Histogram for Exercise Data")
##plt.xlabel("Counts")
##plt.ylabel("Thing")
##plt.grid(axis='y', alpha=0.75)
##plt.show()

#https://www.tutorialspoint.com/numpy/numpy_statistical_functions.htm#:~:text=mean(),of%20elements%20in%20the%20array.

print("------------\n\n")
listmean = np.mean(rawdata)
print("Mean Def  : sum / (num count)")
print("Mean Val  : ",int(listmean),"\n")

listmedian = np.median(rawdata)
print("Median Def: Odd  - (Num Count) + 1 / 2")
print("            Even - (middle-1 + middle-2) / 2")
print("Median Val: ",int(listmedian),"\n")

listmode = mode(rawdata)
print("Mode Def  : Most repeated number")
print("Mode Val  : ",int(listmode),"\n")
print("Note: the list is bi-modal with '10' and '22'\nstats packages often default to lowest mode collection\n")
print("Sorted Data List:\n",sorted(rawdata),"\n")
print("Counts of List:\n",Counter(rawdata),"\n")

print("------------\n\n")
endsession = input ("Close histogram app?: ")
endseshnum = int(endsession)
print("\nYour number: ", endseshnum)

if (endseshnum==1):
	print("\nclosing app...\n")
	sys.exit()

else:
	print("exiting anyway ; )")
	sys.exit()

