import pandas as pd
import numpy as np
import glob


# Get file path for folder instead and read in all of the files from the folder
def ubereats_importer():
    payment_details_df = payment_details_importer()


def payment_details_importer():
    list_of_df = []

    for name in glob.glob("Payment Details/*.csv"):
        list_of_df.append(pd.read_csv(name))

    payment_details_df = pd.concat(list_of_df)


if __name__ == "__main__":
    ubereats_importer()
