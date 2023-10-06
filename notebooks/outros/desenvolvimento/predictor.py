# Importa bibliotecas necessárias
import pandas as pd
import numpy as np

class Predictor:
  
  # Função que gera a previsão de vendas a partir de uma data
  def generate_forecast(self, date, model):
    # Carrega o conjunto de dados da Mobly a partir do caminho especificado
    df = self.load_df("../documentos/outros/base_de_dados/mobly_data_official.csv")
    
    # Converte a data de entrada para o formato datetime
    date = pd.to_datetime(date)
    
    # Gera a semana correspondente à data usando o conjunto de dados carregado
    week = self.generate_week(date, df)
    
    # Cria um novo dataframe para as previsões com base no conjunto de dados e na data
    df_pred = self.create_pred_dataframe(df, date, week)
    
    # Realiza a previsão usando o modelo especificado
    prev = self.forecast(df_pred, model)
    
    # Organiza a tabela de previsões e a data e retorna o resultado
    return self.organize_table(prev, date)
  
  
  # Função que importa os dados da Mobly
  def load_df(self, path):
    # Lê um arquivo CSV a partir do caminho especificado e carrega-o em um DataFrame (df)
    df = pd.read_csv(path, sep=",")
    
    # Agrupa as semanas no DataFrame usando uma função chamada 'group_weeks'
    df_grouped = self.group_weeks(df)
    
    # Retorna o DataFrame resultante após a leitura e o agrupamento
    return df_grouped
  

  # Função que agrupa as semanas
  def group_weeks(self, df):
    # Cria uma nova coluna "week" no DataFrame
    df['week'] = pd.to_datetime(df[['year', 'month', 'day']], errors='coerce').dt.strftime('%U')

    # Converte o resultado para numérico
    df['week'] = pd.to_numeric(df['week'], errors='coerce')

    # Calcula o deslocamento necessário para ajustar as semanas desde janeiro de 2020
    start_date = pd.Timestamp('2020-01-01')
    df['week'] = ((pd.to_datetime(df[['year', 'month', 'day']]) - start_date).dt.days // 7) + 1

    # Retorna o DataFrame com a coluna 'week' atualizada
    return df
  

  # Função que preenche colunas históricas com valores médios arredondados
  def fill_in_historical_columns(self, df, sku, columns):
    # Inicializa um dicionário vazio para armazenar os valores históricos calculados
    historical_values = {}

    # Itera sobre as colunas especificadas para calcular os valores médios arredondados
    for column in columns:
        # Calcula a média arredondada da coluna 'column' para o SKU 'sku'
        historical_value = round(df[df['sku'] == sku][column].mean())

        # Armazena o valor médio arredondado no dicionário 'historical_values' com a chave 'column'
        historical_values[column] = historical_value

    # Retorna o dicionário com os valores médios arredondados
    return historical_values
  

  # Função que cria uma nova linha de dados no DataFrame com base nos parâmetros
  def create_new_line(self, user_date, sku, week, df):    
    # Inicializa uma nova linha com valores padrões para "weekday_name" e "sku"
    new_line = {
        'weekday_name': 0,
        'sku': sku,
    }
    
    # Define a ordem das colunas a serem preenchidas na primeira etapa
    first_order = ['weekday_name', 'sku', 'unit_price', 'shipment_type', 'anchor_category', 'product_department', 'product_category', 'origin_country', 'process_costing', 'sku_color', 'price_status', 'winning_price']
    
    # Preenche as colunas da primeira ordem com valores históricos e atualiza a nova linha
    historical_values = self.fill_in_historical_columns(df, sku, first_order)
    new_line.update(historical_values)
    
    # Preenche a coluna "items_sold" com valores NaN
    new_line['items_sold'] = np.nan
    
    # Preenche as colunas "avg_website_visits_last_week" e "stock_qty" com valores históricos e atualiza a nova linha
    avg_stock_values = self.fill_in_historical_columns(df, sku, ['avg_website_visits_last_week', 'stock_qty'])
    new_line.update(avg_stock_values)
    
    # Obtém informações de data (mês, dia e ano) do objeto "user_date" e atualiza a nova linha
    new_line['month'] = user_date.month
    new_line['day']   = user_date.day
    new_line['year']  = user_date.year
    
    # Preenche as colunas "value_dollar" e "rate_employability" com valores históricos e atualiza a nova linha
    dollar_employability_values = self.fill_in_historical_columns(df, sku, ['value_dollar', 'rate_employability'])
    new_line.update(dollar_employability_values)
    
    # Define 'week' com o valor da semana fornecido como parâmetro
    new_line['week'] = week
    
    # Retorna a nova linha criada
    return new_line
  

  # Função que cria o DataFrame de previsão
  def create_pred_dataframe(self, df, user_date, week):
    # Cria um novo DataFrame vazio com as mesmas colunas do DataFrame original "df"
    df_pred = pd.DataFrame(columns=df.columns)

    # Obtém a lista de SKUs únicos presentes no DataFrame original "df"
    unique_skus = df['sku'].unique()

    # Inicializa uma lista para armazenar os novos dados que serão adicionados ao DataFrame de previsão
    new_data = []
    
    # Itera sobre os SKUs únicos e cria uma nova linha de dados para cada um deles
    for sku in unique_skus:
        new_line = self.create_new_line(user_date, sku, week, df)
        new_data.append(new_line)
    
    # Cria um novo DataFrame "df_pred" a partir dos novos dados gerados
    df_pred = pd.DataFrame(new_data)

    # Retorna o DataFrame de previsão "df_pred"
    return df_pred
  

  # Função que determina a semana correspondente a uma data de acordo com o DataFrame
  def generate_week(self, date, df):
    # Cria a coluna "date" no formato "YYYY-MM-DD"
    df['date'] = pd.to_datetime(df[['year', 'month', 'day']])
    
    try:
      week = ((date - df['date'].min()).days // 7) + 1
      
      # Verifica se a data fornecida pelo usuário está dentro do intervalo de datas do DataFrame original "df"
      if week > 0:
          print(f"A data {date.strftime('%Y-%m-%d')} corresponde à semana {week}.")
          return week
      else:
          print("A data fornecida está antes do início do registro de vendas.")
          return 0
          
    except ValueError:
      print("Data inserida em formato inválido. Use o formato 'YYYY-MM-DD'.")


  # Função que realiza previsões de vendas utilizando um modelo de machine learning
  def forecast(self, df_pred, model):
    # Faz previsões para a coluna "items_sold" no DataFrame "df_pred" usando o modelo fornecido
    forecasts_items_sold = model.predict(df_pred.drop(['items_sold'], axis=1))

    # Preenche a coluna "items_sold" do DataFrame "df_pred" com as previsões
    df_pred['items_sold'] = forecasts_items_sold

    # Retorna o DataFrame atualizado com as previsões de vendas
    return df_pred


  # Função que organiza e formata a tabela de previsões de vendas
  def organize_table(self, df_pred, user_date):
    # Calcula a data de início da semana com base na data fornecida pelo usuário "user_date" e atribui à coluna "data_inicio"
    df_pred['data_inicio'] = user_date - pd.DateOffset(days=user_date.weekday())

    # Calcula a data de final da semana somando 6 dias à data de início e atribui à coluna "data_final"
    df_pred['data_final'] = df_pred['data_inicio'] + pd.DateOffset(days=6)

    # Arredonda os valores da coluna "items_sold" para inteiros, pois representam vendas
    df_pred['items_sold'] = df_pred['items_sold'].astype(int)

    # Seleciona apenas as colunas relevantes no DataFrame "df_pred" para a tabela final
    df_pred = df_pred[['sku', 'data_inicio', 'data_final', 'week', 'items_sold']]

    # Retorna o DataFrame formatado com as informações de vendas previstas
    return df_pred


  # Função que exporta o DataFrame "df_pred" para um arquivo CSV
  def to_csv(self, name, df_pred):
    df_pred.to_csv(f'../notebooks/outros/tabelas_previsão/{name}.csv', index=False)