from indexes.models import Etf
import json
from scripts.test import Momentum_12_1, Avg_Momentum, Ma10, Momentum_3

etf_list = ["LQD", "HYG", "SHV", "SPY", "DJI", "IAU"]

def run():
    Etf.objects.all().delete()

    for ticker in etf_list:
        print(ticker)
        ticker = ticker
        mom_12_1 = Momentum_12_1.get_momentum_12_1(ticker)
        mom_avg = Avg_Momentum.get_avg_momentum(ticker)
        mom_3 = Momentum_3.get_momentum_3(ticker)
        ma_10 = Ma10.get_ma10(ticker)

        e = Etf(ticker=ticker, momentum_12_1=mom_12_1, momentum_avg=mom_avg, ma10=ma_10,
                momentum_3=mom_3)
        e.save()
