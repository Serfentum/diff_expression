import pandas as pd


def is_dataframe(researchable):
    return isinstance(researchable, pd.DataFrame)
