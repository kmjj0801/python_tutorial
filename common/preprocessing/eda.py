import logging
import pandas as pd

def do_eda(df_train:pd.DataFrame):
  logging.info("##################################")
  logging.info("Start do_eda")
  print(f"df_train.shape: {df_train.shape}")
  print(f"df_train의 결측치: {df_train.isnull().sum().sum()}")

