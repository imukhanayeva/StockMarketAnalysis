!python pip install pandas-datareader

import os
import pandas as pd
import datetime
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np
import pandas_datareader.data as web
%matplotlib inline




hisstorical_data = web.DataReader("TSLA", "av-daily", start=datetime(2020, 11, 23), end=datetime(2020, 12, 23), api_key=os.getenv('ALPHAVANTAGE_API_KEY'))

hisstorical_data.iloc["2020-11-30"]


quote=web.get_quote_av(["TSLA"])


