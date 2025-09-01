import logging
import pandas as pd 

def __drop_duplicate(*args):
    for df in args: # args = [df_train, df_test]
        df.drop_duplicates(inplace=True)

def __drop_cols(*args, drop_cols):
    for df in args: # args = [df_train, df_test]
        df.drop(drop_cols, axis=1, inplace=True)

def __fillna(df_train:pd.DataFrame, df_test:pd.DataFrame, fill_cols:list):
    for col in fill_cols: # fill_cols=['age', 'embarked']
        try: 
            # 수치형 데이터 처리 
            _value = df_train[col].median()
        except: 
            # 범주형 데이터 처리 
            _value = df_train[col].mode().values[0]
        finally: 
            # 결측치 채우기 
            df_train[col].fillna(_value, inplace=True)
            df_test[col].fillna(_value, inplace=True) 
        

def do_cleaning(df_train:pd.DataFrame, df_test:pd.DataFrame
                , drop_cols:list = ['name', 'ticket', 'cabin', 'passengerid'],
                fill_cols:list = ['age', 'fare', 'embarked']):
    logging.info("##################################")
    logging.info("Start do_cleaning")
    # 1. row 기준으로 중복된 데이터 제거 
    __drop_duplicate(df_train, df_test)

    # 2. 필요없는 컬럼 제거 
    __drop_cols(df_train, df_test, drop_cols=drop_cols)

    # 3. 결측치에 적용할 데이터 추출 from train 
    # 결측치에 추출한 데이터 적용 
    __fillna(df_train, df_test, fill_cols)

    assert df_train.isnull().sum().sum() == 0, '학습용 데이터에 결측치가 있습니다.'
    assert df_test.isnull().sum().sum() == 0, '평가용 데이터에 결측치가 있습니다.'
