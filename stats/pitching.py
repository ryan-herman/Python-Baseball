import pandas as pd
import matplotlib.pyplot as plt
from data import games

## Plays DataFrame
plays = games[games['type'] == 'play']

## StrikeOuts DataFrame
strike_outs = plays[plays['event'].str.contains('K')]

## Group Data by Year and Game
strike_outs = strike_outs.groupby(['year', 'game_id']).size()

## Reset Index on Strike Outs
strike_outs = strike_outs.reset_index(name='strike_outs')

## Convert Year and Strike_Outs Columns to Numerics
strike_outs = strike_outs.loc[:, ['year', 'strike_outs']].apply(pd.to_numeric)

## Change Plot Formatting
strike_outs.plot(x = 'year', y = 'strike_outs', kind = 'scatter').legend('Strike Outs')
plt.show()