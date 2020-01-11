import pandas as pd
import numpy as np
import random
from functools import reduce 
from operator import mul


BASE_SECURITY_ACES = 100
NUM_POINTS = 1440

def gen_next_data(slot, last_y):
    if slot <= 450:
        # 0000 to 0730: morning before people arrive
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


def gen_val():
    last_y = 0
    slot = 0
    while True:
        if slot <= 450:
            # 0000 to 0730: morning before people arrive
            last_y = 100 + int(random.random() * 8 - 4)
        elif slot <= 600:
            # 0730 to 1000: people start arriving
            last_y = last_y + int(random.random() * 15 - 5)
        elif slot <= 720:
            # 1000 to 1200: a kind of plateau
            last_y = last_y + int(random.random() * 3 - 1.5)
        elif slot <= 780:
            # 1200 to 1300: some people go to lunch
            last_y = last_y + int(random.random() * 8 - 5)
        elif slot <= 840:
            # 1300 to 1400: people come back
            last_y = last_y + int(random.random() * 8 - 3)
        elif slot <= 1020:
            # 1400 to 1700: steadyish state
            last_y = last_y + int(random.random() * 3 - 1.5)
        elif slot <= 1260:
            # 1700 to 2100: people leave office
            last_y = last_y + int(random.random() * 12 - 8)
        else:
            # after 2100: steadyish state
            last_y = 100 + int(random.random() * 8 - 4)
        if last_y < 100:
            last_y = 100
        slot = (slot + 1) % 1440
        yield last_y


def gen_data(timesteps_per_day=1440, days=1):
    assert timesteps_per_day <= 1440
    scaled_ts = None
    ts = np.arange(0, 1440 * days, dtype=int)
    values = np.fromiter(gen_val(), count=1440 * days, dtype=int)
    if timesteps_per_day != 1440:
        # need to scale data
        scaled_ts = np.arange(0, 1440 * days, step=(1440/timesteps_per_day), dtype=int)
        values = np.interp(scaled_ts, ts, values)
        ts = scaled_ts
    return np.vstack((ts, values)).T


def reshape(lst, shape):
    if len(shape) == 1:
        return lst
    n = reduce(mul, shape[1:])
    return [reshape(lst[i*n:(i+1)*n], shape[1:]) for i in range(len(lst)//n)]

if __name__ == '__main__':

    d = gen_data(timesteps_per_day=1440, days=100)
    print(d.shape)
    print(d)
