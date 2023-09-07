#Q = https://leetcode.com/problems/article-views-i/submissions/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata

import pandas as pd
def article_views(views: pd.DataFrame) -> pd.DataFrame:
    filtered_df = views[views['author_id'] == views['viewer_id']]

    result_df = pd.DataFrame({'id': filtered_df['author_id'].unique()})

    result_df = result_df.sort_values(by='id')

    return result_df