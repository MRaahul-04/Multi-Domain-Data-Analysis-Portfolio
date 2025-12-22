def validate_dataframe(df):
    report = {
        "rows": df.shape[0],
        "columns": df.shape[1],
        "missing_values": df.isnull().sum().to_dict(),
        "duplicates": df.duplicated().sum()
    }
    return report
