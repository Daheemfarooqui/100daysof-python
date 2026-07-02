def transform_data(df):
    df = df[df['joining_date']<='26-06-30']
    print('transformation done')
    return df