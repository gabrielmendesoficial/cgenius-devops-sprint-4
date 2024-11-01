from flask import Flask, jsonify, request, make_response
from flask_restful import Api, Resource
import pyodbc
import pandas as pd

app = Flask(__name__)
api = Api(app)

# Conexão com o banco de dados AzureDB
conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=cgenius-resources.database.windows.net;'
    'DATABASE=cgeniusdatabase;'
    'UID=cgeniusbanco;'
    'PWD=ftw1421@'
)

class Cliente(Resource):
    def get(self, cpf):
        query = f"""
            SELECT * FROM Clientes
            LEFT JOIN Compras ON Clientes.Cliente_ID = Compras.Cliente_ID
            WHERE Clientes.CPF = '{cpf}'
        """
        df = pd.read_sql(query, conn)
        
        if df.empty:
            return make_response(jsonify({'message': 'Cliente não encontrado'}), 404)
        
        cliente_data = df.to_dict(orient='records')
        return jsonify(cliente_data)
    
    def post(self):
        data = request.json
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO Clientes (CPF, Nome, Genero)
            VALUES (?, ?, ?)
        """, data['CPF'], data['Nome'], data['Genero'])
        conn.commit()
        return make_response(jsonify({'message': 'Cliente criado com sucesso'}), 201)

    def put(self, cpf):
        data = request.json
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE Clientes
            SET Nome = ?, Genero = ?
            WHERE CPF = ?
        """, data['Nome'], data['Genero'], cpf)
        conn.commit()
        return make_response(jsonify({'message': 'Cliente atualizado com sucesso'}), 200)

    def delete(self, cpf):
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Clientes WHERE CPF = ?", cpf)
        conn.commit()
        return make_response(jsonify({'message': 'Cliente deletado com sucesso'}), 204)

# Recursos adicionais para Compras, Gastos Mensais e Comparativos
class Compras(Resource):
    def get(self):
        query = "SELECT Categoria, SUM(Valor_Compra) as Total_Valor FROM Compras GROUP BY Categoria"
        df = pd.read_sql(query, conn)
        compras_data = df.to_dict(orient='records')
        return jsonify(compras_data)

class GastosMensais(Resource):
    def get(self):
        query = "SELECT Nome, SUM(Gastos_Mensais) as Total_Gastos FROM Clientes GROUP BY Nome"
        df = pd.read_sql(query, conn)
        gastos_data = df.to_dict(orient='records')
        return jsonify(gastos_data)

class GeneroDistribuicao(Resource):
    def get(self):
        query = "SELECT Genero, COUNT(*) as Quantidade FROM Clientes GROUP BY Genero"
        df = pd.read_sql(query, conn)
        genero_data = df.to_dict(orient='records')
        return jsonify(genero_data)

# Rota CRUD para o Cliente
api.add_resource(Cliente, '/cliente', '/cliente/<string:cpf>')

# Rotas para gráficos e comparativos
api.add_resource(Compras, '/compras')
api.add_resource(GastosMensais, '/gastos-mensais')
api.add_resource(GeneroDistribuicao, '/genero-distribuicao')

if __name__ == '__main__':
    app.run(debug=True)
