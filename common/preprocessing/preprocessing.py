import pandas as pd
from sklearn.model_selection import train_test_split

from .cleaning import do_cleaning
from .encoding import do_encoding

def __do_encoding(df_train, df_test, enc_cols):
    normal_cols = list(set(df_train.columns) - set(enc_cols))
    tr_enc, te_enc = do_encoding(df_train[enc_cols], df_test[enc_cols])

    train = pd.concat(
        [df_train[normal_cols].reset_index(drop=True), tr_enc.reset_index(drop=True)]
        , axis=1
    )
    test = pd.concat(
        [df_test[normal_cols].reset_index(drop=True), te_enc.reset_index(drop=True)]
        , axis=1
    ) 
    return train, test

def do_preprocessing(df_train:pd.DataFrame, df_train_target
                    , df_test:pd.DataFrame, 
                    enc_cols:list = ['gender', 'embarked']):
    # 1. cleaning
    do_cleaning(df_train, df_test)

    # 2. encoding
    train, test = __do_encoding(df_train, df_test, enc_cols)

    # 3. scaling 

    # 4. split
    tr_x, te_x, tr_y, te_y = train_test_split(
        train, df_train_target, stratify=df_train_target,
        shuffle=True, test_size=0.2
    )

    return tr_x, te_x, tr_y, te_y, test

