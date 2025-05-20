import pandas as pd


def extract_SWD_events_in_time_window(SWD_events_path, start_sec, end_sec):
    # Load SWD events from .csv
    SWD_events = pd.read_csv(SWD_events_path, delimiter=",", header=None)
    SWD_events.rename(columns={0: 'start_sec', 1: 'end_sec'}, inplace=True)
    SWD_events['duration'] = SWD_events['end_sec'] - SWD_events['start_sec']
    SWD_events = SWD_events.round(1)

    SWD_events_in_window = []

    for index in range(len(SWD_events)):
        if (SWD_events.iloc[index, 0] > start_sec) & (SWD_events.iloc[index, 1] < end_sec):
            SWD_events_in_window.append(SWD_events.iloc[index, :])

    SWD_events_in_window = pd.DataFrame(SWD_events_in_window)
    SWD_events_in_window['start_sec'] -= start_sec
    SWD_events_in_window['end_sec'] -= start_sec
    SWD_events_in_window = SWD_events_in_window.round(1)

    return SWD_events_in_window
