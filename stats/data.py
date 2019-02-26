##  IMPORTS
import os
import glob
import pandas as pd

##  CLEAN & IMPORT DATA
#######################
##  File Management Object
game_files = glob.glob(os.path.join(os.getcwd(), 'games', '*.EVE')) ##  Create object store of all paths of CSV game files
game_files.sort()    ## sort game files list in place for easier pandas ingestion

##  Read CSV Files Into A List of Game Frames
game_frames = []

for game_file in game_files
    game_frame = pd.read_csv(game_file, names=['type', 'multi2', 'multi3', 'multi4', 'multi5', 'multi6', 'event'])
    game_frames.append(game_frame)

##  Concatenate Pandas DataFrames
games = pd.concat(game_frames)  ##  single dataframe containing all data from event files

##  Data Clean-up
games.loc['??', ['Multi5']] = ''

##  Extract Identifiers to a DataFrame
identifiers = games['multi2'].str.extract(r'(.LS(\d{4}\d{5})')
identifiers = identifiers.fillna(method = 'ffill')  ##  Forward Fill DataFrame
identifiers.columns = ['game_id', 'year']   ##  Rename Column Names

##  Concatenate Identifier Columns
games = pd.concat([games, identifiers], axis=1, sort=False)

##  Fill NaN Values
games = games.fillna(' ')

##  Reduce Memory Use of Games DataFrame  Using Categorical Event Type
games.loc[:, 'type'] = pd.Categorical(games.loc[:, 'type'])

##  Print DataFrame
print(games.head())
