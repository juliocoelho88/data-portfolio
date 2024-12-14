import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Carregar o Dataset
data_path = "C:/Users/55119/PycharmProjects/data-portfolio/01_data_analysis/data/eccomerce_sales.csv"
df = pd.read_csv(data_path)

print("Visualizando od dados")
print(df.head())

print("\nEstatistica descritiva")
print(df.describe())

print("\nVerificar valores nulos")
print(df.isnull().sum())

sns.histplot(df['column_name'], kde=True) #Substitua o 'column_name' pela coluna que deseja.
plt.title('Distribuição de Valores - Exemplo')
plt.show()

