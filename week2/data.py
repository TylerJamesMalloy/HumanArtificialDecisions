import numpy as np 
import scipy as sp
import pandas as pd 
import seaborn as sns 
import random


columns = ["Participant ID", "Condition", "Choice", "Reward"]
pd.DataFrame([], columns=columns)

participant_ids = ["".join([str(random.randint(3, 9)) for _ in range(10)]) for _ in range(100)]

CONDITIONS  = [1,2,3,4]
TRAILS      = 10
STIMULI     = 100

for participant_id in participant_ids:
    print(participant_id) 