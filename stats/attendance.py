##  IMPORTS 
import pandas as pd
import matplotlib.pyplot as plt 

from .data import games

##  SELECT AND PLOT DATA
########################
## Select Attendance Data
attendance = games.loc[(games['type'] == 'info') & (games['multi2'] == 'attendance'), ['year', 'multi3']]

##  Column Labels
attendance.columns = ['year', 'attendance']

##  Convert to Numeric
attendance.loc[:, 'column'] = pd.to_numeric(attendance.loc[:, 'column'])

##  Plot DataFrame
attendance.plot(x='year', y='attendance', figsize=(15, 7), kind='bar')
plt.xlabel('Year')  ##  x axis 
plt.ylabel('Attendance')    ##  y axis
plt.axhline(y = attendance['Year'].mean(), label='Mean', linestyle = '--', color = 'green')
plt.show() 