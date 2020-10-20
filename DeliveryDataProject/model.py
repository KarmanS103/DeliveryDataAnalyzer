import pandas as pd
import numpy as np
import glob

uber_report_types = ["Payment Details"]


# , "Order Errors(Menu Item)", "Order Errors(Transaction)",
#                  "Order History", "Downtime", "Customer and Delivery Feedback",
#                  "Menu Item Feedback"]
# TODO: Add remaining reports


def ubereats_importer():
    list_of_dfs = []
    for report in uber_report_types:
        list_of_dfs.append(folder_importer(report))

    return list_of_dfs


# Given a folder name, reads all of the reports in that folder and creates a single dataframe
# from them
# TODO: Remove Duplicates
def folder_importer(folder_name):
    dfs = []
    for name in glob.glob(folder_name + "/*.csv"):
        dfs.append(pd.read_csv(name))
    returndf = pd.concat(dfs)
    return returndf


if __name__ == "__main__":
    uber_eats_reports = ubereats_importer()
    print(uber_eats_reports[0])
