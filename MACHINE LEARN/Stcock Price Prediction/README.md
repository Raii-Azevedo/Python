## Stock Price Prediction
                Este é um exemplo de código em Python que demonstra como realizar previsões de preços de ações usando um modelo de regressão linear. O código utiliza bibliotecas populares, como numpy, pandas e scikit-learn, para processar os dados e criar o modelo de previsão.

###Funcionalidades
    - O código inclui as seguintes funcionalidades:

    - Preparação dos Dados: Uma função chamada prepare_data é responsável por preparar os dados que serão usados para treinar e testar o modelo de previsão. Ela realiza as seguintes etapas:

    - Cria uma coluna chamada 'label' que contém os valores a serem previstos, mas deslocados para o futuro em um número especificado de períodos.

    - Converte a coluna de dados que será usada para previsão em um formato adequado para o modelo.

    - Escala os valores dos dados para que tenham uma média de 0 e desvio padrão de 1 (isso é útil para alguns modelos de machine learning).

    - Cria uma coluna chamada 'X_lately' que contém os últimos valores que serão usados para fazer previsões.

    - Divide os dados em conjuntos de treinamento e teste, onde o conjunto de teste terá uma proporção específica dos dados.

#####Treinamento do Modelo: 
    - O código utiliza um modelo de regressão linear, um algoritmo de aprendizado de máquina, para treinar o modelo. O modelo é alimentado com os dados de treinamento para aprender a fazer previsões com base nos dados históricos.

#####Avaliação do Modelo: 
    - Após o treinamento, o código avalia o desempenho do modelo calculando sua pontuação nos dados de teste. A pontuação indica o quão bem o modelo está se saindo na previsão dos dados de teste.

#####Previsões Futuras:
    - O modelo treinado é usado para fazer previsões para um número especificado de períodos no futuro. Essas previsões são armazenadas em uma estrutura de dados.

#####Utilização
    - Para usar este código, siga as seguintes etapas:

    - Certifique-se de ter as bibliotecas numpy, pandas e scikit-learn instaladas em seu ambiente Python.

- Baixe um conjunto de dados históricos de preços de ações em formato CSV. Certifique-se de que o arquivo contenha as colunas 'Date' e 'Close' (ou ajuste o código de acordo com as colunas do seu arquivo).

- Substitua o caminho do arquivo CSV no código pelo caminho do seu próprio arquivo.

- Configure os parâmetros de previsão, como a coluna a ser usada para previsão, o número de períodos futuros a serem previstos e a proporção de dados para o conjunto de teste.

- Execute o código. Ele carregará os dados, treinará o modelo, avaliará seu desempenho e fará previsões futuras.

- Este código é um exemplo simples de como realizar previsões de preços de ações com um modelo de regressão linear. Você pode personalizá-lo e estendê-lo para atender às suas próprias necessidades de previsão de séries temporais.