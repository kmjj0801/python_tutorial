import os
import numpy as np
import random

def reset_seeds(func, seed=42):
  random.seed(seed)
  os.environ['PYTHONHASHSEED'] = str(seed)    # 파이썬 환경변수 시드 고정
  np.random.seed(seed)

  def wrapper(*args, **kwargs):
    return func(*args, **kwargs)
  
  return wrapper



