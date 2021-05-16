import pandas as pd
import plotly.express as px

tabela_clientes = pd.read_csv('telecom_users.csv')
tabela_clientes = tabela_clientes.drop(["Unnamed: 0"], axis=1)

display(tabela_clientes)

print(tabela_clientes.info()) 
tabela_clientes["TotalGasto"] = pd.to_numeric(tabela_clientes["TotalGasto"], errors="coerce")
tabela_clientes = tabela_clientes.dropna(how="all", axis=1)
tabela_clientes = tabela_clientes.dropna()

print(tabela_clientes.info())

display(tabela_clientes["Churn"].value_counts())
display(tabela_clientes["Churn"].value_counts(normalize=True).map('{:.1%}'.format))


# para edições nos gráficos: https://plotly.com/python/histograms/

for coluna in tabela_clientes:
    grafico = px.histogram(tabela_clientes, x=coluna, color="Churn")
    grafico.show()