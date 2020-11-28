import pandas as pd

def rename_columns(df, names):
    return pd.DataFrame(df, index=names)


if __name__ == '__main__':
    df_input = pd.DataFrame(data=[[1,2,3], [4,5,6]], columns=list('123'))
    names = ('A', 'B', 'C')
    print(rename_columns(df_input, names))