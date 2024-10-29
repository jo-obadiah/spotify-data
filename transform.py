import extract
import pandas as pd

# data quality checks 
def data_quality(dataframe):
    if dataframe.empty:
        print('no songs downloaded')
        return False
    if pd.series(dataframe['played_at']).is_unique:
        pass
    else:
        raise Exception("primary key might contain duplicates")
    if dataframe.isnull.values.any():
        raise Exception('null values found')
