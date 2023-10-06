# Inteli - Instituto de Tecnologia e Liderança 

<p align="center">
<a href= "https://www.inteli.edu.br/"><img src="documentos/outros/inteli.png" alt="Inteli - Instituto de Tecnologia e Liderança" border="0"></a>
</p>

# mobil.ia

## The Lorean

## :student: Integrantes: 
- <a href="https://www.linkedin.com/in/ana-clara-madureira-marques/">Ana Clara Madureira Marques</a>
- <a href="https://www.linkedin.com/in/heitorprudente/">Heitor Elias Prudente</a>
- <a href="https://www.linkedin.com/in/henrique-cox-4644bb270/">Henrique Cox Cabral Oliveira de Moura</a> 
- <a href="https://www.linkedin.com/in/kaleb-carvalho/">Kaleb Isaias Souza de Carvalho</a> 
- <a href="https://www.linkedin.com/in/lucasdasilvabarbosa/">Lucas da Silva Barbosa</a>
- <a href="https://www.linkedin.com/in/raphaela-guiland-ferraz/">Raphaela Guiland Ferraz</a> 

## :teacher: Professores:
### Orientador(a) 
- <a href="https://www.linkedin.com/in/juliastateri/">Julia Stateri</a>
### Instrutores
- <a href="https://www.linkedin.com/in/nobrekoren/">Fernando Koren</a>
- <a href="https://www.linkedin.com/in/henrique-mohallem-paiva-6854b460/">Henrique Paiva</a> 
- <a href="https://www.linkedin.com/in/jefferson-o-silva/">Jefferson de Oliveira</a> 
- <a href="https://www.linkedin.com/in/rafael-jacomossi-6135b0a1/">Rafael Jacomossi</a>

## 📝 Descrição

O desafio enfrentado pela Mobly reside na necessidade de aprimorar o processo de abastecimento de seu estoque, visando a otimização de recursos e a garantia de que os produtos certos estejam disponíveis para atender à demanda dos clientes. Atualmente, a empresa enfrenta dificuldades em tomar decisões precisas de reposição de estoque, o que pode levar a problemas como falta de produtos ou excesso de estoque.

Nesse contexto, o objetivo principal deste projeto é desenvolver um modelo preditivo, denominado **mobil.ia**, altamente eficaz, projetado para fornecer suporte à equipe de abastecimento da Mobly. Esse modelo será capaz de prever com grande precisão a quantidade de itens que serão vendidos para cada SKU (Stock Keeping Unit) específico. Isso permitirá que a empresa tome decisões informadas e estratégicas sobre como e quando reabastecer seu estoque.

A solução proposta terá como base um algoritmo de aprendizado de máquina, que irá analisar os dados históricos de vendas, sazonalidade, tendências do mercado e outros fatores relevantes. Com essas informações, o modelo preditivo será capaz de gerar previsões confiáveis, contribuindo assim para a eficiência operacional da Mobly.

Em resumo, este projeto visa desenvolver uma ferramenta inovadora que aproveita o poder da análise de dados e da inteligência artificial para aprimorar o processo de abastecimento de estoque da Mobly. A precisão das previsões geradas pelo modelo preditivo ajudará a empresa a economizar recursos, evitar a falta de produtos e aprimorar a experiência do cliente, consolidando a posição da Mobly como líder no setor de comércio de móveis e decoração.

## 📁 Estrutura de pastas

Dentre os arquivos presentes na raiz do projeto, definem-se:

- <b>readme.md</b>: arquivo que serve como guia e explicação geral sobre o projeto (o mesmo que você está lendo agora).

- <b>documentos</b>: aqui estarão todos os documentos do projeto. Há também uma pasta denominada <b>outros</b> onde estão presentes documentos complementares.

- <b>notebooks</b>: todos os Jupyter Notebooks criados na plataforma Colab para desenvolvimento do projeto. Há também uma pasta denomina <b>outros</b> onde estão presentes Jupyter Notebooks complementares.

