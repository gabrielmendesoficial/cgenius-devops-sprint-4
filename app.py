import pandas as pd
import pyodbc
from flask import Flask, jsonify, request
import matplotlib.pyplot as plt
import io
import base64

# Inicializando o Flask
app = Flask(__name__)

# Função para conectar ao banco de dados
def get_connection():
    return pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=cgenius-resources.database.windows.net;'
        'DATABASE=cgeniusdatabase;'
        'UID=cgeniusbanco;'
        'PWD=ftw1421@'
    )

# Endpoint para criar um novo cliente
@app.route('/clientes', methods=['POST'])
def create_client():
    data = request.json
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO Clientes (Nome, CPF, Genero) VALUES (?, ?, ?)",
        (data['Nome'], data['CPF'], data['Genero'])
    )
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "Cliente criado com sucesso!"}), 201

# Endpoint para ler todos os clientes
@app.route('/clientes', methods=['GET'])
def read_clients():
    conn = get_connection()
    query = "SELECT * FROM Clientes"
    df = pd.read_sql(query, conn)
    conn.close()
    return jsonify(df.to_dict(orient='records'))

# Endpoint para ler um cliente pelo CPF
@app.route('/clientes/<string:cpf_cliente>', methods=['GET'])
def read_client_data(cpf_cliente):
    conn = get_connection()
    query = f"""
    SELECT * FROM Clientes
    LEFT JOIN Compras ON Clientes.Cliente_ID = Compras.Cliente_ID
    WHERE Clientes.CPF = '{cpf_cliente}' OR Clientes.CPF != '{cpf_cliente}'
    """
    df = pd.read_sql(query, conn)

    if df.empty:
        return jsonify({"message": "Nenhum dado encontrado para o CPF inserido."}), 404

    total_compras_cliente = df[df['CPF'] == cpf_cliente]['Valor_Compra'].sum()
    total_compras_media = df['Valor_Compra'].mean()

    # Gráfico: Comparativo de Compras
    fig1 = plt.figure(figsize=(10, 5))
    plt.bar(['Cliente', 'Média'], [total_compras_cliente, total_compras_media], color=['blue', 'orange'])
    plt.title('Comparativo de Compras do Cliente vs Média')
    plt.ylabel('Total de Compras (R$)')
    plt.tight_layout()
    
    buf1 = io.BytesIO()
    plt.savefig(buf1, format='png')
    buf1.seek(0)
    plt.close(fig1)
    
    img1 = base64.b64encode(buf1.getvalue()).decode()

    return jsonify({
        "total_compras_cliente": total_compras_cliente,
        "total_compras_media": total_compras_media,
        "grafico_comparativo": img1
    })

# Endpoint para atualizar um cliente
@app.route('/clientes/<string:cpf_cliente>', methods=['PUT'])
def update_client(cpf_cliente):
    data = request.json
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE Clientes SET Nome = ?, Genero = ? WHERE CPF = ?",
        (data['Nome'], data['Genero'], cpf_cliente)
    )
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "Cliente atualizado com sucesso!"})

# Endpoint para deletar um cliente
@app.route('/clientes/<string:cpf_cliente>', methods=['DELETE'])
def delete_client(cpf_cliente):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "DELETE FROM Clientes WHERE CPF = ?",
        (cpf_cliente,)
    )
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "Cliente deletado com sucesso!"})

# Rodar a aplicação com: flask run
if __name__ == '__main__':
    app.run(debug=True)
