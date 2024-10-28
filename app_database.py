import pandas as pd
import pickle
import streamlit as st
import matplotlib.pyplot as plt
import pyodbc

# Conexão com o banco de dados AzureDB
conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=cgenius-resources.database.windows.net;'
    'DATABASE=cgeniusdatabase;'
    'UID=cgeniusbanco;'
    'PWD=ftw1421@'
)

with open('model/modelo_recomendacao.pkl', 'rb') as file:
    modelo = pickle.load(file)

st.title('Elite Sales - Recomendações de Call Center')
cpf_cliente = st.text_input('Digite o CPF do Cliente')

if cpf_cliente:
    # Consulta SQL
    query = f"""
    SELECT * FROM Clientes
    LEFT JOIN Compras ON Clientes.Cliente_ID = Compras.Cliente_ID
    WHERE Clientes.CPF = '{cpf_cliente}' OR Clientes.CPF != '{cpf_cliente}'
    """
    df = pd.read_sql(query, conn)

    if not df.empty:
        # Comparativos
        total_compras_cliente = df[df['CPF'] == cpf_cliente]['Valor_Compra'].sum()
        total_compras_media = df['Valor_Compra'].mean()

        # Gráfico 1: Comparativo de Compras
        plt.figure(figsize=(10, 5))
        plt.bar(['Cliente', 'Média'], [total_compras_cliente, total_compras_media], color=['blue', 'orange'])
        plt.title('Comparativo de Compras do Cliente vs Média')
        plt.ylabel('Total de Compras (R$)')
        st.pyplot(plt)

        # Gráfico 2: Gastos Mensais por Cliente
        gastos_clientes = df.groupby('Nome')['Gastos_Mensais'].sum().reset_index()
        plt.figure(figsize=(10, 5))
        plt.bar(gastos_clientes['Nome'], gastos_clientes['Gastos_Mensais'], color='skyblue')
        plt.title('Gastos Mensais por Cliente')
        plt.xlabel('Cliente')
        plt.ylabel('Gastos Mensais (R$)')
        plt.xticks(rotation=45)
        st.pyplot(plt)

        # Gráfico 3: Total de Compras por Categoria
        compras_categoria = df.groupby('Categoria')['Valor_Compra'].sum().reset_index()
        plt.figure(figsize=(10, 5))
        plt.bar(compras_categoria['Categoria'], compras_categoria['Valor_Compra'], color='lightgreen')
        plt.title('Total de Compras por Categoria')
        plt.xlabel('Categoria')
        plt.ylabel('Valor Total das Compras (R$)')
        plt.xticks(rotation=45)
        st.pyplot(plt)

        # Gráfico 4: Distribuição de Gênero dos Clientes
        distribuicao_genero = df['Genero'].value_counts()
        plt.figure(figsize=(8, 8))
        plt.pie(distribuicao_genero, labels=distribuicao_genero.index, autopct='%1.1f%%', startangle=90, colors=['#ff9999','#66b3ff'])
        plt.title('Distribuição de Gênero dos Clientes')
        plt.axis('equal')
        st.pyplot(plt)

        # Gráfico 5: Total de Compras ao Longo do Tempo
        compras_tempo = df.groupby('Data_Compra')['Valor_Compra'].sum().reset_index()
        plt.figure(figsize=(10, 5))
        plt.plot(compras_tempo['Data_Compra'], compras_tempo['Valor_Compra'], marker='o', color='purple')
        plt.title('Total de Compras ao Longo do Tempo')
        plt.xlabel('Data da Compra')
        plt.ylabel('Valor Total das Compras (R$)')
        plt.xticks(rotation=45)
        st.pyplot(plt)

        # Gráfico 6: Comparativo de Compras entre Clientes
        compras_cliente = df.groupby('Nome')['Valor_Compra'].sum().reset_index()
        plt.figure(figsize=(10, 5))
        plt.bar(compras_cliente['Nome'], compras_cliente['Valor_Compra'], color='orange')
        plt.title('Comparativo de Total de Compras entre Clientes')
        plt.xlabel('Cliente')
        plt.ylabel('Total de Compras (R$)')
        plt.xticks(rotation=45)
        st.pyplot(plt)

        # Gráfico 7: Comparativo de Gastos Mensais entre Clientes
        gastos_mensais_cliente = df.groupby('Nome')['Gastos_Mensais'].sum().reset_index()
        plt.figure(figsize=(10, 5))
        plt.bar(gastos_mensais_cliente['Nome'], gastos_mensais_cliente['Gastos_Mensais'], color='red')
        plt.title('Comparativo de Gastos Mensais entre Clientes')
        plt.xlabel('Cliente')
        plt.ylabel('Gastos Mensais (R$)')
        plt.xticks(rotation=45)
        st.pyplot(plt)

    else:
        st.write('Nenhum dado encontrado para o CPF inserido.')

else:
    st.write('Cliente não encontrado. Verifique o CPF inserido.')

conn.close()
