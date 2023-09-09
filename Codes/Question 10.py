#Q = https://leetcode.com/problems/calculate-special-bonus/submissions/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata

import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus'] = employees.apply(lambda row: row['salary'] if row['employee_id'] % 2 == 1 and row['name'][0] != 'M' else 0, axis=1)

    result = employees[['employee_id', 'bonus']].sort_values('employee_id').reset_index(drop=True)
    return result