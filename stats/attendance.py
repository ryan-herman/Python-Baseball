##  IMPORTS
import pandas as pd
import matplotlib.pyplot as plt
from data import games

## Select Attendance
attendance = games.loc[(games['type'] == 'info') & (games['multi2'] == 'attendance'), ['year', 'multi3']]


## New Column Labels
attendance.columns = ['year', 'attendance']

## Convert to Numeric
attendance.loc[:, 'attendance'] = pd.to_numeric(attendance.loc[:, 'attendance'])

## Plot Attendance DataFrame
attendance.plot(x='year', y='attendance', figsize=(15,7), kind='bar')
plt.xlabel('Year') # x axis
plt.ylabel('Attendance') # y axis
plt.axhline(y = attendance['attendance'].mean(), label = 'Mean', linestyle='--', color = 'green')
plt.show()