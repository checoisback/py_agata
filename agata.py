from time_in_ranges import *
from risk import *


class Agata:
    """
    Core class of AGATA.

    ...
    Attributes
    ----------
    data: pd.DataFrame
        Pandas dataframe with a column `glucose` containing the glucose data
        to analyze (in mg/dl).
    glycemic_target: str
        A string defining the set of glycemic targets to use.

    Methods
    -------
    analyze_glucose_profile():
        Runs ReplayBG.
    """

    def __init__(self, data, glycemic_target='diabetes'):

        self.data = data #TODO: validate data
        self.glycemic_target = glycemic_target

    def analyze_glucose_profile(self):
        """
        Analyzes a single glucose profile.

        Parameters
        ----------
        None

        Returns
        -------
        results: dict
            A dictionary containing the results of the analysis i.e.:
            - time_in_ranges: dict
                A dictionary containing the values of the time in range related metrics.
            - risk: dict
                A dictionary containing the values of the risk related metrics.

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
        results = dict()

        # Get time metrics
        results['time_in_ranges'] = dict()
        results['time_in_ranges']['time_in_target'] = time_in_target(self.data, self.glycemic_target)
        results['time_in_ranges']['time_in_tight_target'] = time_in_tight_target(self.data, self.glycemic_target)
        results['time_in_ranges']['time_in_hypoglycemia'] = time_in_hypoglycemia(self.data, self.glycemic_target)
        results['time_in_ranges']['time_in_l1_hypoglycemia'] = time_in_l1_hypoglycemia(self.data, self.glycemic_target)
        results['time_in_ranges']['time_in_l2_hypoglycemia'] = time_in_l2_hypoglycemia(self.data, self.glycemic_target)
        results['time_in_ranges']['time_in_hyperglycemia'] = time_in_hyperglycemia(self.data, self.glycemic_target)
        results['time_in_ranges']['time_in_l1_hyperglycemia'] = time_in_l1_hyperglycemia(self.data, self.glycemic_target)
        results['time_in_ranges']['time_in_l2_hyperglycemia'] = time_in_l2_hyperglycemia(self.data, self.glycemic_target)

        # Get risk metrics
        results['risk'] = dict()
        results['risk']['adrr'] = adrr(self.data)
        results['risk']['lbgi'] = lbgi(self.data)
        results['risk']['hbgi'] = hbgi(self.data)
        results['risk']['bgri'] = bgri(self.data)
        results['risk']['gri'] = gri(self.data)

        # Return results
        return results
