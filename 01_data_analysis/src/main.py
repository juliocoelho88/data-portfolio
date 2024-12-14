import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Carregar o Dataset
data_path = "C:/Users/55119/PycharmProjects/data-portfolio/01_data_analysis/data/eccomerce_sales.csv"

print("Carregando o dataset")
df = pd.read_csv(data_path)

print("\nInformacoes gerais")
print(df.info())

print("\nVisualizando od dados")
print(df.head())

print("\nEstatistica descritiva")
print(df.describe())

print("\nVerificar valores nulos")
print(df.isnull().sum())

plt.figure(figsize=(10,6))
sns.histplot(df['Price'], kde=True, bins=30) #Substitua o 'column_name' pela coluna que deseja.
plt.title('Distribuição da Coluna Price')
plt.xlabel("Valores")
plt.ylabel("Frequencia")
plt.show()

# 2. Gráfico de barras para uma variável categórica
plt.figure(figsize=(10, 6))
df['High'].value_counts().plot(kind='bar')  # Substitua 'column_category' por uma coluna categórica válida
plt.title('Frequência por Categoria')
plt.xlabel('Categorias')
plt.ylabel('Frequência')
plt.show()

