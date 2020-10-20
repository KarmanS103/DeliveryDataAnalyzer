import pandas as pd
import numpy as np


# Get file path for folder instead and read in all of the files from the folder
class DoorDashImporter:
    def begin_import(self):
        doordash_df = pd.read_csv("Payment Details/testdata.csv")
        print(doordash_df.head(5))


if __name__ == "__main__":
    d1 = DoorDashImporter()
    d1.begin_import()
