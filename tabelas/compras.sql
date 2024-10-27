CREATE OR REPLACE TABLE Compras (
    Compra_ID INT PRIMARY KEY IDENTITY(1,1),                         -- Identificador único da compra
    Cliente_ID INT,                                                  -- ID do cliente (chave estrangeira para a tabela Clientes)
    Produto NVARCHAR(100),                                           -- Nome do produto comprado
    Categoria NVARCHAR(50),                                          -- Categoria do produto
    Data_Compra DATE,                                                -- Data da compra
    Valor_Compra DECIMAL(10, 2),                                     -- Valor total da compra
    Quantidade_Parcelas INT,                                         -- Número de parcelas
    Data_Ultima_Compra DATE,                                         -- Data da última compra do cliente
    Produto_Indicado NVARCHAR(100),                                  -- Produto recomendado para o cliente
    Status_Indicacao NVARCHAR(50),                                   -- Status da indicação (Ex: Pendente, Aceito)
    FOREIGN KEY (Cliente_ID) REFERENCES Clientes(Cliente_ID)         -- Relacionamento com a tabela Clientes
);
