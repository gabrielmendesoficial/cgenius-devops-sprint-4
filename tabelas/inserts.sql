-- INSERE OS CLIENTES A TABELA.
INSERT INTO Clientes (Nome, CPF, Segmento, Interesses, Gastos_Mensais, Salario, Tipo_Cartao_Credito, Gasto_Mensal_Cartao, Viaja_Frequentemente, Profissao, Renda_Mensal, Dependentes, Genero, Data_Nascimento, Idade)
VALUES 
('João Silva', '12345678901', 'Varejo', 'Tecnologia', 500.00, 3000.00, 'Visa', 200.00, 1, 'Engenheiro', 4000.00, 2, 'M', '1990-05-15', DATEDIFF(YEAR, '1990-05-15', GETDATE())),
('Maria Oliveira', '23456789012', 'Serviços', 'Moda', 800.00, 5000.00, 'Mastercard', 400.00, 0, 'Designer', 5500.00, 1, 'F', '1985-07-22', DATEDIFF(YEAR, '1985-07-22', GETDATE())),
('Carlos Pereira', '34567890123', 'Varejo', 'Esportes', 1200.00, 4500.00, 'American Express', 600.00, 1, 'Administrador', 4800.00, 3, 'M', '1992-11-10', DATEDIFF(YEAR, '1992-11-10', GETDATE())),
('Ana Costa', '45678901234', 'Varejo', 'Viagens', 700.00, 3200.00, 'Visa', 350.00, 1, 'Professora', 3700.00, 0, 'F', '1995-03-05', DATEDIFF(YEAR, '1995-03-05', GETDATE()));

-- INSERE AS COMPRAS FEITAS PELO CLIENTE, INCLUINDO O SEU RELACIONAMENTO.
INSERT INTO Compras (Cliente_ID, Produto, Categoria, Data_Compra, Valor_Compra, Quantidade_Parcelas, Data_Ultima_Compra, Produto_Indicado, Status_Indicacao)
VALUES 
(1, 'Notebook', 'Eletrônicos', GETDATE(), 2500.00, 5, GETDATE(), 'Smartphone', 'Pendente'),
(1, 'Camiseta', 'Vestuário', GETDATE(), 100.00, 1, GETDATE(), 'Calça Jeans', 'Aceito'),
(2, 'Televisor', 'Eletrônicos', GETDATE(), 1500.00, 12, GETDATE(), 'Soundbar', 'Pendente'),
(3, 'Tênis', 'Esportes', GETDATE(), 300.00, 3, GETDATE(), 'Bermuda', 'Aceito'),
(4, 'Mala de Viagem', 'Acessórios', GETDATE(), 400.00, 2, GETDATE(), 'Necessaire', 'Pendente');
