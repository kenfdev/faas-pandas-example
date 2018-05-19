import pandas as pd
import numpy as np

def handle(req):
    """handle a request to the function
    Args:
        req (str): request body
    """

    dates = pd.date_range('20130101', periods=6)
    df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))

    return df.to_json()
