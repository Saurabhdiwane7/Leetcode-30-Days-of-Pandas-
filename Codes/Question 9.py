#Q = https://leetcode.com/problems/rearrange-products-table/submissions/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata

import pandas as pd

def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:
    melted_df = pd.melt(products, id_vars=['product_id'], var_name='store', value_name='price')
    result_df = melted_df.dropna(subset=['price'])
    result_df = result_df.sort_values(by=['product_id'])
    result_df = result_df.reset_index(drop=True)
    return result_df
