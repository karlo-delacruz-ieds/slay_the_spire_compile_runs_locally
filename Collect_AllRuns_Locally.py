# # Load Libraries
import glob
import os
import json
import numpy as np
import pandas as pd


# # Get Multiple Json Files

json_files = []
chars = ['IRONCLAD','THE_SILENT','DEFECT','WATCHER'] # assuming these files are in the same directory as your code.

for char in chars:
    path = ".\{0}".format(char) # get files in the folder
    print(path)
    json_file = glob.glob(os.path.join(path, "*.RUN")) #make list of paths
    json_files = json_files + json_file
    

# combine multiple json files into one data frame
prep_data = pd.DataFrame()

cnt = 0
tot_cnt = len(json_files)

for file in json_files:
    # get counts of all attempts (all runs)
    with open(file) as json_data:
        data = json.load(json_data)
    
    cnt = cnt + 1
    data = pd.json_normalize(data)
    
    prep_data = prep_data.append(data, ignore_index = True)
    print(str(cnt) + "/" + str(tot_cnt), sep = ' ', end = '\r', flush = True) # print dynamically
    
# filter ascension 20 runs
#prep_data = prep_data[prep_data['ascension_level'] == 20]

# select the columns  to be used
prep_data = prep_data[['gold_per_floor', 'floor_reached', 'playtime', 'items_purged', 'score',
       'play_id', 'local_time', 'is_ascension_mode', 'campfire_choices',
       'neow_cost', 'seed_source_timestamp', 'circlet_count', 'master_deck',
       'relics', 'potions_floor_usage', 'damage_taken', 'seed_played',
       'potions_obtained', 'is_trial', 'path_per_floor', 'character_chosen',
       'items_purchased', 'campfire_rested', 'item_purchase_floors',
       'current_hp_per_floor', 'gold', 'neow_bonus', 'is_prod', 'is_daily',
       'chose_seed', 'campfire_upgraded', 'win_rate', 'timestamp',
       'path_taken', 'build_version', 'purchased_purges', 'victory',
       'max_hp_per_floor', 'card_choices', 'player_experience',
       'relics_obtained', 'event_choices', 'is_beta', 'boss_relics',
       'items_purged_floors', 'is_endless', 'potions_floor_spawned',
       'killed_by', 'ascension_level', 'special_seed']]

prep_data.to_json("LocalA20Runs.json")
prep_data.to_csv("LocalA20Runs.csv", index = False)


