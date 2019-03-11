import pandas as pd
import matplotlib.pyplot as plt
from frames import games, info, events

## Query for Plays that do not have NP events
plays = games.query("type == 'play' and event != 'NP'")

## Relabel Plays Columns for Readability
plays.columns = ['type', 'inning', 'team', 'player', 'count', 'pitches', 'event', 'game_id', 'year']

## Shift DataFrame to remove the same at bat
pa = plays.loc[plays['player'].shift() != plays['player'], ['year', 'game_id', 'inning', 'team', 'player']]

## Group Plate Appearances
pa = pa.groupby(['year', 'game_id', 'team']).size().reset_index(name='PA')

## Reshape Data by Event Type Per Plate Appearance by Setting Event Index and Unstacking the Resulting Frame
events = events.set_index(['year', 'game_id', 'team', 'event_type'])
events = events.unstack().fillna(0).reset_index()

## Clean Events Columns Labels
events.columns = events.columns.droplevel()
events.columns = ['year', 'game_id', 'team', 'BB', 'E', 'H', 'HBP', 'HR', 'ROE', 'SO']
events = events.rename_axis(None, axis='columns')

## Merge Plate Appearances
events_plus_pa = pd.merge(events, pa, how='outer', left_on=['year', 'game_id', 'team'], right_on=['year', 'game_id', 'team'])

## Merge Team
defense = pd.merge(events_plus_pa, info)

## Calculate DER (Defence Efficiency Ratio)
defense.loc[:, 'DER'] = 1 - ((defense['H'] + defense['ROE']) / (defense['PA'] - defense['BB'] - defense['SO'] - defense['HBP'] - defense['HR']))
defense.loc[:, 'year'] = pd.to_numeric(defense.loc[:, 'year'])

## Reshape Defense with Pivot
der = defense.loc[(defense['year'] >= 1978), ['year', 'defense', 'DER']]
der = der.pivot(index = 'year', columns = 'defense', values = 'DER')

## Plot Formatting - xticks
der.plot(x_compat = True, xticks = range(1978, 2018, 4), rot = 45)
plt.show()