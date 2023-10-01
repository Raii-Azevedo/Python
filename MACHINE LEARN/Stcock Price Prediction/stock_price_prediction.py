# Importação das bibliotecas necessárias
import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Função para preparar os dados de treinamento e teste
def prepare_data(df, forecast_col, forecast_out, test_size):
    # Cria uma coluna 'label' com os valores deslocados para cima (shifted) em 'forecast_out' períodos
    label = df[forecast_col].shift(-forecast_out)
    # Converte a coluna de recursos 'forecast_col' em um array numpy
    X = np.array(df[[forecast_col]])
    # Escala os valores dos recursos (média 0, desvio padrão 1)
    X = preprocessing.scale(X)
    # Cria uma coluna 'X_lately' com os 'forecast_out' últimos valores que serão usados para previsão
    X_lately = X[-forecast_out:]
    # Remove as últimas 'forecast_out' linhas de X
    X = X[:-forecast_out]
    # Remove as linhas com valores NaN em 'label'
    label.dropna(inplace=True)
    # Converte 'label' em um array numpy
    y = np.array(label)
    # Divide os dados em conjuntos de treinamento e teste
    X_train, X_test, Y_train, Y_test = train_test_split(
        X, y, test_size=test_size, random_state=0)
    # Retorna os conjuntos de dados e X_lately em uma lista
    response = [X_train, X_test, Y_train, Y_test, X_lately]
    return response

# Função principal
def main():
    # Carrega os dados de um arquivo CSV para um DataFrame
    df = pd.read_csv("C:/Users/Raiis/OneDrive/Área de Trabalho/Python/MACHINE LEARN/prices.csv")
    
    # Define os parâmetros para a previsão
    forecast_col = 'Close'  # Coluna que será usada como recurso para a previsão
    forecast_out = 5  # Número de períodos à frente para fazer a previsão
    test_size = 0.2  # Proporção dos dados a serem usados como conjunto de teste
    
    # Prepara os dados de treinamento e teste usando a função prepare_data
    X_train, X_test, Y_train, Y_test, X_lately = prepare_data(
        df, forecast_col, forecast_out, test_size)
    
    # Inicializa um modelo de regressão linear
    learner = LinearRegression()
    # Treina o modelo com os dados de treinamento
    learner.fit(X_train, Y_train)
    # Calcula a pontuação do modelo nos dados de teste
    score = learner.score(X_test, Y_test)
    # Realiza a previsão com base nos dados em X_lately
    forecast = learner.predict(X_lately)
    
    # Cria um dicionário com os resultados
    response = {}
    response['test_score'] = score  # Pontuação do teste
    response['forecast_set'] = forecast  # Conjunto de previsão
    
    # Imprime os resultados
    print(response)

if __name__ == '__main__':
    main()  
