def incress_salary(df):
    df['New_Salary'] = df['Salary'] + df['Salary'] /10 
    return df

def filter_sales(df):
    df = df[df['Department']=='Sales']
    return df