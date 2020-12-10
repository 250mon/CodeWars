import pandas as pd


def rename_columns(df, names):
    #return df.rename({'1': 'A', '2': 'B', '3': 'C'}, axis='columns')
    df2 = df.copy()
    df2.columns = names
    return df2


# def rename_columns(df, names):
#     return pd.DataFrame(data=df.values, columns=names)


if __name__ == '__main__':
    df_input = pd.DataFrame(data=[[1,2,3], [4,5,6]], columns=list('123'))
    names = ('A', 'B', 'C')
    print(rename_columns(df_input, names))