import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


df = pd.read_csv('graficos_exercicio_modulo_22\ecommerce_estatistica.csv')
df.dropna()


"""
0,Título,Nota,N_Avaliações,Desconto,Marca,Material,Gênero,Temporada,Review1,Review2,Review3,Qtd_Vendidos,
Preço,Nota_MinMax,N_Avaliações_MinMax,
Desconto_MinMax,Preço_MinMax,Marca_Cod,Material_Cod,Temporada_Cod,Qtd_Vendidos_Cod,Marca_Freq,Material_Freq
"""

# Gráfico de  Histograma
# Ver como estão distribuídas as avaliações dos produtos
plt.figure(figsize=(10, 6))
plt.hist(df['Nota'], bins=100, color='#5883a8', alpha=0.8)
plt.title('Histograma - Notas ')
plt.xlabel('Nota')
plt.ylabel('Frequência')
plt.grid(True)
plt.show()


# Gráfico de Dispersão
# Ajudar a entender se produtos com mais avaliações apresentam notas mais altas (ou vice-versa).
plt.scatter(df['Nota'], df['N_Avaliações'])
plt.title('Dispesão - Nota e Quantidade de Avaliações')
plt.xlabel('Nota')
plt.ylabel('Qtd. Avaliações')
plt.show()

# Mapa de Calor
# Poderá detectar padrões ou relações importantes que podem embasar decisões estratégicas.
corr = df[['Nota', 'N_Avaliações', 'Desconto', 'Qtd_Vendidos_Cod']].corr()
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Gráfico de Calor')
plt.show()

# Gráfico de barra
# Visualizar as 10 Marcas com mais frequência
df_marca = df['Marca'].value_counts().head(10)
plt.figure(figsize=(10, 6))
sns.barplot(x=df_marca.index, y=df_marca.values, palette='pastel')
plt.title('Gráfico de Barra - Frequência de Produtos por Marca')
plt.xlabel('Marcas')
plt.ylabel('Quantidade de Produtos')
plt.xticks(rotation=0)
plt.show()

# Gráfico de Pizza
# OS 5 Gêneros mas usados
x = df['Gênero'].value_counts().head(5).index
y = df['Gênero'].value_counts().head(5).values
plt.figure(figsize=(8, 6))
plt.pie(y, labels=x, autopct="%1.1f%%", startangle=90, colors=sns.color_palette('pastel'))
plt.title("Gráfico de Pizza")
plt.show()

# Gráfico de Densidade
# Útil para identificar a “forma” da distribuição – por exemplo, se os preços se concentram em determinada faixa
plt.figure(figsize=(8, 6))
sns.kdeplot(df['Preço'], shade=True, color="green")
plt.title("Gráfico de Densidade")
plt.xlabel("Valores")
plt.ylabel("Densidade")
plt.show()


# Gráfico de Regressão
# É ideal para visualizar a tendência linear (ou ajustar uma reta de regressão)
plt.figure(figsize=(8, 6))
sns.regplot(x=df['Preço'], y=df['Qtd_Vendidos_Cod'], data=df, scatter_kws={'color': 'blue'}, line_kws={'color': 'red'})
plt.title("Gráfico de Regressão")
plt.xlabel("Preço")
plt.ylabel("Quantidade Vendida")
plt.show()


# Gráfico de countplot com hue
sns.countplot(x=df['Preço'].head(10), hue=df['Qtd_Vendidos'].head(10), data=df, palette='pastel')
plt.xlabel('Preço')
plt.ylabel('Quantidade Vendidos')
plt.title('Gráfico de countplot com hue')
plt.show()