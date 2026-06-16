#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import matplotlib.pyplot as plt
plt.rcParams.update({
    'figure.facecolor': 'none',
    'axes.facecolor': 'none',
    'savefig.facecolor': 'none',
    'text.color': '#e0e0e0',
    'axes.labelcolor': '#e0e0e0',
    'xtick.color': '#e0e0e0',
    'ytick.color': '#e0e0e0',
    'axes.edgecolor': '#e0e0e0'
})


# # Title: Breaking Down the Jets' New Core
# 
# #### **A visual analysis of Garrett Wilson and Sauce Gardner's contracts and cap impact**

# In[44]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from IPython.display import Image


# In[ ]:


plt.rcParams['font.family'] = 'Helvetica'


# The New York Jets have officially locked in two of their brightest young stars, wide receiver Garrett Wilson and cornerback Sauce Gardner, with massive new contract extensions. As the team looks to solidify a competitive core around a reloaded roster, these deals mark a turning point in the Jets’ long-term cap strategy. The visualizations below explore how Wilson and Gardner’s cap hits stack up against the league’s top earners and what it means for the Jets' salary cap outlook through 2030.

# After back-to-back 1,000-yard seasons, Garrett Wilson earned a lucrative extension, positioning him among the NFL’s elite receivers. The chart below compares his projected cap hits to the league's top-paid wideouts like Ja'Marr Chase and Justin Jefferson through 2030.

# In[46]:


Year = range(2025, 2031)

# Top 10 highest-paid WRs
Chase = [23.570000, 26.230000, 33.400000, 41.400000, 53.216000, 0]
Jefferson = [15.167600, 38.987600, 43.487600, 47.487600, 0, 0]
Lamb = [15.332353, 38.600000, 41.600000, 21.391000, 0, 0]
Metcalf = [11.000000, 31.000000, 32.500000, 34.000000, 41.500000, 0]
Wilson = [7.032092, 10.074000, 23.250000, 35.925000, 36.574000, 38.500000]
#Brown = [17.523497, 23.393497, 22.705807, 27.588807, 29.307000, 53.520000]
#StBrown = [13.910000, 33.110000, 28.980000, 41.010000, 0, 0]
#Aiyuk = [9.917105, 15.390281, 41.449281, 43.325281, 14.545000, 0]
#Hill = [27.698750, 51.898750, 4.590000, 4.590000, 0, 0]
#Higgins = [24.061765, 26.750000, 30.050000, 33.550000, 0, 0]

WRs = pd.DataFrame({'Year': Year, 'Chase' : Chase, 'Jefferson' : Jefferson, 'Lamb' : Lamb, 'Metcalf' : Metcalf, 'Wilson' : Wilson})#,
                    #'Brown' : Brown, 'StBrown' : StBrown, 'Aiyuk' : Aiyuk, 'Hill' : Hill, 'Higgins' : Higgins})


# In[47]:


WR_plot = WRs.plot(kind = 'bar', stacked = False, x = 'Year',
                   color = {'Chase' : '#bbbbbb', 'Jefferson' : '#bbbbbb', 'Lamb' : '#bbbbbb', 'Metcalf' : '#bbbbbb', 'Wilson' : '#125740'},
                    #'Brown' : '#bbbbbb', 'StBrown' : '#bbbbbb', 'Aiyuk' : '#bbbbbb', 'Hill' : '#bbbbbb', 'Higgins' : '#bbbbbb'},
                   rot = 0,
                   figsize = (10, 5),
                   legend = False)
WR_plot.set_title('Wilson vs Top 10 Highest-Paid WRs')
WR_plot.ticklabel_format(axis = 'y', style = 'plain')
WR_plot.set_xlabel('')
WR_plot.set_ylabel('Cap Hit (in millions of dollars)')
#WR_plot.legend(labels = ['Garrett Wilson', 'Sauce Gardner', 'Other Players', 'Estimated Remaining'])

plt.savefig('../assets/images/2025-7-25-Jets/wr_comparison.png', bbox_inches='tight')
Image(filename='../assets/images/2025-7-25-Jets/wr_comparison.png')


