import pandas as pd
import pyarrow.parquet as pa


def read_train(location):
    return pa.read_table(location)

def read_test(location):
    return pa.read_table(location)

def read_meta_train(metadataLocation):
    return pd.read_csv(metadataLocation)

def read_meta_test(metadataLocation):
    return pd.read_csv(metadataLocation)

metadataLocationTrain = r"Data/metadata_train.csv"
metadataLocationTest = r"Data/metadata_test.csv"


trainData = r"Data/train.parquet"
signalData = read_train(trainData)