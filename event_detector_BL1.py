# -*- coding: utf-8 -*-
"""
Created on Thu May  2 14:22:03 2024

@author: niamh
"""

import numpy as np 
import pandas as pd

#only selecting events in the 24 hours of interest
rat = 381

sample_rate = 250.4

startIndex = 12214513
endIndex = 33849072

startSec = startIndex/sample_rate
endSec = endIndex/sample_rate

print(startSec)
print(endSec)

"To load the data, put file location and name below using double back to front slash"
SWD_events_path="C:\\Users\\niamh\\OneDrive\\Desktop\\Analysis\\EEG\\SWD_Sleep_Analysis\\EventDetector\\SCN2A\\SCN2A_381\\intervals_events_TAINI_1047_B_SCN2A_381_SOM1_HELMET-2023_10_16-0000.csv"

# Load SWD events from .csv
SWD_events = pd.read_csv(SWD_events_path, delimiter=",", header=None)
SWD_events['start_sec'] = SWD_events.iloc[:,0].round(1)
SWD_events['end_sec'] = SWD_events.iloc[:,1].round(1)
SWD_events['dur'] = SWD_events['end_sec'] - SWD_events['start_sec'].round(1)
SWD_events = SWD_events[['start_sec', 'end_sec', 'dur']]


SWD_events_BL1 = []
for index in range(len(SWD_events)):
    if (SWD_events.iloc[index, 0] > startSec) &  (SWD_events.iloc[index, 1] < endSec):
        SWD_events_BL1.append(SWD_events.iloc[index, :])
    else:
        continue

SWD_events_BL1 = pd.DataFrame(SWD_events_BL1, columns=['start_sec', 'end_sec', 'dur'])

SWD_events_BL1['start_sec'] = SWD_events_BL1['start_sec']-startSec

SWD_events_BL1['end_sec'] = SWD_events_BL1['end_sec']-startSec

SWD_events_BL1_round = SWD_events_BL1.round(1)

save_folder = "C:\\Users\\niamh\\OneDrive\\Desktop\\Analysis\\EEG\\SWD_Sleep_Analysis\\EventDetector\\SCN2A\\SCN2A_381"

save_path = f'{save_folder}\\{rat}_24h_reformatted_file.csv'
SWD_events_BL1_round .to_csv(save_path, index=False)

#SWD_events_BL1.to_csv(rat,"_SWD_events_BL1.csv", index=False)

