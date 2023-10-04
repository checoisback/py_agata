import pandas as pd
import numpy as np
import datetime
from datetime import datetime, timedelta
import os
from py_agata.variability import modd


def test_modd():
    """
    Unit test of modd function.

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
    start_time = datetime(2000, 1, 1, 0, 10, 0)
    end_time = datetime(2000, 1, 1, 0, 0, 0) + timedelta(minutes=4000)
    time_interval = timedelta(minutes=5)
    time_range = pd.date_range(start_time, end_time, freq=time_interval)

    # Set a random seed for reproducibility
    np.random.seed(1)

    # Generate random glucose data
    glucose = np.random.randn(len(time_range)) * 70 + 140

    # Create a DataFrame
    d = {'t': time_range, 'glucose': glucose}
    data = pd.DataFrame(data=d)

    #Tests
    assert np.isnan(modd(data)) == False
    assert np.round(modd(data) * 1000) / 1000 == 82.866

    # Set empty data
    t = np.arange(datetime(2000, 1, 1, 1, 0, 0), datetime(2000, 1, 1, 1, 55, 0), timedelta(minutes=5)).astype(
        datetime)
    glucose = np.zeros(shape=(t.shape[0],))
    glucose[0] = np.nan
    glucose[1:3] = [np.nan, np.nan]
    glucose[3] = np.nan
    glucose[4:6] = [np.nan, np.nan]
    glucose[6:8] = [np.nan, np.nan]
    glucose[8:10] = [np.nan, np.nan]
    glucose[10] = np.nan
    d = {'t': t, 'glucose': glucose}
    data = pd.DataFrame(data=d)

    # Tests
    assert np.isnan(modd(data))