import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 423200009# Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 1 - p
    sc  = np.sqrt(np.var(x))/np.sqrt(len(x))

    return x.mean() - sc * norm.ppf(1 - alpha / 2), \
           x.mean() - sc * norm.ppf(alpha / 2)
