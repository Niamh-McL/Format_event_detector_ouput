# -*- coding: utf-8 -*-
"""
Created on Thu May  2 14:22:03 2024

@author: niamh
"""

import pandas as pd

from params import rat, sample_rate, startIndex, endIndex, SWD_events_path, save_folder

#only selecting events in the 24 hours of interest

startSec = startIndex / sample_rate
endSec = endIndex / sample_rate

print(startSec)
print(endSec)

"To load the data, put file location and name below using double back to front slash"

# Load SWD events from .csv
SWD_events = pd.read_csv(SWD_events_path, delimiter=",", header=None)

SWD_events.rename(columns={0: 'start_sec', 1:'end_sec'}, inplace=True)

SWD_events['duration'] = SWD_events['end_sec'] - SWD_events['start_sec']
SWD_events = SWD_events.round(1)

SWD_events_BL1 = []
for index in range(len(SWD_events)):
    if (SWD_events.iloc[index, 0] > startSec) &  (SWD_events.iloc[index, 1] < endSec):
        SWD_events_BL1.append(SWD_events.iloc[index, :])

SWD_events_BL1 = pd.DataFrame(SWD_events_BL1)

SWD_events_BL1['start_sec'] -= startSec
SWD_events_BL1['end_sec'] -= startSec

SWD_events_BL1_round = SWD_events_BL1.round(1)

save_path = f'{save_folder}/{rat}_24h_reformatted_file.csv'
SWD_events_BL1_round .to_csv(save_path, index=False)

