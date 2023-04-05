!pip install yfinance
!pip install pandas
!pip install sklearn
!pip install streamlit

import yfinance as yf
import pandas as pd
from sklearn.linear_model import LinearRegression
import streamlit as st

# Função para capturar dados da Bovespa
def get_data(ticker):
    """
    Função para capturar dados da ação desejada na Bovespa.

    Parâmetros:
        ticker (str): símbolo da ação desejada na Bovespa.
    
    Retorna:
        data (pd.DataFrame): DataFrame com os dados da ação desejada na Bovespa.
    """
    # Captura os dados da ação desejada
    data = yf.download(ticker, start="2010-01-01", end="2023-01-01")
    
    # Verifica se o ticker foi encontrado na base de dados do Yahoo Finance
    if data.empty:
        raise ValueError(f"Ticker '{ticker}' não encontrado na base de dados do Yahoo Finance.")
    
    # Seleciona apenas as colunas Close e Adj Close
    data = data[["Close", "Adj Close"]]
    
    # Renomeia as colunas para um nome mais claro
    data.rename(columns={"Close": "Close Price", "Adj Close": "Adj Close Price"}, inplace=True)
    
    return data

# Função para fazer a previsão de preços de ações
def predict_price(data, days_ahead):
    """
    Função para fazer a previsão de preços de ações.

    Parâmetros:
        data (pd.DataFrame): DataFrame com os dados da ação desejada na Bovespa.
        days_ahead (int): número de dias para fazer a previsão de preços de ações.
    
    Retorna:
        prediction (np.ndarray): array com as previsões dos preços de ações para os dias futuros desejados.
    """
    # Cria uma coluna com o número de dias desde o primeiro dia de registro
    data["Days Since"] = range(len(data))
    
    # Seleciona as colunas Close Price e Days Since como variáveis independentes
    X = data[["Days Since"]].values
    y = data[["Close Price"]].values
    
    # Cria o modelo de regressão linear
    model = LinearRegression()
    model.fit(X, y)
    
    # Cria uma coluna com a previsão dos preços de ações
    data["Prediction"] = model.predict(X)
    
    # Cria uma coluna com a quantidade de dias desde o último dia de registro
    data["Days Ahead"] = range(len(data), len(data) + days_ahead)
    
    # Preve os preços de ações para os dias futuros desejados
    prediction = model.predict(data[["Days Ahead"]].values)
    
    return prediction

# Função que exibe os dados e previsões na interface do Streamlit
def show_data_and_prediction(data, prediction):
   
    Função para exibir os dados e previsões na interface do Streamlit.

    Parâmetros:
        data (pd.DataFrame): DataFrame com os dados da ação desejada na Bovespa.
       
# Cria uma figura com o gráfico da previsão
fig = px.line(data, x=data.index, y=["Close Price", "Prediction"])

# Adiciona a legenda ao gráfico
fig.update_layout(legend=dict(
    orientation="h",
    yanchor="bottom",
    y=1.02,
    xanchor="right",
    x=1
))

# Exibe o gráfico na interface do Streamlit
st.plotly_chart(fig)

# Entrada do usuário para o símbolo da ação
ticker = st.text_input("Insira o símbolo da ação:", "^BVSP")

# Entrada do usuário para a quantidade de dias à frente para prever
days_ahead = st.number_input("Quantos dias à frente deseja prever?", min_value=1, max_value=365, value=30)

# Captura os dados da Bovespa para a ação desejada
data = get_data(ticker)

# Faz a previsão dos preços de ações para os dias à frente desejados
prediction = predict_price(data, days_ahead)

# Exibe os dados e previsões na interface do Streamlit
show_data_and_prediction(data, prediction)

# Exibe o gráfico da previsão na interface do Streamlit
show_prediction_plot(data)
