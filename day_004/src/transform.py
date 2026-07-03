def transform_data(df):
    try:
        df = df[['id', 'name', 'username', 'email', 'address', 'phone', 'website',]]
        print("Transformation done")
        return df
    except Exception as e:
        print(f"Transformation failed: {e}")
        return None