import logging
import pandas as pd
from sklearn.preprocessing import OneHotEncoder

def do_encoding(df_train_str:pd.DataFrame, df_test_str:pd.DataFrame):
    logging.info("##################################")
    logging.info("Start do_encoding")
    """
    범주형 데이터를 숫자 데이터로 변환 
    """
    enc = OneHotEncoder()
    # train
    tr_enc = pd.DataFrame(
        enc.fit_transform(df_train_str).toarray(),
        columns = enc.get_feature_names_out()
    )
    # test 
    te_enc = pd.DataFrame(
        enc.transform(df_test_str).toarray(),
        columns = enc.get_feature_names_out()
    )
    return tr_enc, te_enc