# Sauce Gardner, already a two-time All-Pro by age 24, secured a deal that rivals the biggest names at cornerback. The chart below compares his cap hits to other top CBs, including Patrick Surtain II and Jalen Ramsey.

# In[48]:


# Top 5 highest-paid CBs
Gardner = [9.376964, 12.250000, 23.703000, 28.950000, 38.850000, 36.100000]
Stingley = [12.027366, 27.095000, 25.500000, 26.500000, 27.500000, 0]
Horn = [7.350400, 23.080400, 22.680400, 28.680400, 30.680400, 0]
Surtain = [8.370000, 16.832000, 26.200000, 29.200000, 30.200000, 0]
Ramsey = [4.904000, 17.229000, 19.149000, 31.049000, 0, 0]

CBs = pd.DataFrame({'Year': Year, 'Gardner' : Gardner, 'Stingley' : Stingley, 'Horn' : Horn, 'Surtain Jr.' : Surtain, 'Ramsey' : Ramsey})


# In[49]:


CB_plot = CBs.plot(kind = 'bar', stacked = False, x = 'Year',
                   color = {'Gardner' : '#125740', 'Stingley' : '#bbbbbb', 'Horn' : '#bbbbbb', 'Surtain Jr.' : '#bbbbbb', 'Ramsey' : '#bbbbbb'},
                   rot = 0,
                   figsize = (10, 5),
                   legend = False)
CB_plot.set_title('Gardner vs Top 5 Highest-Paid CBs')
CB_plot.ticklabel_format(axis = 'y', style = 'plain')
CB_plot.set_xlabel('')
CB_plot.set_ylabel('Cap Hit (in millions of dollars)')
#WR_plot.legend(labels = ['Garrett Wilson', 'Sauce Gardner', 'Other Players', 'Estimated Remaining'])

plt.savefig('../assets/images/2025-7-25-Jets/cb_comparison.png', bbox_inches='tight')
Image(filename='../assets/images/2025-7-25-Jets/cb_comparison.png')


# With both young stars locked in, the Jets’ cap structure reflects major investments in homegrown talent. This stacked bar chart shows how Wilson and Gardner’s contracts impact overall team spending over the next six seasons.

# In[50]:


Jets = [278.596841, 238.871933, 189.612808, 103.385933, 85.424000, 76.100000]
Total = [279.200000, 307.120000, 337.830000, 371.620000, 408.780000, 449.650000]

df = pd.DataFrame({'Year': Year, 'Wilson' : Wilson, 'Gardner' : Gardner, 'Jets' : Jets, 'Total' : Total})


# In[51]:


df['Other Players'] = df['Jets'] - (df['Wilson'] + df['Gardner'])
df['Remaining'] = df['Total'] - df['Jets']


# In[52]:


plot = df[['Year', 'Wilson', 'Gardner', 'Other Players', 'Remaining']].plot(kind = 'bar', stacked = True, x = 'Year',
                                                            color = {'Wilson' : 'black',
                                                                     'Gardner' : '#125740',
                                                                     'Other Players' : '#8cd1ba',
                                                                     'Remaining' : '#bbbbbb'},
                                                            rot = 0,
                                                            figsize = (10, 5))
plot.set_title('Jets Cap Spending (Through 2030)')
plot.ticklabel_format(axis = 'y', style = 'plain')
plot.set_xlabel('')
plot.set_ylabel('Cap Spending (in millions of dollars)')
plot.legend(labels = ['Garrett Wilson', 'Sauce Gardner', 'Other Players', 'Estimated Remaining'])

plt.savefig('../assets/images/2025-7-25-Jets/jets_cap.png', bbox_inches='tight')
Image(filename='../assets/images/2025-7-25-Jets/jets_cap.png')


# With Wilson and Gardner now among the highest-paid players at their respective positions, the Jets are signaling a clear commitment to building around elite, homegrown talent. While these deals carry significant financial weight, they reflect the team's confidence in its young foundation and a willingness to compete at the highest level. The real challenge will be balancing star contracts with roster depth — but for now, New York has secured two cornerstones for the foreseeable future.
# 
# *All contract numbers sourced from Spotrac.com*
