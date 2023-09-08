#Q - https://leetcode.com/problems/delete-duplicate-emails/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata

import pandas as pd

def delete_duplicate_emails(person: pd.DataFrame) -> None:
    df = person.drop_duplicates(subset="email",keep ="first",inplace =True)
    return df
