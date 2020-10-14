import pandas as pd
import numpy as np


class DoorDashImporter:
    def begin_import(self):
        filepath = input("What is the file path for your DoorDash Report? ")
        doordash_df = pd.read_csv(filepath)
        print(doordash_df.head(5))


if __name__ == "__main__":
    d1 = DoorDashImporter()
    d1.begin_import()
