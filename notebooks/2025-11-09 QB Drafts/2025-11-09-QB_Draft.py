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


# # Title: insert title here
# 
# #### **insert subheader**

# In[48]:


import pandas as pd
import time
import matplotlib.pyplot as plt
import numpy as np


# In[4]:


# Years to scrape
years = list(range(1970, 2024 + 1))

draft_rows = []

for year in years:
    url = f'https://www.pro-football-reference.com/years/{year}/draft.htm'
    time.sleep(10)
    
    try:
        df = pd.read_html(url)[0]
        df['Year'] = year
        draft_rows.append(df)
        print(f"Scraped year {year}: {len(df)} rows")
    except Exception as e:
        print(f"Error scraping year {year}: {e}")
        continue
  

# Combine all years
if draft_rows:
    draft_df = pd.concat(draft_rows, ignore_index=True)
    draft_df.head()
else:
    print("No data was scraped.")


# In[32]:


qbs = draft_df[draft_df[('Unnamed: 4_level_0', 'Pos')] == 'QB']
qbs.head()


# In[33]:


qbs = qbs[[('Year', ''), 
            ('Unnamed: 0_level_0', 'Rnd'), 
            ('Unnamed: 1_level_0', 'Pick'), 
            ('Unnamed: 2_level_0', 'Tm'), 
            ('Unnamed: 3_level_0', 'Player'), 
            ('Unnamed: 5_level_0', 'Age'), 
            ('Unnamed: 6_level_0', 'To'), 
            ('Misc', 'AP1'), 
            ('Misc', 'PB'), 
            ('Unnamed: 9_level_0', 'St'), 
            ('Approx Val', 'wAV'),
            ('Approx Val', 'DrAV'),
            ('Unnamed: 12_level_0', 'G'), 
            ('Passing', 'Cmp'), 
            ('Passing', 'Att'), 
            ('Passing', 'Yds'), 
            ('Passing', 'TD'), 
            ('Passing', 'Int')]]


# In[34]:


qbs.columns = ['Year', 'Round', 'Pick', 'Tm', 'Player', 'Age', 'To', 'AP1', 'PB', 'St', 'wAV', 'DrAV', 'G', 'Cmp', 'Att', 'Yds', 'TD', 'Int']


# In[35]:


qbs.head()


# In[36]:


print(qbs.shape)


# In[75]:


# Convert 'Pick' column to numeric, coercing errors to NaN, and drop rows where 'Pick' is NaN
qbs['Pick'] = pd.to_numeric(qbs['Pick'], errors='coerce')
qbs = qbs.dropna(subset=['Pick'])
qbs['Pick'] = qbs['Pick'].astype(int)

qbs['wAV'] = pd.to_numeric(qbs['wAV'], errors='coerce')
qbs = qbs.dropna(subset=['wAV'])
qbs['wAV'] = qbs['wAV'].astype(float)

# Convert 'Round' column to numeric
qbs['Round'] = pd.to_numeric(qbs['Round'], errors='coerce')

# Convert 'Year' and 'To' columns to numeric
qbs['Year'] = pd.to_numeric(qbs['Year'], errors='coerce')
qbs['To'] = pd.to_numeric(qbs['To'], errors='coerce')


# In[76]:


qbs['wAV/Yr'] = qbs['wAV'] / (qbs['To'] - qbs['Year'])


# In[80]:


# Set font to Helvetica
plt.rcParams['font.family'] = 'Helvetica'

# Plot
plt.figure(figsize=(12, 8))

# Separate NYJ and other teams
nyj_mask = qbs['Tm'] == 'NYJ'
other_mask = qbs['Tm'] != 'NYJ'

# Plot other teams in gray
plt.scatter(qbs.loc[other_mask, 'Pick'], qbs.loc[other_mask, 'wAV/Yr'], 
            alpha=0.5, color='gray', label='Other Teams')

# Plot NYJ in green
plt.scatter(qbs.loc[nyj_mask, 'Pick'], qbs.loc[nyj_mask, 'wAV/Yr'], 
            alpha=1, color='darkgreen', label='NYJ')

# Label all NYJ points
nyj_qbs = qbs[nyj_mask]
for idx, row in nyj_qbs.iterrows():
    plt.annotate(row['Player'], 
                (row['Pick'], row['wAV/Yr']),
                xytext=(5, 5), textcoords='offset points',
                fontsize=10, alpha=1, fontfamily='Helvetica', color='darkgreen')

# Find and label the highest wAV/Yr points (top 10), excluding NYJ since they're already labeled
top_qbs = qbs[~nyj_mask].nlargest(10, 'wAV/Yr')
for idx, row in top_qbs.iterrows():
    plt.annotate(row['Player'], 
                (row['Pick'], row['wAV/Yr']),
                xytext=(5, 5), textcoords='offset points',
                fontsize=10, alpha=1, fontfamily='Helvetica')

# Add horizontal line at y=0
plt.axhline(y=0, color='black', linewidth=1)

plt.xlabel('Pick')
plt.ylabel('wAV/Yr')
plt.title('QB Draft Pick vs wAV/Yr')
plt.grid(True, which='both', axis='x')
plt.xticks(range(0, 301, 32))
plt.xlim(left=0, right=300)
plt.ylim(bottom=0)
plt.show()


# In[81]:


first_rounders = qbs[qbs['Round'] == 1]


# In[87]:


# Plot
plt.figure(figsize=(12, 8))

# Separate NYJ and other teams
nyj_mask_1 = first_rounders['Tm'] == 'NYJ'
other_mask_1 = first_rounders['Tm'] != 'NYJ'

# Plot other teams in gray
plt.scatter(first_rounders.loc[other_mask_1, 'Pick'], first_rounders.loc[other_mask_1, 'wAV/Yr'], 
            alpha=0.5, color='gray', label='Other Teams')

# Plot NYJ in green
plt.scatter(first_rounders.loc[nyj_mask_1, 'Pick'], first_rounders.loc[nyj_mask_1, 'wAV/Yr'], 
            alpha=1, color='darkgreen', label='NYJ')

# Label all NYJ points
nyj_firsts = first_rounders[nyj_mask_1]
for idx, row in nyj_firsts.iterrows():
    plt.annotate(row['Player'], 
                (row['Pick'], row['wAV/Yr']),
                xytext=(5, 5), textcoords='offset points',
                fontsize=10, alpha=1, fontfamily='Helvetica', color='darkgreen')

# Find and label the highest wAV/Yr points (top 10), excluding NYJ since they're already labeled
top_qbs_1 = first_rounders[~nyj_mask_1].nlargest(5, 'wAV/Yr')
for idx, row in top_qbs_1.iterrows():
    plt.annotate(row['Player'], 
                (row['Pick'], row['wAV/Yr']),
                xytext=(5, 5), textcoords='offset points',
                fontsize=10, alpha=1, fontfamily='Helvetica')

# Add horizontal line at y=0
plt.axhline(y=0, color='black', linewidth=1)

plt.xlabel('Pick')
plt.ylabel('wAV/Yr')
plt.title('QB Draft Pick vs wAV/Yr')
plt.grid(True, which='both', axis='x')
plt.xticks(range(0, 32, 1))
plt.xlim(left=0, right=32)
plt.ylim(bottom=0)
plt.show()

