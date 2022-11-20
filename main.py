import pandas as pd
import getpass

import listclients as lc
#listclients is a local module being imported which has client lists
import os
import glob


current_user = getpass.getuser()

# path where the config file resides
filepath = r"C:\Users\Shamm\Downloads\Client config.xlsx"
filedate  = '20221118'
clientlist = []
# reading clients to the list (clientlist)
#clientlist = lc.listclient(filepath)
clientlist = ['kwala']

# for each client

for i in clientlist:

    ##deriving dynamic path with the client name
    #config_path = rf"C:\Users\{current_user}\Cache Investment Management Pty Ltd\Fund operations - Documents\Database\Global Files\

    config_path = rf"C:\Users\{current_user}\Cache Investment Management Pty Ltd\Fund operations - Documents\Operations\Client\\.format(current_user)"

    #'C:\Users\Bharathy\Cache Investment Management Pty Ltd\Fund operations - Documents\Operations\Client\Bloom\Redemptions'

    # 'C:\Users\{current_user}\Cache Investment Management Pty Ltd\Fund operations - Documents\Operations\Client\Bloom\Redemptions'
    #     #file_path_a= r""
    #     redemption_file_patha = r"C:\Users\Shamm\OneDrive\Desktop\Redemption Model File\Clients\\"
    #     redemption_file_pathb = r"Redemptions\Funded Redemptions - "
    #     finalpath = redemption_file_patha+i+'\\'+redemption_file_pathb+i+' '+ filedate +'.xlsb'
        print(finalpath)

        df =pd.read_excel(finalpath)
        fnldf = df.append(df)
        fnldf.to_excel("Redemption.xlsx")






#
#     #passing path to get all excel files
#     file_paths = glob.glob(finalpath + "\*.xlsb")
#     print(file_paths)
#     for x in file_paths:
#         df = pd.read_excel(x)
#         fnldf = df.append(df)
#
#
# fnldf.to_excel("test.xlsx")
#
# Bloom 20220524
#













