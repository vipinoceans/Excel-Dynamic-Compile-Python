import pandas as pd
import getpass
import listclients as lc

current_user = getpass.getuser()

#getting client list
filepath = r"C:\Users\Shamm\Downloads\Client config.xlsx"
# reading clients to the list (clientlist)
clientlist = lc.listclient(filepath)
#clientlist = []


filedate  = input('Enter file run date in format yyyymmdd \n')
if len(filedate)  != 8:
    print('Invalid file date')
    exit()




#for redemptions
appended_data = []

#for transactions
appended_data2 = []

for client in clientlist:

    # 'C:\Users\Bharathy\Cache Investment Management Pty Ltd\Fund operations - Documents\Operations\Client\Bloom\Redemptions'
    #config_path = rf"C:\Users\{current_user}\Cache Investment Management Pty Ltd\Fund operations - Documents\Operations\Client\\{i}\Redemptions\Funded Redemptions - {i} {filedate}.xlsb"
    # config_path = rf"C:\Users\{current_user}\Cache Investment Management Pty Ltd\Fund operations - Documents\Operations\Client\\{i}\Redemptions\Funded Redemptions - {i} {filedate}.xlsb"
    config_path = rf'C:\Users\Shamm\OneDrive\Desktop\Redemption Model File\Clients\{client}\Redemptions\Funded Redemptions - {client} {filedate}.xlsb'

    #
    #print(config_path)
    try:
        df = pd.read_excel(config_path)
        #fnldf = df.append(df)
        appended_data.append(df)

    except FileNotFoundError:
        print(f" Redemption File  not found for client {client}.")


    config_path2 = rf'C:\Users\{current_user}\OneDrive\Desktop\Redemption Model File\Clients\{client}\Registry\Transaction Enquiry BOD - {client} {filedate}.csv'


    #
    #print(config_path)
    try:
        df = pd.read_csv(config_path2)
        #fnldf = df.append(df)
        appended_data2.append(df)

    except FileNotFoundError:
        print(f" Transaction File  not found for client {client}.")


try:
    appended_data = pd.concat(appended_data)
    appended_data2 = pd.concat(appended_data2)

    try:
        with pd.ExcelWriter('Reconcile.xlsx') as writer:
            appended_data.to_excel(writer, sheet_name='Redemptions')
            appended_data2.to_excel(writer, sheet_name='Transactions')
    except PermissionError:
        print(f"Unable to write to File Reconcile.xlsx , Permission error - file is either open or inaccessible ")

except ValueError:
    print(f"No data to append")



