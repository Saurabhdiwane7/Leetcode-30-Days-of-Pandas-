#Q = https://leetcode.com/problems/game-play-analysis-i/submissions/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata

import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    activity['event_date'] = pd.to_datetime(activity['event_date'])
    result = activity.groupby('player_id')['event_date'].min().reset_index()
    result.rename(columns ={'event_date':'first_login'},inplace =True)
    return result