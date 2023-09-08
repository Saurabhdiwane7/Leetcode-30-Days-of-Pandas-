# Q =https://leetcode.com/problems/find-users-with-valid-e-mails/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata

import pandas as pd

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    df = users[users['mail'].str.contains(r"^[a-zA-Z][a-zA-Z0-9_.-]*@leetcode\.com$")]
    return df
