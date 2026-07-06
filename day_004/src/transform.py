def transform_data(df):
    try:
        df1 = df.copy()
        print("Transformation done")
        return df
    except Exception as e:
        print(f"Transformation failed: {e}")
        return None