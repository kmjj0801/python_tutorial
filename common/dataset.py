import pandas as pd

def load_dataset(path:str, target_col=None) -> pd.DataFrame:
    # 타이타닉 데이터셋 로드하는 코드 작성
    df_features = pd.read_csv(path)
    df_targets = pd.DataFrame()

    if target_col:
        df_targets = df_features[target_col]
        df_features = df_features.drop([target_col], axis=1)

    return df_features, df_targets

