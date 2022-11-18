import pandas as pd


def listclient(filepath):

    configpath = filepath
    df=pd.read_excel(configpath,sheet_name='Client config')
    client_list = df[df.columns[1]].values.tolist()
    print(client_list)
    return client_list

