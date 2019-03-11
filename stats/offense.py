import pandas as pd
import matplotlib.pyplot as plt
from data import games

## Collect Play Data
plays = games[games['type'] == 'play']
plays.columns = ['type', 'inning', 'team', 'player', 'count', 'pitches', 'event', 'game_id','year']

## Select Only Hits from Play Data
hits = plays.loc[plays['event'].str.contains('^(?:S(?!B)|D|T|HR)'), ['inning', 'event']]

## Convert inning Column of Hits DF to number type
hits.loc[:, 'inning'] = pd.to_numeric(hits.loc[:, 'inning'])

## Replacements Dictionary
replacements = {r'^S(.*)': 'single', r'^D(.*)': 'double', r'^T(.*)': 'triple', r'^HR(.*)': 'hr'}

## Replacement Function
hit_type = hits['event'].replace(replacements, regex=True)

## Add hit_type Column to the Hits DataFrame
hits = hits.assign(hit_type=hit_type)

## Group Data by Inning and Hit Type
hits = hits.groupby(['inning', 'hit_type']).size().reset_index(name='count')

## Convert Hit Type to Categorical
hits['hit_type'] = pd.Categorical(hits['hit_type'], ['single', 'double','triple', 'hr'])

## Sort Hit Data
hits = hits.sort_values(['inning', 'hit_type'])

## Pivot DataFrame to Reshape for Plotting
hits = hits.pivot(index = 'inning', columns = 'hit_type', values = 'count')

## Plot to Stacked Bar Graph
hits.plot.bar(stacked = True)
plt.show()