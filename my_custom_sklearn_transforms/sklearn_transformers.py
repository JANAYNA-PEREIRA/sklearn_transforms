from sklearn.base import BaseEstimator, TransformerMixin


# All sklearn Transforms must have the `transform` and `fit` methods
class DropColumns(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.columns = columns

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        # Primeiro realizamos a cópia do dataframe 'X' de entrada
        data = X.copy()
        # Retornamos um novo dataframe sem as colunas indesejadas
        return data.drop(labels=self.columns, axis='columns')
    
    rm_columns = DropColumns(
    columns = ['NOME','INGLES']
)

print(rm_columns)

print("Colunas do dataset original: \n")
print(df_data_1.columns)

rm_columns.fit(X=df_data_1)

# Reconstruindo um DataFrame Pandas com o resultado da transformação
df_data_2 = pd.DataFrame.from_records(
    data=rm_columns.transform(
        X=df_data_1   
    ),
)
print("Colunas do dataset após a transformação ``DropColumns``: \n")
print(df_data_2.columns)



df_data_1 = df_data_1.query("NOTA_DE >=0.0 and NOTA_DE <=10.0")
df_data_1 = df_data_1.query("NOTA_EM >=0.0 and NOTA_EM <=10.0")
df_data_1 = df_data_1.query("NOTA_MF >=0.0 and NOTA_MF <=10.0")
df_data_1 = df_data_1.query("NOTA_GO >=0.0 and NOTA_GO <=10.0")





