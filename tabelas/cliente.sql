CREATE OR REPLACE TABLE Clientes (
    Cliente_ID INT PRIMARY KEY IDENTITY(1,1),        -- Identificador único do cliente
    Nome NVARCHAR(100),                              -- Nome do cliente
    CPF CHAR(11) UNIQUE,                             -- CPF do cliente
    Segmento NVARCHAR(50),                           -- Segmento do cliente
    Interesses NVARCHAR(255),                        -- Interesses do cliente
    Gastos_Mensais DECIMAL(10, 2),                   -- Gastos mensais do cliente
    Salario DECIMAL(10, 2),                          -- Salário do cliente
    Tipo_Cartao_Credito NVARCHAR(50),                -- Tipo de cartão de crédito
    Gasto_Mensal_Cartao DECIMAL(10, 2),              -- Gasto mensal com o cartão de crédito
    Viaja_Frequentemente BIT,                        -- Indica se viaja frequentemente (0 = Não, 1 = Sim)
    Profissao NVARCHAR(100),                         -- Profissão do cliente
    Renda_Mensal DECIMAL(10, 2),                     -- Renda mensal do cliente
    Dependentes INT,                                 -- Número de dependentes
    Genero CHAR(1),                                  -- Gênero (M, F, etc.)
    Data_Nascimento DATE,                            -- Data de nascimento do cliente
    Idade INT                                        -- Idade calculada do cliente
);