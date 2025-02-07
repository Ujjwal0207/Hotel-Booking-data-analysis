#!/usr/bin/env python
# coding: utf-8

# In[22]:


import pandas as pd 
import numpy as np 
import seaborn as sns 
import matplotlib.pyplot as plt 
import warnings  
warnings.filterwarnings('ignore')  


# In[23]:


df = pd.read_csv('hotel_booking.csv')


# In[24]:


df.head()


# In[25]:


df.shape


# In[26]:


# Remove the last 4 columns
df = df.iloc[:, :-4]


# In[27]:


df.shape


# In[28]:


df.columns


# In[29]:


df.info()


# In[30]:


df.describe(include = 'object')


# In[31]:


for col in df.describe(include = 'object').columns:
    print(col)
    print(df[col].unique())
    print('-'*50)


# In[32]:


df.isnull().sum()


# In[33]:


df.drop(['agent', 'company'], axis=1, inplace=True, errors='ignore')
df.dropna(inplace=True)


# In[34]:


df.isnull().sum()


# In[35]:


df.describe()


# In[36]:


df['adr'].plot(kind='box')


# In[37]:


df = df[df['adr']<5000]


# In[38]:


cancelled_perc = df['is_canceled'].value_counts(normalize=True)
print(cancelled_perc)

plt.figure(figsize=(5, 4))
plt.title('Reservation Status Count')
plt.bar(['Not canceled', 'Canceled'], df['is_canceled'].value_counts(), edgecolor='k', width=0.7)
plt.show()


# In[39]:


plt.figure(figsize=(8, 4))
ax1 = sns.countplot(x='hotel',hue='is_canceled',data = df,palette='Blues')
legend_labels,_=ax1. get_legend_handles_labels()
plt.title('Reservation Status in different hotels',size =20)
plt.xlabel('hotel')
plt.ylabel('number of reservations')
plt.show()


# In[40]:


resort_hotel = df[df['hotel']=='Resort Hotel']
resort_hotel['is_canceled'].value_counts(normalize=True)


# In[42]:


city_hotel = df[df['hotel']=='city Hotel']
city_hotel['is_canceled'].value_counts(normalize=True)


# In[43]:


resort_hotel = resort_hotel.groupby('reservation_status_date')[['adr']].mean()
city_hotel = city_hotel.groupby('reservation_status_date')[['adr']].mean()


# In[44]:


plt.figure(figsize=(20,8))
plt.title('Raverage daily rate in city and resort hotel',fontsize = 30)
plt.plot(resort_hotel.index,resort_hotel['adr'],label = 'Resort Hotel')
plt.plot(city_hotel.index,city_hotel['adr'],label = 'city Hotel')
plt.legend(fontsize = 20)
plt.show()


# In[47]:


# Ensure the 'reservation_status_date' column is in datetime format
df['reservation_status_date'] = pd.to_datetime(df['reservation_status_date'])

# Extract the month from the 'reservation_status_date'
df['month'] = df['reservation_status_date'].dt.month

# Set up the figure size for the plot
plt.figure(figsize=(16, 8))

# Create the countplot
ax1 = sns.countplot(x='month', hue='is_canceled', data=df, palette='bright')

# Adjust the legend position
legend_labels, _ = ax1.get_legend_handles_labels()
ax1.legend(bbox_to_anchor=(1, 1))

# Add titles and labels
plt.title('Reservation Status per Month', size=20)
plt.xlabel('Month')
plt.ylabel('Number of Reservations')

# Adjust legend labels
plt.legend(['Not Canceled', 'Canceled'])

# Show the plot
plt.show()


# In[51]:


plt.figure(figsize=(15, 8))

plt.title('ADR per Month', fontsize=30)


sns.barplot(x='month', y='adr', data=df[df['is_canceled'] == 1].groupby('month')[['adr']].sum().reset_index())

plt.legend(fontsize=20)

plt.show()


# In[53]:


cancelled_data = df [df['is_canceled'] == 1]

top_10_country = cancelled_data['country'].value_counts()[:10]

plt.figure(figsize = (8,8))

plt.title('Top 10 countries with reservation canceled')

plt.pie(top_10_country, autopct = '%.2f', labels = top_10_country.index)

plt.show()


# In[55]:


df['market_segment'].value_counts()


# In[56]:


df['market_segment'].value_counts(normalize=True)


# In[63]:


# Assuming df is your main dataframe
cancelled_data = df[df['is_canceled'] == 1]
not_cancelled_df = df[df['is_canceled'] == 0]

# Group by reservation_status_date and calculate mean ADR
cancelled_df_adr = cancelled_data.groupby('reservation_status_date')[['adr']].mean()
cancelled_df_adr.reset_index(inplace=True)
cancelled_df_adr.sort_values('reservation_status_date', inplace=True)

not_cancelled_df_adr = not_cancelled_df.groupby('reservation_status_date')[['adr']].mean()
not_cancelled_df_adr.reset_index(inplace=True)
not_cancelled_df_adr.sort_values('reservation_status_date', inplace=True)

# Plotting
plt.figure(figsize=(20,6))
plt.title('Average Daily Rate')

plt.plot(not_cancelled_df_adr['reservation_status_date'], not_cancelled_df_adr['adr'], label='Not Cancelled')
plt.plot(cancelled_df_adr['reservation_status_date'], cancelled_df_adr['adr'], label='Cancelled')

plt.legend()
plt.show()


# In[65]:


# Filter data between 2016 and 2017-09 for both cancelled and not cancelled data
cancelled_df_adr = cancelled_df_adr[(cancelled_df_adr['reservation_status_date'] > '2016') & (cancelled_df_adr['reservation_status_date'] < '2017-09')]

not_cancelled_df_adr = not_cancelled_df_adr[(not_cancelled_df_adr['reservation_status_date'] > '2016') & (not_cancelled_df_adr['reservation_status_date'] < '2017-09')]


# In[67]:


plt.figure(figsize = (20,6))

plt.title('Average Daily Rate')
plt.plot(not_cancelled_df_adr['reservation_status_date'], not_cancelled_df_adr['adr'], label = 'not cancelled')
plt.plot(cancelled_df_adr['reservation_status_date'],cancelled_df_adr['adr'],label = 'cancelled')
plt.legend(fontsize = 20)


# In[ ]:




