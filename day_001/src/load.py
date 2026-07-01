def save_report(df,output_file):
    df.to_csv(output_file,index = False)
    print("Report Saved Successfully")