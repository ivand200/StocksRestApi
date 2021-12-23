from stocks.models import Stock, Index
import csv
import json
from .defs import Ep, Pe, Div_p, Ma10, Momentum_12_1, Avg_Momentum, Low_range, Momentum_12_2

def run():
    try:
        index_id = Index.objects.filter(name="SP500")[0]
    except:
        index_id = Index.objects.create(name="SP500")

    Stock.objects.filter(index=index_id).delete()

    with open('scripts/SP500.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader)

        for row in reader:
            print(row)
            index = Index.objects.filter(name="SP500")
            ticker = row[0]
            name = row[1]
            mom_12_2 = Momentum_12_2.get_momentum_12_2(row[0])
            avg_mom = Avg_Momentum.get_avg_momentum(row[0])
            ma10 = Ma10.get_ma10(row[0])
            e_p = Ep.get_ep(row[0])
            div_p = Div_p.get_div_p(row[0])


            s = Stock(ticker=ticker, name=name, momentum_12_2=mom_12_2,
                       momentum_avg=avg_mom, ma10=ma10, e_p=e_p, div_p=div_p, index=index[0])
            s.save()
