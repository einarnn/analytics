import pandas as pd
import random

BASE_SECURITY_ACES = 100
NUM_POINTS = 1440

def gen_next_data(slot, last_y):
    if slot <= 450:
        # 0000 to 0730: morning befure people arrive
        retval = 100 + int(random.random() * 8 - 4)
    elif slot <= 600:
        # 0730 to 1000: people start arriving
        retval = last_y + int(random.random() * 15 - 5)
    elif slot <= 720:
        # 1000 to 1200: a kind of plateau
        retval = last_y + int(random.random() * 3 - 1.5)
    elif slot <= 780:
        # 1200 to 1300: some people go to lunch
        retval = last_y + int(random.random() * 8 - 5)
    elif slot <= 840:
        # 1300 to 1400: people come back
        retval = last_y + int(random.random() * 8 - 3)
    elif slot <= 1020:
        # 1400 to 1700: steadyish state
        retval = last_y + int(random.random() * 3 - 1.5)
    elif slot <= 1260:
        # 1700 to 2100: people leave office
        retval = last_y + int(random.random() * 12 - 8)
    else:
        # after 2100: steadyish state
        retval = 100 + int(random.random() * 8 - 4)
    if retval < 100:
        return 100
    else:
        return retval


def gen_random_data_frame(first_index=0):
    '''
    Generate semi-normalized data for a "day" of logons & logoffs. Only semi-
    normalized because the values are still absolute, and only the time is
    normalized (to a data point per minute, not absolute time).
    '''
    last_y = BASE_SECURITY_ACES
    time_vals = []
    y_vals = []
    for i in range(first_index, first_index + NUM_POINTS):
        time_vals.append(i)
        last_y = gen_next_data(i % 1440, last_y)
        y_vals.append(last_y)
    df = pd.DataFrame({'Time': time_vals, 'Security ACEs': y_vals})
    return df
