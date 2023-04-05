Previsão de preços de ações na Bovespa
Este é um código em Python que utiliza o Streamlit para criar uma interface simples que permite ao usuário inserir o símbolo da ação desejada da Bovespa e prever seus preços para um determinado número de dias no futuro. A previsão é feita utilizando um modelo de regressão linear simples.

Bibliotecas utilizadas
As s
streamlit run nome_do_arquivo.pyeguintes bibliotecas foram utilizadas neste projeto:

yfinance: biblioteca para coletar dados de ações da bolsa de valores
pandas: biblioteca para análise de dados
sklearn: biblioteca de aprendizado de máquina
streamlit: biblioteca para criação de interfaces de usuário
Funcionamento
O código é composto de três funções principais:

get_data: que coleta os dados da ação desejada da Bovespa
predict_price: que utiliza um modelo de regressão linear simples para prever os preços da ação para um determinado número de dias no futuro
show_data_and_prediction: que exibe os dados da ação e as previsões na interface do Streamlit
O usuário insere o símbolo da ação desejada na caixa de texto da interface e clica em "Prever preços" para que a previsão seja feita e exibida na interface.

Como executar
Para executar o código, é necessário ter o Python e as bibliotecas listadas acima instaladas em sua máquina. O código pode ser executado através do terminal, utilizando o seguinte comando:
streamlit run nome_do_arquivo.py
Substitua "nome_do_arquivo.py" pelo nome do arquivo que contém o código. Em seguida, o navegador abrirá uma nova guia com a interface criada pelo Streamlit.
