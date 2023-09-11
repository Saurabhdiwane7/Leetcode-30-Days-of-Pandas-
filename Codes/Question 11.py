# Q = https://leetcode.com/problems/find-total-time-spent-by-each-employee/submissions/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata

import pandas as pd
def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    employees['total_time'] = employees['out_time'] - employees['in_time']
    result = employees.groupby(['event_day', 'emp_id'])['total_time'].sum().reset_index()
    result.rename(columns={'event_day': 'day'}, inplace=True)
    return result
