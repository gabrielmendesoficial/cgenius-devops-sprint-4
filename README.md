# Projeto de Assistente IA para Call Centers
![Logo](https://cdn.discordapp.com/attachments/1292610820416475189/1300187723734192220/image-removebg-preview.png?ex=671fedad&is=671e9c2d&hm=0629e4e4ef73f71a6f03f8335fd4489a29f8b6bb14cc8bef3be01211271de0a9&)

## Foco do Projeto
O objetivo deste projeto é desenvolver uma inteligência artificial (IA) que auxilia operadores de call center na geração de textos a partir de informações dos clientes. Isso permite que os operadores ofereçam um atendimento mais eficiente e personalizado.

## Problema a Resolver
Os operadores de call center frequentemente enfrentam desafios relacionados ao tempo de resposta e à personalização do atendimento. A falta de informações consolidadas sobre os clientes pode levar a interações menos satisfatórias e à perda de oportunidades de venda. A nossa solução visa otimizar esse processo.

## Consulte a versão sem o connector do database

 - [Link para o repositorio de IA no Github](https://github.com/gabrielmendesoficial/cgeniusIA)

## Solução
A IA utiliza informações dos clientes, permitindo a geração automática de textos que ajudam os operadores a se comunicarem de forma mais eficiente. Por exemplo, a IA pode sugerir produtos com base nos interesses e histórico de compras do cliente, facilitando o processo de venda e aumentando a satisfação do cliente.

## Custos de Operação da IA
Os custos de operação da IA incluem:

- **Infraestrutura de Servidor:** Custo mensal para manter servidores que hospedam o modelo de IA.
- **Treinamento do Modelo:** Investimentos em recursos computacionais para treinar a IA.
- **Manutenção e Atualizações:** Custos associados à atualização do modelo e manutenção contínua.

## Estrutura dos Dados
Os dados contém as seguintes colunas, cada uma com suas respectivas funções:

| Coluna                   | Descrição |
|--------------------------|-----------|
| ID                       | Identificador único do cliente |
| Nome                     | Nome completo do cliente |
| CPF                      | Cadastro de Pessoa Física |
| Cliente_ID               | Identificador único do cliente na base de dados |
| Produto                  | Produto adquirido pelo cliente |
| Categoria                | Categoria do produto |
| Data_Compra              | Data da compra realizada |
| Valor_Compra             | Valor total da compra |
| Quantidade_Parcelas      | Número de parcelas do pagamento |
| Data_Última_Compra       | Data da última compra realizada pelo cliente |
| Segmento                 | Segmento de mercado do cliente |
| Produto_Indicado         | Produto sugerido pela IA |
| Status_Indicação         | Status da indicação do produto |
| Interesses               | Interesses do cliente (ex: tecnologia, esportes) |
| Gastos_Mensais           | Valor médio gasto pelo cliente mensalmente |
| Salario                  | Salário do cliente |
| Tipo_Cartao_Credito     | Tipo do cartão de crédito do cliente |
| Gasto_Mensal_Cartao     | Gasto médio mensal no cartão de crédito |
| Viaja_Frequentemente     | Indica se o cliente viaja com frequência |
| Profissao                | Profissão do cliente |
| Renda_Mensal             | Renda mensal do cliente |
| Dependentes              | Número de dependentes do cliente |
| Gênero                   | Gênero do cliente |
| Data_Nascimento          | Data de nascimento do cliente |
| Idade                    | Idade do cliente |

## O que o código faz

1. Processamento de Dados dos Clientes: O código lê as informações detalhadas sobre os clientes, como histórico de compras, interesses, gastos mensais, renda, profissão, e outros atributos pessoais. Esses dados são organizados em um DataFrame e usados como base para gerar abordagens personalizadas.

2. Geração de Textos Personalizados: A IA analisa as informações fornecidas e, com base em parâmetros como interesses, faixa de idade, segmento de mercado, entre outros, cria abordagens comerciais que ajudam os operadores de call center a interagir de forma mais direcionada e relevante com cada cliente. Por exemplo, o texto sugerido pode destacar produtos que estão alinhados com os interesses do cliente ou oferecer soluções financeiras baseadas em seu perfil econômico.

3. Sugestão de Produtos: Com base no histórico de compras e nos interesses do cliente, o código sugere automaticamente produtos que podem ser indicados durante o atendimento. Isso permite que os operadores ofereçam recomendações mais assertivas, maximizando as chances de conversão em vendas.

4. Exportação e Visualização de Dados: O código também exporta os dados processados para datasets atualizados, facilitando sua visualização e análise futura. Além disso, ele gera gráficos e relatórios visuais, como histogramas dos interesses dos clientes ou gráficos de barras que mostram a distribuição de idade ou renda.

5. Gestão de Indicadores de Desempenho: O código armazena o status de cada indicação feita pela IA, permitindo acompanhar a performance das recomendações e ajustar as estratégias de abordagem conforme necessário. Isso garante um ciclo contínuo de aprendizado e melhoria.

6. Atualizações Dinâmicas: A cada interação com novos clientes, o código é capaz de atualizar dinamicamente as abordagens e sugestões de produtos com base em novos dados adquiridos, mantendo o sistema sempre alinhado com as necessidades e preferências mais atuais dos clientes.

## Como Iniciar o Código
- Para iniciar o sistema Elite Sales, basta ir no botão em verde "Code" e logo em sequencia no botão "+" do Codespace.
![Parte1](https://i.imgur.com/BZJbEtI.png)
- Depois de clicar no botão de "+" no Codespace ele vai abrir uma nova Guia e deve esperar o termino do seu carregamento.
![Parte2](https://i.imgur.com/RRDUyi9.png)
- No canto inferior direito, você terá a possibilidade de instalar o Python apos clicar no "app_database.py".
![Parte3](https://i.imgur.com/tydqkXD.png)
- A mensagem de instalação não seja enviada a você? Basta entrar na loja de extensões e instalar ela. 
![Parte4](https://i.imgur.com/0RjS5ji.png)
- Depois de instalar o Python basta utilizar o comando "pip install -r requirements.txt" no terminal e os seguintes comandos na ordem:

1. curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
2. curl https://packages.microsoft.com/config/ubuntu/$(lsb_release -rs)/prod.list > /etc/apt/sources.list.d/mssql-release.list
3. sudo apt-get update
4. sudo ACCEPT_EULA=Y apt-get install -y msodbcsql17 unixodbc-dev

![Parte5](https://i.imgur.com/5Hwb4CY.png)
- Instalando todas as dependencias do projeto, voce deve dar continuidade com o comando "streamlit run app_database.py"
![Parte6](https://i.imgur.com/wB9hUQQ.png)


## Conclusão
Este projeto visa revolucionar a forma como os operadores de call center interagem com os clientes, utilizando tecnologia de ponta para melhorar a eficiência e a qualidade do atendimento.
