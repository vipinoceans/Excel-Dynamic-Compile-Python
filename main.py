import listclients as lc
import os
import glob


filepath = r"C:\Users\Shamm\Downloads\Client config.xlsx"

clientlist = []

clientlist = lc.listclient(filepath)


for i in clientlist:

    #Redemptions

    redemption_file_patha = r"C:\Users\Shamm\OneDrive\Desktop\Redemption Model File\Clients"
    redemption_file_pathb = "Redemptions"
    finalpath = os.path.join(redemption_file_patha,i,redemption_file_pathb)

    print(finalpath)













