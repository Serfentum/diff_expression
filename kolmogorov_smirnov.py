import pandas as pd
from scipy.stats.stats import ks_2samp
from scipy.stats import pearsonr

from auxilliary import is_dataframe
from plot import plot_curves


def different_expression(expression='data/sample_expr',
                         path_to_genes='data/genes_set.txt',
                         cutoff=0.05,
                         save=None):
    """
    Determine whether specified genes differ in expression between 2 classes. Use Kolmogorov-Smirnov criterion.
    NOTE: takes a dataframe where genes are columns and observations are rows
    :param expression: str - path to expression data in csv
    :param path_to_genes: str - path to subset of genes where each gene occupy 1 row
    :param cutoff: float - p-value threshold
    :param save: str - save fig in 'save' location if provided
    :return: boolean - whether expression of genes is altered
    """
    # Load data
    if not is_dataframe(expression):
        expression = pd.read_csv(expression)
    with open(path_to_genes, 'r') as source:
        genes = [gene.strip() for gene in source.readlines()]

    # Prepare df for subset of genes
    expression_subset = expression.loc[:, expression.columns.isin(genes)]
    expression_subset.loc[:, 'Description'] = expression.loc[:, 'Description']

    # Correlations between class (phenotype) and expression of each gene
    # and correlations between class and genes from subset
    corrs_all = [pearsonr(expression.loc[:, gene], expression.loc[:, 'Description'])[0] for gene in expression]
    corrs_gene_set = [pearsonr(expression.loc[:, gene], expression.loc[:, 'Description'])[0] for gene in expression_subset]

    # Plot functions
    plot_curves(corrs_all, corrs_gene_set, save)
    # Compute p-value
    p_value = ks_2samp(corrs_gene_set, corrs_all)[1]

    return p_value <= cutoff

