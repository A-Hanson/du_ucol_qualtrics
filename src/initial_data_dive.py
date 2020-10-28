import pandas as pd



if __name__ == "__main__":
    df = pd.read_excel("../data/202110_1st_audit_C_A_Results.xlsx")
    num_cols = df.shape[1]
    unique_course_titles = len(pd.unique(df['Course Title']))
    print(unique_course_titles)
    
    # for c in df.columns:
    #     print("---- %s ____" % c)
    #     print(df[c].value_counts())

    df_summary = df.groupby('Program').count()
    
    
    #print(df_summary.columns)
    