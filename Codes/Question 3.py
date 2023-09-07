# Q =https://leetcode.com/problems/customers-who-never-order/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata

import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    result_df = customers.merge(orders, left_on='id', right_on='customerId', how='left')
    result_df = result_df[result_df['customerId'].isnull()]
    result_df.rename(columns ={"name":"Customers"},inplace =True)
    output = result_df[['Customers']]
    return output
