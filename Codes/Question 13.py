#Q = https://leetcode.com/problems/classes-more-than-5-students/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata

import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    class_counts = courses['class'].value_counts().reset_index()
    class_counts.columns = ['class', 'cnt']
    return class_counts[class_counts['cnt'] >= 5][['class']]
