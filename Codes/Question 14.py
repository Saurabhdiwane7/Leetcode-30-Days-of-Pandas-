#Q = https://leetcode.com/problems/number-of-unique-subjects-taught-by-each-teacher/submissions/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata

import pandas as pd

def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    result = teacher.groupby('teacher_id')['subject_id'].nunique().reset_index()
    result.rename(columns ={'subject_id':'cnt'},inplace =True)
    return result