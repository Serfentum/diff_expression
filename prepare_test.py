import pandas as pd


# Script for creating awesomely formatted sample dataset

path_to_genes = 'data/genes_set.txt'
path_to_expression = 'data/Gender_collapsed_symbols.gct'


expression = pd.read_csv(path_to_expression, sep='\t', skiprows=2)

# Cause row should correspond to observation and description is empty
expression = expression.T.drop('DESCRIPTION', axis=0)
# Create new column with phenotype description
expression.loc[:, 'Description'] = ['Description'] + [0 for i in range(15)] + [1 for i in range(17)]

#
# print(expression.columns)
# print(expression.index)


# Write proper dataframe to csv
expression.to_csv('data/sample_expr', header=False, index=False)