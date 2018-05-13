import numpy as np
import GEOparse


def geo_load(gse='GSE1563'):
    """
    Obtain data from GEO database
    :param gse: str - dataset id from GEO
    :return: Dataframe - expression data
    """
    # Load geo data
    data = GEOparse.get_GEO(geo=gse)

    # Extract expression data and transpose it to common form
    expression = data.pivot_samples('VALUE').T

    # Infer class from metadata description (assumes that 'control' in description denotes control phenotype
    description = data.phenotype_data.description
    expression.loc[:, 'Description'] = np.where(description.str.contains('control', case=False), 1, 0)

    return expression








# supply geo id - field
# supply file with genes - field
# supply p-value=0.05 cutoff - field
# ok - field
###
# load gse, get expression df .
# load genes file .
# analyze .
# display results

