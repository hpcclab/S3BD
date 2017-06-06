# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 14:17:03 2017

Go through the "counts" file and collect the data that needs to be plotted.
Then plot that data.

@author: Jason
"""

import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict

# The x axis
clusterSizes = [10,20,30,40,50,60,70,80]

dataSizes = [50, 100, 150, 200]

# Lists for values for each data set size
# We get one for total terms and files, and average terms and files
totalTerms = defaultdict(list)
totalFiles = defaultdict(list)
averageTerms = defaultdict(list)
averageFiles = defaultdict(list)

g50_tt = []
g50_tf = []
g50_at = []
g50_af = []
g100_tt = []
g100_tf = []
g100_at = []
g100_af = []
g150_tt = []
g150_tf = []
g150_at = []
g150_af = []
g200_tt = []
g200_tf = []
g200_at = []
g200_af = []

# Open every combination of the data sizes and cluster sizes lists
for dSize in dataSizes:
    for cSize in clusterSizes:
        fileName = "counts-" + str(dSize) + "G" + str(cSize) + "C.txt"
        f = open(fileName, 'rb')
        print f.readline().rstrip()
        
        """ Parse the file
        --- File organization:
        --- dSize-cSize
        --- Total Terms-x
        --- Total Files-y
        --- Average Terms-z
        --- Average Files-a
        """
        
        totalTerms[dSize].append(int(f.readline().split('-')[1].rstrip()) / 1000)
        totalFiles[dSize].append(int(f.readline().split('-')[1].rstrip()) / 1000)
        averageTerms[dSize].append(float(f.readline().split('-')[1].rstrip()) / 1000)        
        averageFiles[dSize].append(float(f.readline().split('-')[1].rstrip()) / 1000)
        
        
        f.close()
        
print averageFiles[50]


# Make the figs
plt.plot(clusterSizes, totalTerms[50], marker = 'o', linestyle = '-', color = 'r', label='50GB', linewidth = 2, markersize=10)
plt.plot(clusterSizes, totalTerms[100], marker = '^', linestyle = '--', color = 'b', label='100GB', linewidth=2, markersize=10)
plt.plot(clusterSizes, totalTerms[150], marker = '+', linestyle = '-', color = 'g', label = '150GB', linewidth=2, markersize=10)
plt.plot(clusterSizes, totalTerms[200], marker = '*', linestyle = '--', color = 'r', label = '200GB', linewidth=2, markersize=10)
plt.xlabel('Number of Shards', fontsize=13)
plt.ylabel('Number of Terms (In Thousands)', fontsize=13)
plt.legend(bbox_to_anchor=(1, 1))

plt.savefig('totalTerms_fig.png', dpi=300)

plt.show()

plt.plot(clusterSizes, totalFiles[50], marker = 'o', linestyle = '-', color = 'r', label='50GB', linewidth = 2, markersize=10)
plt.plot(clusterSizes, totalFiles[100], marker = '^', linestyle = '--', color = 'b', label='100GB', linewidth=2, markersize=10)
plt.plot(clusterSizes, totalFiles[150], marker = '+', linestyle = '-', color = 'g', label = '150GB', linewidth=2, markersize=10)
plt.plot(clusterSizes, totalFiles[200], marker = '*', linestyle = '--', color = 'r', label = '200GB', linewidth=2, markersize=10)
plt.xlabel('Number of Shards', fontsize=13)
plt.ylabel('Number of Files (In Thousands)', fontsize=13)
plt.legend(bbox_to_anchor=(1, 1))

plt.savefig('totalFiles_fig.png', dpi=300)

plt.show()

plt.plot(clusterSizes, averageTerms[50], marker = 'o', linestyle = '-', color = 'r', label='50GB', linewidth = 2, markersize=10)
plt.plot(clusterSizes, averageTerms[100], marker = '^', linestyle = '--', color = 'b', label='100GB', linewidth=2, markersize=10)
plt.plot(clusterSizes, averageTerms[150], marker = '+', linestyle = '-', color = 'g', label = '150GB', linewidth=2, markersize=10)
plt.plot(clusterSizes, averageTerms[200], marker = '*', linestyle = '--', color = 'r', label = '200GB', linewidth=2, markersize=10)
plt.xlabel('Number of Shards', fontsize=13)
plt.ylabel('Number of Terms (In Thousands)', fontsize=13)
plt.legend(bbox_to_anchor=(1, 1))

plt.savefig('averageTerms_fig.png', dpi=300)

plt.show()

plt.plot(clusterSizes, averageFiles[50], marker = 'o', linestyle = '-', color = 'r', label='50GB', linewidth = 2, markersize=10)
plt.plot(clusterSizes, averageFiles[100], marker = '^', linestyle = '--', color = 'b', label='100GB', linewidth=2, markersize=10)
plt.plot(clusterSizes, averageFiles[150], marker = '+', linestyle = '-', color = 'g', label = '150GB', linewidth=2, markersize=10)
plt.plot(clusterSizes, averageFiles[200], marker = '*', linestyle = '--', color = 'r', label = '200GB', linewidth=2, markersize=10)
plt.xlabel('Number of Shards', fontsize=13)
plt.ylabel('Number of Files (In Thousands)', fontsize=13)
plt.legend(bbox_to_anchor=(1, 1))

plt.savefig('averageFiles_fig.png', dpi=300)

plt.show()