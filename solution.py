import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 423200009 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 1 - p
    loc = x.mean()
    sc  = np.sqrt(np.var(x))/np.sqrt(len(x))

    return 2*(loc-0.032) + np.sqrt(np.var(2*(x-0.032))) * norm.ppf(alpha / 2) / np.sqrt(len(x)), \
           2*(loc-0.032) + np.sqrt(np.var(2*(x-0.032))) * norm.ppf(1 - alpha / 2) / np.sqrt(len(x))
