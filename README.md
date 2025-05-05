# Análise Estatística e Visualização de Dados com Python

Este projeto utiliza as bibliotecas `matplotlib`, `seaborn` e `pandas` para analisar e visualizar dados de um dataset de e-commerce. Através de gráficos diversos, buscamos identificar padrões e relações que podem embasar decisões estratégicas.

## 📂 Dataset

O dataset `ecommerce_estatistica.csv` contém informações sobre produtos, incluindo:
- **Nota:** Avaliação dos produtos.
- **N_Avaliações:** Número de avaliações recebidas.
- **Desconto:** Percentual de desconto aplicado.
- **Marca:** Nome da marca do produto.
- **Material:** Tipo de material.
- **Gênero:** Categoria de gênero dos produtos.
- **Temporada:** Estação/época do ano relacionada ao produto.
- **Qtd_Vendidos:** Quantidade de vendas registradas.
- **Preço:** Valor do produto.

## 📊 Gráficos Gerados

### 1️⃣ Histograma
Visualiza a distribuição das avaliações dos produtos.

### 2️⃣ Gráfico de Dispersão
Exibe a relação entre a nota e o número de avaliações recebidas.

### 3️⃣ Mapa de Calor
Mostra a correlação entre variáveis numéricas para identificar padrões.

### 4️⃣ Gráfico de Barra
Destaca as 10 marcas com mais frequência no dataset.

### 5️⃣ Gráfico de Pizza
Exibe os 5 gêneros mais comuns nos produtos.

### 6️⃣ Gráfico de Densidade
Revela a distribuição dos preços dos produtos.

### 7️⃣ Gráfico de Regressão
Modela a tendência de vendas com relação ao preço do produto.

### 8️⃣ Countplot com Hue
Visualiza a relação entre preço e quantidade vendida.

## 🚀 Como Executar
1. Certifique-se de ter Python instalado.
2. Instale as bibliotecas necessárias:
   ```bash
   pip install matplotlib seaborn pandas