## 💻 Execução dos projetos
Todos os notebooks do projeto tem o resultado de execução das células visíveis por meio deste [link](https://drive.google.com/drive/folders/1TLwS3xIBtk6UO71Qfgw_Gom_ZZjzxwQx?usp=sharing)
> Alguns notebooks que estão presentes neste repositório GitHub possuem o resultado de execução das células vísiveis

Para que seja possível executar o modelo desenvolvido, que se encontra na pasta `notebooks` e é denominado como `Mobil_ia.ipynb`, é necessário seguir as instruções presentes no tópico **Anexos** da documentação do projeto. 
> A documentação do projeto se encontra na pasta `documentos` e o seu arquivo é denomidado como `documentacao.md`.

Para visualização do vídeo que explica detalhadamente sobre a utilização do modelo, basta clicar nesse [link](https://youtu.be/bLKM0p14TG4).

Abaixo serão listadas as bibliotecas utilizadas para o desenvolvimento do projeto, bem como as suas respectivas versões:
* `Pandas` - Versão 2.0.2
* `Plotly Express` - Versão 0.4.1
* `MissingNo` - Versão 0.5.2
* `Scipy` - Versão 1.11.2
* `Scikit-learn` - Versão 1.3.1
* `Numpy` - Versão 1.25.2
* `Joblib` - Versão 1.3.2

## 🗃 Histórico de lançamentos

* 0.5.0 - 04/09/2023
    * Desenvolvimento do modelo final;
    * Preenchimento da seção 4.5 da documentação, a qual aborda a Avaliação da solução desenvolvida;
    * Preenchimento da seção 5 da documentação, a qual aborda a Conclusão e as Recomenações do projeto. 
* 0.4.0 - 22/09/2023
    * Preenchimento da seção 4.4 da documentação, a qual aborda: a comparação dos novos modelos; a métrica de avaliação desses modelos; os modelos candidatos com tuning de hiperparâmetros; as métricas alcançadas; e o modelo escolhido;
    * Processo de modelagem utilizando `Árvore de Decisão` e `Regressão Linear`;
    * Aplicação da otimização de hiperparâmetros, utilizando `Grid Search` e `Random Search`, nos três modelos;
    * Otimização do `Random Forest Regressor`;
    * Preenchimento da coluna `winning_price` utilizando o método `leg-rows`;
    * Exclusão do período da black friday do dataframe.
* 0.3.0 - 04/09/2023
    * Preenchimento da seção 3 da documentação, a qual trata sobre a Metodologia do projeto;
    * Preenchimento da seção 4.3 da documentação, a qual trata sobre a Preparação dos dados e Modalgem;
    * Escolha das features;
    * Processo de modelagem utilizando `Random Forest Regressor` e `Prophet`;
    * Descrição das métricas gerais de avaliação dos modelos;
    * Escolha do modelo candidato e discussão sobre os seus resultados. 
* 0.2.0 - 25/08/2023
    * Exploração dos dados: identificação de colunas numéricas e categóricas e realização da estatística descritiva;
    * Pré Processamento: identificação e tratamento de _missing values_; identificação de _outliers_; codificação das variáveis categóricas e normalização das _features_;
    * Levantamento de hipóteses. 
* 0.1.0 - 11/08/2023
    * Documentação do entendimento do negócio: Matriz SWOT, Value Proposition Canvas, 5 Forças de Porter e Matriz de Riscos e Oportunidades;
    * Formulação da Política de Privacidade (LGPD);
    * Documentação da descrição da solução a ser desenvolvida;
    * Documentaçãoda experiência do usuário: Personas e Mapa da Jornada do Usuário. 

## 📋 Licença/License

<p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/2023M3T9-Inteli/grupo1/">mobil.ia</a> by <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://github.com/2023M3T9-Inteli/grupo1/">Inteli, <a href="https://www.linkedin.com/in/ana-clara-madureira-marques/">Ana Clara Madureira Marques</a>, <a href="https://www.linkedin.com/in/heitorprudente/">Heitor Elias Prudente</a>, <a href="https://www.linkedin.com/in/henrique-cox-4644bb270/">Henrique Cox Cabral Oliveira de Moura</a>, <a href="https://www.linkedin.com/in/kaleb-carvalho/">Kaleb Isaias Souza de Carvalho</a>, <a href="https://www.linkedin.com/in/lucasdasilvabarbosa/">Lucas da Silva Barbosa</a>, <a href="https://www.linkedin.com/in/raphaela-guiland-ferraz/">Raphaela Guiland Ferraz</a></a> is licensed under <a href="http://creativecommons.org/licenses/by-nc/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution-NonCommercial 4.0 International<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/nc.svg?ref=chooser-v1"></a></p>


## 🎓 Referências

Aqui estão as referências usadas no projeto:

1. Entrevista realizada com parceiros do projeto da empresa Mobly. Entrevista realizada em 4 ago 2023. Local da Entrevista: Instituto de Tecnologia e Liderança (Inteli). Entrevista concedida a: Turma 9.

2. Mannesoft Mais Lojas. Os desafios e oportunidades do mercado de móveis pós-pandemia. 24 nov. 2022. Disponível em: https://www.mannesoftmaislojas.com.br/blog/os-desafios-e-oportunidades-do-mercado-de-moveis-pos-pandemia. Acesso em: 4 ago. 2023.

3. Casarotto, Camila. 5 forças de Porter: entenda como elas influenciam sua estratégia. Rock Content, 11 dez. 2020. Disponível em: https://rockcontent.com/br/blog/5-forcas-de-porter/. Acesso em: 4 ago. 2023. Galvão, Regina. As 5 principais tendências do mercado de decoração em 2021. Exame, 11 fev. 2021. Disponível em: https://exame.com/revista-exame/ambientados-ao-novo-normal/. Acesso em: 5 ago. 2023.

4. Inteli - Instituto de Tecnologia e Liderança, 2023. Termo de Abertura de Projeto do Inteli - TAPI: Projeto Parceiro Empresa Mobly - 3° Módulo - Modelo Preditivo

5. Santos, Thiago G. Google Colab: o que é, tutorial de como usar e criar códigos. 20 jun. 2023. Disponível em: https://www.alura.com.br/artigos/google-colab-o-que-e-e-como-usar. Acesso em: 7 ago. 2023.

6. SHARDA, Ramesh; DELEN, Dursun; TURBAN, Efraim. Business Intelligence e Análise de Dados para Gestão do Negócio. [2019] [Bookman Editora].

7. Mobly. Disponível em: https://www.mobly.com.br/. Acesso em: 4 ago. 2023.

8. Affonso, Aline. Descubra o que é a metodologia CRISP DM. Voitto, 05 mar. 2021. Disponível em: https://www.voitto.com.br/blog/artigo/crisp-dm. Acesso em 29 ago. 2023.

9. M, Padhma. End-to-End Introduction to Evaluating Regression Models. Analytics Vidhya, 28 out. 2021 https://www.analyticsvidhya.com/blog/2021/10/evaluation-metric-for-regression-models/. Acesso em 5 set. 2023.

10. Obi Tayo, Benjamin. What Really is R2-Score in Linear Regression? Medium, 5 nov. 2021. Disponível em: https://benjaminobi.medium.com/what-really-is-r2-score-in-linear-regression-20cafdf5b87c. Acesso em 5 set. 2023.

11. Pessanha, Cínthia. Random Forest: como funciona um dos algoritmos mais populares de ML. Medium, 20 nov. 2019. Disponível em: https://medium.com/cinthiabpessanha/random-forest-como-funciona-um-dos-algoritmos-mais-populares-de-ml-cc1b8a58b3b4. Acesso em: 5 set. 2023.

12. Santo, J. E. Previsão de Séries Temporais com “Prophet”. Flai, 28 jun. 2022. Disponível em: https://www.flai.com.br/jonatas/previsao-de-series-temporais-com-prophet/. Acesso em 14 set. 2023.

13. Miura, Lucas. Modelos de Predição | Otimização de Hiperparâmetros em Python. Medium, 12 abr. 2020. Disponível em: https://medium.com/turing-talks/modelos-de-predi%C3%A7%C3%A3o-otimiza%C3%A7%C3%A3o-de-hiperpar%C3%A2metros-em-python-3436fc55016e#. Acesso em 18 set. 2023.

14. Remigio, Matheus. Árvores de Decisão - Decision Trees. Medium, 9 ago. 2020. Disponível em: https://medium.com/@msremigio/%C3%A1rvores-de-decis%C3%A3o-decision-trees-4cb6857671b3. Acesso em: 21 set. 2023.

15. S, Gabriel. Árvores de decisão e machine learning: uma combinação poderosa para análise preditiva. Linkedin, 24 abr. 2023. Disponível em: https://www.linkedin.com/pulse/%C3%A1rvores-de-decis%C3%A3o-e-machine-learning-uma-combina%C3%A7%C3%A3o-para-s-fraga/?originalSubdomain=pt. Acesso em: 21 set. 2023.

16. Lewis, Christopher. Optimize Hyperparameters with GridSearch. Medium, 7 mai. 2021. Disponível em: https://medium.com/analytics-vidhya/optimize-hyperparameters-with-gridsearch-d351b0fd339d. Acesso em: 21 set. 2023.

17. Damaceno, Laura. Regressão Linear?. Medium, 10 jun. 2020. Disponível em: https://medium.com/@lauradamaceno/regress%C3%A3o-linear-6a7f247c3e29. Acesso em: 13 set. 2023.

18. Tok&Stok. Disponível em: https://www.tokstok.com.br/. Acesso em: 4 ago. 2023.

19. MadeiraMadeira. Disponível em: https://www.madeiramadeira.com.br/. Acesso em: 4 ago. 2023.

20. G1 - Globo Economia. Empresa fatura R$ 150 mil ao mês produzindo móveis de papelão. 25 mai. 2013. Disponível em: https://g1.globo.com/economia/pme/noticia/2013/05/empresa-fatura-r-150-mil-ao-mes-produzindo-moveis-de-papelao.html. Acesso em: 4 ago. 2023.

21. Mobly. Keva Móveis. Disponível em: https://www.mobly.com.br/keva-moveis/. Acesso em: 5 ago. 2023.

22. PROTESTE. Lista de Reclamações Públicas. Disponível em: https://www.proteste.org.br/reclame/lista-de-reclamacoes-publicas/reclamacoes-publicas?referenceid=CPTBR01032811-52. Acesso em: 5 ago. 2023.

23. Reclame Aqui. Mobly. Disponível em: https://www.reclameaqui.com.br/empresa/mobly/. Acesso em: 5 ago. 2023.

24. Redação Olist. A expansão do e-commerce de Casa, Móveis e Decoração em 2023. 27 fev. 2023. Disponível em: https://olist.com/blog/pt/como-vender-mais/inteligencia-competitiva/e-commerce-de-casa-moveis-e-decoracao/. Acesso em: 5 ago. 2023.

25. Rondinelli, Júlia. O case da Mobly como uma história de constante crescimento e aprendizado. E-commerce Brasil, 15 jun. 2021. Disponível em: https://www.ecommercebrasil.com.br/noticias/o-case-da-mobly-como-uma-historia-de-constante-crescimento-e-aprendizado. Acesso em: 5 ago. 2023.

26. Silva, Ana Claudia. Com crescimento do mercado de casa e decoração, aumentam oportunidades para empreender online. 27 abr. 2023. Disponível em: https://www.segs.com.br/demais/343826-com-crescimento-do-mercado-de-casa-e-decoracao-aumentam-oportunidades-para-empreender-online. Acesso em: 5 ago. 2023.

27. Souza, Karina. Mobly: em tempos difíceis, empresa faz 'operação de guerra' e zera consumo de caixa. Exame, 12 nov. 2022. Disponível em: https://exame.com/exame-in/mobly-em-tempos-dificeis-empresa-faz-operacao-de-guerra-e-zera-consumo-de-caixa/. Acesso em: 5 ago. 2023.

28. Volpato, Bruno. Tudo sobre a análise SWOT: o que é, como fazer e template para baixar. Resultados Digitais, 23 ago. 2022. Disponível em: https://resultadosdigitais.com.br/marketing/analise-swot/. Acesso em: 7 ago. 2023.

29. scikit-learn. Scikit-learn: Machine Learning in Python. Versão 0.24.2. 2021. Disponível em: https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html. Acesso em: 20 set. 2023.

30. Faboci, Bruno. Otimizando Random Forest com GridSearch. LinkedIn. Disponível em: https://www.linkedin.com/pulse/otimizando-random-forest-com-gridsearch-bruno-faboci/?originalSubdomain=pt. Acesso em: 22 set 2023.

31. Tran, Khuyen. SHAP: Explain Any Machine Learning Model in Python. Towards Data Science. 24 set. 2021. Disponível em: https://towardsdatascience.com/shap-explain-any-machine-learning-model-in-python-24207127cad7. Acesso em: 03 out. 2023.
