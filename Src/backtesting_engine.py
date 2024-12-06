from dataclasses import dataclass
import pandas as pd
import backtrader as bt
import numpy as np

@dataclass
class First_Strategy(bt.Strategy):
    captial: float

    def bt_one():
        raise NotImplementedError
