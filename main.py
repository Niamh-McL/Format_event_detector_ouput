# -*- coding: utf-8 -*-
"""
Created on Thu May  2 14:22:03 2024

@author: niamh
"""

from params import rat, sample_rate, startIndex, endIndex, SWD_events_path, save_folder
from processing import extract_SWD_events_in_time_window

startSec = startIndex / sample_rate
endSec = endIndex / sample_rate

print(startSec)
print(endSec)

SWD_events_BL1_round = extract_SWD_events_in_time_window(SWD_events_path, startSec, endSec)

save_path = f'{save_folder}/{rat}_24h_reformatted_file.csv'
SWD_events_BL1_round .to_csv(save_path, index=False)

