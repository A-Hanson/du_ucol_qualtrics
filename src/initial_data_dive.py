import pandas as pd



if __name__ == "__main__":
    df = pd.read_excel("../data/202110_1st_audit_C_A_Results.xlsx")
    #print(df.iloc[:, 4].value_counts())
    num_cols = df.shape[1]
    #print(df.info())
    
    for c in df.columns:
        print("---- %s ____" % c)
        print(df[c].value_counts())

    df_summary = df.groupby('Program').count()
    
    
    #print(df_summary.columns)
    