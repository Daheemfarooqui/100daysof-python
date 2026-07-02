

def transform_data(df):
    df = df[df['ep_status'].isin(['ENACH','READY_FOR_DISBURSAL'])]
    df = df[df['fees_amt'] >= 50000]
    print('Data Transformed')
    return df 