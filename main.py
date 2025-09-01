import warnings
warnings.filterwarnings('ignore')

import logging
logging.basicConfig(level=logging.INFO)

import pandas as pd 

from common.dataset import load_dataset
from common.preprocessing.eda import do_eda
from common.preprocessing.preprocessing import do_preprocessing
from common.modeling.model import get_model
from common.modeling.training import do_training
from common.utils import reset_seeds

@reset_seeds
def modeling():
    logging.info("##################################")
    logging.info("Start Load Dataset")
    # 1. train dataset, test dataset 
    df_train, df_train_target = load_dataset("./data/train.csv", target_col="survived")
    df_test, _ = load_dataset("./data/test.csv")
    
    # 2. eda
    do_eda(df_train=df_train)
    
    # 3. data preprocessing
    tr_x, te_x, tr_y, te_y, test = do_preprocessing(df_train, df_train_target, df_test)

    # 4. model
    model = do_training(get_model(), tr_x, tr_y, te_x, te_y)

    # 5. prediction


    # 6. submission



if __name__ == "__main__":
    modeling()

