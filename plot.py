import numpy as np
from matplotlib import pyplot as plt


def plot_curves(corrs_all, corrs_gene_set, save=None):
    """
    Plot correlations distribution
    :param corrs_all: list - correlations between all gene expression and class
    :param corrs_gene_set: list - correlations between gene subset expression and class
    :param save: str - save fig in 'save' location if provided
    :return:
    """
    # Plot CDF of all genes correlation distribution
    ca = len(corrs_all)
    plt.plot(np.sort(corrs_all), np.arange(ca) / ca, label='All available genes')

    # Plot CDF of subset genes correlation distribution
    cgs = len(corrs_gene_set)
    plt.plot(np.sort(corrs_gene_set), np.arange(cgs) / cgs, label='Subset of genes')

    plt.legend()
    plt.grid()
    plt.title('Distributions of all genes expression and set of genes correlations')

    # Save figure
    if save:
        plt.savefig(save)
    plt.show()