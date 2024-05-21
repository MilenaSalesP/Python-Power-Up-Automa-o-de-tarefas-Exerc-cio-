import pandas as pd
import matplotlib.pyplot as plt
# Passo 1: Leitura do Arquivo CSV
df = pd.read_csv('dados_vendas.csv')

# Passo 2: Análise Exploratória de Dados
# Mostrando as primeiras 5 linhas do DataFrame
print("Primeiras 5 linhas do DataFrame:")
print(df.head())

# Informações gerais sobre o DataFrame
print("\nInformações gerais do DataFrame:")
print(df.info())

# Calculando o total de vendas para cada linha
df['Total_Vendas'] = df['Quantidade'] * df['Preco_Unitario']

# Exibindo estatísticas descritivas das colunas numéricas
print("\nEstatísticas descritivas:")
print(df.describe())

# Passo 3: Agrupamento e Agregação
# Calculando o total de vendas por produto
total_vendas_produto = df.groupby('Produto')['Total_Vendas'].sum().reset_index()
print("\nTotal de vendas por produto:")
print(total_vendas_produto)

# Calculando a quantidade total vendida por produto
quantidade_total_produto = df.groupby('Produto')['Quantidade'].sum().reset_index()
print("\nQuantidade total vendida por produto:")
print(quantidade_total_produto)

# Passo 4: Visualização de Dados
# Gráfico de barras do total de vendas por produto
plt.figure(figsize=(10, 5))
plt.bar(total_vendas_produto['Produto'], total_vendas_produto['Total_Vendas'], color='skyblue')
plt.xlabel('Produto')
plt.ylabel('Total de Vendas')
plt.title('Total de Vendas por Produto')
plt.show()

# Gráfico de linha da evolução das vendas totais ao longo do tempo
df['Data'] = pd.to_datetime(df['Data'])
vendas_por_dia = df.groupby('Data')['Total_Vendas'].sum().reset_index()
plt.figure(figsize=(10, 5))
plt.plot(vendas_por_dia['Data'], vendas_por_dia['Total_Vendas'], marker='o', linestyle='-')
plt.xlabel('Data')
plt.ylabel('Total de Vendas')
plt.title('Evolução das Vendas Totais ao Longo do Tempo')
plt.show()

# Passo 5: Insights Adicionais
# Dia com o maior valor de vendas totais
dia_maior_venda = vendas_por_dia[vendas_por_dia['Total_Vendas'] == vendas_por_dia['Total_Vendas'].max()]
print("\nDia com o maior valor de vendas totais:")
print(dia_maior_venda)

# Produto mais vendido em termos de quantidade
produto_mais_vendido = quantidade_total_produto[quantidade_total_produto['Quantidade'] == quantidade_total_produto['Quantidade'].max()]
print("\nProduto mais vendido em termos de quantidade:")
print(produto_mais_vendido)
