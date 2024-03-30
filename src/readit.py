import pandas as pd

def read_data(file_path):
    '''
    Read data from the main data source file
    '''
    df = pd.read_csv(file_path)
    return df

def write_req_tidy_data(df):
    '''
    Operations to transform the data and write it to a new csv file
    '''
    #read data
    df = read_data('data/2020RES_APR2019PubDataShare.csv')
    #getting all APR_RATE column names
    prefix = 'APR_RATE'
    apr_rate_cols = df.filter(regex=f'^{prefix}', axis=1).columns
    #names of other required column
    req_cols = ['SCL_NAME', 'SPORT_NAME'] 
    req_cols.extend(apr_rate_cols)
    #new dataframe with selected columns
    df1 = df[req_cols]
    #melt all the APR_RATE columns
    df2 = pd.melt(df1, id_vars=['SCL_NAME', 'SPORT_NAME'], value_vars=req_cols, var_name='APR_RATE_YEAR', value_name = 'APR_RATE')
    #Extract year from APR_RATE_YEAR values
    df2['APR_RATE_YEAR'] = df2['APR_RATE_YEAR'].apply(lambda x:x.split('_')[2])
    
    #Writing to a file
    df2.to_csv('data/APR_tidy.csv', index = False)

def create_gender_column(df):
    '''
    Creates a new gender column from SPORT_NAME from the given data frame
    '''
    df['Gender'] = df['SPORT_NAME'].apply(lambda x: 'Women' if 'Women' in x else('Men' if 'Men' in x else ('Mixed' if 'Mixed' in x else 'Unknown')))
    return df
