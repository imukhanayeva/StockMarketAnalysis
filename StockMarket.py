!python3 -m pip install yahoo_fin
!python3 -m pip install matplotlib
!python3 -m pip install requests_html




import pandas as pd
import plotly
import plotly.offline as py
import matplotlib.pyplot as plt
plotly.offline.init_notebook_mode(connected=True)
import cufflinks as cf
%matplotlib inline
cf.set_config_file(offline=True)



from yahoo_fin import stock_info as si
stock_info.get_live_price('TSLA')



chart = cf.QuantFig(tesla['TSLA'])
chart.add_bollinger_bands() 
chart.add_macd()
chart.iplot()


how to save new file in github
