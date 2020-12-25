!python3 -m pip install pip --upgrade
!python3 -m pip install pandas --upgrade
!python3 -m pip install pandas-datareader


import os
from datetime import datetime
import pandas_datareader.data as web


historical_time_series_data = web.DataReader("TSLA", "av-daily", start=datetime(2020,11, 23), end=datetime(2020, 12, 23),
api_key='OG5JH42JVFCIUNS8')

historical_time_series_data.loc["2020-11-30"]

web.get_quote_av(["TSLA"])

####ImmediateDeprecationError: 
AVQuotesReader has been immediately deprecated due to large breaks in the API without the
introduction of a stable replacement. Pull Requests to re-enable these data
connectors are welcome.



