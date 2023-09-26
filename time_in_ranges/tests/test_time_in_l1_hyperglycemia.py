import pandas as pd
import numpy as np
import datetime
from datetime import datetime, timedelta

from time_in_ranges import time_in_l1_hyperglycemia


def test_time_in_l1_hyperglycemia():
    """
    Unit test of time_in_l1_hyperglycemia function.

    Parameters
    ----------
    None

    Returns
    -------
    None

    Raises
    ------
    None

    See Also
    --------
    None

    Examples
    --------
    None

    References
    ----------
    None
    """
    # Set test data
    t = np.arange(datetime(2000, 1, 1, 0, 0, 0), datetime(2000, 1, 1, 0, 55, 0), timedelta(minutes=5)).astype(
        datetime)
    glucose = np.zeros(shape=(t.shape[0],))
    glucose[0] = 40
    glucose[1:3] = [60, 60]
    glucose[3] = 80
    glucose[4:6] = [120, 150]
    glucose[6:8] = [200, 200]
    glucose[8:10] = [260, 260]
    glucose[10] = np.nan
    d = {'t': t, 'glucose': glucose}
    data = pd.DataFrame(data=d)

    #Tests
    assert np.isnan(time_in_l1_hyperglycemia(data,'diabetes')) == False
    assert time_in_l1_hyperglycemia(data, 'diabetes') == 20

    assert np.isnan(time_in_l1_hyperglycemia(data, 'pregnancy')) == False
    assert time_in_l1_hyperglycemia(data, 'pregnancy') == 30

    try:
        time_in_l1_hyperglycemia(data,'other')
    except RuntimeError:
        assert True